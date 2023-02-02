rom __future__ import print_function
import sys
import textwrap

def cowsay(str, length=40):
    return build_bubble(str, length) + build_owl()

def build_owl():
    return """
		 o
		  o
		   ___
		  (o o)
		 (  V  )
		/--m-m-
    """

def build_bubble(str, length=40):
    bubble = []

    lines = normalize_text(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalize_text(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]

    elif index == 0:
        return [ "/", "\\\\" ]
    
    elif index == len(lines) - 1:
        return [ "\\\\", "/" ]
    
    else:
        return [ "|", "|" ]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Usage: '%s string'" % sys.argv[0])
        sys.exit(0)

    print (cowsay(sys.argv[1]))