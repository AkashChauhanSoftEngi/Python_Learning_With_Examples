# read content line by line
# no need to f.close(), within in the with block as it takes place automaticlly
with open("/cxldata/python_sample_file") as f:
    s = ""
    for line in f:
        print(line)
        s = s + line
    print(s)
    
    
# Read the whole data into one String
with open("/cxldata/python_sample_file") as f:
    content = f.read()
    print(content)

    
# Read data from a file and sum length of all the words in a file
def file_read_func(path):
    lenSum = 0
    try:
        f = open(path)
        for line in f:
            list1 = line.split()
            
            for i in range(len(list1)):
                lenSum = lenSum + len(list1[i])
        
        f.close()
        
    except:
        return -1
    
    return lenSum

print(file_read_func("/cxldata/python_sample_file"))
