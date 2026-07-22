# ⚽ Fantasy Arena

Fantasy Arena is a Flask-based football prediction web application where users can create prediction rooms, submit score predictions before the deadline, compete with other players, and earn points based on prediction accuracy. The application includes a global leaderboard, room management, authentication, and automatic point calculation.

### New Features
- Global leaderboard that ranks players by their total earned points.
- Prediction deadline system that automatically opens and closes predictions.
- Room owner management (edit/delete rooms).
- Automatic point calculation after match results are submitted.
- Responsive modern UI built with Bootstrap 5 and Font Awesome.
- JavaScript localStorage support for client-side preferences.

---

# 🚀 Features

- User Registration & Login
- Create, Edit, and Delete Rooms
- Submit Football Predictions
- Update Predictions Before Deadline
- Automatic Prediction Lock After Deadline
- Match Result Submission
- Automatic Point Calculation
- Global Leaderboard
- Responsive Bootstrap Design
- Search and Sort Rooms
- Secure Authentication
- JSON File Storage

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

```
football_prediction/
│
├── app.py
├── config.py
├── requirements.txt
│
├── blueprints/
├── services/
├── models/
├── utils/
├── templates/
├── static/
├── data/
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/adelberhan/Fantasy-Arena.git
```

Move into the project

```bash
cd football_prediction
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📦 Prerequisites

Install the required packages:

```bash
pip install -r requirements.txt
```

Main packages:

- Flask
- Werkzeug

---

# 📋 Project Checklist

* **It is available on GitHub and you regularly committed the changes using git.**
  >> GitHub Repository: [adelberhan/Fantasy-Arena](https://github.com/adelberhan/Fantasy-Arena.git)
  >> Git Commit History: Initialized and regularly committed changes across the development lifecycle.

* **It uses the Flask web framework.**
  >> File: [app.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/app.py)
  >> Line numbers: Line 20 (`app = Flask(__name__)`), Line 22 (`app.config.from_object(Config)`), Line 27 (`register_blueprints(app)`), Lines 40-41 (`if __name__ == "__main__": app.run(debug=True)`)

* **It uses at least one module from the Python Standard Library other than the random module (for example, you could use the datetime module.)**
  >> File: [models/room.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/models/room.py)
  >> Line numbers: Line 1 (`from datetime import datetime, timedelta`), Line 65 (`datetime.fromisoformat(match_datetime)`), Line 67 (`match - timedelta(minutes=5)`), Line 74 (`datetime.fromisoformat(self.deadline)`), Line 78 (`datetime.now() >= deadline`), Line 83 (`datetime.fromisoformat(self.match_datetime)`), Line 87 (`datetime.now() >= match_time`)
  >> File: [utils/json_storage.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/utils/json_storage.py)
  >> Line numbers: Line 1 (`import json`), Line 2 (`import os`), Line 3 (`from pathlib import Path`), Line 4 (`from tempfile import NamedTemporaryFile`)

* **It contains at least one class written by you that has both properties and methods (yes, plural!). It uses `__init__()` to let the class initialize the object's properties (note that `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app. Methods that only print something in the terminal will not be considered.**
  >> File: [models/room.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/models/room.py) (Class declaration and definition)
  >> Line numbers: Line 4 (`class Room:`), Lines 7-37 (`__init__()` constructor initializing properties like `room_name` and `match_datetime`), Lines 89-91 (`@property def match_datetime_obj(self):` property)
  >> Line numbers: Lines 39-55 (`to_dict()` method returning a dictionary representation), Lines 71-79 (`prediction_closed()` method to verify deadline), Lines 80-87 (`match_ended()` method to verify match time)
  >> File: [services/room_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/room_service.py) (Class instantiation and method calls)
  >> Line numbers: Lines 116-131 (`room = Room(...)` instantiation), Line 133 (`room.to_dict()` method call)
  >> File: [services/prediction_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/prediction_service.py) (Method call usage)
  >> Line numbers: Line 23 (`room.prediction_closed()` method call)

* **It makes use of JavaScript in the front end and uses the localStorage of the web browser.**
  >> File: [static/js/main.js](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/static/js/main.js)
  >> Line numbers: Line 36 (`let username = localStorage.getItem("username")`), Line 42 (`localStorage.setItem("username", username)`), Line 53 (`localStorage.removeItem("username")`)

* **It uses modern JavaScript (for example, let and const rather than var).**
  >> File: [static/js/main.js](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/static/js/main.js)
  >> Line numbers: Line 6 (`let isAscending = true`), Line 36 (`let username = localStorage.getItem("username")`), Line 2 (`const sortBtn = document.getElementById(...)`), Line 3 (`const container = document.getElementById(...)`), Line 33 (`const usernameElement = document.getElementById(...)`), Line 50 (`const logoutButton = document.getElementById(...)`)

