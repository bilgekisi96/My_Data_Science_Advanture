from scipy import stats


print(stats.binom.pmf(1,10,0.3))
print(stats.binom.cdf(7,10,0.5))
print(stats.binom.pmf(7,10,0.5))
print(1-stats.binom.cdf(7,10,0.5))