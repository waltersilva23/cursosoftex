import { BrowserRouter } from 'react-router-dom'

import Header from "./components/Header";
import Footer from "./components/Footer";

import Rotas from './Rotas';

function App() {
  return (
        <BrowserRouter>
          <Header/>

          <Rotas/> 

          <Footer/>
        </BrowserRouter>
  );
}

export default App;
