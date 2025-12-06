import { useState, useEffect } from "react";
import { Button, StyleSheet, Text, TextInput, View, Image, FlatList } from "react-native";
import { Divider } from '@rneui/themed';

export default function App() {
  const [task, setTask] = useState("");
  const [taskList, setTaskList] = useState([]);
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const taskInputHandler = (enteredTask) => setTask(enteredTask);

  const addTaskHandler = () => {
    if (task.trim() === "") return;
    setTaskList((current) => [...current, task]);
    setTask("");
  };

  const renderTaskItem = ({ item }) => (
    <View style={styles.taskItem}>
      <Text style={styles.taskText}>{item}</Text>
    </View>
  );

  return (
    <View style={styles.appContainer}>
      <View style={styles.header}>
        <Text style={styles.dayText}>Task di Oggi</Text>
        <Divider color="black" width={1} style={styles.divider} />
        <Text style={styles.dayText}>{currentTime.toLocaleTimeString()}</Text>
      </View>

      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          placeholder="Inserisci task..."
          value={task}
          onChangeText={taskInputHandler}
        />
        <Button title="Aggiungi" onPress={addTaskHandler} disabled={task.trim() === ""} />
      </View>

      <Image
        style={styles.image}
        source={{ uri: 'https://media1.tenor.com/m/VWk_uZZ7sdAAAAAd/don-quixote-qoh.gif' }}
      />

      <View style={styles.goalsContainer}>
        <Text style={styles.sectionTitle}>Lista task</Text>
        <Divider color="black" width={1} style={styles.divider} />
        <FlatList
        alwaysBounceVertical={true}
        data={taskList}
        renderItem={renderTaskItem}
        keyExtractor={(_, index) => index.toString()}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    backgroundColor: "#9052bfff",
    paddingTop: 50,
    paddingHorizontal: 16,
  },
  header: {
    alignItems: 'center',
    marginBottom: 20,
  },
  dayText: {
    fontSize: 25,
    fontWeight: 'bold',
  },
  divider: {
    marginVertical: 8,
    alignSelf: 'stretch',
  },
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
  image: {
    height: 200,
    width: '100%',
    marginVertical: 20,
    borderRadius: 10,
  },
  goalsContainer: {
    flex: 1,
  },
  sectionTitle: {
    fontSize: 20,
    marginBottom: 8,
  },
  taskItem: {
    marginVertical: 4,
    padding: 10,
    borderRadius: 6,
    backgroundColor: "#5e0acc",
  },
  taskText: {
    color: "#fff",
    fontSize: 16,
  },
});
