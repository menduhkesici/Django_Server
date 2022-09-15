from message_box import *
from datetime import datetime
import time
import json
import shutil
import os.path

# system data is saved to 'database/system_data.json' file
# commands are read from 'database/command.txt' file

SHOW_MESSAGE_BOX: bool = True
WAITING_PERIOD: int = 1     # waiting period of message box in seconds


def main():
    first_time = True
    while True:
        while True:
            try:
                if not os.path.isdir('./database'):
                    os.mkdir('./database')
                break
            except PermissionError:
                pass

        while True:
            try:
                with open('./database/command.txt', 'w') as command_file:
                    command_file.write('')
                break
            except PermissionError:
                pass

        if os.path.exists('./database/system_data.json'):
            with open('./database/system_data.json') as json_file:
                system_data = json.load(json_file)
        else:
            system_data = dict(last_update=str(datetime.now().strftime("%Y/%m/%d %H:%M:%S")),
                               logbook=[])
            with open('./database/system_data.json', 'w') as outfile:
                json.dump(system_data, outfile, sort_keys=True, indent=4, separators=(',', ': '))

        str_time_logbook = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        if first_time:
            first_time = False
            print(str_time_logbook, ": ", "System is started.")
            if SHOW_MESSAGE_BOX:
                message_box(message="System is started.", time=WAITING_PERIOD)
        else:
            print(str_time_logbook, ": ", "System is reset.")
            if SHOW_MESSAGE_BOX:
                message_box(message="System is reset.", time=WAITING_PERIOD)

        system_data['logbook'].append({
            'Message': "System is started.",
            'Time': str_time_logbook
        })

        while True:
            message = None
            str_time_logbook = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            # check command.txt file
            if os.path.exists('./database/command.txt'):
                with open('./database/command.txt') as f:
                    command = f.readline()
            else:
                command = ''

            # execute the corresponding command
            if len(command) > 0:
                while True:
                    try:
                        with open('./database/command.txt', 'w') as f:
                            f.write('')
                        break
                    except PermissionError:
                        pass
                if command.startswith('f1'):
                    message = "Form 1 filled. " + command[3:]
                elif command.startswith('f2'):
                    message = "Form 2 filled. " + command[3:]
                elif command.startswith('1'):
                    message = "Button 1 pressed."
                elif command.startswith('2'):
                    message = "Button 2 pressed."
                elif command.startswith('3'):
                    message = "Button 3 pressed."
                elif command.startswith('r'):
                    while True:
                        try:
                            if os.path.isdir('./database') and len(os.listdir('./database')) > 1:
                                shutil.rmtree('./database')
                            break
                        except PermissionError:
                            pass
                    break
                else:
                    message = "Unknown command received."
                system_data['logbook'].append({
                    'Message': message,
                    'Time': str_time_logbook
                })

            system_data['last_update'] = str_time_logbook

            # generate .json files
            with open('./database/system_data.json', 'w') as outfile:
                json.dump(system_data, outfile, sort_keys=True, indent=4, separators=(',', ': '))

            # generate info message
            if message is not None:
                print(str_time_logbook, ": ", message)
                if SHOW_MESSAGE_BOX:
                    message_box(message=message, message_x='Status update', time=WAITING_PERIOD)

            time.sleep(0.1)


if __name__ == '__main__':
    main()
