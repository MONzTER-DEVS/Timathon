let table = document.getElementById('table-id');


function deleteRowOfTable(row){
      let rowIndex = row.parentNode.parentNode.rowIndex;
      table.deleteRow(rowIndex);
}

let btnAddRecord = document.getElementById('btn-add-id');
let popupBg = document.querySelector('.popup-bg');
let popupClose = document.querySelector('.popup-close');


btnAddRecord.addEventListener('click', function () {
    popupBg.classList.add('popup-active');
})

popupClose.addEventListener('click', function () {
    popupBg.classList.remove('popup-active');
})

let inputArray = [];
let tableBody = document.getElementsByClassName('table-body')[0];
let popupSubmit = document.getElementsByClassName('popup-submit')[0];
let popupInputs = document.getElementsByClassName('popup-input');
popupSubmit.addEventListener('click', function () {
    for (let i = 0; i < popupInputs.length; i++) {
        inputArray.push(popupInputs[i].value);
    }
    const row = tableBody.insertRow(table.rows.length - 1);
    for (let i = 0; i < inputArray.length; i++) {
        row.insertCell(i).innerHTML = inputArray[i];
    }
    let lastCell = row.insertCell(inputArray.length);
    lastCell.innerHTML = '<button class="btn btn-primary" id="btn-edit"><span class="fa fa-pencil-square-o"></span>Edit</button>\n' +
        '            <button class="btn btn-danger btn-delete" id="btn-delete" onclick="deleteRowOfTable(this)"><span class="fa fa-remove"></span>Delete</button>'
    for (let i = 0; i < popupInputs.length; i++) {
        popupInputs[i].value = '';
    }
    popupBg.classList.remove('popup-active');
    inputArray = [];
})


