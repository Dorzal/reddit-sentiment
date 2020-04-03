import { h } from 'preact';
import { useState } from 'preact/hooks';
import style from './style.css'
import Formulaires from '../../organisms/formulaires';
import Titles from '../../atomics/titles';
import Statistiques from '../../organisms/statistiques';


const initialState = {
    labels: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Setptembre', 'Octobre', 'Novembre', 'Décembre'],
    datasets: [
      {
          label: 'Evolution des sentiments',
          backgroundColor: 'rgba(103, 58, 183,0.2)',
          borderColor: 'rgba(103, 58, 183,1)',
          borderWidth: 4,
          hoverBackgroundColor: 'rgba(255,99,132,0.4)',
          hoverBorderColor: 'rgba(255,99,132,1)',
          data: []
      }
    ]
  };

export default () => {
	const [results, setResults] = useState(initialState)
	const [inputval, setInputVal] = useState('');

	const rechercher = () => {
		
		changeGraphiqueDatas([0.1, 0.3, 0.42, 0.45, 0.6, 0.1, -0.5, -2, 1, 1.5, -0.30, -0.1])
		fetch(`http://localhost:5000/api/data?subject=${inputval}`)
		.then(response => response.json())
		.then(json => {
			//
		})
	}

	const changeGraphiqueDatas = (newDatasets) => {
		var oldDataSet = results.datasets[0];
		var newData = newDatasets;
		var newDataSet = {
			...oldDataSet
		};
		newDataSet.data = newData;
		var newState = {
			...initialState,
			datasets: [newDataSet]
		};

		setResults(newState);
	}

	return (
		<div id={style.content}>
			<div>
				<Formulaires.Recherche
					inputVal={inputval}
					onValid={(val) => rechercher(val)}
					onInputChange={(val) => setInputVal(val)}
					label={<Titles.H2>Rechercher un sujet</Titles.H2>}
					style={{formulaire: style.formulaire, input: style.input, label: style.label}}
				/>
				<Statistiques.Graphique results={results}/>
			</div> 
			
		</div>
	)
}
