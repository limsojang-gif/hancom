import { useState, useEffect } from "react";
import './Clock.css';

const Clock = () => {
  
  const [time, setTime] = useState(new Date().toLocaleTimeString())

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString())  
    }, 1000)                                     
    return () => clearInterval(timer)   
  }, [])                                // [] = 처음 1번만 등록

  return (
    <p className="clock-text">
      ⏰ o(≧▽≦)o 
      
     {/* 시간 부분만 span 태그로 감싸고 이름표를 달아줍니다 */}
      <span className="time-highlight">{time}</span> 
      
      o(≧▽≦)o ⏰
    </p>
  )
}
export default Clock