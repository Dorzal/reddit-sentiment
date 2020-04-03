import style from './style.css'

export default ({
    onClick,
    children
}) => {
    return (
        <div onClick={onClick} class={style.rectangle}>
            {children}
        </div>
    )
}