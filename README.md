# Bài tập 10 - Tích hợp JSON Web Token (JWT) với Spring Boot 3

Dự án này bao gồm hai ví dụ về cách triển khai xác thực (Authentication) và ủy quyền (Authorization) bằng JSON Web Token (JWT) trong **Spring Boot 3** và **Spring Security 6**.

##  Cấu trúc dự án

Dự án được chia thành 2 thư mục tương ứng với 2 thư viện JWT khác nhau:

1. **`jwt-example`**: 
   - Sử dụng thư viện `io.jsonwebtoken` (jjwt).
   - Đây là bài tập ví dụ tiêu chuẩn được thực hành theo nội dung bài giảng.
2. **`nimbus-example`**: 
   - Sử dụng thư viện `com.nimbusds:nimbus-jose-jwt`.
   - Bài tập nâng cao thay thế thư viện `jjwt` bằng thư viện Nimbus.

## 🛠️ Yêu cầu hệ thống (Prerequisites)

- **Java**: 17 hoặc 21
- **Database**: MySQL Server
- **Công cụ build**: Maven (có thể dùng Maven Wrapper `mvnw` đi kèm sẵn trong dự án)

##  Hướng dẫn cài đặt và khởi chạy

### Bước 1: Cấu hình cơ sở dữ liệu (Database)
Cả hai project đều kết nối tới MySQL database tên là `jwt_springboot3`.
Mở file cấu hình tại đường dẫn `src/main/resources/application.properties` của thư mục bạn muốn chạy và điều chỉnh các thông số sau cho phù hợp với máy của bạn:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/jwt_springboot3?serverTimezone=UTC&allowPublicKeyRetrieval=true&useSSL=false
spring.datasource.username=root
spring.datasource.password=1234567@a$  # Đổi thành mật khẩu MySQL của bạn
```

> **Lưu ý:** Thuộc tính `spring.jpa.hibernate.ddl-auto=update` đã được thiết lập, nên các bảng (table) sẽ được tự động tạo trong CSDL khi bạn chạy ứng dụng. Bạn chỉ cần tạo một database trống mang tên `jwt_springboot3` trong MySQL trước khi chạy là được.

### Bước 2: Chạy ứng dụng

Mở terminal/command prompt và di chuyển vào thư mục bạn muốn chạy (`jwt-example` hoặc `nimbus-example`).

Chạy lệnh sau để khởi động:

```bash
# Trên Windows
.\mvnw spring-boot:run

# Trên Linux/Mac
./mvnw spring-boot:run
```

### Bước 3: Kiểm thử chức năng
Ứng dụng sẽ chạy tại port **8005** (`http://localhost:8005`).

Các chức năng bao gồm:
- Trang đăng nhập (Frontend gọi AJAX): `http://localhost:8005/login`
- Các REST API endpoints:
  - `POST /auth/signup`: Đăng ký tài khoản.
  - `POST /auth/login`: Đăng nhập, nhận về Token.
  - `GET /users/me`: Lấy thông tin user hiện tại (Yêu cầu có token Bearer).
