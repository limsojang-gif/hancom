import { useState } from 'react'
import './ProductItem.css' // CSS 파일 불러오기

const ProductItem = ({ name }) => {
    const [count, setCount] = useState(0)

    return (
        /* 전체를 감싸면서 정렬을 담당할 박스
         */
        <div className="product-container">
            <h3>{name}</h3>
            <p>{count}개 담음</p>
            
            
            <button className="add-btn" onClick={() => setCount(c => c + 1)}>
                product 담기
            </button>
        </div>
    )
}

export default ProductItem