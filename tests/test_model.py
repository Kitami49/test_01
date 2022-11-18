import pytest
from django.test import TestCase



from sample_app.models import Calc
from sample_app.models import Post
from django.core.exceptions import ValidationError

print("sample_app.modelsテスト開始!")

def test_正常系_Postの__str__の検証():
    models = Post(name="neko", micropost=10)
    assert str(models)=="neko"

def test_正常系_Postのバリデーション():
    models = Post(name="neko", micropost=10)
    try:
        models.full_clean()
        print("正常系：名前=" + models.name + "、年齢=" + str(models.micropost))
    except:
        pytest.fail()
        
def test_異常系_年齢が数字以外_Postのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Post(name="neko", micropost="num")
        print("異常系：名前=" + models.name + "、年齢="+ models.micropost)
        models.full_clean()
    assert str(e.value) == "{'micropost': ['“num” は整数値にしなければなりません。']}"
    
def test_異常系_数字が大きすぎる_Postのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Post(name="neko", micropost=9999999999999999999999)
        print("異常系：名前=" + models.name + "、年齢="+ str(models.micropost))
        models.full_clean()
    assert str(e.value) == "{'micropost': ['この値は 2147483647 以下でなければなりません。']}"

def test_異常系_名前の文字数超過_Postのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Post(name="nekooooooooooooooooo", micropost=10)
        print("異常系：名前=" + models.name + "、年齢="+ str(models.micropost))
        models.full_clean()
    assert str(e.value) == "{'name': ['この値は 15 文字以下でなければなりません( 20 文字になっています)。']}"
    

def test_正常系_num1とnum2が正常の場合_Calcのバリデーション():
    models = Calc(num1=10, num2=2)
    try:
        models.full_clean()
        print("正常系：num1=" + str(models.num1) + "、num2=" + str(models.num2))
    except:
        pytest.fail()

def test_異常系_num1が数字以外の場合_Calcのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Calc(num1="num", num2=5)
        print("異常系：num1=" + str(models.num1) + "、num2=" + str(models.num2))
        models.full_clean()
    assert str(e.value) == "{'num1': ['“num” は整数値にしなければなりません。']}"
    
def test_異常系_num2が数字以外の場合_Calcのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Calc(num1=10, num2="num")
        print("異常系：num1=" + str(models.num1) + "、num2=" + str(models.num2))
        models.full_clean()
    assert str(e.value) == "{'num2': ['“num” は整数値にしなければなりません。']}"
            
def test_異常系_num1の数字が大きすぎる_Calcのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Calc(num1=9999999999999999999999, num2=5)
        print("異常系：num1=" + str(models.num1) + "、num2=" + str(models.num2))
        models.full_clean()
    assert str(e.value) == "{'num1': ['この値は 2147483647 以下でなければなりません。']}"

def test_異常系_num2の数字が大きすぎる_Calcのバリデーション():
    with pytest.raises(ValidationError) as e:
        models = Calc(num1=10, num2=9999999999999999999999)
        print("異常系：num1=" + str(models.num1) + "、num2=" + str(models.num2))
        models.full_clean()
    assert str(e.value) == "{'num2': ['この値は 2147483647 以下でなければなりません。']}"

# import pytest
# from django.test import TestCase



# from sample_app.models import Calc


# def test_num1が正常の場合_エラーとならない():
#     models = Calc(num1=10, num2=2)
#     try:
#         models.full_clean()
#     except:
#         pytest.fail()






# def test_num2が正常の場合_エラーとならない():
#     models = Calc(num1=15, num2=5)
#     try:
#         models.full_clean()
#     except:
#         pytest.fail()


