import sys
import json
import clipboard

SAVED_DATA = "clipboard.json" #path of where the key value pairs will be saved

def save_data(path, data): 
    with open(path, 'w') as f: #open the file, 'w' puts it in a state to be written to
        json.dump(data,f) #write the data to the file

def load_data(path):
    try: # use try to prevent the program from crashing
        with open(path, 'r') as f: #open the file, 'r' puts it in a state to be read
            data = json.load(f) #load the data from the file
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA) #load the JSON file
    
    if command == "save":
        print("saving")
        key = input("Enter a key : ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('data saved')

    elif command == "load":
        print('loading')
        key = input('enter your key: ')
        if key in data:
            clipboard.copy(data[key])
            print('data copied to clipboard')
        else:
            print('key does not exist')
            
    elif command == "list":
        print('data in your clipboard')
        print(data)
    
    elif command == 'delete':
        print('deleting')
        key = input('enter they key you want to delete ')
        if key in data:
            data.pop(key)
            save_data(SAVED_DATA, data)
            print('data removed')
        else:
            print("key does not exist")
        print(data)
    else:
        print('enter a valid command')
   