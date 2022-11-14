from django.urls import path

from todo_list.todo_app.views import (
    createtodoitem_view,
    createtodolist_view,
    itemdelete_view,
    list_ItemTodolists_view,
    list_todolists_view,
    listdelte_view,
    updatetodoitem_view,
)

# always metion the app name in the urls file
app_name = "todo_app"

urlpatterns = [
    path("", list_todolists_view, name="todolists_index"),
    path("list/<int:list_id>/", list_ItemTodolists_view, name="list"),
    path("list/<int:pk>/delete/", listdelte_view, name="list-delete"),
    # CRUD pattern for todolists
    path("list/add/", createtodolist_view, name="add_list"),
    path("list/<int:list_id>/item/add", createtodoitem_view, name="item-add"),
    path("list/<int:list_id>/item/<int:pk>", updatetodoitem_view, name="item-update"),
    path(
        "list/<int:list_id>/item/<int:pk>/delete", itemdelete_view, name="item-delete"
    ),
]
