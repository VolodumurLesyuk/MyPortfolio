from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project
from .serializers import ProjectSerializer


class ProjectListAPIView(APIView):
    template_name = 'project/list_projects.html'
    renderer_classes = [TemplateHTMLRenderer, ]

    def get(self, request):

        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)

        return Response({'context': serializer.data})


class ProjectDetailAPIView(APIView):
    template_name = 'project/detail.html'
    renderer_classes = [TemplateHTMLRenderer, ]

    def get(self, request, pk):

        queryset = get_object_or_404(Project.objects.all(), pk=pk)
        serializer = ProjectSerializer(queryset)
        return Response({'context': serializer.data})


