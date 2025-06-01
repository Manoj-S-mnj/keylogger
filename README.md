STEP 1 : Initially update the all binary files in Linux system
sudo apt update
STEP 2 : Download an install venv
sudo apt install python3-venv
STEP 3 : install an virtual environment
python3 -m venv venv
STEP 4 : Execute an virtual environment 
source venv/bin/activate
// You will see like this
(venv) ┌──(username㉿kali)-[~/Desktop/python]
STEP 5 : Install pynput
pip install pynput
STEP 6 : Execute the keylogger.py
python keylogger.py
STEP 7 : Type anything in the keyboard 
STEP 8 : deactivate the keylogger
STEP 9 : Open the log.txt file to see the keystrokes of the keyboard
