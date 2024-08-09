<script setup>
    import { ref } from 'vue';
    import { useStore } from 'vuex';
    import axios from '../../axios';
    import { useToast } from 'primevue/usetoast';
    import '../../styles/styles.css';

    const toast = useToast();
    const store = useStore();

    const message = ref();
    const data = ref([]);
    const length = ref(-1);

    if (store.getters.isRegistered === true) {
        axios.get('/administrator/viewMedicines/')
        .then( (response) => {
            data.value = response.data
            length.value = data.value.length
        })
        .catch( (error) => {
            console.log(error)
            message.value = "Log in using an admin account to access this page."
        })
    }
    else {
        message.value = "Log in using an admin account to access this page."
    }

    

</script>

<template>
    <Toast/>

    <div class="centered">
        <h1 class="text-3xl font-bold m-3"> {{ message }}</h1>
    </div>
</template>