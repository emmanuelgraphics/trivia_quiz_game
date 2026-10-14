import random
import os
import csv

categories = ["Old Testament", "New Testament", "Bible Characters", "Books & Verses"]

questions = {
    #================Old Testament===================
    "Old Testament": [
        {   
            "question": "Who built the ark?",
            "choices": {"a": "Moses", "b": "Noah", "c": "Abraham", "d": "David"},
            "answer": "b",
        },
        {
            "question": "What is the first book of the Bible?",
            "choices": {"a": "Genesis", "b": "Exodus", "c": "Psalms", "d": "Matthew"},
            "answer": "a",
        },
        {        
            "question": "Who was swallowed by a great fish?",
            "choices": {"a": "Joel", "b": "Noah", "c": "Daniel", "d": "Jonah"},
            "answer": "d",
        },
        {
            "question": "Who interpreted Pharaoh's dreams in Egypt?",
            "choices": {"a": "Moses", "b": "Aaron", "c": "Daniel", "d": "Joseph"},
            "answer": "d",
        },
        {
            "question": "Who led the Israelites out of Egypt?",
            "choices": {"a": "Moses", "b": "Joshua", "c": "Caleb", "d": "Aaron"},
            "answer": "a",
        },
        {
            "question": "How many plagues did God send on Egypt?",
            "choices": {"a": "7", "b": "12", "c": "10", "d": "5"},
            "answer": "c",
        },
        {
            "question": "Who killed the giant Goliath?",
            "choices": {"a":"Saul", "b":"David", "c": "Jonathan", "d": "Aaron" },
            "answer": "b",
        },
        {
            "question": "Whose strength was tied to his uncut hair?",
            "choices": {"a": "Nebbuchadenezzar", "b": "Gideon", "c": "Samson", "d": "Jacob"},
            "answer": "c",
        },
        {
            "question": "Who was thrown into the lion's den for praying?",
            "choices": {"a": "Daniel", "b": "Elijah", "c": "Jeremiah", "d": "Isaiah"},
            "answer": "a",
        },
        {
            "question": "Which woman became queen and saved her people from Haman?",
            "choices": {"a": "Ruth", "b": "Esther", "c": "Deborah", "d": "Hannah"},
            "answer": "b",
        },
        {
            "question": "Which son of Abraham was he asked to offer as a sacrifice?",
            "choices": {"a": "Ishmael", "b": "Jacob", "c": "Isaac", "d": "Esau"},
            "answer": "c", 
        },
        {
            "question": "Which prophet was taken up to God in a whirlwind?",
            "choices": {"a": "Elisha", "b": "Elijah", "c": "Isaiah", "d": "Ezekiel"},
            "answer": "b",
        },
        {
            "question": "Which King asked God for wisdom and built the temple?",
            "choices": {"a": "Solomon", "b": "David", "c": "Saul", "d": "Hezekiah"},
            "answer": "a",
        },
        {
            "question": "Which woman became queen and saved her people from Haman?",
            "choices": {"a": "Ruth", "b": "Esther", "c": "Deborah", "d": "Hannah"},
            "answer": "b",
        },
        {
            "question": "Whose walls fell after the Israelites marched around the city?",
            "choices": {"a": "Babylon", "b": "Nineveh", "c": "Ai", "d": "Jericho"},
            "answer": "d",
        },
    ],

#================New Testament===================
    "New Testament": [
        {    
            "question": "In which town was Jesus born?",
            "choices": {"a": "Nazareth", "b": "Jerusalem", "c": "Bethlemen", "d": "Capernum"},
            "answer": "c",
        },
        {
            "question": "How many disciples did Jesus choose?",
            "choices": {"a": "12", "b": "10", "c": "7", "d": "70"},
            "answer": "a",
        },
        {
            "question": "Who baptized Jesus in the Jordan river?",
            "choices": {"a": "Peter", "b": "Andrew", "c": "Philip", "d": "John"},
            "answer": "d",
        },
        {
        
            "question": "Which disciple betrayed Jesus?",
            "choices": {"a": "Matthew", "b": "Peter", "c": "Judas", "d": "Matthais"},
            "answer": "c",
        },
        {
            "question": "What was Jesus first recorded miracle, at Cana?",
            "choices": {"a": "Turning water into wine", "b": "Walking on water", "c": "Healing a blind man", "d": "Feeding 5,000"},
            "answer": "a",
        },
        {
            "question": "Which Gospel is the shortest?",
            "choices": {"a": "Matthew", "b": "Mark", "c": "Luke", "d": "John"},
            "answer": "b",
        },
        {
            "question": "What is the last book of the bible?",
            "choices": {"a":"Malachi", "b":"Jude", "c": "Revelation", "d": "Genesis" },
            "answer": "c",
        },
        {
            "question": "What came on the disciples on the day of pentecost?",
            "choices": {"a": "An earthquake", "b": "Manna", "c": "A Great flood", "d": "The Holy Spirit"},
            "answer": "d",
        },
        {
            "question": "Who was the first Christian martyr, stoned to death?",
            "choices": {"a": "Stephen", "b": "Achan", "c": "Paul", "d": "Barnabas"},
            "answer": "a",
        },
        {
            "question": "Which tax collector climed a sycamore tree to see Jesus?",
            "choices": {"a": "Zacchaeus", "b": "Matthew", "c": "Nicodemus", "d": "Bartimaeus"},
            "answer": "a",
        },
        {
            "question": "Which disciple doubted the resurrection until he saw Jesus' wounds?",
            "choices": {"a": "Peter", "b": "Judas", "c": "Thomas", "d": "Philip"},
            "answer": "c",
        },
        {
            "question": "Who did Jesus raise from the dead after four days in the tomb?",
            "choices": {"a": "Jairus daughter", "b": "The widow's son", "c": "Lazarus", "d": "Dorcas"},
            "answer": "c",
        },
        {
            "question": "Which Roman gevernor sentenced Jesus to be crucified?",
            "choices": {"a": "Herod", "b": "Caesar", "c": "Pontius pilate", "d": "Felix"},
            "answer": "c",
        },
        {
            "question": "Saul met Jesus on the road to damascus. What was he later called?",
            "choices": {"a": "Barnabas", "b": "Silas", "c": "Timothy", "d": "Paul"},
            "answer": "d",
        },
        {
            "question": "Which of the disciples was a tax collector?",
            "choices": {"a": "Matthew", "b": "Philip", "c": "John", "d": "Judas Iscariot"},
            "answer": "c",
        },
    ],      
    
#================Bible Characters===================
    "Bible Characters": [
        {
            "question": "Who was the first man created by God?",
            "choices": {"a": "Seth", "b": "Adam", "c": "Cain", "d": "Noah"},
            "answer": "b",
        },
        {
            "question": "Who was Adam's wife?",
            "choices": {"a": "Eve", "b": "Sarah", "c": "Rachael", "d": "Rebecca"},
            "answer": "a",
        },
        {
            "question": "Which brother killed Abel?",
            "choices": {"a": "Seth", "b": "Esau", "c": "Ham", "d": "Cain"},
            "answer": "d",
        },
        {
            "question": "Who was Jacob's twin brother?",
            "choices": {"a": "Laban", "b": "Isaac", "c": "Esau", "d": "Joseph"},
            "answer": "c",
        },
        {
            "question": "Who was the mother of Prophet Samuel?",
            "choices": {"a": "Hannah", "b": "Ruth", "c": "Naomi", "d": "Miriam"},
            "answer": "a",
        },
        {
            "question": "Who was Ruth's  mother in-law?",
            "choices": {"a": "Orpah", "b": "Naomi", "c": "Hannah", "d": "Leah"},
            "answer": "b",
        },
        {
            "question": "Who was Israel's first high priest?",
            "choices": {"a":"Joshua", "b":"Caleb", "c": "Eleazer", "d": "Aaron" },
            "answer": "d",
        },
        {
            "question": "Who was the King after King Saul?",
            "choices": {"a": "Jonathan", "b": "David", "c": "Ishbosheth", "d": "Solomon"},
            "answer": "d",
        },
        {
            "question": "Who was the mother of John the baptist?",
            "choices": {"a": "Elizabeth", "b": "Mary", "c": "Mary Magdalene", "d": "Martha"},
            "answer": "a",
        },
        {
            "question": "Which woman of Jericho hide the Israelite spies?",
            "choices": {"a": "Delilah", "b": "Rahab", "c": "Jezebel", "d": "Deborah"},
            "answer": "b",
        },
        {
            "question": "Who was Paul's young companion who received two letters from him?",
            "choices": {"a": "Silas", "b": "Titus", "c": "Timothy", "d": "Apollos"},
            "answer": "c",
        },
        {
            "question": "Which woman-judge led Israel together with Barak?",
            "choices": {"a": "Miriam", "b": "Jael", "c": "Huldah", "d": "Deborah"},
            "answer": "d",
        },
        {
            "question": "Who was Israel's first king?",
            "choices": {"a": "Saul", "b": "David", "c": "Solomon", "d": "Samuel"},
            "answer": "a",
        },
        {
            "question": "Which son of Jacob was sold into slavery by His brothers?",
            "choices": {"a": "Benjamin", "b": "Judah", "c": "Joseph", "d": "Reuben"},
            "answer": "c",
        },
        {
            "question": "Who sat at Jesus' feet while her sister Martha worked?",
            "choices": {"a": "Salome", "b": "Mary", "c": "Elizabeth", "d": "Lydia"},
            "answer": "b",
        },
    ],

#================Books & Verses===================
    "Books & Verses": [
        {
            "question": "How many books are there in the bible?",
            "choices": {"a": "72", "b": "70", "c": "68", "d": "66"},
            "answer": "d",
        },
        {
            "question": "How many books are there in the New Testament?",
            "choices": {"a": "27", "b": "39", "c": "66", "d": "24"},
            "answer": "a",
        },
        {
            "question": "In which book are the Ten commandments given?",
            "choices": {"a": "Numbers", "b": "Chronicles", "c": "Exodus", "d": "Psalms"},
            "answer": "c",
        },
        {
            "question": "Which book of the bible has 150 chapters?",
            "choices": {"a": "Job", "b": "Psalms", "c": "Esau", "d": "Joseph"},
            "answer": "b",
        },
        {
            "question": "John 3:16 says God so loved the world that He gave His only...",
            "choices": {"a": "Son", "b": "Prophet", "c": "Angel", "d": "Servant"},
            "answer": "a",
        },
        {
            "question": "In which book is the shortest verse, 'Jesus wept'?",
            "choices": {"a": "Luke", "b": "John", "c": "Matthew", "d": "Mark"},
            "answer": "b",
        },
        {
            "question": "Which book is a collection of wise saying?",
            "choices": {"a":"Proverbs", "b":"Songs of Solomon", "c": "Lamentations", "d": "Job" },
            "answer": "a",
        },
        {
            "question": "Which letter of Paul listed the 'fruits of the  Spirit'?",
            "choices": {"a": "Romans", "b": "Phillipians", "c": "Ephesians", "d": "Galatians"},
            "answer": "d",
        },
        {
            "question": "Where is the commonest book in the Bible?",
            "choices": {"a": "Romans", "b": "Phillipians", "c": "Ephesians", "d": "Galatians"},
            "answer": "a",
        },
        {
            "question": "Which book of the bible never mention God?",
            "choices": {"a": "Ruth", "b": "Esther", "c": "Jonah", "d": "Titus"},
            "answer": "b", 
        },
        {
            "question": "Which Psalm begins 'The Earth is of the Lord...'?",
            "choices": {"a": "Psalm 19", "b": "Psalm 12", "c": "Psalm 23", "d": "Psalm 24"},
            "answer": "d", 
        },
        {
            "question": "Which book comes right after Malachi?",
            "choices": {"a": "Mark", "b": "Genesis", "c": "Matthew", "d": "Zechariah"},
            "answer": "c", 
        },
        {
            "question": "Which book follows Nehemiah?",
            "choices": {"a": "Ruth", "b": "Esther", "c": "Jonah", "d": "Titus"},
            "answer": "b", 
        },
        {
            "question": "Which book records the Day of Pentecost?",
            "choices": {"a": "Romans", "b": "Hebrews", "c": "James", "d": "Acts"},
            "answer": "d", 
        },
        {
            "question": "The grace of our Lord Jesus Christ..., can be found where?",
            "choices": {"a": "Romans", "b": "Corinthans", "c": "James", "d": "Acts"},
            "answer": "b", 
        },        
    ],
}

