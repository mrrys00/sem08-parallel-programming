"""
Statistics
"""

import matplotlib.pyplot as plt

results = [301.5283, 290.0063, 317.0638, 409.4627]
gpus_num=range(1,len(results)+1)

# GPUtime_[h] based on hpc-jobs-hisotory
cost_of_parallel_system = [0.34, 0.65, 1.07, 1.83]

base_time = results[0]
cost_of_serial_system = cost_of_parallel_system[0]

# Speedup

speedup_results = [base_time/i for i in results]
plt.plot(gpus_num, speedup_results)

plt.xlabel('GPUs number')
plt.ylabel('Speedup')
plt.title('Speedup')

plt.savefig('speedup.png')
plt.show()

# Normalized speedup

normalized_speedup_results = [(r/base_time)/(par/ cost_of_serial_system) for r, par in zip(results, cost_of_parallel_system)]
plt.plot(gpus_num, normalized_speedup_results)

plt.xlabel('GPUs number')
plt.ylabel('Normalized speedup')
plt.title('Normalized speedup')

plt.savefig('normalized_speedup.png')
plt.show()

# Efficiency

efficiency_results = [s/gpu for s, gpu in zip(speedup_results, gpus_num)]
plt.plot(gpus_num, efficiency_results)

plt.xlabel('GPUs number')
plt.ylabel('Efficiency')
plt.title('Efficiency')

plt.savefig('efficiency.png')
plt.show()

# Serial Fraction
serial_fraction = [1 - (e / gpu) for e, gpu in zip(efficiency_results, gpus_num)]
plt.plot(gpus_num, serial_fraction, label='Serial Fraction')

plt.xlabel('GPUs number')
plt.ylabel('Serial Fraction')
plt.title('Serial Fraction')

# plt.legend()
plt.savefig('speedup_serial_fraction.png')
plt.show()
