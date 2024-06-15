<script setup>
    import axios from 'axios';
    import { onMounted } from 'vue';
    import { useStore } from 'vuex';

    onMounted (() => {
        const store = useStore()
        
        if (store.getters.isRegistered === true){ 
            const usertype = store.getters.getUserDetails['usertype']
            console.log("usertype: "+usertype)
            const url = '/' + usertype + '/logout/'

            console.log("URL: "+url)
            axios.post(url, {'logout': true})
            .then( (response) => {
                console.log(response)
                store.dispatch('logout')
            })   
        }
    })
</script>

<template>
    <h1>Logout successful!</h1>
</template>