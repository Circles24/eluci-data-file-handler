from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse

import pandas as pd
import numpy as np
import uuid
import csv

# Create your views here.

def file_upload_handler(request):

    if request.method == 'POST':

        try:

            dataFile = request.FILES['dataFile']

            main_df = pd.read_excel(dataFile) 

            pc_df = main_df[main_df["Accepted Compound ID"].str.lower().str.endswith(" pc",na = False)]
            lpc_df = main_df[main_df["Accepted Compound ID"].str.lower().str.endswith("lpc",na = False)]
            plasmalogen_df = main_df[main_df["Accepted Compound ID"].str.lower().str.endswith("plasmalogen",na = False)]

            retention_rf_df = main_df
            retention_rf_df.insert(2,"Retention Time Roundoff (in mins)",np.round(main_df["Retention time (min)"]))

            mean_agg_rf_df = retention_rf_df.groupby("Retention Time Roundoff (in mins)").agg('mean').drop(columns="m/z").drop(columns="Retention time (min)")

            df_id = uuid.uuid4()

            main_df.to_csv("{}/{}_main_df.csv".format(settings.MEDIA_ROOT,df_id))
            pc_df.to_csv("{}/{}_pc_df.csv".format(settings.MEDIA_ROOT,df_id))
            lpc_df.to_csv("{}/{}_lpc_df.csv".format(settings.MEDIA_ROOT,df_id))
            plasmalogen_df.to_csv("{}/{}_plasmalogen_df.csv".format(settings.MEDIA_ROOT,df_id))
            retention_rf_df.to_csv("{}/{}_retention_rf_df.csv".format(settings.MEDIA_ROOT,df_id))
            mean_agg_rf_df.to_csv("{}/{}_mean_agg_rf_df.csv".format(settings.MEDIA_ROOT,df_id))

            # print(main_df,pc_df,lpc_df,plasmalogen_df,retention_rf_df,mean_agg_rf_df)
            # print(retention_rf_df["Retention Time Roundoff (in mins)"])

            data={"df_id":df_id}

        except Exception as ex:

            print(ex)
            data = {"msg":"dummy ex message"}

            return JsonResponse(data,safe=False)
    
        return JsonResponse(data,safe=False)

    return JsonResponse({"msg":"Only POST request are allowed"},status=400)

def get_main_df(request):

    df_id = request.GET['df_id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(df_id)

    with open("{}/{}_main_df.csv".format(settings.MEDIA_ROOT,df_id)) as f:
        reader = csv.reader(f)
        writer = csv.writer(response)
        for row in reader:
            writer.writerow(row)

    return response



def get_pc_df(request):

    df_id = request.GET['df_id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(df_id)

    with open("{}/{}_pc_df.csv".format(settings.MEDIA_ROOT,df_id)) as f:
        reader = csv.reader(f)
        writer = csv.writer(response)
        writer.writerows(reader)

    return response


def get_lpc_df(request):

    df_id = request.GET['df_id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(df_id)

    with open("{}/{}_lpc_df.csv".format(settings.MEDIA_ROOT,df_id)) as f:
        reader = csv.reader(f)
        writer = csv.writer(response)
        writer.writerows(reader)

    return response


def get_plasmalogen_df(request):

    df_id = request.GET['df_id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(df_id)

    with open("{}/{}_plasmalogen_df.csv".format(settings.MEDIA_ROOT,df_id)) as f:
        reader = csv.reader(f)
        writer = csv.writer(response)
        writer.writerows(reader)

    return response

def get_retention_rf_df(request):

    df_id = request.GET['df_id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(df_id)

    with open("{}/{}_retention_rf_df.csv".format(settings.MEDIA_ROOT,df_id)) as f:
        reader = csv.reader(f)
        writer = csv.writer(response)
        writer.writerows(reader)

    return response

def get_mean_agg_rf_df(request):

    df_id = request.GET['df_id']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(df_id)

    with open("{}/{}_mean_agg_rf_df.csv".format(settings.MEDIA_ROOT,df_id)) as f:
        reader = csv.reader(f)
        writer = csv.writer(response)
        writer.writerows(reader)

    return response
