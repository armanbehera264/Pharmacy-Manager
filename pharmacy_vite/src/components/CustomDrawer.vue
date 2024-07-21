<script setup>

    const props = defineProps({
        heading: {
            type: String,
            required: true
        }
    })
</script>

<template>
    <Drawer>
        <template #container="{ closeCallback }">
            <div class="flex flex-col h-full">
                <div class="flex items-center justify-between px-6 pt-4 shrink-0">
                    <span class="inline-flex items-center gap-2">
                        <svg width="40" height="50" viewBox="0 5 40 50" fill="none">
                            <image href="../assets/Pharmacy.png" x="2" y="2" height="40" width="40"/>
                        </svg>
                        <span class="font-semibold text-2xl text-primary">{{ heading }}</span>
                    </span>
                    <span>
                        <Button type="button" @click="closeCallback" icon="pi pi-times" rounded outlined></Button>
                    </span>
                </div>
            </div>
        </template>
    </Drawer>
</template>