const videoUpload = document.getElementById('video-upload');
const videoPreview = document.getElementById('video-preview');
const addCaptionsButton = document.getElementById('add-captions');

videoUpload.addEventListener('change', () => {
    const file = videoUpload.files[0];
    const url = URL.createObjectURL(file);
    videoPreview.src = url;
});

addCaptionsButton.addEventListener('click', () => {
    const file = videoUpload.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.output_video) {
            videoPreview.src = `/uploads/${data.output_video}`;
        }
    })
    .catch(error => console.error('Error:', error));
});
