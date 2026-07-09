import './Card.css'

const Card =({ title, desc, emogi}) => {
    return (
        <div className="card">
            <span>{title}</span>
            <h3>{desc}</h3>
            <p>{emogi}</p>
        </div>
       
    )
}

export default Card