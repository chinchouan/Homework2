import json



def get_student_info(data, student_id) -> dict:

    with open(data, 'r', encoding='utf-8') as f:
        dict = json.load(f)
        found_id = False
        for d in dict:
            if d['student_id'] == student_id:
                found_id = True
                return d
        if not found_id:
            raise ValueError('Student ID not found')


menu = """
***************選單***************
1. 查詢指定學號成績
2. 新增指定學號的課程名稱與分數
3. 顯示指定學號的各科平均分數
4. 離開
**********************************"""
if __name__ == '__main__':
    JSONFILE = "./students.json"
    print(get_student_info(JSONFILE, '93546072'))
    active = True
    while active:
        print(menu)
        choice = input("請選擇操作項目：")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            pass


