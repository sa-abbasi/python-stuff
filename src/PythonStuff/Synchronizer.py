

from collections import namedtuple
from pathlib import Path, PurePath
import os
import pathlib
import shutil
import filecmp
from collections import deque
import configparser
import logging
 

Entry = namedtuple ('Entry', {'Left','Right'})



class Synchronizer:
    """description of class"""
     

    def __init__(self, sourcePath, targetPath,log_file_path):
         
        self.source_path = sourcePath
        self.target_path = targetPath        
        self.file_stack= deque() 
        
       
        logging.basicConfig(filename=log_file_path, encoding='utf-8', level=logging.DEBUG,format='%(asctime)s|%(levelname)s|%(name)s|%(message)s')

        self.logger = logging.getLogger('Synchronizer')
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("******************starting_program*********************")

    def load_configuration(self, config_path):
            config = configparser.ConfigParser()
            config.read(config_path)

            self.source_path = config['SyncSetting']['source_path']
            self.target_path= config['SyncSetting']['target_path']

            self.logger.info(f"loaded source_path: {self.source_path} target_path: {self.target_path}")
            #config['SyncSetting'] = {'source_path': 'd:\src_test','target_path': 'd:\src_test2'}
            #with open('D:/repos/PythonLearning/configuration.ini', 'w') as configfile:
            #    config.write(configfile)
   
    def sync_root(self):
        self.file_stack.append(Entry(self.source_path,self.target_path))     

        try:
            while 1==1:
                current_item=self.file_stack.pop()
                self.que_sub_folders(current_item.Left,current_item.Right)#Push sub folders to stack
                self.logger.info(f"synchronizing source_path: {current_item.Left}")
                self.copy_files(current_item.Left,current_item.Right)            

        except IndexError as err:
            pass
            #print('deque error: '+str(err))

    def que_sub_folders(self,source_path,target_path):
         print('quering folders {0}->{1}'.format(source_path,target_path))
         self.logger.info(f"queuing sub-folders to process source_dir: {source_path}")

         f_path = pathlib.Path(source_path)
         for child in f_path.iterdir():
            print('trying to que {0}'.format(str(child)))
            if child.is_dir():
                print('have queued to que {0}'.format(str(child)))
                new_target_path=pathlib.Path(target_path).joinpath(child.name)
                self.file_stack.append(Entry(str(child), str(new_target_path)))# make sure left path goes as full path
                self.logger.info(f"stacked sub-folder source_dir: {str(child)}->{str(new_target_path)}")
                


    def copy_files2(self, source_path, target_path, target_folder):
        dirget_dir = Path(target_path).joinpath(target_folder)
        if not dirget_dir.exists():
            #tf.create()
            shutil.copytree(source_path.joinpath(target_folder), dirget_dir)
        else:    
            for sfile in source_path.iterdir():
                if not os.path.isfile(sfile):
                    continue
                target_file=dirget_dir.joinpath(sfile)
                sf=source_path.joinpath(sfile)            
                if not filecmp.cmp(sf, target_file, shallow=True):
                   cpy_result= shutil.copy(sf,target_file)
                   print('copied_file {0} to {1}'.format(sf,target_file))

    def copy_files(self, left_dir, right_dir):
     
        source_dir=pathlib.Path(left_dir)
        target_dir=pathlib.Path(right_dir)

        if not target_dir.exists():
             target_dir.mkdir()
             self.logger.debug(f"created target dir: {str(target_dir)}")
        
        self.logger.debug(f"copying files from {left_dir}->{right_dir}")
        for sfile in source_dir.iterdir():

            try:

                if not os.path.isfile(sfile):
                    continue
            
                target_file=target_dir.joinpath(sfile.name)

                source_file=source_dir.joinpath(sfile.name)  

                if not target_file.exists():
                    shutil.copy(source_file,target_file)
                    print('copied_file {0} to {1}'.format( str( source_file), str(target_file)))
                    self.logger.info(f"created target file: {str(target_file)}")
                else:
                    if not filecmp.cmp(source_file, target_file, shallow=True):
                        cpy_result= shutil.copy(source_file,target_file)
                        print('copied_file {0} to {1}'.format( str( source_file), str(target_file)))
                        self.logger.info(f"copied_file: {str(source_file)}")
                    else:
                        print('files {0} and {1} are same'.format( str(source_file), str(target_file)))
                        self.logger.info(f"files_are_same source: {str(source_file)} target: {str(target_file)}")

            except Exception as error:
    
                print(f"file_sync_error {str(sfile)}")
                self.logger.error(f"file_sync_error {str(sfile)}")
                self.logger.exception(error)
                #import sys
                #import traceback
                #traceback.print_exception(*sys.exc_info())



def main():

     src_dir="D:/src_test"
     target_dir="D:/src_test2"
     src_dir=""

     config_path='D:/repos/PythonLearning/configuration.ini'
     log_file_path='D:/repos/PythonLearning/file_sync_log.log'

     print('******Synchronizing folders*************')

     worker=Synchronizer(src_dir,target_dir,log_file_path)
     worker.load_configuration(config_path)
     worker.sync_root();

     print('******Synchronization work completed*************')


main()        
