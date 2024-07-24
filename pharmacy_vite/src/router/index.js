import { createWebHistory, createRouter } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import Logout from '../views/Logout.vue'

import Doctor from '../views/DoctorViews/Index.vue'
import DoctorHomePage from '../views/DoctorViews/HomePage.vue'
import DoctorSignin from '../views/DoctorViews/Signin.vue'
import DoctorLogin from '../views/DoctorViews/Login.vue'

import Admin from '../views/AdminViews/Index.vue'
import AdminHomePage from '../views/AdminViews/HomePage.vue'
import AdminLogin from '../views/AdminViews/Login.vue'
import VerifyEmployees from '../views/AdminViews/VerifyEmployees.vue'

import Employee from '../views/EmployeeViews/Index.vue'
import EmployeeHomePage from '../views/EmployeeViews/Homepage.vue'
import EmployeeSignin from '../views/EmployeeViews/Signin.vue'
import EmployeeLogin from '../views/EmployeeViews/Login.vue'

import FrontDesk from '../views/FrontDeskViews/Index.vue'
import FrontDeskHomePage from '../views/FrontDeskViews/HomePage.vue'
import FrontDeskSignin from '../views/FrontDeskViews/Signin.vue'
import FrontDeskLogin from '../views/FrontDeskViews/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/doctor',
    component: Doctor,
    children: [
      {
        path: '',
        name: 'DoctorHomePage',
        component: DoctorHomePage
      },
      {
        path: 'signin',
        name: 'DoctorSignin',
        component: DoctorSignin
      },
      {
        path: 'login',
        name: 'DoctorLogin',
        component: DoctorLogin
      }
    ]
  },
  {
    path: '/administrator',
    component: Admin,
    children: [
      {
        path: '',
        name: 'AdminHomePage',
        component: AdminHomePage
      },
      {
        path: 'login',
        name: 'AdminLogin',
        component: AdminLogin
      },
      {
        path: 'verifyEmployees',
        name: 'VerifyEmployees',
        component: VerifyEmployees
      }
    ]
  },
  {
    path: '/employee',
    component: Employee,
    children: [
      {
        path: '',
        name: 'EmployeeHomePage',
        component: EmployeeHomePage
      },
      {
        path: 'signin',
        name: 'EmployeeSignin',
        component: EmployeeSignin
      },
      {
        path: 'login',
        name: 'EmployeeLogin',
        component: EmployeeLogin
      }
    ]
  },
  {
    path: '/frontdesk',
    component: FrontDesk,
    children: [
      {
        path: '',
        name: 'FrontDeskHomePage',
        component: FrontDeskHomePage
      },
      {
        path: 'signin',
        name: 'FrontDeskSignin',
        component: FrontDeskSignin
      },
      {
        path: 'login',
        name: 'FrontDeskLogin',
        component: FrontDeskLogin
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router