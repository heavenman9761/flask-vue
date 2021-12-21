<template>
    <b-container style="max-width:600px; margin-top:50px" fill-height>
        <b-card
            header="User Register"
            header-tag="header"
            footer=""
            footer-tag="footer"
            title=""
            >
            <b-container fluid>
            <b-row class="my-1" align-v="center">
                <b-col sm="12">
                    <label>회원정보를 입력해주세요</label>
                </b-col>
            </b-row>
            <b-row class="my-1" align-v="center">
                <b-col sm="3">
                <label for="input-none">email:</label>
                </b-col>
                <b-col sm="9">
                <b-form-input id="input-none" :state="null"
                    placeholder="input your email" autofocus v-model="email"></b-form-input>
                </b-col>
            </b-row>

            <b-row class="my-1" align-v="center">
                <b-col sm="3">
                <label for="input-none">name:</label>
                </b-col>
                <b-col sm="9">
                <b-form-input id="input-none" :state="null"
                    placeholder="input your name" v-model="name"
                    ></b-form-input>
                </b-col>
            </b-row>

            <b-row class="my-1" align-v="center">
                <b-col sm="3">
                <label for="input-none">password:</label>
                </b-col>
                <b-col sm="9">
                <b-form-input id="input-none" :state="null"
                    placeholder="input your password" v-model="password"
                    type="password"></b-form-input>
                </b-col>
            </b-row>

            <b-row class="my-1">
                <b-col sm="12">
                    <div>
                    <b-button
                        class="float-right"
                        href="#"
                        variant="success"
                        style="margin-left:3px"
                        @click="toServer()">가입하기
                    </b-button>
                    </div>
                </b-col>
            </b-row>
            </b-container>
        </b-card>
    </b-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: null,
      name: null,
      password: null,
    };
  },
  methods: {
    toServer() {
      axios.post('http://localhost:5000/users/regi', { email: this.email, name: this.name, password: this.password })
        .then((res) => { // this를 쓰기위해 콜백을 이렇게 써야 한다.
        // let data = res.data;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {

  },
};
</script>
