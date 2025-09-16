<template>
  <div class="home">
    <Navbar />

    <h1 class="homepage">Welcome to Expense Manager</h1>
    <p class="description">
      Manage your expenses and categories efficiently using this app. Navigate through the the pages to add new expenses, 
      organize categories, and view detailed.
    </p>

    <!-- expense manager Summary -->
    <div class="dashboard">
      <div class="card">
        <h2>{{ totalExpenses }}</h2>
        <p>Total Expenses</p>
        <small>Number of expense records</small>
      </div>
      <div class="card">
        <h2>{{ totalAmount }}</h2>
        <p>Total expense amount in birr </p>
        <small>Sum of all expenses recorded in the system.</small>
      </div>
      <div class="card">
        <h2>{{ totalCategories }}</h2>
        <p>Expense Categories</p>
        <small>manage your expense categories on the categories page.</small>
      </div>
      <div class="card">
        <h2>Reports</h2>
        <small> View detail reports on the Reports page.</small>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  components: { Navbar },
  computed: {
    ...mapGetters(['allExpenses', 'allExpenseCategories']),
    totalExpenses() {
      return this.allExpenses ? this.allExpenses.length : 0;
    },
    totalAmount() {
      if (!this.allExpenses) return 0;
      return this.allExpenses.reduce((sum, e) => sum + Number(e.amount || 0), 0);
    },
    totalCategories() {
      return this.allExpenseCategories ? this.allExpenseCategories.length : 0;
    }
  },
  methods: {
    ...mapActions(['fetchExpenses', 'fetchExpenseCategories'])
  },
  mounted() {
    this.fetchExpenses();
    this.fetchExpenseCategories();
  }
};
</script>

<style scoped>
.home {
  padding: 20px;
  font-family: Arial, sans-serif;
}

.homepage {
  text-align: center;
  margin-bottom: 10px;
  color: #2c3e50;
}

.description {
  text-align: center;
  margin-bottom: 30px;
  color: #555;
  font-size: 1.1rem;
}

/* Dashboard Cards */
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: transform 0.2s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
}

.card h2 {
  margin: 0;
  font-size: 2rem;
  color: #3498db;
}

.card p {
  margin-top: 8px;
  font-size: 1.1rem;
  color: #333;
  font-weight: bold;
}

.card small {
  display: block;
  margin-top: 6px;
  font-size: 0.9rem;
  color: #777;
}
</style>
