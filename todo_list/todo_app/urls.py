from django.urls import path

from todo_list.todo_app.views import (
    createtodolist_view,
    list_ItemTodolists_view,
    list_todolists_view,
)

# always metion the app name in the urls file
app_name = "todo_app"

urlpatterns = [
    path("", list_todolists_view, name="todolists_index"),
    path("list/<int:list_id>/", list_ItemTodolists_view, name="list"),
    # CRUD pattern for todolists
    path("list/add/", createtodolist_view, name="add_list"),
]
