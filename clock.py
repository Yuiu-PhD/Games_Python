# for more detail, please refer https://docs.python.org/zh-cn/3/library/turtle.html
import turtle as hg
from datetime import *


def skip(step):  # 移动一定距离
    # 抬起画笔，向前运动一段距离放下
    hg.penup()
    hg.forward(step)
    hg.pendown()


def mkHand(name, length):  # 画指针
    # 注册Turtle形状，建立表针Turtle
    hg.reset()
    # 先反向运动一段距离，终点作为绘制指针的起点
    skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    hg.begin_poly()
    hg.forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    hg.end_poly()
    # 返回最后记录的多边形。
    handForm = hg.get_poly()
    hg.register_shape(name, handForm)


def init():
    global secHand, minHand, houHand, printer
    # 重置Turtle指向北
    hg.mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("houHand", 90)
    secHand = hg.Turtle()
    secHand.shape("secHand")
    minHand = hg.Turtle()
    minHand.shape("minHand")
    houHand = hg.Turtle()
    houHand.shape("houHand")

    for hand in secHand, minHand, houHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    # 建立输出文字Turtle
    printer = hg.Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()


def setupClock(radius):  # 绘制表盘
    # 建立表的外框
    hg.reset()
    hg.pensize(7)
    for i in range(60):
        # 向前移动半径值
        skip(radius)
        if i % 5 == 0:
            # 画长刻度线
            hg.forward(20)
            # 回到中心点
            skip(-radius - 20)

            # 移动到刻度线终点
            skip(radius + 20)
            # 下面是写表盘刻度值,为了不与划线重叠，所以对于特殊位置做了处理
            if i == 0:
                hg.write(int(12), align="center",
                         font=("Courier", 14, "bold"))
            elif i == 30:
                skip(25)
                hg.write(int(i/5), align="center",
                         font=("Courier", 14, "bold"))
                skip(-25)
            elif (i == 25 or i == 35):
                skip(20)
                hg.write(int(i/5), align="center",
                         font=("Courier", 14, "bold"))
                skip(-20)
            else:
                hg.write(int(i/5), align="center",
                         font=("Courier", 14, "bold"))

            # 回到中心点
            skip(-radius - 20)
        else:
            # 画圆点
            hg.dot(5)
            skip(-radius)
        # 顺时针移动6°
        hg.right(6)


def week(t):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %02d %02d" % (y, m, d)


def tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    houHand.setheading(30 * hour)

    hg.tracer(False)
    printer.pencolor("red")
    printer.forward(100)
    printer.write("Yuiu", align="center", font=("Courier New", 20, "bold"))
    printer.pencolor("blue")
    printer.back(180)
    printer.write(date(t), align="center", font=("Courier New", 14, "bold"))
    printer.back(20)
    printer.write(week(t), align="center", font=("Courier New", 14, "bold"))
    printer.home()
    hg.tracer(True)

    # 100ms后继续调用tick
    hg.ontimer(tick, 100)


def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    hg.tracer(False)
    init()
    setupClock(160)
    hg.tracer(True)
    tick()
    hg.mainloop()


if __name__ == "__main__":
    main()
