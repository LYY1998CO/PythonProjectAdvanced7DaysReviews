from fastapi import  FastAPI # 创建fastapi框架对象
import uvicorn   # 启动服务器
from fastapi import Response #创建响应报文对象

# ① 创建fastapi对象
api=FastAPI()

# ② 通过路由装饰器装饰定义的返回html网页方法
# 路由装饰器就可以给函数添加新的功能,可以找到对应请求地址中的数据
# api:创建出来的fastapi对象名
# get:请求的方式 get post put
# /render.html:请求行中的 资源路径
@api.get('/render.html')
def render():
    # 获取到了响应报文中的响应体数据
    with open('./html/render.html','r',encoding='utf-8') as f:
        data=f.read()
    # 构建响应报文对象
    response=Response(content=data,media_type='text/html')
    return response

# 如果要浏览不同的网址,返回不同的网页,实际上就是定义多个方法,用路由装饰器装饰就可以
@api.get('/gdp.html')
def gdp():
    with open('./html/gdp.html','r',encoding='utf-8') as f:
        data=f.read()
        return Response(content=data)

# ③ 启动web服务器
uvicorn.run(api,host='127.0.0.1',port=8080)