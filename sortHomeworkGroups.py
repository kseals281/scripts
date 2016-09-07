from os import listdir, makedirs
from os.path import exists, isfile, join
from shutil import copyfile

groups = ['groupA', 'groupB', 'groupC']
dirs = []

groupA = [2732362,2697400,2798618,2780008,2806314,2824248,2821424,2817814,2824681,2823312,2817904,2785797,2728082,2768230,2781871,2823126,2794912,2780293,2825044,2818122,2830917,2818173,2807286]
groupB = [2824273,2753819,2772376,2783028,2777897,2821016,2818233,2808611,2813908,2808710,2817312,2772004,2808909,2823391,2822383,2730470,2778974,2825131,1076998,2768607,2824578,2788421,2834795]
groupC = [2690321,2809357,2709608,2817465,2767505,2788295,2825862,2788407,2824617,2797732,2710130,2823465,2832745,2785236,2729565,2780220,2710142,2783340,2821443,2824800,2823097,2813646,2691593]

mypath = 'C:\\Users\\Khari\\Google Drive\\Howard Fall 2016\\Staff materials\\Grades\\Labs\\Lab 1\\Submissions'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for group in groups:
  dirs.append(mypath + '\\' + group)
  if not exists(dirs[len(dirs) - 1]):
    makedirs(dirs[len(dirs) - 1])





wleralkernf





for idA, idB, idC in zip(groupA, groupB, groupC):
  for f in onlyfiles:
    if str(idA) in f:
      file = mypath + '\\' + f
      copyfile(file, (dirs[0] + '\\' + f))
      continue
    if str(idB) in f:
      file = mypath + '\\' + f
      copyfile(file, (dirs[1] + '\\' + f))
      continue
    if str(idC) in f:
      file = mypath + '\\' + f
      copyfile(file, (dirs[2] + '\\' + f))
      continue
