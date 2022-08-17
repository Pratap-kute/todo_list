from django.contrib import admin

from todo_list.todo_app.models import ToDoItem, TodoList

admin.site.register(ToDoItem)
admin.site.register(TodoList)
