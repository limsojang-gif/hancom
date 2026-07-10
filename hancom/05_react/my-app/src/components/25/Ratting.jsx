const Rating = ({ score }) => {
    return (
        <div>
            {[...Array(30)].map((_, i) => (

            <span key={i}>{i < score ? '👍' : '❤️'}</span>
            
            
            ))}
        </div>
    
    )
}
export default Rating 