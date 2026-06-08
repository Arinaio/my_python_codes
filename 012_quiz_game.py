"""A multiple choice quiz about Supernatural, The Walking Dead, Marvel, Hannibal and Sherlock.
Answer A/B/C/D and get scored at the end. Uses functions, lists and dictionaries"""


def get_questions():
    questions= [
            {
            "question":"In Supernatural, what are the names of the two main brothers?",
            "options":["A) John and Bobby","B) Sam and Dean","C) Cas and Gabriel","D) Sam and Adam"],
            "answer":"B"
            },
            {
            "question":"In The Walking Dead, what weapon does Negan carry?",
            "options":["A) A chainsaw","B) A knife","C) A barbed wire baseball bat","D) A sword"],
            "answer":"C"
            },
            {
            "question":"In Hannibal, what is Hannibal Lecter's profession?",
            "options":["A) Surgeon","B) Psychiatrist","C) Lawyer","D) Professor"],
            "answer":"B"
            },
            {
            "question":"In Sherlock, What is the Address of Sherlock Holmes?",
            "options":["A) 10 Downing Street","B) 221A Baker Street","C) 221B Baker Street","D) 200B Baker Street"],
            "answer":"C"
            },
            {
            "question":"In the MCU, what stone is in Thor's home Asgard?",
            "options":["A) Mind Stone","B) Space Stone","C) Reality Stone","D) Time Stone"],
            "answer":"C"
            },
            ]
    return questions


def ask_questions(question_data, number):
    print(f"\nQuestion {number}:{question_data['question']}")
    for option in question_data['options']:
        print(option)
    
    answer=input("\nYour Answer(A/B/C/D): ")
    
    if answer==question_data['answer']:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The answer was {question_data['answer']}")
        return False
    
def show_results(score,total):
    print(f"\n{'='*35}")
    print("   GAME OVER!")
    print(f"   You got {score} out of {total} correct!")
    if score==total:
        print("   Perfect score! You really know your shows!")
    elif score>=total*0.7:
        print("   Great job!")
    elif score>= total/2:
        print("   Not bad! Rewatch some episodes..")
    else:
        print("   Time for a rewatch marathon...")
    print(f"{'='*35}")
    
    
def play_game():
    questions= get_questions()
    score=0
    
    print("Welcome to the Ultimate Fan Quiz!")
    print("Supernatural | The Walking Dead | Marvel | Hannibal | Sherlock")
    print("Answer with A, B, C, D or D\n")
    
    for i, question in enumerate(questions):
        correct= ask_questions(question, i+1)
        if correct:
            score+=1
    show_results(score, len(questions))
    
play_game()


