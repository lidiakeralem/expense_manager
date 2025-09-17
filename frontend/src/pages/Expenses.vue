<template>
  <div>
    <Navbar />

    <h2>Expenses</h2>
    <p>This page is used to manage your expenses. You can add, update and delete expenses.</p>

    <!-- Toggle Add Expense Form -->
    <button class="btn-add-toggle" @click="showAddForm = !showAddForm">
      {{ showAddForm ? "Cancel" : "Add Expense" }}
    </button>

    <!-- Add Expense Form -->
    <form v-if="showAddForm" @submit.prevent="addExpenseHandler" class="add-form">
      <input v-model="newExpense.employee_name" placeholder="Employee Name" required />
      <input v-model="newExpense.expense_date" type="date" required />
      <input v-model="newExpense.amount" type="number" placeholder="Amount in birr" required />

      <select v-model="newExpense.payment_method">
        <option disabled value=""> Select Payment Method</option>
        <option v-for="m in paymentMethods" :key="m" :value="m">{{ m }}</option> 
      </select>

      <select v-model="newExpense.category">
        <option disabled value="">Select Expense Category</option>
        <option v-for="c in categories" :key="c.name" :value="c.name">{{ c.category_name }}</option>
      </select>

      <input v-model="newExpense.description" placeholder="Description" />
      <button class="btn-add" type="submit">Save Expense</button>
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
          <td>{{ expense.expense_date }}</td>
          <td>{{ expense.employee_name }}</td>
          <td>{{ expense.amount }}</td>
          <td>{{ expense.payment_method }}</td>
          <td>{{ expense.category }}</td>
          <td>{{ expense.description }}</td>
          <td>
            <button class="btn-update" @click="openUpdateModal(expense)">Update</button>
            <button class="btn-delete" @click="deleteExpenseHandler(expense.name)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Update Modal -->
    <div v-if="showUpdateModal" class="modal">
      <div class="modal-content">
        <h3>Update Expense</h3>

        <input v-model="editExpense.employee_name" placeholder="Employee Name" />
        <input v-model="editExpense.expense_date" type="date" />
        <input v-model="editExpense.amount" type="number" placeholder="Amount" />

        <select v-model="editExpense.payment_method">
          <option v-for="m in paymentMethods" :key="m" :value="m">{{ m }}</option>
        </select>

        <select v-model="editExpense.category">
          <option v-for="c in categories" :key="c.name" :value="c.name">{{ c.category_name }}</option>
        </select>

        <input v-model="editExpense.description" placeholder="Description" />

        <button class="btn-save" @click="saveUpdateExpense">Save</button>
        <button class="btn-cancel" @click="showUpdateModal = false">Cancel</button>
      </div>
    </div>
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
        payment_method: '',
        category: '',
        description: ''
      },
      showAddForm: false,   // ✅ toggle for Add form
      showUpdateModal: false,
      editExpense: null
    };
  },
  computed: {
    ...mapGetters(['allExpenses', 'allExpenseCategories', 'allPaymentMethods']),
    expenses() { return this.allExpenses; },
    categories() { return this.allExpenseCategories; },
    paymentMethods() { return this.allPaymentMethods; }
  },
  methods: {
    ...mapActions([
      'fetchExpenses', 'addExpense', 'updateExpense', 'deleteExpense', 'fetchExpenseCategories', 'fetchPaymentMethods'
    ]),
    async addExpenseHandler() {
      if (!this.newExpense.payment_method && this.paymentMethods.length) {
        this.newExpense.payment_method = this.paymentMethods[0];
      }
      await this.addExpense(this.newExpense);
      this.newExpense = { employee_name:'', expense_date:'', amount:'', payment_method:'', category:'', description:'' };
      this.showAddForm = false;  // ✅ hide form after save
    },
    deleteExpenseHandler(name) {
      if(confirm('Are you sure?')) this.deleteExpense(name);
    },
    openUpdateModal(expense) {
      this.editExpense = { ...expense };
      this.showUpdateModal = true;
    },
    async saveUpdateExpense() {
      await this.updateExpense(this.editExpense);
      this.showUpdateModal = false;
    }
  },
  mounted() {
    this.fetchExpenses();
    this.fetchExpenseCategories();
    this.fetchPaymentMethods();
  }
};
</script>

