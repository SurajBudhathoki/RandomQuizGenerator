# Creating quizzes with questions and answers in random order, along with the answer keys in text files.

import random

# The quiz data; Keys are countries and values are their capitals
capitals = {"Afghanistan": "Kabul", "Argentina": "Buenos Aires", "Australia": "Canberra",
            "Austria": "Vienna", "Bangladesh": "Dhaka", "Belgium": "Brussels", "Brazil" : "Brasilia",
            "Cameroon" : "Yaounde", "Canada" : "Ottawa",  "Chile" : "Santiago", "China" : "Beijing",
            "Colombia" : "Bogota", "Costa Rica" : "San Jose", "Croatia" : "Zagreb", "Cuba" : "Havana",
            "Czech Republic" : "Prague", "Denmark" : "Copenhagen", "Egypt" : "Cairo", "El Salvador" : "San Salvador",
            "France" : "Paris", "Germany" : "Berlin", "Greece" : "Athens", "India" : "New Delhi",  "Italy" : "Rome",
            "Japan" : "Tokyo", "Jordan" : "Amman", "Mexico" : "Mexico City", "Nepal" : "Kathmandu",
            "Netherlands" : "Amsterdam", "Pakistan" : "Islamabad",  "Peru" : "Lima", "Philippines" : "Manila",
            "Poland" : "Warsaw", "Portugal" : "Lisbon", "Qatar" : "Doha", "Romania" : "Bucharest",
            "Russia" : "Moscow", "Saudi Arabia" : "Riyadh", "Senegal" : "Dakar", "Serbia" : "Belgrade",
            "Singapore" : "Singapore", "Slovakia" : "Bratislava",  "Spain" : "Madrid", "Sri Lanka" : "Colombo",
            "Sweden": "Stockholm", "Switzerland" : "Bern", "Thailand" : "Bangkok", "Ukraine" : "Kyiv",
            "United Kingdom" : "London", "United States of America" : "Washington, D.C."}

# Generate 20 quiz files.
for quizNum in range(20):
    # Creating the quiz and answer key files
    quizFile = open('quiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('quiz_answers%s.txt' % (quizNum + 1), 'w')

    # Writing header for the quizzes
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Countries and Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    countries = list(capitals.keys())
    random.shuffle(countries)

    # looping through the countries, making a question for each

    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswer = capitals[countries[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
                                                             countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
