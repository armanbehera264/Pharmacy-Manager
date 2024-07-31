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
        const accessToken = localStorage.getItem('accessToken')

        return {'usertype' : usertype, 'username' : username, 'refreshToken': refreshToken, 'accessToken': accessToken}
    }
    return {'usertype' : '', 'username' : '', 'refreshToken': '', 'accessToken': ''}
}