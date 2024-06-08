# AR-MAIN-PROJECT-DEMO

## Overview
This project is a demo for an Augmented Reality (AR) application, developed with Flask and SQLAlchemy. It includes user authentication, featuring sign-up and login functionalities with email and mobile number-based authentication.

## Features
- User Registration
- User Login
- Mobile number-based login

## Requirements
- Postman Software For API & Python 3.x (Any IDE For Code)
- Libraries of Python ↓
  - Flask
  - SQLAlchemy
  - psycopg2
  - bcrypt

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/senkushaIN/AR-MAIN-PROJECT-DEMO.git
    cd AR-MAIN-PROJECT-DEMO
    ```
   
2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your PostgreSQL database and update the database URI in the configuration file (`config.py`):
    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/<dbname>'
    ```

## Running the Application

1. Apply database migrations:
    ```sh
    flask db init  # When creating Database Table For First Time
    flask db migrate -m "Initial migration"  # For Any Changes User Wants In The Table So Please Do This First And Then Upgrade
    flask db upgrade  # For Upgrading The Database of PostgreSQL
    ```

2. Run the Flask application:
    ```sh
    flask run
    ```

## API Endpoints

### Sign Up
- **DEFAULT FLASK GENERATED URL:** `http://127.0.0.1:5000/signup`
- **URL IF CUSTOMIZED IN CODE:** `http://127.0.0.1:5000/<customization as per code>/signup`
- **Method:** `POST`
- **Data Params:**
    ```json
    {
      "name": "your_username",
      "email": "your_email@example.com",
      "mobile": "your_mobile_number",
      "whatsappNotificationEnabled": true
    }
    ```
- **Success Response:**
    - **Code:** 201
    - **Content:** 
        ```json
        {
          "message": "User Created Successfully",
          "status": "Success",
          "data": {
            "token": "<Encrypted Token>"
          }
        }
        ```
- **Error Response:**
    - **Code:** 409
    - **Content:** 
        ```json
        {
          "status": "Failed",
          "message": "Username already exists"
        }
        ```
    - **Code:** 409
    - **Content:** 
        ```json
        {
          "status": "Failed",
          "message": "Email already exists"
        }
        ```
    - **Code:** 409
    - **Content:** 
        ```json
        {
          "status": "Failed",
          "message": "Mobile number already exists"
        }
        ```

### Login
- **DEFAULT FLASK GENERATED URL:** `http://127.0.0.1:5000/login`
- **URL IF CUSTOMIZED IN CODE:** `http://127.0.0.1:5000/<customization as per code>/login`
- **Method:** `POST`
- **Data Params:**
    ```json
    {
      "email": "your_email@example.com",
      "mobile": "your_mobile_number"
    }
    ```
- **Success Response:**
    - **Code:** 200
    - **Content:** 
        ```json
        {
          "message": "Login Successfully",
          "status": "Success",
          "data": {
            "token": "<Encrypted Token>"
          }
        }
        ```
- **Error Response:**
    - **Code:** 401
    - **Content:** 
        ```json
        {
          "message": "Invalid credentials",
          "status": "Failed"
        }
        ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
