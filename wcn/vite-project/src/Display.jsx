import React from "react"

const Display = (props) => {
    return (
        <div>
            <p>Name: {props.name}</p>
            <p>Email: {props.email}</p>
        </div>
    )
}

export default Display
