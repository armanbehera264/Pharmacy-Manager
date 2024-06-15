<script setup>
    // to add fields: specialization
    import { ref } from 'vue';
    import '../../styles/styles.css';
    import CustomPassword from '../../components/CustomPassword.vue';
    import axios from 'axios';
    import router from '../../router' 

    const first_name = ref('');
    const last_name = ref('');
    const primary_phone_number = ref('');
    const secondary_phone_number = ref('');
    const email = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    const age = ref();
    const gender = ref('');
    const genders = ref([
        {gender: 'Male'},
        {gender: 'Female'}, 
        {gender: 'Other'}
    ]);
    const dob = ref('');
    const address = ref('');
    const employee_id = ref('');

    const submit = () => {
        
        const data = {
        first_name: first_name.value,
        last_name: last_name.value,
        primary_phone_number: primary_phone_number.value,
        secondary_phone_number: secondary_phone_number.value,
        email: email.value,
        password: password.value,
        age: age.value,
        gender: gender.value['gender'],
        dob: dob.value,
        address: address.value,
        employee_id: employee_id.value
        };

        var filled = true;
        var passwordCheck = true;

        console.log(data);

        if (password.value != confirmPassword.value) {
            passwordCheck = false;
        }

        // Checks for any empty fields
        /*for (const key in data) {
            if (!data[key] || data[key].trim() === '') {
                filled = false;
            }
        } */

        // If there's any fiele left out - All fields need to be filled
        if (!filled) {
            alert("Please fill in all the required fields!");

            console.log(data);
        }
        else if (!passwordCheck) {
            alert("Password and Confirmation Password do not match.")
        }
        // No errors - Sending message to the backend
        else {
            axios.post('/doctor/signin/', {
                data
            })
            .then( (response) => {
                console.log(response);
                router.push('/doctor/login')  
            })
            .then( (error) => {
                console.log(error);
            })
        }
    }
</script>

<template>
    <h1>Sign in</h1>

    <div id="top-container">
        <div id="container">
            <div class="sub-container">
                <InputText class="elements" id="first-name" placeholder="First Name" v-model="first_name"/>
                <InputText class="elements" id="last-name" placeholder="Last Name" v-model="last_name"/>
            </div>

            <div class="sub-container">
                <InputText class="elements" id="primary-phone-number" placeholder="Primary Phone Number" v-model="primary_phone_number"/>
                <InputText class="elements" id="secondary-phone-number" placeholder="Secondary Phone Number" v-model="secondary_phone_number"/>
            </div>

            <div class="sub-container">
                <InputText class="elements" id="email-id" placeholder="Email Id" v-model="email"/>
            </div>
            <div class="sub-container">
                <CustomPassword class="elements" placeholder="Password" v-model="password"/>
            </div>

            <div class="sub-container">
                <CustomPassword class="elements" placeholder="Confirm Password" v-model="confirmPassword"/>
            </div>

            <div class="sub-container">
                <InputNumber class="elements" id="age" placeholder="Age" inputId="withoutgrouping" :useGrouping="false" v-model="age" :min="0" :max="100" :allowEmpty="False"/>
                <Dropdown class="elements" id="gender" v-model="gender" :options="genders" optionLabel="gender" placeholder="Gender"/>
                <Calendar class="elements" id="dob" v-model="dob" placeholder="DOB"/>
            </div>

            <div class="sub-container">
                <InputText class="elements" id="address" placeholder="Address" v-model="address"/>
            </div>

            <div class="sub-container">
                <InputText class="elements" id="registration" placeholder="Employee ID" v-model="employee_id"/>
            </div>
        </div>

        <div class="vertical-divide"></div>

        <div class="container">
            <img alt="injection-image" src="../..//assets/Injection.png"/>
            <div class="sub-container">
                <span class="quote">"Medicine is not only a science; it is also an art. It does not consist of compounding pills and plasters; it deals withe very processes of life, which must be understood before they may be guided." - Paracelsus</span>
    </div>
        </div>
    </div>

    <Button label="Submit" @click.prevent="submit"/>
</template>