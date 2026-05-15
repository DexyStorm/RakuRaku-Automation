# RakuRaku-Automation

This little script will automate the boring RakuRaku job in Forza Horizon 6.

There are two scripts: simple.py and complex.py<br>
simple.py will only spam "enter" and try to turn auto-drive on. If a job gets picked in which auto-drive cannot be used, simple.py will wait until the job timer has run out and accept a new job, while complex.py tries to exit the current job and re-enter it.


# Requirements: 

You will need python https://www.python.org/downloads/, pip and tessaract https://tesseractocr.org/ installed.

# Usage

Linux:

$ git clone git@github.com:DexyStorm/RakuRaku-Automation.git

$ cd RakuRaku-Automation

RUN THE NEXT COMMAND ONLY THE FIRST TIME YOU CLONE THE REPO<br>
$ python -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

Open Forza Horizon 6 and start a RakuRaku Job.

$ python3 simple.py

Windows:

https://archlinux.org/download/

Macos:

https://www.amazon.com/s?k=gaming+pc&crid=7MSDR5BWRX5H&sprefix=gaming+%2Caps%2C217