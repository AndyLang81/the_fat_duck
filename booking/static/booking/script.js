// static/booking/script.js

document.addEventListener("DOMContentLoaded", function () {
    // Toggle burger menu on mobile
    const burgerIcon = document.getElementById("burger-icon");
    const navMenu = document.getElementById("nav-menu");

    if (burgerIcon && navMenu) {
        burgerIcon.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });
    }

    // Auto-scroll to booking form if there's an error message
    const bookingFormContainer = document.getElementById("booking-form");
    if (bookingFormContainer && bookingFormContainer.querySelector("p")) {
        bookingFormContainer.scrollIntoView({ behavior: "smooth" });
    }

    // Disable fully booked time slots
    const dateInput = document.getElementById("id_date");
    const timeSelect = document.getElementById("id_time");
    const MAX_PER_SLOT = 1;  // demo limit

    function updateTimeOptions() {
        const date = dateInput.value;
        if (!date) return;

        fetch(`/availability/?date=${date}`)
            .then(response => response.json())
            .then(slots => {
                Array.from(timeSelect.options).forEach(opt => {
                    const slot = opt.value;
                    if (slots[slot] >= MAX_PER_SLOT) {
                        opt.disabled = true;
                        opt.style.color = "#ccc";
                    } else {
                        opt.disabled = false;
                        opt.style.color = "";
                    }
                });
            })
            .catch(err => {
                console.error("Error fetching availability:", err);
            });
    }

    if (dateInput && timeSelect) {
        dateInput.addEventListener("change", updateTimeOptions);
        updateTimeOptions();
    }
});
