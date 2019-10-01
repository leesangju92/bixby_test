from django.shortcuts import get_object_or_404, render
from django.db.models import Q
import json, datetime

# rest framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# model
from accounts.models import User

# mongodb
from mongodb import find_query

# Create your views here.
def test(request):
    return render(request, "api/base.html")


def wines(request):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("get request")
    if request.method == "GET":
        queries = dict(request.GET)
        # query를 GET 요청으로 보낼 경우 request.GET을 dict로 변환
        # request.GET의 value 값이 list형식으로 들어와서 list에서 빼주는 for문
        # ex) {'tasting_sweetness': ['{"$gt":2}'], "CATEGORIES": "화이트와인"}
        for key, val in queries.items():
            try:
                # json.loads()를 통해 dict형식의 문자열을 dict로 변환 ex) '{"$gt":2}'
                queries[key] = json.loads(val[0])
            except ValueError:
                # "화이트와인"은 dict로 바꿀 수 없어서 list에서만 빼줌
                queries[key] = val[0]

        wine = find_query(queries)

        return Response(data={"count": len(wine), "wine": wine}, status=status.HTTP_202_ACCEPTED)

    if request.method == "POST":
        queries = request.data
        wine = find_query(queries)

        return Response(data={"count": len(wine), "wine": wine}, status=status.HTTP_202_ACCEPTED)
