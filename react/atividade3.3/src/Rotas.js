import { Routes, Route } from 'react-router-dom';

import Home from './pages/Home'
import Sobre from './pages/Sobre'

function Rotas () {
    return (
        <Routes>
            <Route exact path="/" element={<Home/>}/>
            <Route exact path="/sobre" element={<Sobre/>}/>
        </Routes>
    );
}

export default Rotas;