const express = require("express")
const app = express()

app.use(express.json())

let users = [
  { id: 1, name: "Jin" },
  { id: 2, name: "Kim" },
]

app.put("/api/users/:id", (req, res) => {
  const user = users.find(user => user.id === Number(req.params.id))

  if (!user) {
    return res.status(404).json({ error: "없는 사용자" })
  }

  if (typeof req.body.name !== "string" || req.body.name.trim() === "") {
    return res.status(400).json({ error: "이름을 입력하세요" })
  }

  user.name = req.body.name.trim()
  res.json(user)
})

app.listen(3005, async () => {
  console.log("서버 실행: http://localhost:3005")

  try {
    const response = await fetch("http://localhost:3005/api/users/1", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: "수정된 이름" }),
    })

    console.log(await response.json())
  } catch (error) {
    console.error("요청 실패:", error.message)
  }
})
