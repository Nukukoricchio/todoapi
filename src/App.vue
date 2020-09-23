<template>
  <div id="app"> 
    <div class="row container mx-auto">
      
      <div class="col-md-12">
        <AddTodo v-bind:todos="todos" />
        <br>
        <br>
        <div class="card-hover-shadow-2x mb-3 card">
          <div class="card-header-tab card-header">
            <div
              class="card-header-title font-size-lg text-capitalize font-weight-normal"
            >
              <i class="fa fa-tasks"></i>&nbsp;Task Lists
            </div>
          </div>
          <div class="scroll-area-sm">
            <perfect-scrollbar class="ps-show-limits">
              <div style="position: static;" class="ps ps--active-y">
                <div class="ps-content">
                 <Todos v-bind:todos="todos" />
                </div>
              </div>
            </perfect-scrollbar>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Todos from "./components/Todos";
import AddTodo from "./components/AddTodo";

export default {
  name: "App",
  components: {
    Todos,
    AddTodo,
  },
  data() {
    return {
      todos: [],
      errors: []
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/')
    .then(response => {
      this.todos = response.data;
    })
    .catch(e => {
      this.errors.push(e);
    })
  },
};
</script>

<style></style>
