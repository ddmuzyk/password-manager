import random, json, string

def check_existing_password(func):
    def wrapper(self, website, password):
        try: 
            with open("pass.json", "r") as file:
                credentials = json.load(file)
        except json.JSONDecodeError:
            with open("pass.json", "w") as file:
                file.write(json.dumps({}))
                print("No websites found")
                return False
        if website in credentials:
            print("Website already exists")
            return False
        func(self, website, password)
        print(f'Password for {website} successfully set')
    return wrapper

def check_existing_website(func):
    def wrapper(self, website, old_password, new_password):
        try: 
            with open("pass.json", "r") as file:
                credentials = json.load(file)
        except json.JSONDecodeError:
            with open("pass.json", "w") as file:
                file.write(json.dumps({}))
                print("No websites found")
                return False
        if website not in credentials:
            print("Website does not exist")
            return False
        func(self, website, old_password, new_password)
    return wrapper

class Manager:

    def __init__(self, name=""):
        self.name = name
        self.prohibited = {
            '\\': True,
            '"': True,
            "'": True,
            ' ': True
        }

    def create_password(self, length):
        password = ""
        if length > 0:
            for _ in range(length):
                characters = string.ascii_letters + string.digits + '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
                password += characters[random.randint(0, len(characters) - 1)]
        else:
            return ""
        return password
    
    @check_existing_password
    def set_password(self, website, password):
        with open("pass.json", "r") as file:
            credentials = json.load(file)
        with open("pass.json", "w") as file:
            credentials[website] = password
            file.write(json.dumps(credentials))
    
    @check_existing_website
    def change_password(self, website, old_password, new_password=None):
        with open("pass.json", "r") as file:
            credentials = json.load(file)

        if credentials[website] == old_password:           
            credentials[website] = new_password
            with open("pass.json", "w") as file:
                file.write(json.dumps(credentials))
                print(f'Password for {website} successfully changed')
        else:
            print("Old password is incorrect")
            return False
    
    def get_password(self, website):
        try:
            with open("pass.json", "r") as file:
                credentials = json.load(file)
        except json.JSONDecodeError:
            with open("pass.json", "w") as file:
                file.write(json.dumps({}))
            return False
                
        return credentials[website] if website in credentials else False
    
    def contains_prohibited(self, password):
        for char in password:
            if char in self.prohibited:
                return True
        return False
    
    def list_websites(self):
        try: 
            with open("pass.json", "r") as file:
                websites = json.load(file).keys()
        except json.JSONDecodeError:
            websites = {}
            with open("pass.json", "w") as file:
                file.write(json.dumps(websites))
            print("No websites found")
            return []
        if len(websites) == 0:
            return []
        else:
            return list(websites)
            
    def clear_passwords(self):
        with open("pass.json", "w") as file:
            file.write(json.dumps({}))

    def get_credentials(self):
            try:
                with open("pass.json", "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                with open("pass.json", "w") as file:
                    file.write(json.dumps({}))
                return {}
            
    def check_if_website_exists(self, website):
        try:
            with open("pass.json", "r") as file:
                credentials = json.load(file)
        except json.JSONDecodeError:
            with open("pass.json", "w") as file:
                file.write(json.dumps({}))
            return False
        return website in credentials
    