row1=['🤪','🤪','🤪','🤪']
row2=['🤪','🤪','🤪','🤪']
row3=['🤪','🤪','🤪','🤪']
print(f"{row1}\n{row2}\n{row3}")
matrix=[row1,row2,row3]
index=input("inter your hiding index:")
row_number=int(index[0])
col_number=int(index[1])
selected_row=matrix[row_number-1]
selected_row[col_number-1]="X"
print(f"{row1}\n{row2}\n{row3}")


