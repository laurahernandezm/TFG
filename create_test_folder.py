# -*- coding: utf-8 -*-
"""
Laura Hernández Muñoz - TFG

Create test folder to compute metrics
"""

import os
from os import path as osp
import shutil

#Tracking without bells and whistles test folder to compute metrics
root_wo_bnw = "./information/test/"
test_wo_bnw = "./test_wo_bnw/"

if not os.path.exists(test_wo_bnw):
    os.makedirs(test_wo_bnw)

for file in os.listdir(root_wo_bnw):
    if os.path.isfile(os.path.join(root_wo_bnw, file)) and file.endswith("filtered_trajectories_both.txt"):

        source = root_wo_bnw + file
        target = test_wo_bnw + file[0:6] + ".txt"

        shutil.copyfile(source, target)
