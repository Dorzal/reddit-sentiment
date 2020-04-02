
import InputsWithLabel from '../../molecules/inputsWithLabel';
import Button from '../../atomics/buttons';

import style from './style.css'

export default ({
    label,
    inputVal,
    onValid,
    onInputChange
}) => (
    <div class={style.formulaire}>
        <InputsWithLabel.Vertical 
        label={label}
        input={inputVal}
        onInputChange={onInputChange}
        />
        <Button.Rectangle onClick={onValid}>Rechercher</Button.Rectangle>
    </div>
)
