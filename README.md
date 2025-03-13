# Medical Device Recommender
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![jQuery](https://img.shields.io/badge/jQuery-3.6-blue)
![Last Commit](https://img.shields.io/github/last-commit/freedomofchoice1991/medical_device_recommender)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![openFDA API](https://img.shields.io/badge/openFDA-API-blue)

This project is a **FastAPI-based medical device recommender** that suggests alternative medical devices based on their FDA classification.

## **Features**
✅ Search for a medical device by **Product Code**

✅ Find **strong matches** (same classification code)

✅ Find **potential alternatives** (same medical specialty)

✅ View **grouped classification data**

✅ **Export** results to **CSV or PDF**

✅ **Web-based frontend** using HTML, CSS, and jQuery

✅ **API testing with Pytest**

✅ **Continuous Deployment using GitHub Actions**

---
## **1️⃣ Installation & Setup**

### **Step 1: Clone the Repository**
```bash
   git clone https://github.com/YOUR_USERNAME/medical-device-recommender.git
   cd medical-device-recommender
```

### **Step 2: Set Up a Virtual Environment**
```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
```

### **Step 3: Install Dependencies**
```bash
   pip install -r requirements.txt
```

### **Step 4: Run the FastAPI Server**
```bash
   uvicorn app.main:app --reload
```

✅ The API will now be running at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

✅ API Docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---
## **2️⃣ Fetching FDA Data & Storing in SQLite**

Run the following script to **fetch medical device classifications** and store them in SQLite:
```bash
   python app/database.py
```
This will:
- Create the SQLite database (`medical_devices.db`)
- Fetch classification data from the FDA API
- Store it in the database

---
## **3️⃣ Running Tests with Pytest**

This project includes **unit tests** using `pytest`. Run tests with:
```bash
   pytest tests/
   # or for verbose version
   python -m pytest -v 
```
Tests include:
- Checking if the API is reachable
- Verifying device recommendations
- Handling edge cases (invalid product codes)

---
## **4️⃣ Using the Web Interface**

### **Launch the Web UI**
1. Open your browser
2. Go to: [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)
3. Enter a **Product Code** (e.g., `KNY`)
4. Click **"Search"** to see recommendations
5. Click **"Load Grouped Data"** to view classification groups
6. **Export results** as CSV or PDF

---
## **5️⃣ CI/CD Pipeline with GitHub Actions**

This project includes a **CI/CD pipeline** using GitHub Actions.
### **Pipeline Steps:**
1. **Runs Tests** on every push to `main`
2. **Deploys to the server** after successful tests

### **Setting Up GitHub Secrets**
Go to **GitHub Repository** → **Settings** → **Secrets and Variables** → **Actions** → **New Repository Secret**

Add the following secrets:
- `SSH_PRIVATE_KEY` → Your **private SSH key** for deployment
- `SERVER_IP` → Your **server’s IP address**
- `SERVER_USER` → Your **server’s username**

### **Trigger Deployment**
Push your code to GitHub:
```bash
   git add .
   git commit -m "New feature added"
   git push origin main
```
This will:
1. Run tests automatically
2. Deploy the app if tests pass

---
## **6️⃣ Deploying the FastAPI App to a Server**

### **Step 1: SSH into Your Server**
```bash
   ssh user@your-server-ip
```

### **Step 2: Clone the Repository on the Server**
```bash
   git clone https://github.com/YOUR_USERNAME/medical-device-recommender.git
   cd medical-device-recommender
```

### **Step 3: Set Up Virtual Environment**
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```

### **Step 4: Run the FastAPI Server**
```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 &
```
✅ Your API is now live on your server!

---
## **7️⃣ Running FastAPI in the Background (Optional)**
If you want the API to run **even after you close SSH**, use `pm2`:
```bash
   pip install pm2
   pm2 start "uvicorn app.main:app --host 0.0.0.0 --port 8000" --name fastapi
   pm2 save
```
✅ Now, your API **auto-restarts** if the server reboots!

---
## **🌟 Summary**
✅ Clone Repo → Install Dependencies → Run FastAPI 🚀

✅ Fetch Data → Use Web UI → Export Reports 📊

✅ Run Tests → Deploy Automatically with GitHub Actions 🔄

✅ Deploy to Server → Keep Running in Background 💡

---

## 💡 Contribution & Support
- Found a bug? **Open an issue** on GitHub!
- Want to contribute? **Fork & submit a PR** ✨

📌 **Made with ❤️ using FastAPI & openFDA API**