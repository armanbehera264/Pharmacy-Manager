import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura'

import axios from 'axios';

// Importing PrimeVue components
import InputText from 'primevue/inputtext';
import DatePicker from 'primevue/datepicker';
import Button from 'primevue/button';
import FloatLabel from 'primevue/floatlabel';
import Password from 'primevue/password';
import InputNumber from 'primevue/inputnumber';
import Select from 'primevue/select';
import Divider from 'primevue/divider';
import Menubar from 'primevue/menubar';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

// Importing Custom components
import CustomPassword from './components/CustomPassword.vue';

import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';

axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.defaults.withCredentials = true;

const app = createApp(App);

app.use(PrimeVue, {
    theme: {
         preset: Aura,
         options: {
            prefix: 'p',
            darkModeSelector: 'system',
            cssLayer: false
         },
         ripple: true
    }});
app.component('InputText', InputText);
app.component('DatePicker', DatePicker);
app.component('Button', Button);
app.component('FloatLabel', FloatLabel);
app.component('Divider', Divider);
app.component('Password', Password);
app.component('InputNumber', InputNumber);
app.component('Select', Select);
app.component('Menubar', Menubar);
app.component('Toast', Toast);

app.component('CustomPassword', CustomPassword);

app.use(store);
app.use(router);
app.use(axios)
app.use(ToastService);

app.mount('#app');
