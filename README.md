# Proyecto-Habitabilidad

Project made by:
- Jhojan Steven Aragon Ramirez 20221020060
- Santiago Reyes Gomez 20221020098
- Juan Diego Lozada Gonzalez 20222020014

This project is about make simulations in a buliding with the purpose to indicate how habitable is, according the light the building and the light given by the climate

First of all, we need to create an environment with the following characteristics:

- Windows
```bash
python -m venv venv
```

- Linux
```bash
python3 -m venv venv
```
Then we need to activate the environment with the following command:

- Windows
```bash
.\venv\Scripts\activate
```

- Linux
```bash
source venv/bin/activate
```
After that, we need to install the following packages:

```bash
pip install poetry
```
Poetry is a tool for dependency management in Python projects. It helps you declare, manage and install dependencies of your project.

Then we need to put the next command to create poetry.lock file:

```bash
poetry lock
```
After that we need to install the dependencies with the following command:

```bash
poetry install --no-root
```
We put --no-root because we don't want to install the dependencies in the global level, we want to install them in the project level.

After that, we need to execute the following command to run the project (make sure you are in the correct path):

```bash
python interfaz.py
```
Just wait a few seconds and the project will start.
The interface will be able in the next port http://127.0.0.1:8050/

Enjoy the project! :)

## Contact

Jhojan Steven Aragón jhojanramirez75@gmail.com

Santiago Reyes Gomez santi26reyes@gmail.com

Juan Diego Lozada juandiegolozada123@gmail.com













This Project is the final test of Computer Science 2 in University Distrital Jose de Caldas

![Texto alternativo](Images/logo.jpg "Título opcional")