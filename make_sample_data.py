"""Generates a small SYNTHETIC labeled dataset (data/emails.csv) so the project runs offline.
For your final submission, replace it with a real dataset (e.g. UCI/Kaggle spam.csv)
and run:  python spam_classifier.py train --data data/spam.csv
"""
import csv
import os
import random

random.seed(7)

spam_parts = {
    "open": ["Congratulations!", "URGENT:", "Dear winner,", "Limited offer!", "Act now!", "FREE gift inside.", "Hello friend,", "Final notice:"],
    "body": [
        "You have won a ${amt} gift card. Click http://claim-{x}.biz to claim your prize now",
        "Your account has been suspended. Verify your password immediately at http://secure-{x}.com",
        "Buy cheap meds online with no prescription, 80% discount today only",
        "Make ${amt} per week working from home, no experience needed, sign up free",
        "You are selected for a lottery payout of ${amt}. Send your bank details to receive funds",
        "Get a pre-approved loan of ${amt} with zero credit check, apply now",
        "Hot singles in your area are waiting to chat, click here",
        "Increase your followers fast, 10000 followers for just $5, order now",
        "Your parcel could not be delivered, pay the customs fee of $2 at http://track-{x}.info",
        "Exclusive crypto investment, double your bitcoin in 24 hours, guaranteed returns",
        "Claim your free iPhone now, only a few left, hurry, offer expires tonight",
        "Unsubscribe not possible. Lowest price on watches, replica brands, buy 2 get 1 free",
    ],
    "close": ["Reply STOP to opt out.", "Don't miss out!!!", "Click the link now.", "Offer ends today!", "100% guaranteed.", "Call {ph} now!", ""],
}

ham_parts = {
    "open": ["Hi,", "Hello team,", "Hey,", "Good morning,", "Hi all,", "Dear professor,", "Hi Priya,", "Hey Arun,"],
    "body": [
        "are we still meeting for the {sub} project discussion at {t} tomorrow",
        "please find attached the notes from today's {sub} lecture",
        "can you send me the assignment deadline for {sub}, I could not find it on the portal",
        "the lab session is rescheduled to {t} on Friday, please bring your record book",
        "thanks for helping me with the code yesterday, it finally compiled",
        "reminder that the {sub} internal exam starts next Monday, syllabus is on the notice board",
        "I will be late to the meeting, the bus got delayed, please start without me",
        "here is the draft of our report, let me know your feedback before we submit",
        "are you free for lunch today, we can discuss the hackathon plan",
        "your library book is due on Thursday, please return or renew it",
        "I have pushed the latest changes to the repository, please review the pull request",
        "happy birthday! hope you have a great day and see you at the party in the evening",
    ],
    "close": ["Thanks.", "Regards, Karthik", "See you then.", "Let me know.", "Best,", "Thank you!", ""],
}

subs = ["machine learning", "DBMS", "operating systems", "maths", "networks", "AI"]
times = ["10 am", "2 pm", "4:30 pm", "9 am"]


def fill(s):
    return (s.replace("{amt}", str(random.choice([500, 1000, 5000, 10000, 50000])))
             .replace("{x}", random.choice(["offer", "bonus", "login", "reward", "pay"]))
             .replace("{ph}", "0" + str(random.randint(7000000000, 9999999999)))
             .replace("{sub}", random.choice(subs))
             .replace("{t}", random.choice(times)))


def make(parts):
    return fill(" ".join(p for p in (random.choice(parts["open"]), random.choice(parts["body"]), random.choice(parts["close"])) if p))


rows = [("spam", make(spam_parts)) for _ in range(300)] + [("ham", make(ham_parts)) for _ in range(500)]
random.shuffle(rows)
os.makedirs("data", exist_ok=True)
with open("data/emails.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["label", "text"])
    w.writerows(rows)
print(f"Wrote data/emails.csv with {len(rows)} rows")
