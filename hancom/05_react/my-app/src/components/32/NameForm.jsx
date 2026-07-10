import { useState } from "react";
import { TextField, Typography, Box } from '@mui/material';

const NameForm = () => {
    const [name, setName] = useState("");

    return (
        /* Box를 사용해 여백과 가운데 정렬을 설정합니다 */
        <Box sx={{ padding: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 3 }}>
            
            {/* 기본 input 대신 TextField를 사용합니다 */}
            <TextField 
                label="이름을 입력해" 
                variant="outlined" 
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            
            {/* 기본 p 태그 대신 Typography를 사용합니다 */}
            <Typography variant="h5" color="primary" fontWeight="bold">
                안녕 {name}!
            </Typography>
            
        </Box>
    )
}

export default NameForm;