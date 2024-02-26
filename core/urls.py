from django.urls import path
from . import views



urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('home/', views.home, name="home"),
    path('not_have_permissions/', views.not_have_permissions, name="not_have_permissions"),

    
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


    
    # path('bill2/', views.bill2.as_view(), name="bill2"),
    path('bill2/', views.make_bill, name="bill2"),
    # path('download-bill-pdf/<int:bill_id>/', views.download_bill_pdf, name='download_bill_pdf'),


    path('all_bills/', views.show_bills, name="all_bills"),
    # path('all_bills/', views.show_bills.as_view(), name="all_bills"),


    
    path('show_payments/', views.show_payments, name="show_payments"),
    path('add_new_payment_link/', views.add_payment_link, name="add_new_payment_link"),
    path('edit_payment_link/<slug>/', views.edit_payment_link, name="edit_payment_link"),
    path('delete_payment_link/<slug>/', views.delete_payment_link, name="delete_payment_link"),



    path("show_banks/", views.show_banks, name="show_banks"),
    path("show_bank_accounts_to_users/", views.show_bank_accounts_to_users, name="show_bank_accounts_to_users"),
    path("add_bank_account/", views.add_bank_account, name="add_bank_account"),
    path("edit_bank_account/<slug>/", views.edit_bank_account, name="edit_bank_account"),
    path("delete_bank_account/<slug>/", views.delete_bank_account, name="delete_bank_account"),



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
    path('done_tasks/', views.done_tasks, name='done_tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<slug>/', views.delete_task, name='delete_task'),
    path('my_tasks/', views.user_task, name='my_tasks'),
    path('user_done_task/<slug>/', views.user_done_task, name='user_done_task'),


    # path('online_order/', views.OnlineOrder.as_view(), name='online_order'),
    path('online_order/', views.online_order, name='online_order'),
    path('bill_edit/<slug>/', views.bill_edit, name='bill_edit'),


    path('phone_and_account_manage/', views.manage_phone_and_account, name='phone_and_account_manage'),

    # Links for the Phones model and its views
    path('all_phones/', views.show_all_phones, name='all_phones'),
    path('edit_phone/<slug>/', views.edit_phone, name='edit_phone'),
    path('delete_phone/<slug>/', views.delete_phone, name='delete_phone'),

    # Links for the PhoneNumberr model and its views
    path('users_phones/', views.show_all_user_phones, name='users_phones'),
    path('add_phone_to_user/', views.add_phone_to_user, name='add_phone_to_user'),
    path('edit_user_phone/<slug>/', views.edit_user_phone, name='edit_user_phone'),
    path('delete_user_phone/<slug>/', views.delete_user_phone, name='delete_user_phone'),

    # Links for the Account model and its views
    path('users_accounts/', views.show_all_user_accounts, name='users_accounts'),
    path('create_new_account/', views.create_new_account, name='create_new_account'),
    path('edit_user_account/<slug>/', views.edit_user_account, name='edit_user_account'),
    path('delete_user_account/<slug>/', views.delete_user_account, name='delete_user_account'),


    path("item-refund/<slug>/", views.item_refund, name="item_refund"),
    path("user-refunds", views.user_refunds, name="user_refunds"),
    path("all-refunds/", views.show_all_refunds_to_admin, name="show_all_refunds_to_admin"),



    # path('download_pdf/', views.download_pdf, name='download_pdf'),
    # path('generate_order_summary/', views.generate_order_summary, name="generate_order_summary"),
    # path('sendmail/', views.send_mail_to_all_users,name="send_mail_to_all_users"),

    path('show_final_report/', views.show_final_report, name="show_final_report"),
    path('view_final_users_report_pdf/<slug_code>/', views.view_final_users_report_pdf, name="view_final_users_report_pdf"),
    path('download_final_users_report_pdf/<slug_code>/', views.download_final_users_report_pdf, name='download_final_users_report_pdf'),


    # path('get_final_report/', views.get_final_report, name="get_final_report"),






]
