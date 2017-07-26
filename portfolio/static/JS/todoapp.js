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
    }
};

var handlers = {
    addTodo: function(input) {
        todoList.addTodo(input.value);
        input.value = "";
        view.displayTodos();
    },
    changeTodo: function() {
        var changeTodoPositionInput = document.getElementById(
            "changeTodoPositionInput"
        );
        var changeTodoTextInput = document.getElementById("changeTodoTextInput");
        todoList.changeTodo(
            changeTodoPositionInput.valueAsNumber,
            changeTodoTextInput.value
        );
        changeTodoPositionInput.value = "";
        changeTodoTextInput.value = "";
        view.displayTodos();
    },
    deleteTodo: function(position) {
        todoList.deleteTodo(position);
        view.displayTodos();
    },
    toggleAll: function() {
        var lis = document.getElementById("todos").getElementsByTagName("li");
        var lisCount = lis.length;
        var checkedCount = 0;

        //count total with checked class and if same as total lis then remove checked class
        for (var i = 0; i < lisCount; i++) {
            if (lis[i].classList.contains("checked")) {
                checkedCount += 1;
            }
        };

        if (lisCount === checkedCount) {
            for (var i = 0; i < lisCount; i++) {
                lis[i].classList.remove("checked");
                todoList.todos[lis[i].id].completed = false;
            };
        } else {
            for (var i = 0; i < lisCount; i++) {
                lis[i].classList.add("checked");
                todoList.todos[lis[i].id].completed = true;
            };
        }
    },
    markCompleted: function(element) {
        var todo = todoList.todos[element.id];

        if (element.classList.contains("checked")) {
            todo.completed = !todo.completed;
            element.classList.remove("checked");
        } else {
            todo.completed = !todo.completed;
            element.classList.add("checked");
        }
    },
    deleteAll: function() {
        todoList.todos.length = 0;
        view.displayTodos();
    },
    addTodoClick: function() {
        var addTodoTextInput = document.getElementById("addTodoTextInput");
        handlers.addTodo(addTodoTextInput);
    }
};

var view = {
    displayTodos: function() {
        var todosUl = document.getElementById("todos");
        todosUl.innerHTML = "";

        todoList.todos.forEach(function(todo, position) {
            var todoLi = document.createElement("li");
            var todoTextWithCompletion = "";

            todoTextWithCompletion = todo.todoText;

            todoLi.id = position;
            todoLi.textContent = todoTextWithCompletion;

            if (todo.completed === false) {
                todoLi.className = "list-group-item";
            } else {
                todoLi.className = "list-group-item checked";
            }

            todoLi.appendChild(this.createDeleteButton());
            todosUl.appendChild(todoLi);
        }, this);
    },
    createDeleteButton: function() {
        var deleteButton = document.createElement("button");
        deleteButton.className = "deleteButton btn btn-xs pull-right";

        var icon = document.createElement("span");
        icon.className = "glyphicon glyphicon-trash";

        deleteButton.appendChild(icon);

        return deleteButton;
    },
    setUpEventListeners: function() {
        var todosUl = document.getElementById("todos");
        var addTodoTextInput = document.getElementById("addTodoTextInput");

        //if enter addTodo else if escape remove input
        addTodoTextInput.addEventListener(
            "keyup",
            function(event) {
                if (event.which === ENTER_KEY) {
                    handlers.addTodo(addTodoTextInput);
                }
                if (event.which === ESCAPE_KEY) {
                    addTodoTextInput.value = "";
                }
            },
            false
        );

        //get element that was clicked and run appropriate handler
        todosUl.addEventListener(
            "click",
            function(event) {
                var elementClicked = event.target;

                if (elementClicked.className === "glyphicon glyphicon-trash") {
                    handlers.deleteTodo(parseInt(elementClicked.closest("LI").id));
                }
                if (elementClicked.tagName === "LI") {
                    handlers.markCompleted(elementClicked);
                }
            },
            false
        );
    }
};

view.setUpEventListeners();