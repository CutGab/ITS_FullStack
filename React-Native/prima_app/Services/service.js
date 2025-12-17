const TASK_URL = "https://todoapp-76f34-default-rtdb.europe-west1.firebasedatabase.app/tasks";

async function handlerResponse(response) {
    if (!response.ok) {
        const errorText=response.text();
        throw new Error("Fire base error: "+response.status+" "+errorText)

    }
    response.json()
}

export async function fetchTasks() {
    try {
    const response = await fetch(TASK_URL+".json")
    const data = await handlerResponse(response)
    if(!data) {
        return []
    }

    return Object.keys(data).map(([id, value]) => ({
        id,
        text: value.text,
        done: Boolean(value.done)
        // ...data[d]
    }))

    } catch(err) {
        console.error("ERRORE fetchTasks: "+ err)
    }
}