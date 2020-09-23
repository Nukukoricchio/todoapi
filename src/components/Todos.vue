<template>
  <div>
    <ul> 
      <li v-for="todo in todos" v-bind:key="todo.id">
        <Todo
          v-bind:todo="todo"
          v-on:delete-todo="deleteTodo"
        ></Todo>
      </li>
    </ul>
  </div>
</template>

<script>
import Todo from "./Todo";
import axios from "axios";

export default {
  name: "Todos",
  components: {
    Todo,
  },
  props: ["todos"],
  methods: {
    deleteTodo(todoId) {
      let url = 'http://127.0.0.1:8000/api/' + todoId + '/';
      axios.delete(url)
      .then(() => {
        this.todos = this.todos.filter((todo) => todo.id !== todoId);
      })
      .catch(error => {
        console.log(error);
      })
    }
  }
};
</script>

<style lang="scss" scoped></style>
