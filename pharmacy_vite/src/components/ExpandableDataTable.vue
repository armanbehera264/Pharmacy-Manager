<template>
    <DataTable tableStyle="max-width: 20rem" datakey="statName">
        <Column expander style="width: 10%"/>
        <Column field="statName" style="width:60%"></Column>
        <Column field="count" style="width: 30%"></Column>
        <template #expansion="slotProps">
            <div class="sub-card" v-if="slotProps.data.subFields">
                <DataTable :value="slotProps.data.subFields" datakey="subFieldName">
                    <Column field="subFieldName"></Column>
                    <Column field="value"></Column>
                </DataTable>
            </div>
        </template>
    </DataTable>
</template>