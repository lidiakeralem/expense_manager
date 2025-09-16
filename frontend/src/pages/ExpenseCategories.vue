<template>
  <div>
    <Navbar />

    <h2>Expense Categories</h2>
    <p>
      This page is used to manage your expense category. You can add, update and delete your expense category.
    </p>

    <!-- Button to show add form -->
    <button class="btn-add-toggle" @click="showAddForm = !showAddForm">
      {{ showAddForm ? "Cancel" : "Add Category" }}
    </button>

    <!-- Add Category Form -->
    <form v-if="showAddForm" @submit.prevent="addCategoryHandler" class="add-form">
      <input v-model="newCategory.category_name" placeholder="Category Name" required />
      <input v-model="newCategory.description" placeholder="Description" />
      <button class="btn-add" type="submit">Save Category</button>
    </form>

    <!-- Categories Table -->
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
            <button class="btn-update" @click="openUpdateModal(category)">Update</button>
            <button class="btn-delete" @click="deleteCategoryHandler(category.name)">Delete</button>
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
        <button class="btn-save" @click="saveUpdateCategory">Save</button>
        <button class="btn-cancel" @click="showUpdateModal = false">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  components: { Navbar },
  data() {
    return {
      newCategory: { category_name: '', description: '' },
      showAddForm: false,
      showUpdateModal: false,
      editCategory: null,
    }
  },
  computed: {
    ...mapGetters(['allExpenseCategories']),
    categories() {
      return this.allExpenseCategories
    },
  },
  methods: {
    ...mapActions([
      'fetchExpenseCategories',
      'addExpenseCategory',
      'updateExpenseCategory',
      'deleteExpenseCategory',
    ]),

    async addCategoryHandler() {
      await this.addExpenseCategory(this.newCategory)
      this.newCategory = { category_name: '', description: '' }
      this.showAddForm = false // hide form after saving
    },

    deleteCategoryHandler(name) {
      if (confirm('Are you sure?')) this.deleteExpenseCategory(name)
    },

    openUpdateModal(category) {
      this.editCategory = { ...category }
      this.showUpdateModal = true
    },

    async saveUpdateCategory() {
      await this.updateExpenseCategory(this.editCategory)
      this.showUpdateModal = false
    },
  },
  mounted() {
    this.fetchExpenseCategories()
  },
}
</script>


