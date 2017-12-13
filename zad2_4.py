from multiprocessing import Pool
from collections import Counter
import glob

def build_histogram(filepath):
 
  
    hist = Counter()
    with open(filepath) as f:
        for line in f:
            hist[line.strip()] += 1
    return hist


def main():
  
    datafile_paths = glob.glob("test24*.txt")

    pool = Pool(processes=3)
    histograms = pool.map(build_histogram, datafile_paths)

    pool.close()
    pool.join()

    merged_hist = histograms[0]
    for h in histograms[1:]:
        merged_hist.update(h)

    for word, count in merged_hist.items():
        print("%s: %s" % (word, count))


if __name__ == "__main__":
    main()