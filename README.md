# assignment
Assignment CSV Project

### Requirements

- Install Python Version 3.11.2 from https://www.python.org/downloads/release/python-3112/

### Project Setup and Installation


- Install pip:
  ```bash
  sudo apt-get install python-pip
  ```
- Install virtualenv used for creating python virtual environments from https://virtualenv.pypa.io/en/latest/installation.html
- Create a directory for storing virtual envs, say for example your home directory. 

  ```bash
  cd /path/to/your/home/
  mkdir envs
  cd envs
  ```
- Inside envs directory create a virtual environment for this project using python 3.11.2
  ```bash
  virtualenv env_assignment -p python3.11
  ```
- Now this environment named env_assignment can be activated from anywhere, we will activate it from here now.
  ```bash
  source env_assignment/bin/activate
  ```
- Now clone this repo, make sure your environment is activated and install the requirements like below:

  ```bash
  pip install -r requirements.txt
  ```
- Run the project migrations for db changes used by Django
  
  ```bash
  python manage.py migrate
  ```
- Run the project instance/server for development

  ```bash
  python manage.py runserver
  ```
 
- Your project will run on localhost:8000/ by default
- Here are some sample endpoints that you can test

  - localhost:8000/
  - localhost:8000/action=list
  - localhost:8000/?year=2023
  - localhost:8000/?year=2023&product=UCOME
  - localhost:8000/?year=2023&product=UCOME&supplier=Sipes, Harber and Lynch
  - localhost:8000/?action=average-product-price-per-year&year=2023&product=UCOME

