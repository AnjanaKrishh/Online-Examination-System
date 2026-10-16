from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionsDb
from ExamApp.serializer import QuestionsSerializer


class QuestionListView(APIView):

    def get(self, request):
        qs = QuestionsDb.objects.all()
        serializer = QuestionsSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Question added successfully"
            })

        return Response(serializer.errors)
class QuestionDetailView(APIView):

    def get(self, request, id):
        qs = QuestionsDb.objects.get(id=id)
        serializer = QuestionsSerializer(qs)
        return Response(serializer.data)

    def put(self, request, id):
        qs = QuestionsDb.objects.get(id=id)
        serializer = QuestionsSerializer(qs, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Question updated successfully"
            })

        return Response(serializer.errors)

    def delete(self, request, id):
        qs = QuestionsDb.objects.get(id=id)
        qs.delete()

        return Response({
            "message": "Question deleted successfully"
        })