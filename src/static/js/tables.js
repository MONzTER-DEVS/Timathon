// let table = document.getElementById('table-id');
// let cells = table.getElementsByClassName('table-elements');
// let editBtn = document.getElementById('btn-edit');
// let delBtn = document.getElementById('btn-delete');
//
// if (cells) {
//     for (let i = 0; i < cells.length; i++) {
//         editBtn.addEventListener('click', function () {
//             if (this.hasAttribute('data-clicked')){
//                 return;
//             }
//             this.setAttribute('data-clicked', 'yes');
//             this.setAttribute('data-text', this.innerHTML);
//             let input = document.createElement('input');
//             input.setAttribute('type', 'text');
//             input.value = this.innerHTML;
//             // input.style.width = this.offsetWidth - (this.clientLeft * 2) + 'px';
//             // input.style.height = this.offsetHeight - (this.clientTop * 2) + 'px';
//             input.onblur = function () {
//                 let td = input.parentElement;
//                 let originalText = input.parentElement.getAttribute('data-text');
//                 let currentText = this.value;
//                 if(originalText !== currentText){
//                     td.removeAttribute('data-clicked');
//                     td.removeAttribute('data-text');
//                     td.innerHTML = currentText;
//                 }
//                 else{
//                     td.removeAttribute('data-clicked');
//                     td.removeAttribute('data-text');
//                     td.innerHTML = originalText;
//                 }
//             }
//
//             this.innerHTML = '';
//             this.append(input);
//             this.firstElementChild.select();
//         })
//     }
// }
//
//
