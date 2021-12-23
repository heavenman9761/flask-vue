<template>
  <section class="container">
    <h1>Demo Charts</h1>
    <div class="columns">
      <div class="column">
        <b-input-group class="mb-3">
          <b-form-input
            id="example-input"
            v-model="startDate"
            type="text"
            placeholder="YYYY-MM-DD"
            autocomplete="off"
          ></b-form-input>
          <b-input-group-append>
            <b-form-datepicker
              v-model="startDate"
              button-only
              right
              locale="ko-KR"
              aria-controls="example-input"
              @context="onContext"
            ></b-form-datepicker>
          </b-input-group-append>
        </b-input-group>
      </div>
      <div class="column">
        <b-input-group class="mb-3">
          <b-form-input
            id="example-input1"
            v-model="endDate"
            type="text"
            placeholder="YYYY-MM-DD"
            autocomplete="off"
          ></b-form-input>
          <b-input-group-append>
            <b-form-datepicker
              v-model="endDate"
              button-only
              right
              locale="ko-KR"
              aria-controls="example-input"
              @context="onContext"
            ></b-form-datepicker>
          </b-input-group-append>
        </b-input-group>
      </div>
      <div class="column">
        <b-button
            class="float-right"
            variant="primary"
            style="margin-left:3px"
            @click="getData()">Get Data
        </b-button>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h3>Line Chart</h3>
        <line-chart v-bind:chart-data="datacollection"></line-chart>
      </div>
      <div class="column">
        <h3>Bar Chart</h3>
        <reactive v-bind:chart-data="datacollection"></reactive>
      </div>
    </div>
  </section>
</template>

<script>
  import axios from 'axios';
  import LineChart from '@/components/LineChart'
  import Reactive from '@/components/Reactive'
  export default {
    name: 'VueChartJS',
    components: {
      LineChart,
      Reactive
    },
    data () {
      return {
        startDate: '2021-03-10',
        endDate: '2021-03-21',
        maeJangCode: '0101',
        datacollection: null
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
              label: 'Data One',
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
      onContext(ctx) {
        this.formatted = ctx.selectedFormatted
        this.selected = ctx.selectedYMD
      },
      getData() {
        var gumak = []
        var date = []
        const path = 'http://localhost:5000/maechul/daymaechul';
        axios.post(path, {'token': localStorage.getItem('access_token'),
          'maeJangCode': this.maeJangCode,
          'startDate': this.startDate,
          'endDate': this.endDate})
        .then((res) => { // this를 쓰기위해 콜백을 이렇게 써야 한다.
          if (res.status === 200) {
            for (var i = 0; i <= res.data.datas.length - 1; i++) {
              gumak.push(res.data.datas[i].GumAk)
              date.push(res.data.datas[i].MaeChulDate)
            }

            this.datacollection = {
              labels: date,
              datasets: [{
                label: '일자별 매출',
                backgroundColor: '#f87979',
                // Data for the x-axis of the chart
                data: gumak
              }]
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
      }
    }
  }
</script>