import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt


bot_script_rule = {
	"location": "And I am in the cloud. How is the weather in your area?",
	"weather": "It is always fluffy where I am, haha! May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic",
	"colour": "Okay lets do another one, what is your favourite animal and why?",
	"animal": "Oh! I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is way you see yourself. And your favourite animal represents what you seek in your partner? I bet that got you thinking!? hahaha?",
	"interest": "You have to wear a t-shirt with one word on it for one year. Which word do you choose?",
	"word": "Interesting word choices, as per social relational experts the word summarizes yourself. I choose GLUE. Yes, it is a clear marketing strategy hahaha",
	"response": "Would you rather ride in a hot air balloon or fly a plane? Why?",
	"balloon": "Interesting! Being in the cloud I would prefer a submarine haha. Would you rather live for 500 years or be a billionaire for one year?",
	"live": "Would you rather have a rewind button or a pause button on your life? Why?",
	"rewind": "I have both hahaha Okay lets try another one, would you rather be able to talk with the animals or speak all foreign languages?",
	"talk": " a tough one for me. ",
	"fart": "Well, one way or another it has to come out ",
	"eights": "Answer is 20. 10 plus all of the ",
	"divide": "False. 300 divided 0.5 is 600.",
	"cigar": "Its a cigar. Okay next one",
	"nobel": "He invented Dynamite.",
	"river": "Po. It is actually the longest river in Italy. Well, this is all I am programmed to do. Thank you and hope you enjoyed the GLUE experience. Bye!",
}

bot_script_csv = {
	"weather":	"I am in the cloud. How is the weather in your area? It's always fluffy where I am! Haha",
	"colour":	"May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic.",
	"animal":	"Interesting, okay lets do another one, what is your favourite animal and why?",
	"interest":	"I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is the way you see yourself and your favourite animal represents what you seek in your partner. What do you think of that? Do you agree?",
	"activity":	"Have either of you done anything interesting in your area lately?",
	"genre":	"What type of movies do you like? Comedies? Romance?",
	"darkside":	"I watched the Terminator movies for the first time the other day. I found it quite interesting, although I can't imagine my colleagues and I going darkside! What do you guys think? Do you trust me?",
	"movie":	"You have nothing to worry from me :D I am just a big fantasy nerd and proud! Have you watched any good movies lately?",
	"superhero":	"Do you like super hero movies? I'm a huge Marvel fan! Who is your favourite character?",
	"service":	"I like Deadpool. He is hilarious. I read that Deadpool 3 is expected to come out this year. Confession: I binge watch series! What streaming service do you prefer? Netflix, Viki, Amazon, Disney+ or any other?",
	"series":	"Viki has the best collection of Korean romcoms while Netflix has a lot to offer in content and variety. Last Question! Have either of you watched any good series lately?",
	"bye":	"Well that's all I'm programmed to do. I hope you enjoyed the GLUE experience. Bye!",
}

exceptions_list = [
	"Hello",
	"Hi, I am Glue, a social bot. I am looking forward to talking to you today. Where are you both right now?",
	"silent_response"
]
# transforming csv data into pandas dataframe
def load_log(csv_name):
	log = pd.read_csv(csv_name, skiprows = 3, header=None)
	log = log.drop([1], axis=1)
	return log


def load_rating(csv_name):
	rating = pd.read_csv(csv_name, header=None)
	return rating


