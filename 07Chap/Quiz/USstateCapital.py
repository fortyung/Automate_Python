import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 5 test question
for quiznum in range(5):
	# generatates the Quiz and Answer files
	quizFile = open('captialQuiz%s.txt' % (quiznum + 1), 'w')
	answerFile = open('captialAnswers%s.txt' % (quiznum + 1), 'w')

	# Header file
	quizFile.write('Name:\nDate:\nTime:')
	quizFile.write((' ' * 20 ) + 'Form%s' % (quiznum + 1))
	quizFile.write('\n\n')

	# Shuffling the order of the state
	States = list(capitals.keys())
	random.shuffle(States)

	for i in range(50):
		# The correct answers
		correctAns = capitals[States[i]]
		wrongAns = list(capitals.values())

		# wrong answers = list of all the capitals without the correct answer
		del wrongAns[wrongAns.index(correctAns)]

		# only 3 wrong answers
		wrongAns = random.sample(wrongAns, 3)

		# Multi chioce options
		options = wrongAns + [correctAns]
		random.shuffle(options)

		quizFile.write('%s. What is the capital of %s?\n' % (i + 1, States[i]))
		for j in range(4):
			quizFile.write('\t%s. %s\n' % ('ABCD'[j], options[j]))
		quizFile.write('\n\n')
		answerFile.write('%s. %s\n' % (i + 1, 'ABCD'[options.index(correctAns)]))

	quizFile.close()
	answerFile.close()