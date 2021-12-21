import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../router';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: null,
    isLogin: false,
    isLoginError: false,
  },
  mutations: {
    // 로그인이 성공했을때,
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    // 로그인이 실패했을때
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = true;
    },
    logout(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
  },
  actions: {
    // 로그인 시도
    login({ commit }, loginObj) {
      const path = 'http://localhost:5000/users/login';
      axios.post(path, loginObj)
        .then((res) => { // this를 쓰기위해 콜백을 이렇게 써야 한다.
          if (res.status === 200) {
            const { token } = res.data;
            localStorage.setItem('access_token', token);
            const userInfo = {
              userid: res.data.userid,
              name: res.data.name,
            };

            // dispatch("getMemberInfo", res.data);
            commit('loginSuccess', userInfo);
          } else {
            commit('loginError');
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },

    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('access_token');
      router.push('/');
    },

    // getMemberInfo({commit}, userData) {
    //   let token = localStorage.getItem("access_token");
    //   let config = {
    //     "access-token": token
    //   }

    //   axios.post('api/users/2', config)
    //     .then(response => {
    //       let userInfo = {
    //         first_name: response.data.data.first_name,
    //         last_name: response.data.data.last_name,
    //         avatar: response.data.data.avatar,
    //         email: response.data.data.email,
    //         id: response.data.data.id
    //       }
    //       commit("loginSuccess", userInfo)
    //     })
    //     .catch(() => {
    //       commit("loginError")
    //     });
    // }
  },
  modules: {
  },
});
