
export default ({
    value,
    onChange,
    style
}) => {
    return (
        <input type="text" value={value} class={style} onChange={(e) => onChange(e.target.value)}/>
    )
}