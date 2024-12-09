

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

        if (error.response.status === 401 && !originalRequest._retry) {
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