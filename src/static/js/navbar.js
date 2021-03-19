// console.log("Testing!");
const nav = document.querySelector("nav");

const colorNav = '#e9eadb';
const tempNavHeight = 120;
function changeColorNav(){
    if (nav.getBoundingClientRect().top + document.documentElement.scrollTop > tempNavHeight) {
        nav.style.backgroundColor = colorNav;
        nav.style.transition = "all 0.4s ease-in";
        nav.style.zIndex = "5"
    } else {
        nav.style.transition = "all 0.4s ease-in";
        nav.style.backgroundColor = "transparent";
        nav.style.border = 0;
    }
}

window.addEventListener('scroll', changeColorNav);
