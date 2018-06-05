import statistics
sample_list = [2,3,4,56,3,26,7,8,4,3,9,30,40]
sd = statistics.stdev(sample_list)
print("sd: ", sd)
mean_value = statistics.mean(sample_list)
print("mean: ", mean_value)
median_value = statistics.median(sample_list)
print("median: ", median_value)
print("variance: ", statistics.variance(sample_list))
