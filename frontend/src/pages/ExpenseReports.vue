<template>
  <div>
    <Navbar />
    <h1>Expense Reports</h1>

    <!-- Filters -->
    <div class="filters">
      <label>
        From:
        <input type="date" v-model="filters.startDate" />
      </label>
      <label>
        To:
        <input type="date" v-model="filters.endDate" />
      </label>
      <label>
        Category:
        <select v-model="filters.category">
          <option value="">All</option>
          <option v-for="c in categories" :key="c.name" :value="c.name">
            {{ c.category_name }}
          </option>
        </select>
      </label>
      <!-- <button class="btn-filter" @click="applyFilters">Apply Filters</button> -->
      <button class="btn-reset" @click="resetFilters">Reset Filters</button>
    </div>

    <!-- Report Table -->
    <table border="1" cellpadding="5">
      <thead>
        <tr>
          <th>Date</th>
          <th>Employee</th>
          <th>Amount</th>
          <th>Payment</th>
          <th>Category</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="exp in filteredReports" :key="exp.name">
          <td>{{ exp.expense_date }}</td>
          <td>{{ exp.employee_name }}</td>
          <td>{{ exp.amount }}</td>
          <td>{{ exp.payment_method }}</td>
          <td>{{ exp.category }}</td>
          <td>{{ exp.description }}</td>
        </tr>
      </tbody>
    </table>

    <!-- Totals -->
    <div class="totals">
      <h3>Total Expenses: {{ totalExpenses }}</h3>
    </div>

    <!-- Chart -->
    <div class="chart-container">
      <h4>Expenses by Category</h4>
      <Bar :data="categoryChartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import { mapGetters, mapActions } from 'vuex';

// Import vue-chartjs + Chart.js
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  components: { Navbar, Bar },
  data() {
    return {
      filters: { startDate: '', endDate: '', category: '' },
      chartOptions: {
        responsive: true,
        plugins: {
          legend: { display: false },
          title: { display: true, text: 'Expense Amounts per Expense Category' }
        }
      }
    };
  },
  computed: {
    ...mapGetters({
      reports: 'allExpenseReports',
      categories: 'allExpenseCategories'
    }),
    filteredReports() {
      return this.reports.filter(exp => {
        const dateOk =
          (!this.filters.startDate || exp.expense_date >= this.filters.startDate) &&
          (!this.filters.endDate || exp.expense_date <= this.filters.endDate);
        const categoryOk = !this.filters.category || exp.category === this.filters.category;
        return dateOk && categoryOk;
      });
    },
    totalExpenses() {
      return this.filteredReports.reduce((sum, exp) => sum + Number(exp.amount), 0);
    },
    categoryTotals() {
      const totals = {};
      this.filteredReports.forEach(exp => {
        totals[exp.category] = (totals[exp.category] || 0) + Number(exp.amount);
      });
      return totals;
    },
    categoryChartData() {
      return {
        labels: Object.keys(this.categoryTotals),
        datasets: [
          {
            label: 'Amount',
            backgroundColor: '#3498db',
            data: Object.values(this.categoryTotals)
          }
        ]
      };
    }
  },
  methods: {
    ...mapActions(['fetchExpenseReports', 'fetchExpenseCategories']),
    applyFilters() {
      // reactive already
    },
    resetFilters() {
      this.filters = { startDate: '', endDate: '', category: '' };
    }
  },
  async mounted() {
    await this.fetchExpenseReports();
    await this.fetchExpenseCategories();
    setInterval(() => this.fetchExpenseReports(), 5000);
  }
};
</script>

<style scoped>
.filters {
  margin-bottom: 20px;
  padding: 10px;
  background: #f4f4f4;
  border-radius: 6px;
  display: flex;
  gap: 15px;
  align-items: center;
}

.chart-container {
  margin-top: 30px;
  height: 400px;
}
</style>
