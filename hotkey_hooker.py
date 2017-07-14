from pyhooked import Hook, KeyboardEvent, MouseEvent

from audio_notes_recorder import user_handler


def handle_events(args):
    ##print (args)
    if isinstance(args, KeyboardEvent):
        if args.current_key == 'Space' and args.event_type == 'key up' and 'Lcontrol' in args.pressed_key:
            user_handler()


    if isinstance(args, MouseEvent):
        if args.mouse_x == 300 and args.mouse_y == 400:
            print("Mouse is at (300,400")

if __name__ == "__main__":
    hk = Hook()  # make a new instance of PyHooked
    hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
    hk.hook()  # hook into the events, and listen to the presses