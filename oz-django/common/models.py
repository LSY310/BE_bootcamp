from django.db import models

# Create your models here.
# admin pannel에 아래 데이터가 보여봤자 의미가 없음. 
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 해당 object 생성 시간을 기준, 업데이트 후 수정x
    updated_at = models.DateTimeField(auto_now=True) # 해당 object가 업데이트된 시간을 기준, 업데이트된 현재 시간 기준으로 수정

    # Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용
    class Meta:
        abstract = True # DB 테이블에 추가하는 것을 원하지 않는다.