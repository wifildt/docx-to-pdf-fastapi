# 📝 Service chuyển đổi DOCX sang PDF (FastAPI)

Service **FastAPI** giúp chuyển đổi tài liệu **DOCX sang PDF**, tích hợp với **AWS S3**, **LibreOffice**, và **unoconv**.  
✅ **Tải tệp DOCX từ S3**  
✅ **Chuyển đổi sang PDF bằng `unoconv`**  
✅ **Tải lên lại PDF vào S3**  

---

## 🚀 **Tính năng**
- **FastAPI** → API hiệu suất cao
- **Tích hợp AWS S3** → Tải lên & tải xuống
- **LibreOffice & Unoconv** → Chuyển đổi DOCX sang PDF
- **Triển khai bằng Docker** → Dễ dàng triển khai trên máy chủ
- **Swagger UI & ReDoc** → Tự động tạo tài liệu API

---

## 📌 **1️⃣ Cài đặt ban đầu**
### ✅ **Sao chép kho mã nguồn**
```bash
git clone https://github.com/your-username/docx-to-pdf-fastapi.git
cd docx-to-pdf-fastapi
```

### ✅ **Thiết lập biến môi trường (`.env`)**
Tạo tệp `.env`:
```bash
touch .env
```
Thêm nội dung sau:
```ini
# Cấu hình AWS
AWS_REGION=ap-southeast-1
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
S3_BUCKET=your-s3-bucket-name

# Cấu hình LibreOffice
LIBREOFFICE_PATH=/usr/lib/libreoffice/program
```

---

## 📌 **2️⃣ Chạy Service trên máy cục bộ**
### ✅ **Cài đặt môi trường Python**
```bash
pip install -r requirements.txt
```

### ✅ **Chạy FastAPI**
```bash
uvicorn app.main:app --reload
```

Mở **Swagger UI** để kiểm tra API:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)  
Mở **ReDoc** để xem tài liệu API:  
👉 [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---

## 📌 **3️⃣ Chạy bằng Docker**
### ✅ **Xây dựng Docker Image**
```bash
docker build -t docx-to-pdf-fastapi .
```

### ✅ **Chạy Docker Container**
```bash
docker run --env-file .env -p 8000:8000 docx-to-pdf-fastapi
```