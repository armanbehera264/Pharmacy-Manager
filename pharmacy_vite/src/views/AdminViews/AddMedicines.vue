<script setup>
    import { useStore } from 'vuex';
    import { useToast } from 'primevue/usetoast';
    import { ref } from 'vue';
    import '../../styles/styles.css';
    import axios from '../../axios';
    import { format } from 'date-fns';

    const store = useStore();
    const toast = useToast();

    const message = ref('');

    const ingredientsCount = ref(1);
    const ingredientsData = ref([]);
    let selectedIngredients = ref([]);

    const allergiesCount = ref(1);
    const allergiesData = ref([]);
    let selectedAllergies = ref([]);

    const categoriesCount = ref(1);
    const categoriesData = ref([]);
    let selectedCategories = ref([]);

    const sideEffectsCount = ref(1);
    const sideEffectsData = ref([]);
    let selectedSideEffects = ref([]);

    const filteredArray = ref();

    let name = ref('');
    let stock = ref();
    let price = ref();
    let manufacturer = ref('');
    let expiration_date = ref('');
    let description = ref('');

    if (store.getters.isRegistered) { 
        const usertype = store.getters.getUserDetails['usertype']
        if (usertype === 'administrator' || usertype === 'pharmacy') {
            axios.get('/administrator/addMedicines/')
            .then((response) => {
                allergiesData.value = response.data.allergies
                ingredientsData.value = response.data.ingredients
                categoriesData.value = response.data.categories
                sideEffectsData.value = response.data.sideEffects
            })
            .catch((error) => {
                toast.add({ severity:'warn', summary: 'Unsuccessful in getting data from the server.', message: 'Please try again.', life:3000 });
            })
        } else {
            message.value = "Log in using an admin or pharmacist user to access this page."
        }
    }

    const search = (event, fullArray) => {
        setTimeout(() => {
            if (!event.query.trim().length) {
                filteredArray.value = [...fullArray]
            } else {
                filteredArray.value = fullArray.filter((element) => {
                    return element.name.toLowerCase().startsWith(event.query.toLowerCase());
                });
            }
        }, 50);
    }

    const submit = () => {
        const categoriesArray = [];

        for (let i = 0; i < categoriesCount.value; i++) {
            categoriesArray[i] = {
                "name": selectedCategories.value[i].name ? selectedCategories.value[i].name : selectedCategories.value[i],
                "usage_priority": (i + 1)
            };
        }

        axios.post('/administrator/addMedicines/', {
            "name": name.value,
            "stock": stock.value ? stock.value : 0,
            "price": price.value ? price.value : 0,
            "description": description.value,
            "manufacturer": manufacturer.value,
            "expiration_date": expiration_date.value ? format(new Date(expiration_date.value), 'yyyy-MM-dd') : '',
            "ingredients": selectedIngredients.value.map(ingredient => ({ name: ingredient })),
            "allergies": selectedAllergies.value.map(allergy => ({ name: allergy })),
            "sideEffects": selectedSideEffects.value.map(sideEffect => ({ name : sideEffect })),
            "categories": categoriesArray
        })
        .then( (response) => {
            toast.add({ severity:'success', summary: 'Successfully added medicine', life: 2000 });
            
            // Reload the page
            setTimeout(() => {
                window.location.reload();
            }, 2000);
        })  
        .catch( (error) => {
            toast.add({ severity:'warn', summary: 'Unsuccessful in adding medicine.', message: 'Please try again in some time.', life:3000 });
        })
    }
</script>

