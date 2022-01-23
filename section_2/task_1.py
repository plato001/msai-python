age_spans = [
    {'age': '< 5', 'percent': 1.09}, {'age': '5 - 10', 'percent': 14.08},
    {'age': '11 - 17', 'percent': 53.06}, {'age': '18 - 24', 'percent': 24.1},
    {'age': '25 - 34', 'percent': 5.04}, {'age': '35 - 44', 'percent': 1.58},
    {'age': '45 - 54', 'percent': 0.65}, {'age': '55 - 64', 'percent': 0.29},
    {'age': '64 <', 'percent': 0.1}
]

sources = [
    {'source': 'Other online resources (videos, blogs, etc)', 'percent': 59.53},
    {'source': 'School', 'percent': 53.59},
    {'source': 'Books / Physical media', 'percent': 51.53},
    {'source': 'Online Courses or Certification', 'percent': 40.39},
    {'source': 'Online Forum', 'percent': 31.62},
    {'source': 'Friend or family member', 'percent': 18.28},
    {'source': 'Colleague', 'percent': 17.15},
    {'source': 'Coding Bootcamp', 'percent': 10.24},
]


if __name__ == '__main__':
    print("Most popular sources of information on programming:")
    print([el["source"] for el in sources if el["percent"] > 50])
