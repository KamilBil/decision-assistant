from rest_framework import viewsets, permissions
from .models import DecisionTree
from .serializers import DecisionTreeSerializer

class DecisionTreeViewSet(viewsets.ModelViewSet):
    queryset = DecisionTree.objects.all()
    serializer_class = DecisionTreeSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.decisiontree_set.all()
