var popupBgFiles = document.querySelector('.popup-bg');
var btnOk = document.getElementById('btn-ok');
var btnTimes = document.getElementById('btn-close-files');
btnOk.addEventListener('click', function () {
        location.href = '/';
})
btnTimes.addEventListener('click', function () {
    location.href = '/';
})
popupBgFiles.classList.add('popup-active-files');
