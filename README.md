# HBNB (AirBnB clone v2 - MySQL)
![Holberton logo](https://www.holbertonschool.com/holberton-logo.png)
> This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON and MySQL.

## Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

## Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

### Create
`create <class name>`
Ex:
`create BaseModel`

### Show
`show <class name> <object id>`
Ex:
`show User my_id`

### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

### All
`all` or `all <class name>`
Ex:
`all` or `all State`

### Quit
`quit` or `EOF`

### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Authors
* **Miranda Evans**
* **Kevin Yook** - [yook00627](https://github.com/yook00627)
* **Luis Miguel Moreno Cano** - [lucho1503](https://github.com/lucho1503)
* **Diego Monroy** - [diegozencode](https://github.com/diegozencode)
