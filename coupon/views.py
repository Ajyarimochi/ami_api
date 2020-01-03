from django.shortcuts import render
from .models import Coupon #Couponクラスをインポート
from rest_framework import viewsets, filters

from .serializer import CouponSerializer
from django_filters import rest_framework as filters #filtersetを継承したフィルタセットを作るのに必要
from rest_framework import permissions # 認証機能の追加


class CustomFilter(filters.FilterSet):
    # フィルタの定義
    deadline = filters.DateFilter(field_name='deadline', lookup_expr='gte')

    class Meta:
        model = Coupon
        fields = ['deadline'] #定義したフィルタを列挙

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    filter_fields = ('status','code')
    #フィルタセットの指定
    filter_class = CustomFilter
    