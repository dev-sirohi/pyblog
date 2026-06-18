import { Box } from '@mui/material';
import { useParams } from 'react-router-dom';
import { useCallback, useEffect, useState } from 'react';
import { call_api } from '../api_utils.js';
import { Endpoints } from '../endpoints.js';
import { useToast } from '../hooks/useToast.js';

export default function BlogEntry() {
    const [loading, setLoading] = useState(false);
    const toast = useToast();
    const params = useParams();
    const [entry, setEntry] = useState({});
    const [entryId, setEntryId] = useState(params.id);

    const fetchEntry = useCallback(async () => {
        try {
            const entryData = await call_api(Endpoints.Post.Entry, entryId);
            setEntry(entryData);
        } catch (error) {
            toast.error(error.message);
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchEntry();
    }, [fetchEntry, entryId]);

    return <Box></Box>;
}
