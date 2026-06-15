const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("keyup", function() {
    let filter = searchInput.value.toLowerCase();

    let rows = document.querySelectorAll("table tr");

    rows.forEach((row, index) => {
        if(index === 0) return;

        row.style.display =
            row.textContent.toLowerCase().includes(filter)
            ? ""
            : "none";
    });
});