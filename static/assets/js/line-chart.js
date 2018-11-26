function renderLineGraph(dates,dayRevenue,dayCount){
  var chartData = [];
  for (i=0;i<57;i++) {
    chartData.push({
        date: new Date(dates[i]),
        revenue: dayRevenue,
        count: dayCount
        });
  }

  var chart = AmCharts.makeChart("day_stats", {
      "type": "serial",
      "theme": "light",
      "marginRight": 20,
      "autoMarginOffset": 20,
      "marginTop": 7,
      "legend": {
          "useGraphSettings": true
      },
      "dataProvider": chartData,
      "synchronizeGrid":true,
      "valueAxes": [{
          "id":"v1",
          "axisColor": "#FF6600",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "left"
      }, {
          "id":"v2",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.1,
          "position": "right"
      }],
      "graphs": [{
          "valueAxis": "v1",
          "lineColor": "#FF6600",
          "bullet": "round",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Revenue",
          "valueField": "revenue",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v2",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Count",
          "valueField": "count",
  		"fillAlphas": 0
      }],
      "chartScrollbar": {},
      "chartCursor": {
          "cursorPosition": "mouse"
      },
      "categoryField": "date",
      "categoryAxis": {
          "parseDates": true,
          "axisColor": "#DADADA",
          "dashLength": 1,
          "minorGridEnabled": true
      },
      "export": {
      	"enabled": true,
          "position": "top-right"
       }
  });

  chart.addListener("dataUpdated", zoomChart);
  zoomChart();

  function zoomChart() {
      chart.zoomToIndexes(chartData.length - 40, chartData.length - 1);
  }
}
/*

function renderLineGraph(dates,dayRevenue,dayCount){

  am4core.useTheme(am4themes_animated);
  var chart = am4core.create("day_stats", am4charts.XYChart);
  var chartData = [];
  for (var i = 0; i < 57; i++) {
    var newDate = new Date(dates[i]);
    chartData.push({
      date: newDate,
      value: dayCount[i]
    });
  }
  chart.data = chartData;
  var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  var series = chart.series.push(new am4charts.LineSeries());
  series.dataFields.valueY = "value";
  series.dataFields.dateX = "date";
  series.tooltipText = "{value}"
  series.strokeWidth = 2;
  series.minBulletDistance = 15;

  // Drop-shaped tooltips
  series.tooltip.background.cornerRadius = 20;
  series.tooltip.background.strokeOpacity = 0;
  series.tooltip.pointerOrientation = "vertical";
  series.tooltip.label.minWidth = 40;
  series.tooltip.label.minHeight = 40;
  series.tooltip.label.textAlign = "middle";
  series.tooltip.label.textValign = "middle";

  // Make bullets grow on hover
  var bullet = series.bullets.push(new am4charts.CircleBullet());
  bullet.circle.strokeWidth = 2;
  bullet.circle.radius = 4;
  bullet.circle.fill = am4core.color("#fff");

  var bullethover = bullet.states.create("hover");
  bullethover.properties.scale = 1.3;

  // Make a panning cursor
  chart.cursor = new am4charts.XYCursor();
  chart.cursor.behavior = "panXY";

  // Create vertical scrollbar and place it before the value axis
  chart.scrollbarY = new am4core.Scrollbar();
  chart.scrollbarY.parent = chart.leftAxesContainer;
  chart.scrollbarY.toBack();

  // Create a horizontal scrollbar with previe and place it underneath the date axis
  chart.scrollbarX = new am4charts.XYChartScrollbar();
  chart.scrollbarX.series.push(series);
  chart.scrollbarX.parent = chart.bottomAxesContainer;

  chart.events.on("ready", function () {
    dateAxis.zoom({start:0.79, end:1});
  });
}
*/
