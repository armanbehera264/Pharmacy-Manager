import axios from 'axios';
import router from './router';

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000'
});

const getAccessToken = () => {
    return localStorage.getItem('accessToken');
};

const getRefreshToken = () => {
    return localStorage.getItem('refreshToken');
}

const refreshAccessToken = async () => {
    const refreshToken = getRefreshToken();

    if (!refreshToken) {
        return null;
    }

    try {
        const response = await instance.post('/api/v1/jwt/refresh', { refresh: refreshToken });
        const accessToken = response.data.access;
        localStorage.setItem('accessToken', accessToken);
        return accessToken;
    } catch (error) {
        console.log(`Refresh token error: ${error}`);
        return null; // The refresh token is invalid or expired.
    }
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

        console.log(`Error: ${error.response.status}`)

        if (error.response.status === 403 && !originalRequest._retry) {
            originalRequest._retry = true;
            const newAccessToken = await refreshAccessToken();
            console.log(`Access Token: ${newAccessToken}`)
            if (newAccessToken) {
                originalRequest.headers['Authorization'] = `JWT ${newAccessToken}`;
                return instance(originalRequest);
            }
        }

        if (error.response.status === 401) {
            console.error(error)
            const usertype = localStorage.getItem('usertype')
            router.push(`/${usertype}/login`)
        }

        return Promise.reject(error);
    }
)

export default instance;