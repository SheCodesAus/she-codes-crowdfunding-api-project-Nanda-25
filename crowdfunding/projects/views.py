from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, permissions

from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, CustomUserSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

class ProjectListFilter(generics.ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['owner', 'date_created', 'is_open']

class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly
    ]
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

class LikeListCreate(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Project.objects.get(pk=pk).bookmarked_by.all()
    
    def create(self, request, *args, **kwargs):
        qs = self.get_queryset()
        pk = self.kwargs["pk"]
        project = Project.objects.get(pk=pk)
        if qs.filter(id=self.request.user.id).exists():
            project.bookmarked_by.remove(self.request.user)
        else: 
            project.bookmarked_by.add(self.request.user)
        serializer = self.get_serializer(project.bookmarked_by.all(), many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
