<template>
  <div class="login-container">
    <h1>Login</h1>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">{{ loading ? 'Logging in...' : 'Login' }}</button>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import { mapMutations } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      error: ''
    };
  },
  methods: {
    ...mapMutations(['setLoggedIn']),
    async login() {
      this.loading = true;
      this.error = '';
      try {
        const response = await axios.post('http://expensesite.localhost:8002/api/method/login', {
          usr: this.username,
          pwd: this.password
        }, { withCredentials: true });

        if (response.data.message === 'Logged In') {
          this.setLoggedIn(true);
          this.$router.push('/home');
        } else {
          this.error = 'Invalid username or password';
        }
      } catch (err) {
        this.error = 'Login failed';
        console.error(err);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 30px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}
.login-container input {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
}
.error { color: red; margin-top: 10px; }
</style>
