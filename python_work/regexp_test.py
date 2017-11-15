import re

def parse_fname(fname):
    "parse filename into dictionary of facets"

    pattern = (r"\\(?P<model>[^\\]+)" + 
               r"\\(?P<run>[^\\]+)" +
               r"\\(?P<version>[^\\]+)" +
               r"\\(?P<input>[^\\]+)")
               
    m = re.match(pattern, fname)
    if m == None:
        return None

    return m.groupdict()


if __name__ == '__main__':

    fname = r"\mymodel\myrun\myversion\thing"

    mydict = parse_fname(fname)

    print "Version is {}".format(mydict["version"])

