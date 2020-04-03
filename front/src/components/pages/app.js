import { h, Component } from 'preact';

import Header from '../templates/header';
import Content from '../templates/content';


export default class App extends Component {
	
	render() {
		return (
			<div id="app">
				<Header />
				<Content />
			</div>
		);
	}
}
