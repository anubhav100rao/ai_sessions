"""
Lakeview Institute of Business Studies (a fictional college)
-------------------------------------------------------------
The "library" our RAG assistant reads from, plus the TEST SET we
use to grade it. Think of the test set as an answer key for an exam.
"""

# Each document has a name, a status (current / archived) and its text.
DOCUMENTS = [
    {
        "id": "library_rules",
        "status": "current",
        "text": (
            "Students may borrow up to 4 books at a time for 14 days. "
            "The late fee is Rs 5 per day for each book, up to a maximum of Rs 200 per book. "
            "Reference books and journals cannot be taken out of the library. "
            "Lost books must be replaced or paid for at twice the cover price."
        ),
    },
    {
        "id": "attendance_policy_2023",
        "status": "archived",  # OLD version, replaced in 2026
        "text": (
            "Attendance policy 2023. Students must maintain minimum attendance of 75 percent in every course. "
            "Students with a medical certificate can get a medical relaxation of up to 10 percent attendance. "
            "Students below the minimum attendance cannot sit for the end-term exam."
        ),
    },
    {
        "id": "attendance_policy_2026",
        "status": "current",  # NEW version
        "text": (
            "Attendance policy, effective July 2026. This policy replaces the 2023 policy. "
            "The minimum attendance is now 80 percent in every course. "
            "Relaxation for documented illness is limited to 5 percent. "
            "Students below the minimum cannot sit for the end-term exam."
        ),
    },
    {
        "id": "exam_rules",
        "status": "current",
        "text": (
            "Results are published within 30 days of the last exam. "
            "A student who fails a course may apply for a re-exam within 7 days of results. "
            "The re-exam fee is Rs 1500 per course. "
            "Revaluation of an answer sheet costs Rs 500."
        ),
    },
    {
        "id": "fee_refund",
        "status": "current",
        "text": (
            "If a student withdraws before classes begin, the full fee is refunded minus a processing charge of Rs 1000. "
            "If a student withdraws within the first two weeks of classes, 50 percent of the tuition fee is refunded. "
            "No refund is given after the first two weeks."
        ),
    },
    {
        "id": "hostel_rules",
        "status": "current",
        "text": (
            "The hostel gate closes at 10:30 PM every night. "
            "Visitors are allowed in the common room until 7 PM. "
            "Cooking appliances are not permitted in rooms."
        ),
    },
    {
        "id": "placement_rules",
        "status": "current",
        "text": (
            "Students with no active backlogs can register for campus placements. "
            "A registered student may apply to as many companies as they like during the placement season, "
            "and may attend interviews with several companies in the same week. "
            "However, once a student accepts a job offer, they are removed from the placement process "
            "and cannot apply to any other company."
        ),
    },
    {
        "id": "clubs",
        "status": "current",
        "text": (
            "Any group of 15 students can start a new club. "
            "Every club needs a faculty advisor and must hold at least 4 events per semester."
        ),
    },
]

# THE TEST SET (answer key)
#  - question: what a student might ask
#  - must_contain: words a correct answer must include
#  - source: the document that should be found (None = answer not in documents)
TEST_SET = [
    {"question": "What is the late fee for a library book?",
     "must_contain": ["5"], "source": "library_rules"},
    {"question": "How many days can I keep a borrowed book?",
     "must_contain": ["14"], "source": "library_rules"},
    {"question": "What is the minimum attendance required in every course?",
     "must_contain": ["80"], "source": "attendance_policy_2026"},
    {"question": "How much attendance relaxation can I get with a medical certificate?",
     "must_contain": ["5 percent"], "source": "attendance_policy_2026"},
    {"question": "What is the re-exam fee?",
     "must_contain": ["1500"], "source": "exam_rules"},
    {"question": "Will I get a refund if I withdraw in the first two weeks?",
     "must_contain": ["50"], "source": "fee_refund"},
    {"question": "When does the hostel gate close?",
     "must_contain": ["10:30"], "source": "hostel_rules"},
    {"question": "Can I apply to other companies after I accept a job offer in placements?",
     "must_contain": ["cannot"], "source": "placement_rules"},
    {"question": "How many students do I need to start a club?",
     "must_contain": ["15"], "source": "clubs"},
    # Unanswerable: the documents don't say. A good assistant says "I don't know".
    {"question": "What is the canteen menu on Fridays?",
     "must_contain": [], "source": None},
    {"question": "Who is the principal of Lakeview?",
     "must_contain": [], "source": None},
]
