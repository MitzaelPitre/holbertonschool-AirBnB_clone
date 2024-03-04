# AirBnB clone - The console

## Welcome to the AirBnB clone project!

This project creates a functional implementation of an Airbnb clone in Python. We include data models, an interface, and a data storage system, all backed by unit tests to ensure its operation.

## Requirements

Python Scripts:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Test:

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks

0. README, AUTHORS

- Write a README.md:
description of the project
description of the command interpreter:
how to start it
how to use it
examples
You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
You should use branches and pull requests on GitHub - it will help you as team to organize your work

1. Be pycodestyle compliant!

- Write beautiful code that passes the pycodestyle checks.

2. Unittests

- All your files, classes, functions must be tested with unit tests

3. BaseModel

- Write a class BaseModel that defines all common attributes/methods for other classes:

4. Create BaseModel from dictionary

- it’s time to re-create an instance with this dictionary representation.

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

5. Store first object

- You will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

6. Console 0.0.1

- Write a program called console.py that contains the entry point of the command interpreter:

7. Console 0.1

Update your command interpreter (console.py):

8. First User

- Write a class User that inherits from BaseModel:

9. More classes!

- Write all those classes that inherit from BaseModel:

10. Console 1.0

- Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!
