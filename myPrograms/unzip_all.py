#!/usr/bin/python
# by sfzhang 2016.12.27
import os
import sys
import zipfile
import tarfile
import re
import gzip
import bz2
import shutil


def unzip_all(input_dir, output_dir=None):
    """ recursively extract all compressed files in a directory to
        another directory
        support type: .bz2, .gz, .zip, .tgz, .tbz
    """
    abs_input_dir = os.path.abspath(input_dir)
    tgz_pattern = re.compile(r"\.tgz|\.tar\.gz")
    tbz2_pattern = re.compile(r"\.tbz|\.tar.bz2")
    gz_pattern = re.compile(r"\.gz")
    bz2_pattern = re.compile(r"\.bz2")
    if output_dir is not None:
        abs_output_dir = os.path.abspath(output_dir)
    else:
        abs_output_dir = os.getcwd()
    if os.path.isdir(abs_input_dir) & os.path.exists(abs_input_dir):
        for path, dirs, files in os.walk(input_dir):
            for file in files:
                file_abspath = os.path.join(path, file)
                if zipfile.is_zipfile(file):
                    opener, mode = zipfile.ZipFile, "r"
                elif re.search(tgz_pattern, file):
                    opener, mode = tarfile.open, "r:gz"
                elif re.search(tbz2_pattern, file):
                    opener, mode = tarfile.open, "r:bz2"
                elif re.search(gz_pattern, file):
                    # you can also use file[:-3] instead of file.replace(....)
                    ungzip_file = os.path.join(abs_output_dir, file.replace(".gz", ""))
                    with gzip.open(file_abspath, "rb") as f_in, gzip.open(ungzip_file, "wb") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    print("{:.<140}{:.>25}".format(file_abspath, "\033[33m【Done!】\033[0m"))
                    continue
                elif re.search(bz2_pattern, file):
                    unbz2_file = os.path.join(abs_output_dir, file.replace(".bz2", ""))
                    with open(file_abspath, "rb") as f_in, open(unbz2_file, "wb") as f_out:
                        f_out.write(bz2.decompress(f_in.read()))
                    print("{:.<140}{:.>25}".format(file_abspath, "\033[33m【Done!】\033[0m"))
                    continue
                else:
                    continue
                with opener(file_abspath, mode) as fobj:
                    if os.path.exists(abs_output_dir):
                        fobj.extractall(abs_output_dir)
                    else:
                        try:
                            os.makedirs(abs_output_dir)
                        except:
                            sys.stdout.write("Operation Failed! \
                                                unable to Create %s" % abs_output_dir)
                        else:
                            fobj.extractall(abs_output_dir)
                print("{:.<140}{:.>25}".format(file_abspath, "\033[33m【Done!】\033[0m"))

    else:
        sys.stdout.write("%s is not a valid directory!" % input_dir)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stdout.write("Please indicate a directory where you want to start from!\n")
    unzip_all("C:\\Users\\Admin\\Desktop\\datasets", "c:\\cygwin64\\home\\Admin\\dataset")
