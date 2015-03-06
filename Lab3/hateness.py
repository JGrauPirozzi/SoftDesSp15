""" How hated is ... now? by Jaime Grau """

""" User input for the hated thing. """

hated = raw_input("Please enter a name: ")
#print hated

""" Check the user input. """

chated = hated.replace("#", "")
chated = ''.join(('#',chated))
#print chated

""" Feedback to users. """

print "Sending you request please wait..."

""" Stream for hachtag of the hated thing. """

box = []
from pattern.web import *
s = Twitter().stream(hated)
for i in range(10):
    time.sleep(1)
    s.update(bytes=1024)
    box.append(s[-1].text if s else '')

""" Clean the output. """

nbox = ''.join(box)
remove = "@#"
for i in range(0,len(remove)):
	nbox = nbox.replace(remove[i],"")
#print nbox

""" Check the hateness. """

from pattern.en import *
hateness = sentiment(nbox)
#print hateness[0]
#print hateness[1]

""" Interpreting the hateness. """

if hateness[1] < 0.05:
	sys.exit("Try againg we couldn't get enough results.")

if hateness[0] > 0.5:
	print "The new jesus."
elif hateness[0] > 0.4:
	print "A jurk."
elif hateness[0] > 0.3:
	print "An ass hole."
elif hateness[0] <= 0.3:
	print "The devil in person."




