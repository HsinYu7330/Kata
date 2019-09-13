'''
Human Readable Time

convert integer to HH:MM:SS
HH: range 00-99
MM: range 00-59
SS: range 00-59
'''

def make_readable(seconds):
    
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)