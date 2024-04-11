import json
import os


def get_student_info(data, student_id) -> dict:
    """
    This function takes a dict of student info and returns a dict of student id info
    :param data: dict of student info
    :param student_id: student id
    :return: dict of student id info
    """
    with open(data, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
        found_id = False
        for d in data_dict:
            if d['student_id'] == student_id:
                found_id = True
                return d
        if not found_id:
            raise ValueError(f"=>發生錯誤: 學號 {student_id} 找不到.")


def add_course(student_id, course_name, course_score):
    pass


menu = """
***************選單***************
1. 查詢指定學號成績
2. 新增指定學號的課程名稱與分數
3. 顯示指定學號的各科平均分數
4. 離開
**********************************"""
if __name__ == '__main__':
    JSONFILE = "./students.json"
    active = True
    while active:
        print(menu)
        data_exists = os.path.isfile(JSONFILE)
        choice = input("請選擇操作項目：")
        if choice == '1':
            try:
                if data_exists:
                    sid = input("請輸入學號: ")
                    datas = get_student_info(JSONFILE, sid)
                    format_datas = json.dumps(
                        datas, indent=4, ensure_ascii=False
                    )
                    print(f"=>學生資料: {format_datas}")
                else:
                    print("檔案：students.json不存在")
            except ValueError as ve:
                print(ve)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            active = False
            continue
        else:
            pass


