import statistical_tests as stat
import evaluation as data
import numpy as np
import pandas as pd
from scipy import stats

rg_turn_counter, rg_score_1, rg_score_2, rg_composite_score, rg_glue_icebreaker, rg_alana_bot, rg_duration, rg_time_per_glue_turn, rg_coherence_metric_1, rg_coherence_metric_2, rg_coherence_metric_3, rg_coherence_metric_3_percent, cc_turn_counter, cc_score_1, cc_score_2, cc_composite_score, cc_glue_icebreaker, cc_alana_bot, cc_duration, cc_time_per_glue_turn, cc_coherence_metric_1, cc_coherence_metric_2, cc_coherence_metric_3, cc_coherence_metric_3_percent, rg_avg_rating, rg_response_rating, cc_avg_rating, cc_response_rating, likert_rating = data.run()

rg_q1 = likert_rating[1:7][1].to_numpy()
rg_q2 = likert_rating[1:7][2].to_numpy()
rg_q3 = likert_rating[1:7][3].to_numpy()
rg_q4 = likert_rating[1:7][4].to_numpy()
rg_q5 = likert_rating[1:7][5].to_numpy()
rg_q6 = likert_rating[1:7][6].to_numpy()

# rg_q2 = np.asarray(likert_rating[1:7][2]).reshape(0,6)
# rg_q3 = np.asarray(likert_rating[1:7][3]).reshape(0,6)
# rg_q4 = np.asarray(likert_rating[1:7][4]).reshape(0,6)
# rg_q5 = np.asarray(likert_rating[1:7][5]).reshape(0,6)
# rg_q6 = np.asarray(likert_rating[1:7][6]).reshape(0,6)
# cc_q1 = np.asarray(likert_rating[7:][1]).reshape(0,6)
cc_q1 = likert_rating[7:][1].to_numpy()
cc_q2 = likert_rating[7:][2].to_numpy()
cc_q3 = likert_rating[7:][3].to_numpy()
cc_q4 = likert_rating[7:][4].to_numpy()
cc_q5 = likert_rating[7:][5].to_numpy()
cc_q6 = likert_rating[7:][6].to_numpy()

rg_score =  np.concatenate((rg_score_1, rg_score_2), axis=0)
cc_score =  np.concatenate((cc_score_1, cc_score_2), axis=0)



print("*************************************")
print("**** Turn counter ****")
print("ChitChat")
print(stats.describe(cc_turn_counter))
print("Mean {0}, SD {1}".format(cc_turn_counter.mean(), cc_turn_counter.std()))
print("GameBot")
print(stats.describe(rg_turn_counter))
print("Mean {0}, SD {1}".format(rg_turn_counter.mean(), rg_turn_counter.std()))
stat.check_icebreaker_statistical_significance(cc_turn_counter, rg_turn_counter)


print("**** Normalised user turns count ****")
print("ChitChat")
print(stats.describe(cc_score))
print("Mean {0}, SD {1}".format(cc_score.mean(), cc_score.std()))
print("GameBot")
print(stats.describe(rg_score))
print("Mean {0}, SD {1}".format(rg_score.mean(), rg_score.std()))
stat.check_icebreaker_statistical_significance(cc_score, rg_score)


print("**** Normalised composite user turns count ****")
print("ChitChat")
print(stats.describe(cc_composite_score))
print("Mean {0}, SD {1}".format(cc_composite_score.mean(), cc_composite_score.std()))
print("GameBot")
print(stats.describe(rg_composite_score))
print("Mean {0}, SD {1}".format(rg_composite_score.mean(), rg_composite_score.std()))
stat.check_icebreaker_statistical_significance(cc_composite_score, rg_composite_score)


print("\n**** Glue icebreaker ****")
print("ChitChat")
print(stats.describe(cc_glue_icebreaker))
print("Mean {0}, SD {1}".format(cc_glue_icebreaker.mean(), cc_glue_icebreaker.std()))
print("GameBot")
print(stats.describe(rg_glue_icebreaker))
print("Mean {0}, SD {1}".format(rg_glue_icebreaker.mean(),rg_glue_icebreaker.std()))
stat.check_icebreaker_statistical_significance(cc_glue_icebreaker, rg_glue_icebreaker)


print("\n**** Alana Bot ****")
print("ChitChat")
print(stats.describe(cc_alana_bot))
print("Mean {0}, SD {1}".format(cc_alana_bot.mean(), cc_alana_bot.std()))
print("GameBot")
print(stats.describe(rg_alana_bot))
print("Mean {0}, SD {1}".format(rg_alana_bot.mean(),rg_alana_bot.std()))
stat.check_icebreaker_statistical_significance(cc_alana_bot, rg_alana_bot)


print("\n**** Duration ****")
print("ChitChat")
print(stats.describe(cc_duration))
print("Mean {0}, SD {1}".format(cc_duration.mean(), cc_duration.std()))
print("GameBot")
print(stats.describe(rg_duration))
print("Mean {0}, SD {1}".format(rg_duration.mean(), rg_duration.std()))
stat.check_icebreaker_statistical_significance(cc_duration, rg_duration)

