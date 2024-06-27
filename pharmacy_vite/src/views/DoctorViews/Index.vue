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
            state: 'always',
            command: () => {
                router.push('/doctor/')
            }
        },
        {
            label: 'Signin',
            icon: 'pi pi-sign-in',
            state: 'loggedout',
            command: () => {
                router.push('/doctor/signin')
            }
        },
        {
            label: 'Login',
            icon: 'pi pi-user',
            state: 'loggedout',
            command: () => {
                router.push('/doctor/login')
            }
        },
        {
            label: 'Logout',
            icon: 'pi pi-sign-out',
            state: 'loggedin',
            command: () => {
                router.push('/logout')
            }
        }
    ])

    const loggedIn = computed(() => store.getters.isRegistered);

    const updateState = () => {
        store.dispatch('updateState');
        const instance = getCurrentInstance();
        instance.proxy.$forceUpdate();
    }

    const toRender = (state) => {

        if (state === 'loggedout' && !loggedIn.value){
            return true
        }
        else if (state === 'loggedin' && loggedIn.value){
            return true
        }
        else if (state === 'always'){
            return true
        }
        else {
            return false
        }
    }

    onMounted(() => {
        updateState();
        window.addEventListener('storage', updateState);
    })

    onBeforeUnmount(() => {
        window.removeEventListener('storage', updateState);
    });
</script>

<template>
    <Menubar :model="items">
        <template #start>
            <svg width="50" height="40">
                <image href="../../assets/Pharmacy.png" x="2" y="2" height="36" width="36"/>
            </svg>
        </template>
        <template #item="{ item, props }">
            <a v-if="toRender(item.state)" :target="item.target" v-bind="props.action">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
            </a>
        </template>
    </Menubar>

    <router-view/>
</template>