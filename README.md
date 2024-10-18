```markdown
# Doctors Appointment API

This is a simple Flask API for managing doctor appointments, which includes operations to list, add, update, and delete doctor records. The API documentation is provided using Swagger UI, and you can also import the Postman collection to test the endpoints.

## Features

- View all doctors.
- Add a new doctor.
- Update existing doctor details by ID.
- Delete a doctor by ID.
- Swagger UI for API documentation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/doctors-appointment-api.git
   cd doctors-appointment-api
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. **Run the Flask app:**
   ```bash
   python app.py
   ```

2. **Access the Swagger UI:**
   Open your browser and go to: `http://localhost:5000/api/docs` to view the API documentation.

## API Endpoints

### Get All Doctors
- **URL:** `/api/doctors`
- **Method:** `GET`
- **Response:**
  - 200: List of doctors.
  - 404: No doctors found.

### Add a New Doctor
- **URL:** `/api/doctors`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "doctor_name": "Ali Hassan",
    "Speciality": "Cardiologist",
    "session_price": "400",
    "Address": "Downtown Cairo"
  }
  ```
- **Response:**
  - 201: Doctor added successfully.

### Update a Doctor by ID
- **URL:** `/api/doctor/{id}`
- **Method:** `PUT`
- **Body:**
  ```json
  {
    "doctor_name": "Ali Hassan",
    "Speciality": "Neurologist",
    "session_price": "600",
    "Address": "Downtown Cairo"
  }
  ```
- **Response:**
  - 201: Doctor updated successfully.
  - 404: Doctor not found.

### Delete a Doctor by ID
- **URL:** `/api/doctor/{id}`
- **Method:** `DELETE`
- **Response:**
  - 204: Doctor deleted successfully.
  - 404: Doctor not found.

## Swagger Documentation

- Swagger UI is available at: `http://localhost:5000/api/docs`
- The Swagger JSON file is located in `/static/swagger.json`.

## Postman Collection

A Postman collection is provided to easily test the API. To import the collection:
1. Open Postman.
2. Click "Import" and select the `postman.json` file.

## Dependencies

- Python 3.6+
- Flask
- Flask-Swagger-UI

## License

This project is licensed under the MIT License.
```

### Key Sections Explained:
- **Installation**: Guides users on how to set up the project and install dependencies.
- **API Endpoints**: Provides a brief overview of the available endpoints, request methods, and sample request/response bodies.
- **Swagger Documentation**: Explains how to access the Swagger UI for exploring the API.
- **Postman Collection**: Informs users about the availability of the Postman collection for testing.
- **License**: Mentions the licensing information.

This `README.md` gives a clear overview of how to set up, run, and use your API.
