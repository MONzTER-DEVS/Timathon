const selected = document.querySelector('.selected');
const optionsContainer = document.querySelector('.options-container');
const optionsList = document.querySelectorAll('.option');
const arrow = document.querySelector('.arrow-css');

selected.addEventListener('click', function () {
    // arrow.classList.remove('fa-arrow-down');
    // arrow.classList.add('fa-arrow-up')
    optionsContainer.classList.toggle('active-options');
});
var indexHead;
var head;
optionsList.forEach(o => {
    console.log(o);
    o.addEventListener('click', () => {
        // arrow.classList.remove('fa-arrow-up')
        // arrow.classList.add('fa-arrow-down');
        selected.innerHTML = o.querySelector('label').innerHTML;
        // index = optionsList.indexOf(o);
        head = o.textContent;
        optionsContainer.classList.remove('active-options');
    })
})


function search() {
    let filter = document.getElementById('search-input').value.toUpperCase();
    let table_ = document.getElementById('table-id');
    let tr = table_.getElementsByTagName('tr');
    for (let i = 0; i < optionsList.length; i++) {
        if (optionsList[i].textContent === head) {
            indexHead = i;
        }
        for (let i = 0; i < tr.length; i++) {
            let td = tr[i].getElementsByTagName('td')[indexHead];
            if (td) {
                let textValue = td.textContent || td.innerHTML
                if (textValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }

            }
        }
    }
}
