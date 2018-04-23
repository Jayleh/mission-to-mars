// Reference scrape button by its id
var $scrapeBtn = document.getElementById("scrape-btn");

// Trigger event handler when scrape button is clicked
function handleScrapeClick() {
    $scrapeBtn.setAttribute("disabled", "disabled");
}

// Add event listiner to scrape button
$scrapeBtn.addEventListener("click", handleScrapeClick);