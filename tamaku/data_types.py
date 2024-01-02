import enum


class WinnerType(str, enum.Enum):
    """
    Represents name of a player
    """
    MAT = "MAT"
    PAT = "PAT"

    def __str__(self):
        return str(self.value)
