import time


# 通过生成器实现单线程下的并行效果
def consumer(name):
    print('%s 准备吃包子！ ' %name)
    while True:
        baozi = yield
        print('包子[%s]来了，被[%s]吃了！ ' %(baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('开始准备做包子了')
    for i in range(1, 4):
        time.sleep(1)
        print('做了一个包子，分两半！')
        c.send(i)
        c2.send(i)


# c = consumer('CRH')
# c.__next__()

producer('alex')