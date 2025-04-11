const open = document.getElementById("menu-open-button")
const close = document.getElementById("menu-close-button")
const nav_links_box = document.querySelector(".nav-links-box")
const overlay = document.getElementById("overlay");
const show = document.querySelector(".show")

open.addEventListener('click', () => {
    nav_links_box.classList.add("show")
    overlay.style.display = "block";
})
close.addEventListener('click', () => {
    nav_links_box.classList.remove("show")
    overlay.style.display = "none";
})