# Pupil Middleman Server with MATLAB support

## Contents
* Simple python wrapper function for communicating with pupil_capture and external stimulus presentation programs that do not support zeromq, such as MATLAB.
* Examples for pupil_capture control using MATLAB and PTB3
* Potentially useful MATLAB support functions.

This repository also contains examples for pupil_capture control using MATLAB and Psychtoolbox 3, as and some other (potentially) useful MATLAB support scripts. 

## What does it do?
Provides a simple solution to allow programs such as MATLAB to communicate with pupil_capture.
Enables external programs to connect via udp listening socket and converts bytes received from the socket into "annotations" (pupil-labs's name for events/triggers) to be sent to pupil_capture.
Generates basic logs for debugging purposes.

## Some warnings
This is a barebones middleman server that is fit for our use cases, not necessarily optimal for yours. Further, the implementtion here is outdated beyond pupil services 1.8-26, and it won't work with the newer rollouts. We will update this in the future when we have to deploy these hardware in our labs again. Pupil also provide native matlab support now, so if you're only needing that, you no longer require this tool.

UDP sockets can be unreliable (https://www.wikiwand.com/en/Reliability_(computer_networking)), although pilot testing to date suggests that it is possible to create a stable and consistent connection).
Finally, there is no real implementation of time and jitter compensation/calibration. There is a Time-Sync module by Pupil Labs for this, which I will implement in the future.

## Getting Started
You may need to modify the IP addresses/ports in 'sample_mm.py'
Simply run 'sample_mm.py' in terminal to start the middleman server. 

## Running the middleman
The middleman will run up to a certain point, based on whether you have pupil-recorder on or not. You may also want to ping the middleman with some integers. For this, there is a sample trigger dictionary. I may conver this to an if tree later if mixed-cases become a thing. 

## TODO
* Implement an actual exit method
* Time-sync implementation for compatibility with Pupil Labs' system.
* Completion of TCP ports through either multi-threading or non-blocking implementation. 
* Better log file generation 
* Modify 'sample_mm.py' to allow for interactive control i.e. stream eye-tracker data directly to a UDP socket, to allow for gaze-contingent eye-tracking etc. (TOM)
* Enable interactive calibration via MATLAB/PTB3 (Tom)

## Acknowledgments
* mtaung wrote the python scripts, tombullock wrote the MATLAB scripts.
* This code draws heavily from Pupil Labs' [pupil-helpers](https://github.com/pupil-labs/pupil-helpers) repository. 

