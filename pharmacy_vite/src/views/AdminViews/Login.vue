<script setup>
    import { ref } from 'vue';
    import '../../styles/styles.css';
    import CustomPassword from '../../components/CustomPassword.vue';
    import axios from 'axios';
    import { useStore } from 'vuex';
    
    const first_name = ref('');
    const last_name = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    const registration = ref('');

    const store = useStore();

    const submit = () => {

        const data = {
            first_name: first_name.value,
            last_name: last_name.value,
            password: password.value,
            registration: registration.value
        }

        var passwordCheck = true;

        if (password.value != confirmPassword.value){
            passwordCheck = false;
        }

        if (!passwordCheck){
            alert("Password and Confirmation Password do not match!")
        }
        else {
            console.log(data);
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
            .then( (error) => {
                // If an error is raised
                console.log(error);
            })
        }
    };
</script>

<template>

    <h1>Log in</h1>

    <div id="top-container">
        <div id="container">
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
        </div>
    </div>
</template>