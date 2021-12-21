<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand router :to="{ name: 'Home' }">IOT middleware</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">User</b-nav-item>
        <b-nav-item href="#">Gateway</b-nav-item>
        <b-nav-item href="#">Band</b-nav-item>
        <b-nav-item href="#">Pee Detector</b-nav-item>
        <b-nav-item href="#">IAQ</b-nav-item>
        <b-nav-item router :to="{ name: 'Books' }">Books</b-nav-item>
        <b-nav-item router :to="{ name: 'DayMaeChul' }">일별매출</b-nav-item>
        <b-nav-item router :to="{ name: 'VueChartJs' }">VueChart</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item v-if="!isLogin" router :to="{ name: 'Login' }" right>Sign In</b-nav-item>
        <b-nav-item-dropdown v-else right>
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item router :to="{ name: 'Profile' }">Profile</b-dropdown-item>
          <b-dropdown-item @click="logout">SignOut</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
    </b-navbar>

    <router-view/>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'App',

  data: () => ({
    drawer: null,
  }),
  computed: {
    ...mapState(['isLogin']),
  },
  methods: {
    ...mapActions(['logout']),
  },
  mounted() {
    this.$socket.on('respose', (data) => {
      console.log(data)
    }),
    this.$socket.on('iotdata', (data) => {
      console.log(data)
    })
  },
};
</script>

<style>
#app {
  margin-top: 0px
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
