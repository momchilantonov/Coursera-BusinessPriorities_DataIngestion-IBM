import scipy.stats as stats


def geometric_distribution(p, k):
    '''
    INPUT: probability of success and trials
    OUTPUT: determined probability
    '''

    return stats.geom.cdf(k, p)


print(geometric_distribution(0.5, 20))
