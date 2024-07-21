<script setup>
    import router from '../../router';
    import { watch } from 'vue';
    import { ref, computed } from 'vue';
    import { useStore } from 'vuex';
    
    const store = useStore();
    const drawerVisible = ref(false);

    const items = ref([
        {
            label: 'Home',
            icon: 'pi pi-home',
            loggedIn: false,
            loggedOut: true,
            command: () => {
                router.push('/admin/')
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
                router.push('/admin/login')
            }
        },
        {
            label: 'Logout',
            icon: 'pi pi-sign-out',
            loggedIn: true,
            loggedOut: false,
            command: () => {
                router.push('/logout')
            }
        }
    ])

    const loggedIn = computed(() => store.state.isRegistered);
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