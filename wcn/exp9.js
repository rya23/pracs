const { time, log } = require("console")
const fs = require("fs")

fs.readFile("example.txt", "utf8", (err, data) => {
    if (err) {
        console.log(err)
    } else {
        console.log(data)
    }
})

// Event Looop

console.log("Start")

setTimeout(() => {
    console.log("Inside timeout")
}, 1000)

console.log("End")

//  Express

const express = require("express")
const app = express()

const port = 3000

app.use("/", (req, res) => {
    res.send("Hello")
})
app.listen(port, () => {
    console.log(`Listening on http://localhost:${port}`)
})
