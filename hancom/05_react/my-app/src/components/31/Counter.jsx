import { useState } from "react";
import './Counter.css';

const Counter = () => {
    const [count, setCount] = useState(0)
    
  return (
    /* 빈 태그 대신 CSS 클래스가 들어간 div로 묶어줍니다 
      리셋에도 classNamed을 붙여 준다 . */
    <div className="counter-container">
      <button onClick={() => setCount(c => c-1)}>-1</button>
      <span>{count}</span>
      <button onClick={() => setCount(c => c+1)}>+1</button>
      
      <button className="reset-btn" onClick={() => setCount(0)}>리셋</button>
    </div>
  )
}
export default Counter