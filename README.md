# Tixito-PythonAPIs

## Overview
This project is a demo for an authentication system using Python, Flask, SQLAlchemy, and React. It includes user registration and login functionalities with email and mobile number-based authentication, and it interacts with a React frontend.

## Features
- User Registration
- User Login
- Mobile number-based login
- JWT Token generation for authenticated sessions

## Requirements
- Python 3.x
- PostgreSQL
- Node.js and npm for the React frontend

### Python Libraries
- Flask
- Flask-CORS
- SQLAlchemy
- Flask-Migrate
- psycopg2
- jwt
- bcrypt
- python-dotenv

### JavaScript Libraries
- React
- axios
- react-router-dom
- react-toastify

## Backend Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/lipikam1110/Tixito-PythonAPIs.git
    cd Tixito-PythonAPIs
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

5. Set up your PostgreSQL database and update the database URI in the configuration file (`config.py`):
    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/<dbname>'
    ```

## Running the Backend Application

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

## Frontend Installation

1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Install the required packages:
    ```sh
    npm install
    ```

3. Start the React application:
    ```sh
    npm start
    ```

## API Endpoints

### Sign Up
- **URL:** `http://127.0.0.1:5001/Authentication/signup`
- **Method:** `POST`
- **Data Params:**
    ```json
    {
      "name": "your_username",
      "email": "your_email@example.com",
      "mobile": "your_mobile_number",
      "whatsappNotificationEnable": true
    }
    ```
- **Success Response:**
    - **Code:** 201
    - **Content:** 
        ```json
        {
          "status": "success",
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
          "status": "failed",
          "message": "Username already exists"
        }
        ```
    - **Code:** 409
    - **Content:** 
        ```json
        {
          "status": "failed",
          "message": "Email already exists"
        }
        ```
    - **Code:** 409
    - **Content:** 
        ```json
        {
          "status": "failed",
          "message": "Mobile number already exists"
        }
        ```

### Login
- **URL:** `http://127.0.0.1:5001/Authentication/login`
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
          "status": "success",
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
          "status": "failed",
          "message": "Invalid credentials"
        }
        ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
