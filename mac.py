
import uuid,re 

  
print ("The MAC address in formatted way is : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])) 

print ("The MAC address in formatted and less complex way is : ", end="") 
print (':'.join(re.findall('..', '%012x' % uuid.getnode()))) 