# coding=utf-8
import threading

import pyaudio
from datetime import datetime, time
import os

# coding=utf-8
##TODO обернуть в класс
from Recorder import Recorder

is_recording = False;
current_audio_file = []


def start_recording():
    global is_recording, current_audio_file
    is_recording = True;
    time_stamp = datetime.now()
    filename = time_stamp.strftime('%Y_%m_%d_%H_%M_%S') + ".wav"
    print ("Start recording")

    rec = Recorder(channels=2)
    current_audio_file = rec.open(filename, 'wb')
    current_audio_file.start_recording()
    threading.Timer(1, sound).start()


def sound():
    os.system('\a')
    print ("Sound")


def end_recording():
    global is_recording, current_audio_file
    is_recording = False;
    print ("Sound")
    os.system('\a')
    print ("Stop recording")
    current_audio_file.stop_recording()
    current_audio_file.close();


def user_handler():
    if (is_recording):
        end_recording();
    else:
        start_recording();