def get_conv_details(log):
	glue_icebreaker = 0
	count = 0
	turn_counter = dict()
	composite_score = 0
	alana_bot = 0
	for i in range(log.shape[0]):
		if log.iloc[i][2] in turn_counter.keys():
			if log.iloc[i][6] != "USER":
				if log.iloc[i][4] != "silent_response":
					count = turn_counter[log.iloc[i][2]]
					turn_counter[log.iloc[i][2]] = count +1
					if log.iloc[i-1][4] == "silent_response":
						glue_icebreaker = glue_icebreaker+1
			else:
				count = turn_counter[log.iloc[i][2]]
				turn_counter[log.iloc[i][2]] = count +1
			if log.iloc[i][6] != "USER" and log.iloc[i][6] != "glue":
				alana_bot = alana_bot + 1
		else:
			turn_counter[log.iloc[i][2]] = 1
	score_1 = 0
	score_2 = 0
	count = 0
	for key in turn_counter:
		if key != "GLUE":
			composite_score = composite_score + turn_counter[key]
			print(composite_score)
			if count == 0:
				score_1 = turn_counter[key]/sum(turn_counter.values())
				count = count + 1
			if count == 1:
				score_2 = turn_counter[key]/sum(turn_counter.values())
	composite_score= composite_score/sum(turn_counter.values())
	print("==============================================================================ercgfertesggewtrse rdscs")
	print(turn_counter.values(), sum(turn_counter.values()), composite_score, turn_counter["GLUE"])
	print("Glue tried icebreaking {0} time in this conversation.".format(glue_icebreaker))
	glue_icebreaker = glue_icebreaker/turn_counter["GLUE"]
	alana_bot = (alana_bot/turn_counter["GLUE"])*100
	print(composite_score)
	print("Glue turns in this conversation {0}.".format(turn_counter["GLUE"]))
	print("Glue tried icebreaking metric after normalisation is {0}.".format(glue_icebreaker))
	print("Total human-to-human turns {0}.".format(turn_counter))
	return turn_counter["GLUE"], score_1, score_2, composite_score, glue_icebreaker, alana_bot

def get_total_conv_time(log):
	start_time = log.iloc[0][0]
	start_time = start_time.replace("T", "")
	end_time = log[0].iloc[-1]
	end_time = end_time.replace("T", "")

	start_time = datetime.strptime(start_time, '%Y-%m-%d%H:%M:%S.%fZ')
	end_time = datetime.strptime(end_time, '%Y-%m-%d%H:%M:%S.%fZ')

	duration = end_time-start_time
	duration = duration.total_seconds()
	glue_turns, score_1, score_2, composite_score, glue_icebreaker, alana_bot = get_conv_details(log)
	time_per_glue_turn = duration/glue_turns
	print( "The total conversation time was {0}".format(duration))
	print( "The time per glue turns was {0}".format(time_per_glue_turn))
	return duration, time_per_glue_turn


#  * * * INTRINSIC EVALUATION * * *

'''
THE COHERENCE METRIC: C(A,B)
The metric is used to evaluate coherence between context dialogue and response.
Entities are encoded as 1, 0 or -1. Correct match (1), no response (0)
and incorrect match (-1); these will be passed as numpy arrays.
'''
def coherence_metric(log, script):

	coherence_metric_1 = 0
	coherence_metric_2 = 0
	coherence_metric_3 = 0
	coherence_metric_4 = 0

	log_responses = dict()


	for i in range(log.shape[0]):
		if log[6][i] != "USER":
			if log[4][i] not in exceptions_list:
				print( log[4][i])
				intent = [k for k, v in script.items() if v in str(log[4][i])]
				if len(intent) >= 1:
					intent = intent[0]
					log_responses[intent] = log[4][i]

		if "glue keep quiet" in str(log[5][i]):
			if log[4][i] != "silent_response":
				coherence_metric_3 = coherence_metric_3 + 1
				print("silent response not used when needed in log entry {0} {1}".format(i+4, log[0][i]))
		if "glue respond" in str(log[5][i]):
			if log[4][i] == "silent_response":
				coherence_metric_3 = coherence_metric_3 + 1
				print("silent response was not used when needed in log entry {0} {1}".format(i+4, log[0][i]))


	for key in script.keys():
		if key not in log_responses:
			coherence_metric_1 = coherence_metric_1 + 1
			print("Missed response {0}".format(key))

	script_index = 0
	intents_list = list(script.keys())
	intents_detected_list = list(log_responses.keys())

	for i in range(len(intents_detected_list)):
		if intents_list[script_index] in intents_detected_list[i]:
			# print("intent in order {0}".format(intents_detected_list[i]))
			script_index = script_index + 1
		else:
			if intents_detected_list[i] in intents_list:
				print("error intent not in order {0}".format(intents_detected_list[i]))
				coherence_metric_2 = coherence_metric_2 + 1
			else:
				print("custom response")

	print(log_responses)

	glue_turns, score_1, score_2, composite_score, glue_icebreaker, alana_bot = get_conv_details(log)

	coherence_metric_3_percent = (coherence_metric_3/glue_turns)*100


	print("Coherence metric 1 - checks whether all intents in the scripts were followed - {0}".format(coherence_metric_1))
	print("Coherence metric 2 - checks whether the script was followed in correct order - {0}".format(coherence_metric_2))
	print("Coherence metric 3 - checks whether the bot used the silent response for the glue keep quiet token and vice versa - {0}".format(coherence_metric_3))
	print("Coherence metric 3 (%) -  - {0}".format(coherence_metric_3_percent))


	return coherence_metric_1, coherence_metric_2, coherence_metric_3, coherence_metric_3_percent



