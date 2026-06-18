import { Box, Button, TextField, Typography } from '@mui/material';
import { useState } from 'react';
import { Endpoints } from '../endpoints.js';
import { useToast } from '../hooks/useToast.js';
import { call_api, post_with_body } from '../api_utils.js';
import { useNavigate } from 'react-router-dom';
import { Route } from '../page_links.js';
import { isEmptyOrNull } from '../string_utils.js';

const fieldWidth = {
    xs: '90%',
    sm: '60%',
    md: '40%',
    lg: '25%',
};

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const toast = useToast();
    const navigate = useNavigate();

    const initLogin = async () => {
        if (isEmptyOrNull(email)) {
            setEmail('');
            toast.success('Email is required');
            return;
        }
        if (isEmptyOrNull(password)) {
            setPassword('');
            toast.success('Password is required');
            return;
        }
        try {
            const response_data = await call_api(Endpoints.Auth.Login, {
                email: email,
                username: email,
                password: password,
            });
            toast.success('Successfully logged in');
            setTimeout(() => {
                navigate(Route.Home, { replace: true });
            });
        } catch (error) {
            toast.error(error.message);
        }
    };

    return (
        <Box
            sx={{
                minHeight: '100vh',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
            }}
        >
            <TextField
                variant="filled"
                color="primary"
                size="small"
                sx={{
                    padding: 1,
                    margin: 1,
                    width: fieldWidth,
                }}
                placeholder="Email or Username"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            ></TextField>
            <TextField
                variant="filled"
                color="primary"
                size="small"
                sx={{
                    padding: 1,
                    margin: 1,
                    width: fieldWidth,
                }}
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            ></TextField>
            <Button
                variant="contained"
                size="small"
                sx={{
                    padding: 1,
                    margin: 1,
                    width: fieldWidth,
                }}
                onClick={initLogin}
            >
                Login
            </Button>
        </Box>
    );
}

export default Login;
