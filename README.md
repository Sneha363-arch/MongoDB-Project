MongoDB Student Analytics Dashboard
Overview

This project is a full-stack Student Analytics Dashboard that manages and analyzes large student datasets. It uses MongoDB as the database and Flask as the backend to process data and provide insights through a web-based interface.

Features
Search and filter student records based on parameters such as department and marks
Sort data in ascending or descending order
Pagination for handling large datasets efficiently
Aggregation pipelines for analytics:
Average marks calculation
Department-wise distribution
Data visualization using tables, bar charts, and pie charts
Tech Stack
Backend: Flask (Python)
Database: MongoDB
Database Driver: PyMongo
Frontend: HTML, CSS, JavaScript
Visualization: Chart.js (or equivalent)
System Architecture

Frontend → Flask Backend → PyMongo → MongoDB

Core Functionalities
Data Retrieval

Student data is retrieved using filtering, sorting, and pagination:

collection.find(query).sort("marks", -1).skip(offset).limit(limit)
Aggregation

MongoDB aggregation pipelines are used for analytics:

pipeline = [
    {"$group": {"_id": "$department", "avgMarks": {"$avg": "$marks"}}},
    {"$sort": {"avgMarks": -1}}
]
Pagination

Efficient handling of large datasets using:

skip()
limit()
Project Structure
MongoDB-Project/
│── backend/
│   ├── app.py
│   ├── routes/
│   └── db_config.py
│
│── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
│── data/
│   └── students.json
│
│── README.md
Setup Instructions
Clone Repository
git clone https://github.com/Sneha363-arch/MongoDB-Project.git
cd MongoDB-Project
Install Dependencies
pip install flask pymongo
Run Application
python app.py
Access Application

Open browser and go to:

http://localhost:5000
Use Cases
Analyze student performance
Compare department-wise results
Identify high-performing students
Limitations
No authentication or authorization
Basic UI design
Not optimized for large-scale deployment
Future Improvements
Add authentication (JWT)
Upgrade frontend to React
Deploy on cloud platforms
Improve UI and user experience
Author

Sneha
