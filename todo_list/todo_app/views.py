from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

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


class CreateTodoList(CreateView):
    model = TodoList
    fields = ["title"]

    # template_name = "todo_app/create_todo_list.html"

    # def get_success_url(self):
    #     return reverse("todo_app:list_todolists")

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context


createtodolist_view = CreateTodoList.as_view()


class CreateToDoItem(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    # template_name = "todo_app/create_todo_item.html"
    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = TodoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = TodoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list.id])


createtodoitem_view = CreateToDoItem.as_view()


class UpdateToDoItem(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list" "title",
        "description",
        "due_date",
    ]

    # template_name = "todo_app/create_todo_item.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Update item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list.id])
