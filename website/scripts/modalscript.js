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

//retrieve selected image from localStorage
window.onload = function() {
    // Retrieve selected image from localStorage
    let selectedImage = localStorage.getItem('selectedImage');

    // Find the image container
    let container = document.getElementById('imageContainer');

    if (selectedImage) {
        // Create an img element
        let img = document.createElement('img');
        img.src = selectedImage; // Use the saved image path
        img.alt = "Selected Image";
        img.className = "selected-image";

        // Add image to the container
        container.appendChild(img);
    } else {
        // Show message if no image was selected
        container.innerHTML = "<p class='message'>No image selected.</p>";
    }
};