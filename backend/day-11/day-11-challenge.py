filePath = 'backend/day-11/text.txt'

def validateInput(user_input, old_val):
    return user_input or old_val

def successfulProcess(data):
    print("\nSuccessfully modified and sorted data! Here's the updated file:")
    for line in data:
        print(line)

def readFile(data):
    with open(filePath, 'r') as file:
        content = file.readlines()
        for line in content:
            data.append(validateInput(input(f"Enter new value for {line.strip()} [Enter to skip]: "), line.strip()))

def writeFile(data):
    with open(filePath, 'w') as file:
        for line in data:
            file.writelines(f"{line}\n")
        successfulProcess(data)

def start():
    try:
        newContent = []
        readFile(newContent)
        writeFile(sorted(newContent))
    except FileNotFoundError:
        print("File does not exists!")
    except IOError:
        print("Error occurred while reading or writing the file.")
    except Exception as e:
        print(f"Error occured: {e}")
    except KeyboardInterrupt:
        print("\nProcess cancelled!")

start()