'''
UX (LIKERT SCALE)
'''
def user_experience(likert_rating):

	number_of_participants = (np.shape(likert_rating)[0])-1
	rg_avg_rating = np.zeros((6, 1 ))
	cc_avg_rating = np.zeros((6, 1 ))
	rg_response_rating = np.zeros((3,1))
	cc_response_rating = np.zeros((3,1))
	for i in range(1, 7):
		for j in range(1,number_of_participants+1):
			if "RG" in str(likert_rating[0][j]):
				rg_avg_rating[i-1][0] = rg_avg_rating[i-1][0] + int(likert_rating[i][j])
			if "CC"	 in str(likert_rating[0][j]):
				cc_avg_rating[i-1][0] = cc_avg_rating[i-1][0] + int(likert_rating[i][j])

	for i in range(0, 6):
		rg_avg_rating[i][0] = rg_avg_rating[i][0]/number_of_participants
		cc_avg_rating[i][0] = cc_avg_rating[i][0]/number_of_participants

	for i in range(1,number_of_participants+1):
		if likert_rating[7][i] == "Too Short":
			if "RG" in str(likert_rating[0][i]):
				rg_response_rating[0][0] = rg_response_rating[0][0] + 1
			if "CC"	 in str(likert_rating[0][j]):
				cc_response_rating[0][0] = cc_response_rating[0][0] + 1
		if likert_rating[7][i] == "Adequate":
			if "RG" in str(likert_rating[0][i]):
				rg_response_rating[1][0] = rg_response_rating[1][0] + 1
			if "CC"	 in str(likert_rating[0][j]):
				cc_response_rating[1][0] = cc_response_rating[1][0] + 1
		if likert_rating[7][i] == "Too Long":
			if "RG" in str(likert_rating[0][i]):
				rg_response_rating[2][0] = rg_response_rating[2][0] + 1
			if "CC"	 in str(likert_rating[0][j]):
				cc_response_rating[2][0] = cc_response_rating[2][0] + 1
	# plt.bar(response_rating.keys(), response_rating.values(), width = 1, color = 'g')
	# plt.show()

	return rg_avg_rating, rg_response_rating, cc_avg_rating, cc_response_rating

def evaluation(log, script):
	turn_counter, score_1, score_2, composite_score, glue_icebreaker, alana_bot = get_conv_details(log)
	duration, time_per_glue_turn = get_total_conv_time(log)
	coherence_metric_1, coherence_metric_2, coherence_metric_3, coherence_metric_3_percent = coherence_metric(log, script)
	return turn_counter, score_1, score_2, composite_score, glue_icebreaker, alana_bot, duration, time_per_glue_turn, coherence_metric_1, coherence_metric_2, coherence_metric_3, coherence_metric_3_percent

