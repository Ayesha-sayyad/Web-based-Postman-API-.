# Web-based-Postman-API-.
Design a web-based application that accepts a list of numbers, computes the sum of those numbers, and returns the result. The application should save each transaction and its result in a database for future reference. If the same request is issued again, the result should be returned from the database instead of being recalculated.

**🔢 Sum API Project**

A simple Django RESTful API to calculate the sum of a list of numbers. It also uses caching to improve performance and avoid repeated calculations for the same input.

**🚀 Features**
Accepts a list of numbers in a POST request and returns their sum.

Caches previously computed results to speed up repeated requests.

Returns a cached: true flag in the response if the result was returned from cache.


**🛠️ Tech Stack**
Python 3.x

Django 5.x

Django REST framework

SQLite (default for development)

Redis (optional for real caching)

Postman

**📦 Installation**

1. Clone the repository
git clone https://github.com/your-username/sum_api_project.git
cd sum_api_project

3. Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac

4. Run database migrations:
python manage.py migrate

5. Start the development server:
python manage.py runserver

6. Open your browser at: [http://127.0.0.1:8000/sum/](http://127.0.0.1:8000/api/sum)

**📬 API Usage**

Endpoint: api/sum/
Method: POST
Payload Format:
{
  "numbers": [1, 2, 3, 4]
}

Success Response:
{
  "sum": 10,
  "cached": false
}

Error Responses:
If numbers is missing:
{ "error": "'numbers' key is required" }

If list contains non-integer:
{ "error": "All elements must be integers" }

If list is empty:
{ "sum": 0, "cached": false }

**✅ Running Tests**
Run all unit tests using:
python manage.py test api

The test cases cover:
Valid sum input
Empty list
Cached result
Invalid string input
Missing numbers key


**Output**
<img width="1877" height="822" alt="Screenshot 2025-08-01 003733" src="https://github.com/user-attachments/assets/919da76a-4ade-4794-b4d5-4be6906dd83a" />
<img width="1899" height="914" alt="Screenshot 2025-08-01 003616" src="https://github.com/user-attachments/assets/8c333f79-83d9-4d4f-99cd-a2938735d3be" />
<img width="1916" height="972" alt="Screenshot 2025-07-30 164233" src="https://github.com/user-attachments/assets/6b31583d-866f-4943-ac7f-80b146182393" />

