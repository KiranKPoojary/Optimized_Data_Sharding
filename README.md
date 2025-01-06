# 🛡️ **Optimized Data Sharding and Clustering System**

## 📑 **Overview**

This project provides an **end-to-end system** for **uploading, sharding, and clustering datasets** using **Flask (backend)** and **React.js (frontend)**. Users can:
- Upload datasets in `.csv` format.
- Select from multiple sharding algorithms (`Hash`, `KMeans`, `DBSCAN`).
- Monitor **real-time sharding progress**.
- View **shard metadata and details** dynamically.

---

## 🚀 **Key Features**

- **🔼 File Upload:** Upload datasets seamlessly via a user-friendly UI.
- **📊 Sharding Algorithms:** Supports:
   - `Hash-based` Sharding  
   - `KMeans` Clustering  
   - `DBSCAN` Clustering  
- **📈 Real-Time Monitoring:** Dynamic status updates on sharding progress.
- **🗂️ Shard Visualization:** Detailed metadata for each shard, including file paths and summary statistics.
- **🌐 Cross-Origin Access:** Enabled using **Flask-CORS** for smooth API integration.

---

## 🛠️ **Tech Stack**

### **Backend:**
- 🐍 Python (Flask)
- 🐼 Pandas
- 📊 scikit-learn
- 🌐 Flask-CORS

### **Frontend:**
- ⚛️ React.js
- 🔗 Axios

### **Deployment (Optional):**
- 🐳 Docker
- ☸️ Kubernetes

---

# ⚙️ **Project Setup and Execution Steps**

## 📂 **Step 1: Clone the Repository**

Clone the project from GitHub:

```bash
git clone https://github.com/YourUsername/optimized-data-sharding.git
cd optimized-data-sharding
```

##  🐍 **Step 2: Backend Setup**
Navigate to the backend folder:

```bash

# Go to the backend directory
cd backend/

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment (Linux/MacOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

# Create necessary directories if they don't exist
mkdir -p uploads shards

# Start the backend server
python app.py
```
## **Backend will run at: http://127.0.0.1:5000**

##  🐍 **💻 Step 3: Frontend Setup**
```bash
# Go to the frontend directory
cd ../frontend/

# Install dependencies
npm install

# Start the frontend server
npm start
```

## **Frontend will be available at: http://127.0.0.1:3000**

## 🌐 **Step 4: API Configuration**
Ensure the frontend API is correctly pointing to the backend.

```bash
Copy code
# Open api.js for editing
nano src/services/api.js
```  

Ensure the file contains:
```bash
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:5000';
```