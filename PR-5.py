# =====================================================
# SPORTS COORDINATOR - STUDENT EVENT MANAGEMENT SYSTEM
# =====================================================

# =====================================================
# 1. STORE STUDENT SCORES IN DICTIONARIES
# =====================================================
data = {}

numberOfStudents = int(input("Enter the number of students: "))

for i in range(numberOfStudents):
    name = input(f"Enter the name of student {i+1}: ")
    data[name] = {}

    numberOfEvents = int(input(f"Enter the number of events for {name}: "))
    for j in range(numberOfEvents):
        event = input(f"Enter event {j+1} name: ")
        score = int(input(f"Enter {name}'s score in {event}: "))
        data[name][event] = score

print("\n--- Initial Student Data ---")
print(data)

# =====================================================
# 2. UPDATE, DELETE, OR FILTER DATA
# =====================================================

# --- UPDATE: Modify existing student score ---
def update_score(data, student_name, event_name, new_score):
    """Update a student's score for a specific event"""
    if student_name in data:
        if event_name in data[student_name]:
            old_score = data[student_name][event_name]
            data[student_name][event_name] = new_score
            print(f"Updated {student_name}'s score in {event_name}: {old_score} -> {new_score}")
        else:
            data[student_name][event_name] = new_score
            print(f"Added new event {event_name} for {student_name} with score {new_score}")
    else:
        print(f"Student {student_name} not found!")

# --- DELETE: Remove student or event data ---
def delete_student(data, student_name):
    """Delete a student from the data"""
    if student_name in data:
        del data[student_name]
        print(f"Deleted student: {student_name}")
    else:
        print(f"Student {student_name} not found!")

def delete_event_score(data, student_name, event_name):
    """Delete a specific event score for a student"""
    if student_name in data and event_name in data[student_name]:
        del data[student_name][event_name]
        print(f"Deleted {event_name} score for {student_name}")
    else:
        print(f"Record not found!")

# --- FILTER: Filter students by criteria ---
def filter_students_by_min_score(data, min_score):
    """Filter students who have at least one score >= min_score"""
    filtered = {student: events for student, events in data.items() 
                if any(score >= min_score for score in events.values())}
    return filtered

def filter_students_by_event(data, event_name):
    """Filter students who participated in a specific event"""
    filtered = {student: events for student, events in data.items() 
                if event_name in events}
    return filtered

# Example: Update a score
print("\n--- Update Operation ---")
if data:
    first_student = list(data.keys())[0]
    if data[first_student]:
        first_event = list(data[first_student].keys())[0]
        update_score(data, first_student, first_event, 95)

print("\n--- Data After Update ---")
print(data)

# Example: Filter students with score >= 50
print("\n--- Filtered Students (score >= 50) ---")
high_scorers = filter_students_by_min_score(data, 50)
print(high_scorers)

# =====================================================
# 3. USE SETS TO TRACK PARTICIPATION IN EVENTS
# =====================================================
print("\n" + "="*50)
print("SET OPERATIONS FOR EVENT PARTICIPATION")
print("="*50)

# Extract all student names as a set
studentNames = {student for student in data.keys()}
print("\n--- All Students (Set) ---")
print(studentNames)

# Extract all event names as a set
allEvents = {event for student, events in data.items() for event in events.keys()}
print("\n--- All Events (Set) ---")
print(allEvents)

# Create a dictionary mapping each event to its set of participants
eventParticipants = {}
for event in allEvents:
    eventParticipants[event] = set()
    for student, events in data.items():
        if event in events:
            eventParticipants[event].add(student)

print("\n--- Event Participants Mapping ---")
for event, participants in eventParticipants.items():
    print(f"{event}: {participants}")

# --- SET OPERATIONS: Union, Intersection, Difference ---
print("\n--- Set Operations Between Events ---")
events_list = list(allEvents)

