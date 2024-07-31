<script setup>
    import axios from '../../axios';
    import { useStore } from 'vuex';
    import { ref } from 'vue';
    import { useToast } from 'primevue/usetoast';
    import { setCookie, getCookieValue } from '../../services.js'

    /*const data = ref([
        {
            "id": 1,
            "last_login": null,
            "is_superuser": false,
            "is_staff": true,
            "is_active": true,
            "date_joined": "2024-07-07T05:46:59.808432Z",
            "username": "ArmanBeheraregistered",
            "email": "armanbehera264@gmail.com",
            "first_name": "Arman",
            "last_name": "Behera",
            "age": 60,
            "gender": "Male",
            "primary_phone_number": "07681075012",
            "secondary_phone_number": "07681075012",
            "role": "Doctor",
            "is_verified": false,
            "occupation": "Doctor",
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 2,
            "last_login": null,
            "is_superuser": false,
            "is_staff": true,
            "is_active": true,
            "date_joined": "2024-07-07T05:47:53.082171Z",
            "username": "ArmanBeheraisregistered",
            "email": "armanbehera264@gmail.com",
            "first_name": "Arman",
            "last_name": "Behera",
            "age": 60,
            "gender": "Male",
            "primary_phone_number": "07681075012",
            "secondary_phone_number": "0",
            "role": "Doctor",
            "is_verified": false,
            "occupation": "Doctor",
            "groups": [],
            "user_permissions": []
        }
    ])*/

    const data = ref();

    const message = ref();
    const selected = ref();

    const verificationDialog = ref();
    const deletionDialog = ref();

    const store = useStore();
    store.dispatch('initializeStore');
    const toast = useToast();

    if (store.getters.isRegistered === true){
        axios.get('/api/v1/users/me/')
        .then( (response) => {
            console.log(response)
            // data.value = response
        })
        .then( (error) => {
            console.log(error)
            message.value = "Log in using an admin account to access this page."
        })
    }
    else {
        message.value = "Log in using an admin account to access this page."
    }

    const confirmVerification = () => {
        verificationDialog.value = true;
    }

    const confirmDeletion = () => {
      deletionDialog.value = true;
    }

    // To send post request to the backend
    const sendVerification = () => {
        
        console.log(selected.value.id)
        data.value = data.value.filter(val => !selected.value.includes(val));
        selected.value = null;
        verificationDialog.value = false;
        toast.add({severity:'success', summary: 'Successfully verified users!', life: 3000});
    }

    // To post request to the backend
    const sendDelete = () => {

        console.log(selected.value)
        data.value = data.value.filter(val => !selected.value.includes(val));
        selected.value = null;
        deletionDialog.value = false;
        toast.add({severity:'success', summary: 'Successfully deleted users!', life: 3000});
    }
    
</script>

<template>
    <Toast/>

    <div class="centered">
        <h1>{{ message }}</h1>
    </div>
    
    <div class="top-container">
        
        <div class="container">
            <h1>Verify Employees</h1>
            <div class="sub-container" style="margin-left:7rem;">
                <div class="card">
                    <DataTable :value="data" v-model:selection="selected" datakey="id" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
                        
                        <Column selectionMode="multiple" style="width: 3rem"></Column>
                        <Column field="first_name" header="First Name" style="width: 20%" sortable></Column>
                        <Column field="last_name" header="Last Name" style="width: 20%" sortable></Column>
                        <Column field="role" header="Role" style="width: 20%" sortable></Column>
                        <Column field="email" header="Email" style="width:50%" sortable></Column>
                    </DataTable>
                </div>
            </div>
            
            <div class="sub-container"> 
                <Button label="Verify" icon="pi pi-check-circle" severity="success" @click="confirmVerification" style="margin-left: 25rem; margin-top: 3rem;" :disabled="!selected || !selected.length"/>
                <Button label="Delete" icon="pi pi-trash" severity="danger" @click="confirmDeletion" style="margin-left: 2rem; margin-top: 3rem;" :disabled="!selected || !selected.length"/>
            </div>    
        </div>
    </div>

    <Dialog v-model:visible="verificationDialog" :style="{ width: '450px' }" header="Confirm">
        <div class="flex items-center gap-4">
            <i class="pi pi-exclamation-triangle !text-3xl" />
            <span>Are you sure you want to verify the selected users?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" text @click="verificationDialog = false"/>
            <Button label="Yes" icon="pi pi-check" text @click="sendVerification"/>
        </template>
    </Dialog>

    <Dialog v-model:visible="deletionDialog" :style="{ width: '450px' }" header="Confirm">
        <div class="flex items-center gap-4">
            <i class="pi pi-exclamation-triangle !text-3xl" />
            <span>Are you sure you want to delete the selected users?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" text @click="deletionDialog = false"/>
            <Button label="Yes" icon="pi pi-check" text @click="sendDelete"/>
        </template>
    </Dialog>

</template>