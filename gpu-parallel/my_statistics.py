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
gpu_2_stats = [(8, 204.5360100865364), (16, 105.8844422698021), (32, 61.94584774971008), (64, 33.31284034252167), (128, 18.470202684402466), (256, 11.345814824104309), (512, 8.333375930786133), (1024, 6.227170705795288), (2048, 5.430916965007782)]
rooftop_gpu_1_stats = [(512, 8.023683905601501), (1024, 6.045764267444611), (2048, 4.9635767340660095), (4096, 4.815049052238464), (8192, 4.663374602794647), (16384, 5.06444650888443), (32768, 5.068949043750763), (65536, 4.689917623996735), (131072, 4.184209525585175), (262144, 4.187199950218201), (524288, 4.173584878444672)]
rooftop_gpu_2_stats = [(512, 9.075098037719727), (1024, 6.190158247947693), (2048, 5.567627191543579), (4096, 5.800414502620697), (8192, 5.5308215618133545), (16384, 4.951357960700989), (32768, 4.750052452087402), (65536, 3.997591197490692), (131072, 4.032990992069244), (262144, 4.019867241382599), (524288, 4.016986191272736)]
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

plt.rcParams['font.size'] = 14
plt.figure(figsize=(20,12))

plt.plot(norm_batch_cpu_stats, speed_cpu_stats, label='CPU')
plt.plot(norm_batch_gpu_1_stats, speed_gpu_1_stats, label='1x GPU')
plt.plot(norm_batch_gpu_2_stats, speed_gpu_2_stats, label='2x GPU')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Speedup')
plt.title('Speedup')
plt.legend()

plt.savefig('speedup.png')
plt.show()

# Speedup

roof_speed_gpu_1_stats = [rooftop_gpu_1_stats[0][1]/y for _, y in rooftop_gpu_1_stats]
roof_speed_gpu_2_stats = [rooftop_gpu_2_stats[0][1]/y for _, y in rooftop_gpu_2_stats]
roof_norm_batch_gpu_1_stats = [math.log2(x) for x, _ in rooftop_gpu_1_stats]
roof_norm_batch_gpu_2_stats = [math.log2(x) for x, _ in rooftop_gpu_2_stats]

roof_cpu_stats = max(speed_cpu_stats)
roof_gpu_1_stats = max(roof_speed_gpu_1_stats)
roof_gpu_2_stats = max(roof_speed_gpu_2_stats)

plt.rcParams['font.size'] = 14
plt.figure(figsize=(20,12))

plt.plot(norm_batch_cpu_stats, speed_cpu_stats, label='CPU')
plt.plot(roof_norm_batch_gpu_1_stats, roof_speed_gpu_1_stats, label='1x GPU')
plt.plot(roof_norm_batch_gpu_2_stats, roof_speed_gpu_2_stats, label='2x GPU')
plt.axhline(y=roof_cpu_stats, color='blue', linestyle=':', label='CPU roof')
plt.axhline(y=roof_gpu_1_stats, color='orange', linestyle=':', label='1x GPU roof')
plt.axhline(y=roof_gpu_2_stats, color='green', linestyle=':', label='2x GPU roof')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Speedup')
plt.title('Rooftop based on speedup')
plt.legend()

plt.savefig('rooftop.png')
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

plt.rcParams['font.size'] = 14
plt.figure(figsize=(20,12))

plt.plot(norm_batch_cpu_stats, efficiency_cpu_results, label='CPU')
plt.plot(norm_batch_gpu_1_stats, efficiency_gpu_1_results, label='1x GPU')
plt.plot(norm_batch_gpu_2_stats, efficiency_gpu_2_results, label='2x GPU')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Efficiency')
plt.title('Efficiency')
plt.legend()

plt.savefig('efficiency.png')
plt.show()

# Serial Fraction

serial_cpu_results = [1 - (e / gpu) for e, gpu in zip(efficiency_cpu_results, norm_batch_cpu_stats)]
serial_gpu_1_results = [1 - (e / gpu) for e, gpu in zip(efficiency_gpu_1_results, norm_batch_gpu_1_stats)]
serial_gpu_2_results = [1 - (e / gpu) for e, gpu in zip(efficiency_gpu_2_results, norm_batch_gpu_2_stats)]

plt.rcParams['font.size'] = 14
plt.figure(figsize=(20,12))

plt.plot(norm_batch_cpu_stats, serial_cpu_results, label='CPU')
plt.plot(norm_batch_gpu_1_stats, serial_gpu_1_results, label='1x GPU')
plt.plot(norm_batch_gpu_2_stats, serial_gpu_2_results, label='2x GPU')

plt.xlabel('Batch size [2^batch_size]')
plt.ylabel('Serial Fraction')
plt.title('Serial Fraction')
plt.legend()

plt.savefig('serial_fraction.png')
plt.show()
