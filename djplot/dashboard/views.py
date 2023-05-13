from django.shortcuts import render
from .models import *
import pandas as pd

# Create your views here.

def create_df(file_path):
    try:
        df = pd.read_excel(file_path)
        print(df)
    except ValueError:
        ValueError("Invalid File Type!")

    # -> if want to update database use this, but model for first_name and etc. must be created in model.py
    # class name (models.Model) and then first_name = models.CharField(max_length=100) and etc.
    # i[1] -> 1 represent row of the file dataframe
    # fake database can be created at mockaroo.com
    """else:
        list_of_df = [list(row) for row in df.values]

        for i in list_of_df:
            first_name = i[1]
            last_name = i[2]
            email = i[3]"""
    

def home(request):
    # Upload file
    if request.POST:
        file = request.FILES['file']
        obj = GetFile.objects.create(file = file)
        create_df(obj.file)
    return render(request, 'dashboard/home.html')