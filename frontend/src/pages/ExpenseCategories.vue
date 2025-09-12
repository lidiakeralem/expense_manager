<template>
  <div>
    <Navbar />

    <h2>Expense Categories</h2>

    <!-- Add Category Form -->
    <form @submit.prevent="addCategoryHandler">
      <input v-model="newCategory.category_name" placeholder="Category Name" required />
      <input v-model="newCategory.description" placeholder="Description" />
      <button type="submit">Add Category</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>Category Name</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="category in categories" :key="category.name">
          <td>{{ category.category_name }}</td>
          <td>{{ category.description }}</td>
          <td>
            <button @click="openUpdateModal(category)">Update</button>
            <button @click="deleteCategoryHandler(category.name)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Update Modal -->
    <div v-if="showUpdateModal" class="modal">
      <div class="modal-content">
        <h3>Update Category</h3>
        <input v-model="editCategory.category_name" placeholder="Category Name" />
        <input v-model="editCategory.description" placeholder="Description" />
        <button @click="saveUpdateCategory">Save</button>
        <button @click="showUpdateModal = false">Cancel</button>
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
      newCategory: { category_name:'', description:'' },
      showUpdateModal: false,
      editCategory: null
    };
  },
  computed: {
    ...mapGetters(['allExpenseCategories']),
    categories() { return this.allExpenseCategories; }
  },
  methods: {
    ...mapActions(['fetchExpenseCategories','addExpenseCategory','updateExpenseCategory','deleteExpenseCategory']),

    async addCategoryHandler() {
      await this.addExpenseCategory(this.newCategory);
      this.newCategory = { category_name:'', description:'' };
    },

    deleteCategoryHandler(name) {
      if(confirm('Are you sure?')) this.deleteExpenseCategory(name);
    },

    openUpdateModal(category) {
      this.editCategory = { ...category };
      this.showUpdateModal = true;
    },

    async saveUpdateCategory() {
      await this.updateExpenseCategory(this.editCategory);
      this.showUpdateModal = false;
    }
  },
  mounted() {
    this.fetchExpenseCategories();
  }
};
</script>

<style>
.modal {
  position: fixed;
  top:0; left:0; width:100%; height:100%;
  background: rgba(0,0,0,0.5);
  display:flex; justify-content:center; align-items:center;
}
.modal-content {
  background:white; padding:20px; border-radius:5px; width:400px;
}
</style>
