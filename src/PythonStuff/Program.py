 

from importlib.resources import path
from ntpath import join
from pickle import FROZENSET
import CollectionTest as ct
from pathlib import Path
from pathlib import PurePath

import Synchronizer as sn
import os
import pathlib
import shutil
from collections import deque
from collections import namedtuple
from Calculator import Calculator



def main():     
     

    c=Calculator()
    c.Add(1,2)
    c.Add(1,2,3)
    c.PosCheck(x=3, y=35)
    c.CallRand()

   

   #s1='D:/src_test/2021april'
   #src_path = pathlib.Path(s1)
   #for child in src_path.iterdir():
   #     if os.path.isfile(child):
   #         print(join( child,' is file'))
   #     else:
   #         print(join( child,' is dir'))

    #p= pathlib.Path('d:\src_test')
    
    #worker=sn.Synchronizer("D:/src_test","D:/src_test2")
    #worker.sync_root();

    #p=10
    #q="hello world"
    

    #cc=ct.CollectionTest2(3.0,4.2)
    #cc.named_tuple_test();

    #print(cc.r)
    #print(cc.class_level_var)

    

    #c2=ct.CollectionTest2(5,6)
    #c2.class_level_var="Static val2"
    #print(c2.r)
    #print(c2.class_level_var)


    

    #set_work()

    #dict_work()

    #tuple_work2()
   
   # working_with_list()

   #  eq_is_test()

   #  boolean_test()

def set_work():
    print('working with sets')
    x1 = set(['and', 'python', 'data', 'structure'])
    print(x1)
    x2=set(['apple','banana','lemons','data'])
    print('set union')
    print(x1|x2)
    print(x1.union(x2))

    print(x1 & x2) #intersection of sets
    print('set difference')
    print (x1-x2)

    print('set xor')
    print (x1^x2)

    print('set symetric difference')
    print (x1.symmetric_difference(x2))

    print('set subset testing')
    print (x1<=(x2))

    fzset=frozenset(['and', 'python', 'data', 'structure'])
    print(fzset)



def dict_work():
    my_dict={
        '1': 'data',
        '2': 'structure',
        '3': 'python',
        '4': 'programming',
        '5': 'languag'
    }

    print(my_dict)
    print(list(my_dict.keys()))

    keyval=my_dict.pop('2')
    print(keyval)
    it=my_dict.popitem()
    print(it)

    d2={'a':'first letter','b':'second letter'}
    my_dict.update(d2);

    print(my_dict)




def tuple_work2():
    t1 = ("entry1", "entry2", "entry3")
   
    print(t1)
    print('tuple indexing')
    print (t1[0])
    print (t1[-2])

    print('tuple slicing')
    print(t1[1:])

    t2=t1+(1,2)
    print(t2)

    t3=(3,4)*3
    print(t3)

    print (3 in t3)

    for p in t2:
        print (p)

 
def working_with_list():
    a=[1,2,3,4]
    print(a)
    a+=[8,9]
    print(a)
    

def eq_is_test():

    fl=[]
    sl=fl

    if fl == sl:
        print ('fl is eq sl')
    else:
        print('fl is not eq sl')

    if fl is sl:
        print ('fl is really sl')
    else:
        print('fl is really not sl')

def boolean_test():
    a=10
    if not a:
        print ('a is false')
    else:
        print ('a is true')

main()

#C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\Scripts on path