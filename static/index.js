document.addEventListener('DOMContentLoaded', function() {
    const uploadButton = document.querySelector('.upload-button');
    const fileInput = document.getElementById('cv-input');
    const uploadArea = document.querySelector('.upload-area');

  
    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;

       
        const allowedTypes = ['.pdf', '.doc', '.docx'];
        const fileExtension = file.name.toLowerCase().substring(file.name.lastIndexOf('.'));
        if (!allowedTypes.includes(fileExtension)) {
            alert('Please upload a PDF, DOC, or DOCX file');
            return;
        }

     
        const formData = new FormData();
        formData.append('cv', file);

        try {
          
            uploadButton.textContent = 'Uploading...';
            uploadButton.disabled = true;

            
            const response = await fetch('/upload-cv', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const data = await response.json();
                uploadButton.textContent = 'Upload Successful!';
                uploadButton.style.backgroundColor = '#4CAF50';
                uploadButton.style.color = 'white';
                
                setTimeout(() => {
                    window.location.href = '/results'; 
                }, 1500);
            } else {
                throw new Error('Upload failed');
            }
        } catch (error) {
            console.error('Error:', error);
            uploadButton.textContent = 'Upload Failed';
            uploadButton.style.backgroundColor = '#f44336';
            uploadButton.style.color = 'white';
            
            
            setTimeout(() => {
                uploadButton.textContent = 'Upload CV';
                uploadButton.style.backgroundColor = '';
                uploadButton.style.color = '';
                uploadButton.disabled = false;
            }, 2000);
        }
    });


    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

 
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.style.borderColor = '#2196F3';
            uploadArea.style.backgroundColor = '#E3F2FD';
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.style.borderColor = '#ddd';
            uploadArea.style.backgroundColor = '';
        });
    });

   
    uploadArea.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const file = dt.files[0];
        fileInput.files = dt.files;
        fileInput.dispatchEvent(new Event('change'));
    });
});