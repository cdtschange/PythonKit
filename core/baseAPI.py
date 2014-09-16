#coding=utf-8
from core.baseResult import *

def base_get_list(provider):
    objs = provider.load();
    result = baseJson()
    result['data'] =  objs
    return result

def base_get_list_bypage(provider, start, num):
    objs = provider.loadByPage(start, num);
    result = baseJson()
    result['data'] =  objs
    return result

def base_post_obj(provider, params):
    obj = provider.create(params)
    if obj is None:
        result = baseJson(201, '创建用户失败')
        return result
    result = baseJson()
    return result, obj

def base_get_obj(provider, oid):
    obj = provider.loadById(oid)
    if obj is None:
        result = baseJson(404, '用户不存在')
        return result
    result = baseJson()
    return result, obj

def base_put_obj(provider, oid, params):
    obj = provider.updateById(oid, params)
    if obj is None:
        result = baseJson(201, '更新用户失败')
        return result
    return result, obj

def base_delete_obj(provider, oid):
    obj = provider.deleteById(oid)
    if obj is None:
        result = baseJson(204, '删除用户失败')
        return result
    return result, obj