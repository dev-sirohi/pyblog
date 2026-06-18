import { isEmptyOrNull } from './string_utils.js';

if (isEmptyOrNull(import.meta.env.VITE_API_BASE)) {
    throw new Error('API_BASE not set');
}
export const Base = import.meta.env.VITE_API_BASE;

export const HttpVerb = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
    DELETE: 'DELETE',
};

export const PayloadType = {
    QUERY: 'QUERY_PARAMS',
    BODY: 'BODY',
};

export const Endpoints = {
    Auth: {
        Login: {
            url: '/v1/auth/login',
            method: HttpVerb.POST,
            payloadType: PayloadType.BODY,
        },
        Register: {
            url: '/v1/auth/register',
            method: HttpVerb.POST,
            payloadType: PayloadType.BODY,
        },
        Logout: {
            url: '/v1/auth/logout',
            method: HttpVerb.POST,
            payloadType: PayloadType.QUERY,
        },
    },
    Feed: {
        Feed: {
            url: '/v1/feed',
            method: HttpVerb.GET,
            payloadType: PayloadType.QUERY,
        },
        DiscoveryFeed: {
            url: '/v1/feed/discovery',
            method: HttpVerb.POST,
            payloadType: PayloadType.QUERY,
        },
    },
    Post: {
        Entry: {
            url: '/v1/post/',
            method: HttpVerb.POST,
            payloadType: PayloadType.QUERY,
        },
    },
};
