import evaluation
from scipy.stats import shapiro
from scipy.stats import pearsonr
from scipy.stats import spearmanr


def check_data_distribution(data):
    stat, p = shapiro(data)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably Gaussian')
    else:
	    print('Probably not Gaussian')
    return p



def check_correlation(data_1, data_2):
    if check_data_distribution(data_1) > 0.05:
        stat, p = pearsonr(data_1, data_2)
        print('stat=%.3f, p=%.3f' % (stat, p2))
        if p > 0.05:
        	print('Probably independent')
        else:
        	print('Probably dependent')
    else:
        stat, p = spearmanr(data_1, data_2)
        print('stat=%.3f, p=%.3f' % (stat, p))
        if p > 0.05:
            print('Probably independent')
        else:
	        print('Probably dependent')
