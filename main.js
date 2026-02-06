// Biến đếm số lượng giỏ hàng
let cartCount = 0;

// Chọn phần tử hiển thị số lượng
const cartCountElement = document.querySelector('.cart-count');

// Hàm thêm vào giỏ hàng
function addToCart() {
    // Tăng số lượng
    cartCount++;
    
    // Cập nhật giao diện
    cartCountElement.innerText = cartCount;
    cartCountElement.style.display = 'inline-block';

    // Hiệu ứng thông báo nhỏ
    alert("Đã thêm sản phẩm vào giỏ hàng thành công!");
    
    // Log ra console để kiểm tra
    console.log("Số lượng trong giỏ: " + cartCount);
}

// Hiệu ứng đơn giản cho thanh tìm kiếm (Optional)
const searchInput = document.querySelector('.search-bar input');
searchInput.addEventListener('focus', function() {
    this.parentElement.style.boxShadow = '0 0 10px rgba(255, 55, 155, 0.5)';
});

searchInput.addEventListener('blur', function() {
    this.parentElement.style.boxShadow = 'none';
});