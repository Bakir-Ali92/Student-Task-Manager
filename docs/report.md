# Assignment Report: Student Task Manager Development

**Student Name:** Muhammad Bakir Ali 
**Student ID:** FA23-BSE-101-A  
**Repository URL:** https://github.com/Bakir-Ali92/Student-Task-Manager

---

## Part A: Repository Setup and Version Control
A public repository named `studenttaskmanager` was successfully created on GitHub. The repository was initialized with a `README.md`, a Python `.gitignore` file, and an MIT License. The basic structure of the `task_manager.py` application was developed locally and pushed to the `main` branch using a standard Git workflow (`git status`, `add`, `commit`, `push`). 

## Part B: Branching and Feature Development
Three separate feature branches were created to modularize development:
1. `feature/addtask`: Implemented adding tasks with validation to reject empty titles.
2. `feature/completetask`: Implemented logic to mark tasks as completed (`[x]`).
3. `feature/deletetask`: Implemented task removal using index validation.

**Why Branches are Useful:**
Branches are essential because they allow developers to work on new features, fix bugs, or experiment in an isolated environment without destabilizing the main production codebase (`main` branch). This workflow prevents unfinished code from breaking the application and enables multiple team members to work concurrently on different features without their changes interfering with one another.

## Part C: GitHub Issues and Pull Requests
To organize the development process, four GitHub Issues were created and labeled appropriately (e.g., *enhancement*, *testing*). 
For each feature branch, a Pull Request (PR) was opened against the `main` branch and linked to its corresponding Issue. Code changes were reviewed, a review comment was added, and the branches were successfully merged into `main`, automatically closing the linked issues.

## Part D: Merge Conflict Resolution
A merge conflict was deliberately created by modifying the same line in `README.md` ("Project status: Planning") differently across two separate branches.

**What Caused the Conflict:**
A merge conflict occurs when two branches modify the exact same line in a file, or when one branch edits a file while another deletes it. Git cannot automatically determine which developer's changes should take precedence. Therefore, it halts the merge process and requires manual intervention to choose the correct code. 

I resolved this by opening the affected file, removing Git's conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`), keeping the desired final text, and completing the merge with a new commit.

**Screenshots:**
*Conflict Markers Before and After Successful Resolution:*
in screenshots/conflicts.png

## Part E: GitHub Actions and Testing
A test suite was created using Python's built-in `unittest` framework, covering the addition, completion, and deletion of tasks. A Continuous Integration (CI) pipeline was set up using GitHub Actions to automatically run these tests upon any push or Pull Request to the `main` branch.

**Screenshots:**
*Failed GitHub Actions Run (Intentional test break):*
in screenshots/failed.png

*Successful GitHub Actions Run:*
in screenshots/pass.png

## Part F: Documentation and Release
Project documentation was finalized to ensure end-users can easily run the application:
1. Updated the `README.md` with features, setup instructions, usage, and testing commands.
2. Created a dedicated user guide in `docs/userguide.md`.
3. Packaged the stable project state into a GitHub Release tagged as `v1.0.0`, including detailed release notes.