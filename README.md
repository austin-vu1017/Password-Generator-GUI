# Password-Generator-GUI
A password generator app that stores website name, username/email, and password in a .json file in the local directory. Features include generating password and saving to a file.

## Modules
- tkinter: used for GUI setup
- tkiner (messagebox): used to display popup windows for error and confirmation
- random: used for choice(), randint(), and shuffle() to generate a secured password
- pyperclip (copy): used to copy the generated password to the user's clipboard
- json: used to stored user's data. Previously was a text file, but for better future data management. .json is imported.

## Methods
- generate_pw(): generate a password using lists that contains ASCII characters. Separated into symbols, numbers, and letters. Using list comprehenion, the password is created first from letters, then added onto with symbols and numbers. Afterwards, shuffled and copied onto user's clipboard
- save(): the info in the fields are stored into a dictionary. If Else will check if any fields are empty. Else, asks user if they confirm the info inputted which will then be added into a .json file. Exception handling is available in the case the data.json does not exist. Try to read file, if not found create and add data into newly created file. Else, if data.json exists, add onto the existing file.
- find_password(): user can search their info in the website they've added. Type in the website name in the website field and click on search to find the website's info. Errors will pop up if file doesn't exists and if website doesn't exist. If website exists, a message box will appear with the email/username and password of the corresponding website.
