# MY FINAL PROJECT

Fantasy Arena is a Flask-based football prediction web application where users can create prediction rooms, submit score predictions before the deadline, compete with other players, and earn points based on prediction accuracy.

The new features implemented include a global leaderboard ranking players by total points, automatic point calculation upon match result submission, and automated prediction lockouts based on match deadlines.

## Prerequisites

The required Python packages are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

Key packages include:

- `Flask`
- `Werkzeug`

## Project Checklist

- [x] It is available on GitHub.

  > > GitHub Repository: [adelberhan/Fantasy-Arena](https://github.com/adelberhan/Fantasy-Arena.git)

- [x] It uses the Flask web framework.

  > > File: [app.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/app.py)
  > > Line numbers: Line 20 (`app = Flask(__name__)`), Line 22 (`app.config.from_object(Config)`), Line 27 (`register_blueprints(app)`), Lines 40-41 (`if __name__ == "__main__": app.run(debug=True)`)

- [x] It uses at least one module from the Python Standard Library other than the random module.
      Please provide the name of the module you are using in your app.
  - Module name: `datetime`
    > > File: [models/room.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/models/room.py)
    > > Line numbers: Line 1 (`from datetime import datetime, timedelta`), Line 65 (`datetime.fromisoformat(match_datetime)`)

- [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's properties (note that `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app.
      Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name for the class definition: `models/room.py`
  - Line number(s) for the class definition: Lines 4 to 91
  - Name of two properties: `room_name`, `match_datetime`
  - Name of two methods: `to_dict()`, `prediction_closed()`
  - File name and line numbers where the methods are used:
    - `to_dict()` is used in [services/room_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/room_service.py) (Line 133)
    - `prediction_closed()` is used in [services/prediction_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/prediction_service.py) (Line 23)
      > > File: [models/room.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/models/room.py) (Lines 4-91)

- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.

  > > File: [static/js/main.js](static/js/main.js)
  > > Line numbers: Line 36 (`let username = localStorage.getItem("username")`), Line 42 (`localStorage.setItem("username", username)`), Line 53 (`localStorage.removeItem("username")`)

- [x] It uses modern JavaScript (for example, let and const rather than var).
  - File: `static/js/main.js`
  - Line 36 (`let username = localStorage.getItem("username")`),Line 33 (`const usernameElement = document.getElementById(...)`)

- [x] It makes use of the reading and writing to the same file feature.

  > > File: [utils/json_storage.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/utils/json_storage.py)
  > > Line numbers: Lines 28-40 (`load_json` reads from a JSON file path), Lines 43-72 (`save_json` writes atomically to the same JSON file path)

- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least one example of a conditional statement in your code.
  - File name: `utils/validators.py`
  - Line number(s): Lines 12 to 18
    > > File: [utils/validators.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/utils/validators.py) (Lines 12-18)

- [x] It contains loops. Please provide below the file name and the line number(s) of at least one example of a loop in your code.
  - File name: `services/dashboard_service.py`
  - Line number(s): Lines 163 to 178
    > > File: [services/prediction_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/dashboard_service.py) (Lines 13-16)

- [x] It lets the user enter a value in a text box at some point. This value is received and processed by your back end Python code.

  > > File: [templates/rooms/create.html](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/templates/rooms/create.html)
  > > Line numbers: Line 17 (`<input type="text" name="room_name">` room name text box)

  > > File: [blueprints/rooms/routes.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/blueprints/rooms/routes.py)
  > > Line numbers: Line 42 (`request.form` extracts the user values to pass to room builder logic)

- [x] It doesn't generate any error message even if the user enters a wrong input.

  > > File: [services/room_service.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/services/room_service.py) (Validating form and capturing errors)
  > > Line numbers: Lines 59-100 (`validate_room_form` intercepts invalid inputs and returns validation messages gracefully)
  > > File: [templates/components/flash_messages.html](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/templates/components/flash_messages.html) (Client-side display)
  > > Line numbers: Lines 1-5 (User interface rendering the flashed messages directly in the web browser instead of crashing or printing standard server stacktraces)

- [x] It is styled using your own CSS.

  > > File: [static/css/style.css](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/static/css/style.css)
  > > Line numbers: Lines 1-163 (Core styles)

- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.

  > > File: [app.py](file:///d:/Docements/Web_dev/RemoteCoders/Fantasy%20Arena/app.py)
  > > Line numbers: Lines 1-42 (Uses Flask application factories, error handlers, and modular Blueprint registrations, no debug prints)

- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.
  > > GitHub Repository: [adelberhan/Fantasy-Arena](https://github.com/adelberhan/Fantasy-Arena.git)
