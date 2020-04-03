
import Titles from '../../atomics/titles';
import style from './style.css';

const Header = () => (
	<header class={style.header}>
		<Titles.H1 style={style.h1}>Un sujet, un sentiment</Titles.H1>
	</header>
);

export default Header;
