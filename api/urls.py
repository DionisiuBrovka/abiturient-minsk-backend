from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', RootView.as_view({'get': 'list'}), name='api-v1'),
    path('establishment/', EstablismentListView.as_view({'get': 'list'}), name='establishments'),
    path('establishment/<int:pk>/', EstablismentDetailView.as_view({'get': 'list'})),
    path('speciality/', SpecialityListView.as_view({'get': 'list'}), name='specialitys'),
    path('speciality/sso/', SpecialitySSOListView.as_view({'get': 'list'}), name='specialitys-sso'),
    path('speciality/pto/', SpecialityPTOListView.as_view({'get': 'list'}), name='specialitys-pto'),
    path('speciality/<int:pk>/', SpecialityDetailView.as_view({'get': 'list'})),
    path('skill/', SkillListView.as_view({'get': 'list'}), name='skills'),
    path('skill/<int:pk>/', SkillDetailView.as_view({'get': 'list'}),),
    path('skill/linked/', SkillLinkedListView.as_view({'get': 'list'}), name='skills-linked'),
    path('skill/<int:pk>/est/', SkillESTListView.as_view({'get': 'list'}), name='specialitys-est'),
    path('skill/sso/', SkillSSOListView.as_view({'get': 'list'}), name='skills-sso'),
    path('skill/pto/', SkillPTOListView.as_view({'get': 'list'}), name='skills-pto'),
    path('skill/linked/sso/', SkillLinkedSSOListView.as_view({'get': 'list'}), name='skills-linked-sso'),
    path('skill/linked/pto/', SkillLinkedPTOListView.as_view({'get': 'list'}), name='skills-linked-pto'),
    path('event/', EventsListView.as_view({'get': 'list'}), name='events'),
    path('event/<int:pk>/', EventsDetailView.as_view({'get': 'list'})),
    path('faq/', FAQListView.as_view({'get': 'list'}), name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)