print("\n**** Time per glue turns ****")
print("ChitChat")
print(stats.describe(cc_time_per_glue_turn))
print("Mean {0}, SD {1}".format(cc_time_per_glue_turn.mean(), cc_time_per_glue_turn.std()))
print("GameBot")
print(stats.describe(rg_time_per_glue_turn))
print("Mean {0}, SD {1}".format(rg_time_per_glue_turn.mean(), rg_time_per_glue_turn.std()))
stat.check_icebreaker_statistical_significance(cc_time_per_glue_turn, rg_time_per_glue_turn)

print("\n**** Coherence metric 1 ****")
print("ChitChat")
print(stats.describe(cc_coherence_metric_1))
print("Mean {0}, SD {1}".format(cc_coherence_metric_1.mean(), cc_coherence_metric_1.std()))
print("GameBot")
print(stats.describe(rg_coherence_metric_1))
print("Mean {0}, SD {1}".format(rg_coherence_metric_1.mean(), rg_coherence_metric_1.std()))
stat.check_icebreaker_statistical_significance(cc_coherence_metric_1, rg_coherence_metric_1)

print("\nCoherence metric 2")
print("ChitChat")
print(stats.describe(cc_coherence_metric_2))
print("Mean {0}, SD {1}".format(cc_coherence_metric_2.mean(), cc_coherence_metric_2.std()))
print("GameBot")
print(stats.describe(rg_coherence_metric_2))
print("Mean {0}, SD {1}".format(rg_coherence_metric_2.mean(), rg_coherence_metric_2.std()))
stat.check_icebreaker_statistical_significance(cc_coherence_metric_2, rg_coherence_metric_2)

print("\nCoherence metric 3")
print("ChitChat")
print(stats.describe(cc_coherence_metric_3))
print("Mean {0}, SD {1}".format(cc_coherence_metric_3.mean(), cc_coherence_metric_3.std()))
print("GameBot")
print(stats.describe(rg_coherence_metric_3))
print("Mean {0}, SD {1}".format(rg_coherence_metric_3.mean(), rg_coherence_metric_3.std()))
stat.check_icebreaker_statistical_significance(cc_coherence_metric_3, rg_coherence_metric_3)

print("\nCoherence metric 3 (%)")
print("ChitChat")
print(stats.describe(cc_coherence_metric_3_percent))
print("Mean {0}, SD {1}".format(cc_coherence_metric_3_percent.mean(), cc_coherence_metric_3_percent.std()))
print("GameBot")
print(stats.describe(rg_coherence_metric_3_percent))
print("Mean {0}, SD {1}".format(rg_coherence_metric_3_percent.mean(), rg_coherence_metric_3_percent.std()))
stat.check_icebreaker_statistical_significance(cc_coherence_metric_3_percent, rg_coherence_metric_3_percent)

print("\nUser experience question 1")
print("ChitChat")
print(stats.describe(cc_q1))
print("Mean {0}, SD {1}".format(cc_q1.mean(), cc_q1.std()))
print("GameBot")
print(stats.describe(rg_q1))
print("Mean {0}, SD {1}".format(rg_q1.mean(), rg_q1.std()))
stat.check_UX_statistical_significance(cc_q1, rg_q1)

print("\nUser experience question 2")
print("ChitChat")
print(stats.describe(cc_q2))
print("Mean {0}, SD {1}".format(cc_q2.mean(), cc_q2.std()))
print("GameBot")
print(stats.describe(rg_q2))
print("Mean {0}, SD {1}".format(rg_q2.mean(), rg_q2.std()))
stat.check_UX_statistical_significance(cc_q2, rg_q2)

print("\nUser experience question 3")
print("ChitChat")
print(stats.describe(cc_q3))
print("Mean {0}, SD {1}".format(cc_q3.mean(), cc_q3.std()))
print("GameBot")
print(stats.describe(rg_q3))
print("Mean {0}, SD {1}".format(rg_q3.mean(), rg_q3.std()))
stat.check_UX_statistical_significance(cc_q3, rg_q3)

print("\nUser experience question 4")
print("ChitChat")
print(stats.describe(cc_q4))
print("Mean {0}, SD {1}".format(cc_q4.mean(), cc_q4.std()))
print("GameBot")
print(stats.describe(rg_q4))
print("Mean {0}, SD {1}".format(rg_q4.mean(), rg_q4.std()))
stat.check_UX_statistical_significance(cc_q4, rg_q4)

print("\nUser experience question 5")
print("ChitChat")
print(stats.describe(cc_q5))
print("Mean {0}, SD {1}".format(cc_q5.mean(), cc_q5.std()))
print("GameBot")
print(stats.describe(rg_q5))
print("Mean {0}, SD {1}".format(rg_q5.mean(), rg_q5.std()))
stat.check_UX_statistical_significance(cc_q5, rg_q5)

