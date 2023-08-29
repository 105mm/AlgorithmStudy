import random
import string
import os

# 사용할 수 있는 특수문자
valid_chars = string.ascii_letters + string.digits + r'!@#$%^&()-_+='

# 총 용량 (bytes로 변환)
total_size_gb = 215
total_size_bytes = total_size_gb * 1024 * 1024 * 1024

# 파일 생성
files = []

while total_size_bytes > 0:
    # 랜덤한 용량 생성 (1MB 이상 50MB 이하)
    file_size = random.randint(1, 50) * 1024 * 1024  # Bytes로 변환

    # 총 용량이 충분한지 확인
    if total_size_bytes < file_size:
        break

    # 랜덤한 파일 이름 생성 (170글자 이상 190글자 이하)
    file_name = ''.join(random.choice(valid_chars) for _ in range(random.randint(170, 190))) + ".txt"

    # 총 용량 조정
    total_size_bytes -= file_size

    files.append((file_name, file_size))
"""
# 출력하고 싶다면
for file_name, file_size in files:
    output_line = f"D:\\{file_name}\t{str(file_size)}\t{'1'}"
    print(output_line)
"""
# 결과를 선택한 드라이브 루트 디렉토리에 파일로 저장
output_path = "C:\\Users\king7.DESKTOP-F3EIMPM\Desktop\dummy12\output.txt"
with open(output_path, "w") as f:
    for file_name, file_size in files:
        output_line = f"G:\\{file_name}\t{str(file_size)}\t{'1'}\n"
        f.write(output_line)

print(f"Results saved to: {output_path}")
