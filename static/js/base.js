// Dark Mode Toggle
const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");

function updateIcon() {
    if (document.body.getAttribute("data-bs-theme") === "dark") {
        themeIcon.classList.remove("bi-sun");
        themeIcon.classList.add("bi-moon");
    } else {
        themeIcon.classList.remove("bi-moon");
        themeIcon.classList.add("bi-sun");
    }
}

themeToggle.addEventListener("click", () => {
    if (document.body.getAttribute("data-bs-theme") === "dark") {
        document.body.setAttribute("data-bs-theme", "light");
        localStorage.removeItem("theme");
    } else {
        document.body.setAttribute("data-bs-theme", "dark");
        localStorage.setItem("theme", "dark");
    }
    updateIcon();
});

// Load saved theme
if (localStorage.getItem("theme") === "dark") {
    document.body.setAttribute("data-bs-theme", "dark");
    updateIcon();
} else {
    document.body.setAttribute("data-bs-theme", "light");
    updateIcon();
}

