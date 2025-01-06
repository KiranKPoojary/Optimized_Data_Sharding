# 🛡️ Optimized Data Sharding and Clustering System

## 📑 **Overview**

This project provides a **Flask-based backend** and **React.js-based frontend** to enable **database upload, sharding, and clustering operations**. Users can upload a CSV dataset, select a clustering or sharding algorithm, monitor real-time progress, and view detailed metadata for each shard.

---

## 🚀 **Key Features**

- **🔼 File Upload:** Upload datasets via an intuitive frontend UI.
- **📊 Sharding Algorithms:** Supports `Hash-based`, `KMeans`, and `DBSCAN` algorithms.
- **📈 Real-time Monitoring:** Track sharding progress dynamically via status updates.
- **🗂️ Shard Visualization:** View metadata and details of created shards.
- **🌐 Cross-Origin Access:** Enabled via Flask-CORS for seamless frontend-backend communication.

---

## 🛠️ **Tech Stack**

### **Backend:**
- Python (Flask)
- Pandas
- scikit-learn
- Flask-CORS

### **Frontend:**
- React.js
- Axios

### **Deployment Tools:**
- Docker (optional)
- Kubernetes (optional)

---

## ⚙️ **Setup Instructions**

### 🐍 **Backend Setup**

1. Navigate to the backend folder:
   ```bash
   cd backend/
