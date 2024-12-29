FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file:
        todos = list(file.readlines())
    return todos


def write_todos(todos, filepath=FILEPATH):
    """ Write the new to-dos in a text file. """
    with open(filepath, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello from functions what the ?? LOL")