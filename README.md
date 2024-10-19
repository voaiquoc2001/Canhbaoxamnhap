Để sử dụng ứng dụng, người dùng cần thực hiện những bước sau:
⦁	Cài đặt môi trường chạy chương trình:
⦁	Text Editor: Visual Code
⦁	Tạo thư mục nơi lưu trữ dự án
⦁	Cài đặt extension Python trên visualcode
⦁	Cài đặt các thư viện cần thiết trên Vscode, gõ lệnh trực tiếp trên Terminal của Vscode:
    ⦁	python -m pip install --upgrade pip
    ⦁	pip install Pillow
    ⦁	pip install opencv-python
    ⦁	Nếu đã có phiên bản cũ trong máy, ta có thể nâng cấp open-cv lên bản mới nhất: pip install --upgrade opencv-python
    ⦁	pip install numpy
    ⦁	Sau đó kiểm tra đã cài các package trên chưa thì gõ lệnh: pip list
⦁	Cần có 1 tài khoản mạng xã hội, cụ thể ở đây là Telegram
⦁	Tìm kiếm từ khoá “BotFather” chọn tài khoản có tích xanh
    ⦁	Nhập câu lệnh: /start
    ⦁	Nhập: /newbot để tạo bot
    ⦁	Tiếp theo cần đặt tên cho bot, ví dụ ở dây là my_bot
    ⦁	Sau đó, BotFather của telegram sẽ gửi những thông tin cần thiết cho chúng ta, cụ thể là id vừa tạo của con bot. Hãy ghi nhớ dòng “Use this token to access the HTTP API:”, tránh tiết lộ dòng token cho người ngoài.
    ⦁	Tiến hành lấy id người dùng như sau: Nhập đoạn liên kết này vào trình duyệt ⦁	https://api.telegram.org/bot[TOKEN]/getUpdates thay [TOKEN] bằng đoạn token mà BotFather vừa gửi cho chúng ta.
    ⦁	Sau đó nhấn Enter để đi đến link đó và lấy được id người dùng.
    ⦁	Vào chương trình thay đoạn mã trong settings.py như sau:
        ⦁	Thay TOKEN_BOT bằng token của bạn.
        ⦁	Thay CHAT_ID bằng id của người dùng.
⦁	Chạy chương trình như sau: python main.py
⦁	Thiết lập các điểm cần xác định khu vực phát hiện xâm nhập bằng cách nhấp chuột trái (Cần ít nhất 4 điểm)
    ⦁	Sau khi có đủ các điểm để xác định khu vực, nhấn phím “D” để bắt đầu xác định đối tượng
    ⦁	Phím “ R”: để xoá điểm vừa chọn
    ⦁	Phím “A”: xoá toàn bộ điểm vừa chọn
    ⦁	Phím “Q”: để thoát chương trình

