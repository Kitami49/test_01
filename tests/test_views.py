import pytest
from pytest import *
from django.test import TestCase
from django.urls import reverse

from sample_app.views import *

class NekoGetTest(TestCase):
    def test_create_get(self):
        print("viewsテスト開始!")
        response = self.client.get(reverse('sample_app:create_post'))
        print("正常系：Getで" + (reverse('sample_app:create_post') + "にアクセス"))
        self.assertEqual(response.status_code, 200)
        
    def test_read_get(self):
        response = self.client.get(reverse('sample_app:read_post'))
        self.assertEqual(response.status_code, 200)
        
class NekoPostTest(TestCase):
        def test_create_post(self):
            data={
                'name': "ネコ",
                'micropost': "10",
            }
            response = self.client.post(reverse('sample_app:create_post'), data)
            print("正常系：Postで" + (reverse('sample_app:create_post') + "にアクセス"))
            self.assertEqual(response.status_code, 302)
            
        def test_create_valid(self):
            data={
                'name': "nekooooooooooooo",
                'micropost': 10,
            }
            response = self.client.post(reverse('sample_app:create_post'), data)
            print("異常系：Postで名前のバリデーション違反")
            self.assertEqual(response.status_code, 302)

class CalcGetTest(TestCase):
    
    def test_calcGet_view(self):
        response = self.client.get(reverse('sample_app:calc'))
        print("正常系：Getで" + (reverse('sample_app:calc') + "にアクセス"))
        self.assertEqual(response.status_code, 200)

class CalcPostTest(TestCase):
    def test_calcPost_view(self):
        data={
            'num1': 5,
            'num2': 10,
        }
        response = self.client.post(reverse('sample_app:calc'), data)
        print("正常系：Postで" + (reverse('sample_app:calc') + "にアクセス"))
        print("加算:"+str(response.context['sum'])+ "減算:" +str(response.context['sub'])+"乗算:" +str(response.context['mul'])+ "除算:"+str(response.context['div']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['sum'], 15.0)
        self.assertEqual(response.context['sub'], -5.0)
        self.assertEqual(response.context['mul'], 50.0)
        self.assertEqual(response.context['div'], 0.5)
        
    def test_calcPost_0div_view(self):
        data={
            'num1': 5,
            'num2': 0,
        }
        with pytest.raises(Exception) as e:
            
            print("異常系：Postで" + (reverse('sample_app:calc') + "にアクセスして0割り"))
            response = self.client.post(reverse('sample_app:calc'), data)
            print("加算:"+str(response.context['sum'])+ "減算:" +str(response.context['sub'])+"乗算:" +str(response.context['mul'])+ "除算:"+str(response.context['div']))
            assert str(e.value) == "ZeroDivisionError: division by zero"
            