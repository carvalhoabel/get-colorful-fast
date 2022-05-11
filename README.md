# Get Colorful

This project take a picture in gray scale and become it a colorful picture. It takes a grey scale image and change it to a colorful image. It project is build in [Python.](https://www.python.org/)

# Requiremtents and Dependencies

What was used to do this project, libraries and API's.

## Libraries

Below, you can see the requirements to this project.

* certifi 2021.10.8
* charset-normalizer 2.0.12
* idna 3.3
* requests 2.27.1
* urllib3 1.26.9
* pytest 7.1.2

You can found that list at [requirements.txt](requirements.txt), to install that, please run: <code>pip install -r requirements.txt</code>.

## Project API

This project as made with [DeepAI](https://deepai.org/machine-learning-model/colorizer) colorizer API, it is a fantastic project. It's an external API.

It returns a json with an **output url** if ```success``` else an **error message.**

At this project, I did a class, you can find [here.](src/core/api/api_deepai.py) It has two methods:

* Method 1 # Download from an URL;
* Method 2 # Download from a local file;

> Note: I imported the method post as ```deep_ai``` from ```requests```library, it was used to make a request from this API. To come here, it is need to pass to a successful validation process before.

# Project Architecture

Look at how the project packages organization was thought.

```
    src >
    |   __init__.py
    |   core >
    |   |   api >
    |   |   |   __init__.py
    |   |   |   api_deepai.py
    |   |   facade >
    |   |   |   __init__.py
    |   |   |   facade.py
    |   |   message >
    |   |   |   __init__.py
    |   |   |   message.py
    |   |   service >
    |   |   |   __init__.py
    |   |   |   service.py
    |   |   singleton >
    |   |   |   __init__.py
    |   |   |   sing_facade.py
    |   |   |   sing_message.py
    |   |   utils >
    |   |   |   __init__.py
    |   |   |   utils.py
    |   model >
    |   |   __init__.py
    |   |   picture.py
    |   view >
    |   |   __init__.py
    tests > # to test, run "pytest" here
    |   download > # (not pushed) it belongs to tests only
    |   images >
    |   |   __init__.py
    |   |   img1954.jpg
    |   |   img1962.jpg
    |   utils >
    |   |   __init__.py
    |   |   utils.py
    |   __init__.py
    |   test_tests.py
    main.py
    LICENSE
    README.md
    requirements.txt
```

# Project Data Model

The file **[```picture.py```](src/model/picture.py)** is the project model class. It is to save data to make required operation. It has the following parameters:

* ```name -> picture file name;```
* ```source -> picture source, online or local file;```
* ```save -> the path where the file changed must be saved;```
* ```online -> boolean to switch between online or local file;```

# Testing Project

To make request automatic testings were used <code>pytest</code> module at **[tests](tests)** package. You need to enter at this directory and run <code>pytest</code>, they are 10 tests, if all success, everything is fine.

# Project Design

Here you can see how this project communicate to another layers.

+ [Picture instance](src/model/picture.py) <code><strong>Model to access backend by SingFacade, Facade, Service and APIDeepAI if checks successful.</strong></code>
    + [SingFacade](src/core/singleton/sing_facade.py) - <code>Get Facade instance, a class method facade(). It returns Facade().</code>
        + [Facade](src/core/facade/facade.py) <code>Get Facade instance from SingFacade. <strong>It has 2(two) possible nethods</strong>, it returns json type.</code>
            + [Service](src/core/service/service.py) <code>Instance to access service, checks data and if success, access APIDeep instance. It returns a json.</code>
                + [APIDeepAI](src/core/api/api_deepai.py) <code>Where send data to API and download photo <strong>(Service() checks needs to be a success).</strong></code>
                + [SingMessage](src/core/singleton/sing_message.py) <code>Singleton Pattern to Access Message</code>
                    + [Message](src/core/message/message.py) <code>Message Class accessed by it Singleton, it is used only here.</code>
                + [Utils Module](src/core/utils/utils.py) <code>This module has required functions to use at Service instance.</code>      
