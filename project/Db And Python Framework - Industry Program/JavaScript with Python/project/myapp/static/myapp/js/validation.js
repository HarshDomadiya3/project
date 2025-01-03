function validateForm() {
    let name = document.getElementById("id_name").value;
    let email = document.getElementById("id_email").value;
    let age = document.getElementById("id_age").value;
    let errorMessage = document.getElementById("error-message");
    errorMessage.style.display = "none";

    if (!name || !email || !age) {
        errorMessage.textContent = "All fields must be filled out.";
        errorMessage.style.display = "block";
        return false;
    }

    if (age < 18) {
        errorMessage.textContent = "You must be at least 18 years old.";
        errorMessage.style.display = "block";
        return false;
    }

    // Add more validation rules as needed

    return true;
}
