<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  props: {
    date: {
      type: Array,
    },
    gumak: {
      type: Array,
    }
  },
  data() {
    return {
      chartData: {
        labels: this.date,
        datasets: [
          {
            label: '일별매출',
            backgroundColor: '#f87979',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            data:this.gumak
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
      this.renderChart(this.chartData, this.options)
    }
  },
}
</script>