export const initializeStore = ({ commit, getters }) => {
    const isRegistered = getters.isRegistered;

    if (isRegistered) {
        const userDetails= getters.getUserDetails;
        commit('setIsRegistered', true);
        commit('setUsername', userDetails.username);
        commit('setUserType', userDetails.usertype);
        commit('setRefreshToken', userDetails.refreshToken);
        commit('setAccessToken', userDetails.accessToken);
    }
}

export const logout = ({ commit }) => {
    localStorage.setItem('usertype', '');
    localStorage.setItem('username', '');
    localStorage.setItem('isRegistered', JSON.stringify(false));
    localStorage.setItem('refreshToken', '');
    localStorage.setItem('accessToken', '')
    commit('logout');
}

export const setLoginDetails = ({ commit }, payload) => {
    localStorage.setItem('usertype', payload.usertype);
    localStorage.setItem('username', payload.username);
    localStorage.setItem('isRegistered', JSON.stringify(payload.isRegistered));
    localStorage.setItem('refreshToken', payload.refreshToken);

    commit('setUserType', payload.usertype);
    commit('setUsername', payload.username);
    commit('setIsRegistered', payload.isRegistered);
    commit('setRefreshToken', payload.refreshToken);
    commit('setAccessToken', payload.accessToken);
}