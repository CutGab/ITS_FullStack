import { useState, useEffect, useRef } from "react";
import { StyleSheet, Text, View, Image, FlatList, Animated, Modal, Button } from "react-native";
import { Divider } from '@rneui/themed';
import { fadeInFromBelow } from './utils';
import TaskInput from './components/TaskInput';
import TaskItem from './components/TaskItem';
import { fetchTasks } from "./Services/service";

export default function App() {
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const translateY = useRef(new Animated.Value(50)).current;

  const [taskList, setTaskList] = useState([]);
  const [currentTime, setCurrentTime] = useState(new Date());
  const [modalVisible, setModalVisible] = useState(false); // ✅ modal state

  useEffect(() => {
    fadeInFromBelow(fadeAnim, translateY, 1000);
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const addTaskHandler = (taskText) => {
    const newTask = { id: Date.now().toString(), task: taskText };
    setTaskList((current) => [...current, newTask]);
    setModalVisible(false);
  };

  async function loadTasks() {
    const tasks = await fetchTasks();
    setTaskList(tasks)
  }

  useEffect(() => {
    loadTasks()
  }, [])

  const deleteTask = (id) => {
    setTaskList(current => current.filter(t => t.id !== id));
  };

  return (
    <Animated.View
      style={[
        styles.appContainer,
        { opacity: fadeAnim, transform: [{ translateY }] },
      ]}
    >
      <View style={styles.header}>
        <Text style={styles.dayText}>Task di Oggi</Text>
        <Divider color="black" width={1} style={styles.divider} />
        <Text style={styles.dayText}>{currentTime.toLocaleTimeString()}</Text>
      </View>

      {/* Button to open modal */}
      <Button title="Aggiungi Task" onPress={() => setModalVisible(true)} />

      {/* Modal */}
      <Modal
        visible={modalVisible}
        animationType="slide"
        transparent={true}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <TaskInput onAddTask={addTaskHandler} />
            <Button title="Chiudi" onPress={() => setModalVisible(false)} />
          </View>
        </View>
      </Modal>

      <Image
        style={styles.image}
        source={{ uri: 'https://media.tenor.com/W85ad914NFcAAAAj/limbus-limbus-company.gif' }}
      />

      <View style={styles.goalsContainer}>
        <Text style={styles.sectionTitle}>Lista task</Text>
        <Divider color="black" width={1} style={styles.divider} />

        <FlatList
          data={taskList}
          renderItem={({ item }) => <TaskItem taskItem={item} onDelete={deleteTask} />}
          keyExtractor={(item) => item.id.toString()}
        />
      </View>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    backgroundColor: "#ff9500ff",
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
  image: {
    height: 300,
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
  modalOverlay: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',
    padding: 16,
  },
  modalContent: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 16,
  },
});
