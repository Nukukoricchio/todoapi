<template>
  <div>
    <form @submit.prevent="addNewTodo" class="form-inline">
      <div class="form-group">
        <input type="text" v-model="title" name="title" class="form-control" placeholder="Add to do"/> 
        <button type="submit" class="btn btn-primary">Add</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "AddTodo",
  props: ["todos"],
  data() {
    return {
      title: "",
    };
  },
  methods: { 
    addNewTodo() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/',
        data: {
          title: this.title,
          completed: false
        }
      }).then(response => {
        let newTodo = {
          id: response.data.id,
          title: this.title,
          completed: false,
          created: response.data.created
        };
        this.todos = this.todos.unshift(newTodo);
        this.title = "";
      }).catch(error => console.log(error))
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
