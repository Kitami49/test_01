from django.test import TestCase



from sample_app.forms import CalcForm


class Test_CalcFormまわり(TestCase):
#     def test_Calcに値がある場合_エラー(self):
#         form =CalcForm({num1})
#         assert form.__init__()



    def test_Calcに値がある場合_エラー(self):
        form =CalcForm({'num1' : '',
                        'num2' : ''})
        assert form.__init__