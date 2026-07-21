# MY FINAL PROJECT: ⚽ Fantasy Arena

Fantasy Arena is a Flask-based football prediction web application that allows users to register, create prediction rooms, submit football score predictions before the prediction deadline, compete with other players, and earn points based on prediction accuracy.

The project introduces a complete football prediction management system with automatic point calculation, room management, secure user authentication, a global leaderboard, and JavaScript localStorage integration for persistent client-side state.

---
# 🏆 Scoring System

| Prediction | Points |
|------------|-------:|
| Correct winner and exact score | 5 |
| Correct winner, wrong score | 2 |
| Correct draw and exact score | 3 |
| Draw predicted, wrong score | 1 |
| Incorrect prediction | 0 |

---

# 🚀 Key Features

### 🔐 User Authentication
- Secure user registration and login
- Session-based authentication
- Username validation
- Password validation
- Flash message feedback

### ⚽ Football Prediction System
- Create football prediction rooms
- Edit and delete owned rooms
- Submit predictions before the deadline
- Update predictions until the deadline closes
- Automatic prediction lock after kickoff

### 🏆 Scoring & Leaderboard
- Automatic point calculation
- Global leaderboard
- Winner and draw prediction scoring
- Total points tracking

### 💾 Data Persistence
- JSON-based storage
- Automatic file initialization
- Reading and writing to the same JSON files

### 🎨 User Experience
- Responsive Bootstrap 5 interface
- Search rooms
- Sort rooms
- Navbar animations
- JavaScript localStorage support

---

# 🛠️ Tech Stack

- Python 3
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JavaScript (ES6)
- Font Awesome

---

# 📁 Project Structure

```text
Fantasy-Arena/
├── app.py
├── config.py
├── requirements.txt
│
├── blueprints/
│   ├── auth/
│   ├── dashboard/
│   ├── predictions/
│   ├── profile/
│   └── rooms/
│
├── models/
│   ├── room.py
│   ├── prediction.py
│   └── user.py
│
├── services/
├── utils/
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── data/
│   ├── users.json
│   ├── rooms.json
│   └── predictions.json
│
└── README.md
```

---

# 📋 Project Checklist

- [✅] The project is available on GitHub.
- [✅] Uses the Flask web framework (`app.py`).
- [✅] Uses Python Standard Library modules:
  - `json`
  - `os`
  - `pathlib`
  - `uuid`
  - `datetime`
  - `tempfile`
- [✅] Contains custom classes with properties and methods.
  - File: `models/room.py`
  - Properties:
    - `room_name`
    - `match_datetime`
  - Methods:
    - `to_dict()`
    - `prediction_closed()`
- [✅] Uses JavaScript and browser `localStorage`.
  - File: `static/js/main.js` (Line 52)
- [✅] Uses modern JavaScript (`const`, `let`).
  - File: `static/js/main.js` (Line 2) (Line 18)
- [✅] Reads and writes to the same JSON files.
- [✅] Contains conditional statements.
- [✅] Contains loops.
- [✅] Accepts user input through forms.
- [✅] Handles invalid input safely using validation and Flask flash messages.
- [✅] Uses custom CSS.
- [✅] Organized using Flask Blueprints, Services, Models, and Utility modules.
- [✅] All required exercises have been completed and pushed to GitHub.

---

# 📡 Application Routes

## 🔐 Authentication

| Route | Method | Description |
|--------|--------|-------------|
| `/login` | GET, POST | User login |
| `/register` | GET, POST | User registration |
| `/logout` | GET | Logout current user |

### 🏠 Dashboard

| Route | Method | Description |
|--------|--------|-------------|
| `/` | GET | Landing page |
| `/dashboard` | GET | User dashboard |
| `/leaderboard` | GET | Global leaderboard |

### ⚽ Rooms

| Route | Method | Description |
|--------|--------|-------------|
| `/rooms` | GET | List all rooms |
| `/rooms/create` | GET, POST | Create room |
| `/rooms/<room_code>` | GET | Room details |
| `/rooms/<room_code>/edit` | GET, POST | Edit room |
| `/rooms/<room_code>/delete` | POST | Delete room |

### 📝 Predictions

| Route | Method | Description |
|--------|--------|-------------|
| `/predictions/<room_code>` | POST | Submit or update prediction |
| `/predictions/result/<room_code>` | POST | Submit match result |

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/adelberhan/Fantasy-Arena.git
cd Fantasy-Arena
```

### Create a virtual environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧑‍💻 Running the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# ⚙️ Configuration

The application uses the default Flask configuration defined in `config.py`.

Project data is automatically initialized inside the `data/` directory during the first application startup.

---
