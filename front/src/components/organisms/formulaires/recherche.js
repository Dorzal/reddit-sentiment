
import InputsWithLabel from '../../molecules/inputsWithLabel';
import style from './style.css'
export default ({
    label,
    inputVal,
    onInputChange
}) => (
    <div class={style.formulaire}>
        <InputsWithLabel.Vertical 
        label={label}
        input={inputVal}
        onInputChange={onInputChange}
        />
    </div>
)
