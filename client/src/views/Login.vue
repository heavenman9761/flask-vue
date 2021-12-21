<template>
    <b-container style="max-width:600px; margin-top:50px" fill-height>
        <b-alert
            :show="isLoginError"
            variant="danger">
            아이디와 비빌번호를 확인하세요.
        </b-alert>
        <b-alert :show="isLogin"
            variant="success">
            로그인이 완료되었습니다.
        </b-alert>
        <b-card
            header="Sign In"
            header-tag="header"
            footer=""
            footer-tag="footer"
            title=""
            >
            <b-container fluid>
            <b-row class="my-1" align-v="center">
                <b-col sm="12">
                    <label>메일주소와 비밀번호를 입력해주세요</label>
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
                        router :to="{ name: 'UserRegi' }">회원가입
                    </b-button>
                    <b-button
                        class="float-right"
                        href="#"
                        variant="primary"
                        style="margin-left:3px"
                        @click="login({ email: email, password: password })">Sign In
                    </b-button>
                    <b-button
                        class="float-right"
                        href="#"
                        variant="primary"
                        style="margin-left:3px"
                        @click="toServer()">getList
                    </b-button>
                    </div>
                </b-col>
            </b-row>
            </b-container>
        </b-card>
    </b-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import axios from 'axios';

export default {
  data() {
    return {
      email: null,
      password: null,
    };
  },
  methods: {
    ...mapActions(['login']),
    toServer() {
      const token = localStorage.getItem('access_token');
      const obj = { token };
      const path = 'http://localhost:5000/users/';
      axios.post(path, obj)
        .then((res) => { // this를 쓰기위해 콜백을 이렇게 써야 한다.
          if (res.status === 200) {
            console.log(res.data.users);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState(['isLogin', 'isLoginError']),
  },
};
</script>
