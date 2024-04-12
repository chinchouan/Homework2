import json
import os


def get_student_info(student_id: str) -> dict:
    """
    This function takes a student id and returns a dictionary
    of the student information
    :param student_id: student id
    :return: a dictionary of the student information
    """

    with open(JSONFILE, 'r', encoding='utf-8') as f:
        data_dict: dict = json.load(f)
        found_id: bool = False
        for d in data_dict:
            if d['student_id'] == student_id:
                found_id = True
                result: dict = d
        if not found_id:
            raise ValueError(f"=>發生錯誤: 學號 {student_id} 找不到.")
        return result


def add_course(student_id: str, course_name: str, course_score: str) -> str:
    """
    This function takes dictionary of the student information
    and add new data to dict of student's course information
    :param student_id: student id
    :param course_name: course name
    :param course_score: course score
    :return: add result success or fail(error)
    """

    get_student_info(student_id)
    if course_name == "" or course_score == "":
        raise ValueError("=>其它例外: 課程名稱或分數不可空白.")
    else:
        with open(JSONFILE, 'r', encoding='utf-8') as f:
            data_dict: dict = json.load(f)
            for d in data_dict:
                if d['student_id'] == student_id:
                    d['courses'].append(
                        {'name': course_name, 'score': float(course_score)}
                    )
        with open(JSONFILE, 'w', encoding='utf-8') as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=4)

    return "=>課程已成功新增。"


def calculate_average_score(student_data: dict) -> float:
    """
    This function takes a dictionary of student information
    and calculate average score
    :param student_data: student information
    :return: average score
    """

    total_courses: float = 0.0
    total_score: float = 0.0
    for c in student_data['courses']:
        total_courses += 1.0
        total_score += c['score']
    if total_score == 0.0:
        return 0.0
    else:
        return total_score / total_courses


# menu declare
menu = """
***************選單***************
1. 查詢指定學號成績
2. 新增指定學號的課程名稱與分數
3. 顯示指定學號的各科平均分數
4. 離開
**********************************"""
# main programming
# (Use this block to avoid being called when being considered a module)
if __name__ == '__main__':
    # Constant to the json path
    JSONFILE: str = "./students.json"
    # Active the menu program
    active: bool = True
    while active:
        print(menu)
        data_exists: bool = os.path.isfile(JSONFILE)
        choice: str = input("請選擇操作項目：")
        if choice == '1':
            try:
                if data_exists:
                    # get student data and format it
                    sid: str = input("請輸入學號: ")
                    datas: dict = get_student_info(sid)
                    format_datas: str = json.dumps(
                        datas, indent=4, ensure_ascii=False
                    )
                    print(f"=>學生資料: {format_datas}", end="")
                else:
                    print("檔案：students.json不存在")
            except ValueError as ve:
                print(ve, end="")
            continue
        elif choice == '2':
            try:
                if data_exists:
                    sid: str = input("請輸入學號: ")
                    cname: str = input("請輸入要新增課程的名稱: ")
                    cscore: str = input("請輸入要新增課程的分數: ")
                    print(add_course(sid, cname, cscore), end="")
                else:
                    print("檔案：students.json不存在", end="")
            except ValueError as ve:
                print(ve, end="")
            continue
        elif choice == '3':
            try:
                # get student data
                sid: str = input("請輸入學號: ")
                the_student_info: dict = get_student_info(sid)
                msg: str = "=>各科平均分數: "
                # calculate the student's score average
                msg= msg + f"{calculate_average_score(the_student_info):.2f}"
                print(msg, end="")
            except ValueError as ve:
                print(ve, end="")
            continue
        elif choice == '4':
            active = False
            print("=>程式結束。", end="")
            continue
        else:
            print("請選擇1.到4.，輸入如:1。", end="")
            continue
