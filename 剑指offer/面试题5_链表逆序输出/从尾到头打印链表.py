# -*- coding: utf-8 -*-
__date__ = '2020/1/1 16:20'


RES = []  # 全局变量用作存储逆置后的结果


class SingleNode:
    """单链表节点"""

    def __init__(self, item):
        self.item = item  # 结点存放数据
        self.next = None  # 后继结点


class SingleLinkList:
    """ 单链表 """

    def __init__(self):
        self.head = None

    def is_empty(self):  # 链表是否为空
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur:  # 只要指针不空
            count += 1
            cur = cur.next  # 指针后移
        return count

    def travel(self):
        """ 遍历链表 """
        cur = self.head
        while cur:
            print(cur.item, end='->')
            cur = cur.next
        print(None)  # 链表最后指针指向None

    def add(self, item):
        """ 头插法 """
        node = SingleNode(item)  # 新建一个结点
        node.next = self.head
        self.head = node

    def append(self, item):
        """ 尾插法 """
        node = SingleNode(item)  # 新建一个结点
        if self.is_empty():  # 链表为空
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node


def print_from_tail_linklist(linklist=None):
    """ 非递归从尾到头打印链表 """
    if linklist == None:
        return None
    else:
        stack = []  # 用列表模拟栈
        cur = linklist.head
        while cur != None:
            stack.append(cur.item)
            cur = cur.next

        while len(stack) > 0:
            RES.append(stack.pop(-1))
        return RES


def print_from_tail_linklist_recur(node=None, res=RES):
    """ 递归从尾到头打印链表 """
    if node:
        print_from_tail_linklist_recur(node.next, RES)
        RES.append(node.item)
    return RES





if __name__ == "__main__":
    linklist = SingleLinkList()

    linklist.append(1)
    linklist.append(2)
    linklist.append(3)
    linklist.append(4)
    linklist.travel()

    # 1,非递归
    # print(print_from_tail_linklist(linklist))

    # 2,递归
    node = linklist.head
    print(print_from_tail_linklist_recur(node, RES))