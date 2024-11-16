from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import shutil
from dotenv import load_dotenv
import tempfile
import base64
from groq import Groq
import fitz
import uuid
from JobAPI import get_job_ids, get_job_details

load_dotenv() 

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
groq_client = Groq(api_key=GROQ_API_KEY)

UPLOAD_FOLDER = os.path.join(tempfile.gettempdir(), 'cv_uploads')
TEMP_FOLDER = os.path.join(tempfile.gettempdir(), 'cv_temp')
for folder in [UPLOAD_FOLDER, TEMP_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def pdf_to_images(pdf_path):
    """Convert PDF to list of base64 encoded images"""
    doc = fitz.Document(pdf_path)
    images = []
    for page in doc:
        pix = page.get_pixmap()  # Use default scaling factor for original quality
        img_data = pix.tobytes()
        img_base64 = base64.b64encode(img_data).decode()
        images.append(img_base64)
    return images

def analyze_cv_with_groq(images):
    """Analyze CV images using Groq's vision model"""
    messages = []
    for idx, img_base64 in enumerate(images):
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": "Please analyze this CV page and provide a professional summary. "},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_base64}",
                    },
                },
            ],
            
        })

    chat_completion = groq_client.chat.completions.create(
        messages=messages,
        model="llama-3.2-90b-vision-preview",
        temperature = 0.1
        #response_format={"type": "json_object"},
    )
    
    return chat_completion.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv_page():
    upload_id = session.get('upload_id')
    summary = session.get('cv_summary')

    if not upload_id or not summary:
        return redirect(url_for('index'))
    
    image_path = os.path.join(TEMP_FOLDER, f"{upload_id}.txt")
    try:
        with open(image_path, 'r') as f:
            cv_image = f.read()
    except:
        cv_image = None
        
    return render_template('cv.html', cv_image=cv_image, summary=summary)

@app.route('/upload-cv', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and file.filename.endswith('.pdf'):
        try:
            upload_id = str(uuid.uuid4())
            
            temp_path = os.path.join(UPLOAD_FOLDER, f"{upload_id}.pdf")
            file.save(temp_path)
            
            images = pdf_to_images(temp_path)
            
            summary = analyze_cv_with_groq(images)
            
            image_path = os.path.join(TEMP_FOLDER, f"{upload_id}.txt")
            with open(image_path, 'w') as f:
                f.write(images[0])
            
            session['upload_id'] = upload_id
            session['cv_summary'] = summary
            
            return jsonify({'status': 'success', 'redirect': '/cv'})
            
        except Exception as e:
            print(f"Error processing CV: {str(e)}")
            return jsonify({'error': str(e)}), 500
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/cleanup')
def cleanup():
    upload_id = session.get('upload_id')
    if upload_id:
        image_path = os.path.join(TEMP_FOLDER, f"{upload_id}.txt")
        if os.path.exists(image_path):
            os.remove(image_path)
    return '', 204

@app.route('/job-listings')
def job_listings():
    return render_template('listing.html')

@app.route('/api/job-listings')
def api_job_listings():
    job_ids = get_job_ids()
    limited_job_ids = job_ids[:2] 
    job_details = [get_job_details(job_id) for job_id in limited_job_ids]

    return jsonify(job_details)

if __name__ == '__main__':
    app.run(debug=True)


