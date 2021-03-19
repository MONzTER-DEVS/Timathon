titleText = document.getElementsByClassName('heading-desc')[0];
buttonOne = document.getElementsByClassName('btn-get-started')[0]
buttonTwo = document.getElementsByClassName('btn-how-it-works')[0];
image = document.getElementsByClassName('heading-img')[0];
featuresText = document.getElementsByClassName('features-text')[0];
window.addEventListener('DOMContentLoaded', titleAnimation = () => {
    titleText.classList.add('animation-fade-up');
    buttonOne.classList.add('animation-fade-up');
    buttonTwo.classList.add('animation-fade-up');
    image.classList.add('animation-fade-up');
    featuresText.classList.add('animation-fade-up');
});

// if(navbar.classList.contains('navbar-animation')){
//     /* animation: amination-name animation-duration animation-iteration-count; */
//     navbar.style.animation: '2.5s 1 '
// }