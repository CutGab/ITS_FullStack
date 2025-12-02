const rootDiv = document.getElementById("root");
const root = ReactDOM.createRoot(rootDiv);

const App = () => {
    return (

        <div>
            <h1 className="h1"> Lista Skill </h1>
            <Tabella />


        </div>



    );
}

const Tabella = () => {
    return (

        <div>
            <ul className="main">
                <li className="php"> PHP </li>
                <li className="js"> JS </li>
                <li className="html"> HTML </li>
            </ul>
        </div>
    );
}

root.render(<App />)