<!-- <style>
.add-form {
  display: flex;
  flex-direction: column;
  gap: 12px; /* space between fields */
  max-width: 400px;
  margin: 20px 0;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f9f9f9;
}

.add-form input,
.add-form select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.add-form input:focus,
.add-form select:focus {
  border-color: cornflowerblue;
  box-shadow: 0 0 5px rgba(100, 149, 237, 0.5);
  outline: none;
}

.btn-add {
  padding: 10px;
  background-color: cornflowerblue;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-add:hover {
  background-color: royalblue;
}

.btn-add-toggle {
  margin-bottom: 10px;
  background: seagreen;
  color: white;
  padding: 8px 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.modal {
  position: fixed;
  top:0; left:0; width:100%; height:100%;
  background: rgba(0,0,0,0.5);
  display:flex; justify-content:center; align-items:center;
}
.modal-content {
  background:white; padding:20px; border-radius:5px; width:400px;
}
/* .btn-add {
  border: none;
  background-color: cornflowerblue;
  border-radius: 5px;
  padding: 8px 14px;
  color: white;
} */
.btn-update {
  color: blueviolet;
  border-radius: 1px;
  padding: 8px 14px;
}
.btn-delete {
  color: chocolate;
  border-radius: 1px;
  padding: 8px 14px;
}
.btn-save {
  color: rgb(107, 24, 240);
  padding: 3px 7px;
}
.btn-cancel {
  color: rgb(192, 60, 60);
  padding: 3px 7px;
}
</style> -->



<style>
/* ✅ Add Expense Form */
.add-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 420px;
  margin: 20px 0;
  padding: 16px;
  border: 1px solid #e5e5e5;
  border-radius: 8px;
  background: #fafafa;
}

.add-form input,
.add-form select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}
.add-form input:focus,
.add-form select:focus {
  border-color: #888;
  outline: none;
}

/* ✅ Buttons */
button {
  cursor: pointer;
  font-size: 14px;
}

.btn-add {
  padding: 8px 14px;
  background: #4a6fa5; /* muted blue */
  color: white;
  border: none;
  border-radius: 6px;
}
.btn-add:hover { background: #3a5a85; }

.btn-add-toggle {
  margin-bottom: 15px;
  background: #6b7280; /* neutral gray */
  color: white;
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
}
.btn-add-toggle:hover { background: #4b5563; }

.btn-update {
  color: rgb(95, 55, 241);
  border: none;
  border-radius: 6px;
  padding: 6px 12px;
}
.btn-update:hover { background: #4b5563; }

.btn-delete {
  color: rgb(241, 86, 86);
  border: none;
  border-radius: 6px;
  padding: 6px 12px;
}
.btn-delete:hover { background: #991b1b; }

.btn-save {
  background: #4a6fa5;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px 14px;
}
.btn-cancel {
  background: #9ca3af; /* soft gray */
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px 14px;
  margin-left: 8px;
}

/* ✅ Expense List Table */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background: #fff;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid #e5e5e5;
}
thead {
  background: #f3f4f6; /* light gray */
  color: #111827;      /* dark gray text */
}
th, td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #e5e5e5;
}
tbody tr:nth-child(even) {
  background: #fafafa;
}
tbody tr:hover {
  background: #f1f5f9;
}

/* ✅ Update Modal */
.modal {
  position: fixed;
  top:0; left:0; width:100%; height:100%;
  background: rgba(0,0,0,0.4);
  display:flex; justify-content:center; align-items:center;
}
.modal-content {
  background:white;
  padding: 20px;
  border-radius: 8px;
  width: 420px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.modal-content input,
.modal-content select {
  width: 100%;
  padding: 10px;
  margin-bottom: 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}
</style>

