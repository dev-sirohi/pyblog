import './App.css';
import Login from './pages/login.jsx';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/home.jsx';
import BlogEntry from './pages/blog_entry.jsx';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<Home />} />
                <Route path="/entry:id" element={<BlogEntry />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
