import { Card, CardContent, Button, Stack } from '@mui/material'

const Menu = () => {
    return (
        <Card>
            <CardContent>
                {/* Stack 컴포넌트로 버튼들을 가로로 묶어줍니다 */}
                <Stack direction="row" spacing={2} justifyContent="center">
                    <Button variant="outlined">블로그</Button>
                    <Button variant="contained">홈</Button>
                    <Button variant="outlined">그림</Button>
                </Stack>
            </CardContent>
        </Card>
    )
}

export default Menu