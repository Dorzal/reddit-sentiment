import { h } from 'preact';
import { useState } from 'preact/hooks';
import style from './style.css'
import Loader from '../../atomics/loader'
import Formulaires from '../../organisms/formulaires';
import Titles from '../../atomics/titles';
import Statistiques from '../../organisms/statistiques';
import moment from 'moment'
import ReactNotifications, {store} from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css'
import 'animate.css';

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
	const [loading, setLoading] = useState(false)
	const [results, setResults] = useState(initialState)
	const [inputval, setInputVal] = useState('');

	const rechercher = () => {
		setLoading(true);
		
		fetch(`http://localhost:5000/api/data?sujet=${inputval}`)
		.then(response => response.json())
		.then(json => {
			if (json.result == false) {
				store.addNotification({
					message: 'Nous collectons les données merci de rééssayer dans quelques secondes',
					insert: "top",
  					container: "top-right",
					type: 'info',                         // 'default', 'success', 'info', 'warning'
					animationIn: ["animated", "fadeIn"],     // animate.css classes that's applied
					animationOut: ["animated", "fadeOut"],   // animate.css classes that's applied
					dismiss: {
					  duration: 3000 
					}
				  })
			} else {
				let labels = json.result.map(res => { return moment(res.date).format('MMMM Do YYYY, h')})
				let datas = json.result.map(res => { return res.polarite})
				changeGraphiqueDatas(labels, datas);
			}
			setLoading(false);
		})
		
	}

	const changeGraphiqueDatas = (newLabels, newDatasets) => {
		var oldDataSet = results.datasets[0];
		var newData = newDatasets;
		var newDataSet = {
			...oldDataSet
		};
		newDataSet.data = newData;
		var newState = {
			...initialState,
			labels: newLabels,
			datasets: [newDataSet]
		};

		setResults(newState);
	}

	return (
		<div id={style.content}>
			<div>
				<ReactNotifications />
				<Formulaires.Recherche
					inputVal={inputval}
					onValid={(val) => rechercher(val)}
					onInputChange={(val) => setInputVal(val)}
					label={<Titles.H2>Rechercher un sujet</Titles.H2>}
					style={{formulaire: style.formulaire, input: style.input, label: style.label}}
				/>
				<Statistiques.Graphique results={results}/>
				<Loader.Fullscreen loading={loading}/>
			</div> 
			
		</div>
	)
}
