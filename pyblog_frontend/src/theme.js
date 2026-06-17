import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#2563EB', // clean blue
      light: '#60A5FA',
      dark: '#1D4ED8',
    },
    secondary: {
      main: '#7C3AED', // purple accent
    },
    background: {
      default: '#F1F5F9', // page bg
      paper: '#FFFFFF', // cards
    },
    text: {
      primary: '#0F172A',
      secondary: '#64748B',
    },
    error: {
      main: '#EF4444',
    },
    success: {
      main: '#22C55E',
    },
  },
  typography: {
    fontFamily: 'Inter, Roboto, sans-serif',
    h1: { fontWeight: 700 },
    h2: { fontWeight: 700 },
    h5: { fontWeight: 600 },
    h6: { fontWeight: 600 },
    button: { textTransform: 'none', fontWeight: 500 }, // disables ALL CAPS on buttons
  },
  shape: {
    borderRadius: 10, // rounded corners everywhere
  },
  spacing: 8, // 1 unit = 8px (default, explicit here for clarity)
});

export default theme;
