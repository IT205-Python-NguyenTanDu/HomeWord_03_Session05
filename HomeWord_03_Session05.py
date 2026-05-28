# PHÂN TÍCH INPUT / OUTPUT
# Input:
#   num_rooms (int) : số lượng phòng học cần kiểm tra  - nhập 1 lần
#   num_rows  (int) : số hàng ghế của mỗi phòng        - nhập lại mỗi phòng
#   num_cols  (int) : số ghế trên mỗi hàng             - nhập lại mỗi phòng
# Output:
#   - Sơ đồ chỗ ngồi bằng ký tự *, ví dụ 3 hàng x 5 ghế:
#       *****
#       *****
#       *****
#   - Hoặc thông báo lỗi tương ứng theo từng trường hợp


# ĐỀ XUẤT GIẢI PHÁP
# Bước 1: Nhập num_rooms, nếu <= 0 thì in lỗi và kết thúc
# Bước 2: Dùng vòng for lặp qua từng phòng học
# Bước 3: Nhập num_rows, num_cols rồi kiểm tra:
#         - <= 0  → dùng continue để bỏ qua, sang phòng kế
#         - > 10  → dùng break để dừng toàn bộ chương trình
# Bước 4: Dữ liệu hợp lệ → dùng vòng for in num_rows dòng, mỗi dòng "*" x num_cols


# PSEUDOCODE
# INPUT num_rooms
# IF num_rooms <= 0  →  PRINT lỗi, END
#
# FOR i = 1 TO num_rooms
#     INPUT num_rows, num_cols
#     IF num_rows <= 0 OR num_cols <= 0  →  PRINT lỗi, CONTINUE
#     IF num_rows > 10 OR num_cols > 10  →  PRINT lỗi, BREAK
#     FOR row = 1 TO num_rows
#         PRINT "*" x num_cols


# Bước 1: Nhập và kiểm tra số lượng phòng học
num_rooms = int(input("Nhập số lượng phòng học: "))

if num_rooms <= 0:
    print("Số lượng phòng học không hợp lệ")

else:
    # Bước 2: Lặp qua từng phòng học
    for i in range(1, num_rooms + 1):
        print(f"\n--- Phòng học thứ {i} ---")

        num_rows = int(input("  Nhập số hàng ghế    : "))
        num_cols = int(input("  Nhập số ghế mỗi hàng: "))

        # Bước 3: Kiểm tra dữ liệu phòng học
        if num_rows <= 0 or num_cols <= 0:       # hàng hoặc ghế <= 0 → bỏ qua phòng này
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if num_rows > 10 or num_cols > 10:       # hàng hoặc ghế > 10 → dừng chương trình
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        # Bước 4: In sơ đồ chỗ ngồi
        print(f"  Sơ đồ phòng ({num_rows} hàng × {num_cols} ghế):")
        for row in range(num_rows):
            print("*" * num_cols)               # mỗi hàng ghế = "*" lặp num_cols lần