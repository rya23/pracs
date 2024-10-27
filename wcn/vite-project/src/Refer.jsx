import React, { useRef, useState } from "react"

const Refer = () => {
    let ref = useRef(0)
    const [count, setcount] = useState(0)
    function handleClick() {
        ref.current = ref.current + 1
        setcount(count + 1)
        alert("You Clicled " + ref.current + " times!!")
    }

    return (
        <div>
            <button onClick={handleClick}>Click me</button>
            {ref.current}
        </div>
    )
}

export default Refer
