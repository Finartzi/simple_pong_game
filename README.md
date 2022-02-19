# Simple Pong game  - By @TokyoEdTech

<https://www.youtube.com/watch?v=C6jJg9Zan7w>

## Virtual environment

    "#" means in terminal input:

    - Installing virtual environment
        # pip3 install virtualenv

    - creation on virtual environment
        # python3 -m venv /path/to/new/virtual/environment
        In this my case:
        # python3 -m venv ~/programmin/pythonized/simple_pong_game/pong-venv

    - Checking, if venv works
        #python3 -m venv -h
        You can see in terminal "(venv)" in the beginning of a new line before prompt

    - starting of a virtual environment
        # source (your project path/)venv/bin/activate
        # source pong-venv/bin/activate

    - ending of a virtual environment
        # deactivate

    - Creating requirements.txt file (if it doesn't exist already)
        # pip3 freeze > requirements.txt
    
    - Loading requirements.txt - modules
        # pip3 install -r requirements.txt

## Needed packages

    - # pip3 install turtle
    - # sudo apt install python3-tk

## Solving aids listed here

    - <https://docs.python.org/3/library/venv.html>
