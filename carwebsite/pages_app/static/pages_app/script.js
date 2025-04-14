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
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            window.scrollTo({
                top: target.offsetTop,
                behavior: "smooth"
            });
        }
    });
});