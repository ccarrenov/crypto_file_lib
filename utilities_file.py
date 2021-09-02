#!/usr/bin/env python
#IMPORT OS LIB FOR OPERATION SYSTEM
import os
#IMPORT SHUTIL LIB FOR OPERATION FILE AND COLLECTION OF FILE
import shutil
#IMPORT TRACEBACK LIB FOR PRINT ERROR
import traceback

class Files():

    def file_to_lines_utf8(self, fullpathfile):
        return self.file_to_lines(fullpathfile, 'utf-8')

    def file_to_lines(self, fullpathfile, encoding):
        try:
            origin = open(fullpathfile, 'r', encoding=encoding)
            return origin.readlines()
        except Exception:
            print('Read File Exception: File {0} not find or not available'.format(fullpathfile))
            print(traceback.format_exc())
        return []

    def lines_to_file_utf8(self, fullpathfile, lines):
        self.lines_to_file(fullpathfile, lines, 'utf-8')

    def lines_to_file(self, fullpathfile, lines, encoding):
        try:        
            self.delete_file(fullpathfile)
            f = open(fullpathfile, "a", encoding=encoding)
            for line in lines:
                f.write('{0}\n'.format(line))
            f.close()
        except Exception:
            print('Remove/Create Exception: File {0} not available'.format(fullpathfile))
            print(traceback.format_exc())    

    def delete_and_create_folder(self, fullpathfolder):
        try:
            if os.path.exists(fullpathfolder):
                shutil.rmtree(fullpathfolder)
            os.mkdir(fullpathfolder)
        except Exception:
            print('Remove/Create Exception: Folder {0} not available'.format(fullpathfolder))
            print(traceback.format_exc())

    def delete_file(self,fullpathfolder):
        try:
            if os.path.exists(fullpathfolder):
                os.remove(fullpathfolder)
        except Exception as ex:
            print('Remove Exception: Folder {0} not available'.format(fullpathfolder))
            print(traceback.format_exc())