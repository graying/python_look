import array
import binascii

s = 'this is the array.'
a = array.array('c', s)

print 'As string:', s
print 'As array :', a
print a[1], a[2], a[3]
