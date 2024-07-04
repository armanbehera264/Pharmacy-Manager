export function setCookie(name, value, expiryHours) {
    const now = new Date();
    now.setTime(now.getTime() + (expiryHours * 60 * 60 * 1000)); // Milliseconds in hours
    const expires = `expires=${now.toUTCString()}`;
    document.cookie = `${name}=${value}; ${expires}; SameSite=Lax; Secure`;
}