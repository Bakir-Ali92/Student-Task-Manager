# Student Task Manager

A Python-based console application to manage daily tasks. This project was developed to practice a complete Git and GitHub version control workflow, including feature branching, pull requests, automated testing, and releases.

## Features
* **Add Tasks:** Create new tasks (includes validation to prevent empty task names).
* **Complete Tasks:** Mark specific tasks as `[x]` completed.
* **Delete Tasks:** Remove tasks entirely from the list.
* **View Tasks:** Display a numbered list of all current tasks and their status.

## Setup Steps
This application uses standard Python and requires no external libraries.
1. Clone the repository to your local machine:
   `git clone https://github.com/YOUR-USERNAME/studenttaskmanager.git`
2. Navigate into the project folder:
   `cd studenttaskmanager`

## Usage
Run the application from your terminal or command prompt:
`python task_manager.py`

## Test Instructions
This project uses Python's built-in `unittest` framework. To run the automated tests and see the results, run the following command in the root directory:
`python -m unittest discover -s tests -v`