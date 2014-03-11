import sys
import os
import socket
# run this file to setup your environment and run the website

if 'ip-' in socket.gethostname():
    print 'ip!'
    python_scripts_dir = '/home/ubuntu/cs231a/src/python/'
    params_scripts_dir = '/home/ubuntu/data/non_root_df_41k/'
    matlab_scripts_dir = '/home/ubuntu/cs231a/src/matlab/'
elif '-mba' in socket.gethostname():
    print 'mba!'
    python_scripts_dir = '../cs231a/src/python/'
    params_scripts_dir = '../../Downloads/params/non_root_df_41k/'
    matlab_scripts_dir = '../cs231a/src/matlab/'
else:
    print 'local dir :/ ... guessing'
    python_scripts_dir = '../cs231a/src/python/'
    params_scripts_dir = '../../Downloads/params/non_root_df_41k/'
    matlab_scripts_dir = '../cs231a/src/matlab/'

sys.path.append(python_scripts_dir)
