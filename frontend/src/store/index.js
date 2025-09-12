import { createStore } from 'vuex';
import axios from 'axios';

axios.defaults.baseURL = 'http://expensesite.localhost:8002/api/method/'; // Frappe backend
axios.defaults.withCredentials = true; // use session cookies

export default createStore({
    state: {
        isLoggedIn: false,
        expenses: [],
        expenseCategories: [],
        expenseReports: []
    },
    getters: {
        isLoggedIn: state => state.isLoggedIn,
        allExpenses: state => state.expenses,
        allExpenseCategories: state => state.expenseCategories,
        allExpenseReports: state => state.expenseReports
    },
    mutations: {
        setLoggedIn(state, value) { state.isLoggedIn = value; },
        setExpenses(state, expenses) { state.expenses = expenses; },
        setExpenseCategories(state, categories) { state.expenseCategories = categories; },
        setExpenseReports(state, reports) { state.expenseReports = reports; }
    },
    actions: {
        // ========== EXPENSES ==========
        async fetchExpenses({ commit }) {
            try {
                const res = await axios.get('expense_manager.api.get_expenses');
                commit('setExpenses', res.data.message || res.data);
            } catch (err) { console.error(err); }
        },
        async addExpense({ dispatch }, expense) {
            try {
                await axios.post('expense_manager.api.create_expense', expense);
                dispatch('fetchExpenses'); // refresh list
            } catch (err) { console.error(err); }
        },
        async updateExpense({ dispatch }, expense) {
            try {
                await axios.post('expense_manager.api.update_expense', expense);
                dispatch('fetchExpenses');
            } catch (err) { console.error(err); }
        },
        async deleteExpense({ dispatch }, name) {
            try {
                await axios.post('expense_manager.api.delete_expense', { name });
                dispatch('fetchExpenses');
            } catch (err) { console.error(err); }
        },

        // ========== EXPENSE CATEGORIES ==========
        async fetchExpenseCategories({ commit }) {
            try {
                const res = await axios.get('expense_manager.api.get_expenseCategories');
                commit('setExpenseCategories', res.data.message || res.data);
            } catch (err) { console.error(err); }
        },
        async addExpenseCategory({ dispatch }, category) {
            try {
                await axios.post('expense_manager.api.create_expenseCategory', category);
                dispatch('fetchExpenseCategories');
            } catch (err) { console.error(err); }
        },
        async updateExpenseCategory({ dispatch }, category) {
            try {
                await axios.post('expense_manager.api.update_expenseCategory', category);
                dispatch('fetchExpenseCategories');
            } catch (err) { console.error(err); }
        },
        async deleteExpenseCategory({ dispatch }, name) {
            try {
                await axios.post('expense_manager.api.delete_expenseCategory', { name });
                dispatch('fetchExpenseCategories');
            } catch (err) { console.error(err); }
        },

        // ========== EXPENSE REPORTS ==========
        async fetchExpenseReports({ commit }) {
            try {
                const res = await axios.get('expense_manager.api.get_expenses'); // using same as expenses
                commit('setExpenseReports', res.data.message || res.data);
            } catch (err) { console.error(err); }
        }
    }
});
