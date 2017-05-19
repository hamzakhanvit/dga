import gfapy

class gfa_parser(object):

     def __init__(self, filename):
         self.filename = filename
         
     
     def read_gfa_file(self):
         g = gfapy.Gfa.from_file(self.filename)
         for line in g.lines: 
             print(line)
         return 1          
