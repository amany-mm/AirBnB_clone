# AirBnB clone - The console
![airbnb-project](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240514%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240514T181956Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5151d9fab02ac029d61a6c2fc05396d2b9fa3f9e7a60105ca396c63841e5bf94)


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
![console-diagram](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240515%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240515T100347Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a0a800fd30f7e306cc0112afa9f76ff2df6bf5ef79fb8107a317ebc59cbbeefa)


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
