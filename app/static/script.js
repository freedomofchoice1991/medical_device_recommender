// Fetch recommendations based on product code
function searchDevice() {
    let productCode = $("#product_code").val().trim(); // Get input

    if (!productCode) {
        alert("Please enter a product code.");
        return;
    }

    // Send request to FastAPI
    $.get(`/recommend/${productCode}`, function (data) {
        let tableBody = $("#recommendations tbody");
        let explanationDiv = $("#search-explanation");

        tableBody.empty(); // Clear table
        explanationDiv.empty(); // Clear previous explanation

        // If no matches found, show message
        if (data.strong_matches.length === 0 && data.potential_alternatives.length === 0) {
            explanationDiv.html(`<p>No alternatives found for <b>${productCode}</b>.</p>`);
            return;
        }

        // Add explanatory text
        explanationDiv.html(`
            <p>You searched for <b>${productCode}</b>.</p>
            <p>This device is classified as <b>${data.strong_matches[0]?.classification_code || "Unknown"}</b>.</p>
            <p><b>Strong Matches</b> belong to the same classification code.</p>
            <p><b>Potential Alternatives</b> belong to the same medical specialty but have a different classification code.</p>
        `);

        // Add strong matches to table
        data.strong_matches.forEach(device => {
            tableBody.append(`<tr>
                <td>${device.product_code}</td>
                <td>${device.device_name}</td>
                <td>${device.classification_code}</td>
            </tr>`);
        });

        // Add potential alternatives to table
        data.potential_alternatives.forEach(device => {
            tableBody.append(`<tr>
                <td>${device.product_code}</td>
                <td>${device.device_name} (Alternative)</td>
                <td>${device.classification_code}</td>
            </tr>`);
        });
    }).fail(function () {
        alert("Error fetching data. Please try again.");
    });
}



// Fetch and display grouped classification data
function loadGrouped() {
    $.get("/grouped", function (data) {
        let tableBody = $("#grouped tbody");
        let explanationDiv = $("#grouped-explanation");

        tableBody.empty(); // Clear previous table
        explanationDiv.empty(); // Clear previous explanation

        // Add explanation text
        explanationDiv.html(`
            <p>The table below shows devices grouped by their classification code.</p>
            <p>Devices with the same classification code share similar intended medical applications.</p>
        `);

        let lastClassification = ""; // Track last classification code

        data.grouped_devices.forEach(row => {
            let classification = row[0] || "Unknown"; // Default to "Unknown" if empty
            let device = row[1];

            // If it's a new classification code, add a row for it
            if (classification !== lastClassification) {
                tableBody.append(`<tr>
                    <td><b>${classification}</b></td>
                    <td>${device}</td>
                </tr>`);
            } else {
                // Otherwise, just add the device in a new row under the same classification
                tableBody.append(`<tr>
                    <td></td>
                    <td>${device}</td>
                </tr>`);
            }

            lastClassification = classification; // Update last seen classification code
        });
    });
}


// Export table data to CSV
function exportToCSV() {
    let csv = "Product Code,Device Name\n";
    $("#recommendations tbody tr").each(function () {
        let row = $(this).find("td").map(function () { return $(this).text(); }).get().join(",");
        csv += row + "\n";
    });

    let blob = new Blob([csv], { type: "text/csv" });
    let a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "device_recommendations.csv";
    a.click();
}

// Export table data to PDF (simple method)
function exportToPDF() {
    let printContent = document.querySelector(".container").innerHTML;
    let newWin = window.open("");
    newWin.document.write("<html><head><title>Export</title></head><body>");
    newWin.document.write(printContent);
    newWin.document.write("</body></html>");
    newWin.print();
    newWin.close();
}
