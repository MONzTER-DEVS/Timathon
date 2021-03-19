titleText = document.getElementsByClassName('heading-desc')[0];
buttonOne = document.getElementsByClassName('btn-get-started')[0]
buttonTwo = document.getElementsByClassName('btn-how-it-works')[0];
image = document.getElementsByClassName('heading-img')[0];
window.addEventListener('DOMContentLoaded', titleAnimation = () => {
    titleText.classList.add('animation');
    buttonOne.classList.add('animation');
    buttonTwo.classList.add('animation');
    image.classList.add('animation');
});

// if(navbar.classList.contains('navbar-animation')){
//     /* animation: amination-name animation-duration animation-iteration-count; */
//     navbar.style.animation: '2.5s 1 '
// }