<template>
    <Toast />

    <div class="centered">
        <h1 class="text-3xl font-bold m-3">{{ message }}</h1>
    </div>

    <div class="centered" v-if="!message">
        <h1 class="text-3xl font-bld m-3">Add Medicines</h1>
    </div>

    <div class="container mx-auto p-6 bg-grey shadow-md rounded-lg">
        <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div class="flex flex-col space-y-4">
                <InputText id="Name" placeholder="Name *" v-model.trim="name" class="p-inputtext-sm w-full" />
                <InputNumber id="stock" placeholder="Stock *" inputId="withoutgrouping" :useGrouping="false" v-model.number="stock" :min="0" :allowEmpty="true" class="p-inputnumber-sm w-full" />
                <InputNumber id="price" placeholder="Price *" inputId="currency-india" mode="currency" currency="INR" currencyDisplay="code" locale="en-IN" v-model.number="price" :min="0" :allowEmpty="true" class="p-inputnumber-sm w-full" />
                <InputText id="Manufacturer" placeholder="Manufacturer" v-model.trim="manufacturer" class="p-inputtext-sm w-full" />
                <DatePicker v-model="expiration_date" dateFormat="dd/mm/yy" placeholder="Expiration Date" class="p-datepicker-sm w-full" />
                <FloatLabel class="mt-4">
                    <Textarea v-model="description" autoResize rows="5" cols="54" class="w-full" />
                    <label>Description</label>
                </FloatLabel>
            </div>

            <div class="flex flex-col space-y-6">
                <div class="flex flex-col space-y-4">
                    <label class="font-semibold">Ingredients</label>
                    <div v-for="n in ingredientsCount" :key="n" class="flex items-center space-x-4">
                        <AutoComplete :placeholder="`Ingredient ${n}`" v-model="selectedIngredients[n - 1]" optionLabel="name" dropdown :suggestions="filteredArray" @complete="(event) => search(event, ingredientsData)" class="w-full" />
                    </div>
                    <Button label="Add Ingredient" @click.prevent="ingredientsCount += 1" class="p-button-sm" />
                </div>

                <div class="flex flex-col space-y-4">
                    <label class="font-semibold">Allergies</label>
                    <div v-for="n in allergiesCount" :key="n" class="flex items-center space-x-4">
                        <AutoComplete :placeholder="`Allergy ${n}`" v-model="selectedAllergies[n - 1]" optionLabel="name" dropdown :suggestions="filteredArray" @complete="(event) => search(event, allergiesData)" class="w-full" />
                    </div>
                    <Button label="Add Allergy" @click.prevent="allergiesCount += 1" class="p-button-sm" />
                </div>
            </div>

            <div>
                <div class="flex flex-col space-y-4">
                    <label class="font-semibold">Categories</label>
                    <div v-for="n in categoriesCount" :key="n" class="flex items-center space-x-4">
                        <AutoComplete :placeholder="`Use ${n}`" v-model="selectedCategories[n - 1]" optionLabel="name" dropdown :suggestions="filteredArray" @complete="(event) => search(event, categoriesData)" class="w-full" />
                    </div>
                    <Button label="Add Use" @click.prevent="categoriesCount += 1" class="p-button-sm" />
                </div>

                <div class="flex flex-col space-y-4">
                    <label class="font-semibold mt-4">Side Effects</label>
                    <div v-for="n in sideEffectsCount" :key="n" class="flex items-center space-x-4">
                        <AutoComplete :placeholder="`Side Effect ${n}`" v-model="selectedSideEffects[n - 1]" optionLabel="name" dropdown :suggestions="filteredArray" @complete="(event) => search(event, sideEffectsData)" class="w-full" />
                    </div>
                    <Button label="Add Side Effect" @click.prevent="sideEffectsCount += 1" class="p-button-sm" />
                </div>    
            </div>
        </div>
        <div class="flex justify-center mt-4">
            <Button label="Submit" @click.prevent="submit" class="p-button-lg" />
        </div>
    </div>
</template>

<style scoped>
.container {
    max-width: 1200px;
}

.sub-container {
    margin-bottom: 1rem;
}

.vertical-divide {
    margin: 0 1rem;
}

.flex-col > .sub-container {
    margin-bottom: 0;
}

.p-button-sm {
    width: auto;
    margin-top: 0.5rem;
}

.p-button-lg {
    padding: 0.75rem 1.5rem;
    font-size: 1.1rem;
}
</style>