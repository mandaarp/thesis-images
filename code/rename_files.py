import glob, os, sys

if len(sys.argv) < 3:
    print "usage: python " + sys.argv[0] + " PREFIX PATH"
    exit
else:
    rename(sys.argv[2], sys.argv[1])
def rename(path, prefix):
    g = glob.glob(os.path.join(path,"*.jpg")
    for i in range(len(g)):
        os.rename(g[i], prefix + str(i+1) + ".jpg")
