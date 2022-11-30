def upper(st):
    return st.upper()

def asc(c):
    return ord(c)

def locate(st,c):
    for i,chr in enumerate(st):
        if chr == c:
            return i
    return -1

'''
1.Discard the characters up to and including the first dot.
2. Discard the characters including and to the right of the remaining leftmost dot.
3. Convert the characters to uppercase.
4. Add the ASCII values of the characters together
'''
def hash(sitename):
    i = locate(sitename,".")
    sitename = sitename[i+1:]
    i = locate(sitename,".")
    sitename = sitename[:i]
    sitename = upper(sitename)
    asci = 0
    for chr in sitename:
        asci += asc(chr)
    return asci

    
print(hash("www.ocr.org.uk"))
print(hash("www.foo.co.uk"))
#python hash.py