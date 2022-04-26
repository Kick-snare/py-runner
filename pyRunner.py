import subprocess as sp
import sys
import os
import shutil
 
testcase = ['' for i in range(10)]
testcase[0] = '홍유준\n부산광역시 연제구 연산2동\n123\n1234'
testcase[1] = '48\n5\n120'
# testcase[2] = ''
# testcase[3] = ''
# testcase[4] = ''

if os.path.exists("_Results"):
    shutil.rmtree("_Results")
os.makedirs("_Results")

dirs = sp.run(args=['ls -d *assignsubmission_file_/'], shell=True, text=True, capture_output=True, encoding='utf-8')
dirNameList = dirs.stdout.split('\n')

for dirName in dirNameList:
    if len(dirName) == 0 : continue
    studentName = dirName.split('-')[0]
    print("⇩ ", studentName)

    pyfiles = sp.run(args=['ls '+ dirName.replace(' ', '\ ') + '*.py'], shell=True, text=True, capture_output=True, encoding='utf-8') \
                .stdout  \
                .strip() \
                .split('\n') \

    flag = False

    for idx, fileName in enumerate(pyfiles):
        if len(fileName)==0:
            continue
        print(" >", fileName.split('/')[1])
        flag = True
 
        with open('./_Results/0'+str(idx+1)+'_'+studentName+'.txt', "a", encoding='utf-8') as result:
            result.write('\n######## OUTPUT ########\n\n')
            sp.run(["chmod", "a+x", fileName])
            out = sp.run(args=[sys.executable, fileName], text=True, capture_output=True, input=testcase[idx])
            result.write(out.stdout)

            pycode = open('./' +fileName, 'r', encoding='utf-8')
            result.write('\n\n###### '+fileName.split('/')[1]+' ######\n\n')
            result.write(pycode.read())
            pycode.close()
        result.close()
    print()

    if(flag == False):
        wrong = open('./_Results/ERR_'+studentName, "w", encoding='utf-8')
        wrong.close()
