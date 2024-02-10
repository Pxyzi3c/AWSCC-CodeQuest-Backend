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
            if website_key in data and new_data in data[website_key]:
                print(f"Password already exists for website: {self.getWebsiteName(website_key)}")
                return
            else:
                data.setdefault(website_key, []).append(new_data)

            self.__updateData('backend/day-15/data.json', data)
            print("Password added successfully!")
        except Exception as e:
            print(f"An error occured: {e}")

    def getData(self, filter_key = None):
        try: 
            data = self.__loadData('backend/day-15/data.json')
            filtered_items = {}
            if filter_key:
                if filter_key in data:
                    filtered_items = {filter_key: data[filter_key]}
                else:
                    for website_key, accounts in data.items():
                        filtered_accounts= [
                            account for account in accounts if filter_key in account.values()
                        ]
                        if filtered_accounts:
                            filtered_items[website_key] = filtered_accounts
                if filtered_items:
                    self.displayData(filtered_items)
                else:
                    print("Keyword is not found on our record!")
            else:
                self.displayData(data)
        except Exception as e:
            print(f"An error occured: {e}")
    
    def displayData(self, data: object):
        for website, account in data.items():
            print(f"Website: {self.getWebsiteName(website)}")
            for details in account:
                print(f"\tEmail: {details['email']}")
                print(f"\tPassword: {details['password']}")

    def deleteData(self):
        try:
            data = self.__loadData('backend/day-15/data.json')
            website_key = self.getWebsiteKey()
            for account in data.get(website_key, []):
                if account.get('email') == self.email and account.get('password') == self.password:
                    data[website_key].remove(account)
                    self.__updateData('backend/day-15/data.json', data)
                    print("Password deleted successfully!")
                    return
            print("Email and password combination not found in the record! Please check your inputs and try again")
        except FileNotFoundError:
            print("File not found! Please check the file path")
        except Exception as e:
            print(f"An error occurred: {e}")

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

def getUserInput():
    website = input("Website name: ")
    email = input("Email: ")
    password = input("Password: ")
    return PasswordManager(website, email, password)

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
                getUserInput().addData()
            elif selected_option == "VIEW":
                password_manager.getData()
            elif selected_option == "SEARCH":
                keyword = input("Enter a keyword [website/email/password]: ")
                password_manager.getData(keyword)
            elif selected_option == "DELETE":
                getUserInput().deleteData()
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