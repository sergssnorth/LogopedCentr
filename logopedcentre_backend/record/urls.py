from django.urls import path, include
from record import views

urlpatterns = [
    path('latest-directions/', views.LatestDirectionsList.as_view()),
    path('latest-specialists/', views.LatestSpecialistsList.as_view()),
    path('direction-specialists/<slug:direction_id>/', views.DirectionSpecialistsList.as_view()),
    
    
    
    path('directions/<slug:direction_slug>', views.LatestDirectionsList.as_view()),

    # path('products/search/', views.search),
    # path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view()),
    # path('products/<slug:category_slug>', views.CategoryDetail.as_view())
]