for i in range(len(events_list)):
    for j in range(i + 1, len(events_list)):
        event1, event2 = events_list[i], events_list[j]
        participants1 = eventParticipants[event1]
        participants2 = eventParticipants[event2]
        
        print(f"\n{event1} vs {event2}:")
        print(f"  Union (participated in either): {participants1 | participants2}")
        print(f"  Intersection (participated in both): {participants1 & participants2}")
        print(f"  Difference ({event1} only): {participants1 - participants2}")
        print(f"  Difference ({event2} only): {participants2 - participants1}")
        print(f"  Symmetric Difference (participated in exactly one): {participants1 ^ participants2}")

# =====================================================
# 4. AGGREGATE DATA CALCULATIONS
# =====================================================
print("\n" + "="*50)
print("AGGREGATE DATA ANALYSIS")
print("="*50)

# --- Average Score Per Student ---
print("\n--- Average Score Per Student ---")
studentAverages = {}
for student, events in data.items():
    if events:
        avg_score = sum(events.values()) / len(events)
        studentAverages[student] = round(avg_score, 2)
        print(f"{student}: {studentAverages[student]}")
    else:
        studentAverages[student] = 0
        print(f"{student}: No events participated")

# --- Highest and Lowest Scores Per Event ---
print("\n--- Highest and Lowest Scores Per Event ---")
eventStats = {}
for event in allEvents:
    scores = [(student, data[student][event]) for student in data if event in data[student]]
    if scores:
        highest = max(scores, key=lambda x: x[1])
        lowest = min(scores, key=lambda x: x[1])
        all_scores = [s[1] for s in scores]
        eventStats[event] = {
            'highest': highest,
            'lowest': lowest,
            'all_scores': all_scores
        }
        print(f"\n{event}:")
        print(f"  Highest: {highest[0]} with score {highest[1]}")
        print(f"  Lowest: {lowest[0]} with score {lowest[1]}")
        print(f"  All Scores: {all_scores}")

# --- Total Participants Per Event ---
print("\n--- Total Participants Per Event ---")
for event, participants in eventParticipants.items():
    print(f"{event}: {len(participants)} participant(s) - {participants}")

# =====================================================
# 5. IDENTIFY TOP-PERFORMING STUDENTS ACROSS ALL EVENTS
# =====================================================
print("\n" + "="*50)
print("TOP-PERFORMING STUDENTS")
print("="*50)

# --- Total Score Per Student ---
print("\n--- Total Score Per Student ---")
studentTotalScores = {}
for student, events in data.items():
    total = sum(events.values())
    studentTotalScores[student] = total
    print(f"{student}: {total}")

# --- Ranking by Total Score ---
print("\n--- Students Ranked by Total Score ---")
sortedByTotal = sorted(studentTotalScores.items(), key=lambda x: x[1], reverse=True)
for rank, (student, total) in enumerate(sortedByTotal, 1):
    print(f"Rank {rank}: {student} with total score {total}")

# --- Ranking by Average Score ---
print("\n--- Students Ranked by Average Score ---")
sortedByAverage = sorted(studentAverages.items(), key=lambda x: x[1], reverse=True)
for rank, (student, avg) in enumerate(sortedByAverage, 1):
    print(f"Rank {rank}: {student} with average score {avg}")

# --- Top Performer in Each Event ---
print("\n--- Top Performer in Each Event ---")
for event, stats in eventStats.items():
    print(f"{event}: {stats['highest'][0]} (Score: {stats['highest'][1]})")

# --- Students with Multiple Event Participation ---
print("\n--- Multi-Event Participants ---")
for student, events in data.items():
    event_count = len(events)
    if event_count > 1:
        print(f"{student}: Participated in {event_count} events - {list(events.keys())}")

# --- Overall Summary ---
print("\n" + "="*50)
print("OVERALL SUMMARY")
print("="*50)

if sortedByTotal:
    print(f"\nOverall Top Performer (by Total Score): {sortedByTotal[0][0]} with {sortedByTotal[0][1]} points")
if sortedByAverage:
    print(f"Best Average Score: {sortedByAverage[0][0]} with {sortedByAverage[0][1]} average")
print(f"Total Events Conducted: {len(allEvents)}")
print(f"Total Students: {len(data)}")
print(f"Total Participations: {sum(len(events) for events in data.values())}")
