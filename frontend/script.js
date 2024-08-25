document.getElementById('uploadButton').addEventListener('click', function() {
    var fileInput = document.getElementById('fileInput');
    var formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const videoPreviewDiv = document.getElementById('videoPreview');
        const summaryDiv = document.getElementById('summary');
        const previewElement = document.getElementById('videoPreviewElement');
        const summaryTextElement = document.getElementById('summaryText');
        const statusDiv = document.getElementById('status');

        statusDiv.classList.add('hidden');

        if (data.video_path) {
            videoPreviewDiv.classList.remove('hidden');
            previewElement.src = `/uploads/${data.video_path}`;
        }

        if (data.transcript_path) {
            summaryDiv.classList.remove('hidden');
            fetch(`/uploads/${data.transcript_path}`)
                .then(response => response.text())
                .then(text => {
                    summaryTextElement.textContent = text;
                });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        statusDiv.classList.add('hidden');
    });
});
