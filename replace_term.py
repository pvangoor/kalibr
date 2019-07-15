import glob

def fix_file(fname, keyword, replacement):
    f = open(fname, 'r')
    lines = []
    flag = False
    for line in f.readlines():
        if keyword in line:
            flag = True
            line = line.replace(keyword, replacement)
        lines.append(line)
    f.close()

    f = open(fname, 'w')
    f.writelines(lines)
    f.close()

    if (flag):
        print(fname)


cpp_files = glob.glob("**/*.cpp", recursive=True)
hpp_files = glob.glob("**/*.hpp", recursive=True)
all_files = cpp_files + hpp_files

keyword = "cv::32F"
replacement = "CV_32F"


# fix_file('test.cpp', keyword, replacement)

for fname in all_files:
    fix_file(fname, keyword, replacement)