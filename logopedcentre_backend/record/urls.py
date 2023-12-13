from django.urls import path, include
from record import views

urlpatterns = [
    path('latest-directions/', views.LatestDirectionsList.as_view()),
    path('latest-specialists/', views.LatestSpecialistsList.as_view()),
    path('direction-specialists/<slug:direction_slug>/', views.DirectionSpecialistsList.as_view()),
    path('account/<slug:user_id>/info/', views.AccountInfoDetail.as_view()),
    path('account/<slug:user_id>/children_info/', views.AccountChildrensInfoDetail.as_view()),
    path('account/<slug:user_id>/remove_info/', views.DeleteAccountDetail.as_view()),
    path('get_user_id/<slug:token>/', views.UserIdDetail.as_view()),
    path('account/add_info/', views.addInfoAccount),
    path('account/edit_info/', views.editInfoAccount),
    path('account/add_children/', views.addChildren),
    path('record/add_record_children/',views.addRecord),
    path('account/delete_children/', views.deleteChildren),
    path('specialist/get_shedule/<slug:specialist_id>/', views.LatestSpecialistShedule.as_view()),
    path('directions/<slug:direction_slug>', views.LatestDirectionsList.as_view()),

    # path('products/search/', views.search),
    # path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view()),
    # path('products/<slug:category_slug>', views.CategoryDetail.as_view())
]

