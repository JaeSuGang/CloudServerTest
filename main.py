import openpyxl
import os
import time

if __name__ == "__main__":
    if os.path.exists("test.xlsx"):
        wb = openpyxl.load_workbook("test.xlsx")
        print("이미 파일이 존재하여 열었음")

    else:
        wb = openpyxl.Workbook()
        wb.save("test.xlsx")
        print("파일이 존재하지않아 생성하고 저장함")

    while True:
        time.sleep(1)
        print("작동중", time.strftime("%H:%M:%S", time.localtime()))