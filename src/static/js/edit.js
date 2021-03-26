// Variables
let table_body = document.getElementsByClassName('table-body')[0];
let editBtn = document.getElementsByClassName('btn-edit-class');
let popupBgEdit = document.querySelector('.popup-bg-edit');
let popupCloseEdit = document.querySelector('#popup-close-edit');
let saveBtn = document.getElementById('save-changes');
let cancelBtn = document.getElementById('cancel-changes');
let input_array = [];
var Rows;

function editBtnsLoop() {
 // Looping all the edit buttons
 for (let i = 0; i < editBtn.length; i++) {
  // click event
  editBtn[i].addEventListener('click', function () {
   // entering the default data in the input cells
   let popupInputEdit = document.getElementsByClassName('popup-input-edit');
   popupBgEdit.classList.add('popup-bg-active-edit');
   let rows = table_body.rows[i];
   for (let j = 0; j < popupInputEdit.length; j++) {
    popupInputEdit[j].value = rows.cells[j].innerHTML;
   }
   // console.log(rows);
   Rows = rows;
  })
 }
}
editBtnsLoop()

popupCloseEdit.addEventListener('click', function () {
 popupBgEdit.classList.remove('popup-bg-active-edit');
})

popupInputs = document.getElementsByClassName('popup-input-edit');

// save button - click event
saveBtn.addEventListener('click', function () {
 // getting the values in the input cells
 for (let i = 0; i < popupInputs.length; i++) {
  input_array.push(popupInputs[i].value);
 }
 // making the change in the actual table
 for (let j = 0; j < Rows.cells.length; j++) {
  Rows.cells[j].innerHTML = input_array[j];
 }
 // adding the edit and delete buttons in the last cell
 let lastCellIndex = Rows.cells.length - 1;
 Rows.cells[lastCellIndex].innerHTML = '<button class="btn btn-primary btn-edit-class" id="btn-edit"><span\n' +
     '                        class="fa fa-pencil-square-o"></span>Edit</button>\n' +
     '                <button class="btn btn-danger btn-delete" id="btn-delete" onclick="deleteRowOfTable(this)"><span\n' +
     '                        class="fa fa-remove"></span>Delete</button>';
 editBtnsLoop();
 // clearing the inputs from the input array
 input_array = [];
 // closing the popup
 popupBgEdit.classList.remove('popup-bg-active-edit');
})

// cancel button - click event
cancelBtn.addEventListener('click', function () {
 // just closing the popup
 popupBgEdit.classList.remove('popup-bg-active-edit');
 editBtnsLoop();
})

