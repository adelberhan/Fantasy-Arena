class Prediction:
    """Prediction model."""

    def __init__(
        self,
        id,
        room_id,
        user_id,
        home_prediction,
        away_prediction,
        earned_points,
    ):
        self.id = id
        self.room_id = room_id
        self.user_id = user_id
        self.home_prediction = home_prediction
        self.away_prediction = away_prediction
        self.earned_points = earned_points

    def to_dict(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "user_id": self.user_id,
            "home_prediction": self.home_prediction,
            "away_prediction": self.away_prediction,
            "earned_points": self.earned_points,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)