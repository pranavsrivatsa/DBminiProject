/*--------------  customer age group bar chart start ------------*/
function renderGraph(ageRanges){
  glabels = ["0-10","11-18","19-30","31-50","51-70","71-100"]
  if ($('#visitor_graph').length) {
      var ctx = document.getElementById("visitor_graph").getContext('2d');
      var chart = new Chart(ctx, {
          // The type of chart we want to create
          type: 'bar',
          // The data for our dataset
          data: {
              labels: glabels,
              datasets: [{
                  label: "Count",
                  data: ageRanges,
                  backgroundColor: [
                      '#8416fe',
                      '#3a3afb',
                      '#8416fe',
                      '#3a3afb',
                      '#8416fe',
                      '#3a3afb',
                      '#8416fe',
                      '#3a3afb',
                      '#3a3afb',
                      '#8416fe'
                  ]
              }]
          },
          // Configuration options go here
          options: {
              legend: {
                  display: false
              },
              animation: {
                  easing: "easeInOutBack"
              },
              scales: {
                  yAxes: [{
                      display: !1,
                      ticks: {
                          fontColor: "#cccccc",
                          beginAtZero: !0,
                          padding: 0
                      },
                      gridLines: {
                          zeroLineColor: "transparent"
                      }
                  }],
                  xAxes: [{
                      display: !1,
                      gridLines: {
                          zeroLineColor: "transparent",
                          display: !1
                      },
                      ticks: {
                          beginAtZero: !0,
                          padding: 0,
                          fontColor: "#cccccc"
                      }
                  }]
              }
          }
      });
  }
};

/*--------------  customer age group bar chart start ------------*/
if ($('#ambarchart3').length) {
    var chart = AmCharts.makeChart("ambarchart3", {
        "type": "serial",
        "theme": "light",
        "categoryField": "year",
        "rotate": true,
        "startDuration": 1,
        "categoryAxis": {
            "gridPosition": "start",
            "position": "left"
        },
        "trendLines": [],
        "graphs": [{
                "balloonText": "Income:[[value]]",
                "fillAlphas": 0.8,
                "id": "AmGraph-1",
                "lineAlpha": 0.2,
                "title": "Income",
                "type": "column",
                "valueField": "income",
                "fillColorsField": "color"
            },
            {
                "balloonText": "Expenses:[[value]]",
                "fillAlphas": 0.8,
                "id": "AmGraph-2",
                "lineAlpha": 0.2,
                "title": "Expenses",
                "type": "column",
                "valueField": "expenses",
                "fillColorsField": "color2"
            }
        ],
        "guides": [],
        "valueAxes": [{
            "id": "ValueAxis-1",
            "position": "top",
            "axisAlpha": 0
        }],
        "allLabels": [],
        "balloon": {},
        "titles": [],
        "dataProvider": [{
                "year": 2014,
                "income": 23.5,
                "expenses": 18.1,
                "color": "#7474f0",
                "color2": "#C5C5FD"
            },
            {
                "year": 2015,
                "income": 26.2,
                "expenses": 22.8,
                "color": "#7474f0",
                "color2": "#C5C5FD"
            },
            {
                "year": 2016,
                "income": 30.1,
                "expenses": 23.9,
                "color": "#7474f0",
                "color2": "#C5C5FD"
            },
            {
                "year": 2017,
                "income": 29.5,
                "expenses": 25.1,
                "color": "#7474f0",
                "color2": "#C5C5FD"
            },
            {
                "year": 2018,
                "income": 24.6,
                "expenses": 25,
                "color": "#7474f0",
                "color2": "#C5C5FD"
            }
        ],
        "export": {
            "enabled": false
        }

    });
}
/*--------------  bar chart 10 amchart END ------------*/
