#Bitly code test 2014

#question 1 solution

def Text_Blocking(lst):
    """(list of strs)->list of strs
    
    takes a list of str and returns a list of str as if the given list were
    read as columns.
    
    REQUIRED: 
    -text will contain between 1 and 50 elements, inclusive.

    -Each element of text will contain between 1 and 50 characters, inclusive.

    -Each element of text will contain the same number of characters.

    -Each character in text will be an uppercase letter ([A-Z]).
    
    >>>Text_Blocking(["AAA",
    "BBB",
    "CCC"])
    ["ABC", "ABC", "ABC"]
    
    >>>Text_Blocking(["AAAAAAAAAAAAA"])
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
    """

    new_list = []
    length_of_first_element = len(lst[0])
    lst[0].split('\n') #split at newline
    for i in range(length_of_first_element):
        new_str = ""
        for j in lst:
            new_str += j[i]    
        new_list.append(new_str)
    return new_list

#question 2 Solution

class RaceAverage():
    
    def __init__(self):
        return None
    
    def avgMinutes(self, times):
        '''(self, list of str) -> int
        
        take a list of race times and return the average finish time.
        
        REQUIRED: 
        - times contains between 1 and 50 elements inclusive

        -each element of times is formatted as specified above, 
        with hh between 01 and 12 inclusive, mm between 00 and 59 inclusive, 
        and d between 1 and 99 inclusive

        -each element of times represents a time later than the start of the race.
        
        >>> x=RaceAverage()
        >>> x.avgMinutes(["12:00 PM, DAY 1", "12:01 PM, DAY 1"]
        241
        >>> x.avgMinutes(["12:00 AM, DAY 2"])
        960
        '''
        #create lists to hold values for minutes, days, ampm, hours, number of
        #racers and total minutes
        num_of_racers = len(times)
        total_minutes = 0
        hour = []
        minute = []
        days = []
        ampm = []
        for i in times:
            hour.append(i[0:2])
            minute.append(i[3:5])
            days.append(i[14:])
            ampm.append(i[6])
            
        #days
        for i in days:
            total_minutes += ((int(i)-1)*1440)
            
        #strip leading 0 from times
        for i in hour:
            if i in ['01','02','03','04','05','06','07','08','09']:
                i.strip('0')
        for i in minute:
            if i in ['01','02','03','04','05','06','07','08','09']:
                i.strip('0')
            
        #hours
        for i in range(len(hour)):
            if int(hour[i])<8 and ampm[i] == 'A':
                total_minutes += (int(hour[i])-8)*60
            elif int(hour[i])==12 and ampm[i]=='A':
                total_minutes-=8*60            
            elif int(hour[i])>8 and ampm[i] == 'A':
                total_minutes += (int(hour[i])-8)*60
            elif ampm[i]=='P':
                if int(hour[i])==12: 
                    total_minutes += 4*60
                else:
                    total_minutes += (int(hour[i])+4)*60
        #minutes
        for i in minute:
            total_minutes+=int(i)
            
        #Take Averages
        if (total_minutes/num_of_racers)-round(total_minutes/num_of_racers)==0.5:
            return int((total_minutes/num_of_racers)+.5)
        else:   
            return round(total_minutes/num_of_racers)