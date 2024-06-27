<script setup>
// @ is an alias to /src
    import '../styles/styles.css';

</script>


<template>
    <div class="centered">
      <!-- <HelloWorld msg="Welcome to Your Vue.js App"/>-->
        <Button class="routerlink" @click="$router.push('/admin/login')">Admin Login</Button>
        <Button class="routerlink" @click="$router.push('/doctor/login')">Doctor Login</Button>
        <Button class="routerlink" @click="$router.push('/frontdesk/login')">Front Desk Login</Button>
        <Button class="routerlink" @click="$router.push('/employee/login')">Employee Login</Button>
    </div>
</template>