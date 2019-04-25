const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const reverseButton = document.querySelector('#reverse_btn');
    const fetchButton = document.querySelector('#fetch_btn');
    const addButton = document.querySelector('#add_todo_btn');
    const inputArea = document.querySelector('#add_todo_input');

// TODO: input, Add 버튼에 createTodo와 이벤트 리스너를 잘 버무린다.
    const createTodo = (inputText, completed = false) => {
        // Card
        const todoCard = document.createElement('div');

        todoCard.classList.add('ui', 'segment', 'todo-item');
        if (completed) todoCard.classList.add('secondary');

        // Card > Wrapper
        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');
        // Card > Wrapper > input ( checkbox)
        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');
        input.checked = completed;

        input.addEventListener('click', e => {
            if (input.checked) {
                label.classList.add('completed-label');
                todoCard.classList.add('secondary');
            } else {
                label.classList.remove('completed-label');
                todoCard.classList.remove('secondary');
            }
        });
        // Card > Wrapper > input (text)
        const label = document.createElement('label');
        label.innerHTML = inputText;
        if (completed) label.classList.add('completed-label');

        // Card > Icon
        const deleteIcon = document.createElement('i'); // <i></i>
        deleteIcon.classList.add('close', 'icon', 'delete-icon'); // <i class="close icon"></i>

        deleteIcon.addEventListener('click', e => {
            todoBox.removeChild(todoCard);
        });

        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);

        return todoCard
    };
    inputArea.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            todoBox.appendChild(createTodo(inputArea.value, true));
        }
    });
    addButton.addEventListener('click', e=> {
        todoBox.appendChild(createTodo(inputArea.value));
    });

    reverseButton.addEventListener('click', e => {
        reverseTodos()
    });
// TODO: 버튼 만들고, 데이터 받아오게 이벤트 리스너 클릭 얍!
    fetchButton.addEventListener('click', e => {
            const fetchData = URL => {
                fetch(URL)
                    .then(res => res.json())
                    .then(todos => {
                        for (const todo of todos) {
                            todoBox.appendChild(createTodo(todo.title, todo.completed));
                        }
                    })
            };
        fetchData('https://koreanjson.com/todos');
    });




    const reverseTodos = () => {
        const allTodos = Array.from(document.querySelectorAll('.todo-item')); // 원본이 하나이므로 파이썬의 deepcopy처럼 copy 해준다. Array.from() 함수 안에 넣어줌 그래야 while문 반복하고 for문 들어가서 새로운 todo를 더해줌

        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild);
        }
        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo)
        }
    };
// todoBox.appendChild(createTodo('hihi', true));
// todoBox.appendChild(createTodo('hihi', true));
};

init();
