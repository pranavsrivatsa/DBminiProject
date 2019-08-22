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
