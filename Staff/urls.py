from django.urls import path
from Staff.views import shome,d_p_viewdata,add_test,applytest
urlpatterns = [
    path('',shome,name="shome"),
    path('pdviewdata',d_p_viewdata,name="pdviewdata"),
    path('add_test',add_test,name="add_test"),
    path('applytest',applytest,name="applytest"),

]