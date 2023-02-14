from prettytable import PrettyTable

def TableFunc(data):
    # 创建表格
    table = PrettyTable()
    table.field_names = data[0].keys()
    for row in data:
        table.add_row(row.values())
    # 打印表格
    print(table)
data = [{"name": "Alice", "age": 25, "gender": "female"},
        {"name": "Bob", "age": 30, "gender": "male"},
        {"name": "Charlie", "age": 35, "gender": "male"}]


def TableFunny():

    # 输出表格和图案    
    print("      _.-^^---....,,-- ")
    print("  _--                  --_ ")
    print(" <                        >) ")
    print(" |                         | ")
    print("  \._                   _./ ")
    print("     ```--. . , ; .--''' ")
    print("           | |   | ")
    print("        .-=||  | |=-. ")
    print("        `-=#$%&%$#=-' ")
    print("           | ;  :| ")
    print("         _| ''`-.._ ")
    print("        / `--._  \ ")
    print("        /         \ ")
# TableFunc(data)