import { useState, useEffect } from "react";

const skills = [
    {id: 1, name:'JavaScript'},
    {id: 2, name: 'React'},
    {id: 3, name: 'Vue'},
    {id: 4, name: 'Angular'},
    {id: 5, name: 'TypeScript'},
    {id: 6, name: 'Node.js'},
    {id: 7, name: 'PHP'},
    {id: 8, name: 'Laravel'},
    {id: 9, name: 'WordPress'},
    {id: 10, name: 'CSS/SASS'},

]


function CheckBoxCounter () {

    const [count, setCount] = useState (0);

    const handleChange = (e) => {
        setCount(e.target.checked ? count + 1 : count - 1)
    }

    return (
        <div>

            <ul>
                {skills.map(skill =>
                    <li key = {skill.id}>
                        <input type="checkbox" onChange={handleChange} />
                        {skill.name}
                    </li>
                )}
            </ul>

            {count > 5 && alert ("Hai selezionato più di 5 skill")}

            <h1> Hai selezionato {count} skill. </h1>

        </div>
    );
}

export default CheckBoxCounter;