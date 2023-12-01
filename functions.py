import matplotlib.pyplot as plt
import sys
import classes as cl
import main


def collection_portal(my_data):
    loop_break = False
    while not loop_break:
        choice = int(input('Collection portal:\n\t'
                           '1. List all connections\n\t'
                           '2. Print a collection\n\t'
                           '3. Create new empty collection\n\t'
                           '4. Plot two collections\n\t'
                           '5. Add two collections\n\t'
                           '6. Subtract two collections\n\t'
                           '7. Back to main menu\n'))
        try:
            match choice:
                case 1:
                    print(my_data)
                case 2:
                    print(my_data)
                    name = input("What is the name of the collections who's values you would like to print?\n")
                    referenced_object = my_data.collection_dictionary[name]
                    print(referenced_object)
                    print(referenced_object.print_values())
                case 3:
                    name = input('What would you like the name of the new collection to be?\n')
                    my_data.create_empty_collection(name)
                    print(my_data.collection_dictionary[name])
                case 4:
                    print(my_data)
                    plot_two_collections(my_data)
                case 5:
                    print(my_data)
                    add_two_collections(my_data)
                case 6:
                    print(my_data)
                    subtract_two_collections(my_data)
                case 7:
                    loop_break = True
                case _:
                    print("That is not a valid input. Try again.")
        except:
            print("An error occured, returning to collection menu...")


def import_portal(my_data):
    """
    TODO Add ability to import specific columns.
    :param my_data:
    :return:
    """
    input_file = input("Enter the path to the file.\n")
    read_from_file(my_data, input_file)


def plot_two_collections(my_data):
    cl1 = input('What is the name of the collection you would like on the x axis?\n')
    cl2 = input('What is the name of the collection you would like on the y axis?\n')
    fig, my_plot = plt.subplots()
    my_plot.plot(my_data.collection_dictionary[cl1].data, my_data.collection_dictionary[cl2].data)
    plt.show()


def add_two_collections(my_data):
    print('What are the names of the two collections you would like to add.\n'
          'Hit enter after inputting the first collection name.'
          'The sum \nwill be created as a new collection.\n')
    collection1 = input()
    collection2 = input()
    new_collection = my_data.collection_dictionary[collection1] + my_data.collection_dictionary[collection2]
    new_collection_name = input('What would you like the new collection to be named.')
    new_collection.name = new_collection_name
    my_data.add_collection(new_collection)
    print(new_collection)


def subtract_two_collections(my_data):
    print('What are the names of the two collections you would like to subtract.'
          'Hit enter after inputting the first collection name.'
          'The difference will be created as a new collection.\n')
    collection1 = input()
    collection2 = input()
    new_collection = my_data[collection1] - my_data[collection2]
    new_collection_name = input('What would you like the new collection to be named.')
    new_collection.name = new_collection_name
    my_data.add_collection(new_collection)
    print(new_collection)


def read_from_file(my_data, f='sample_data.csv', fxn=None):
    if fxn != None:
        if len(sys.argv) > 1:
            with open(sys.argv[1], 'rt', newline='', encoding='utf-8-sig') as data_file:
                fxn()
        else:
            with open(f, 'rt', newline='', encoding='utf-8-sig') as data_file:
                fxn()
    else:
        if len(sys.argv) > 1:
            with open(sys.argv[1], 'rt', newline='', encoding='utf-8-sig') as data_file:
                my_data.auto_import(data_file)
        else:
            with open(f, 'rt', newline='', encoding='utf-8-sig') as data_file:
                my_data.auto_import(data_file)
