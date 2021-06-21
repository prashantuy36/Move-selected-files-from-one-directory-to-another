source_dir = r'D:\[CourseClub.ME] AppliedAICourse - Applied Machine Learning Course\to do'
dest_dir = r'D:\[CourseClub.ME] AppliedAICourse - Applied Machine Learning Course\Applied AI'
arr = os.listdir(source_dir)

for i in arr:
    sub_folder = os.path.join(source_dir, i)
    arr2 = os.listdir(sub_folder)
    for j in arr2:
        if j.endswith(".mp4") or j.endswith(".mkv") or j.endswith(".pdf"):
            path = os.path.join(dest_dir, i)
            shutil.move(os.path.join(sub_folder, j), path)