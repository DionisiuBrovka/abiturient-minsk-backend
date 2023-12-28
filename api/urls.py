from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', MainView.as_view({'get': 'list'})),
    path('api/v1/', RootView.as_view({'get': 'list'}), name='api-v1'),
    path('api/v1/establishment/', EstablismentListView.as_view({'get': 'list'}), name='establishments'),
    path('api/v1/establishment/<int:pk>/', EstablismentDetailView.as_view({'get': 'list'})),
    path('api/v1/speciality/', SpecialityListView.as_view({'get': 'list'}), name='specialitys'),
    path('api/v1/speciality/sso/', SpecialitySSOListView.as_view({'get': 'list'}), name='specialitys-sso'),
    path('api/v1/speciality/pto/', SpecialityPTOListView.as_view({'get': 'list'}), name='specialitys-pto'),
    path('api/v1/speciality/<int:pk>/', SpecialityDetailView.as_view({'get': 'list'})),
    path('api/v1/skill/', SkillListView.as_view({'get': 'list'}), name='skills'),
    path('api/v1/skill/<int:pk>/', SkillDetailView.as_view({'get': 'list'}),),
    path('api/v1/skill/linked/', SkillLinkedListView.as_view({'get': 'list'}), name='skills-linked'),
    path('api/v1/skill/<int:pk>/est/', SkillESTListView.as_view({'get': 'list'}), name='specialitys-est'),
    path('api/v1/skill/sso/', SkillSSOListView.as_view({'get': 'list'}), name='skills-sso'),
    path('api/v1/skill/pto/', SkillPTOListView.as_view({'get': 'list'}), name='skills-pto'),
    path('api/v1/skill/linked/sso/', SkillLinkedSSOListView.as_view({'get': 'list'}), name='skills-linked-sso'),
    path('api/v1/skill/linked/pto/', SkillLinkedPTOListView.as_view({'get': 'list'}), name='skills-linked-pto'),
    path('api/v1/event/', EventsListView.as_view({'get': 'list'}), name='events'),
    path('api/v1/event/<int:pk>/', EventsDetailView.as_view({'get': 'list'})),
    path('api/v1/faq/', FAQListView.as_view({'get': 'list'}), name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)