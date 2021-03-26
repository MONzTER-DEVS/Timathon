// console.log("Testing!");
const nav = document.querySelector(".navbar-div");

const colorNav = 'rgba(0, 0, 0, 0.5)';
const tempNavHeight = 120;
function changeColorNav(){
    if (nav.getBoundingClientRect().top + document.documentElement.scrollTop > tempNavHeight) {
        nav.style.backgroundColor = colorNav;
        // nav.style.backDrop = "blur(10px)";
        nav.style.boxShadow = "0 0 1em #000000"
        nav.style.transition = "all 0.4s ease-in";
        nav.style.zIndex = "5"
    } else {
        nav.style.transition = "all 0.4s ease-in";
        nav.style.backgroundColor = "transparent";
        nav.style.boxShadow = ""
        nav.style.border = 0;
    }
}

window.addEventListener('scroll', changeColorNav);
