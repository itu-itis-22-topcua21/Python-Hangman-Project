import os
import operator

score_file = "scores.txt"

def write_score(player_name, score):
    if not os.path.exists(score_file):
        with open(score_file, 'w'): pass
    with open(score_file, 'a') as file:
        file.write(f"{player_name},{score}\n")

def get_top_10_scores():
    scores = {}
    if not os.path.exists(score_file):
        return scores
    with open(score_file, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            scores[name] = int(score)
    return dict(sorted(scores.items(), key=operator.itemgetter(1), reverse=True)[:10])