* **It makes use of the writing to and reading from the same file feature.**
  >> File: [utils/json_storage.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/utils/json_storage.py)
  >> Line numbers: Lines 28-40 (`load_json` reads from a JSON file path), Lines 43-72 (`save_json` writes atomically to the same JSON file path)
  >> File: [services/room_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/room_service.py) (Reading and writing to rooms.json)
  >> Line numbers: Line 114 (`load_json` read call), Line 135 (`save_json` write call to the same `rooms.json` file path)
  >> File: [services/prediction_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/prediction_service.py) (Reading and writing to predictions.json)
  >> Line numbers: Line 63 (`load_json` read call), Line 72 (`save_json` write call to the same `predictions.json` file path)

* **It contains both conditional statements and loops.**
  >> File: [services/prediction_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/prediction_service.py)
  >> Line numbers: Lines 119-150 (`if`/`elif`/`else` conditional branches inside `calculate_points`), Lines 163-178 (`for prediction in predictions:` loop inside `update_predictions_points`), Lines 264-276 (`for pred in predictions:` loop and `for u in users:` loop inside `get_global_leaderboard`)

* **It doesn't generate any error message even if the user enters a wrong input.**
  >> File: [services/room_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/room_service.py) (Validating form and capturing errors)
  >> Line numbers: Lines 59-100 (`validate_room_form` intercepts invalid inputs and returns validation messages gracefully)
  >> File: [blueprints/rooms/routes.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/blueprints/rooms/routes.py) (Displaying validation failure status to the user)
  >> Line numbers: Line 50 (`flash(message, "danger")`), Line 164 (`flash(message, "danger")`)
  >> File: [templates/components/flash_messages.html](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/templates/components/flash_messages.html) (Client-side display)
  >> Line numbers: Lines 1-5 (User interface rendering the flashed messages directly in the web browser instead of crashing or printing standard server stacktraces)

* **It lets the user enter a value in a text box at some point. This value should be received and processed by your back end Python code.**
  >> File: [templates/rooms/create.html](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/templates/rooms/create.html)
  >> Line numbers: Line 17 (`<input type="text" name="room_name">` room name text box), Line 24 (`home_team` text box), Line 30 (`away_team` text box)
  >> File: [blueprints/rooms/routes.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/blueprints/rooms/routes.py)
  >> Line numbers: Line 46 (`request.form` extracts the user values to pass to room builder logic)

* **It is styled using CSS.**
  >> File: [static/css/style.css](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/static/css/style.css)
  >> Line numbers: Lines 1-163 (Core styles, grid system, cards, hover animations, buttons styling)
  >> File: [static/css/landing.css](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/static/css/landing.css)
  >> Line numbers: Lines 1-76 (Landing page visual styling)
  >> File: [static/css/navbar.css](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/static/css/navbar.css)
  >> Line numbers: Lines 1-27 (Modern clean glassmorphism responsive navbar styling)

* **The code follows the code and style conventions we introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.**
  >> File: [app.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/app.py)
  >> Line numbers: Lines 1-42 (Uses Flask application factories, error handlers, and modular Blueprint registrations, no debug prints)
  >> File: [services/room_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/room_service.py)
  >> Line numbers: Lines 1-345 (Fully documented helpers using docstrings and explanatory comments, no unused code, no print statement)
  >> File: [templates/components/flash_messages.html](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/templates/components/flash_messages.html)
  >> Line numbers: Lines 1-5 (User feedback is shown in browser alert blocks rather than using standard print or console logs)

---

# 📸 Screenshots

| Landing Page | Dashboard |
| :---: | :---: |
| ![Landing Page](static/images/Camp-Nou-4.webp) | ![Dashboard](static/images/logo.png) |

| Room Details & Predictions | Global Leaderboard |
| :---: | :---: |
| ![Room Details](static/images/Fantasy%20Arena.png) | ![Leaderboard](static/images/logo.png) |

---

# 🚀 Future Improvements

- 📧 **Email Notifications**: Notify users when match predictions open or deadlines approach.
- ⚽ **Match API Integration**: Auto-sync live scores and match schedules via external Football APIs.
- 🛡️ **Admin Dashboard**: Comprehensive management interface for admins to create and settle official matches.
- 👤 **User Profiles & Avatars**: Profile customization, avatar upload, and user statistics.
- 📊 **Advanced Statistics**: Performance analytics, prediction accuracy graphs, and head-to-head records.
- 🌙 **Dark Mode**: Seamless toggle between Light and Dark themes saved to `localStorage`.
- 📑 **Pagination**: Server-side pagination for rooms and global leaderboards to scale with user growth.

---

# 📸 Application Pages

- Landing Page
- Dashboard
- Rooms
- Room Details
- Create Room
- Edit Room
- Leaderboard
- Login
- Register

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

# 👨‍💻 Author

**Adel Ahmed**

Fantasy Arena – Football Prediction Challenge
