from django.views.generic import ListView

from todo_list.todo_app.models import ToDoItem, TodoList


class ListTodoLists(ListView):
    model = TodoList
    template_name = "todo_app/index.html"
    # context_object_name = "object_list"
    # paginate_by = 10
    # ordering = ["title"]
    # queryset = TodoList.objects.all()


list_todolists_view = ListTodoLists.as_view()


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/item_list.html"
    # context_object_name = "object_list"
    # paginate_by = 10
    # ordering = ["-created_date"]
    # queryset = ToDoItem.objects.all()

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = TodoList.objects.get(id=self.kwargs["list_id"])
        return context


list_ItemTodolists_view = ItemListView.as_view()
