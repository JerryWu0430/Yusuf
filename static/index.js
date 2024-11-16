document.addEventListener('DOMContentLoaded', function() {
    const uploadButton = document.querySelector('.upload-button');
    const fileInput = document.getElementById('cv-input');

    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        if (!file.name.endsWith('.pdf')) {
            alert('Please upload a PDF file');
            return;
        }

        const formData = new FormData();
        formData.append('pdf', file);

        uploadButton.textContent = 'Processing...';
        uploadButton.disabled = true;

        try {
            const response = await fetch('/upload-cv', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            console.log('Response:', data);

            if (response.ok && data.status === 'success') {
                uploadButton.textContent = 'Success!';
                uploadButton.style.backgroundColor = '#4CAF50';
                uploadButton.style.color = 'white';
                
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 1000);
            } else {
                throw new Error(data.error || 'Upload failed');
            }
        } catch (error) {
            console.error('Error:', error);
            uploadButton.textContent = 'Upload Failed';
            uploadButton.style.backgroundColor = '#f44336';
            uploadButton.style.color = 'white';
            alert('Error uploading file: ' + error.message);
            
            setTimeout(() => {
                uploadButton.textContent = 'Upload CV';
                uploadButton.style.backgroundColor = '';
                uploadButton.style.color = '';
                uploadButton.disabled = false;
            }, 2000);
        }
    });
});