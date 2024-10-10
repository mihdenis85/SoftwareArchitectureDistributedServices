# SoftwareArchitectureDistributedServices

This project is twitter-like system based on service-based pattern from [FOSA].

## Agenda

* [Demo](#demo)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Project Structure](#project-structure)
* [Services Overview](#services-overview)
* [Contacts](#contacts)

## Demo

## Features

- User Service: registration/getting users.
- Message Service: post/get/like messages.
- Feed service: get all posted messages.

## Prerequisites

- Python 3.10+
- Nginx

## Installation

1. Clone the repository:

```shell
git clone https://github.com/mihdenis85/SoftwareArchitectureDistributedServices.git
```

2. Install the required packages for every service:

```shell
cd src/feed_service
pip install -r requirements.txt
cd ..
cd src/message_service
pip install -r requirements.txt
cd ..
cd src/user_service
pip install -r requirements.txt
cd ..
cd ..
```

3. Install nginx\
https://nginx.org/en/docs/install.html

## Usage

1. Run nginx (follow the instruction from official nginx website)

2. Run user service:

```shell
cd src/user_service
uvicorn main:app --host 127.0.0.1 --port 8001
```

3. Run message service (use different terminal instance):

```shell
cd src/user_service
uvicorn main:app --host 127.0.0.1 --port 8002
```

4. Run feed service (use different terminal instance):

```shell
cd src/user_service
uvicorn main:app --host 127.0.0.1 --port 8003
```

5. Run as many clients as you want (use separate terminal instance for each client):

```shell
python client.py
```

## Project Structure

```
├── src
│   ├── feed_service
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   ├── message_service
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   ├── user_service
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   ├── __init__.py
├── .gitignore
├── client.py
└── README.md
```

## Services Overview

### User Service

Provides user registration functionality, and checking that user exists.

### Message Service

Provides functionality to post, get and like messages.

### Feed Service

Provides functionality to get all messages.

## Contacts

- Denis Mikhailov - d.mikhailov@innopolis.university
- Anton Chulakov - a.chulakov@innopolis.university
- Adel Shagaliev - a.shagaliev@innopolis.iniversity
- Ilya Zubkov - i.zubkov@innopolis.university