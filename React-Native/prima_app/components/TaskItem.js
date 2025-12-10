import { Text, Pressable, StyleSheet } from "react-native";

const TaskItem = ({ taskItem, onDelete }) => {
  return (
    <Pressable
      onPress={() => onDelete && onDelete(taskItem.id)}
      android_ripple={{ color: "#26ff00ff" }}
      style={({ pressed }) => [
        styles.taskItem,
        pressed && styles.pressedItem, // opacity feedback while pressed
      ]}
    >
      <Text style={styles.taskText}>{taskItem.task}</Text>
    </Pressable>
  );
};
  
const styles = StyleSheet.create({
  taskItem: {
    marginVertical: 4,
    padding: 10,
    borderRadius: 6,
    backgroundColor: "#bf6300ff",
  },
  taskText: {
    color: "#fff",
    fontSize: 16,
  },
  pressedItem: {
    opacity: 0.5, // visual feedback on press
  },
});

export default TaskItem;
