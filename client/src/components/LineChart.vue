<script>
  import { Line, mixins } from 'vue-chartjs'
  const { reactiveProp } = mixins
  export default {
    extends: Line,
    mixins: [ reactiveProp ],
    data () {
      return {
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true,
                callback: function(value, index, values) {
                  if(parseInt(value) >= 1000){
                    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                  } else {
                    return value;
                  }
                }
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    mounted () {
      this.renderChart(this.chartData, this.options)
    }
  }
</script>
