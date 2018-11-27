function renderDayGraph(dates,dayRevenue,dayCount,Days){
  var chartData = [];
  for (i=0;i<Days;i++) {
    chartData.push({
        date: new Date(dates[i]),
        revenue: dayRevenue[i],
        count: dayCount[i]
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
/* --------------------------- */
function renderRideDayRevenueGraph(dates,cr,drr,dtr,fwr,gtr,rcr,wrr,ssr,cir,gr,hours){
  var chartData = [];
  for (i=0;i<hours;i++) {
    chartData.push({
        date: new Date(dates[i]),
        carousel: cr[i],
        darkride : drr[i],
        droptower : dtr[i],
        ferriswheel : fwr[i],
        gyrotower : gtr[i],
        rollercoaster : rcr[i],
        waterride : wrr[i],
        spiralslide : ssr[i],
        circus : cir[i],
        gravitron : gr[i]
        });
    }

  var chart = AmCharts.makeChart("ride_day_stats", {
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
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v3",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v4",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v5",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v6",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v7",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v8",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v9",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }, {
          "id":"v10",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "right"
      }],
      "graphs": [{
          "valueAxis": "v1",
          "lineColor": "#FF6600",
          "bullet": "round",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Carousel",
          "valueField": "carousel",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v2",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Darkride",
          "valueField": "darkride",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v3",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Droptower",
          "valueField": "droptower",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v4",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Ferriswheel",
          "valueField": "ferriswheel",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v5",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Gyrotower",
          "valueField": "gyrotower",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v6",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Rollercoaster",
          "valueField": "rollercoaster",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v7",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Waterride",
          "valueField": "waterride",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v8",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Gravitron",
          "valueField": "gravitron",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v9",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "SpiralSlide",
          "valueField": "spiralslide",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v10",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Circus",
          "valueField": "circus",
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
/* ---------------------------------- */
function renderRideDayCountGraph(dates,cc,drc,dtc,fwc,gtc,rcc,wrc,ssc,cic,gc,hours){
  var chartData = [];
  for (i=0;i<hours;i++) {
    chartData.push({
        date: new Date(dates[i]),
        carousel: cc[i],
        darkride: drc[i],
        droptower: dtc[i],
        ferriswheel: fwc[i],
        gyrotower: gtc[i],
        rollercoaster: rcc[i],
        waterride: wrc[i],
        spiralslide: ssc[i],
        circus: cic[i],
        gravitron: gc[i]
        });
    }

  var chart = AmCharts.makeChart("ride_day_count", {
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
          "axisAlpha": 0.1,
          "position": "left"
      }, {
          "id":"v2",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.2,
          "position": "left"
      }, {
          "id":"v3",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.3,
          "position": "left"
      }, {
          "id":"v4",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.4,
          "position": "left"
      }, {
          "id":"v5",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.5,
          "position": "left"
      }, {
          "id":"v6",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.6,
          "position": "right"
      }, {
          "id":"v7",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.7,
          "position": "right"
      }, {
          "id":"v8",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.8,
          "position": "right"
      }, {
          "id":"v9",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 0.9,
          "position": "right"
      }, {
          "id":"v10",
          "axisColor": "#FCD202",
          "axisThickness": 2,
          "axisAlpha": 1,
          "position": "right"
      }],
      "graphs": [{
          "valueAxis": "v1",
          "lineColor": "#FF6600",
          "bullet": "round",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Carousel",
          "valueField": "carousel",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v2",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Darkride",
          "valueField": "darkride",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v3",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Droptower",
          "valueField": "droptower",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v4",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Ferriswheel",
          "valueField": "ferriswheel",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v5",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Gyrotower",
          "valueField": "gyrotower",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v6",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Rollercoaster",
          "valueField": "rollercoaster",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v7",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Waterride",
          "valueField": "waterride",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v8",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Gravitron",
          "valueField": "gravitron",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v9",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "SpiralSlide",
          "valueField": "spiralslide",
  		"fillAlphas": 0
      }, {
          "valueAxis": "v10",
          "lineColor": "#FCD202",
          "bullet": "square",
          "bulletBorderThickness": 1,
          "hideBulletsCount": 30,
          "title": "Circus",
          "valueField": "circus",
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
