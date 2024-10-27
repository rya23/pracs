import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import App from "./App.jsx"
import Display from "./Display.jsx"
import Routing from "./Routing.jsx"
import Keys from "./Keys.jsx"
import Refer from "./Refer.jsx"

createRoot(document.getElementById("root")).render(
    <StrictMode>
        {/* <App />  */}
        <Keys />
        {/* <Routing /> */}
        <Refer />
    </StrictMode>
)
