from pyhooked import Hook, KeyboardEvent, MouseEvent
import time

from audio_notes_recorder import user_handler, start_recording, end_recording

was_up_before = True;

def handle_events(args):
    global was_up_before
    #print (args.current_key)
    if isinstance(args, KeyboardEvent):
        if args.current_key == 'Capital' and args.event_type == 'key down' and was_up_before:
            was_up_before = False
            start_recording()

        if args.current_key == 'Capital' and args.event_type == 'key up':
            was_up_before = True
            time.sleep(0.2)
            end_recording()

if __name__ == "__main__":
    hk = Hook()  # make a new instance of PyHooked
    hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
    hk.hook()  # hook into the events, and listen to the presses