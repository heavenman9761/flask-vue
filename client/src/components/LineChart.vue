<script>
  import { Line } from 'vue-chartjs'

  export default {
    extends: Line,
    props: {
      date: {
          type: Array
      },
      gumak: {
        type: Array
      }
    },
    data () {
      return {
        chartData: {
          labels: this.date,
          datasets: [
            {
              label: '일별매출',
              backgroundColor: '#B71C1C',
              pointBackgroundColor: '#B71C1C',
              borderWidth: 2,
              pointBorderColor: '#EF9A9A',
              pointBackgroundColor: '#EF9A9A',
              data: this.gumak,
              fill: false
            }
          ]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
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
    watch: {
      date: function() {
        // this.renderChart(this.chartData, this.options)
        update()
      }
    },
    mounted () {
      this.renderChart(this.chartData, this.options)
    },
  }
</script>
