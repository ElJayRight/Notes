local_28 = ['' for x in range(8)]
local_40 = ['' for x in range(8)]
local_38 = ['' for x in range(8)]
local_30 = ['' for x in range(8)]
local_48 = ['' for x in range(8)]
local_30[7]='p'
local_48[1]='T'
local_48[7]='k'
local_28[4]='d'
local_40[3]='4'
local_38[4]='e'
local_40[2]='_'
local_48[0]='H'
local_28[2]='r'
local_28[3]='3'
local_30[1]='_'
local_48[2]='B'
local_30[5]='r'
local_48[3]='{'
local_30[2]='b'
local_48[5]='r'
local_40[5]='4'
local_30[6]='3'
local_38[3]='v'
local_40[4]='p'
local_28[1]='1'
local_30[3]='3'
local_38[1]='n'
local_48[4]='b'
local_28[0]='4'
local_40[1]='n'
local_38[0]=','
local_40[0]='3'
local_48[6]='0'
local_38[7]='t'
local_40[7]='t'
local_30[0]='0'
local_40[6]='r'
local_28[5]='}'
local_38[5]='r'
local_38[6]='_'
local_38[2]='3'
local_30[4]='_'

flag = []
for i in [local_48,local_40,local_38,local_30,local_28]:
    flag.extend(i)
r = ''.join(flag)
print(r)