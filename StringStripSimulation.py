#! python27
# a function simulates string.strip()
# sfzhang 2016/07/01
import re,sys
def strip_simulation (strToStrip,strToSearch=None):
    if not strToSearch:
        return re.compile('(^(\n|\t| )*)|((\n|\t| )*$)').sub('',strToStrip)
    else:
        search_list = list(strToSearch)
        str_pattern = '|'.join(search_list)
        print str_pattern
        print r'^('+str_pattern+')*|('+str_pattern+')*$'
        return re.compile(r'^('+str_pattern+')*|('+str_pattern+')*$').sub('',strToStrip)

if __name__=="__main__":
    
	print "Usage :  reStrip.py targetString [Pattern]"
	if len(sys.argv[1:]) == 0:
	    print "At least one target string to strip"
	else:
	    print strip_simulation(sys.argv[1],sys.argv[2])

	

