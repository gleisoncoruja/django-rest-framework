from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),  # home
    path('recipes/search/', views.RecipeSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/',
         views.RecipeCategory.as_view(), name="category"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),
    path(
        'recipes/api/v1/',
        views.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1"),

    path(
        'recipes/api/v1/<int:pk>/',
        views.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail"),

    path('recipes/theory/', views.theory, name="theory"),

    path('recipes/tags/<slug:slug>',
         views.RecipeListViewTag.as_view(),
         name="tag"
         ),

    path(
        'recipes/api/v2/',
        views.RecipeAPIv2List.as_view(),
        name='recipes_api_v2'
    ),

    path(
        'recipes/api/v2/<int:pk>/',
        views.RecipeAPIv2Detail.as_view(),
        name="recipes_api_v2_detail"
    ),

    path(
        'recipes/api/v2/tag/<int:pk>/',
        views.recipe_api_tag,
        name="recipes_api_v2_tag"
    ),


]