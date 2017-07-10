/**
 * Created by GarethMoger.com on 10/07/2017.
 */

var ENTER_KEY = 13;
var ESCAPE_KEY = 27;

var todoList = {
  todos: [],
  addTodo: function(todoText) {
    this.todos.push({
      todoText: todoText,
      completed: false
    });
  },
  changeTodo: function(position, todoText) {
    this.todos[position].todoText = todoText;
  },
  deleteTodo: function(position) {
    this.todos.splice(position, 1);
  },
  toggleCompleted: function(position) {
    var todo = this.todos[position];
    todo.completed = !todo.completed;
  },
  toggleAll: function() {
    var totalTodos = this.todos.length;
    var completedTodos = 0;

    // Get number of completed todos.
    this.todos.forEach(function(todo){
      if (todo.completed === true) {
        completedTodos++;
      }
    });

    // If everything’s true, make everything false, else make everything true
    this.todos.forEach(function(todo){
      if (completedTodos === totalTodos){
        todo.completed = false;
      } else {
        todo.completed = true;
      }
    });
  }
};

var handlers = {
    addTodo: function(input) {
        todoList.addTodo(input.value);
        input.value = '';
        view.displayTodos();
    },
    changeTodo: function() {
        var changeTodoPositionInput = document.getElementById('changeTodoPositionInput');
        var changeTodoTextInput = document.getElementById('changeTodoTextInput');
        todoList.changeTodo(changeTodoPositionInput.valueAsNumber, changeTodoTextInput.value);
        changeTodoPositionInput.value = '';
        changeTodoTextInput.value = '';
        view.displayTodos();
    },
        deleteTodo: function(position) {
        todoList.deleteTodo(position);
        view.displayTodos();
    },
    toggleCompleted: function() {
        var toggleCompletedPositionInput = document.getElementById('toggleCompletedPositionInput');
        todoList.toggleCompleted(toggleCompletedPositionInput.valueAsNumber);
        toggleCompletedPositionInput.value = '';
        view.displayTodos();
    },
    toggleAll: function() {
        todoList.toggleAll();
        view.displayTodos();
     },
    markCompleted: function(element) {
        if(element.classList.contains('checked')){
            element.classList.remove('checked');
        } else {
            element.classList.add('checked');
        }
    }
};

var view = {
    displayTodos: function() {
        var todosUl = document.getElementById('todos');
        todosUl.innerHTML = '';


        todoList.todos.forEach(function(todo, position) {
            var todoLi = document.createElement('li');
            var todoTextWithCompletion = '';

            if (todo.completed === true) {
                todoTextWithCompletion = '(x) ' + todo.todoText;
            } else {
                todoTextWithCompletion = '( ) ' + todo.todoText;
            }

            todoLi.id = position;
            todoLi.textContent = todoTextWithCompletion;
            todoLi.className = 'list-group-item';
            todoLi.appendChild(this.createDeleteButton());
            todosUl.appendChild(todoLi);
        }, this);
    },
    createDeleteButton: function(){
        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'X';
        deleteButton.className = 'deleteButton btn btn-xs pull-right';
        //add <span class="glyphicon glyphicon-trash"></span>
        //add <span><input type="checkbox" value=""></span>

        return deleteButton;
    },
    setUpEventListeners: function(){
        var todosUl = document.getElementById('todos');
        var addTodoTextInput = document.getElementById('addTodoTextInput');

        //if enter addTodo else if escape remove input
        addTodoTextInput.addEventListener('keyup', function(event){
           if(event.which === ENTER_KEY) {
               handlers.addTodo(addTodoTextInput);
           }
            if(event.which === ESCAPE_KEY) {
               addTodoTextInput.value = '';
           }
        });

        //get element that was clicked and run appropriate handler
        todosUl.addEventListener('click', function(event){
            var elementClicked = event.target;

            if (elementClicked.className === 'deleteButton btn btn-xs pull-right'){
                handlers.deleteTodo(parseInt(elementClicked.parentNode.id));
            }
            if (elementClicked.tagName === 'LI'){
                handlers.markCompleted(elementClicked);
            }
        });
    }
};

view.setUpEventListeners();