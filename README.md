# Flask SQLite3 CRUD API

This is a basic Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations on a SQLite3 database. It provides a simple API for managing user data, including their names and email addresses.

## Features

- Create a new user
- List all users
- Retrieve a single user by ID
- Update user details
- Delete a user

## Prerequisites

- Python 3.7 or higher
- Flask library
- SQLite3 (comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.

   ```bash
   git clone <repository_url>
   cd flask_sqlite_crud
   ```

2. Create a virtual environment (optional but recommended).

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies.

   ```bash
   pip install flask
   ```

4. Run the application.

   ```bash
   python app.py
   ```

5. Access the application at `http://127.0.0.1:5000`.

## API Endpoints

### Create a User

**POST** `/users`

- **Request Body**:
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

### List All Users

**GET** `/users`

- **Response**:
  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  ]
  ```

### Get a User by ID

**GET** `/users/<user_id>`

- **Response** (if user exists):
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Response** (if user does not exist):
  ```json
  {
      "error": "User not found."
  }
  ```

### Update a User

**PUT** `/users/<user_id>`

- **Request Body**:
  ```json
  {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
  }
  ```

### Delete a User

**DELETE** `/users/<user_id>`

- **Response** (if user exists):
  ```json
  {
      "message": "User deleted successfully."
  }
  ```
- **Response** (if user does not exist):
  ```json
  {
      "error": "User not found."
  }
  ```

## Project Structure

```
flask_sqlite_crud/
├── app.py          # Main application file
├── users.db        # SQLite3 database file (generated automatically)
└── README.md       # Project documentation
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Feel free to fork this repository and submit a pull request.

## Contact

For questions or feedback, please contact [your_email@example.com].
