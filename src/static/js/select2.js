const selectedTwo = document.querySelector('.selected-two');
const optionsContainerTwo = document.querySelector('.options-container-two');
const optionsListTwo = document.querySelectorAll('.option-two');

selectedTwo.addEventListener('click', function () {
    // arrow.classList.remove('fa-arrow-down');
    // arrow.classList.add('fa-arrow-up')
    optionsContainerTwo.classList.toggle('active-options-two');
});

var choice = 'bar';
optionsListTwo.forEach(o => {
    console.log(o);
    o.addEventListener('click', () => {
        // arrow.classList.remove('fa-arrow-up')
        // arrow.classList.add('fa-arrow-down');
        selectedTwo.innerHTML = o.querySelector('label').innerHTML;
        // index = optionsList.indexOf(o);
        choice = selectedTwo.innerHTML.toLowerCase();
        localStorage.setItem('graph', choice);
        optionsContainerTwo.classList.remove('active-options-two');
    })
})