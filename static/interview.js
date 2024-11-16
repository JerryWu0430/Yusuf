const button = document.getElementById('interviewButton');
const statusText = document.querySelector('.status-text');
let isRecording = false;

button.addEventListener('click', () => {
    isRecording = !isRecording;
    if (isRecording) {
        button.innerHTML = '<i class="fas fa-microphone-slash"></i> End Interview';
        button.classList.add('recording');
        statusText.textContent = 'Alice is listening...';
    } else {
        button.innerHTML = '<i class="fas fa-microphone"></i> Start Interview';
        button.classList.remove('recording');
        statusText.textContent = 'Press the button to start your interview with Alice';
    }
});