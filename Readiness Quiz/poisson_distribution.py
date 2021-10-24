import scipy.stats as stats


def poisson_distribution(mu, k):
    '''
    INPUT: parameter of the poisson distribution and number of accidents
    OUTPUT: determined probability
    '''

    return stats.poisson.ppf(k, mu)


print(poisson_distribution(7, 0.5))
