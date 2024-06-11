# TIXITO
---

## RS_TICKET

### Description

This pull request introduces a comprehensive set of API endpoints for managing tickets within the Tixito-PythonAPIs project. The following features and functionalities have been implemented:

### Features

1. **Create Ticket Endpoint**
   - **URL**: `/tickets`
   - **Method**: `POST`
   - **Description**: Allows users to create a new ticket by providing necessary details such as `actualPrice`, `comment`, `eventVenuesID`, `imageURL`, `listingPrice`, `lock`, `ordersID`, `sellerID`, `sellingPrice`, `status`, `type`, `validatedOn`, and `verified`.
   - **Error Handling**: Returns appropriate error messages and status codes for bad requests, unauthorized access, and database connection failures.

2. **Get Ticket Endpoint**
   - **URL**: `/tickets/<int:ticket_id>`
   - **Method**: `GET`
   - **Description**: Retrieves the details of a specific ticket by its ID.
   - **Error Handling**: Returns appropriate error messages and status codes for ticket not found and database connection failures.

3. **Update Ticket Price Endpoint**
   - **URL**: `/tickets/<int:ticket_id>/price`
   - **Method**: `PATCH`
   - **Description**: Updates the selling price of a specific ticket by its ID.
   - **Error Handling**: Returns appropriate error messages and status codes for bad requests, ticket not found, and database connection failures.

4. **Validate Ticket Endpoint**
   - **URL**: `/tickets/<int:ticket_id>/validate`
   - **Method**: `PATCH`
   - **Description**: Updates the validation status of a specific ticket by its ID.
   - **Error Handling**: Returns appropriate error messages and status codes for bad requests, ticket not found, and database connection failures.

### Enhancements

- **Error Handling**: Custom error handlers for `404 Not Found` and `500 Internal Server Error` have been implemented to provide more user-friendly error messages.
- **Logging**: Integrated logging to capture and log errors for easier debugging and maintenance.

### Database Connection

- Utilizes PostgreSQL for database operations.
- Includes a `get_db_connection` function to handle database connection setup and error handling.

### Setup Instructions

1. **Create `requirements.txt` File**

   Ensure the following dependencies are listed in your `requirements.txt` file:

   ```plaintext
   Flask
   psycopg2-binary
   ```

2. **Clone the Repository**

   ```sh
   git clone https://github.com/lipikam1110/Tixito-PythonAPIs.git
   cd Tixito-PythonAPIs
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**

   Ensure you have a PostgreSQL database set up with the required schema. Update the database credentials in the `get_db_connection` function in `app.py`.

5. **Run the Application**

   ```sh
   python app.py
   ```

6. **Use API Endpoints**

   Test the API endpoints using tools like Postman or Curl.

### How to Test

1. **Set up PostgreSQL Database**: Ensure you have a PostgreSQL database set up with the required schema.
2. **Configure Environment Variables**: Update the database credentials in the `get_db_connection` function.
3. **Run the Application**: Start the Flask application by running:
   ```sh
   python app.py
   ```
4. **Use API Endpoints**: Test the API endpoints using tools like Postman or Curl.

### Notes

- Make sure to handle sensitive data appropriately and not to hardcode credentials in the code.
- Follow the project's contribution guidelines for any further enhancements or bug fixes.

---
