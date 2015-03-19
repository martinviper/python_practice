#import modules
import os
import string
##################################################
_HOST_LOGS_DIR = r'D:\02_TEMP___'
_SUBDIR_LIST = []
_UNARCHIVED_FILES = []
_HOST_SCANNED_FOR_UNARCHIVED_FILES = "TSTDUB509"
##################################################
def recursive_directory_check(current_dir,subdirList,number_of_unarchived_files):
    try :
        dirsList = [os.path.join(current_dir, subdir) for subdir in os.listdir(current_dir)]
    except:
        print ("Wrong path name/directory name used as _HOST_LOGS_DIR")
        return

    for new_subdir in dirsList:
        if os.path.isdir(new_subdir):
            if len(os.listdir(new_subdir)):
                subdir_with_files = os.listdir(new_subdir)
                for file_or_directory in subdir_with_files:
                    subdir_item_path = os.path.join(new_subdir, file_or_directory)
                    if os.path.isfile(subdir_item_path):
                        number_of_unarchived_files.extend([subdir_item_path])
                        if new_subdir not in subdirList:
                            subdirList.extend([new_subdir])
                    else:
                        recursive_directory_check(new_subdir,subdirList,number_of_unarchived_files)
##################################################
def main():
    host_dir = _HOST_LOGS_DIR
    subdirList = _SUBDIR_LIST
    unarchived = _UNARCHIVED_FILES
    scanned_host = _HOST_SCANNED_FOR_UNARCHIVED_FILES
    recursive_directory_check(host_dir,subdirList,unarchived)
    print '------------------------------------------------------'
    print 'TOTAL subdirectories with unarchived files found:',len(subdirList)
    print 'Number of unarchived files:', len(unarchived)
    print '------------------------------------------------------'
    filename = 'C:\\' + scanned_host + '_unarchived_files.txt'
    file_with_archives_scanned = open(filename, 'w')
    file_with_archives_scanned.write("----------------------------------------------------------------------------------------" + '\n')
    file_with_archives_scanned.write("TOTAL subdirectories with unarchived files found: " + str(len(subdirList)) + '\n')
    file_with_archives_scanned.write("Number of unarchived files: " + str(len(unarchived)) + '\n')
    file_with_archives_scanned.write("----------------------------------------------------------------------------------------" + '\n')
    file_with_archives_scanned.write("Below list of subdirectories with unarchived files found:" + '\n')
    file_with_archives_scanned.write("----------------------------------------------------------------------------------------" + '\n')
    for dirs in subdirList:
        dirname_converted = string.replace(dirs, '\\', '/')
        print(dirname_converted)
        file_with_archives_scanned.write(dirname_converted + '\n')
    file_with_archives_scanned.write("----------------------------------------------------------------------------------------" + '\n')
    file_with_archives_scanned.close()
    #input("Enter any key to exit ...")
##################################################
if __name__ == '__main__':
    main()
##################################################
