import Logo from './logo192.png';

function Header () {
    return (
        <header>
            <img src={Logo} alt="logo React"/>
            <h1>Testando componentes</h1>
        </header>
    );
};

export default Header;