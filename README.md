# Pupil Middleman
Simple python wrapper for communicating with pupil and external programmes that do not support zeromq. It is very imperfect but I hope it helps people that are struggling to get their Pupil trackers live.

## What does it do?
Frankly, nothing illuminating. I wrote this as a simple solution to a problem I've been having using systems that do not support zeromq natively. 
This middleman will allow for connections to any various sockets on other programs and will convert bytes received from said sockets into annotations (triggers) to be sent to pupil-recorder.
There is also basic logging to try and debug anything that may go wrong during a session. 
The code is object oriented and hopefully easy to parse and understand. I have done my best to comment it as necessary. If there are problems with this, please do contact me. 

## Some warnings
First, this was an excercise on my part to better understand the pupil communications system and python in general. I am not comprehensively confident in my abilities with python, and you should take this as a foreword of how things may go wrong with this module. 

As of right now, the middleman only works with UDP sockets. These are [unreliable](https://www.wikiwand.com/en/Reliability_(computer_networking)) and should be used with caution. I am not responsible for how you deploy these in your work, and have done my best to detail the limitations of this module. 

Finally, there is no real implementation of time and jitter compensation/calibration. There is a Time-Sync module by Pupil Labs for this, which I will implement in the future.

## Getting Started

Everything here is very simple and should work out of the box. 
Simply run the sample_server.py script to demo how the middleman works. 

## Running the middleman

The middleman will run up to a certain point, based on whether you have pupil-recorder on or not. You may also want to ping the middleman with some integers. For this, there is a sample trigger dictionary. I may conver this to an if tree later if mixed-cases become a thing. 

## TODO

* Implement an actual exit method
* Time-sync implementation for compatibility with Pupil Labs' system.
* Completion of TCP ports through either multi-threading or non-blocking implementation. 
* Better log file generation 
## Acknowledgments

* Most of this code is based on a series of helper scripts from Pupil Labs' [pupil-helpers](https://github.com/pupil-labs/pupil-helpers) repository. 

