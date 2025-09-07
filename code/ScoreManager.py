import json
import os


class ScoreManager:
    def __init__(self):
        self.scores_file = 'scores.json'
        self.scores = []
        self.load_scores()

    def load_scores(self):
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r') as file:
                    self.scores = json.load(file)
            except:
                self.scores = []
        else:
            self.scores = []

    def save_score(self, score):
        new_entry = {
            'score': score
        }
        self.scores.append(new_entry)

        self.scores.sort(key=lambda x: x['score'], reverse=True)
        self.scores = self.scores[:10]

        with open(self.scores_file, 'w') as file:
            json.dump(self.scores, file, indent=4)

    def get_top_scores(self, limit=3):
        return self.scores[:limit]