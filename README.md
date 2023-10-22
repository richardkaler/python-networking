# python-networking
I plan to add quite a bit here to make navigating this repo easier. let's start with the basics 

REQUIRED PACKAGES for ssh_input_connect.py: 

NOTE: See below - regaring my thoughts on python venvs 

python3 -m venv virtual-env #The first argument or the name of the Python version may vary but for most systems using Python 3, this command will do  

To activate the venv: 
source ./virtual-env/bin/activate 
NOTE: In a Linux terminal, once the venv has been activated, you should see (virtual-env) to the left of your user name. Whenvever you see that, your venv 
is active - and whatever you install using pip will pertain to the venv created. That simple. To leave the venv simply type ' deactivate ' - without single quotes 

pip install paramiko 
(This is critical and without it the basic ssh functionality of the script will not work.) 
pip install maskpass 
(This is a cool library that allows you to input a password for the ssh server targeted - and without the input echoing on the terminal.) 

I would like to include a requirements text so that all of these packages run automatically - and that having been said, I am a firm believer in using Python virtual environments. Do not be so bold 
as to install these dependencies with pip without first setting up a venv. I have scripts that will install the venv for you but if you're new to Python it's as simple as: 
python -m venv virtual-env (or whatever you want to name your venv as the final argument) 


Very bad things happen when Python coders are so audacious as to install dependencies without using a venv - and you can read all about dependency conflicts which will invariably arise as a result. 

Soon enough, I will add instructions on how to convert your Python binaries into standalone executables using pyinstaller. In order for that to work, 
the required packages listed above must first be installed. 

