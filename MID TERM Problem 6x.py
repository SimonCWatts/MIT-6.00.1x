
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            #PLACE A LINE OF CODE HERE
            return s2[len(s1):]
        if s2 == '':
            #PLACE A LINE OF CODE HERE
            return s1[len(s2):]
        else:
            #PLACE A LINE OF CODE HERE
            return s1[0] + helpLaceStrings(s2, s1[1:], out)
    
    return helpLaceStrings(s1, s2, '')
    


s1 = 'abc'
s2 = '123'

print('string1:', s1, '\nstring2:', s2, '\nlaced:', laceStringsRecur(s1, s2))