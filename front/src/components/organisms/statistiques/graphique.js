import { useState, useEffect } from 'preact/hooks';
import { Line } from 'react-chartjs-3';

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
          data: [0.1, 0.3, 0.42, 0.45, 0.6, 0.1, -0.5, -2, 1, 1.5, -0.30, -0.1]
      }
    ]
  };
  
const Graph = () => {
    const [datas, SetDatas] = useState(initialState)

	useEffect(() => {
        setInterval(function(){
            console.log("YO")
			var oldDataSet = datas.datasets[0];
			var newData = [];

			for(var x=0; x< datas.labels.length; x++){
				newData.push(Math.random());
			}

			var newDataSet = {
				...oldDataSet
			};

			newDataSet.data = newData;

			var newState = {
				...initialState,
				datasets: [newDataSet]
			};

			SetDatas(newState);
		}, 5000);
    }, [])
	
    return (
        <Line
        data={datas} 
        options={{
            maintainAspectRatio: false
        }}/>
    );
	
};
  

export default () => {
    return (
        <div style={{height: "75vh"}}>
            <Graph />
        </div>
    )
}