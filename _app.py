import streamlit as st

st.title('To-do App')

class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'

    # 객체가 리스트 안에 있을 때 리스트 안의 요소들을 출력하면 __repr__만 나온다.(__str__은 안나옴)
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'

        # repr은 eval()로 다시 객체로 바꿀 수 있는 문자열 형태로 작성하는 게 원칙이다.
        # return f'Todo(task="{self.__task}", done={self.__done})'
        # return f'Todo(task={self.__task!r}, done={self.__done})'

# __repr__ 심화 설명
# todo = Todo('숙제하기')
# print(id(todo))
# todo2 = eval(repr(todo))
# print(id(todo2))

def add_todo():
    print(f'함수가 호출 될 때 주머니에 담긴 값: {st.session_state.new_task}')
    todo = Todo(st.session_state.new_task)
    # print(todo)
    st.session_state.todos.append(todo)

# todos(todo 객체를 담을 리스트)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장된다.(session_state에 새로운 키 초기화)
st.text_input('새로운 할일 추가', key='new_task', on_change=add_todo)  # input 창에 내용을 작성(기존과 다른 내용)하고
                                                                         # 엔터하면 add_todo함수 호출

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        st.write(f'{i}번째 todo => {todo}')
else:
    st.info('할일을 추가해 보세요.')