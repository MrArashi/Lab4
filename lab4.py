#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 
import os

class MTable:

    def msg():
        print("")
        print("Если вы хотите вывести пользователей на экран, введите 'l'")
        print("Если вы хотите добавить пользователя, введите 'a'")
        print("Если вы хотите удалить пользователя, введите 'd'")
        print("Если вы хотите провести поиск данных, введите 'o'")
        print("Выход из программы - 'e'")
        print("")
    def preview():
        print("")
        print("Name-1")
        print("Surname-2")
        print("Address-3")
        print("Company-4")
        print("Date-5")
        print("Meeting-6")
        print("Phone-7")
        print("")
            
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def create(TableName, Fields):
        db = sqlite3.connect(os.path.abspath(__file__)+'.db')
        sql = db.cursor()
        sql.execute("CREATE TABLE IF NOT EXISTS " + TableName + " (" + Fields + ")")
        db.commit()
        db.close()

    def insert(TableName, Fields, Values):
        db = sqlite3.connect(os.path.abspath(__file__)+'.db')
        sql = db.cursor()
        sql.execute("INSERT INTO " + TableName + " (" + Fields + ") VALUES (" + Values + ")")
        db.commit()
        db.close()

    def select(TableName, Fields):
        db = sqlite3.connect(os.path.abspath(__file__)+'.db')
        sql = db.cursor()
        for values in sql.execute("SELECT " + Fields + " FROM " + TableName):
            print(values)
        db.close()

    def selectWhere(TableName, Field, WhereField, WhereValues):
        db = sqlite3.connect(os.path.abspath(__file__)+'.db')
        sql = db.cursor()
        for values in sql.execute("SELECT " + Field + " FROM " + TableName + " WHERE " + WhereField + " LIKE " + "'%" + WhereValues + "%'"):
            print(values)
        db.close()
    
    def delete(TableName, Fields, WhereValues):
        db = sqlite3.connect(os.path.abspath(__file__)+'.db')
        sql = db.cursor()
        sql.execute("DELETE FROM " + TableName + " WHERE " + Fields + " = " + WhereValues)
        db.commit()
        db.close()


MTable.create("organizer", "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, surname TEXT, address TEXT, company TEXT, date TEXT, meeting TEXT, phone INTEGER")
MTable.clear()
infinity = 1

while infinity == 1:
    MTable.msg()
    l = input("Введите символ: ");  

    if(l!='l' or l!='a' or l!='d' or l!=o or l!=e):
       MTable.clear()

    if l == "l":
        MTable.clear()
        MTable.select("organizer", "*")

    elif l == "a":
        MTable.clear()
        name = str("'"+input('Имя: ')+"', ")
        surname = str("'"+input('Фамилия: ')+"', ")
        address = str("'"+input('Адрес: ')+"', ")
        company = str("'"+input('Компания: ')+"', ")
        date = str("'"+input('Расписание: ')+"', ")
        meeting = str("'"+input('Встреча: ')+"', ")
        phone = int(input('Телефон: '))
        s = name + surname + address + company + date + meeting + str(phone)
        MTable.insert("organizer", "name, surname, address, company, date, meeting, phone", s)

    elif l == "d":
        MTable.clear()
        MTable.select("organizer", "*")
        x = input("Номер пользователя, которого хотите удалить: ")
        MTable.delete("organizer", "ID", x)
        MTable.clear()
        MTable.select("organizer", "*")
        print("Номер пользователя, которого удалили был: " + x)

    elif l == "o":
        MTable.clear()
        MTable.preview()
        a = int(input("Вид данных: "))
        
        if a == 1:
            x = "name"
        elif a == 2:
            x = "surname"
        elif a == 3:
            x = "address"
        elif a == 4:
            x = "company"
        elif a == 5:
            x = "date"
        elif a == 6:
            x = "meeting"        
        elif a == 7:
            x = "phone"
        print ("Your choice " + x)
        y = str(input("Ввод данных: "))
        print("")
        print("Список")
        MTable.selectWhere("organizer", "*", x, y)
       
    elif l == "e":
        quit()