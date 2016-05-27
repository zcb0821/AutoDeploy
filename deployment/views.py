# encoding: utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from utilities.djangohelper import *
from models import Cluster
import uuid
import requests
import json
from datetime import datetime
from bigdata.settings import DEPLOY_URL


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def clusters(request):
    """
    :param request:
    :return:
    """
    return render(request, 'clusters.html')


@login_required()
def rest_clusters(request):
    if request.method == 'GET':
        clusters = Cluster.objects.filter(user_id=request.user.id)
        return JsonResponse(clusters, encoder=QuerySetJSONEncoder, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        cluster = Cluster()
        cluster.id = data['id']
        cluster.name = data['name']
        cluster.systems = data['systems']['storage'] + data['systems']['compute']
        cluster.created = datetime.now()
        cluster.user = request.user
        cluster.save()

        data['config']['id'] = cluster.id
        response = requests.post(url=DEPLOY_URL, data=json.dumps(data['config']))

        if json.loads(response.text).get('result') == 'success':
            return JsonResponse(model_to_dict(cluster))
        else:
            return JsonResponse({
                'error': response['error_message']
            })
    else:
        return HttpResponse(status=404)


@login_required()
def cluster(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    if cluster.user_id == request.user.id:
        context = model_to_dict(cluster)
        context['managements'] = cluster.managements()
        return render(request, 'cluster.html', context=context)
    else:
        return HttpResponse('你不是该集群的拥有者，无权管理！')


@login_required
def rest_cluster(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    if cluster and cluster.user_id == request.user.id:
        if request.method == 'GET':
            pass
        elif request.method == 'DELETE':
            cluster.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return JsonResponse({
            'error': '你不是'
        })


@login_required
def assist(request):
    """
    辅助选型参数推荐
    :param request: Django Request Object
    :return: Django Response Object
    """
    # return JsonResponse({
    #     'storage': ['HDFS', 'HBase'],
    #     'compute': ['Spark', 'MapReduce']
    # })
    requirements = json.loads(request.body)
    response = requests.get(url=DEPLOY_URL+'/BigdataResource/rest/requirement', params=requirements)
    data = json.loads(response.text)
    if data['result'] == 'success':
        return JsonResponse(data['selection'], safe=False)
    else:
        return JsonResponse({
            'error': data['error_message']
        })


@login_required
def selectsystems(request):
    headers = {
        'content-type': 'text/plain'
    }
    response = requests.post(url=DEPLOY_URL+'/BigdataResource/rest/selectsystem', data=request.body, headers=headers)
    data = response.json()
    if data['result'] == 'success':
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({
            'error': data['error_message']
        })


@login_required
def rest_status(request, cluster_id):
    """
    get the status of cluster
    :param request: Django Request Object
    :param cluster_id: 集群 id
    :return: if error occurs, return {
                'error': 'error_message'
            } else return {
                'is_completed': boolean
                'addrs': string array like ['166.111.81.129']
            }
    """
    cluster = Cluster.objects.get(id=cluster_id)
    if cluster and cluster.user_id == request.user.id:
        return JsonResponse({
            'is_completed': True,
            'addrs': ['166.111.81.209']
        })
        # repost the request
        response = request.get(url='', data={'id':cluster.id})
        data = json.loads(response.text)
        if data['status'] == 'deployed':
            return JsonResponse({
                'is_completed': True,
                'addrs': data['ipadds']
            })
        else:
            return JsonResponse({
                'is_completed': False
            })
    else:
        return JsonResponse({
            'error': '无权限'
        })


@login_required
def generate_uuid(request):
    return JsonResponse({
        'uuid': str(uuid.uuid1())
    })