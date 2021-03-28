var fileUploadChart = function (e) {
    let file = e.target.files;
    let show = "<span>Selected File: </span>"+file[0].name;
    let output = document.getElementById('selector-label-chart');
    output.innerHTML = show;
    output.classList.add('active');
};

let fileInputChart = document.getElementById('file-upload-id');
fileInputChart.addEventListener('change', fileUploadChart);