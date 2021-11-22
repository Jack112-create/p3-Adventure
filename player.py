import random


class Player:
    """
    Creates a player providing a
    level of confidence,
    job, and a list of skills
    """

    def __init__(self, name):
        self.name = name
        self.job = ''
        self.confidence = 100
        self.skills = []
        self.score = 0

    def show_stats(self):
        print(f"""
{self.name.upper()} THE DEVELOPER!
Here are your stats:

Name: {self.name}
----------------------
Confidence: {self.confidence}
----------------------
Skills: {self.skills}
----------------------
Job: {self.job}
----------------------
Score: {self.score}
""")

    def increase_score(self):
        self.score += 1

    def lower_score(self):
        # Stops score from going below 0.
        if self.score > 0:
            self.score -= 1

    def lower_confidence(self, new_confidence=random.randint(1, 15)):
        min_confidence = 0
        self.confidence = self.confidence - new_confidence
        # Stops confidence level from going below 0.
        if self.confidence < min_confidence:
            self.confidence = 0
        print('\nYour confidence has dropped.')
        print("Confidence Level:", self.confidence)

    def set_skills(self, new_skill):
        self.skills.append(new_skill)
