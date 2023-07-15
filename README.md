# 马里奥跑酷

![image-20230715224541334](READEME.assets/image-20230715224541334.png)

本项目《马里奥跑酷》是基于python中的pygame库实现的一款类跑酷游戏

## 操作说明


1. 运行main.py文件

   ```
   python main.py
   ```

2. 游戏主菜单时，上下选择模式（目前仅开发出单人模式，选择双人模式仍为单人）

3. 回车键开始游戏

## 游戏介绍

![image-20230715224639781](READEME.assets/image-20230715224639781.png)

1. 主人公通过键盘左右键移动，空格键跳跃
2. 碰到金币会收集起来，获得2积分
3. 从正上方落下会踩死虫子，会获得2个积分，左右碰撞到会减少一次生命
4. 踩空会减少一次生命
5. 游戏中会出现水管，砖块，地板等障碍物，无其他作用
6. 一次游戏总共有三条生命，生命数为0时游戏结束，Game over
7. 最终到达城堡游戏成功

## 文件说明

- resources存储游戏所需图片和音效
- state包括三个游戏中需要的三个界面文件（.py）
- sprite包括两个精灵类
- source包括游戏初始化一些工具型文件，const.py存储常量值

