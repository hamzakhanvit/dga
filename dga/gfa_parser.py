import gfapy

class gfa_parser(object):

     def __init__(self, filename):
         self.filename = filename
         
     
     def read_gfa_file(self):
         '''
         Reads a GFA file
         '''
         g = gfapy.Gfa.from_file(self.filename)

         #Print all lines in the GFA file
         #print ("\tAll lines:\n===================\n")
         #for line in g.lines: 
             #print(line)

         #print ("\tAll segments:\n===================\n")
         #Print all segments in the GFA file
         #for line in g.segments:
         #    print(line)
         

         #print ("\tAll fragments:\n===================\n")
         #Print all segments in the GFA file
         #for line in g.fragments:
         #    print(line)

         print ("\tAll edges:\n===================\n")
         #Print all edges in the GFA file
         print(g.edges) 

         return 1          
    
