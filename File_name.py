import os
file_list = os.listdir(r'W:\050 PLM\041 ECO request\ECO#770021_New tree PQ build updates\Document & Drawings')
for name in range(0, len(file_list), 2):
    print(file_list[name:name+2])
