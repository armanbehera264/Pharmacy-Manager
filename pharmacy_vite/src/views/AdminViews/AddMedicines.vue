<script setup>
    import { useStore } from 'vuex';
    import { useToast } from 'primevue/usetoast';
    import { ref } from 'vue';
    import '../../styles/styles.css';
    import axios from '../../axios';

    const store = useStore();
    const toast = useToast();

    const message = ref('');

    const ingredientsCount = ref(1);
    const ingredientsData = ref([]);
    const selectedIngredients = ref(Array(ingredientsCount.value).fill(null));
    const filteredIngredients = ref();

    const allergiesCount = ref(1);
    const allergiesData = ref([]);
    const selectedAllergies = ref([]);
    const filteredAllergies = ref([]);

    const categoriesCount = ref(1);
    const categoriesData = ref([]);
    const selectedCategories = ref([]);
    const filteredCategories = ref();

    const sideEffectsCount = ref(1);
    const sideEffectsData = ref([]);
    const selectedSideEffects = ref([]);
    const filteredSideEffects = ref();
    
    const name = ref('');
    const stock = ref();
    const price = ref();
    const manufacturer = ref('');
    const expiration_date = ref('');
    const description = ref('');

    if (store.getters.isRegistered){ 

        const usertype = store.getters.getUserDetails['usertype']
        if (usertype === 'administrator' || usertype === 'pharmacy') {

            axios.get('/administrator/addMedicines/')
            .then( (response) => {
                allergiesData.value = response.data.allergies
                ingredientsData.value = response.data.ingredients
                categoriesData.value = response.data.categories
                sideEffectsData.value = response.data.sideEffects
                
            })
            .catch( (error) => {
                toast.add({severity:'warn', summary: 'Unsuccessful in getting data from the server.', message: 'Please try again.', life:3000});
            })
        } else {
            message.value = "Log in using an admin or pharmacist user to access this page."
        }
    }

    const searchIngredients = (event) => {
        setTimeout(() => {
            if (!event.query.trim().length) {
                filteredIngredients.value = [...ingredientsData.value]
            } else {
                filteredIngredients.value = ingredientsData.value.filter((ingredient) => {
                    return ingredient.name.toLowerCase().startsWith(event.query.toLowerCase());
                });
            }
        }, 50);
    }

    const search = (event, filteredArray, fullArray) => {
        setTimeout(() => {
            if (!event.query.trim().length) {
                console.log(filteredArray)
                console.log(fullArray)
                filteredArray = [...fullArray]
            } else {
                filteredArray = fullArray.filter((element) => {
                    return element.name.toLowerCase().startsWith(event.query.toLowerCase());
                });
            }
        }, 50);
    }

    const searchAllergies = (event) => {
        setTimeout(() => {
            if (!event.query.trim().length) {
                filteredAllergies.value = [...allergiesData.value]
            } else {
                filteredIngredients.value = allergiesData.value.filter((allergy) => {
                    return allergy.name.toLowerCase().startsWith(event.query.toLowerCase());
                });
            }
        }, 50);
    }

    const submit = () => {
        console.log(selectedIngredients.value)
    }
</script>

<template>
    <Toast/>

    <div class="centered">
        <h1 class="text-3xl font-bold m-3"> {{ message }}</h1>
    </div>

    <div class="top-container">
        <div class="container">
            <div class="sub-container">
                <InputText class="elements" id="Name" placeholder="Name *" v-model.trim="name"/>
                <InputNumber class="elements" id="stock" placeholder="Stock *" inputId="withoutgrouping" :useGrouping="false" v-model.number="stock" :min="0" :allowEmpty="true"/>
            </div>
            <div class="sub-container">
                <InputNumber class="elements" id="price" placeholder="Price *" inputId="currency-india" mode="currency" currency="INR" currencyDisplay="code" locale="en-IN" v-model.number="price" :min="0" :allowEmpty="true"/>
                <InputText class="elements" id="Manufacturer" placeholder="Manufacturer" v-model.trim="manufacturer"/>
            </div>

            <div class="sub-container">
                <DatePicker v-model="expiration_date" dateFormat="dd/mm/yy" placeholder="Expiration Date"/>
            </div>

            <div class="vertical-divide"></div>

            <div class="sub-container mt-4">
                <FloatLabel>
                    <Textarea v-model="description" autoResize rows="5" cols="54"/>
                    <label>Description</label>
                </FloatLabel>
            </div>
        </div>

        <div class="vertical-divide"></div>

        <div class="sub-container">
            <div class="container" >
                <div class="sub-container" v-for="n in ingredientsCount" :key="n">
                    <AutoComplete :placeholder="`Ingredient ${n}`" v-model="selectedIngredients[n]" optionLabel="name" dropdown :suggestions="filteredIngredients" @complete="(event) => search(event, filteredIngredients, ingredientsData)"></AutoComplete>
                </div>
                <Button label="Add Ingredient" @click.prevent="ingredientsCount += 1"/>
                
                <div class="sub-container" v-for="n in allergiesCount" :key="n">
                    <AutoComplete :placeholder="`Allergy ${n}`" v-model="selectedAllergies[n]" optionLabel="name" dropdown :suggestions="filteredAllergies" @complete="searchAllergies"></AutoComplete>
                </div>
                <Button label="Add Allergy" @click.prevent="allergiesCount += 1"/>
            </div>
        </div>
    </div>
    <Button label="Submit" @click.prevent="submit"/>
</template>