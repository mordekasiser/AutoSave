# AutoSave

AutoSave 助手是一款实用的自动保存工具，由两个核心组件构成：进程监控器和快捷键触发器。进程监控器负责实时检测指定应用程序的运行状态，而快捷键触发器则按照预设的时间间隔，自动模拟按下 Ctrl+S 组合键来触发保存操作。这款工具特别适合那些需要频繁保存工作内容，但容易忘记手动保存的用户，可以有效防止因意外情况导致的工作内容丢失。

## 使用说明及修改指南

使用前的重要提醒：这个自动保存程序仅适用于支持Ctrl+S快捷键保存的软件。在启动自动保存前，请务必先手动打开目标程序，并使用"另存为"功能将文件保存到你想要的位置，这样后续的自动保存才会保存在正确的路径下。

首先运行"检测进程"程序，通过它查看需要自动保存的目标程序的进程名称。运行后程序会显示当前激活窗口的进程名，找到你需要自动保存的程序时，记录下它的进程名称，然后你就可以关闭了。注意：记录的进程名必须全部使用小写字母（比如mindmaster.exe，而不是MindMaster.exe）。

接下来打开"定向保存"程序进行修改。你需要找到代码中的 target_process = "mindmaster.exe" 这行，将引号中的进程名替换为你刚才记录的目标程序进程名（记住保持全小写）。如果想调整自动保存的时间间隔，修改 time.sleep(10) 中的数值，这个数值代表秒数，比如要设置5分钟就改为300。如果需要更改退出程序的快捷键，可以修改 keyboard.add_hotkey('ctrl+q') 中的组合键设置。

完成修改后运行这个"定向保存"程序，它会在后台持续运行，并将所有的保存操作记录在日志文件中。你可以通过设定的快捷键（默认是Ctrl+Q）来退出程序。

# AutoSave

AutoSave Assistant is a practical auto-save tool consisting of two core components: a process monitor and a hotkey trigger. The process monitor is responsible for real-time detection of the specified application's running status, while the hotkey trigger automatically simulates pressing the Ctrl+S key combination at preset time intervals to trigger the save operation. This tool is particularly suitable for users who need to frequently save their work content but tend to forget to save manually, effectively preventing loss of work due to unexpected situations.

## Usage Instructions and Modification Guide

Important reminder before use: This auto-save program only works with software that supports the Ctrl+S shortcut key for saving. Before starting the auto-save function, you must first manually open the target program and use the "Save As" function to save the file to your desired location, ensuring that subsequent auto-saves will be stored in the correct path.

First, run the "Process Identification" program to view the process name of the target program you want to auto-save. Once running, the program will display the process name of the currently active window. When you find the program you need to auto-save, note down its process name, note down its process name. Note: The recorded process name must be in all lowercase letters (for example, mindmaster.exe, not MindMaster.exe).

Next, open the "Specific Application Saving" program for modification. You need to find the line target_process = "mindmaster.exe" in the code and replace the process name in quotes with your target program's process name (remember to keep it lowercase). If you want to adjust the auto-save interval, modify the value in time.sleep(10), where this value represents seconds - for example, change it to 300 for a 5-minute interval. If you need to change the program exit shortcut, you can modify the key combination in keyboard.add_hotkey('ctrl+q').

After completing the modifications, run this "Specific Application Saving" program. It will continue running in the background and log all save operations to a log file. You can exit the program using the configured shortcut key (default is Ctrl+Q).
