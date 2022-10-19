class Week:
    '''
    A class of weekdays, representing each day with a number
    '''
    def week_day(number):
        match number:
            case 1:
                print('It is Monday')
            case 2:
                print('It is Tuesday')
            case 3:
                print('It is Wednesday')
            case 4:
                print('It is Thursday')
            case 5:
                print('It is Friday')
            case 6:
                print('It is Saturday')
            case 7:
                print('It is Sunday')


try:
    user_input = int(input('Enter a number from 1 to 7: '))
    if user_input < 1 or user_input > 7:
        raise ValueError('There are only 7 Weekdays, starting at 1 !')
    week = Week
    week.week_day(user_input)
except ValueError as e:
    print(e)