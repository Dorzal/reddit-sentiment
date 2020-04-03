import { h } from 'preact';
import { useState } from 'preact/hooks';
import style from './style.css'
import Formulaires from '../../organisms/formulaires';
import Titles from '../../atomics/titles';
import Statistiques from '../../organisms/statistiques';

export default () => {
	const [results, setResults] = useState(false)
	const [inputval, setInputVal] = useState('');

	const rechercher = () => {
		alert(inputval)
		setInputVal(inputval)
	}

	return (
		<div id={style.content}>
			<div onClick={() => setSearched(false)}>
				
				<Formulaires.Recherche
					inputVal={inputval}
					onValid={(val) => rechercher(val)}
					onInputChange={(val) => setInputVal(val)}
					label={<Titles.H2>Rechercher un sujet</Titles.H2>}
					style={{formulaire: style.formulaire, input: style.input, label: style.label}}
				/>
				<Statistiques.Graphique />
			</div> 
			
		</div>
	)
}
