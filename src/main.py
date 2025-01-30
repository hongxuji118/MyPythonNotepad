import os
import time
from datetime import datetime

# 全局变量
notes = []
PASSWORD = "123456"

# 密码验证功能
def verify_password():
    print("=== 欢迎使用记事本程序 ===")
    input_password = input("请输入密码以继续：")
    if input_password != PASSWORD:
        print("密码错误，程序即将退出。")
        exit()

# 添加记事
def add_note():
    content = input("请输入记事内容：")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"content": content, "timestamp": timestamp})
    print("记事添加成功！")

# 查看记事
def view_notes():
    if not notes:
        print("暂无任何记事！")
        return
    print("\n=== 已保存的记事 ===")
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note['content']} (时间: {note['timestamp']})")

# 删除记事
def delete_note():
    view_notes()
    if not notes:
        return
    try:
        idx = int(input("请输入要删除的记事编号：")) - 1
        if 0 <= idx < len(notes):
            deleted = notes.pop(idx)
            print(f"记事删除成功：{deleted['content']}")
        else:
            print("输入编号无效！")
    except ValueError:
        print("请输入有效的数字！")

# 搜索记事
def search_note():
    keyword = input("请输入搜索关键词：")
    results = [note for note in notes if keyword in note['content']]
    if results:
        print("\n=== 搜索结果 ===")
        for idx, note in enumerate(results, start=1):
            print(f"{idx}. {note['content']} (时间: {note['timestamp']})")
    else:
        print("未找到匹配的记事！")

# 修改记事
def edit_note():
    view_notes()
    if not notes:
        return
    try:
        idx = int(input("请输入要修改的记事编号：")) - 1
        if 0 <= idx < len(notes):
            new_content = input("请输入新的记事内容：")
            notes[idx]['content'] = new_content
            notes[idx]['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("记事修改成功！")
        else:
            print("输入编号无效！")
    except ValueError:
        print("请输入有效的数字！")

# 导出记事
def export_notes():
    if not notes:
        print("暂无任何记事可导出！")
        return
    with open("notepad_export.txt", "w", encoding="utf-8") as f:
        for note in notes:
            f.write(f"{note['content']} (时间: {note['timestamp']})\n")
    print("记事已成功导出至 notepad_export.txt")

# 主程序循环
def main():
    verify_password()
    while True:
        print("\n=== 记事本功能菜单 ===")
        print("1. 添加记事")
        print("2. 查看记事")
        print("3. 删除记事")
        print("4. 搜索记事")
        print("5. 修改记事")
        print("6. 导出记事")
        print("7. 退出程序")
        print("===================")
        choice = input("请选择功能 (1-7): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search_note()
        elif choice == "5":
            edit_note()
        elif choice == "6":
            export_notes()
        elif choice == "7":
            print("程序已退出，再见！")
            break
        else:
            print("无效的选择，请重新输入！")

if __name__ == "__main__":
    main()
