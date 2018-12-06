<template>
  <div>
    {{ msg }}
    <form>
      <button @click="addTodo()">ADD TASK</button>
      <button @click="removeTodo()">DELETE FINISHED TASKS</button>
      <p>input: <input type="text" v-model="newTodo"></p>
      <p>task: {{ newTodo }}</p>
    </form>
    <div class="task-list">
      <label class="task-list__item"
            v-for="todo in todos"
            :key="todo.id"
            >
        <input type="checkbox"><button>EDIT</button>{{ todo.text }}
      </label>
    </div>
    {{ todos }}
  </div>
</template>

<script>
import axios from 'axios'

const URL_BASE = 'http://127.0.0.1:5000'
const headers = {
//   'Content-Type': 'application/json;charset=UTF-8',
  'Access-Control-Allow-Origin': '*'
}

export default {
  name: 'todo',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      newTodo: null,
      todos: [
        { id: 1, text: 'vue-router', done: false },
        { id: 2, text: 'vuee', done: false },
        { id: 3, text: 'vue-loader', done: false },
        { id: 4, text: 'awesome-vue', done: true }
      ]
    }
  },
  created () {
    this.getTodo()
  },
  methods: {
    getTodo () {
      console.log(URL_BASE + '/api/todo')
    //   axios.get(
    //     URL_BASE + '/api/todo',
    //     {
    //       headers: headers
    //     }
    //   ).then((res) => {
    //     console.log(res)
    //   }).catch((error) => {
    //     console.log(error)
    //   })
    },
    addTodo (event) {
      let todotext = this.newTodo && this.newTodo.trim()
      console.log(todotext)
      if (!todotext) {
        return
      }
      this.todos.push({
        text: todotext,
        done: false
      })
      this.newTodo = null
    },
    removeTodo (event) {
      for (let i = this.todos.length - 1; i >= 0; i--) {
        if (this.todos[i].done) this.todos.splice(i, 1)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@mixin flex-vender() {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  display: -ms-flex;
  display: -o-flex;
}
.task-list {
  @include flex-vender;
  flex-direction: column;
  align-items: center;
  &__item {
    width: 270px;
    text-align: left;
    $element: #{&};
    &--checked {
      @extend #{$element};
      color: #85a6c6;
    }
  }
}
</style>
