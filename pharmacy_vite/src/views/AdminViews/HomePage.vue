<script setup>
    
    import axios from 'axios';
    import { useStore } from 'vuex';

    const store = useStore();
    store.dispatch('updateState');
    
    
</script>

<template>
    
</template>