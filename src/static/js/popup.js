// const openPopupButtons = document.querySelectorAll('[data-model-target]');
// const closePopupButtons = document.querySelectorAll('[data-close-button]');
const overlay = document.getElementById('overlay');
const addRecordButton = document.getElementsByClassName('table-add-record')[0];
addRecordButton.addEventListener('click', function (){
    overlay.style.backgroundColor = 'yellow';
})


// openPopupButtons.forEach(button => {
//     button.addEventListener('click', ()=>{
//         const popup = document.querySelector(button.dataset.modelTarget);
//         openPopup(popup);
//     })
// })
//
// closePopupButtons.forEach(button => {
//     button.addEventListener('click', ()=>{
//         const popup = buttonc.closest('.popup-inner-div')
//         closePopup(popup);
//     })
// })
//
// function openPopup(popup){
//     if(popup == null) return
//     popup.classList.add('active')
//     overlay.classList.add('active')
// }
//
// function closePopup(popup){
//     if(popup == null) return
//     popup.classList.remove('active')
//     overlay.classList.remove('active')
// }