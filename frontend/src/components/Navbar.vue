<template>
  <nav class="navbar">
    <div class="logo">
      <h2>Expense Manager</h2>
    </div>

    <ul class="nav-links" v-if="isLoggedIn">
      <li :class="{ active: currentRoute === '/home' }">
        <router-link to="/home">Home</router-link>
      </li>
      <li :class="{ active: currentRoute === '/expenses' }">
        <router-link to="/expenses">Expenses</router-link>
      </li>
      <li :class="{ active: currentRoute === '/expense-categories' }">
        <router-link to="/expense-categories">Categories</router-link>
      </li>
      <li :class="{ active: currentRoute === '/expense-reports' }">
        <router-link to="/expense-reports">Reports</router-link>
      </li>
      <li>
        <button class="logout-btn" @click="logout">Logout</button>
      </li>
    </ul>

    <div v-else>
      <router-link to="/login">Login</router-link>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';

export default {
  computed: {
    ...mapGetters(['isLoggedIn']),
    currentRoute() {
      return this.$route.path;
    }
  },
  methods: {
    ...mapMutations(['setLoggedIn']),
    logout() {
      if (confirm('Are you sure you want to logout?')) {
        this.setLoggedIn(false);
        this.$router.push('/login');
      }
    }
  }
};
</script>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #a2c2d1;
  color: #fff;
}
.navbar .nav-links {
  list-style: none;
  display: flex;
  gap: 15px;
  margin: 0;
  padding: 0;
}
.navbar .nav-links li {
  margin: 0;
}
.navbar .nav-links li a {
  color: #fff;
  text-decoration: none;
}
.navbar .nav-links li.active a {
  font-weight: bold;
  text-decoration: underline;
}
.logout-btn {
  background-color: #e53e3e;
  border: none;
  color: #fff;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}
.logout-btn:hover {
  background-color: #c53030;
}
.logo h2 {
  margin: 0;
}
</style>
