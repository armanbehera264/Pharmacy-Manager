<script setup>
    import axios from 'axios';
    import { useStore } from 'vuex';
    import { ref } from 'vue';

    const userData = ref();
    const inventoryData = ref();



    const expandedRows = ref();

    const store = useStore();
    store.dispatch('updateState');

    axios.get('/api/v1/users/me')
    .then( (response) => {
        console.log(response)
    })
    .then( (error) => {
        console.log(error)
    })
    
    
</script>

<template>
    <div class="container">
        
        <div class="sub-container">
            <div class="card" style="margin-left: 20px;">
                <ExpandableDataTable :value="userData" dataKey="statName" v-model:expandedRows = "expandedRows"/>
            </div>
        </div>
    </div>
</template>