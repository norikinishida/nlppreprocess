import argparse
import os

def main(args):
    path_indir = args.input

    filenames = os.listdir(path_indir)
    filenames = [n for n in filenames if n.startswith("raw_") and n.endswith(".txt")]
    filenames.sort()

    with open("./filelist.txt", "w") as f:
        for filename in filenames:
            f.write("%s\n" % os.path.join(path_indir, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    args = parser.parse_args()
    main(args)
