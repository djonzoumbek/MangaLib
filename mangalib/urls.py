from django.urls import path

from .views import home, show, add, delete, edit, list_authors, add_author, show_author, edit_author, del_author

app_name = "mangalib"
urlpatterns = [
    path('', home, name='home'),
    path('<int:book_id>/', show, name='show'),
    path('add_book', add, name='add'),
    path('edit_book/<int:book_id>/', edit, name='edit'),
    path('delete_book/<int:book_id>/', delete, name='delete'),
    path('list_author/' , list_authors, name='list_authors'),
    path('add_author/', add_author, name='add_author'),
    path('show_author/<int:author_id>/', show_author, name='show_author'),
    path('edit_author/<int:author_id>/', edit_author, name='edit_author'),
    path('del_author/<int:author_id>/', del_author, name='del_author'),

]
