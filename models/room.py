from datetime import datetime, timedelta


class Room:
    """Room model."""

    def __init__(
        self,
        id,
        room_name,
        room_code,
        owner_id,
        home_team,
        away_team,
        home_logo,
        away_logo,
        match_datetime,
        deadline,
        home_score,
        away_score,
        created_at,
        updated_at,
    ):
        self.id = id
        self.room_name = room_name
        self.room_code = room_code
        self.owner_id = owner_id
        self.home_team = home_team
        self.away_team = away_team
        self.home_logo = home_logo
        self.away_logo = away_logo
        self.match_datetime = match_datetime
        self.deadline = deadline
        self.home_score = home_score
        self.away_score = away_score
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "room_name": self.room_name,
            "room_code": self.room_code,
            "owner_id": self.owner_id,
            "home_team": self.home_team,
            "away_team": self.away_team,
            "home_logo": self.home_logo,
            "away_logo": self.away_logo,
            "match_datetime": self.match_datetime,
            "deadline": self.deadline,
            "home_score": self.home_score,
            "away_score": self.away_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @staticmethod
    def calculate_deadline(match_datetime):
        """Calculate prediction deadline."""

        match = datetime.fromisoformat(match_datetime)

        deadline = match - timedelta(minutes=5)

        return deadline.isoformat(timespec="minutes")

    def prediction_closed(self):
        """Return True if prediction deadline has passed."""

        deadline = datetime.fromisoformat(
            self.deadline
        )

        return datetime.now() >= deadline

    def match_ended(self):
        """Return True if the match has ended."""

        match_time = datetime.fromisoformat(
            self.match_datetime
        )

        return datetime.now() >= match_time

    @property
    def match_datetime_obj(self):
        return datetime.fromisoformat(self.match_datetime)