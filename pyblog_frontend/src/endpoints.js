import { isEmptyOrNull } from './string_utils.js';

if (isEmptyOrNull(import.meta.env.VITE_API_BASE)) {
    throw new Error('API_BASE not set');
}
export const Base = import.meta.env.VITE_API_BASE;

export const Endpoints = {
    Auth: {
        Login: '/v1/auth/login',
        Register: '/v1/auth/register',
        Logout: '/v1/auth/logout',
    },
};
