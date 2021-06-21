import shutil
import os

source_dir = r'D:\[CourseClub.ME] AppliedAICourse - Applied Machine Learning Course\to do'
dest_dir = r'D:\[CourseClub.ME] AppliedAICourse - Applied Machine Learning Course\Applied AI'

arr = os.listdir(source_dir)
for i in arr:
    sub_folder = os.path.join(dest_dir, i)
    os.mkdir(sub_folder)