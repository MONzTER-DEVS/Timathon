let editBtn = document.getElementsByClassName('btn-edit-class');
let tableBody = document.getElementsByClassName('table-body')[0];
for (let i = 0; i < editBtn.length; i++) {
 editBtn[i].addEventListener('click', function () {
  rows = tableBody.rows[i];
 })
}

// let btnAddRecord = document.getElementById('btn-add-id');
// let popupBg = document.querySelector('.popup-bg');
// let popupClose = document.querySelector('.popup-close');


// btnAddRecord.addEventListener('click', function () {
//     popupBg.classList.add('popup-active');
// })

// popupClose.addEventListener('click', function () {
//     popupBg.classList.remove('popup-active');
// })



