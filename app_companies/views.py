from django.shortcuts import render
from .models import Company
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getAllCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createCompany(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def companyDetail(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



# VISTAS QUE LLAMAN A LA API Y DEVUELVEN HTMLS
import requests
from django.shortcuts import redirect, get_object_or_404

def company_dashboard(request, id):
    api_url = f"http://127.0.0.1:8000/companies/{id}/detail/"  # URL de la API
    response = requests.get(api_url)

    if response.status_code == 200:
        company = response.json()
    else:
        company = None  # si la API falla, devolvemos None

    return render(request, 'app_companies/dashboard.html', {'company': company})

def update_company(request, id):
    api_url = f"http://127.0.0.1:8000/companies/{id}/detail/"
    response = requests.get(api_url)

    if response.status_code == 200:
        company = response.json()
    else:
        return render(request, "app_companies/update_company.html", {"error": "Error al obtener datos."})

    if request.method == "POST":
        data = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "phone": request.POST["phone"],
            "address": request.POST["address"],
            "user_id": company["user_id"],
        }

        # hacemos la petición PUT a la API para actualizar los datos
        update_url = f"http://127.0.0.1:8000/companies/{id}/update/"
        update_response = requests.put(update_url, data=data)

        if update_response.status_code == 200:
            return redirect(f"/companies/{id}/dashboard/")  # Redirige de vuelta al dashboard
        else:
            return render(request, "app_companies/update_company.html", {
                "company": company,
                "error": "Error al actualizar la empresa. Verifica los datos."
            })

    return render(request, "app_companies/update_company.html", {"company": company})
