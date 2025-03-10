from django.shortcuts import render
from .models import Company
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer
from rest_framework import status
import logging
from django.db.models import Q
from django.contrib.auth.decorators import login_required


logger = logging.getLogger('app_companies')

# Create your views here.

@api_view(['GET'])
def getAllCompanies(request):
    logger.debug('Getting all companies')
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def createCompany(request):
#     serializer = CompanySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createCompany(request):
    logger.debug('Creating a company')
    data = request.data.copy()
    user_id = data.pop('user_id', None)
    
    if user_id is None:
        return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    data['user_id'] = user_id
    serializer = CompanySerializer(data=data)

    if Company.objects.filter(Q(name=data['name']) | Q(email=data['email'])).exists():
        return Response({"error": "A company with this name or email already exists."}, status=status.HTTP_400_BAD_REQUEST)
    

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT','GET','DELETE', 'PATCH'])
def companyDetail(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        logger.error(f'Company with id {id} not found')
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        logger.debug(f'Retrieving details of company with ID {id}')
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        logger.debug(f'Updating company with ID {id}')
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Company with id {id} updated')
            return Response(serializer.data)
        logger.warning(f'Error updating company with ID {id}: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        logger.debug(f'Patching company with id {id}')
        serializer = CompanySerializer(instance=company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Company with id {id} was patched')
            return Response(serializer.data)
        logger.warning(f'Error patching company with id {id}: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        logger.warning(f'Deleting company with id {id}')
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def create_company_form(request, user_id):
    if request.method == 'POST':
        company_data = {
            'user_id': user_id,
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'address': request.POST.get('address'),
        }
        response = requests.post('http://localhost:8000/companies/create/', json=company_data)
        
        if response.status_code == 201:
            company_id = response.json().get('id')
            
            if company_id:
                return redirect('companies:company_dashboard', id=company_id)
            else:
                return redirect('home')
        else:
            try:
                error_message = response.json().get('error', 'Error creating company')  # Extraer el mensaje de error de la respuesta JSON
            except:
                error_message = 'Error creating company'

            return render(request, 'create_company.html', {'error': error_message, 'user_id': user_id})
    else:
        return render(request, 'create_company.html', {'user_id': user_id})

    



# VISTAS QUE LLAMAN A LA API Y DEVUELVEN HTMLS
import requests
from django.shortcuts import redirect, get_object_or_404
from app_companies.models import Company
from datetime import datetime

@login_required(login_url='login')
def company_dashboard(request, id):
    company = get_object_or_404(Company, id=id)
    
    # llamamos a la API para obtener los envíos de la empresa
    shipments_url = f"http://127.0.0.1:8000/shipments/{id}/co-shipments/"
    response = requests.get(shipments_url)

    shipments = []
    if response.status_code == 200:
        shipments = response.json()  # convertimos la respuesta JSON en una lista de diccionarios

        # convertimos y formatear las fechas
        for shipment in shipments:
            shipment["created_at"] = datetime.fromisoformat(shipment["created_at"].replace("Z", "")).strftime("%Y-%m-%d %H:%M")
            shipment["finished_at"] = datetime.fromisoformat(shipment["finished_at"].replace("Z", "")).strftime("%Y-%m-%d %H:%M")
    return render(request, 'app_companies/cp-dashboard.html', {
        'company': company,
        'shipments': shipments
    })


@login_required(login_url='login')
def update_company(request, id):
    api_url = f"http://127.0.0.1:8000/companies/{id}/detail/"
    response = requests.get(api_url)

    if response.status_code == 200:
        company = response.json()
    else:
        return render(request, "app_companies/cp-update.html", {"error": "Error al obtener datos."})

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
            return redirect(f"/companies/{id}/cp-dashboard/")  # Redirige de vuelta al dashboard
        else:
            return render(request, "app_companies/cp-update.html", {
                "company": company,
                "error": "Error al actualizar la empresa. Verifica los datos."
            })

    return render(request, "app_companies/cp-update.html", {"company": company})