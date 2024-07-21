export function setCookie(name, value) {

    document.cookie = `${name}=${value}; SameSite=Lax; path=`;
}

export function getCookieValue(cookieName) {

    const name = cookieName + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';'); // Splits all cookies into separate elements

    // Returns the cookie itself which matches the name
    for(let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}