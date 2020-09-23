<template>
  <div class="widget-content p-0">
    <div class="widget-content-wrapper">
      <div
        class="widget-content-left"
        v-bind:class="{ completed: todo.completed }"
        v-if="!isEditing"
      >
        <div class="widget-heading">
          <p v-on:click="markComplete" style="color: red;">
            <i class="fa fa-check" v-show="todo.completed"></i
            ><span> &nbsp;</span> <span> &nbsp;</span>{{ todo.title }}
          </p>
          <p><b>Created: </b>{{ todo.created }}</p>
        </div>
      </div>
      <form v-else class="flex-grow-1" @submit.prevent="finishEditing()">
        <input
          type="text"
          class="form-control"
          v-model="newTitle"
          @blur="finishEditing()"
          ref="newTodo"
        />
      </form>
      <div class="widget-content-right">
        <button
          class="border-0 btn-transition btn btn-outline-success"
          v-on:click="startEditing()"
        >
          <i class="fa fa-edit"></i>
        </button>
        <button
          @click="deleteTodo()"
          class="border-0 btn-transition btn btn-outline-danger"
        >
          <i class="fa fa-trash"></i>
        </button>
      </div>
    </div>
    <hr />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Todo",
  props: ["todo"],
  data() {
    return {
      isEditing: false,
      newTitle: "",
    };
  },
  methods: {
    markComplete: function() {
      axios({
        method: "put",
        url: 'http://127.0.0.1:8000/api/' + this.todo.id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          completed: true,
        }
      }).then(() => {
        this.todo.completed = true;
      })
    },
    deleteTodo() {
      this.$emit('delete-todo', this.todo.id);
    },
    startEditing() {
      if (this.isEditing) {
        this.finishEditing();
      } else {
        this.newTitle = this.todo.title;
        this.isEditing = true;
        this.$nextTick(() => this.$refs.newTodo.focus());
      }
    },
    finishEditing() {
      axios({
        method: "put",
        url: 'http://127.0.0.1:8000/api/' + this.todo.id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          title: this.newTitle,
        }
      }).then(() => {
        this.isEditing = false;
        this.todo.title = this.newTitle;
      })
    },
  },
};
</script>

<style scoped>
.completed {
  text-decoration: line-through;
}
</style>
