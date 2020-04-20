import os

# Prints the files in a hierarchical display

path = "C:/Users/maste/Desktop/Python PDF Project"
arr = os.listdir("C:/Users/maste/Desktop/Python PDF Project/")
list_of_list = []
for x in arr:
    if os.path.isdir(x):
        print(x)
i=0
for (path, dirs, files) in os.walk(path):
    # if os.path.isdir(path):
    print(path)
    print(dirs)
    arr = files
    list_of_list += arr
    print(files)
    print("----")
    i += 1
    if i >= 4:
        break
# print("x")  
# print(list_of_list)
# os.path.isdir(arr[0])
# print(arr)
# print(glob.glob("C:\\Users\\maste\\Desktop\\Python PDF Project\\*"))
