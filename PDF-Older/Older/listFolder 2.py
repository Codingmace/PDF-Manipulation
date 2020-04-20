import os

def main(): 
    path = "C:/Users/maste/Desktop/Python PDF Project"
    arr = os.listdir(path)
    fins = []    
    for x in arr:
        if os.path.isdir(x):
            print(x)
            fins += [x]
    print(fins)
    fin = []
    for r in fins:
        if "Text" in r:
            fin.append(rec(r))
    print("q")
    print(fin)
    # Testing out an array
    ar = [1, 2, 3, 4]
    ar.append(4)
    ar += [2]
    print(ar)
    print(len(fin[0]))
    pfin = []
    i = False
#    print(po.pop(0))
    num = 0
    while num < len(fin):
        po = fin[num]
        tem = po[0]
        temp = -1
#        tem = po.remove(0)
        po.pop(0)
        pfin.append(tem)
        while len(po) > 0:
            if i:
                tem = po[0]
                po.pop()
                pfin.append(tem)
            try: 
                temp = po.index(tem)
            except:
                temp = -1
            if temp >= 0:
                print("p" )
                print(len(po))
                print(" ")
                po.remove(temp)
                print(len(po))
                i = False
            else:
                i = True
        num+= 1
    print(len(pfin))
# Go through and find the files
# Compare dates of files if duplicates
# Merge if needed
# Then create new file


def rec(path): # Get the files in folders
    q = os.listdir(path)
    return q

main()