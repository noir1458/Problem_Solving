def get(N):
    pattern = "1234567890"
    result = (pattern * (N // len(pattern) + 1))[:N]
    
    # 결과를 파일에 저장
    with open("result.txt", "w") as f:
        f.write(result)
    
    return result

# 3000자리 숫자 생성하고 파일로 저장
print(get(3000))