print("====================")
print("BIBLE TRIVIA QUIZ")
print("====================")


name = input("Enter your name: ")

print(f"Welcome, {name}!")
print(f"Choose a category: ")

number = 1
for category in categories:
    print(f"{number}. {category}")
    number += 1

choice = input(f"Enter the number of your category: ")

if choice == "1":
    selected_category = "Old Testament"
elif choice == "2":
    selected_category = "New Testament"
elif choice == "3":
    selected_category = "Bible Characters"
elif choice == "4":
    selected_category = "Books & Verses"
else:
    print("Invalid choice: Please try again later.")
    exit()

print(f"You selected: {selected_category}")

# To get questions from the selected category
quiz_questions = questions[selected_category].copy()

# to shuffle the questions
random.shuffle(quiz_questions)

# to recorrd the scores
score = 0

print("-----------------------")
print("Let the quiz begin!!!")
print("-----------------------")

# to ask the question
for question in quiz_questions:
    print(f"+ {question["question"]}")

    # choice options
    for choice, answer in question["choices"].items():
        print(f"{choice}. {answer}")

    answer = input("Enter your answer(a, b, c, d): ")

    # verifyying the answers
    while answer not in ["a", "b", "c", "d"]:
        print("Invalid answer! Please enter a, b, c, d ")
        answer = input("Your answer: ")

    if answer == question["answer"]:
        print("Correct, Well done!!!")
        score += 1
    else:
        print("Sorry, that's incorrect. ")
        print(f"The correct answer is:. {question["answer"]}")

print("=======================")
print("    QUIZ COMPLETED!")
print("...scores calculated...")
print("=======================")
print(f"Player: {name}")
print(f"Category: {selected_category}")
print(f"Your score: {score}/{len(quiz_questions)}")
print("==========================")

# save the players score
with open("leaderboard.csv", "a") as file:
    file.write(f"{name}, {score}, {len(quiz_questions)}\n")

print("Score saved successfully!")

# leaderboard
players = []
with open("leaderboard.csv", "r") as file:
    for line in file:
        details = line.strip().split(",")
        players.append(details)
players.sort(key=lambda x: int(x[2]), reverse=True)

print("====TOP 5 PLAYERS====")

for player in players[:5]:
    print(f"{player[0]} - {player[2]}/{len(quiz_questions)}")

print("======================")
print("Thank you for playing Bible Trivia!")





