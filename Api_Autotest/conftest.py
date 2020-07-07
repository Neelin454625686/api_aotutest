#把接口封装成方法来调用
import pytest
import requests
import urllib3
import allure_pytest
import pytest_assume



urllib3.disable_warnings() #这个方法用来解除https请求预警的 不然无法请求https请求

Environment="https://fcloud.qccvas.com"     #dev测试环境
# Environment="https://cloud.qccvas.com"     #线上测试环境
bus_tenant="dev004"        #企业标识
login_account="rui"
login_password="123456"

@pytest.fixture(scope="package")
def test_business_tenant():       ##量子溯源app——获取企业标识接口 2.1
    business_tenant_url="/gateway-nginx/QCCVAS-BIZ-MANAGER/company/selectByCondition?&tenantId={0}&model=OPPO%20R11".format(bus_tenant)  #2.1企业登录接口

    headers={

        "Charset":"UTF-8",
        "Connection":"Keep-Alive",
        "Accept-Language":"zh-CN, zh;q=0.8, en-US;q=0.5, en;q=0.3",
        "log-header":"I am the log request header.",
        "Authorization":"",
        "Content-Type":"application/json"
    }

    re=requests.get(url=Environment+business_tenant_url,headers=headers,verify = False)
    re=re.json()
    assert re["success"]==True
    assert re["resultCode"]=="0"
    try:
        if re["data"] :
            return re
    except KeyError:
        print("没有查询到该企业")





# @pytest.fixture(scope="package")
# def test_business_login(): #量子溯源app——企业登录接口 2.1





