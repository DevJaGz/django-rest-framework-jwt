from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models


class TodoListView(APIView):
    """Listar Todos"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        try:
            todos = models.Todo.objects.filter(user_id=user.id)
            serializer = serializers.TodoSerializer(todos, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Exception": str(e)})
