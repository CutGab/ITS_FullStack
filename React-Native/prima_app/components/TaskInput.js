import { useState } from 'react';
import { View, TextInput, Button, StyleSheet } from 'react-native';

export default function TaskInput({ onAddTask }) {
  const [task, setTask] = useState('');

  // Update state when user types
  const taskInputHandler = (enteredTask) => setTask(enteredTask);

  // Call the parent handler and reset input
  const addTaskHandler = () => {
    if (task.trim() === '') return; // prevent empty tasks
    onAddTask(task);
    setTask('');
  };

  return (
    <View style={styles.inputContainer}>
      <TextInput
        style={styles.textInput}
        placeholder="Inserisci task..."
        value={task}
        onChangeText={taskInputHandler}
      />
      <Button
        title="Aggiungi"
        onPress={addTaskHandler}
        disabled={task.trim() === ''}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  inputContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  textInput: {
    borderWidth: 1,
    borderColor: '#000',
    width: '70%',
    padding: 8,
    borderRadius: 6,
    backgroundColor: '#fff',
  },
});
