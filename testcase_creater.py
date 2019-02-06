import os
import shutil
import zipfile
prefix=input('Please input the prefix of testcases:\n')
input_suffix=input('Please input the suffix of input file:\n')
output_suffix=input('Please input the suffix of output file:\n')
testcase_num=int(input('Please input the number of testcases:\n'))
work_dir=os.getcwd()
os.system(work_dir+'\\compile.bat')
def yes_or_no(marked_words):
    result=input(marked_words+' [yes/no]:')
    while True:
        if result=='y'or'yes':
            return True
        elif result=='n'or'no':
            return False
        else:
            result=input("Can't recognize your reesult,please input your result again.\n")
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for dir in dirs:
                filelist.append(os.path.join(root,dir))
            for name in files:
                filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()
for x in range(1,testcase_num+1):
    os.system(work_dir+'\\run_once.bat')
    src_input=work_dir+'\\testcase.in'
    dst_input=work_dir+'\\testcase\\{}{}.{}'.format(prefix,x,input_suffix)
    src_output=work_dir+'\\testcase.out'
    dst_output=work_dir+'\\testcase\\{}{}.{}'.format(prefix,x,output_suffix)
    shutil.move(src_input,dst_input)
    shutil.move(src_output,dst_output)
if yes_or_no('Do you want to create a zip file whitch contents the testcases?'):
    zip_filename=input("Please input the zip filename.(No suffix):\n")
    zip_dir(work_dir+'\\testcase',zip_filename+'.zip')
else:
    exit(0)
