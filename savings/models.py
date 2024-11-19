from django.db import models
from django.conf import settings

# Create your models here.
class SavingProducts(models.Model):
    dcls_month = models.IntegerField()      # 공시제출월
    fin_co_no = models.IntegerField()       # 금융회사코드
    kor_co_nm = models.CharField(max_length=50) # 은행이름
    fin_prdt_cd = models.TextField()         # 금융상품코드
    fin_prdt_nm = models.TextField()            # 상품이름
    join_way = models.TextField()               # 가입방법
    mtrt_int = models.TextField()           # 만기후 이자율
    spcl_cnd = models.TextField()           # 우대사항
    join_deny = models.IntegerField()       # {1:제한없음, 2:서민전용, 3:일부제한}
    join_member = models.TextField()        # 가입대상
    etc_note = models.TextField()           # 비고(가입한도, 방식 등)
    max_limit = models.IntegerField(null=True)     # 최대한도
    dcls_strt_day = models.IntegerField()   # 공시 시작일
    dcls_end_day = models.IntegerField(null=True)    # 공시 종료일
    fin_co_subm_day = models.IntegerField() # 금융회사 제출일

class UserSavings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bank = models.CharField(max_length=50)
    product = models.TextField()
    mtrt = models.FloatField()          # 만기후 이자율
    join_deny = models.IntegerField()   # {1:제한없음, 2:서민전용, 3:일부제한}
    join_member = models.TextField()    # 1이 아닐때만 null=True
    max_limit = models.FloatField()     # 최대한도

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    savings_product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    score = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    pass