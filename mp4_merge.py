import os
import glob
import subprocess

dvd_dir = 'D:\\DVD'
dvd_subdir = 'VIDEO_TS'
os.chdir(dvd_dir)
dirlist = os.listdir(dvd_dir)
for directory in (dirlist):
    list_file = directory + '.txt'
    find_dir = dvd_dir + '\\' + directory + '\\' + dvd_subdir
    mp4_list = glob.glob(find_dir + '\\' + '*.mp4')
    if mp4_list == []:
        continue
    f = open(list_file, 'w')
    for file in (mp4_list):
        f.write('file ' + '\'' + file + '\'\n')
    f.close()
    param = ' -f concat -safe 0 -i ' + list_file + ' -c copy ' + directory + '.mp4'
    print('Processing ' + directory + '...\n')
    os.system('ffmpeg.exe' + param)      
    print('  DONE\n')    
    
