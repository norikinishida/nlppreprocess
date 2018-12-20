# -*- coding: utf-8 -*-

import argparse
import os

def run(path_in, path_out, filelist_name,
        name_begin, name_end, ext):
    filenames = os.listdir(path_in)
    if (name_begin is not None) and (name_end is not None):
        filenames = [n for n in filenames if n.startswith(name_begin) and n.endswith(name_end)]
    elif (name_begin is not None) and (name_end is None):
        filenames = [n for n in filenames if n.startswith(name_begin)]
    elif (name_begin is None) and (name_end is not None):
        filenames = [n for n in filenames if n.endswith(name_end)]
    filenames.sort()
    print("# of files=%d" % len(filenames))

    with open(os.path.join(path_out, filelist_name), "w") as f:
        print("Writing %s" % os.path.join(path_out, filelist_name))
        if ext is None:
            for filename in filenames:
                f.write("%s\n" % os.path.join(path_in, filename))
        else:
            if not ext.startswith("."):
                ext = "." + ext
            for filename in filenames:
                f.write("%s\t%s\n" % (os.path.join(path_in, filename),
                                      os.path.join(path_out, filename + ext)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--filelist_name", type=str, required=True)
    parser.add_argument("--begin", type=str, default=None)
    parser.add_argument("--end", type=str, default=None)
    parser.add_argument("--ext", type=str, default=None)
    args = parser.parse_args()

    path_in = args.input_dir
    path_out = args.output_dir
    filelist_name = args.filelist_name
    name_begin = args.begin
    name_end = args.end
    ext = args.ext
    run(path_in, path_out, filelist_name,
         name_begin, name_end, ext)