print("\nUser experience question 6")
print("ChitChat")
print(stats.describe(cc_q6))
print("Mean {0}, SD {1}".format(cc_q6.mean(), cc_q6.std()))
print("GameBot")
print(stats.describe(rg_q6))
print("Mean {0}, SD {1}".format(rg_q6.mean(), rg_q6.std()))
stat.check_UX_statistical_significance(cc_q6, rg_q6)

print("{0}\n\n{1}\n\n{2}\n\n{3}\n\n{4}\n\n{5}\n\n{6}\n\n{7}\n\n{8}\n\n{9}\n\n{10}\n\n{11}\n\n{12}\n\n{13}\n\n{14}\n\n{15}\n\n{16}\n\n{17}\n\n{18}\n\n{19}".format(rg_turn_counter, rg_score_1, rg_score_2, rg_glue_icebreaker, rg_alana_bot, rg_duration, rg_coherence_metric_1, rg_coherence_metric_2, rg_coherence_metric_3, rg_coherence_metric_3_percent, cc_turn_counter, cc_score_1, cc_score_2, cc_glue_icebreaker, cc_alana_bot, cc_duration, cc_coherence_metric_1, cc_coherence_metric_2, cc_coherence_metric_3, cc_coherence_metric_3_percent))

turn_counter = np.concatenate((cc_turn_counter, rg_turn_counter), axis=1)
np.savetxt("turn_counter.csv", (turn_counter), delimiter= ",", header ="cc_turn_counter, rg_turn_counter" )

score_1 = np.concatenate((cc_score_1, rg_score_1), axis=1)
np.savetxt("score_1.csv", (score_1), delimiter= ",", header ="cc_score_1, rg_score_1" )

score_2 = np.concatenate((cc_score_2, rg_score_2), axis=1)
np.savetxt("score_2.csv", (score_2), delimiter= ",", header ="cc_score_2, rg_score_2" )

score = np.concatenate((cc_score, rg_score), axis=1)
np.savetxt("score.csv", (score), delimiter= ",", header ="cc_score, rg_score" )

composite_score = np.concatenate((cc_composite_score, rg_composite_score), axis=1)
np.savetxt("composite_score.csv", (composite_score), delimiter= ",", header ="cc_composite_score, rg_composite_score" )

glue_icebreaker = np.concatenate((cc_glue_icebreaker, rg_glue_icebreaker), axis=1)
np.savetxt("glue_icebreaker.csv", (glue_icebreaker), delimiter= ",", header ="cc_glue_icebreaker, rg_glue_icebreaker" )

alana_bot = np.concatenate((cc_alana_bot, rg_alana_bot), axis=1)
np.savetxt("alana_bot.csv", (alana_bot), delimiter= ",", header ="cc_alana_bot, rg_alana_bot" )

duration = np.concatenate((cc_duration, rg_duration), axis=1)
np.savetxt("duration.csv", (duration), delimiter= ",", header ="cc_duration, rg_duration" )

time_per_glue_turn = np.concatenate((cc_time_per_glue_turn, rg_time_per_glue_turn), axis=1)
np.savetxt("time_per_glue_turn.csv", (time_per_glue_turn), delimiter= ",", header ="cc_time_per_glue_turn, rg_time_per_glue_turn" )

coherence_metric_1 = np.concatenate((cc_coherence_metric_1, rg_coherence_metric_1), axis=1)
np.savetxt("coherence_metric_1.csv", (coherence_metric_1), delimiter= ",", header ="cc_coherence_metric_1, rg_coherence_metric_1" )

coherence_metric_2 = np.concatenate((cc_coherence_metric_2, rg_coherence_metric_2), axis=1)
np.savetxt("coherence_metric_2.csv", (coherence_metric_2), delimiter= ",", header ="cc_coherence_metric_2, rg_coherence_metric_2" )

coherence_metric_3 = np.concatenate((cc_coherence_metric_3, rg_coherence_metric_3), axis=1)
np.savetxt("coherence_metric_3.csv", (coherence_metric_3), delimiter= ",", header ="cc_coherence_metric_3, rg_coherence_metric_3" )

coherence_metric_3_percent = np.concatenate((cc_coherence_metric_3_percent, rg_coherence_metric_3_percent), axis=1)
np.savetxt("coherence_metric_3_percent.csv", (coherence_metric_3_percent), delimiter= ",", header ="cc_coherence_metric_3_percent, rg_coherence_metric_3_percent" )



# np.savetxt("turn_counter.csv", (rg_turn_counter.flatten(), cc_turn_counter.flatten()), delimiter= ",")

# numpy.savetxt("temp", a, fmt=fmt, header="SP,1,2,3", )

# df = pd.DataFrame({"name1" : rg_turn_counter.reshape(3,1), "name2" : cc_turn_counter.reshape(3,1)}, index=[1])
# df.to_csv("turn_counter.csv", index=False)
