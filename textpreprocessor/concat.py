import argparse

def run(paths_in, path_out):
    with open(path_out, "w") as f:
        for path_in in paths_in:
            for s in open(path_in):
                f.write("%s" % s)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=str, nargs="+", required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    paths_in = args.inputs
    path_out = args.output
    run(paths_in=paths_in, path_out=path_out)
