'''
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# 깔끔한 풀이가 될수 있도록 다시 풀어보기
'''
#첫 풀이
def solution(board):
    board = board
    for idx1 in range(len(board)):
        for idx2 in range(len(board[idx1])):
            if board[idx1][idx2] == 1:
                if idx1-1 >= 0 and idx2 >= 0:
                    if board[idx1-1][idx2-1] != 1:
                        board[idx1-1][idx2-1] = 3
                if idx1-1 >= 0:
                    if board[idx1-1][idx2] != 1:
                        board[idx1-1][idx2] = 3
                if idx1-1 >= 0 and idx2+1 < len(board[idx1]):
                    if board[idx1-1][idx2+1] != 1:
                        board[idx1-1][idx2+1] = 3
                if idx2-1 >= 0:
                    if board[idx1][idx2-1] != 1:
                        board[idx1][idx2-1] = 3
                #board[idx1][idx2] = 1
                if idx2+1 < len(board[idx1]):
                    if board[idx1][idx2+1] != 1:
                        board[idx1][idx2+1] = 3
                if idx1+1 < len(board) and idx2-1 >= 0:
                    if board[idx1+1][idx2-1] != 1:
                        board[idx1+1][idx2-1] = 3
                if idx1+1 < len(board):
                    if board[idx1+1][idx2] != 1:
                        board[idx1+1][idx2] = 3
                if idx1+1 < len(board) and idx2+1 < len(board[idx1]):
                    if board[idx1+1][idx2+1] != 1:
                        board[idx1+1][idx2+1] = 3
    #print(board)
    answer = 0
    for idx1 in range(len(board)):
        for idx2 in range(len(board[idx1])):
            if board[idx1][idx2] == 0:
                answer += 1
    return answer

def main():
    board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
    print(solution(board))
    return None
if __name__ == "__main__":
    main()