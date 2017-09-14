""" """
class Hotel:
     """ """
	 def __init__(self):
	     self.l = []

     def checkIn(self, name):
         """ """
         self.l.append(name)
         
     def checkOut(self, name):
         """ """
         self.l.pop(self.l.index(name))
         
     def display(self):
          """ """
          return self.l