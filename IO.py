'''
Created on 9 May 2013

@author: Floris
'''
def readData(sFile):
    matrix = []
    try:
        print "Read Data from " + str(sFile)
        f = open(sFile, "r")
        data = f.readlines()
        for line in data:
            #strip line from \n and \t
            row = line.strip().split("\t")
            #add row to data matrix
            matrix.append(row)
        print "Read Complete"
    except IOError:
        print 'Error: reading ' + str(sFile)
    finally:
        f.close()
    return matrix

def readData_by_line(file_object):
    """Lazy reader to read a file line by line"""
    while True:
        line = file_object.readline()
        if not line:
            break
        yield line

def readLastLine(sFile):
    with open(sFile, 'rb') as fh:
        fh.seek(-500, 2)
        return fh.readlines()[-1].decode()
    return ''

def writeData(sFile, arr, reverse=False, overWrite=False):
    try:
        print "Write Start in " + str(sFile)
        openMethod = "a"
        if (overWrite):
            openMethod = "w"
        f = open(sFile, openMethod)
        
        if(reverse):
            arr.reverse()
        
        for i in range(0, len(arr)):
            row = ""
            width = len(arr[i])
            for j in range (0, width):
                # replace characters that are important for our reader/writer to work
                s = str(arr[i][j])
                s = s.replace("\n", " ")
                s = s.replace("\t", " ")
                s = s.replace("\r", " ")
                # Add tab character for data separation
                row += s + '\t'
            # Replace last \t with a newline character
            row = row[:-1] + '\n'      
            f.write(row)
        print "Write Complete"
    except IOError:
        print 'Error: writing tweets'
    finally:
        f.close()
        
def dumpData(sFile, data):
    try:
        print "Write Start in " + str(sFile)
        f = open(sFile, "a")
        f.write(str(data))
        print "Write Complete"
    except IOError:
        print 'Error: failed to dump data'
    finally:
        f.close()