// Toggle burger menu on mobile
document.addEventListener("DOMContentLoaded", function () {
    const burgerIcon = document.getElementById("burger-icon");
    const navMenu = document.getElementById("nav-menu");

    if (burgerIcon && navMenu) {
        burgerIcon.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });
    }
});
