import random
import sys

def generate_answer():
    """產生一個不重複的4位數字作為答案"""
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def check_guess(answer, guess):
    """檢查猜測結果，返回 A 和 B 的數量"""
    a_count = 0  # 數字和位置都正確
    b_count = 0  # 數字正確但位置錯誤
    
    for i in range(4):
        if guess[i] == answer[i]:
            a_count += 1
        elif guess[i] in answer:
            b_count += 1
    
    return a_count, b_count

def is_valid_guess(guess):
    """驗證輸入是否有效（4位數字且不重複）"""
    if len(guess) != 4:
        return False
    if not guess.isdigit():
        return False
    if len(set(guess)) != 4:  # 檢查是否有重複數字
        return False
    return True

def play_game():
    """進行一局遊戲"""
    answer = generate_answer()
    max_attempts = 10
    attempts = 0
    
    print("=" * 50)
    print("歡迎來到 1A2B 猜數字遊戲！")
    print("規則：猜一個4位數字（數字不重複）")
    print("A = 數字和位置都正確")
    print("B = 數字正確但位置錯誤")
    print(f"你有 {max_attempts} 次機會")
    print("=" * 50)
    print()
    
    while attempts < max_attempts:
        attempts += 1
        
        # 取得玩家輸入
        while True:
            guess = input(f"第 {attempts} 次猜測：").strip()
            
            if not is_valid_guess(guess):
                print(" " * 13 + "→ 請輸入4個不重複的數字！")
                continue
            break
        
        # 檢查結果
        a_count, b_count = check_guess(answer, guess)
        
        # ANSI 顏色代碼：綠色代表 A，黃色代表 B
        green = "\033[92m"
        yellow = "\033[93m"
        reset = "\033[0m"
        
        # 向上移動一行，回到輸入的那一行，在同一行顯示結果
        result = f"  →  {green}{a_count}A{reset}{yellow}{b_count}B{reset}"
        sys.stdout.write(f"\033[A")  # 向上移動一行
        sys.stdout.write(f"\r第 {attempts} 次猜測：{guess}{result}\n")
        sys.stdout.flush()
        
        # 檢查是否獲勝
        if a_count == 4:
            print()
            print("🎉" * 20)
            print(f"恭喜你！答案就是 {answer}")
            print(f"你總共猜了 {attempts} 次")
            print("🎉" * 20)
            return True
    
    # 用完所有次數仍未猜中
    print()
    print("😢" * 20)
    print(f"很遺憾，你已經用完所有 {max_attempts} 次機會")
    print(f"正確答案是：{answer}")
    print("😢" * 20)
    return False

def main():
    """主程式"""
    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 15 + "1A2B 猜數字遊戲" + " " * 16 + "║")
    print("╚" + "═" * 48 + "╝")
    print()
    
    while True:
        play_game()
        print()
        
        # 詢問是否重玩
        while True:
            replay = input("是否要再玩一局？(Y/N): ").strip().upper()
            if replay in ['Y', 'N', 'YES', 'NO']:
                break
            print("請輸入 Y 或 N")
        
        if replay in ['N', 'NO']:
            print()
            print("謝謝遊玩！再見！👋")
            print()
            break
        
        print("\n" + "─" * 50 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n遊戲已中斷。再見！👋\n")
        sys.exit(0)

