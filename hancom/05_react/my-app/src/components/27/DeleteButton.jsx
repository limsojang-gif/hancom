import Button from '@mui/material/Button'

const DeleteButton = () => {
    return (
        <Button variant="contained" color="error" onClick={() => alert('삭제합니다')}>
            삭제
        </Button>
    )
}

export default DeleteButton
