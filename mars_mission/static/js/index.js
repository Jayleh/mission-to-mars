// // Reference scrape button by its id
// var $scrapeBtn = document.getElementById("scrape-btn");

// // Trigger event handler when scrape button is clicked
// function handleScrapeClick() {
//     $scrapeBtn.setAttribute("disabled", "disabled");
// }

// // Add event listiner to scrape button
// $scrapeBtn.addEventListener("click", handleScrapeClick);


// Function to show progress bar
function showProgress() {
    var elem = d3.select(".progress-bar");
    var width = 0;
    var id = setInterval(frame, 550);
    function frame() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++;
            elem.style("width", `${width}%`);
        }
    }
}


var $scrapeBtn = d3.select("#scrape-btn");

$scrapeBtn.on("click", function () {
    // Disable button
    $scrapeBtn.attr("disabled", "disabled");

    // Make progress bar visible
    var $progressBar = d3.select(".progress");
    $progressBar.style("visibility", "visible");

    showProgress();

})