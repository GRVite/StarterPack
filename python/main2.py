#!/usr/bin/env python

'''
	File name: main2.py
	Author: Guillaume Viejo
	Date created: 12/10/2017    
	Python Version: 3.5.2

This script will introduce you to the basics of neuroseries
It is the package used to handle spike time, epoch of wake/rem/sleep, etc
It is build on pandas
'''
import numpy as np
import pandas as pd
# the folder neuroseries should be in current directory 
# to check, you can type ls in ipython3 to list all the files and folders in your current directory
import neuroseries as nts

# let's create fake data for example the time of 10 spikes between 0 and 15 s
my_spike = np.random.uniform(0, 15, 10)
# let's sort them in ascending order of apparition 
my_spike = np.sort(my_spike)
# we can include them in a neuroserie object called a Ts (Time series)
my_spike = nts.Ts(my_spike, time_units = 's')
# DON'T FORGET THE time_units otherwise it will consider you have spikes in microseconds
# Observe your dataset
my_spike
# The first column indicates the timestamps in microseconds
# The second column is full of NaN (Not A Number) because it's just time stamps

# IF you have timestamps associated with a value for example 15 points of EEG each second
my_eeg = np.sin(np.arange(0, 15))
# You use a Tsd (Time series data)
my_eeg = nts.Tsd(t = np.arange(15), d = my_eeg, time_units = 's')
# Observe your variable 
my_eeg
# And how the software transform you timetamps in second in timestamps in microsecond

# Now if you are using a fancy probe and recording for example 3 channel at the same times
# You use a TsdFrame 
my_channels =  np.random.rand(15, 3)
my_channels = nts.TsdFrame(t = np.arange(15), d = my_channels, time_units = 's')

# If I want the data of my recording between second 5 to second 12
my_spike.as_units('s').loc[5:12]
my_eeg.as_units('s').loc[5:12]
my_channels.as_units('s').loc[5:12]
# Shoud be the same in millisecond
my_spike.as_units('ms').loc[5000:12000]
my_eeg.as_units('ms').loc[5000:12000]
my_channels.as_units('ms').loc[5000:12000]
# And in microseconds which is the default mode
my_spike.loc[5000000:12000000]
my_eeg.loc[5000000:12000000]
my_channels.loc[5000000:12000000]
# Dont miss a zero...


# Next we can define epoch of whatever you want
# For example the first and last 5 second are rem sleep, 5 to 10 s is wake
my_rem = nts.IntervalSet(start = [0, 10], end = [5, 15], time_units = 's')
my_wake = nts.IntervalSet(start = [5], end = [10], time_units = 's')
#Observe the different variables by typing them in the terminal
# What are the spike that occurs during rem sleep?
spike_during_rem = my_spike.restrict(my_rem)
# What is the value of the eeg during wake?
eeg_during wake = my_eeg.restrict(my_wake)
# What is the value of the channels during both wake and rem
wake_and_rem = my_wake.union(my_rem)
channels_wake_rem = my_channels.restrict(wake_and_rem)

# How to remove the first 2 second of the wake_and_rem interval :
to_remove = nts.IntervalSet(start = [0], end = [2], time_units = 's')
wake_and_rem = wake_and_rem.set_diff(to_remove)
