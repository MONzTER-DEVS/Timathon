var fileUpload = function (e) {
    let file = e.target.files;
    let show = "<span>Selected File: </span>"+file[0].name;
    let output = document.getElementById('selector-label');
    output.innerHTML = show;
    output.classList.add('active');
};

let fileInput = document.getElementById('file-upload-id');
fileInput.addEventListener('change', fileUpload);


