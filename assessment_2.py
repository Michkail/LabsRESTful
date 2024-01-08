df_sales = open("./sales_location.txt", "w+")
df_sales.writelines(["0001", ",", "Rizal", ",", "100\n"])
df_sales.writelines(["0003", ",", "Wanda", ",", "200\n"])
df_sales.writelines(["0004", ",", "Wanda", ",", "300\n"])
df_sales.writelines(["0005", ",", "Rizal", ",", "40\n"])
df_sales.writelines(["0001", ",", "Ken", ",", "50\n"])
df_sales.writelines(["0001", ",", "Lenny", ",", "60\n"])
df_sales.writelines(["0002", ",", "Lenny", ",", "70\n"])

df_sales.close()

df_location = open("./location.txt", "w+")
df_location.writelines(["0001", ",", "Jakarta\n"])
df_location.writelines(["0002", ",", "Bandung\n"])
df_location.writelines(["0003", ",", "Surabaya\n"])
df_location.writelines(["0004", ",", "Semarang\n"])
df_location.writelines(["0005", ",", "Padang\n"])

df_location.close()

print("DATA SALES")
dfs = open("./sales_location.txt", "r+")
print(dfs.read())

print("DATA LOCATION")
dfl = open("./location.txt", "r+")
print(dfl.read())

print("TASK")
dfst = open("./sales_location.txt", "r+")
with open("./location.txt", "r+") as dflt:
    for x, y in enumerate(dflt):
        cond = '0002'
        if '0002' and '0001' in y:
            # with open("./sales_location.txt", "r+") as dslt:
            print("number", x + 1)
            print("line", y)
            break