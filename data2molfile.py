
filename = input("何か入力してください: ")

# ユーザーが入力した値を表示
print("filename=" + filename)
# テキストファイルを開いて全行を読み込む

with open(filename, 'r') as file:
    lines = file.readlines()

# 9行目から13行目の数値を取得
input_string1 = lines[8]
stripped_input1 = input_string1.strip()
atom_types = int(stripped_input1.split()[0])
print("atom_types=", atom_types)

input_string2 = lines[9]
stripped_input2 = input_string2.strip()
bond_types = int(stripped_input2.split()[0])
print("bond_types=", bond_types)

input_string3 = lines[10]
stripped_input3 = input_string3.strip()
angle_types = int(stripped_input3.split()[0])
print("angle_types=", angle_types)

input_string4 = lines[11]
stripped_input4 = input_string4.strip()
dihedral_types = int(stripped_input4.split()[0])
print("dihedral_types=", dihedral_types)

input_string5 = lines[12]
stripped_input5 = input_string5.strip()
improper_types = int(stripped_input5.split()[0])
print("improper_types=", improper_types)
print("---------------------")


# "Atoms"という文字列が現れた行数を取得
row_Atoms = 0
for i, line in enumerate(lines):
    if "Atoms" in line:
        row_Atoms = i

# "Atoms"の次の行からatom_types行分のデータを取得
matrix_Atoms = []
for i in range(row_Atoms + 2, row_Atoms + 2 + atom_types):
    data = lines[i].strip().split()
    AtomNumber, Atomtype, AtomID, q, atomx, atomy, atomz = data[0], data[1], data[2], data[3], data[4], data[5], data[6]
    matrix_Atoms.append([int(AtomNumber), int(Atomtype), int(AtomID), float(q), float(atomx), float(atomy), float(atomz)])

# matrix_Atomsを表示してみる
for row in matrix_Atoms:
    print(row[0])

output_filename = filename.replace(".lmp", "_1.molfile")

# ファイルを作成して書き込みモードで開く
with open(output_filename, 'w') as output_file:
    # 1行目に"#filename"を書き込む
    output_file.write("#" + "filename" + "\n")

    # 3行目から7行目に"your_file.txt"の対応する行をコピーする
    for i in range(1, 7):
        output_file.write(lines[i])
    output_file.write("\n")    
    output_file.write("Coords\n")
    output_file.write("\n")  

    # 11行目以降に matrix_Atoms のデータを書き込む
    for atom_data in matrix_Atoms:
        # 4列になるように AtomNumber, atomx, atomy, atomz を書き込む
        output_file.write(f"{atom_data[0]}\t{atom_data[4]}\t{atom_data[5]}\t{atom_data[6]}\n")
    
    
    output_file.write("\n")    
    output_file.write("Types\n")
    output_file.write("\n") 
    
    for atom_data in matrix_Atoms:
    # 4列になるように AtomNumber, atomx, atomy, atomz を書き込む
        output_file.write(f"{atom_data[0]}\t{atom_data[2]}\n")
        
    output_file.write("\n")    
    output_file.write("Charges\n")
    output_file.write("\n") 
    
    for atom_data in matrix_Atoms:
    # 4列になるように AtomNumber, atomx, atomy, atomz を書き込む
        output_file.write(f"{atom_data[0]}\t{atom_data[3]}\n")   
        
        
# "Atoms"という文字列が現れた行数を取得
    row_Atoms = 0
    for i, line in enumerate(lines):
        if "Bonds" in line:
            row_Bonds = i   
    
    for line in lines[row_Bonds -1:]:
        output_file.write(line)     
        
        
    # ファイルを閉じた後、"filename.molfile" が作成されます


