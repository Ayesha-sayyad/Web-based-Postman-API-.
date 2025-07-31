from django.shortcuts import render

# Create your views here.
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SumRequest
'''
@api_view(['POST'])
def calculate_sum(request):
    try:
        nums = request.data.get("numbers", [])
        nums_sorted = sorted(nums)
        nums_json = json.dumps(nums_sorted)

        # Check if the request already exists
        existing = SumRequest.objects.filter(numbers=nums_json).first()
        if existing:
            return Response({"sum": existing.result, "cached": True})

        result = sum(nums_sorted)
        SumRequest.objects.create(numbers=nums_json, result=result)
        return Response({"sum": result, "cached": False})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['POST'])
def calculate_sum(request):
    try:
        numbers = request.data.get("numbers", [])
        numbers_sorted = sorted(numbers)
        numbers_json = json.dumps(numbers_sorted)

        existing = SumRequest.objects.filter(numbers=numbers_json).first()
        if existing:
            print(f"[CACHE HIT] Numbers: {numbers_sorted}, Sum: {existing.result}")
            return Response({"sum": existing.result, "cached": True})

        total = sum(numbers_sorted)
        SumRequest.objects.create(numbers=numbers_json, result=total)
        print(f"[NEW CALCULATION] Numbers: {numbers_sorted}, Sum: {total}")
        return Response({"sum": total, "cached": False})

    except Exception as e:
        print(f"[ERROR] {e}")
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
