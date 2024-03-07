from django.urls import path
from apps.cart.views import CartListViews, QuantityChangeLogics, create_cart_item,create_cart_item_flour, QuantityChangeLogicsFlour
from . import views
urlpatterns = [
    path('cart', CartListViews.as_view(), name='cart_list'),
    path('minus/<int:pk>/', QuantityChangeLogics.minus_quantity, name='minus_quantity'),
    path('pilus/<int:pk>/', QuantityChangeLogics.pilus_quantity, name='pilus_quantity'),
    path('minus_flour/<int:pk>/', QuantityChangeLogicsFlour.minus_quantity_flour, name='minus_quantity_flour'),
    path('pilus_flour/<int:pk>/', QuantityChangeLogicsFlour.pilus_quantity_flour, name='pilus_quantity_flour'),
    path('add_to_cart/<int:pk>/', create_cart_item, name='add_to_cart'),
    path('add_to_cart_flour/<int:pk>/', create_cart_item_flour, name='add_to_cart_flour'),
    path('card/', views.detail_card, name="detail_card"),
]
