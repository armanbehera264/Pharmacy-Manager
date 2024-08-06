<script setup>
    import axios from '../../axios';
    import { useStore } from 'vuex';
    import { ref } from 'vue';

    const unverifiedUsersData = ref([]);
    const medicineInventoryData = ref([]);
    const employeesData = ref([]);

    const store = useStore();
    store.dispatch('initializeStore');

    const expandedRows = ref();

    if (store.getters.isRegistered) {

        axios.get('administrator/verifyEmployees/')
        .then( (response) => {
            unverifiedUsersData.value = response.data
        })
        .catch( (error) => {
            console.log("Error getting unverified users data.")
        })

        axios.get('administrator/viewEmployees/')
        .then( (response) => {
            employeesData.value = response.data
        })
        .catch( (error) => {
            console.log("Error getting employees data")
        })

        // To get data for inventory

    }
</script>

<template>
    <div class="container">
        <div class="sub-container">
            <div class="card" style="margin-left: 20px;">
                <DataTable :value="employeesData" datakey="id" :rows="2" paginator tableStyle="min-width: 22rem">
                    <Column field="first_name" header="First Name" style="width: 20%" sortable></Column>
                    <Column field="last_name" header="Last Name" style="width: 20%" sortable></Column>
                </DataTable>
                <div class="centered">
                    <Button label="View Employees" icon="pi pi-external-link"  iconPos="right" @click="$router.push({ name: 'ViewEmployees' })" style="margin: 0.5rem"/>
                </div>
            </div>
        </div>

        <div class="sub-container">
            <div class="card" style="margin-left: 20px;">
                <DataTable :value="unverifiedUsersData" datakey="id" :rows="2" paginator tableStyle="min-width: 22rem" v-if="unverifiedUsersData.length != 0">
                    <Column field="first_name" header="First Name" style="width: 20%" sortable></Column>
                    <Column field="last_name" header="Last Name" style="width: 20%" sortable></Column>
                </DataTable>

                <div v-if="unverifiedUsersData.length === 0" class="centered placeholder-table" style="min-width: 20rem; padding:1rem">
                    All users verified!
                </div>

                <div class="centered" v-if="unverifiedUsersData.length != 0">
                    <Button label="Verify Employees" icon="pi pi-external-link"  iconPos="right" @click="$router.push({ name: 'VerifyEmployees' })" style="margin: 0.5rem"/>
                </div>
            </div>
        </div>
    </div>
</template>