# main.py

import os

# 定义记事文件的路径
NOTES_FILE = "notes.txt"

def add_note():
    """添加记事"""
    note = input("请输入记事内容：")
    if note.strip():
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("记事添加成功！")
    else:
        print("输入不能为空！")

def view_notes():
    """查看记事"""
    if os.path.exists(NOTES_FILE):
        print("\n=== 已保存的记事 ===")
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = f.readlines()
            if notes:
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("没有任何记事！")
    else:
        print("没有任何记事！")
    print("===================\n")

def delete_note():
    """删除记事"""
    print("功能开发中：删除记事...")

def main():
    while True:
        print("\n=== 记事本功能菜单 ===")
        print("1. 添加记事")
        print("2. 查看记事")
        print("3. 删除记事")
        print("4. 退出程序")
        print("===================")
        choice = input("请选择功能 (1-4): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("程序已退出，再见！")
            break
        else:
            print("无效的选择，请输入1到4之间的数字！")

if __name__ == "__main__":
    main()
