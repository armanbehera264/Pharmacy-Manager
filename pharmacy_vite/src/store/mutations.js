export default {
    setUserType(state, usertype) {
        state.usertype = usertype;
    },

    setIsRegistered(state, isRegistered) {
        state.isRegistered = isRegistered;
    },

    setUsername(state, username) {
        state.username = username;
    },
    
    setRefreshToken(state, refresh) {
        state.refreshToken = refresh
    },

    setAccessToken(state, access) {
        state.accessToken = access
    },

    logout (state) {

        state.usertype = '';
        state.isRegistered = false;
        state.username = '';
        state.accessToken = '';
        state.refreshToken = '';
    }
}