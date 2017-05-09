#!/usr/bin/env
# by sfzhang 2016.11.11

import optparse
import sys
import os


def parser():

    info = 'Usage: %s [Options]' % sys.argv[0]
    desc = 'A python script using optparse module'
    prog_name = 'whatever'

    parser = optparse.OptionParser(usage=info, description=desc, prog=prog_name)

    parser.add_option('-c', action='store', dest='text')
    parser.add_option('--content', action='store', dest='text')
    parser.add_option('-o', action='store', dest='outputfile')
    parser.add_option('--output', action='store', dest='outputfile')
    parser.add_option('-d', action='store_true', dest='debug')
    parser.add_option('--debug', action='store_true', dest='debug')

    parser.set_defaults(debug=False)


def parser_test():

    opt, args = parser.parse_args()
    print('opt: %s, args: %s' % (opt, args))
    if all([opt.text, opt.outputfile]):
        outfile = opt.outputfile
        debug_flag = opt.debug
        text_to_write = opt.text.strip("'")  # avoid quote content twice
        with open(outfile, 'w') as f:
            f.write(text_to_write)
    else:
        print('Usage: %s' % os.path.basename(sys.argv[0]))
        print('-h/--help     help')
        print('-c/--content= content to write to the target file')
        print('-d/--debug    execute command in debug mode')
        print('-o/--output=  target file to write')
        raise SystemExit(1)

if __name__ == "__main__":
    parser_test()







