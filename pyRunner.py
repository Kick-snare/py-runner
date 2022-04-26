import subprocess as sp
import sys
import os
import shutil

base_dir = '/Users/yoojunhong/Desktop/assignment/'
file_list = sorted(os.listdir(base_dir))
assign_list = list(filter(lambda str : '컴퓨터및프로그래밍입문' in str, file_list))

print ("Select the directory to excute")

for i in range(len(assign_list)):
    print(i, '\t:', assign_list[i][42::])

curr_dir = base_dir

while True:
    try:
        curr_dir += assign_list[int(input('> '))]
        break
    except IndexError as e:
        print("Invalid Number!")

testcase = ['' for i in range(10)]
testcase[0] = '23\n48\n59\n2515'
testcase[1] = '2000'
testcase[2] = '2885'
# testcase[3] = ''
# testcase[4] = ''

if os.path.exists(curr_dir + "/_Results"): 
    shutil.rmtree(curr_dir + "/_Results")
os.makedirs(curr_dir + "/_Results")

dirNameList = list(filter(lambda str : str.endswith("assignsubmission_file_") , os.listdir(curr_dir)))

for dirName in dirNameList:
    if len(dirName) == 0 : continue
    studentName = dirName.split('-')[0]
    print("⇩ ", studentName)

    pyfiles = sorted(list(filter(lambda str : str.endswith(".py"), os.listdir(curr_dir + '/' + dirName))))
    flag = False

    for idx, fileName in enumerate(pyfiles):
        if len(fileName)==0: continue
        print(" >", fileName)
        flag = True

        with open(f'{curr_dir}/_Results/0{str(idx+1)}_{studentName}.txt', "w", encoding='utf-8') as result:
            filePath = f'{curr_dir}/{dirName}/{fileName}'
            
            result.write('\n######## OUTPUT ########\n\n')
            sp.run(["chmod", "a+x", filePath])
            out = sp.run(args=[sys.executable, filePath], text=True, capture_output=True, input=testcase[idx])
            result.write(out.stdout)

            pycode = open(filePath, 'r', encoding='utf-8')
            result.write('\n\n###### '+fileName+' ######\n\n')
            result.write(pycode.read())
            pycode.close()

    if(flag == False):
        wrong = open(f'{curr_dir}/_Results/ERR_{studentName}', "w", encoding='utf-8')
        wrong.close()
