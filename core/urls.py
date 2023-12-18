from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name="home"),
    path('item_detail/<slug>/', views.item_detail, name='item_detail'),
    path('have_offer/', views.have_offer, name="have_offer"),
    path('new_arrived/', views.new_arrived, name="new_arrived"),
    path('best_seller/', views.best_seller, name="best_seller"),





    path('shop/', views.shop, name="shop"),
    path('store/', views.store, name="store"),
    # path('add_product/', views.add_product, name="add_product"),
    path('add_item/', views.add_item, name="add_item"),
    path('edit_item_in_store/<slug>/', views.edit_item_in_store, name="edit_item_in_store"),
    path('delete_from_store/<slug>/', views.delete_from_store, name="delete_from_store"),


    


    path('order_summary/', views.order_summary, name="order_summary"),
    path('add-to-cart/<slug>/', views.add_to_cart, name="add-to-cart"),
    path('remove_single_item_from_cart/<slug>/', views.remove_single_item_from_cart, name="remove_single_item_from_cart"),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name="remove_from_cart"),


    # path('bill/', views.bill, name="bill"),
    # path('bill/', views.bill.as_view(), name="bill"),
    path('bill2/', views.bill2.as_view(), name="bill2"),

    path('all_bills/', views.show_bills, name="all_bills"),
    # path('all_bills/', views.show_bills.as_view(), name="all_bills"),


    
    path('banks_and_payments/', views.banks, name="banks_and_payments"),
    path('add_new_payment_link/', views.add_payment_link, name="add_new_payment_link"),
    path('delete_payment_link/<slug>/', views.delete_payment_link, name="delete_payment_link"),


    path('chart-data/', views.chart_data, name='chart_data'),
    path('chart/', views.chart_view, name='chart_view'),

    path('add_penality/', views.penality, name='add_penality'),
    path('show_all_penalities/', views.show_all_penalities, name='show_all_penalities'),
    path('my_penalities/', views.user_penality, name='my_penalities'),
    path('delete_penality/<slug>/', views.delete_penality, name='delete_penality'),


    path('show_all_rewards/', views.show_all_rewards, name='show_all_rewards'),
    path('add_reward/', views.reward, name='add_reward'),
    path('delete_reward/<slug>/', views.delete_reward, name='delete_reward'),
    path('my_rewards/', views.user_reward, name='my_rewards'),




    path('show_all_tasks/', views.show_all_tasks, name='show_all_tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<slug>/', views.delete_task, name='delete_task'),
    path('my_tasks/', views.user_task, name='my_tasks'),


    path('online_order/', views.OnlineOrder.as_view(), name='online_order'),

]
