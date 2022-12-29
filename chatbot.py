import random

# Define a list of common questions and their answers
questions_and_answers = [
  ("What are your business hours?", "We are open from 9am to 5pm, Monday to Friday."),
  ("Where is the restroom?", "The restroom is down the hallway to the right."),
  ("Where can I find the HR department?", "The HR department is located on the second floor, room 201."),
  ("Where can I find the marketing department?", "The marketing department is located on the third floor, room 301.")
]

# Define a list of greetings and farewells
greetings = ["Hello!", "Hi there!", "Welcome to our company!"]
farewells = ["Goodbye!", "See you later!", "Thank you for visiting!"]

# Print a random greeting
print(random.choice(greetings))

# Loop until the user enters "exit"
while True:
  # Prompt the user for a question
  question = input("What can I help you with today? ")

  # If the user entered "exit", break out of the loop
  if question.lower() == "exit":
    break

  # Initialize a flag to indicate if the question was answered
  answered = False

  # Check if the question is in the list of common questions
  for q, a in questions_and_answers:
    if q.lower() in question.lower():
      # If the question matches, print the answer and set the flag to True
      print(a)
      answered = True
      break

  # If the question was not answered, print a message
  if not answered:
    print("I'm sorry, I cannot help with that. Please ask a receptionist for assistance.")

# Print a random farewell
print(random.choice(farewells))
