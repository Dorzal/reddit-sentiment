import { h } from 'preact';
import { useState } from 'preact/hooks';
import style from './style.css'
import Formulaires from '../../organisms/formulaires';
import Titles from '../../atomics/titles';

export default () => {
	const [results, setResults] = useState(false)
	const [inputval, setInputVal] = useState('');

	const rechercher = (val) => {
		alert(val)
		setInputVal(val)
	}

	return (
		<div id={style.content}>
			<div onClick={() => setSearched(false)}>
				
				<Formulaires.Recherche
					inputVal={inputval}
					onInputChange={(val) => rechercher(val)}
					label={<Titles.H1>Rechercher un sujet</Titles.H1>}
					style={{formulaire: style.formulaire, input: style.input, label: style.label}}
				/>
			</div> 
			
		</div>
	)
}
