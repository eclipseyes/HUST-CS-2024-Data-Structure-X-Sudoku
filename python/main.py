import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui, QtCore
from Ui_start import Ui_MainWindow as Ui_StartWindow
from Ui_rules import Ui_RulesWindow
from Ui_mode import Ui_MainWindow as Ui_ModeWindow
from Ui_upload import Ui_MainWindow as Ui_UploadWindow
from Ui_difficulty import Ui_MainWindow as Ui_DifficultyWindow
from Ui_game import Ui_MainWindow as Ui_GameWindow

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 动态获取C程序的路径
        if hasattr(sys, '_MEIPASS'):
            self.c_programs_dir = os.path.join(sys._MEIPASS, 'c')
        else:
            self.c_programs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../c')


        # 创建并添加各个界面到 QStackedWidget
        self.start_ui = Ui_StartWindow()
        self.rules_ui = Ui_RulesWindow()
        self.mode_ui = Ui_ModeWindow()
        self.upload_ui = Ui_UploadWindow()
        self.difficulty_ui = Ui_DifficultyWindow()
        self.game_ui = Ui_GameWindow()

        # 加载界面
        self.start_widget = QMainWindow()
        self.start_ui.setupUi(self.start_widget)
        self.stacked_widget.addWidget(self.start_widget)

        self.rules_widget = QMainWindow()
        self.rules_ui.setupUi(self.rules_widget)
        self.stacked_widget.addWidget(self.rules_widget)

        self.mode_widget = QMainWindow()
        self.mode_ui.setupUi(self.mode_widget)
        self.stacked_widget.addWidget(self.mode_widget)

        self.upload_widget = QMainWindow()
        self.upload_ui.setupUi(self.upload_widget)
        self.stacked_widget.addWidget(self.upload_widget)

        self.difficulty_widget = QMainWindow()
        self.difficulty_ui.setupUi(self.difficulty_widget)
        self.stacked_widget.addWidget(self.difficulty_widget)

        self.game_widget = QMainWindow()
        self.game_ui.setupUi(self.game_widget)
        self.stacked_widget.addWidget(self.game_widget)

        # 绑定按钮事件
        self.start_ui.rules.clicked.connect(self.show_rules)
        self.start_ui.game.clicked.connect(self.show_mode)

        self.rules_ui.rules_back.clicked.connect(self.show_main)
        self.mode_ui.upload.clicked.connect(self.show_upload)
        self.mode_ui.puzzle.clicked.connect(self.show_difficulty)
        self.mode_ui.mode_back.clicked.connect(self.show_main)
        self.difficulty_ui.difficulty_back.clicked.connect(self.show_mode)
        self.upload_ui.upload_back.clicked.connect(self.show_mode)

        self.upload_ui.file_choose.clicked.connect(self.on_file_choose_clicked)
        self.upload_ui.solve_button.clicked.connect(self.on_solve_button_clicked)
        self.upload_ui.better_solve_button_1.clicked.connect(lambda: self.on_better_solve_button_clicked(1))
        self.upload_ui.better_solve_button_2.clicked.connect(lambda: self.on_better_solve_button_clicked(2))
        self.upload_ui.better_solve_button_3.clicked.connect(lambda: self.on_better_solve_button_clicked(3))

        self.upload_ui.source_button.clicked.connect(self.open_source_file)
        self.upload_ui.save_button.clicked.connect(self.open_saved_file)
        self.upload_ui.dpll_button.clicked.connect(self.open_dpll_file)
        self.upload_ui.cdcl_button.clicked.connect(self.open_cdcl_file)

        # 绑定难度按钮，传递不同的参数来生成对角线数独题目
        self.difficulty_ui.easy.clicked.connect(lambda: self.prepare_game("easy"))
        self.difficulty_ui.simple.clicked.connect(lambda: self.prepare_game("simple"))
        self.difficulty_ui.intermediate.clicked.connect(lambda: self.prepare_game("intermediate"))
        self.difficulty_ui.expert.clicked.connect(lambda: self.prepare_game("expert"))

        self.game_ui.game_back.clicked.connect(self.show_difficulty)
        self.game_ui.check_button.clicked.connect(self.check_solution)
        self.game_ui.peek_button.clicked.connect(self.peek_solution)
        self.game_ui.show_button.clicked.connect(self.show_solution)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game_time)

        self.peek_count = 0
        self.game_time_seconds = 0
        self.is_answer_shown = False
        self.answer_file_path = "solution.txt"
        self.previous_user_input = []  # 用于存储用户输入的状态

    def get_selected_difficulty(self):
        """根据用户选择返回不同难度级别"""
        if self.difficulty_ui.easy.isChecked():
            return "easy"
        elif self.difficulty_ui.simple.isChecked():
            return "simple"
        elif self.difficulty_ui.intermediate.isChecked():
            return "intermediate"
        elif self.difficulty_ui.expert.isChecked():
            return "expert"
        return "easy"

    def prepare_game(self, difficulty):
        """根据选择的难度准备游戏"""
        self.timer.start(1000)
        self.peek_count = 0
        self.game_time_seconds = 0
        self.is_answer_shown = False
        self.game_ui.peek_count.setVisible(False)
        self.game_ui.game_time.setVisible(True)
        # 确定挖洞数量
        difficulty_levels = {
            "easy": "1",  # 假设"easy"对应20个挖洞
            "simple": "2",  # "simple" 对应30个挖洞
            "intermediate": "3",  # "intermediate" 对应40个挖洞
            "expert": "4"   # "expert" 对应50个挖洞
        }
        # 获取数值型的难度级别
        difficulty_level = difficulty_levels.get(difficulty, "1")

        # 调用C程序生成对角线数独题目
        semantic_file_path = "generated_puzzle.cnf"  # 生成的语义编码CNF文件路径
        natural_file_path = "altered_puzzle.cnf"  # 生成的自然编码CNF文件路径
        generator_path = os.path.join(self.c_programs_dir, 'generate_diagonal_sudoku.exe')

        solver_path = os.path.join(self.c_programs_dir, 'sudoku_solver.exe')


        try:
            result = subprocess.run([generator_path, difficulty_level, semantic_file_path, natural_file_path], check=True, capture_output=True, text=True, encoding='utf-8')
            print(f"Puzzle generation completed, CNF files saved to: {semantic_file_path} and {natural_file_path}")
            print(f"C program output: {result.stdout}")

            # 运行解算器
            result = subprocess.run([solver_path, natural_file_path], check=True, capture_output=True, text=True, encoding='utf-8')
            print("Solution file generated.")
            print(f"Solver output: {result.stdout}")
 
            # 转换解文件为数独网格格式
            if not self.convert_solution_to_grid("solution.cnf"):
                print("Error converting solution to grid format.")
                return

        except subprocess.CalledProcessError as e:
            print(f"Error generating puzzle or solution: {e}")
            print(f"C program error output: {e.stderr}")
            return
        except Exception as e:
            print(f"Other error: {e}")
            return

        # 清空游戏界面并显示新生成的数独
        self.show_game()
        self.display_puzzle(semantic_file_path)
    
    def convert_solution_to_grid(self,solution_cnf_path):
        """
        使用 cnf_to_grid.exe 将 CNF 格式的解转换为数独网格格式。
        """
        converter_path = os.path.join(self.c_programs_dir, 'cnf_to_grid.exe')

        grid_output_path = "solution.txt"  # 转换后的数独网格路径

        try:
            # 调用转换器程序
            result = subprocess.run([converter_path, solution_cnf_path, grid_output_path], check=True, capture_output=True, text=True, encoding='utf-8')
            print(f"Solution converted and saved to: {grid_output_path}")
            print(f"C program output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting solution: {e}")
            print(f"C program error output: {e.stderr}")
            return False
        except Exception as e:
            print(f"Other error: {e}")
            return False

        return True

    def display_puzzle(self, cnf_file_path):
        """将CNF格式的数独题目转换为可显示的数独格局"""
        parser_path = os.path.join(self.c_programs_dir, 'cnf_to_grid.exe')

        puzzle_file_path = "sudoku_puzzle.txt"  # 生成的数独格局路径

        try:
            result = subprocess.run([parser_path, cnf_file_path, puzzle_file_path], check=True, capture_output=True, text=True, encoding='utf-8')
            print(f"Puzzle parsed and grid generated, saved to: {puzzle_file_path}")
            print(f"C program output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Parsing error: {e}")
            print(f"C program error output: {e.stderr}")
            return
        except Exception as e:
            print(f"Other error: {e}")
            return

        # 在游戏界面显示生成的数独网格
        self.load_puzzle_to_ui(puzzle_file_path)

    def load_puzzle_to_ui(self, puzzle_file_path):
        """加载解析后的数独网格并显示在游戏界面上"""
        try:
            with open(puzzle_file_path, 'r') as f:
                puzzle_lines = f.readlines()
            if not puzzle_lines:
                print("Error: Puzzle file is empty or not properly formatted.")
                return

            print(f"Loaded puzzle from file: {puzzle_file_path}")
            table = self.game_ui.sudoku_table
            table.setRowCount(9)
            table.setColumnCount(9)
            
            for row_idx, line in enumerate(puzzle_lines):
                numbers = line.strip().split()
                for col_idx, num in enumerate(numbers):
                    item = QTableWidgetItem("" if num == '0' else num)
                    item.setTextAlignment(Qt.AlignCenter)

                    if num != '0':  # 0 表示空格
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 禁止修改
                        item.setForeground(QtGui.QBrush(Qt.black))
                    else:
                        # 允许输入
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                        item.setForeground(QtGui.QBrush(Qt.blue))
                    table.setItem(row_idx, col_idx, item)

            # 强制刷新 UI
            table.viewport().update()
            table.repaint()

            # 调用 Qt 事件循环来确保 UI 刷新
            QtGui.QGuiApplication.processEvents()
        
            print("Successfully loaded puzzle into the UI.")  # 添加调试信息

        except Exception as e:
            print(f"Error loading puzzle to UI: {e}")

    def on_file_choose_clicked(self):
        # 每次选择文件前，重置UI状态
        self.upload_ui.judge.clear()
        self.upload_ui.saved_path.clear()
        self.upload_ui.optimization_rate.clear()
        self.upload_ui.dpll_time.clear()
        self.upload_ui.dpll_address.clear()
        self.upload_ui.cdcl_time.clear()
        self.upload_ui.cdcl_address.clear()

        self.upload_ui.judge_label.hide()
        self.upload_ui.judge.hide()
        self.upload_ui.saved_path_label.hide()
        self.upload_ui.saved_path.hide()
        self.upload_ui.rate_label.hide()
        self.upload_ui.optimization_rate.hide()
        self.upload_ui.dpll_time_label.hide()
        self.upload_ui.dpll_time.hide()
        self.upload_ui.dpll_address_label.hide()
        self.upload_ui.dpll_address.hide()
        self.upload_ui.cdcl_time_label.hide()
        self.upload_ui.cdcl_time.hide()
        self.upload_ui.cdcl_address_label.hide()
        self.upload_ui.cdcl_address.hide()
        self.upload_ui.dpll_button.hide()
        self.upload_ui.cdcl_button.hide()

        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "CNF Files (*.cnf);;All Files (*)")
        if file_path:
            file_path = os.path.abspath(file_path)
            print(f"Chosen file path: {file_path}")

            self.upload_ui.cnf_path.setText(file_path)
            self.upload_ui.cnf_path.show()

            if not os.path.exists(file_path):
                print("Error: File does not exist.")
                return
            
            cnf_parser_path = os.path.join(self.c_programs_dir, 'cnf_parser.exe')

            if not os.path.exists(cnf_parser_path):
                print(f"Error: cnf_parser.exe not found at {cnf_parser_path}")
                return
            
            saved_path = os.path.abspath("output_result.txt")
            
            try:
                # 指定编码为 utf-8
                result = subprocess.run([cnf_parser_path, file_path, saved_path], check=True, capture_output=True, text=True, encoding='utf-8')
                print(f"Parsing completed, results saved to: {saved_path}")
                print(f"C program output: {result.stdout}")
            except subprocess.CalledProcessError as e:
                print(f"Parsing error: {e}")
                print(f"C program error output: {e.stderr}")
            except Exception as e:
                print(f"Other error: {e}")

            self.upload_ui.saved_path.setText(saved_path)
            self.upload_ui.saved_path.show()
            self.upload_ui.saved_path_label.show()
            self.upload_ui.solve_button.show()
            self.upload_ui.source_button.show()
            self.upload_ui.save_button.show()

    def on_solve_button_clicked(self):
        """执行 solver.exe """
        cnf_file_path = self.upload_ui.cnf_path.text()
        if not cnf_file_path:
            print("No CNF file selected.")
            return

        result_file_path = cnf_file_path + ".res"
        solver_path = os.path.join(self.c_programs_dir, 'solver.exe')


        try:
            # 指定编码为 utf-8
            result = subprocess.run([solver_path, cnf_file_path], check=True, capture_output=True, text=True, encoding='utf-8')
            print(f"Solving completed, results saved to: {result_file_path}")
            print(f"Solver output: {result.stdout}")

            self.upload_ui.dpll_address.setText(result_file_path)
            self.upload_ui.dpll_address.show()
            
            # 读取生成的结果文件
            if os.path.exists(result_file_path):
                with open(result_file_path, 'r') as f:
                    lines = f.readlines()
                    result_status = None
                    solve_time = None
                    for line in lines:
                        if line.startswith('s'):
                            result_status = line.strip()
                        elif line.startswith('t'):
                            solve_time = line.strip().split(' ')[1]

                    if result_status == 's 1':
                        self.upload_ui.dpll_time.setText(f"{solve_time} ms")
                        self.upload_ui.judge.setText("有解")
                    elif result_status == 's 0':
                        self.upload_ui.dpll_time.setText(f"{solve_time} ms")
                        self.upload_ui.judge.setText("无解")

        except subprocess.CalledProcessError as e:
            print(f"Error running solver: {e}")
            print(f"Solver error output: {e.stderr}")
        except Exception as e:
            print(f"Other error: {e}")

        self.upload_ui.dpll_time_label.show()
        self.upload_ui.dpll_time.show()
        self.upload_ui.dpll_address_label.show()
        self.upload_ui.dpll_address.show()
        self.upload_ui.dpll_button.show()
  
        self.upload_ui.judge_label.show()
        self.upload_ui.judge.show()
        
        self.calculate_and_display_optimization_rate()

    def on_better_solve_button_clicked(self, pickvar_choice):
        """执行 better_solver.exe 并传递参数以选择不同的 PickVar 函数"""
        cnf_file_path = self.upload_ui.cnf_path.text()
        if not cnf_file_path:
            print("No CNF file selected.")
            return

        result_file_path = f"{cnf_file_path}_faster.res"
        solver_path = os.path.join(self.c_programs_dir, 'better_solver.exe')


        try:
            # 运行带参数的 better_solver.exe
            result = subprocess.run([solver_path, cnf_file_path, str(pickvar_choice)], check=True, capture_output=True, text=True, encoding='utf-8')
            print(f"Solving completed with PickVar_{pickvar_choice}, results saved to: {result_file_path}")
            print(f"Solver output: {result.stdout}")

            self.upload_ui.cdcl_address.setText(result_file_path)
            self.upload_ui.cdcl_address.show()
            
            # 读取生成的结果文件
            if os.path.exists(result_file_path):
                with open(result_file_path, 'r') as f:
                    lines = f.readlines()
                    result_status = None
                    solve_time = None
                    for line in lines:
                        if line.startswith('s'):
                            result_status = line.strip()
                        elif line.startswith('t'):
                            solve_time = line.strip().split(' ')[1]

                    if result_status == 's 1':
                        self.upload_ui.cdcl_time.setText(f"{solve_time} ms")
                        self.upload_ui.judge.setText("有解")
                    elif result_status == 's 0':
                        self.upload_ui.cdcl_time.setText(f"{solve_time} ms")
                        self.upload_ui.judge.setText("无解")

        except subprocess.CalledProcessError as e:
            print(f"Error running solver: {e}")
            print(f"Solver error output: {e.stderr}")
        except Exception as e:
            print(f"Other error: {e}")

        self.upload_ui.cdcl_time_label.show()
        self.upload_ui.cdcl_time.show()
        self.upload_ui.cdcl_address_label.show()
        self.upload_ui.cdcl_address.show()
        self.upload_ui.cdcl_button.show()

        self.upload_ui.judge_label.show()
        self.upload_ui.judge.show()
        
        self.calculate_and_display_optimization_rate()

    def calculate_and_display_optimization_rate(self):
        """计算优化率并显示"""
        dpll_time_text = self.upload_ui.dpll_time.text().replace(" ms", "")
        cdcl_time_text = self.upload_ui.cdcl_time.text().replace(" ms", "")

        # 检查 dpll_time 和 cdcl_time 是否都有值
        if cdcl_time_text and (not dpll_time_text or dpll_time_text == "(未实现)"):
            # 如果 dpll_time 没有值或为初始状态，且 cdcl_time 有值，显示为无限大
            self.upload_ui.optimization_rate.setText("∞")
            self.upload_ui.rate_label.show()
            self.upload_ui.optimization_rate.show()
        elif dpll_time_text and cdcl_time_text:
            # 如果 dpll_time 和 cdcl_time 都有值，则计算优化率
            dpll_time = float(dpll_time_text)
            cdcl_time = float(cdcl_time_text)
        
            optimization_rate = ((dpll_time - cdcl_time) / dpll_time) * 100
            self.upload_ui.optimization_rate.setText(f"{optimization_rate:.2f}%")
            self.upload_ui.rate_label.show()
            self.upload_ui.optimization_rate.show()

    def open_source_file(self):
        file_path = self.upload_ui.cnf_path.text()
        if file_path:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(file_path))

    def open_saved_file(self):
        saved_path = self.upload_ui.saved_path.text()
        if saved_path:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(saved_path))

    def open_dpll_file(self):
        dpll_path = self.upload_ui.dpll_address.text()
        if dpll_path:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(dpll_path))

    def open_cdcl_file(self):
        cdcl_path = self.upload_ui.cdcl_address.text()
        if cdcl_path:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(cdcl_path))

    def check_solution(self):
        """检查用户的答案是否正确"""
        if not os.path.exists(self.answer_file_path):
            print("Error: Solution file not found.")
            return

        correct_grid = []
        with open(self.answer_file_path, 'r') as f:
            correct_grid = [line.strip().split() for line in f.readlines()]

        table = self.game_ui.sudoku_table
        wrong_count = 0

        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item and item.text().isdigit():
                    if item.text() != correct_grid[row][col]:
                        wrong_count += 1

        if wrong_count == 0:
            self.game_ui.check_information.setText("填写全部正确！")
        else:
            self.game_ui.check_information.setText(f"您当前填错了 {wrong_count} 个数字。")

        self.game_ui.check_information.setVisible(True)
        QTimer.singleShot(5000, lambda: self.game_ui.check_information.setVisible(False))

    def peek_solution(self):
        """偷看答案"""
        table = self.game_ui.sudoku_table  # 确保 table 在函数开始时定义

        if not self.is_answer_shown:
            self.peek_count += 1

            if not os.path.exists(self.answer_file_path):
                print("Error: Solution file not found.")
                return

             # 清空并保存用户当前输入的状态
            self.previous_user_input = []

            for row in range(table.rowCount()):
                row_data = []
                for col in range(table.columnCount()):
                    item = table.item(row, col)
                    row_data.append(item.text() if item else "")
                self.previous_user_input.append(row_data)

            # 显示答案
            with open(self.answer_file_path, 'r') as f:
                answer_lines = [line.strip().split() for line in f.readlines()]

            for row in range(table.rowCount()):
                for col in range(table.columnCount()):
                    item = table.item(row, col)
                    if item and item.flags() & Qt.ItemIsEditable:  # 如果是可编辑单元格，则显示答案
                        item.setText(answer_lines[row][col])
                        item.setForeground(QtGui.QBrush(Qt.black))

            QTimer.singleShot(5000, lambda: self.hide_peek())
    
    def hide_peek(self):
        """隐藏偷看的答案"""
        table = self.game_ui.sudoku_table
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item and item.flags() & Qt.ItemIsEditable:  # 如果是可编辑单元格，则隐藏
                     # 恢复用户之前输入的内容
                    item.setText(self.previous_user_input[row][col] if self.previous_user_input else "")
                    item.setForeground(QtGui.QBrush(Qt.blue))  # 恢复为蓝色字体

    def show_solution(self):
        """显示完整的答案"""
        if not os.path.exists(self.answer_file_path):
            print("Error: Solution file not found.")
            return

        with open(self.answer_file_path, 'r') as f:
            answer_lines = [line.strip().split() for line in f.readlines()]

        table = self.game_ui.sudoku_table

        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    item.setText(answer_lines[row][col])
                    item.setForeground(QtGui.QBrush(Qt.black))

        # 停止计时但显示时间
        self.timer.stop()
        self.game_ui.game_time.setVisible(True)  # 确保游戏时间显示
        self.game_ui.game_time.setText(f"游戏时间：{self.game_time_seconds // 60:02}:{self.game_time_seconds % 60:02}")

        # 显示偷看次数
        self.game_ui.peek_count.setVisible(True)
        self.game_ui.peek_count.setText(f"偷看次数：{self.peek_count}")

        self.is_answer_shown = True

    def update_game_time(self):
        """更新游戏时间"""
        if not self.is_answer_shown:
            self.game_time_seconds += 1
            minutes = self.game_time_seconds // 60
            seconds = self.game_time_seconds % 60
            self.game_ui.game_time.setText(f"游戏时间：{minutes:02}:{seconds:02}")

    def show_rules(self):
        self.stacked_widget.setCurrentWidget(self.rules_widget)

    def show_mode(self):
        self.stacked_widget.setCurrentWidget(self.mode_widget)

    def show_upload(self):
        self.stacked_widget.setCurrentWidget(self.upload_widget)

    def show_difficulty(self):
        self.stacked_widget.setCurrentWidget(self.difficulty_widget)

    def show_game(self):
        self.game_ui.check_information.setVisible(False)
        table = self.game_ui.sudoku_table
        if table:
            table.horizontalHeader().setDefaultSectionSize(55)
            table.verticalHeader().setDefaultSectionSize(55)
            table.horizontalHeader().setMinimumSectionSize(55)
            table.verticalHeader().setMinimumSectionSize(55)
            table.setFont(QtGui.QFont("Arial", 22))
            for row in range(table.rowCount()):
                for col in range(table.columnCount()):
                    item = table.item(row, col)
                    if item is None:
                        item = QTableWidgetItem()
                        table.setItem(row, col, item)
                    item.setText("")
                    item.setTextAlignment(Qt.AlignCenter)
        # 强制刷新 UI
        table.viewport().update()
        table.repaint()

        self.stacked_widget.setCurrentWidget(self.game_widget)
        
    def show_main(self):
        self.stacked_widget.setCurrentWidget(self.start_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
