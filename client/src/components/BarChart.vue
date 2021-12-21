<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  props: ['chartData', 'options'],
  mounted () {
    this.renderChart(this.chartData, this.options)
  },
  watch: { // this will be our flag for update
      'chartData.update_flag': function(new_val, old_val) {
          this.$data._chart.update();
      }
  },
}
</script>