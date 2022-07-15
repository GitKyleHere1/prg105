# A trivia game where 2 players answer 5 questions each and receive a score at the end.

import question
import player
import random


# Define main function
def main():
    # Create players
    player1 = player.Player("Player 1", 0, 0)
    player2 = player.Player("Player 2", 0, 0)

    # Create Questions
    q1 = question.Question("What is the capital of Illinois?", "A: Chicago", "B: Springfield", "C: Woodstock", "D: Algonquin", "B")
    q2 = question.Question("Regarding 'The Beatles', which is a correct song title?", "A: The Final Countdown", "B: Bohemian Rhapsody", "C: We Will Rock You", "D: Hey Jude", "D")
    q3 = question.Question("Who is the owner of the electric car brand 'Tesla'?", "A: Nikola Tesla", "B: Michael Jordan", "C: Elon Musk", "D: Mr. Bean", "C")
    q4 = question.Question("Which president was said to have had wooden teeth?", "A: Abraham Lincoln", "B: George Washington", "C: Barack Obama", "D: John F Kennedy", "A")
    q5 = question.Question("Which topping does not belong on a pizza?", "A: Pepperoni", "B: Onions", "C: Sausage", "D: Pineapple", "D")
    q6 = question.Question("Where did Python (programming language) get its name inspired from?", "A: Snakes", "B: Monty Python", "C: A video game", "D: None of these", "B")
    q7 = question.Question("Who invented the lightbulb?", "A: Benjamin Franklin", "B: Sigmund Freud", "C: Albert Einstein", "D: Thomas Edison", "D")
    q8 = question.Question("What country is home to the Eiffel Tower?", "A: New York", "B: France", "C: Egypt", "D: England", "B")
    q9 = question.Question("Who was the founder of Ford Motor Company?", "A: Henry Ford", "B: Larry Ford", "C: Jerry Ford", "D: Gary Ford", "A")
    q10 = question.Question("Who was the first person on the moon?", "A: Shaquille O'Neal", "B: Louis Armstrong", "C: A Monkey", "D: Neil Armstrong", "D")

    # Create a list of the questions and then shuffle the list
    question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    random.shuffle(question_list)

    # Set a sublist of questions for each player
    question_set1 = question_list[:5]
    question_set2 = question_list[5:]

    # Display play 1 turn
    print(player1.get_name() + ", It is your turn to answer 5 questions.\n")

    # Loop through player 1's questions
    for q in question_set1:
        print(q.get_question(), q.get_answer1(), q.get_answer2(), q.get_answer3(), q.get_answer4(), sep="\n")

        # Get answer from player
        answer = input("\nWhat is your answer?: ").upper()

        # Increment question count
        player1.increment_question_count()

        # Check if player has correct answer, if correct, increment the score for the player
        if answer == q.get_answer():
            print("That is correct!")
            player1.increment_score()
        else:
            # Message for incorrect answer
            print("Sorry that was not correct, the correct answer was {}.".format(q.get_answer()))

        print("\nNext Question:\n")

    # Display play 2 turn
    print(player2.get_name() + ", It is your turn to answer 5 questions.")

    # Loop through player 2's questions
    for q in question_set2:
        print(q.get_question(), q.get_answer1(), q.get_answer2(), q.get_answer3(), q.get_answer4(), sep="\n")

        # Get answer from player
        answer = input("\nWhat is your answer?: ").upper()

        # Increment question count
        player2.increment_question_count()

        # Check if player has correct answer, if correct, increment the score for the player
        if answer == q.get_answer():
            print("That is correct!")
            player2.increment_score()
        else:
            # Message for incorrect answer
            print("Sorry that was not correct, the correct answer was {}.".format(q.get_answer()))

        print("\nNext Question:\n")

    # Display scores for players
    print(player1.get_name() + ", you scored {} out of {}.".format(player1.get_score(), player1.get_question_count()))
    print(player2.get_name() + ", you scored {} out of {}.".format(player2.get_score(), player2.get_question_count()))

    # Print winner or draw
    if player1.get_score() > player2.get_score():
        print(player1.get_name() + " is the winner!")
    elif player2.get_score() > player1.get_score():
        print(player2.get_name() + " is the winner!")
    else:
        print("Tie Game!")


# Call Main
main()
