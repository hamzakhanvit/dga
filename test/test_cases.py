import dga, pkg_resources

def test_gfa_parser():
     inputfile =  pkg_resources.resource_filename('dga', 'data/test-contigs-gfa')
     f = dga.gfa_parser(inputfile)   
     success = f.read_gfa_file() 
     assert success == 1
