# AirBnB Console :house:
### Description :pen:
 The AirBnB Console is a command-line interpreter created for the purpose of handling objects similar to those found on Airbnb. It offers an easy-to-use interface for performing actions like creating, viewing, modifying, and removing instances of different classes like BaseModel, User, State, City, Amenity, Place, and Review. The Console involves the development of a console-driven application meant for the management of objects like the ones found on Airbnb. The Console includes a range of capabilities, including instance creation, information presentation, attribute modification, and instance removal. All the data is serialized and deserialized to and from JSON files to ensure effective data management.

#

### Features :pushpin:
- Create Instances - Creates new object/instance of the BaseModel class and save them into a JSON file.
- Display Information - The console lets you see in-depth information about specific objects/instances using their class name and ID.
- Delete Instances - You can remove object/instances by providing their class name and ID, and the console will automatically save the changes to the JSON file.
- List Instances - The console provides the option to list all object/instances or filter them by class name or ID.
- Update Attributes - You can modify object/instance attributes by providing their class name, ID, the attribute name, and the new value and the console saves the changes to JSON.

#

### Installation! :file_folder:
**Clone the repository; example below:**
```
root@user$ git clone https://github.com/ericpo1sh/holbertonschool-AirBnB_clone.git
```
**Then navigate to the projects root directory and run console.py; example below:**
```
holbertonschool-AirBnB_clone$ ./console.py
```
**The application should be running and the following promp should display:**
```
(hbnb)
```
#

#### Command Usage, Syntax, Descriptions :blue_book:

| Syntax | Description |
| -------| ----------- |
| `create <class_name>` | Creates new object/instance of the BaseModel class and save them into a JSON file. |
| `show <class_name> <id>` | See information about specific objects/instances using their class name and ID. |
| `destroy <class_name> <id>` | Destroy object/instances with class name and ID. |
| `all` ***or*** `all <class_name>` | Prints string representation of all instances or all instances of a specific class. |
| `update <class_name> <id> <atr_name> <atr_value>` | Update a specific instance and add a attribute name and value. |
| `clear` | Clear the screen. |
| `quit` | Exit the program. |
#

### List of availiable Classes :round_pushpin:
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

#

### Examples! :bulb:
**In this example, we create a new instance of BaseModel, a new ID is returned.**

```
(hbnb) create BaseModel
ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
```
**Now lets use the show command on this newly created instance.**
```
(hbnb) show BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
[BaseModel] (ab763e7e-4bc8-4380-bb07-0a07a8f1a56d) {'id': 'ab763e7e-4bc8-4380-bb07-0a07a8f1a56d',
'created_at': datetime.datetime(2023, 10, 9, 10, 38, 1, 900183),
'updated_at': datetime.datetime(2023, 10, 9, 10, 38, 1, 900224)}
```
**Now lets update the instance and add a new object to it.**
```
(hbnb) update BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d Name "Eric"
(hbnb) show BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
[BaseModel] (ab763e7e-4bc8-4380-bb07-0a07a8f1a56d) {'id': 'ab763e7e-4bc8-4380-bb07-0a07a8f1a56d',
'created_at': datetime.datetime(2023, 10, 9, 10, 38, 1, 900183),
'updated_at': datetime.datetime(2023, 10, 9, 11, 3, 0, 44871),
'Name': 'Eric'}
```
**Now lets use the all command to display any instance of any Class!**
```
(hbnb) create BaseModel
a8259ae7-2ecb-4fb9-aafc-0e4244adf089
(hbnb) create User
2e2244f0-4f38-4c5e-9ecd-fe3f452bf7b8
(hbnb) create Place
af95611c-9ab1-459d-809c-f371eac2a5ef
(hbnb) all
[BaseModel] (a8259ae7-2ecb-4fb9-aafc-0e4244adf089) {'id': 'a8259ae7-2ecb-4fb9-aafc-0e4244adf089',
'created_at': datetime.datetime(2023, 10, 9, 11, 43, 8, 384959),
'updated_at': datetime.datetime(2023, 10, 9, 11, 43, 8, 384984)}
[User] (2e2244f0-4f38-4c5e-9ecd-fe3f452bf7b8) {'id': '2e2244f0-4f38-4c5e-9ecd-fe3f452bf7b8',
'created_at': datetime.datetime(2023, 10, 9, 11, 43, 11, 498325),
'updated_at': datetime.datetime(2023, 10, 9, 11, 43, 11, 498340)}
[Place] (af95611c-9ab1-459d-809c-f371eac2a5ef) {'id': 'af95611c-9ab1-459d-809c-f371eac2a5ef',
'created_at': datetime.datetime(2023, 10, 9, 11, 43, 14, 199276),
'updated_at': datetime.datetime(2023, 10, 9, 11, 43, 14, 199337)}
(hbnb) 
```

**Now lets destroy the instance!**
```
(hbnb) destroy BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
(hbnb) show BaseModel ab763e7e-4bc8-4380-bb07-0a07a8f1a56d
** no instance found **
```
## Authors/Contact info :phone: :mailbox:
* **Eric Dzyk** **|** [Github](https://github.com/ericpo1sh) **|** [LinkedIn](https://linkedin.com/in/eric-dzyk-1b8976213) **|** [Email](mailto:ericpo1sh@gmail.com)  
* **Sammy Ansari** **|** [Github](https://github.com/O-01) **|** [LinkedIn](https://linkedin.com/in/sam-ansari-579553287) **|** [Email](mailto:na.01goli@gmail.com)
##
![Holberton School - School of Computer Science and Programming](https://uploads-ssl.webflow.com/6105315644a26f77912a1ada/63eea844ae4e3022154e2878_Holberton.png)
##
