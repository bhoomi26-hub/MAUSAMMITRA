# 🌤️ MAUSAM MITRA (मौसम मित्र)
### Personalized Weather Intelligence & Decision-Support System

MAUSAM MITRA is a smart, personalized weather intelligence platform designed for the Smart India Hackathon (SIH). Unlike generic weather apps that only display temperature and rain probability, **MAUSAM MITRA** analyzes weather conditions against specific user activities (e.g., farming, commuting, outdoor sports, travel) to provide hyper-local risk assessment and actionable recommendations.

---

## 🏗️ Technology Stack

- **Frontend**: HTML5, Vanilla CSS3 (Custom Glassmorphism Design System), Vanilla JavaScript (ES6 Modules)
- **Backend**: Python 3.10+, Flask, Flask-CORS, Requests
- **Weather API**: OpenWeatherMap / WeatherAPI (Integrated via Flask backend proxy)
- **Location**: Browser Geolocation API & Nominatim / Weather API Search
- **Maps**: Leaflet.js + OpenStreetMap (Ready for overlay integration)
- **Architecture**: Modular REST API design (Database & ML integration ready)

---

## 📁 Project Structure

```text
mausam-mitra/
│
├── frontend/
│   ├── index.html              # Main UI dashboard
│   ├── css/
│   │   └── style.css           # Weather-themed modern glassmorphism styles
│   ├── js/
│   │   ├── app.js              # Application entry point & Health check
│   │   ├── weather.js          # Weather data fetching & rendering UI
│   │   ├── location.js         # Geolocation & city search handlers
│   │   ├── recommendations.js  # Actionable advice UI logic
│   │   └── alerts.js           # Severe weather notifications
│   └── assets/                 # Icons and static images
│
├── backend/
│   ├── app.py                  # Flask main entry & server config
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables (API keys)
│   ├── .gitignore              # Backend ignored files
│   ├── routes/
│   │   ├── weather.py          # Weather API endpoints
│   │   ├── location.py         # Location search endpoints
│   │   └── recommendations.py  # Risk engine & advisory endpoints
│   ├── services/
│   │   ├── weather_service.py  # Third-party weather API integration
│   │   ├── risk_engine.py      # Weather risk calculation rules
│   │   └── recommendation_engine.py # Decision support engine
│   └── utils/
│       └── helpers.py          # Formatter & helper functions
│
└── README.md                   # Project documentation
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. Verify by running:
```bash
python --version
```

### 2. Set Up Python Virtual Environment (Backend)

Navigate to the `backend` directory:
```bash
cd backend
```

Create a virtual environment named `venv`:
- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Backend Dependencies

With the virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```

### 4. Start the Flask Backend Server

Run the main application:
```bash
python app.py
```
The server will launch at `http://127.0.0.1:5000/`. You can test the health endpoint at:
[http://127.0.0.1:5000/api/health](http://127.0.0.1:5000/api/health)

### 5. Launch the Frontend

Open `frontend/index.html` in your browser:
- You can double-click `frontend/index.html` to open it in your web browser.
- Alternatively, use Live Server extension in VS Code.

When opened, the dashboard will automatically test connection to the Flask backend and display the real-time API status badge!

---

## 🔌 API Endpoints (Phase 1)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/api/health` | Backend status check endpoint |

---

## 🛡️ License
Built with ❤️ for SIH (Smart India Hackathon).
