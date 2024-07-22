<script setup>
    import axios from '../axios';
    import { onMounted } from 'vue';
    import { useStore } from 'vuex';
    import { ref } from 'vue';
    import { getCookieValue } from '../services'

    const message = ref('');

    onMounted (() => {
        const store = useStore()
        
        if (store.getters.isRegistered === true){ 
            const usertype = store.getters.getUserDetails['usertype']
            const url = '/' + usertype + '/logout/'

            const cookie = getCookieValue("jwt")
            console.log(cookie)

            axios.post(url, 
            { 
                "logout" : true,
                "cookie" : cookie
            }, 
            {
                withCredentials: true
            })
            .then( (response) => {
                store.dispatch('logout')
                document.cookie = 'jwt=; max-age=0; path=/'
                message.value = "Logout successful!"
            })
            .catch( (error) => {
                message.value = "Logout unsuccessful!"
                console.log(error);
                store.dispatch('logout')
                document.cookie = 'jwt=; max-age=0; path=/'
            })
        }
    })
</script>

<template>
    <div class="centered">
        <h1>{{ message }}</h1>
    </div>

    <div class="centered">
        <Button label="small" class="routerlink" @click="$router.push('/')">Home Page</Button>
    </div>
</template>