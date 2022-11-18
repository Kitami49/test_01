import pytest
from django.test import TestCase
#from django.core.urlresolvers import resolve, Resolver404
from django.urls import *
from django.urls import Resolver404, resolve
from django.urls import path
from sample_app.views import calc_view, create_post, read_post

#from sample_app.views import calc



from sample_app.views import PostForm



class Test_URL解決まわり(TestCase):

    
    def test_ねこ登録フォームの存在しないURLの場合_No1_エラー(self):
        with pytest.raises(Resolver404):
            resolve('/neko/create/NoExist/')


    def test_ねこ登録フォームのURLの場合_No1_正常系(self):
        found = resolve('/neko/create/')
        assert found.func.__name__ == create_post.__name__


    def test_ねこ登録フォームの存在しないURLの場合_No2_エラー(self):
        with pytest.raises(Resolver404):
            resolve('/neko/NoExist/')
            

    def test_ねこ登録フォームの存在しないURLの場合_No2_正常系(self):
        found = resolve('/neko/')
        assert found.func.__name__ == read_post.__name__


    def test_数値計算の存在しないURLの場合_エラー(self):
        with pytest.raises(Resolver404):
            resolve('/calcNoExist/')
    

    def test_数値計算のURLの場合_正常系(self):
        found = resolve('/calc/')
        assert found.func.__name__ == calc_view.__name__

