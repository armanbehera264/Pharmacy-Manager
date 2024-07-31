import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000'
});

const getAccessToken = () => {
    return localStorage.getItem('accessToken');
};

const getRefreshToken = () => {
    return localStorage.getItem('refreshToken');
}

const refreshAccessToken = () => {
    const refreshToken = getRefreshToken()

    instance.post('/api/v1/jwt/refresh/', { refresh: refreshToken })
    .then( (response) => {
        const accessToken = response.data.access;
        localStorage.setItem('accessToken', accessToken)
        return accessToken
    })
    .catch( (error) => {
        if (error.response.status === 401) {
            console.log("Refresh token expired. Please log in again.")
            const usertype = localStorage.getItem('usertype')
            router.push(`/${usertype}/login`)
        }
        else {
            console.error(error.response)
        }
        return null
    })
}

instance.interceptors.request.use(
    async (config) => {
        let accessToken = getAccessToken();

        if (!accessToken) {
            accessToken = await refreshAccessToken();
        }
        if (accessToken) {
            config.headers['Authorization'] = `JWT ${accessToken}`
        }

        return config;
    },
    (error) => {
        return Promise.reject(error)
    }   
)

instance.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        const originalRequest = error.config

        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true; // Used to prevent infinite retry loops
            const newAccessToken = await refreshAccessToken();
            if (newAccessToken) {
                originalRequest.headers['Authorization'] = `JWT ${newAccessToken}`;
                return instance(originalRequest);
            }
        }
        return Promise.reject(error);
    }
);

export default instance;