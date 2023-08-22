# Doctor Kevin House
- Please run pipenv shell
- cd into the lib directory
- run Python seed_2.py
- once finshed run Python cli.py to start the program

## Project requirements

In this project, we're going to use these skills to create a CLI. You won't be able to fit everything in from phase 3, but the following are the minimum requirements:
- A CLI application that solves a real-world problem and adheres to best practices.
- A database created and modified with SQLAlchemy ORM with 2+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists and dicts

Consider these stretch goals as you progress through your project:

- database created and modified with SQLAlchemy ORM with 3+ related tables.
- Use of many-to-many relationships with SQLAlchemy ORM.
- Use of additional data structures, such as ranges and tuples.

## Creating project
To start the project I used the template provided by the course for phase 3 project. I then removed the metadata as instructed using rm -rf .git .canvas
This removed the Git Repo and allows me to create and track my own local repository and push it into my own Git Repo. I renamed the file to project name, the used git init
to create my local repository. git add --all then added all the local files. git commit -m'initial commit' made my first commit and commit al my saved work to the repository. I creatyed a new reposiroty on my GitHub website. I copied the shh and ran git remote add origin `<github url>` to map my local repository to my git hub repo. Finally i pushed using git push -u origin main to make my first push and upload my project to my github repo.

## Installing necessary libraries and packages
For this project i install sqlalchemy and alembic to start. 

    pipenv install sqlalchemy alembic
installed the sqlalchemy library anlong with the alembic library. Then I was ready to enter my pip enviroment. 

    pipenv shell
## Functionality