
# Bank API 
This is a simple Flask API for retrieving information about banks and branches from a SQLite database. 
## Features 
- **/healthcheck**: A health check route to ensure the API is up and running.
 - **/banks**: Endpoint to retrieve a list of all banks. 
 - **/branches/<ifsc>**: Endpoint to retrieve details of a specific bank branch using its IFSC code. 
 ## Requirements
  - Python 3.x
  - Flask
  - Flask-CORS 
  - Flask-Swagger 
 
 ## Testing
 Use the link to test and use the API.
 
  ## Installation for develeopment 
  1. Clone the repository: `git clone <repo_url> cd bank-api `
  2. Install dependencies: `pip install -r requirements.txt `
  
  ## Usage 
  4. Start the Flask server: python app.py 
  5. Access the Swagger UI for API documentation and testing at `http://localhost:5000/apidocs`. 
  ## API Endpoints 
  ### Health Check 
  - **URL:** `/healthcheck`
   - **Method:** GET 
   - **Response:** ```json {"message": "ok"} ``` 
 ### Get All Banks
  - **URL:** `/banks` 
  - **Method:** GET
  - **Response:** ```json [ {"id": 1, "name": "Bank A"}, {"id": 2, "name": "Bank B"}, ... ] ``` 
  ### Get Branch by IFSC Code 
  - **URL:** `/branches/<ifsc>`
  - **Method:** GET 
  - **Parameters:** 
  - - `ifsc` (path parameter): IFSC code of the branch 
  - **Responses:**
  -  - **200 OK** 
  ```json { "ifsc": "IFSC001", "branch": "Branch Name", "address": "Branch Address", "city": "Branch City", "district": "Branch District", "state": "Branch State", "bank": { "id": 1, "name": "Bank A" } } ``` 
  - - **404 Not Found** 
  - ```json { "message": "Branch with IFSC '<ifsc>' not found" } ``` 
  ## License 
  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
