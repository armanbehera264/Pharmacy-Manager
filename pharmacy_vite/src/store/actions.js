export const setUserType = ({ commit }, payload) => {
    localStorage.setItem('usertype', payload);
    commit('setUserType', payload);
}

export const setUsername = ({ commit }, payload) => {
    localStorage.setItem('username', payload);
    commit('setUsername', payload);
}

export const setIsRegistered = ({ commit }, payload) => {
    localStorage.setItem('isRegistered', JSON.stringify(payload));
    commit('setIsRegistered', payload);
}

export const updateState = ({ commit, getters }) => {
    const isRegistered = getters.isRegistered;

    if (isRegistered) {
        const userDetails= getters.getUserDetails;
        commit('setIsRegistered', true);
        commit('setUsername', userDetails.username);
        commit('setUserType', userDetails.usertype);
    }
}

export const logout = ({ commit }) => {
    localStorage.setItem('usertype', '');
    localStorage.setItem('username', '');
    localStorage.setItem('isRegistered', JSON.stringify(false));
    commit('logout');
}