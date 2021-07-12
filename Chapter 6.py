with open('todos.txt', 'w') as todos:
    print('One', file=todos)
    print('Two', file=todos)
    print('Three', file=todos)

# with open('todos.txt') as task:
#     for str in task:
#         print(str)