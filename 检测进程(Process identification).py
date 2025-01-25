import win32gui
import win32process
import psutil
import time

def print_window_process():
    try:
        print("\n按 Ctrl+C 退出程序")
        while True:
            # 获取当前窗口句柄
            hwnd = win32gui.GetForegroundWindow()
            # 获取窗口标题
            window_title = win32gui.GetWindowText(hwnd)
            # 获取进程信息
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process_name = psutil.Process(pid).name()
            
            print(f"\n当前窗口信息:")
            print(f"标题: {window_title}")
            print(f"进程名称: {process_name}")
            print("-" * 50)
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n程序已退出")

if __name__ == "__main__":
    print_window_process()