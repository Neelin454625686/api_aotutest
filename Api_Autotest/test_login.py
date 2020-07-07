import requests
import pytest
import allure_pytest
import urllib3
from Api_Autotest import conftest as cf






def test_ceshi(test_business_tenant):
    print(test_business_tenant["data"])
    pass



if __name__ == '__main__':
    pytest.main(['-v','-s','Api_Autotest/test_login.py'])


