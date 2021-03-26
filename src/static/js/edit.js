let table_body = document.getElementsByClassName('table-body')[0];
let editBtn = document.getElementsByClassName('btn-edit-class');
let popupBgEdit = document.querySelector('.popup-bg-edit');
let popupCloseEdit = document.querySelector('#popup-close-edit');

for (let i = 0; i < editBtn.length; i++) {
 editBtn[i].addEventListener('click', function () {
 let popupInputEdit = document.getElementsByClassName('popup-input-edit');
  popupBgEdit.classList.add('popup-bg-active-edit');
  let rows = table_body.rows[i];
  for (let j = 0; j < popupInputEdit.length; j++) {
   popupInputEdit[j].value = rows.cells[j].innerHTML;
  }
 console.log(rows);
 })
}

popupCloseEdit.addEventListener('click', function () {
 popupBgEdit.classList.remove('popup-bg-active-edit');
})

