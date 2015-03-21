var chart;

$(function () {
    sections();
    hideCharts();
    chart = getChartObj();
    get_price_log();
});

function getDataset(labels, data) {
    return {
        labels: labels,
        datasets: [
            {
                label: "My First dataset",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: data
            }
        ]
    }
}

function hideCharts() {
    $("#myChart").hide();
}

function showCharts() {
    $("#myChart").show();
}

function getChartObj() {
    var ctx = $("#myChart").get(0).getContext("2d");
    width_five_percent = screen.width * 0.05;
    ctx.canvas.width = screen.width - width_five_percent;
    return new Chart(ctx);
}

function get_price_log() {
    $.ajax({
        url: "/summary",
        success: onSuccess,
        error: function (err) {
            console.log("error");
        }
    });
}

function onSuccess(result) {
    hide_loading();
    console.log("success");
    console.log(result);
    var labels = [];
    var data = [];
    var index;
    for (index = 0; index < result.log.length; ++index) {
        labels.push(result.log[index][0]);
        data.push(result.log[index][1]);
    }
    var dataset = getDataset(labels, data);
    chart.Line(dataset, {});
    showCharts();
}

function hide_loading() {
    $("#loading").hide();
}
