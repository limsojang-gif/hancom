import { useEffect } from "react";

const Hello = () => {
    useEffect (() => {
        console.log("화면 들때 1번만 실행 되")
    }, [])

    return <p>안녕하세요</p>
}

export default Hello