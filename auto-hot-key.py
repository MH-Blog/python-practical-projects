# -*- coding: utf-8 -*-
# @Time  : 2019/12/20 下午12:45
# @Author: MagicHuang
# @File  : auto-got-key

"""
定制自己的快捷键
pynput文档：https://pythonhosted.org/pynput/index.html

"""
from pynput.keyboard import Controller, Listener, Key
import time
from threading import Thread


class ComboListener:
    def __init__(self):
        self._cur_keys = []
        self._keymap = {
            'aaa': 'hello world',
            'bbb': 'good game'
        }
        self._run()

    def _on_press(self, key):
        try:
            self._cur_keys.append(key.char)
        except AttributeError:
            self._cur_keys.append(key.name)

    def _run(self):
        l = Listener(on_press=self._on_press)
        l.daemon = True
        l.start()

        cleanerThread = Thread(target=self._cleaner)
        cleanerThread.daemon = True
        cleanerThread.start()

    def get_combo(self):
        if len(self._cur_keys) >= 3:
            combo = self._cur_keys[-3:]
            return combo

    def _cleaner(self):
        while True:
            time.sleep(0.7)
            self._cur_keys.clear()

    def get_parsed_comob(self):
        combo = self.get_combo()
        if combo:
            key = ''.join(combo)
            if key in self._keymap.keys():
                return self._keymap[key]


def send(combo_content):
    for _ in range(3):
        k.press(Key.backspace)
        k.release(Key.backspace)
    k.type(combo_content)


cl = ComboListener()
k = Controller()
while True:
    combo_conten = cl.get_parsed_comob()
    if combo_conten:
        send(combo_conten)
