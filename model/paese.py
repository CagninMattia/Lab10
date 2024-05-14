from dataclasses import dataclass

@dataclass
class Paese:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return self.CCode

    def __str__(self):
        return f"{self.StateNme}"