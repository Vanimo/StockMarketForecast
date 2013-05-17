'''
Created on 17 May 2013

@author: Floris
'''
import datetime

one = datetime.datetime.strptime("30-04-2013", "%d-%m-%Y")
print one
one = one + datetime.timedelta(days=1)
print one