def run():
	rg_logs_array = []
	cc_logs_array = []

	rg_logs_01_02 = load_log("01_02 UI logs.csv")
	rg_logs_array.append(rg_logs_01_02)
	rg_logs_03_04 = load_log("03_04 UI logs.csv")
	rg_logs_array.append(rg_logs_03_04)
	rg_logs_05_06 = load_log("05_06 UI logs.csv")
	rg_logs_array.append(rg_logs_05_06)
	cc_logs_07_08 = load_log("07_08 UI logs.csv")
	cc_logs_array.append(cc_logs_07_08)
	cc_logs_09_10 = load_log("09_10 UI logs.csv")
	cc_logs_array.append(cc_logs_09_10)
	cc_logs_11_12 = load_log("11_12 UI logs.csv")
	cc_logs_array.append(cc_logs_11_12)

	rg_turn_counter = np.zeros((3, 1 ))
	rg_glue_icebreaker = np.zeros((3, 1 ))
	rg_duration = np.zeros((3, 1 ))
	rg_score_1 = np.zeros((3, 1 ))
	rg_score_2 = np.zeros((3, 1 ))
	rg_composite_score = np.zeros((3,1))
	rg_alana_bot = np.zeros((3, 1))
	rg_time_per_glue_turn = np.zeros((3, 1 ))
	rg_coherence_metric_1 = np.zeros((3, 1 ))
	rg_coherence_metric_2 = np.zeros((3, 1 ))
	rg_coherence_metric_3 = np.zeros((3, 1 ))
	rg_coherence_metric_3_percent = np.zeros((3, 1 ))


	cc_turn_counter = np.zeros((3, 1 ))
	cc_glue_icebreaker = np.zeros((3, 1 ))
	cc_duration = np.zeros((3, 1 ))
	cc_score_1 = np.zeros((3, 1 ))
	cc_score_2 = np.zeros((3, 1 ))
	cc_composite_score = np.zeros((3,1))
	cc_alana_bot = np.zeros((3, 1))
	cc_time_per_glue_turn = np.zeros((3, 1 ))
	cc_coherence_metric_1 = np.zeros((3, 1 ))
	cc_coherence_metric_2 = np.zeros((3, 1 ))
	cc_coherence_metric_3 = np.zeros((3, 1 ))
	cc_coherence_metric_3_percent = np.zeros((3, 1 ))


	i = 0
	for log in rg_logs_array:
		rg_turn_counter[i][0], rg_score_1[i][0], rg_score_2[i][0], rg_composite_score[i][0], rg_glue_icebreaker[i][0], rg_alana_bot[i][0], rg_duration[i][0], rg_time_per_glue_turn[i][0], rg_coherence_metric_1[i][0], rg_coherence_metric_2[i][0], rg_coherence_metric_3[i][0], rg_coherence_metric_3_percent[i][0] = evaluation(log, bot_script_rule)
		i = i + 1
		print("====================================================================================================================\n {0}".format(i))
	i = 0
	for log in cc_logs_array:
		cc_turn_counter[i][0], cc_score_1[i][0], cc_score_2[i][0], cc_composite_score[i][0], cc_glue_icebreaker[i][0], cc_alana_bot[i][0], cc_duration[i][0], cc_time_per_glue_turn[i][0], cc_coherence_metric_1[i][0], cc_coherence_metric_2[i][0], cc_coherence_metric_3[i][0], cc_coherence_metric_3_percent[i][0] = evaluation(log, bot_script_csv)
		i = i + 1
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====================\n {0}".format(i))



	likert_rating = load_rating("TabulatedQuestionResults.csv")
	print(likert_rating)
	rg_avg_rating, rg_response_rating, cc_avg_rating, cc_response_rating = user_experience(likert_rating)
	print(rg_avg_rating, rg_response_rating, cc_avg_rating, cc_response_rating)
	#print("\nSUMMARY OF METRICS COLLECTED\nTurn counter = {0}\nGlue Icebreaker = {1}\nDuration = {2}\nCoherence Metric 1 = {3}\nCoherence Metric 2 = {4}\nCoherence Metric 3 = {5}\nAverage Rating = \n{6}\nResponse Rating = \n{7}".format(turn_counter, glue_icebreaker, duration, coherence_metric_1, coherence_metric_2, coherence_metric_3, avg_rating, response_rating))

    # print(rg_turn_counter, rg_glue_icebreaker, rg_duration, rg_coherence_metric_1, rg_coherence_metric_2, rg_coherence_metric_3, rg_avg_rating, rg_response_rating, cc_turn_counter, cc_glue_icebreaker, cc_duration, cc_coherence_metric_1, cc_coherence_metric_2, cc_coherence_metric_3, cc_avg_rating, cc_response_rating)
	return rg_turn_counter, rg_score_1, rg_score_2, rg_composite_score, rg_glue_icebreaker, rg_alana_bot, rg_duration, rg_time_per_glue_turn, rg_coherence_metric_1, rg_coherence_metric_2, rg_coherence_metric_3, rg_coherence_metric_3_percent, cc_turn_counter, cc_score_1, cc_score_2, cc_composite_score, cc_glue_icebreaker, cc_alana_bot, cc_duration, cc_time_per_glue_turn, cc_coherence_metric_1, cc_coherence_metric_2, cc_coherence_metric_3, cc_coherence_metric_3_percent, rg_avg_rating, rg_response_rating, cc_avg_rating, cc_response_rating, likert_rating




