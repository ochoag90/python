# make list to hold onto our items
shopping_list = []

def show_help():
# print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'Help' for a Help Menu.
Enter 'SHOW' to see your current list
""")
def show_list():
    # print out the list
    print("Here's your list:")
    
    for item in shopping_list:
        print(item)

while True:
    # ask for new items
    new_item = input("> ")
    
    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    #else new_item
    # add new items to our list
    shopping_list.append(new_item)

show_list()
