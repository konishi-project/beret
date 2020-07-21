# Beret

**Wait, another backend?**

- Yes, I've decided that the effort of refactoring the previous one (Zimmerman) would take a lot more
of my resources than just making a new one.

**What's the goal?**

Just know that FastAPI has taken some inspirations from Flask and has a similar feel to it, so contributors won't feel much difference.

- The goal is to use a more modern framework that utilizes the standard of developing web REST APIs.

- The previous implementation was written using Flask
with the Flask-RESTX framework which is a fork and drop-in replacement for Flask-RESTPlus **(Project has been considered dead and unmaintained)**,which is quite buggy at the moment and the development is slow.

- It's not about the latest and greatest, but another reason to be doing this is to eventually have a stable and that the implemetation properly scales which utilizes unit testing to assist with its development process, which FastAPI supports really well.

**Why "Beret"?**

I couldn't really think of another name, "Be" stands for
backend, "re" simple means reformed, and just decided to add a "t" at the end. I do have plans however to archive the old backend and rename this project to Zimmerman to remove any confusion, so it might not matter at the end.

## Requirements

@TODO: Complete requirements section needed to run the application.

## Contributing

@TODO: Complete contributing section and guidelines for people to contribute to the project.

## Installation and Setting up

@TODO: Complete installation and setting up section so that it will run in most environments.

To run the application use (On Linux/MacOS): `$ uvicorn src.main:app`

## Deploying

There are a lot of guides on how to deploy a FastAPI application, which is also available in their [documentation](https://fastapi.tiangolo.com/deployment/).