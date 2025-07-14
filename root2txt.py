import ROOT
from ROOT import TFile, TTree, vector

def root2txt(filename, treename, outfilename):
    f = TFile(filename)
    t = f.Get(treename)
    wf = vector['double'](0)
    t.SetBranchAddress('wf_i', wf)

    outfile = open(outfilename, 'w')
    for i in range(100):
        t.GetEntry(i)

        outfile.write(f"{i} ")
        for value in wf:
            outfile.write(f"{value:.6f} ")
        outfile.write("\n")

    f.Close()

if __name__ == '__main__':
    root2txt('source.root', 'sim', 'source.txt')