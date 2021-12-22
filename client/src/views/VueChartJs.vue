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
        <line-chart v-bind:date="date" v-bind:gumak="gumak"></line-chart>
      </div>
      <div class="column">
        <h3>Bar Chart</h3>
        <bar-chart v-bind:date="date" v-bind:gumak="gumak"></bar-chart>
      </div>
    </div>
  </section>
</template>

<script>
  import axios from 'axios';
  import LineChart from '@/components/LineChart'
  import BarChart from '@/components/BarChart'
  export default {
    name: 'VueChartJS',
    components: {
      LineChart,
      BarChart,
    },
    data () {
      return {
        startDate: '2021-03-10',
        endDate: '2021-03-21',
        maeJangCode: '0101',
        payload: [],
        gumak: [],
        date: [],
      }
    },
    methods: {
      onContext(ctx) {
        this.formatted = ctx.selectedFormatted
        this.selected = ctx.selectedYMD
      },
      getData() {
        this.gumak = []
        this.date = []
        const path = 'http://localhost:5000/maechul/daymaechul';
        axios.post(path, {'token': localStorage.getItem('access_token'),
          'maeJangCode': this.maeJangCode,
          'startDate': this.startDate,
          'endDate': this.endDate})
        .then((res) => { // this를 쓰기위해 콜백을 이렇게 써야 한다.
          if (res.status === 200) {
            for (var i = 0; i <= res.data.datas.length - 1; i++) {
              this.gumak.push(res.data.datas[i].GumAk)
              this.date.push(res.data.datas[i].MaeChulDate)
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