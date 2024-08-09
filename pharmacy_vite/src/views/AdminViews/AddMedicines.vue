<script setup>
    import { useStore } from 'vuex';
    import { useToast } from 'primevue/usetoast';
    import { ref } from 'vue';
    import '../../styles/styles.css';
    import axios from '../../axios';

    const store = useStore();
    const toast = useToast();

    const message = ref('');

    const allergiesCount = ref(1);
    const categoriesCount = ref(1)

    const allergiesData = ref([]);
    const categoriesData = ref([]);
    const sideEffectsData = ref([]);
    const ingredientsData = ref([]);

    if (store.getters.isRegistered){ 

        const usertype = store.getters.getUserDetails['usertype']
        if (usertype === 'administrator' || usertype === 'pharmacy') {

            axios.get('/administrator/addMedicines/')
            .then( (response) => {
                allergiesData.value = response.data.allergies
                ingredientsData.value = response.data.ingredients
                categoriesData.value = response.data.categories
                sideEffectsData.value = response.data.sideEffects
            })
            .catch( (error) => {
                toast.add({severity:'warn', summary: 'Unsuccessful in getting data from the server.', message: 'Please try again.', life:3000});
            })
        } else {
            message.value = "Log in using an admin or pharmacist user to access this page."
        }
    }


</script>

<template>
    <Toast/>

    <div class="centered">
        <h1 class="text-3xl font-bold m-3"> {{ message }}</h1>
    </div>

    <div class="top-container">
        <div class="container">
            <div class="sub-container">
                <InputText class="elements" id="Name" placeholder="Name *" v-model.trim="first_name"/>
                <InputNumber class="elements" id="age" placeholder="Age*" inputId="withoutgrouping" :useGrouping="false" v-model.number="age" :min="0" :allowEmpty="false"/>
            </div>
        </div>
    </div>
    
</template>