const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultSection = document.getElementById('resultSection');
const captionResult = document.getElementById('captionResult');
const loading = document.getElementById('loading');
const newImageBtn = document.getElementById('newImageBtn');

let selectedFile = null;

uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFile(e.target.files[0]);
    }
});

function handleFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('Lütfen geçerli bir görüntü dosyası seçin.');
        return;
    }
    
    selectedFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        uploadArea.style.display = 'none';
        previewSection.style.display = 'block';
        resultSection.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

analyzeBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    loading.style.display = 'block';
    resultSection.style.display = 'none';
    analyzeBtn.disabled = true;

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
        const response = await fetch('/api/caption', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Bir hata oluştu');
        }

        const data = await response.json();
        captionResult.textContent = data.caption;
        resultSection.style.display = 'block';
        newImageBtn.style.display = 'inline-block';
    } catch (error) {
        alert('Hata: ' + error.message);
    } finally {
        loading.style.display = 'none';
        analyzeBtn.disabled = false;
    }
});

newImageBtn.addEventListener('click', () => {
    selectedFile = null;
    fileInput.value = '';
    previewImage.src = '';
    uploadArea.style.display = 'block';
    previewSection.style.display = 'none';
    resultSection.style.display = 'none';
    newImageBtn.style.display = 'none';
});

async function checkHealth() {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        if (!data.ready && !data.loading) {
            captionResult.textContent = 'Model yüklenemedi: ' + data.error;
            resultSection.style.display = 'block';
        }
    } catch (error) {
        console.error('Health check failed:', error);
    }
}

checkHealth();