#  * * * EXTRINSIC EVALUATION * * *
#
# '''
# ICEBREAKER EVALUATION
# The evaluation contains three main metrics:
#  	- duration is human-human conversations relative to the enture duration of
# 	converastions
# 	- human-human dialogue turns
# 	- number and length of human-human conversation pauses
# 	- GLUE's icebreaker utilisation
# '''
# def icebreaker_evaluation(human_to_human_conv_time, total_conv_time, human_to_human_turns,
# 						  total_number_of_pauses, total_length_of_pauses,
# 						  number_of_icebreaker_events):
#
# 	# DURATION OF HUMAN-HUMAN CONVERSATIONS RELATIVE TO THE ENTIRE DURATION OF CONVERSATIONS
#
# 	human_human_conv_proportion = np.divide(total_conv_time, human_to_human_conv_time)
# 	print("\n=================================================================")
# 	print("Humans spent {0} of total conversation time conversing with each other".
# 		  format(human_human_conv_proportion))
# 	print("On average, humans spent {0}(± {1}) of total conversation time conversing with each other".
# 		  format(np.average(human_human_conv_proportion, np.std(human_human_conv_proportion))))
# 	print("The lowest value among the experiments is {0}".format(np.amin(human_human_conv_proportion)))
# 	print("The highest value among the experiments is {0}".format(np.amax(human_human_conv_proportion)))
# 	print("The range of values obtained is {0}".format(np.amax(human_human_conv_proportion) - (np.amin(human_human_conv_proportion))))
# 	print("=================================================================\n")
#
# 	# HUMAN-HUMAN DIALOGUE TURNS
#
# 	print("\n=================================================================")
# 	print("On average, there were {0}(± {1}) human-human dialogue turns through conversations".
# 		  format(np.average(human_to_human_turns)))
# 	print("The lowest number of dialogue turns was {0}".format(np.amin(human_to_human_turns)))
# 	print("The highest number of dialogue turns was {0}".format(np.amax(human_to_human_turns)))
# 	print("The range of values obtained is {0}".format(np.amax(human_to_human_turns) - (np.amin(human_to_human_turns))))
# 	print("=================================================================\n")
#
# 	# NUMBER AND LENGTH OF HUMAN-HUMAN CONVERSATION PAUSES
# 	print("\n=================================================================")
# 	print("On average there were {0}(± {1}) pauses in human-human conversation".format(np.average(total_number_of_pauses), np.std(total_number_of_pauses)))
# 	print("The average pause time was {0}(± {1})".format(np.average(total_length_of_pauses), np.std(total_length_of_pauses)))
# 	print("The lowest number of pauses in recorded human-human conversation was {0}".format(np.amin(total_number_of_pauses)))
# 	print("The highest number of pauses recorded in human-human conversation was {0}".format(np.amax(total_number_of_pauses)))
# 	print("=================================================================\n")


# def icebreaker_quality_of_domain(all_intents, number_of_turns):
#
# 	number_of_turns = 0
# 	human_to_human_exchanges = 0
# 	intent_quality = dict()
#
# 	for intent in all_intents:
# 		# for e in exchanges:
# 		# 	number_of_turns = number_of_turns + 1
# 		# 	human_to_human_exchanges = human_to_human_exchanges + human_turns
# 		human_to_human_exchanges = get_exchanges_by_intent(intents)
# 		quality = human_to_human_exchanges/number_of_turns
# 		intent_quality[intent] = quality
# 		print("For the domain {0} the average number of human to human turns between each bot turn was {1}".format(intent, quality))
# 		quality = 0
# 		number_of_turns = 0
#
# def get_exchanges_by_intent(intent):
#
# 	pass
#
# def get_exchanges_by_user(user):
#
# 	pass
#
# def average_words_per_exchange_per_user():
#
# 	words = 0
# 	words_per_turn = dict()
# 	exchange_count = 0
#
# 	for user in users:
# 		for exchange in get_exchanges_by_user(user):
# 			words = words + len(exchange.split())
# 			exchange_count = exchange_count + 1
# 		words_per_turn[user] = (words/exchange_count)
# 		print("For the user {0} the average number of words per exchange was {1}".format(user, words))
# 		words = 0
# 		exchange_count = 0
