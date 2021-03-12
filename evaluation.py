import pandas as pd
import numpy as np

# transforming csv data into pandas dataframe
def load_data(csv_name):
	data = pd.read_csv(csv_name, header=None)
	return data


#  * * * INTRINSIC EVALUATION * * *

'''
THE COHERENCE METRIC: C(A,B)
The metric is used to evaluate coherence between context dialogue and response.
Entities are encoded as 1, 0 or -1. Correct match (1), no response (0)
and incorrect match (-1); these will be passed as numpy arrays.
'''
def coherence_metric(total_input_entities, total_matched_response_entities):
	pass


'''
DOMAIN COVERAGE
The metric is used to evaluate the domain coverage during Icebreaker event.
'''
def domain_coverage(total_domains, total_icebreaker_events, domains_used):
	pass

#  * * * EXTRINSIC EVALUATION * * *

'''
ICEBREAKER EVALUATION
The evaluation contains three main metrics:
 	- duration is human-human conversations relative to the enture duration of
	converastions
	- human-human dialogue turns
	- number and length of human-human conversation pauses
	- GLUE's icebreaker utilisation
'''
def icebreaker_evaluation(human_to_human_conv_time, total_conv_time, human_to_human_turns,
							total_number_of_pauses, total_length_of_pauses,
							number_of_icebreaker_events):

# DURATION OF HUMAN-HUMAN CONVERSATIONS RELATIVE TO THE ENTIRE DURATION OF CONVERSATIONS

	human_human_conv_proportion = np.divide(total_conv_time, human_to_human_conv_time)
	print("\n=================================================================")
	print("Humans spent {0} of total conversation time conversing with each other".
		format(human_human_conv_proportion))
	print("On average, humans spent {0}(± {1}) of total conversation time conversing with each other".
		format(np.average(human_human_conv_proportion, np.std(human_human_conv_proportion))))
	print("The lowest value among the experiments is {0}".format(np.amin(human_human_conv_proportion)))
	print("The highest value among the experiments is {0}".format(np.amax(human_human_conv_proportion)))
	print("The range of values obtained is {0}".format(np.amax(human_human_conv_proportion) - (np.amin(human_human_conv_proportion)))
	print("=================================================================\n")

# HUMAN-HUMAN DIALOGUE TURNS

	print("\n=================================================================")
	print("On average, there were {0}(± {1}) human-human dialogue turns through conversations".
			format(np.average(human_to_human_turns)))
	print("The lowest number of dialogue turns was {0}".format(np.amin(human_to_human_turns)))
	print("The highest number of dialogue turns was {0}".format(np.amax(human_to_human_turns)))
	print("The range of values obtained is {0}".format(np.amax(human_to_human_turns)) - (np.amin(human_to_human_turns))))
	print("=================================================================\n")

# NUMBER AND LENGTH OF HUMAN-HUMAN CONVERSATION PAUSES
	print("\n=================================================================")
	print("On average there were {0}(± {1}) pauses in human-human conversation".format(np.average(total_number_of_pauses), np.std(total_number_of_pauses)))
	print("The average pause time was {0}(± {1})".format(np.average(total_length_of_pauses), np.std(total_length_of_pauses)))
	print("The lowest number of pauses in recorded human-human conversation was {0}".format(np.amin(total_number_of_pauses)))
	print("The highest number of pauses recorded in human-human conversation was {0}".format(np.amax(total_number_of_pauses)))
	print("=================================================================\n")

'''
UX (LIKERT SCALE)
'''
def user_experience():
	pass
