from ParentFolder.Dir1 import file1
from ParentFolder.Dir2 import file2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    file1.print1()
    file2.print2()
    file2.loadFromDir1()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
