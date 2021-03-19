import evaluation
from scipy.stats import shapiro, pearsonr, spearmanr
from scipy.stats import ttest_rel, wilcoxon
from scipy.stats import ttest_ind, mannwhitneyu


def check_data_distribution(data):
    stat, p = shapiro(data)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Data is normally distributed and therefore parametric tests will be used for analysis.')
    else:
	    print('Data is not normally distributed and therefore non-parametric tests will be used for analysis.')
    return p


def check_correlation(data_1, data_2):
    if check_data_distribution(data_1) > 0.05:
        stat, p = pearsonr(data_1, data_2)
    else:
        stat, p = spearmanr(data_1, data_2)
    print('stat=%.3f, p=%.3f' % (stat, p2))
    if p > 0.05:
        print('No correlation.')
    else:
        print('Correlation detected!')


def check_UX_statistical_significance(data_1, data_2):
    if check_data_distribution(data_1) > 0.05:
        stat, p = ttest_ind(data_1, data_2)
    else:
        stat, p = wilcoxon(data_1, data_2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('No statistical difference between samples.')
    else:
        print('Samples are statistically different from each other.')



def check_icebreaker_statistical_significance(data_1, data_2):
    if check_data_distribution(data_1) > 0.05:
        stat, p = ttest_ind(data_1, data_2)
    else:
        stat, p = mannwhitneyu(data_1, data_2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
	    print('No statistical difference between samples.')
    else:
	    print('Samples are statistically different from each other.')
