'''
완전탐색 문제
1부터 N//2까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인하고,
가장 짧게 압축되는 길이를 출력
'''
inputs = input()
answer = inputs
for unit in range(1, len(inputs) // 2 + 1):
    compressed = ""
    prev = inputs[:unit]
    cnt = 1
    for i in range(unit, len(inputs), unit):
        if prev == inputs[i: i+unit]:
            cnt += 1
        else:
            compressed += str(cnt) + prev if cnt > 1 else prev
            prev = inputs[i: i+unit]
            cnt = 1
    # 남아있는 문자열에 대해서 처리
    compressed += str(cnt) + prev if cnt > 1 else prev
    # 길이가 더 짧은 압축문자열로 업데이트
    if len(answer) > len(compressed):
        answer = compressed



print(''.join(str(s) for s in answer))
