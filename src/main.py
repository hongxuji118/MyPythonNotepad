import os

# 定义记事本类
class Notepad:
    def __init__(self):
        self.notes = []

    # 添加记事
    def add_note(self, note):
        self.notes.append(note)

    # 查看记事
    def view_notes(self):
        if self.notes:
            for index, note in enumerate(self.notes, start=1):
                print(f"{index}. {note}")
        else:
            print("没有记事！")

    # 删除记事
    def delete_note(self, note_id):
        if 0 < note_id <= len(self.notes):
            deleted_note = self.notes.pop(note_id - 1)
            print(f"记事 '{deleted_note}' 删除成功！")
        else:
            print("无效的记事编号！")

    # 搜索记事
    def search_notes(self, keyword):
        results = [note for note in self.notes if keyword in note]
        if results:
            print("=== 搜索结果 ===")
            for index, result in enumerate(results, start=1):
                print(f"{index}. {result}")
        else:
            print(f"没有找到包含关键词 '{keyword}' 的记事！")

    # 修改记事
    def modify_note(self, note_id, new_content):
        if 0 < note_id <= len(self.notes):
            self.notes[note_id - 1] = new_content
            print("记事修改成功！")
        else:
            print("无效的记事编号！")

    # 导出记事到文件
    def export_notes(self):
        if self.notes:
            with open("notepad_export.txt", "w", encoding="utf-8") as f:
                for index, note in enumerate(self.notes, start=1):
                    f.write(f"{index}. {note}\n")
            print("记事已成功导出到 notepad_export.txt！")
        else:
            print("没有可导出的记事！")

# 主程序
def main():
    notepad = Notepad()

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
            note = input("请输入记事内容：")
            notepad.add_note(note)
            print("记事添加成功！")
        elif choice == "2":
            print("\n=== 已保存的记事 ===")
            notepad.view_notes()
        elif choice == "3":
            notepad.view_notes()
            try:
                note_id = int(input("请输入要删除的记事编号："))
                notepad.delete_note(note_id)
            except ValueError:
                print("请输入有效的数字！")
        elif choice == "4":
            keyword = input("请输入要搜索的关键词：")
            notepad.search_notes(keyword)
        elif choice == "5":
            notepad.view_notes()
            try:
                note_id = int(input("请输入要修改的记事编号："))
                new_content = input("请输入新的记事内容：")
                if new_content:
                    notepad.modify_note(note_id, new_content)
                else:
                    print("输入不能为空！")
            except ValueError:
                print("请输入有效的数字！")
        elif choice == "6":
            notepad.export_notes()
        elif choice == "7":
            print("程序已退出，再见！")
            break
        else:
            print("无效的选择，请输入1到7之间的数字！")

if __name__ == "__main__":
    main()
