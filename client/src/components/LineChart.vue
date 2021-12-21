<script>
  import { Line } from 'vue-chartjs'
  export default {
    extends: Line,
    data () {
      return {
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
    props: ['datacollection'],
    mounted () {
      this.renderChart(this.datacollection, this.options)
    }
  }
</script>