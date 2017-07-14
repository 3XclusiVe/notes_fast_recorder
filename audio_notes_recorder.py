# coding=utf-8
##TODO обернуть в класс
is_recording = False;

def start_recording():
    global is_recording
    is_recording = True;
    print ("Sound")
    print ("Start recording")


def end_recording():
    global is_recording
    is_recording = False;
    print ("Sound")
    print ("Stop recording")


def user_handler():
    if(is_recording):
        end_recording();
    else:
        start_recording();

