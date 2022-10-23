# Write a program that analyzes the entered number and , depending on the number, gives
# the day of the week that corresponds to this number(1 is Monday, 2 is Tuesday, etc.). Take

# into account cases of entering numbers from 8 and more, as well as cases of entering non-
# numerical data.
import logging
logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


def define_day_week(day):
    day_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    try:
        user_day = int(day)
        if day <= 0 or day > 7:
            raise IndexError("Your number is out of range")
        if type(day) == float:
            raise Exception("Your number is a float type")
    except ValueError as ex:
        logging.exception(f'Value error.Info: {ex}')
    except IndexError as ex:
        logging.exception(f'Index error.Info: {ex}')
    except Exception as ex:
        logging.exception(f'Error Info: {ex}')
    else:
        print(day_week[user_day-1])
    finally:
        print("The 'try except' is finished")


define_day_week(56)
define_day_week('bhjjk')
define_day_week(7)
define_day_week(-1)
define_day_week(5.6)
