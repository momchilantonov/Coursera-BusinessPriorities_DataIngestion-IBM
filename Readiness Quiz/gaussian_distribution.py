import scipy.stats as stats


def gaussian_distribution(loc_val, scale_val, cdf_val):
    '''
    INPUT: loc (mean of the distribution), scale (standard deviation of the distribution), and cdf values
    OUTPUT: determined probability
    '''

    return stats.norm.cdf(loc_val, scale_val, cdf_val)


print(gaussian_distribution(50, 20, 80))
