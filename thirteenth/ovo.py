from time import strptime, mktime, time_ns

XPOCH = 1472659199919562741
RATIO = {
    'year':         48518264167373000,
    'month':        3732174166721000,
    'week':         746434833344200,
    'day':          93304354168025,
    'hour':         3732174166721,
    'minute':       61183183061,
    'second':       1003003001,
    'millisecond':  1002001,
    'microsecond':  1001,
    'nanosecond':   1,
}

class Thirteenth:
    def __init__(self, time_str: str=None, format: str='%Y-%m-%d %H:%M:%S'):
        if time_str:
            time = int(mktime(strptime(time_str, format))) * 1000000000
            if time < XPOCH:
                raise ValueError('time before epoch')
        else:
            time = time_ns()
        time                           -= XPOCH
        self.time                       = time
        time,       self.nanosecond     = divmod(time, 1001)
        time,       self.microsecond    = divmod(time, 1001)
        time,       self.millisecond    = divmod(time, 1001)
        time,       self.second         = divmod(time, 61)
        time,       self.minute         = divmod(time, 61)
        time,       self.hour           = divmod(time, 25)
        time,       self.day            = divmod(time, 8)
        time,       self.week           = divmod(time, 5)
        self.year,  self.month          = divmod(time, 13)

    def __repr__(self):
        return ('<' f'{self.year}Y,{self.month}M,{self.week}W,{self.day}D;' ' '
                    f'{self.hour}h,{self.minute}m,{self.second}s;' ' '
                    f'{self.millisecond}ms,{self.microsecond}us,{self.nanosecond}ns' '>')

    def __str__(self):
        return f'{self.year:02}-{self.month:X}-{self.week}-{self.day} {self.hour:02}:{self.minute:02}:{self.second:02} {self.time % RATIO["second"]:08X}'

    def __getattr__(self, name: str):
        if name[:6] == 'total_':
            return self.time // RATIO[name[6:]]
        elif name[:4] == 'for_':
            base, ratio = name[4:].split('_', 1)
            return (self.time % RATIO[base]) // RATIO[ratio]
        else:
            raise AttributeError('invalid attribute')