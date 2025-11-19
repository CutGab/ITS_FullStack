class TaskManager:

    def __init__(self, tasks: dict [str, bool | str] = {}) -> None:
        self.tasks = tasks

    def create_task(self, task_id: str, descrizione: str) -> dict | str:
        if task_id in self.tasks:
            return "Errore, la task esiste già."
        
        else:
            self.tasks[task_id] = {"Descrizione": descrizione,
                                   "Completato": False
                                   }

    def complete_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore, task non trovata."
        
        else:
            if self.tasks[task_id]["Completato"]:
                return "Task già completata."
            
            else:
                self.tasks[task_id]["Completato"] = True
                return self.tasks[task_id]
            
    
    def update_description(self, task_id: str, new_descrizione: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore, task non trovata."
            
        else:
            self.tasks[task_id]["Descrizione"] = new_descrizione
            return self.tasks[task_id]
        
    def remove_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore, task non trovata."
        
        else:
            return self.tasks.pop(task_id)
        

    def list_tasks(self) -> list[str]:
        
        return list(self.tasks.keys())
    

    def get_task(self, task_id: str) -> list[str]:
        if task_id not in self.tasks:
            return "Errore, task non trovata."
        
        else:
            return self.tasks[task_id]
        