# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    X, Y, Z = map(int, input().split())
    C_k = 3
    C_r = C_k + 2
    C_f = C_r + 7
    total_cost = X * C_k + Y * C_r + Z * C_f
    print(total_cost)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
