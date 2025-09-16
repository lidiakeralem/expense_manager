<template>
  <div class="login-container">
    <h1>Welcome to Expense Manager</h1>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">{{ loading ? 'Logging in...' : 'Login' }}</button>
    <p v-if="error" class="error">{{ error }}</p>
  </div>

  <!-- Forgot Password link -->
  <div class="forgotpwd">
    <button @click="showForgotModal = true">Forgot Password?</button>
  </div>

  <!-- Forgot Password Modal -->
  <div v-if="showForgotModal" class="modal-overlay">
    <div class="modal">
      <h3>Forgot Password</h3>

      <!-- Email + Send + Cancel in one row -->
      <div class="forgot-row">
        <input v-model="forgotEmail" placeholder="Enter your email" />
        <button class="send-btn" @click="sendResetLink" :disabled="loadingForgot">
          {{ loadingForgot ? 'Sending...' : 'Send' }}
        </button>
        <button class="cancel-btn" @click="closeModal">Cancel</button>
      </div>

      <p v-if="forgotMessage" :class="{'success': forgotSuccess, 'error': !forgotSuccess}">
        {{ forgotMessage }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      loading: false,
      error: "",
      showForgotModal: false,
      forgotEmail: "",
      loadingForgot: false,
      forgotMessage: "",
      forgotSuccess: false,
    };
  },
  methods: {
    ...mapMutations(["setLoggedIn"]),
    async login() {
      this.loading = true;
      this.error = "";
      try {
        const response = await axios.post(
          "http://expensesite.localhost:8002/api/method/login",
          { usr: this.username, pwd: this.password },
          { withCredentials: true }
        );

        if (response.data.message === "Logged In") {
          this.setLoggedIn(true);
          this.$router.push("/home");
        } else {
          this.error = "Invalid username or password";
        }
      } catch (err) {
        this.error = "Login failed";
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    closeModal() {
      this.showForgotModal = false;
      this.forgotEmail = "";
      this.forgotMessage = "";
      this.forgotSuccess = false;
    },

    sendResetLink() {
      if (!this.forgotEmail) {
        this.forgotMessage = "Please enter your email";
        this.forgotSuccess = false;
        return;
      }

      this.loadingForgot = true;
      this.forgotMessage = "";

      axios
        .post(
          "http://expensesite.localhost:8002/api/method/frappe.core.doctype.user.user.reset_password",
          { user: this.forgotEmail },
          { headers: { "Content-Type": "application/json" }, withCredentials: true }
        )
        .then(() => {
          this.forgotMessage = "Reset link has been sent to your email.";
          this.forgotSuccess = true;

          setTimeout(() => this.closeModal(), 3000);
        })
        .catch(() => {
          this.forgotMessage = "Failed to send reset link. Please try again.";
          this.forgotSuccess = false;
        })
        .finally(() => {
          this.loadingForgot = false;
        });
    },
  },
};
</script>

<style>
/* --- Login Container --- */
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 30px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: #ffffff;
  box-shadow: 0 4px 8px rgba(0,0,0,0.05);
  text-align: center;
}

.login-container h1 {
  margin-bottom: 20px;
  color: #1f2937;
  font-size: 22px;
  font-weight: 600;
}

.login-container input {
  width: 100%;
  padding: 12px;
  margin: 8px 0;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 14px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.login-container input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
  outline: none;
}

.login-container button {
  width: 100%;
  padding: 12px;
  margin-top: 12px;
  background: #2563eb;
  color: #fff;
  font-size: 15px;
  font-weight: 500;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.login-container button:hover {
  background: #1d4ed8;
}

/* --- Modal Overlay (center everything) --- */
.forgotpwd {
  margin-top: 15px;
  text-align: center; 
  color: #1d4ed8;
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

/* --- Modal Box --- */
.modal {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  min-width: 280px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.modal h3 {
  margin-bottom: 12px;
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
}

/* --- Forgot Row (email + buttons in one row, centered) --- */
.forgot-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

/* Small email field */
.forgot-row input {
  width: 160px;
  padding: 6px;
  font-size: 13px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
}

/* Buttons */
.forgot-row button {
  padding: 6px 12px;
  font-size: 13px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.2s ease;
}

/* Send button styled */
.forgot-row .send-btn {
  background: #2563eb;
  color: white;
  border: 1px solid #1d4ed8;
}
.forgot-row .send-btn:hover {
  background: #1d4ed8;
}

/* Cancel button styled */
.forgot-row .cancel-btn {
  background: #f9fafb;
  color: #374151;
  border: 1px solid #d1d5db;
}
.forgot-row .cancel-btn:hover {
  background: #e5e7eb;
}

/* --- Messages --- */
.success { color: green; margin-top: 10px; font-size: 13px; }
.error { color: red; margin-top: 10px; font-size: 13px; }
</style>
