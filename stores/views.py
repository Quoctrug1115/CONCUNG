from django.shortcuts import render
from django.core.serializers import serialize
from .models import Shop

def map_view(request):
    # Lấy dữ liệu cửa hàng để hiển thị bản đồ
    shops_data = serialize('geojson', Shop.objects.all())
    return render(request, 'map.html', {'shops_json': shops_data})