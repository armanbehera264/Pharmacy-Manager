<script setup>
    import router from '../../router';
    import { watch } from 'vue';
    import { ref, computed } from 'vue';
    import { useStore } from 'vuex';
    import axios from 'axios';
    
    const store = useStore();
    const drawerVisible = ref(false);
    store.dispatch('initializeStore');

    const items = ref([
        {
            label: 'Home',
            icon: 'pi pi-home',
            loggedIn: false,
            loggedOut: true,
            command: () => {
                router.push({ name: 'AdminHomePage' })
            }
        },
        {
            label: 'Menu',
            icon: 'pi pi-bars',
            loggedIn: true,
            loggedOut: false,
            command: () => {
                drawerVisible.value = true;
            }
        },
        {
            label: 'Login',
            icon: 'pi pi-user',
            loggedIn: false,
            loggedOut: true,
            command: () => {
                router.push({ name: 'AdminLogin' })
            }
        },
        {
            label: 'Logout',
            icon: 'pi pi-sign-out',
            loggedIn: true,
            loggedOut: false,
            command: () => {
                router.push({ name: 'Logout'})
            }
        }
    ]);

    const loggedIn = computed(() => store.state.isRegistered);

    const getAccess = () => {

        const refreshToken = store.state.refreshToken

        axios.post('/api/v1/jwt/refresh/', refreshToken)
        .then( (response) => {
            axios.defaults.headers.common['Authorization'] = "JWT " + response.data.access
            console.log(response);
        })
        .then( (error) => {
            console.log(error)
            const userDetails = store.getters.isRegistered
            router.push(`/${userDetails.usertype}/login`)
        })
    }

    watch(loggedIn, (newVal, oldVal) => {
        
        console.log('asdasdas')
        if (newVal === true){
            // The access token is refreshed every 19 minutes
            /*setInterval(() => {
                getAccess();
            }, 1140000);*/
            console.log('newVal is set to true.')
            /*setInterval(() => {
                getAccess();
                console.log('The code is being repeated.')
            }, 5000);*/
        }   
    });
</script>

<template>
    <!-- To implement a side bar if logged in-->
    <div class="card flex justify-center">
        <CustomDrawer v-model:visible="drawerVisible" heading="Admin Page"/>
    </div>
    <Menubar :model="items">
        <template #start>
            <svg width="50" height="40">
                <image href="../../assets/Pharmacy.png" x="2" y="2" height="36" width="36"/>
            </svg>
        </template>
        <template #item="{ item, props }">
            <a v-if="item.loggedIn == loggedIn || item.loggedOut == !loggedIn" :target="item.target" v-bind="props.action">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </template>
    </Menubar>
    <router-view/>
</template>