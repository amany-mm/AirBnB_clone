# AirBnB clone - The console
![airbnb-project](https://github.com/amany-mm/AirBnB_clone/blob/master/images/hbnb-logo.png)


## Description of the project
The goal of the project is to deploy on your server a simple copy of the AirBnB website.


## Description of the command interpreter:
This is the 1st step of the project - The console
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

The console will perform the following tasks:
* Create a new object
* Retrieve an object from a file
* Do operations on objects
* Destroy an object


## Diagram overview
![console-diagram](https://github.com/amany-mm/AirBnB_clone/blob/master/images/hbnb-console-diagram.png)


## Execution
Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


## Testing
All tests should also pass in non-interactive mode: 
```bash
$ echo "python3 -m unittest discover tests" | bash
```
