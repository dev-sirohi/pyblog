import { Box, Typography } from '@mui/material';
import { useCallback, useEffect, useState } from 'react';
import { call_api, get, post_with_query } from '../api_utils.js';
import { useToast } from '../hooks/useToast.js';
import { Endpoints } from '../endpoints.js';

export default function Home() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [page, setPage] = useState(1);
    const toast = useToast();

    const fetchPosts = useCallback(async () => {
        try {
            const newPosts = await call_api(Endpoints.Feed.Feed);
            setPosts(newPosts);
        } catch (error) {
            toast.error(error.message);
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        void fetchPosts();
    }, [fetchPosts, page]);

    return (
        <Box
            sx={{
                width: '100%',
                height: '100vh',
                display: 'flex',
                justifyContent: 'center',
                backgroundColor: 'lightblue',
            }}
        >
            <Box
                sx={{
                    width: '50%',
                    display: 'flex',
                    flexDirection: 'row',
                    justifyContent: 'center',
                    backgroundColor: 'lightgreen',
                }}
            ></Box>
        </Box>
    );
}
