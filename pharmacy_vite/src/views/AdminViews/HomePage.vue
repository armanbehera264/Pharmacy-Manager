<script setup>
    
    import axios from 'axios';
    import { useStore } from 'vuex';
    import { ref } from 'vue';

    const userData = ref([
        {
            statName: "Current User Count",
            count: "50",
            subFields: [
                {
                    subFieldName: "Doctor Count",
                    value: "20"
                },
                {
                    subFieldName: "Employee Count",
                    value: "5"
                }
            ]
        },
        {
            statName: "Unverified Users",
            count: "3",
            subFields: [
                {
                    subFieldName: "Arman Behera",
                    value: "Doctor"
                },
                {
                    subFieldName: "Jane Smith",
                    value: "Employee"
                },
                {
                    subFieldName: "John Doe",
                    value: "Front Desk"
                }
            ]
        }
    ]);

    const inventoryData = ref([
        {
            statName: "Ondem",
            value: "30"
        },
        {
            statName: "O2",
            value: "10"
        }
    ]);

    const expandedRows = ref();

    const store = useStore();
    store.dispatch('updateState');
    
    
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