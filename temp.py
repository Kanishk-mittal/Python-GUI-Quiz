import json
from datetime import datetime

# Original dictionary
answers = {
    11: 'Water',
    12: 'Water',
    13: 'Au',
    14: 'Au',
    15: 'Au',
    16: 'Au',
    17: 'O',
    18: 'N',
    19: 'C',
    20: 'He'
}

# Convert dictionary to JSON string
answers_json = json.dumps(answers)

# Prepare SQL query
query = f"""
INSERT INTO attempts (id, student_roll_no, quiz_id, answers, marks_obtained, time_stamp) 
VALUES (
    '8',
    '2023BCY0001', 
    '2', 
    '{answers_json}', 
    0, 
    '{datetime.now()}'
)
"""

print(query)
