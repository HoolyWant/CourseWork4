from abc import ABC


class JobSearchAPI(ABC):
    def __init__(self, specialty: str):
        self.specialty = specialty
