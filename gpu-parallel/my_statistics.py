"""
Statistics
"""

import math
import matplotlib.pyplot as plt

# results = [301.5283, 290.0063, 317.0638, 409.4627, 540.5675, 564.0306, 823.7327, 1083.4349]
# gpus_num=range(1,len(results)+1)

cpu_stats = [(8, 395.601097881794), (16, 304.63434541225433), (32, 284.1278433203697), (64, 254.52484291791916), (128, 253.47213745117188), (256, 260.5937339067459)]
# base_cpu_time = cpu_stats[0][1]
# cpu_stats_x = [i[0] for i in cpu_stats]
# cpu_stats_y = [i[1] for i in cpu_stats]
gpu_1_stats = [(8, 232.82304418087006), (16, 117.64689600467682), (32, 59.69391429424286), (64, 31.07266902923584), (128, 16.66574651002884), (256, 9.285167515277863), (512, 7.106492400169373), (1024, 5.886879861354828), (2048, 5.02317214012146)]
gpu_2_stats = [(8, 557.2692332863808), (16, 292.67795956134796), (32, 161.57144767045975), (64, 91.3252404332161), (128, 51.05502200126648), (256, 30.272819995880127), (512, 22.362390279769897), (1024, 16.31369298696518), (2048, 16.045155704021454)]
# gpu_2_stats_x = [i[0] for i in gpu_2_stats]
# gpu_2_stats_y = [i[1] for i in gpu_2_stats]

# GPUtime_[h] based on hpc-jobs-hisotory
# cost_of_parallel_system = [0.34, 0.65, 1.07, 1.83, 3.02, 3.79, 7.32, 9.71]

# base_time = results[0]
# cost_of_serial_system = cost_of_parallel_system[0]

# Speedup

speed_cpu_stats = [cpu_stats[0][1]/y for _, y in cpu_stats]
speed_gpu_1_stats = [gpu_1_stats[0][1]/y for _, y in gpu_1_stats]
speed_gpu_2_stats = [gpu_2_stats[0][1]/y for _, y in gpu_2_stats]
norm_batch_cpu_stats = [math.log2(x) for x, _ in cpu_stats]
norm_batch_gpu_1_stats = [math.log2(x) for x, _ in gpu_1_stats]
norm_batch_gpu_2_stats = [math.log2(x) for x, _ in gpu_2_stats]

plt.rcParams['font.size'] = 10
plt.plot(norm_batch_cpu_stats, speed_cpu_stats, label='CPU')
plt.plot(norm_batch_gpu_1_stats, speed_gpu_1_stats, label='1x GPU')
plt.plot(norm_batch_gpu_2_stats, speed_gpu_2_stats, label='2x GPU')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Speedup')
plt.title('Speedup')
plt.legend()

plt.savefig('speedup.png')
plt.show()

# Normalized speedup

# normalized_speedup_results = [(r/base_time)/(par/ cost_of_serial_system) for r, par in zip(results, cost_of_parallel_system)]
# plt.plot(gpus_num, normalized_speedup_results)

# plt.xlabel('Batch size')
# plt.ylabel('Normalized speedup')
# plt.title('Normalized speedup')

# plt.savefig('normalized_speedup.png')
# plt.show()

# Efficiency

efficiency_cpu_results = [s/gpu for s, gpu in zip(speed_cpu_stats, norm_batch_cpu_stats)]
efficiency_gpu_1_results = [s/gpu for s, gpu in zip(speed_gpu_1_stats, norm_batch_gpu_1_stats)]
efficiency_gpu_2_results = [s/gpu for s, gpu in zip(speed_gpu_2_stats, norm_batch_gpu_2_stats)]

plt.plot(norm_batch_cpu_stats, efficiency_cpu_results, label='CPU')
plt.plot(norm_batch_gpu_1_stats, efficiency_gpu_1_results, label='1x GPU')
plt.plot(norm_batch_gpu_2_stats, efficiency_gpu_2_results, label='2x GPU')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Efficiency')
plt.title('Efficiency')

plt.savefig('efficiency.png')
plt.show()

# Serial Fraction

serial_cpu_results = [1 - (e / gpu) for e, gpu in zip(efficiency_cpu_results, norm_batch_cpu_stats)]
serial_gpu_1_results = [1 - (e / gpu) for e, gpu in zip(efficiency_gpu_1_results, norm_batch_gpu_1_stats)]
serial_gpu_2_results = [1 - (e / gpu) for e, gpu in zip(efficiency_gpu_2_results, norm_batch_gpu_2_stats)]

plt.plot(norm_batch_cpu_stats, serial_cpu_results, label='CPU')
plt.plot(norm_batch_gpu_1_stats, serial_gpu_1_results, label='1x GPU')
plt.plot(norm_batch_gpu_2_stats, serial_gpu_2_results, label='2x GPU')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Serial Fraction')
plt.title('Serial Fraction')

# plt.legend()
plt.savefig('serial_fraction.png')
plt.show()
