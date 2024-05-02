power_consume_10_sec:
	sudo cat /sys/devices/virtual/powercap/intel-rapl/intel-rapl\:0/energy_uj && sleep 10 && sudo cat /sys/devices/virtual/powercap/intel-rapl/intel-rapl\:0/energy_uj

run_docker:
	docker run -it --privileged -p 8888:8888 -v `pwd`:/jupyter/ eumaster4hpccyfronet/energy-aware-computing-mooc
