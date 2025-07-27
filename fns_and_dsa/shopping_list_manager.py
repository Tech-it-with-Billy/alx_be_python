shopping_list = []

def add_item():
    item = input('Add  item name: ')
    shopping_list.append(item)

def remove_items():
    item = input('Remove item: ')
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print('Item not in the list!')

def display_current_list():
    for idx, item in enumerate(shopping_list, start=1):
        print(f"{idx}. {item}")