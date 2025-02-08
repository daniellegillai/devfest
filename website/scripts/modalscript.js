// Select all buttons that open modals
const modalButtons = document.querySelectorAll(".open-modal");

// Select all close buttons
const closeButtons = document.querySelectorAll(".close");

// Function to open a modal
modalButtons.forEach(button => {
    button.addEventListener("click", () => {
        const modalId = button.getAttribute("data-modal");
        document.getElementById(modalId).style.display = "block";
    });
});

// Function to close a modal
closeButtons.forEach(button => {
    button.addEventListener("click", () => {
        const modalId = button.getAttribute("data-modal");
        document.getElementById(modalId).style.display = "none";
    });
});

// Close modal if user clicks outside the modal content
window.addEventListener("click", (event) => {
    document.querySelectorAll(".modal").forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});