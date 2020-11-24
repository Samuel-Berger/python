# README

Diverse

## Just Run the Thing

In case everything necessary is installed, this will hopefuylly run the code.

```sh
cd ~/git/python     # Or where you clone the repo
source env/bin/activate
pip install -r requirements.txt
podman run --rm -v $PWD:/srv:z -p 8000:8000 --name fastapi -d fastapi
firefox localhost:8000
# when done
podman stop fastapi
deactivate
```

## Types

[Built in types](https://docs.python.org/3/library/stdtypes.html)
Python Tutorial

## List of some different variable types

```python
x = 123      # integer
x = 123L     # long integer
x = 3.14      # double float
x = "hello"       # string
x = [0,1,2]       # list
x = (0,1,2)       # tuple
x = open(‘hello.py’, ‘r’)  # file
```

## the Python Interpreter

### Execute from Python Interpreter

From [Stack Overflow](https://stackoverflow.com/a/1027730):

```python
>>> exec(open("filename.py").read())
# or
>>> from pathlib import Path
>>> exec(Path("filename.py").read_text())
```

### Create virtual enviroment from existing project

Adapted from [Stack Overflow](https://stackoverflow.com/a/41746628) to work on Ubuntu.
Make sure you make a copy of your project or commit everything to a version control system
before doing these changes, that way you can easily roll back in case something goes wrong.

First `cd` into an existing project then do as follows:

```sh
virtualenv env  # perhaps not: https://stackoverflow.com/a/39713544
pip3 freeze > requirements.txt
vi requirements.txt
# comment out everything you don't explicity need,
# see https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e
source env/bin/activate
pip install -r requirements.txt
deactivate # To exit the enviroment
```

It is a good idea to add the `env` directory to your `.gitignore`.

### Create a web back-end

First install [podman](https://podman.io/getting-started/installation).
Fedora Magazine has [a nice article](https://fedoramagazine.org/use-fastapi-to-build-web-services-in-python/)
on how to get started. Beware that it might work better to start the container with
`podman run --rm -v $PWD:/srv:z -p 8000:8000 --name fastapi -d fastapi` and the visit
`http://localhost:8000/` with a web browser. The python file serving the site also
need to be namned `main.py`.

When the service is working, try using Docker
[best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
to adapt the Docker container to use 64-bit Fedora and then Ubuntu.

## Misc

A list of The Python Interpreters [Built-in Functions](https://docs.python.org/3/library/functions.html#execfile)

## External Links

* [Installation](https://pip.pypa.io/en/latest/installing/#using-linux-package-managers)
* [Tutorial](https://www.w3schools.com/python/default.asp)
* [VirtualEnv](https://www.code-learner.com/how-to-install-and-use-python-virtualenv-module/)
* [To Do](https://www.programcreek.com/2013/08/leetcode-problem-classification)
* [Best practices](https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5)
* [FastAPI](https://fastapi.tiangolo.com/) with [example](https://fedoramagazine.org/use-fastapi-to-build-web-services-in-python/)
