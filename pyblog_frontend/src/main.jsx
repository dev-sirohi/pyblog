import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.jsx';
import { ThemeProvider } from '@mui/material/styles';
import theme from './theme.js';
import { SnackbarProvider } from 'notistack';

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <ThemeProvider theme={theme}>
            <SnackbarProvider maxSnack={3}>
                <App />
            </SnackbarProvider>
        </ThemeProvider>
    </StrictMode>
);
