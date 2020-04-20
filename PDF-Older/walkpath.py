import os

def my_handle(sentence):
    return sentence.strip()
    
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def path(mypath):
    f = []
    for(dirName, subdirlist, fileList) in os.walk(mypath):
        for fname in fileList:
            if "pdf" in fname:
                f.append(fname)
#                 f.append(dirName + fname)
#                 print(fname)
    return f

# path(".")
ar = path("C:\\Users\\maste\\Dropbox\\XXX\\iPhone Text Backup 2\\")
# print("THE" +str(ar))
# print(ar[0])
# result = remove_duplicates(ar)
# print(result)
print(ar)

# # Remove duplicates from this list.
# result = remove_duplicates(ar)
# # print(result[0])
# print(result)


# # Convert to a set and back into a list.
# set = set(ar)
# results = list(set)
# print(results)