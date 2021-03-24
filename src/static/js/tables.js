let table = document.getElementById('table-id');


function deleteRowOfTable(row){
      let rowIndex = row.parentNode.parentNode.rowIndex;
      table.deleteRow(rowIndex);
}



