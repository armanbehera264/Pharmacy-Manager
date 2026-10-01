# Pharmacy Manager

A full-stack pharmacy and clinic management system. A **Django REST** backend handles authentication, role-based access and the medicine inventory, and a **Vue 3** single-page app provides separate portals for administrators and doctors.

## Features

**Administrator**
- Sign in with JWT authentication
- Verify newly registered employees before they can log in
- View and manage employee accounts
- Add, view and edit medicines, including stock, price, expiry date, manufacturer, ingredients, categories, side effects and allergen warnings

**Doctor**
- Register (with registration number, specialisation, experience and consultation fee) and log in
- View their own doctor profile

**Platform**
- Role-based users: Admin, Doctor, Pharmacy, FrontDesk, Patient
- Accounts must be verified by an admin before a token is issued
- Short-lived access tokens (20 minutes) with refresh tokens (1 day), refreshed automatically by the frontend

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Django 5, Django REST Framework, Djoser, SimpleJWT, django-cors-headers, python-decouple |
| Database | SQLite |
| Frontend | Vue 3, Vite, Vue Router, Vuex, Axios |
| UI | PrimeVue, PrimeFlex, Tailwind CSS |

## Project structure

```
Pharmacy-Manager/
├── pharmacy_django/            # Backend
│   ├── administrator/          # Custom User model, admin endpoints, JWT auth classes
│   ├── doctor/                 # Doctor, Patient, Appointment, Prescription models + endpoints
│   ├── pharmacy/               # Medicine, ingredient, category, side-effect, allergy, lab test models
│   ├── frontdesk/              # Front desk user
│   ├── api/                    # Custom JWT serializer (adds role to the token)
│   └── pharmacy_django/        # Project settings and root URLs
└── pharmacy_vite/              # Frontend
    └── src/
        ├── views/              # AdminViews/ and DoctorViews/ pages
        ├── router/             # Vue Router config
        ├── store/              # Vuex store
        └── axios.js            # Axios instance with token refresh handling
```

## Getting started

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm

### 1. Backend

```bash
cd pharmacy_django

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies (there is no requirements.txt yet)
pip install "django==5.0.3" djangorestframework djoser djangorestframework-simplejwt \
    django-cors-headers python-decouple PyJWT Pillow
```

Create a `.env` file in `pharmacy_django/` with your own secrets:

```
SECRET_KEY=<your-django-secret-key>
JWT_SECRET=<your-jwt-signing-key>
```

Then set up the database and start the server:

```bash
python manage.py migrate
python manage.py runserver      # http://127.0.0.1:8000
```

To create the first administrator, open a Django shell (`python manage.py shell`) and call `User.objects.create_superuser(...)` from `administrator.models`. It requires `username`, `age`, `gender`, `primary_phone_number`, `role`, `first_name`, `last_name` and a `password`.

### 2. Frontend

```bash
cd pharmacy_vite
npm install
npm run dev                     # http://localhost:5173
```

The frontend expects the API at `http://127.0.0.1:8000` (set in `src/axios.js`). The backend allows CORS from `http://localhost:5173` and `http://localhost:8080`.

## API overview

| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/jwt/create/`, `/api/v1/jwt/refresh/` | POST | Obtain and refresh JWT tokens (Djoser / SimpleJWT) |
| `/administrator/signin/` | POST | Administrator sign-in |
| `/administrator/logout/` | POST | Log out |
| `/administrator/verifyEmployees/` | GET, POST | List and approve pending employees |
| `/administrator/viewEmployees/` | GET, POST | View employees |
| `/administrator/viewMedicines/` | GET, POST | View medicines |
| `/administrator/addMedicines/` | GET, POST | Add a medicine (GET returns the available options) |
| `/doctor/signin/` | POST | Doctor registration |
| `/doctor/doctor/` | GET | Authenticated doctor's profile |
| `/doctor/logout/` | POST | Log out |

Authenticated requests use the header `Authorization: JWT <access_token>`.

## Data model

- **User**: custom user with age, gender, phone numbers, role and an `is_verified` flag
- **DoctorUser / PatientUser**: profile extensions of `User`
- **Appointment**: links a doctor and a patient, with date, time, reason and status
- **Prescription**: tied to an appointment, with prescribed medicines (frequency, timing, duration), prescribed lab tests and a digital signature
- **Medicines**: stock, price, expiry, with many-to-many links to ingredients, categories, side effects and allergies
- **LabTests**: name, description and cost
