# '''
# 需要安装的库：
# pip install pyautogui
# pip install keyboard
# pip install pywin32
# pip install psutil
# '''
import time
import pyautogui
import keyboard
import sys
from datetime import datetime
import logging
import win32gui
import win32process
import psutil

# 配置日志_autosave（日记名）
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('autosave.log'),
        logging.StreamHandler()
    ]
)

def get_active_process():
    """获取当前激活窗口的进程名称"""
    try:
        # 获取当前窗口句柄
        hwnd = win32gui.GetForegroundWindow()
        # 获取进程ID
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        # 获取进程名称
        process_name = psutil.Process(pid).name().lower()
        return process_name
    except:
        return ""

def auto_save():
    try:
        # 设置目标进程名称
        target_process = "mindmaster.exe"
        
        while True:
            # 等待5分钟（测试的时候可以调成30秒，反正时间自己改）
            time.sleep(10)  # 300秒
            
            # 检查当前激活窗口是否是目标程序
            current_process = get_active_process()
            
            if current_process == target_process:
                # 按下Ctrl+S_触发按键
                pyautogui.hotkey('ctrl', 's')
                
                # 记录保存时间
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.info(f"MindMaster文件已自动保存 - {current_time}")
            
    except KeyboardInterrupt:
        logging.info("自动保存程序已停止")
        sys.exit()

def main():
    logging.info("自动保存程序已启动")
    logging.info("按下 Ctrl+Q 可以退出程序")
    logging.info("目标程序: MindMaster")
    
    # 退出快捷键_反正自己改，也可以后台直接关
    keyboard.add_hotkey('ctrl+q', lambda: sys.exit())
    
    # 启动自动保存
    auto_save()

if __name__ == "__main__":
    main()