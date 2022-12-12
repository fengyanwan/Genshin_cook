# genshin_cook
原神烹饪半自动 genshin impact cook helper

需要模块：time、random、numpy、pyautogui、pillow

游戏是管理员模式运行，解释器也要管理员权限才能操作鼠标，我用的pycharm，其他ide没试过。

思路：将每个画面截图，在圆环区域找出深黄色区域，下次截图时比较深黄色区域内是不是出现了白色点，出现白色则说明时机已到，快快起锅

目前还有很多地方不够完美，有时候点了没反应，直接卡住。有时候材料不够直接退了。不说了，砍木头做家具去了
