<template>
  <section class="container">
    <h1>Demo examples of vue-chartjs</h1>
    <b-button
          class="float-right"
          variant="primary"
          style="margin-left:3px"
          @click="getData()">xxx
      </b-button>
    <div class="columns">
      <div class="column">
        <h3>Line Chart</h3>
        <!-- <line-chart v-bind:chartdata="bardatacollection"></line-chart> -->
      </div>
      <div class="column">
        <h3>Bar Chart</h3>
        <bar-chart v-bind:chart-data="bardatacollection" v-bind:options="barchartoptions"></bar-chart>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h3>Bubble Chart</h3>
        <!-- <bubble-chart></bubble-chart> -->
      </div>
      <div class="column">
        <h3>Reactivity - Live update upon change in datasets</h3>
        <!-- <reactive :chart-data="datacollection"></reactive>
        <button class="button is-primary" @click="fillData()">Randomize</button> -->
      </div>
    </div>
  </section>
</template>

<script>
  import axios from 'axios';
  // import LineChart from '@/components/LineChart'
  import BarChart from '@/components/BarChart'
  // import BubbleChart from '@/components/BubbleChart'
  // import Reactive from '@/components/Reactive'
  export default {
    name: 'VueChartJS',
    components: {
      // LineChart,
      BarChart,
      // BubbleChart,
      // Reactive
    },
    data () {
      return {
        startDate: '2021-03-10',
        endDate: '2021-03-21',
        maeJangCode: '0101',
        payload: [],
        datacollection: null,
        bardatacollection: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              pointBackgroundColor: 'white',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              data: [40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100]
            }
          ]
        },
        barchartoptions: {
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
    created () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          datasets: [
            {
              label: 'Data Two',
              backgroundColor: '#f87979',
              // Data for the x-axis of the chart
              data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
            }
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      },
      getData() {
        const path = 'http://localhost:5000/maechul/daymaechul';
        axios.post(path, {'token': localStorage.getItem('access_token'),
            'maeJangCode': this.maeJangCode,
            'startDate': this.startDate,
            'endDate': this.endDate})
          .then((res) => { // this를 쓰기위해 콜백을 이렇게 써야 한다.
            if (res.status === 200) {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    }
  }
</script>