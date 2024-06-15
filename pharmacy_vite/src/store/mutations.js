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

    logout (state) {

        state.usertype = '';
        state.isRegistered = false;
        state.username = '';
    }
}