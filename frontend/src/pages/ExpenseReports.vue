<template>
  <div>
    <Navbar />
    <h1>Expense Reports</h1>
    <table border="1" cellpadding="5">
      <thead>
        <tr>
          <th>Date</th><th>Employee</th><th>Amount</th><th>Payment</th><th>Category</th><th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="exp in reports" :key="exp.name">
          <td>{{ exp.expense_date }}</td>
          <td>{{ exp.employee_name }}</td>
          <td>{{ exp.amount }}</td>
          <td>{{ exp.payment_method }}</td>
          <td>{{ exp.category }}</td>
          <td>{{ exp.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  components:{Navbar},
  computed:{...mapGetters({reports:'allExpenseReports'})},
  methods:{...mapActions(['fetchExpenseReports'])},
  async mounted(){ await this.fetchExpenseReports(); setInterval(()=>this.fetchExpenseReports(),5000); }
};
</script>
