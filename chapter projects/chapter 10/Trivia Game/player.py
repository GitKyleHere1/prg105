# A class module for player

class Player:
    # Define attributes
    def __init__(self, name, score, question_count):
        self.__name = name
        self.__score = score
        self.__question_count = question_count

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def set_question_count(self, question_count):
        self.__question_count = question_count

    def increment_score(self):
        self.__score += 1

    def increment_question_count(self):
        self.__question_count += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_question_count(self):
        return self.__question_count

    def __str__(self):
        return " ".join([self.__name, self.__score, self.__question_count])
