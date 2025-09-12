<template>
  <div>
    <Navbar />

    <h2>Expenses</h2>

    <!-- Add Expense Form -->
    <form @submit.prevent="addExpenseHandler">
      <input v-model="newExpense.employee_name" placeholder="Employee Name" required />
      <input v-model="newExpense.expense_date" type="date" required />
      <input v-model="newExpense.amount" type="number" placeholder="Amount" required />
      <select v-model="newExpense.payment_method">
        <option>Cash</option>
        <option>Card</option>
        <option>Other</option>
      </select>
      <select v-model="newExpense.category">
        <option v-for="c in categories" :key="c.name" :value="c.name">{{ c.category_name }}</option>
      </select>
      <input v-model="newExpense.description" placeholder="Description" />
      <button type="submit">Add Expense</button>
    </form>

    <!-- Expenses Table -->
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Employee</th>
          <th>Amount</th>
          <th>Payment Method</th>
          <th>Category</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="expense in expenses" :key="expense.name">
          <td><input v-model="expense.expense_date" type="date" /></td>
          <td><input v-model="expense.employee_name" /></td>
          <td><input v-model="expense.amount" type="number" /></td>
          <td>
            <select v-model="expense.payment_method">
              <option>Cash</option>
              <option>Card</option>
              <option>Other</option>
            </select>
          </td>
          <td>
            <select v-model="expense.category">
              <option v-for="c in categories" :key="c.name" :value="c.name">{{ c.category_name }}</option>
            </select>
          </td>
          <td><input v-model="expense.description" /></td>
          <td>
            <button @click="updateExpenseHandler(expense)">Update</button>
            <button @click="deleteExpenseHandler(expense.name)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  components: { Navbar },
  data() {
    return {
      newExpense: {
        employee_name: '',
        expense_date: '',
        amount: '',
        payment_method: 'Cash',
        category: '',
        description: ''
      }
    };
  },
  computed: {
    ...mapGetters(['allExpenses', 'allExpenseCategories']),
    expenses() { return this.allExpenses; },
    categories() { return this.allExpenseCategories; }
  },
  methods: {
    ...mapActions([
      'fetchExpenses', 'addExpense', 'updateExpense', 'deleteExpense', 'fetchExpenseCategories'
    ]),
    async addExpenseHandler() {
      await this.addExpense(this.newExpense);
      this.newExpense = { employee_name:'', expense_date:'', amount:'', payment_method:'Cash', category:'', description:'' };
    },
    updateExpenseHandler(expense) {
      this.updateExpense(expense);
    },
    deleteExpenseHandler(name) {
      if(confirm('Are you sure?')) this.deleteExpense(name);
    }
  },
  mounted() {
    this.fetchExpenses();
    this.fetchExpenseCategories();
  }
};
</script>
