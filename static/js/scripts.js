document.addEventListener("DOMContentLoaded", () => {
    // Highlight rows on hover
    const rows = document.querySelectorAll("table tbody tr");
    rows.forEach(row => {
        row.addEventListener("mouseover", () => {
            row.style.backgroundColor = "#f0f8ff"; // Light blue
        });
        row.addEventListener("mouseout", () => {
            row.style.backgroundColor = ""; // Reset to default
        });
    });

    // Confirm deletion
    const deleteForms = document.querySelectorAll("form[action^='/delete/']");
    deleteForms.forEach(form => {
        form.addEventListener("submit", (event) => {
            const confirmDelete = confirm("Are you sure you want to delete this trade?");
            if (!confirmDelete) {
                event.preventDefault(); // Prevent form submission
            }
        });
    });

    // Validate input before submitting the form
    const addForm = document.querySelector("form[action='/add']");
    if (addForm) {
        addForm.addEventListener("submit", (event) => {
            const currencyPair = addForm.querySelector("input[name='currency_pair']").value.trim();
            const date = addForm.querySelector("input[name='date']").value.trim();
            const typeOfTrade = addForm.querySelector("input[name='type_of_trade']").value.trim();

            if (!currencyPair || !date || !typeOfTrade) {
                alert("Please fill out all required fields.");
                event.preventDefault(); // Prevent form submission
            }
        });
    }
});
