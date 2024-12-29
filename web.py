import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my to-do app")
st.write("This app is to increase your productivity")


for index, x in enumerate(todos):
    if x.strip("\n") != "":
        checkbox = st.checkbox(x, key=f"{x}")
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[x]
            st.rerun()

st.text_input(label="_", placeholder="Add a new to-do...",
              key="new_todo", on_change=add_todo)
