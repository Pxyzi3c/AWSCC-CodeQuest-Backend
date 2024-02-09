import json

class PasswordManager:
    def __init__(self, website: str, email: str, password: str):
        self.website = website
        self.email = email
        self.password = password

    def __loadData(self, path: str):
        with open(path, 'r') as file:
            return json.load(file)
    
    def __updateData(self, path: str, data: object):
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    def addData(self):
        try:
            data = self.__loadData('backend/day-15/data.json')

            new_data = {
                "email": self.email,
                "password": self.password
            }

            website_key = self.getWebsiteKey()
            if website_key not in data:
                data[website_key] = []
            data[website_key].append(new_data)

            self.__updateData('backend/day-15/data.json', data)
        except:
            print("An error occured!")
        else: 
            print("Password added successfully!")

    def getData(self):
        try: 
            data = self.__loadData('backend/day-15/data.json')
            
            for website, account in data.items():
                print(f"Website: {self.getWebsiteName(website)}")
                for details in account:
                    print(f"\tEmail: {details['email']}")
                    print(f"\tPassword: {details['password']}")
        except:
            print("An error occured while fetching the data!")

    def deleteData(self):
        try:
            data = self.__loadData('backend/day-15/data.json')
            
            data_to_delete = {
                'email': self.email,
                'password': self.password
            }

            website_key = self.getWebsiteKey()
            data[website_key].remove(data_to_delete)

            self.__updateData('backend/day-15/data.json', data)
        except KeyError:
            print("Website key not found on the record! Please check your inputs and try again")
        except ValueError:
            print("Password is not found on the record! Please check your inputs and try again")
        except:
            print("An error occured!")
        else:
            print("Password deleted successfully!")

    def updateData(self):
        print("Update data function")

    def getWebsiteName(self, code: str):
        try:
            data = self.__loadData('backend/day-15/websites.json')

            for website in data:
                if code == website['code']:
                    return website['name']
        except:
            print("Error fetching website names!")
    
    def getWebsiteKey(self):
        try:
            data = self.__loadData('backend/day-15/websites.json')

            for website in data:
                if self.website.lower() == website['name'].lower():
                    return website['code']

            return self.website.lower().replace(' ', '_')    
        except:
            print("Error fetching website keys")
    
def generateDivider():
    i = 50
    counter = 1
    while not counter > i:
        print('*', end='')
        counter += 1
    print()

def start():
    options = (
        (1, "Add a password"),
        (2, "View passwords"),
        (3, "Search"),
        (4, "Delete a password"),
        (5, "Update a password") 
    )
    
    while True:
        password_manager = PasswordManager("", "", "")

        print("OPTIONS")
        for process_number, process_description in options:
            print(f"  {process_number} - {process_description}")
        
        try:
            selected_option = options[(int(input("Select an option: "))) - 1][1].split()[0].upper()

            generateDivider();
            if selected_option == "ADD":
                website = input("Website name: ")
                email = input("Email: ")
                password = input("Password: ")
                PasswordManager(website, email, password).addData()
            elif selected_option == "VIEW":
                password_manager.getData()
            elif selected_option == "SEARCH":
                password_manager.getData()
            elif selected_option == "DELETE":
                website = input("Website name: ")
                email = input("Email: ")
                password = input("Password: ")
                PasswordManager(website, email, password).deleteData()
            elif selected_option == "UPDATE":
                password_manager.updateData()

            generateDivider()
            another_process = input("Do you want to perform another operation? [y/n] ").lower()

            if not another_process == 'y':
                break
        except KeyboardInterrupt:
            print("\n OPERATION CANCELLED")
            break

start()