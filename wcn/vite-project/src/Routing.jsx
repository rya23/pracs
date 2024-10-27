import React from "react"

import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom"

const Home = () => {
    return <div> Home</div>
}

const About = () => {
    return <div> About</div>
}
const Routing = () => {
    return (
        <Router>
            <nav>
                <Link to="/home">Home</Link>
                <Link to="/about">About</Link>
            </nav>

            <Routes>
                <Route path="/home" element={<Home />} />
                <Route path="/about" element={<About />} />
            </Routes> 
        </Router>
    )
}

export default Routing
