// Fetch data and plot the graph and table
function fetchMppcDataAndPlot() {
    $.getJSON('/_fetch_mppc_data', function (data) {

        const trace = [{
            x: data.bin_centers,
            y: data.bin_values,
            type: 'bar',
            width: data.bin_widths,
            // marker: {
            //     color: 'blue'
            // },
        }];

        // Layout configuration
        const layout = {
            showlegend: false,
            height: 750,
            grid: { rows: 2, columns: 2, pattern: 'independent', xgap: 0.1, ygap: 0.2 },
            margin: { t: 20, l: 45, r: 45 },
        };

        // Plot the graph
        Plotly.newPlot('trendGraph', trace, layout, {
            toImageButtonOptions: {
                format: 'png',
                filename: "monitor_trend_",
                scale: 1
            }
        });


    });
}

// Execute on page load
$(document).ready(function () {
    // Update graph on button click
    $('#updateButton').click(function() {
        fetchMppcDataAndPlot();
    });
});