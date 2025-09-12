<!-- <template>
  <div>
    <router-view />
  </div>
</template> -->

<template>
  <div id="app">
    <!-- Show nav only if user is logged in -->
    <nav v-if="isAuthenticated">
      <router-link to="/home">Home</router-link> |
      <router-link to="/expenses">Expenses</router-link> |
      <router-link to="/categories">Categories</router-link> |
      <router-link to="/report">Report</router-link> |
      <button @click="logout">Logout</button>
    </nav>

    <router-view />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
  methods: {
    ...mapActions(["logout"]),
  },
};
</script>

<style>
nav {
  padding: 10px;
  background: #f4f4f4;
  margin-bottom: 20px;
}

nav a {
  margin-right: 10px;
  text-decoration: none;
  color: #333;
}

button {
  cursor: pointer;
}
</style>
