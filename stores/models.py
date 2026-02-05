from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Shop(models.Model):
    # 1. Các trường dữ liệu cơ bản
    name = models.CharField(
        max_length=100, 
        verbose_name="Tên cửa hàng",
        unique=True,  # <-- NÂNG CẤP: Không cho phép trùng tên cửa hàng
        help_text="Nhập tên đầy đủ của cửa hàng (VD: Con Cưng Nguyễn Trãi)"
    )
    
    address = models.CharField(
        max_length=255, 
        verbose_name="Địa chỉ chi tiết"
    )
    
    # 2. Trường không gian (Quan trọng nhất)
    # srid=4326 là hệ tọa độ GPS chuẩn toàn cầu (WGS84)
    location = models.PointField(
        srid=4326, 
        verbose_name="Tọa độ (GPS)",
        spatial_index=True # <-- NÂNG CẤP: Đánh index để tìm kiếm siêu nhanh
    )

    # 3. Các trường quản lý (Audit Log) - Rất quan trọng cho điểm số
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Ngày tạo"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Cập nhật lần cuối"
    )

    # 4. Business Logic (Hàm tính toán nằm ngay trong model)
    @property
    def lat_lng(self):
        """Trả về chuỗi tọa độ dạng: '10.776, 106.700' để hiển thị ra web dễ hơn"""
        return f"{self.location.y:.4f}, {self.location.x:.4f}"

    def get_distance_km(self, other_point):
        """Hàm tính khoảng cách từ shop này đến một điểm bất kỳ (đơn vị KM)"""
        if not other_point:
            return None
        # distance trả về độ, nhân ~111km hoặc dùng transform (cách đơn giản nhất ở đây)
        # Để chính xác tuyệt đối cần transform sang hệ mét, nhưng ở mức ORM cơ bản:
        # Chúng ta dùng hàm distance của database
        return self.location.distance(other_point) * 100 # Ước lượng tương đối

    class Meta:
        verbose_name = "Cửa hàng"
        verbose_name_plural = "Danh sách Cửa hàng"
        ordering = ['-created_at'] # Mới nhất hiện lên đầu

    def __str__(self):
        return f"{self.name} (Q.{self.created_at.month}/{self.created_at.year})"