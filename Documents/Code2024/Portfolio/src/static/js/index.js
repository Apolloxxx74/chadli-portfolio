const Aboutme = document.querySelector("#homelink");
const education = document.querySelector("#educationlink");
const contact = document.querySelector("#contactlink");
const services = document.querySelector("#serviceslink");

// Store all nav items in an array
const navItems = [Aboutme, education, contact, services];

// Function to remove all active classes
function resetColors() {
    navItems.forEach(item => {
        item.classList.remove("active-green", "active-yellow", "active-blue", "active-purple");
    });
}

// Add event listeners
Aboutme.addEventListener("click", function() {
    resetColors();
    Aboutme.classList.add("active-yellow");
});

education.addEventListener("click", function() {
    resetColors();
    education.classList.add("active-green");
});

contact.addEventListener("click", function() {
    resetColors();
    contact.classList.add("active-blue");
});

services.addEventListener("click", function() {
    resetColors();
    services.classList.add("active-purple");
});

    

