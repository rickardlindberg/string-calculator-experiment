def describe_string_calulator():

    # Empty string returns 0

    calculating(""              , gives("0"))

    # Single numbers returned as is

    calculating("1"             , gives("1"))
    calculating("2"             , gives("2"))

    # Sums numbers separated by comma

    calculating("1,2"           , gives("3"))
    calculating("3,4,5"         , gives("12"))

    # Sums numbers separated by newline

    calculating("1\n2"          , gives("3"))
    calculating("3\n4\n5"       , gives("12"))

    # Sums numbers separated by custom delimiter
    # Pattern is "//[one char delimiter]\n[rest of input]

    calculating("//;\n3;4;5"    , gives("12"))

    # Sums numbers separated by mixed delimiters

    calculating("3,4\n5"        , gives("12"))
    calculating("//;\n3,4\n5;6" , gives("18"))

# ----------------------------------------------------------
#                 code to make specs execute
# ----------------------------------------------------------

from subprocess import Popen, PIPE
import sys

def calculating(in_str, expected_out):
    check_spec(in_str, expected_out)

def gives(x):
    return x

def check_spec(in_str, expected_out):
    p = Popen(sys.argv[1:], stdin=PIPE, stdout=PIPE)
    out = p.communicate(in_str)[0]
    if out == expected_out:
        print "OK"
    else:
        print "FAIL: Expected '%s' to give '%s' but got '%s'" % (in_str, expected_out, out)

describe_string_calulator()
