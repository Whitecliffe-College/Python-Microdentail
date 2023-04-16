"""
Test data students can use as a tip and also check their solutions

    book = WeightedGradebook()
    book.add_student('Albert Einstein')
    book.report_grade('Albert Einstein', 'Math', 75, 0.05)
    book.report_grade('Albert Einstein', 'Math', 65, 0.15)
    book.report_grade('Albert Einstein', 'Math', 70, 0.80)
    book.report_grade('Albert Einstein', 'Gym', 100, 0.40)
    book.report_grade('Albert Einstein', 'Gym', 85, 0.60)
    print(book.average_grade('Albert Einstein'))
"""

# One way to implement this feature is to change the innermost dictionary; 
# instead of mapping subjects (its keys) to a list of grades (its values), 
# we can use the tuple of (score, weight) in the values list

from collections import defaultdict

class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            # We can use the tuple unpacking to get the score and weight
            subject_avg, total_weight = 0, 0
            
            # from the tuple
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            
            score_sum += subject_avg / total_weight
            score_count += 1
        
        return score_sum / score_count