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

    instance.post('api/v1/jwt/refresh', { refresh: refreshToken })
    .then( (response) => {
        const accessToken = response.data.access;
        localStorage.setItem('accessToken', accessToken)
        return accessToken
    })
}

instance.interceptors.request.use(
    async(config) => {
        let accessToken = getAccessToken();

        if (accessToken) {
            config.headers['Authorization'] = `JWT ${accessToken}`
        }

        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

instance.interceptors.response.use(
    (response) => {
        return response
    },
    async (error) => {
        const originalRequest = error.config

        console.log(error.response.status)
        if (error.response.status === 403 && !originalRequest._retry) {
            originalRequest._retry = true;
            const newAccessToken = await refreshAccessToken();
            if (newAccessToken) {
                originalRequest.headers['Authorization'] = `JWT ${newAccessToken}`;
                return instance(originalRequest);
            }
        }
        return Promise.reject(error);
    }
)

export default instance;