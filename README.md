<div align="center">

# Used Cars Scraping 

</div>


<hr>

## Table of Contents

- [About Project](#about-project)
- [Application functional](#functional)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Shutdown](#shutdown)


<hr>

## About Project

The project is designed to bridge the information gap in the used car market. 
By collecting, and presenting data effectively, this project aims to empower users 
with the knowledge they need to make smart choices in buying or selling their vehicles. 
It has the potential to simplify the used car shopping process and foster 
a more transparent and competitive market environment.
<br>

<hr>

## Functional

1. Make used cars detail info scraping which is selling now <br>
2. Manage information using the PostgreSQL
3. Get the possibility to receive updated data by auto scraping every day at 12:00 by Kyiv
4. TTransfer the data into different databases, etc. from json file with all data
5. Receive always actual data in json file by auto database dump at 00:00 by Kyiv

<hr>

## Technologies

- [Django Official Documentation](https://docs.djangoproject.com/)
<br>`Django` is a high-level Python Web framework. 
In this project, it's used to create the backend service. 
<br>In this project Django is used as the ORM.


- [Postgres Official Documentation](https://www.postgresql.org/docs/)
<br>`Postgres` is a powerful, open-source object-relational database system. 
In this project, it is used as the main data store. 
<br>This service runs the latest version of Postgres, exposed on port 5432.


- [Celery Documentation](https://docs.celeryq.dev/en/stable/)
<br>`Celery` is a simple, flexible, and reliable distributed system to process vast amounts of messages, 
while providing operations with the tools required to maintain such a system.
It’s a task queue with focus on real-time processing, while also supporting task scheduling. 
<br>In this project, it is used to run periodic tasks in the background. 


- [Redis Documentation](https://redis.io/docs/)
<br>`Redis` is an open source (BSD licensed), in-memory data structure store used as 
a database, cache, message broker, and streaming engine. 
<br>In this project, it is used as a Celery message broker. 


- [Selenium Documentation](https://www.selenium.dev/documentation/)
<br>`Selenium` is an umbrella project for a range of tools and libraries that enable 
and support the automation of web browsers.
<br>In this project, it is used for used car scraping info. 


<hr>



## Prerequisites

1. Make sure you have Python installed on your system. 
You can check the installation instructions [here for Python](https://www.python.org/downloads/).
2. Make sure you have Docker and Docker Compose installed on your system. 
You can check the installation instructions [here for Docker](https://docs.docker.com/get-docker/) 
and [here for Docker Compose](https://docs.docker.com/compose/install/).

<hr>

## Setup

1. Clone the project:
```
https://github.com/diana-shyrokikh/used-cars-scraping.git
```

2. Navigate to the project directory:
```
cd used-cars-scraping
```

3. Сreate your .env file taking as an example .env.example file


4. Build and run the Docker containers:
```
docker-compose build
docker-compose up
```


<hr>

## Shutdown

1. To stop running application use CTRL-BREAK

<hr>
