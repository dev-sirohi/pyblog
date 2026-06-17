import { isEmptyOrNull } from './string_utils.js';
import { Base } from './endpoints.js';

export const HttpVerb = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
    DELETE: 'DELETE',
};

export const get = async (endpoint = '') => {
    if (isEmptyOrNull(endpoint)) {
        throw new Error('Invalid endpoint');
    }
    let response, data;
    try {
        response = await fetch(Base.concat(endpoint), {
            method: HttpVerb.GET,
            headers: {
                'Content-Type': 'application/json',
            },
        });
        data = await response.json();
    } catch (error) {
        throw new Error('Network error');
    }
    if (!response.ok) {
        throw new Error(data.Message);
    }
    return data;
};

export const post_with_query = async (endpoint = '', params = {}) => {
    if (isEmptyOrNull(endpoint)) {
        throw new Error('Invalid endpoint');
    }
    let response, data;
    try {
        response = await fetch(Base.concat(endpoint).concat('?').concat(buildQueryParamStr(params)), {
            method: HttpVerb.POST,
            headers: {
                'Content-Type': 'application/json',
            },
        });
        data = await response.json();
    } catch (error) {
        throw new Error('Network error');
    }
    if (!response.ok) {
        throw new Error(data.Message);
    }
    return data;
};

export const post_with_body = async (endpoint = '', payload = {}) => {
    if (isEmptyOrNull(endpoint)) {
        throw new Error('Invalid endpoint');
    }
    if (!payload) {
        throw new Error('Invalid payload');
    }
    let response, data;
    try {
        response = await fetch(Base.concat(endpoint), {
            method: HttpVerb.POST,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });
        data = await response.json();
        if (!response.ok) {
            throw new Error(data.Message);
        }
    } catch (error) {
        throw new Error('Network error');
    }
    return data;
};

export const buildQueryParamStr = (params) => {
    if (!params) {
        throw new Error('Invalid params');
    }
    return Object.keys(params)
        .map((key) => {
            if (isEmptyOrNull(key)) {
                throw new Error('Invalid params key');
            }
            if (isEmptyOrNull(params[key])) {
                throw new Error('Invalid params value');
            }
            return `${key}=${params[key]}`;
        })
        .join('&');
};
