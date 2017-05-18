from dga import gfa_parser

def test_gfa_parser():
     inputfile = '/.mounts/labs/simpsonlab/users/h2khan/projects/proj1-diploid-assembly/canu-runs/yeast/sk1/sk1-auto/test.contigs.gfa'
     f = gfa_parser(inputfile)
     assert f.read_gfa_file() == 1
