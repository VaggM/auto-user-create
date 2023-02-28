import pandas as pd


# Get new passwords
textfile = 'passwords.txt'

with open(textfile) as f:
    lines = f.readlines()

passwords = []

for line in lines:
    index = line.find('New password:')
    error = line.find('Failure/Error:')
    if index != -1:
        password = line[index+14:].rstrip()
        passwords.append(password)
    if error != -1:
        passwords.append('')
        

# Open excel, write the new dataframe
excel = 'TrustFirstUsers.xlsx'
sheetname = 'Sheet1'
df = pd.read_excel(excel)

df['Password'] = df['Password'].replace(df['Password'].values, passwords)

with pd.ExcelWriter(excel, engine='openpyxl', mode='a') as writer:
    workBook = writer.book
    try:
        workBook.remove(workBook[sheetname])
    except:
        print("Worksheet does not exist")
    finally:
        df.to_excel(writer, sheet_name=sheetname, index=False)
