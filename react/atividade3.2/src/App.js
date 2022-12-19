import {useState, useEffect} from 'react';

function App() {

  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Você clicou ${count} vezes`;
  });

  return (
    <div>
      <p>Você clicou {count} vezes</p>
      <button onClick={() => setCount(count + 1)}>
        Clique aqui
      </button>
      {/* para diminuir é só colocar count - 1 */}
    </div>
  );
}

export default App;
