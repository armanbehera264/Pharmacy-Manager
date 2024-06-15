<script setup>
    import { ref } from 'vue';
    import '../../styles/styles.css';
    import CustomPassword from '../../components/CustomPassword.vue';
    import axios from 'axios';
    import { useStore } from 'vuex';
    import {useToast} from 'primevue/usetoast';
    
    const first_name = ref('');
    const last_name = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    const registration = ref('');

    const store = useStore();
    const toast = useToast();

    const warn = (summary, detailed) => {
        toast.add({ severity: 'warn', summary: summary, detail: detailed, life: 5000 });
    }

    const submit = () => {

        const data = {
            first_name: first_name.value,
            last_name: last_name.value,
            password: password.value,
            registration: registration.value
        }

        let post = true;

        console.log(data);

        if (password.value != confirmPassword.value){
            post = false;
            warn("Passwords do not match!", "Password and confirmation password do not match. Ensure that they are the same.")
        }

        console.log("post:"+post)
        if (post) {
            axios.post("/doctor/login/", {
                data
            })
            .then( (response) => {
                
                console.log(response);
                var username = data['first_name'] + data['last_name'] + data['registration'];
                console.log("U: "+username);
                store.dispatch('setIsRegistered', true);
                store.dispatch('setUserType', 'doctor');
                store.dispatch('setUsername', username);
                console.log(store.getters.getUserDetails);  
            })
            .catch( (error) => {
                // If an error is raised not working now
                warn("Unauthorized credentials!", "Invalid username/password or unauthorized by the admin. Contact admin for further details.");
            })
        }
    };
</script>

<template>
    
    <div class="flex align-items-center justify-content-center">
        <Toast/>
        <h1>Login</h1>
    </div>

    <div class="top-container">
        <div class="container">
            <div class="sub-container">
                <InputText class="elements" id="first-name" placeholder="First Name" v-model="first_name"/>
                <InputText class="elements" id="last-name" placeholder="Last Name" v-model="last_name"/>
            </div>

            <div class="sub-container">
                <CustomPassword class="elements" placeholder="Password" v-model="password"/>
            </div>
            
            <div class="sub-container">
                <CustomPassword class="elements" placeholder="Confirm Password" v-model="confirmPassword"/>
            </div>

            <div class="sub-container">
                <InputText class="elements" id="registration" placeholder="Doctor Registration Number" v-model="registration"/>
            </div>

            <Button label="Submit" @click.prevent="submit"/>
            <br>
            Need to make a new account?<router-link class="links" :to="{ name: 'DoctorSignin'}">Sign In</router-link>
        </div>
    </div>
</template>