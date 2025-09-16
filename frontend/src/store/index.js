import { createStore } from 'vuex';
import axios from 'axios';

axios.defaults.baseURL = 'http://expensesite.localhost:8002/api/method/'; // Frappe backend
axios.defaults.withCredentials = true; // use session cookies

// Attach CSRF token header for POST/PUT/DELETE to avoid 417
axios.interceptors.request.use((config) => {
    const needsCsrf = ['post', 'put', 'patch', 'delete'].includes((config.method || '').toLowerCase());
    if (needsCsrf) {
        const csrf = (document.cookie.match(/(^|; )frappe-csrf-token=([^;]*)/) || [])[2];
        if (csrf) {
            config.headers = config.headers || {};
            config.headers['X-Frappe-CSRF-Token'] = decodeURIComponent(csrf);
        }
    }
    return config;
});

export default createStore({
    state: {
        isLoggedIn: false,
        expenses: [],
        expenseCategories: [],
        expenseReports: [],
        paymentMethods: []
    },
    getters: {
        isLoggedIn: state => state.isLoggedIn,
        allExpenses: state => state.expenses,
        allExpenseCategories: state => state.expenseCategories,
        allExpenseReports: state => state.expenseReports,
        allPaymentMethods: state => state.paymentMethods
    },
    mutations: {
        setLoggedIn(state, value) { state.isLoggedIn = value; },
        setExpenses(state, expenses) { state.expenses = expenses; },
        setExpenseCategories(state, categories) { state.expenseCategories = categories; },
        setExpenseReports(state, reports) { state.expenseReports = reports; },
        setPaymentMethods(state, methods) { state.paymentMethods = methods; }
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
        },

        // // ========== PAYMENT METHODS from DocType ==========
        async fetchPaymentMethods({ commit, state }) {
            const fallbackDefaults = ['Cash', 'Card', 'Bank', 'Mobile Wallet', 'Other'];
            try {
                const base = axios.defaults.baseURL?.replace(/\/api\/method\/$/, '') || 'http://expensesite.localhost:8002';
                const candidateDoctypes = ['Expense', 'Expenses', 'Expense Manager', 'Expense Entry'];
                let options = [];
                for (const doctype of candidateDoctypes) {
                    try {
                        const url = `${base}/api/resource/DocType/${encodeURIComponent(doctype)}`;
                        const res = await axios.get(url);
                        const doc = (res.data && res.data.data) || (res.data && res.data.message);
                        const fields = (doc && doc.fields) || [];
                        const pm = fields.find(f => f.fieldname === 'payment_method');
                        if (pm && pm.options) {
                            options = pm.options.split('\n').map(s => s.trim()).filter(Boolean);
                            if (options.length) break;
                        }
                    } catch (e) {
                        // permission error or not found; try next
                    }
                }
                // If still empty, derive from existing expense records
                if (!options.length && Array.isArray(state.expenses)) {
                    const derived = Array.from(new Set(state.expenses
                        .map(e => (e && e.payment_method) ? String(e.payment_method).trim() : '')
                        .filter(Boolean)));
                    if (derived.length) options = derived;
                }
                // If still empty, use hard fallback
                if (!options.length) options = fallbackDefaults;
                commit('setPaymentMethods', options);
            } catch (err) {
                console.error(err);
                // On unexpected failure, set to defaults to avoid blank UI
                commit('setPaymentMethods', fallbackDefaults);
            }
        }

    }
});
