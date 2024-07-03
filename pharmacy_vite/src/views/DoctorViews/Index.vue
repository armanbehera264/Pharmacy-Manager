<script setup>
    import router from '../../router';
    import { watch } from 'vue';
    import { ref, computed, onMounted, onBeforeUnmount, getCurrentInstance } from 'vue';
    import { useStore } from 'vuex';
    
    const store = useStore();

    const items = ref([
        {
            label: 'Home',
            icon: 'pi pi-home',
            loggedIn: true,
            command: () => {
                router.push('/doctor/')
            }
        },
        {
            label: 'Signin',
            icon: 'pi pi-sign-in',
            loggedIn: false,
            command: () => {
                router.push('/doctor/signin')
            }
        },
        {
            label: 'Login',
            icon: 'pi pi-user',
            loggedIn: false,
            command: () => {
                router.push('/doctor/login')
            }
        },
        {
            label: 'Logout',
            icon: 'pi pi-sign-out',
            loggedIn: true,
            command: () => {
                router.push('/logout')
            }
        }
    ])

    const loggedIn = computed(() => store.state.isRegistered);
</script>

<template>
    <Menubar :model="items">
        <template #start>
            <svg width="50" height="40">
                <image href="../../assets/Pharmacy.png" x="2" y="2" height="36" width="36"/>
            </svg>
        </template>
        <template #item="{ item, props }">
            <a v-if="item.loggedIn == loggedIn" :target="item.target" v-bind="props.action">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </template>
    </Menubar>
    {{ loggedIn }}
    <router-view/>
</template>