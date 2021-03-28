// var fullPath = document.getElementById('upload').value;
// if (fullPath) {
//     var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
//     var filename = fullPath.substring(startIndex);
//     if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
//         filename = filename.substring(1);
//     }
//     alert(filename);
// }
var filepath;

const submitChartFormBtn = document.getElementById('submit-chart');
submitChartFormBtn.addEventListener('click', message => {
    // let file = document.getElementById('file-upload-id-chart');
    // alert(file.files[0].name);
    let fullPath = document.getElementById('file-upload-id-chart').value;
    if (fullPath) {
        let startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
        let filename = fullPath.substring(startIndex);
        if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
            filename = filename.substring(1);
        }
        filepath = `../src/media/${filename}`;
        // alert(filename);
    }
})

function parseData(createGraph){
    Papa.parse(filepath, {
        download: true,
        complete: function (results) {
            console.log(results.data);
            createGraph(results.data);
        }
    });
}

function createGraph(data) {

}

parseData(createGraph);




