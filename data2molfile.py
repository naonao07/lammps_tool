
filename = input("lmpファイル名を入力してください: ")

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


# molfileを作成する
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
        
        
# "Bonds"という文字列が現れた行数を取得
    row_Atoms = 0
    for i, line in enumerate(lines):
        if "Bonds" in line:
            row_Bonds = i   
    
    for line in lines[row_Bonds -1:]:
        output_file.write(line)     
        
        
    # ファイルを閉じた後、"filename.molfile" が作成されます


# coeffファイルを作成する
coeff_filename = filename.replace(".lmp", ".setting")

with open(coeff_filename, 'w') as coeff_file:
    # 1行目に"#filename"を書き込む
    coeff_file.write("#" + coeff_filename + "\n")
    coeff_file.write("\n")
        
# "Masses"という文字列が現れた行数を取得
    row_Masses = 0
    for i, line in enumerate(lines):
        if "Masses" in line:
            row_Masses = i   
    

#massコマンドに変換する
    for i in range(row_Masses + 2, row_Masses + 2 + atom_types):
        data = lines[i].strip()
        modified_line = "mass " + data  # "mass" を挿入
        coeff_file.write(modified_line + '\n')
    coeff_file.write("\n") 

# "Pair Coeffs"という文字列が現れた行数を取得
    row_pair_coeff = 0
    for i, line in enumerate(lines):
        if "Pair Coeffs" in line:
            row_pair_coeff = i   
    

#pair_coeffコマンドに変換する
    for i in range(row_pair_coeff + 2, row_pair_coeff + 2 + atom_types):
        data = lines[i].strip()
        pair_coeffID = i - row_pair_coeff - 1

        modified_line = "pair_coeff " + str(pair_coeffID) + " " + data  # "pair_coeff" を挿入
        coeff_file.write(modified_line + '\n')
    coeff_file.write("\n") 


# "Bond Coeffs"という文字列が現れた行数を取得
    row_bond_coeff = 0
    for i, line in enumerate(lines):
        if "Bond Coeffs" in line:
            row_bond_coeff = i   
    

#bond_coeffコマンドに変換する
    for i in range(row_bond_coeff + 2, row_bond_coeff + 2 + bond_types):
        data = lines[i].strip()
        modified_line = "bond_coeff " + data  # "bond_coeff" を挿入
        coeff_file.write(modified_line + '\n')
    coeff_file.write("\n") 


# "Angle Coeffs"という文字列が現れた行数を取得
    row_angle_coeff = 0
    for i, line in enumerate(lines):
        if "Angle Coeffs" in line:
            row_angle_coeff = i   
    

#angle_coeffコマンドに変換する
    for i in range(row_angle_coeff + 2, row_angle_coeff + 2 + angle_types):
        data = lines[i].strip()
        modified_line = "angle_coeff " + data  # "bond_coeff" を挿入
        coeff_file.write(modified_line + '\n')
    coeff_file.write("\n") 


# "Dihedral Coeffs"という文字列が現れた行数を取得
    row_dihedral_coeff = 0
    for i, line in enumerate(lines):
        if "Dihedral Coeffs" in line:
            row_dihedral_coeff = i   
    

#dihedral_coeffコマンドに変換する
    for i in range(row_dihedral_coeff + 2, row_dihedral_coeff + 2 + dihedral_types):
        data = lines[i].strip()
        modified_line = "dihedral_coeff " + data  # "bond_coeff" を挿入
        coeff_file.write(modified_line + '\n')
    coeff_file.write("\n") 


# "Improper Coeffsという文字列が現れた行数を取得
    row_improper_coeff = 0
    for i, line in enumerate(lines):
        if "Improper Coeffs" in line:
            row_improper_coeff = i   
    

#improper_coeffコマンドに変換する
    for i in range(row_improper_coeff + 2, row_improper_coeff + 2 + improper_types):
        data = lines[i].strip()
        modified_line = "improper_coeff " + data  # "bond_coeff" を挿入
        coeff_file.write(modified_line + '\n')
    coeff_file.write("\n")
