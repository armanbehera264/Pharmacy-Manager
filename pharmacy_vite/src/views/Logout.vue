<script setup>
    import axios from 'axios';
    import { onMounted } from 'vue';
    import { useStore } from 'vuex';
    import router from '../router'; 
    import { ref } from 'vue';

    const leftWidth = ref('48%');

    onMounted (() => {
        const store = useStore()
        
        if (store.getters.isRegistered === true){ 
            const usertype = store.getters.getUserDetails['usertype']
            const url = '/' + usertype + '/logout/'

            axios.post(url, {'logout': true})
            .then( (response) => {
                store.dispatch('logout')
            })
            .catch( (error) => {
                store.dispatch('logout')
                console.log(error);
            })
        }
    })
</script>

<template>
    <div class="centered">
        <h1>Logout successful!</h1>
    </div>

    <div class="centered">
        <Button label="small" class="routerlink" @click="$router.push('/')">Home Page</Button>
    </div>
</template>