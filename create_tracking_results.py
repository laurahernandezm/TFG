# -*- coding: utf-8 -*-
"""
Laura Hernández Muñoz - TFG

Copy results to ./tracking_results/
"""

import os
from os import path as osp
import shutil

#Tracking without bells and whistles output folder
source_wo_bnw = "./tracking_wo_bnw/output/tracktor/Peds1/Tracktor++/"
target_wo_bnw = "./tracking_results/"
target_wo_bnw_train = "./tracking_results/train/"
target_wo_bnw_test = "./tracking_results/test/"

if not os.path.exists(target_wo_bnw):
    os.makedirs(target_wo_bnw)

if not os.path.exists(target_wo_bnw_train):
    os.makedirs(target_wo_bnw_train)

    if not os.path.exists(target_wo_bnw_test):
        os.makedirs(target_wo_bnw_test)

for file in os.listdir(source_wo_bnw):
    if os.path.isfile(os.path.join(source_wo_bnw, file)) and file.endswith(".txt"):

      source = source_wo_bnw + file

      target = ""

      if (file[1] == "r"):

        target = target_wo_bnw_train + file

      elif (file[1] == "e"):

        target = target_wo_bnw_test + file

      shutil.copyfile(source, target)
