# Aluno: Victor Cora Colombo
# RA: 727356

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
seq_file = dir_path + "/sequential.py"
paral_file = dir_path + "/parallel.py"

print("RUNNING: time python %s 50000" % (seq_file))
os.system("time python %s 50000" % (seq_file))

print("\n\n\n\nRUNNING: time python %s 10000000" % (seq_file))
os.system("time python %s 10000000" % (seq_file))

print("\n\n\n\nRUNNING: time mpiexec -n 4 python %s 50000" % (paral_file))
os.system("time mpiexec -n 4 python %s 50000" % (paral_file))

print("\n\n\n\nRUNNING: time mpiexec -n 4 python %s 10000000" % (paral_file))
os.system("time mpiexec -n 4 python %s 10000000" % (paral_file))
