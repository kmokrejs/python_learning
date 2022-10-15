from typing import Type
from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, min_, max_, professor):
        self.name = name
        self.code = code
        self.min = min_
        self.max = max_
        self.professors = []
        self.enrollments  = []

        if isinstance(professor,Professor):
                self.professors.append(professor)
        elif isinstance(professor,list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise TypeError("Invalid professor..",)

            self.professors = professor
        else: 
            raise TypeError("Invalid professor...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError("Invalid professor...")
        
        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError("Invalid enrollment...")

        if len(self.enrollments) >= self.max:
            raise TypeError("Cannot enroll, maximum capacity has been reached.")

        self.enrollments.append(enroll)

    def is_canceled(self):
        return len(self.enrollments) < self.min