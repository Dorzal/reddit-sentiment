import Inputs from '../../atomics/inputs/index'
import Labels from '../../atomics/labels/index'

import style from './style.css'

export default ({
    label,
    value,
    onInputChange
}) => {
    return (
        <div class={style.vertical}>
            <Labels.Simple style={style.label}>{label}</Labels.Simple>
            <Inputs.Text value={value}  style={style.vertical.input} onChange={onInputChange}/>
        </div>
    )
}