export const isEmptyOrNull = (str, strip = false) => {
    return !(typeof str === 'string' && str.length > 0 && (!strip || str.trim().length > 0));
};
