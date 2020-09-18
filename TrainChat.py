#!/usr/bin/python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


my_bot = ChatBot(
    "Training demo",
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///db.sqlite3')

list_trainer = ListTrainer(my_bot)
# 直接写语句训练
list_trainer.train(["你叫什么名字？", "我叫小白兔！", ])
list_trainer.train([
    "Test1",
    "Test2",
    "Test3",
    "Test4",
])
# 使用自定义语句训练它
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train( r"./chatbot/")
