import openpyxl
import os
import time

if __name__ == "__main__":
    save_dir = os.getcwd()
    file_dir = os.path.join(save_dir, "test.xlsx")

    if os.path.exists(file_dir):
        wb = openpyxl.load_workbook(file_dir)
        print("이미 파일이 존재하여 열었음")

    else:
        wb = openpyxl.Workbook()
        wb.save(file_dir)
        print("파일이 존재하지않아 생성하고 저장함")

    while True:
        time.sleep(1)
        print("작동중", time.strftime("%H:%M:%S", time.localtime()))