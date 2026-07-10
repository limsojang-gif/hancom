import { useState, useEffect } from "react";
import './Every.css';


const Every = () => {
    const [count, setCount] = useState(0)

    useEffect(() => {
        console.log('렌더링 될때 마다 실행 중')
    })

      return <button onClick={() => setCount(c => c +1)}>{count}</button>
    }
export default Every