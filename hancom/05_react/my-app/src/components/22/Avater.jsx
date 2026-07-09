import './Avater.css'

const Avater = ({name, online}) => {
    return(
        <>
            <h1>{name}</h1>
            {online && <p>👍</p>}
        </>
    )
}
export default Avater