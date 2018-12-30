import os
import array
import binascii

#s = 'this is the array.'
#a = array.array('c', s)

#print 'As string:', s
#print 'As array :', a
#print a[1], a[2], a[3]

thread = os.fork()
if thread == 0:
    print ("this is in child processing...")
#    while True:
#        print ("pid = 0")

else:
    print ("this is in parent processing...")
    #while True:
#        print ("pid = " + str(pid))
