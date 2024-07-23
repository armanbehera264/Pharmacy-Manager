export const isRegistered = state => {
    const isRegistered = localStorage.getItem('isRegistered');

    if (isRegistered !== null) {
        if (isRegistered === 'true') {

            const usertype = localStorage.getItem('usertype');
            const username = localStorage.getItem('username');

            if (usertype !== null && username !== null) {
                return true
            }
        }
    }
    return false
}

export const getUserDetails = state => {

    if (isRegistered) {

        const usertype = localStorage.getItem('usertype');
        const username = localStorage.getItem('username');
        const refreshToken = localStorage.getItem('refreshToken')

        return {'usertype' : usertype, 'username' : username, 'refreshToken': refreshToken}
    }
    return {'usertype' : '', 'username' : '', 'refreshToken': ''}
}