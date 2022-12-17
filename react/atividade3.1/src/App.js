import './App.css';
import Dados from './components/Dados';


function App() {

  const nome='Walter'
  const idade='31 anos'
  const curso='front-end'
  
  return (
  <>
    <Dados nome={nome} idade={idade} curso={curso} />
  </>
  )
}

export default App;
