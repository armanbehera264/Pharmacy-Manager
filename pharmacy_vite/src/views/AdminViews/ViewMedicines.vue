<script setup>
    import { ref } from 'vue';
    import { useStore } from 'vuex';
    import axios from '../../axios';
    import { useToast } from 'primevue/usetoast';
    import '../../styles/styles.css';

    const toast = useToast();

    const store = useStore();
    store.dispatch('initializeStore');

    const deletionDialog = ref();
    const selected = ref()
    const message = ref();
    const data = ref([]);
    const length = ref(-1);

    if (store.getters.isRegistered === true) {
        axios.get('/administrator/viewMedicines/')
        .then( (response) => {
            data.value = response.data
            length.value = data.value.length
            console.log(data.value)
        })
        .catch( (error) => {
            console.log(error)
            message.value = "Log in using an admin account to access this page."
        })
    }
    else {
        message.value = "Log in using an admin account to access this page."
    }

    const confirmDeletion = () => {      
        deletionDialog.value = true;
    }

    const sendRequest = () => {
        deletionDialog.value = false;

        let idArray = []

        for (let i = 0; i < selected.value.length; i++) {
            idArray.push(selected.value[i]['id'])
        }

        axios.post('/administrator/viewMedicines/', { ids: idArray })
        .then( (response) => {
            
            data.value = data.value.filter(val => !selected.value.includes(val));
            selected.value = null;

            toast.add({severity:'success', summary: 'Successfully deleted users!', life: 3000});
        })
        .catch( (error) => {
            toast.add({severity:'warn', summary: 'Unsuccesful in deleting users.', message: 'Please try again.', life:3000});
        })
    }
</script>

<template>
    <Toast />

    <div class="centered">
        <h1 class="text-3xl font-bold m-3">{{ message }}</h1>
    </div>

    <div class="top-container" v-if="data.length >= 0">
        <div class="container">
            <div class="centered">
                <h1 class="text-3xl font-bold m-3">View Medicines</h1>    
            </div>

            <div class="sub-container" style="margin-left:7rem;" v-if="data.length != 0">
                <div class="card">
                    <DataTable :value="data" v-model:selection="selected" datakey="id" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
                        <Column selectionMode="multiple" style="width: 3rem"></Column>
                        <Column field="name" header="Name" style="width: 20%" sortable></Column>
                        <Column field="stock" header="Stock" style="width: 20%" sortable></Column>
                        <Column field="price" header="Price" style="width: 20%" sortable></Column>
                        <Column field="manufacturer" header="Manufacturer" style="width:20%" sortable></Column>
                        <Column field="expiration_date" header="Expiration Date" style="width: 20%" sortable></Column>
                    </DataTable>
                </div>
            </div>

            <div class="centered" v-if="data.length == 0">
                <h1 class="text-l font-bold m-2">There are no medicines registered in the system.</h1>
            </div>

            <div class="flex justify-center space-x-4 mt-8">
                <Button label="Delete" icon="pi pi-trash" severity="danger" @click="confirmDeletion" :disabled="!selected || !selected.length" v-if="data.length > 0"/>
                <Button label="Add Medicines" icon="pi pi-plus" severity="success" @click="$router.push({ name: 'AddMedicines' })"/>  
            </div>

        </div>
    </div>

    <div v-else>
        <h1 class="text-3xl font-bold m-3">There are no employees in the system.</h1>
    </div>

    <Dialog v-model:visible="deletionDialog" :style="{ width: '450px' }" header="Confirm">
        <div class="flex items-center gap-4">
            <i class="pi pi-exclamation-triangle !text-3xl" />
            <span>Are you sure you want to delete the selected users?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" text @click="deletionDialog = false"/>
            <Button label="Yes" icon="pi pi-check" text @click="sendRequest"/>
        </template>
    </Dialog>
</template>