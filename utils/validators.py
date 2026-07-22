def validate_username(username):
    """Validate username."""

    username = username.strip()

    if len(username) < 2:
        return False, "Username must be at least 3 characters."

    return True, ""


def validate_password(password):
    """Validate password."""

    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    return True, ""

def validate_room_name(room_name):
    """Validate room name."""

    if len(room_name.strip()) < 3:
        return False, "Room name is too short."

    return True, ""

def validate_team_name(team):
    """Validate team name."""

    if len(team.strip()) < 2:
        return False, "Team name is too short."

    return True, ""
