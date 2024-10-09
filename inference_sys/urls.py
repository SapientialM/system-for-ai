from django.urls import path
from . import views

urlpatterns = [
    path('forward', views.forward, name='forward'),
    path('reverse', views.reverse, name='reverse'),
    path('rules', views.rules, name='rules'),
    path('operations/get_rules', views.get_rules, name='get_rules'),  # 添加获取规则的视图
    path('operations/add_rule', views.add_rule, name='add_rule'),
    path('operations/delete_rule', views.delete_rule, name='delete_rule'),
    path('operations/edit_rule', views.edit_rule, name='edit_rule'),
    path('operations/get_facts', views.get_facts, name='get_facts'),
    path('operations/get_facts_conclusions', views.get_facts_conclusions, name='get_facts_conclusions'),
    path('operations/add_fact', views.add_fact, name='add_fact'),
    path('operations/delete_fact', views.delete_fact, name='delete_fact'),
    path('operations/edit_fact', views.edit_fact, name='edit_fact'),
    path('operations/batch_add_facts', views.batch_add_facts, name='batch_add_facts'),
    path('operations/forward_rules', views.forward_rules, name='forward_rules'),
    path('operations/reverse_fact', views.reverse_fact, name='reverse_fact'),
]
