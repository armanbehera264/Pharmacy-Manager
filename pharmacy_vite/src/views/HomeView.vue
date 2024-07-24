<script setup>
// @ is an alias to /src
    import '../styles/styles.css';

</script>


<template>
    <div class="centered">
        <Button class="routerlink" @click="$router.push({ name: 'AdminLogin' })">Admin Login</Button>
        <Button class="routerlink" @click="$router.push({ name: 'DoctorLogin' })">Doctor Login</Button>
        <Button class="routerlink" @click="$router.push({ name: 'FrontDeskLogin' })">Front Desk Login</Button>
        <Button class="routerlink" @click="$router.push({ name: 'EmployeeLogin' })">Employee Login</Button>
    </div>
</template>