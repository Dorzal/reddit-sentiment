import { useState, useEffect } from 'preact/hooks';
import { Line } from 'react-chartjs-3';
 
const Graph = ({
    results
}) => {
    const [datas, SetDatas] = useState(results)

    useEffect(() => {
        SetDatas(results);
    }, [results])

    return (
        <Line
        data={datas} 
        options={{
            maintainAspectRatio: false
        }}/>
    );
	
};
  

export default ({
    results
}) => {
    return (
        <div style={{height: "75vh"}}>
            <Graph results={results}/>
        </div>
    )
}