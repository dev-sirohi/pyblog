import { useSnackbar } from 'notistack';

export const useToast = () => {
    const { enqueueSnackbar } = useSnackbar();

    return {
        success: (msg) => enqueueSnackbar(msg, { variant: 'success', autoHideDuration: 2000 }),
        error: (msg) => enqueueSnackbar(msg, { variant: 'error', autoHideDuration: 2000 }),
        warn: (msg) => enqueueSnackbar(msg, { variant: 'warning' }),
        info: (msg) => enqueueSnackbar(msg, { variant: 'info' }),
    };
};
