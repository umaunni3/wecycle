import numpy as np
try:
    entries = np.load('data.npy')
except:
    # most likely errored because data.npy hasn't been created yet
    entries = -1
#id num, name, img url, address, weekday hrs, saturday hrs, sunday hrs, tag1, tag2, tag3, info, website
table_size = len(entries) # number of rows in the table

if  type(entries) == int:
    mappings = {} #nothing to put into mappings yet
else:
    mappings = {int(e[0]):e[1] for e in entries}

def readEntry(id_num):
    """ Return the specified row in entries """
    global entries
    try:
        return entries[id_num][1:]
    except:
        #probably error is that entries == -1; that is, no data table exists yet
        return np.array([None for _ in range(len(entries[0] - 1))])

def newEntry(arr):
    global entries
    global table_size
    assert len(arr) == len(entries[0]) - 1 ; "array size does not match size of table"
    new_entries = np.insert(arr, 0, table_size) #add id num to beginning of array before appending
    mappings[table_size] = arr[0]
    if type(entries) == int:
        #no data.npy file exists yet; must create data table for the first time
        entries = new_entries
    else:
        #data.npy already exists and so does the table; just adding to it at this point
        entries = np.vstack((entries, new_entries))
    table_size = len(entries)
    np.save('data.npy', entries)

def removeEntry(id_num):
    global entries
    try:
        entries = np.vstack((entries[:int(id_num)-1], entries[int(id_num):]))
    except:
        # not sufficient entries or whatever
        raise ValueError

def getEntriesTable():
    global entries
    return entries
