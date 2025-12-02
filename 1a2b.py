import random
import sys


# ANSI 顏色代碼
class Colors:
    GREEN = '\033[92m'      # 綠色 - 用於 A（數字和位置都對）
    YELLOW = '\033[93m'     # 黃色 - 用於 B（數字對但位置錯）
    RED = '\033[91m'        # 紅色 - 用於錯誤訊息
    CYAN = '\033[96m'       # 青色 - 用於提示
    BOLD = '\033[1m'        # 粗體
    RESET = '\033[0m'       # 重置顏色


def generate_secret_number():
    """產生一個 4 位不重複的數字"""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))


def calculate_result(secret, guess):
    """計算 A 和 B 的數量"""
    a_count = 0
    b_count = 0
    
    for i in range(4):
        if guess[i] == secret[i]:
            a_count += 1
        elif guess[i] in secret:
            b_count += 1
    
    return a_count, b_count


def validate_input(guess):
    """驗證輸入是否合法"""
    if len(guess) != 4:
        return False, "請輸入 4 位數字！"
    
    if not guess.isdigit():
        return False, "請只輸入數字！"
    
    if len(set(guess)) != 4:
        return False, "數字不可重複！"
    
    return True, ""


def play_game():
    """進行一局遊戲"""
    secret = generate_secret_number()
    max_attempts = 10
    
    print("=" * 50)
    print(f"{Colors.CYAN}{Colors.BOLD}歡迎來到 1A2B 猜數字遊戲！{Colors.RESET}")
    print("=" * 50)
    print(f"{Colors.BOLD}遊戲規則：{Colors.RESET}")
    print("- 電腦已隨機產生 4 個不重複的數字")
    print(f"- {Colors.GREEN}{Colors.BOLD}A{Colors.RESET} 代表數字和位置都正確")
    print(f"- {Colors.YELLOW}{Colors.BOLD}B{Colors.RESET} 代表數字正確但位置錯誤")
    print(f"- 您最多有 {Colors.BOLD}{max_attempts}{Colors.RESET} 次機會")
    print("=" * 50)
    print()
    
    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = input(f"第 {attempt:2d} 次猜測: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\n遊戲中斷！")
                return False
            
            valid, error_msg = validate_input(guess)
            if not valid:
                print(f"\033[A\r第 {attempt:2d} 次猜測: {guess}  →  {Colors.RED}{error_msg}{Colors.RESET}\033[K")
                continue
            break
        
        a_count, b_count = calculate_result(secret, guess)
        
        # 將結果顯示在同一行的右側（向上移動一行，清除並重新打印）
        # A 用綠色（完全正確），B 用黃色（部分正確）
        result = f"{Colors.GREEN}{Colors.BOLD}{a_count}A{Colors.RESET}{Colors.YELLOW}{Colors.BOLD}{b_count}B{Colors.RESET}"
        print(f"\033[A\r第 {attempt:2d} 次猜測: {guess}  →  {result}\033[K")
        
        if a_count == 4:
            print()
            print("=" * 50)
            print(f"{Colors.GREEN}{Colors.BOLD}🎉 恭喜你！您猜對了！答案是 {secret}{Colors.RESET}")
            print(f"{Colors.CYAN}您總共猜了 {attempt} 次{Colors.RESET}")
            print("=" * 50)
            return True
    
    print()
    print("=" * 50)
    print(f"{Colors.RED}😢 很遺憾，您已用完 {max_attempts} 次機會！{Colors.RESET}")
    print(f"{Colors.YELLOW}正確答案是：{Colors.BOLD}{secret}{Colors.RESET}")
    print("=" * 50)
    return False


def main():
    """主程式"""
    print()
    print(f"{Colors.CYAN}{Colors.BOLD}╔═══════════════════════════════════════════╗{Colors.RESET}")
    # 標題：中文字元佔2個顯示寬度，需要調整空格數量
    # "1A2B 猜數字遊戲 v1.0" 顯示寬度 = 5 + 10 + 5 = 20
    # 邊框內寬度43，左邊8空格，20字元標題，右邊需要15空格
    print(f"{Colors.CYAN}{Colors.BOLD}║        1A2B 猜數字遊戲 v1.0               ║{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚═══════════════════════════════════════════╝{Colors.RESET}")
    print()
    
    while True:
        play_game()
        print()
        
        while True:
            try:
                play_again = input(f"{Colors.CYAN}是否要再玩一次？(Y/N): {Colors.RESET}").strip().upper()
            except (KeyboardInterrupt, EOFError):
                print(f"\n\n{Colors.YELLOW}感謝遊玩！再見！{Colors.RESET}")
                sys.exit(0)
            
            if play_again in ['Y', 'YES', 'N', 'NO']:
                break
            print(f"{Colors.RED}請輸入 Y 或 N！{Colors.RESET}")
        
        if play_again in ['N', 'NO']:
            print()
            print(f"{Colors.YELLOW}感謝遊玩！再見！{Colors.RESET}")
            break
        
        print()


if __name__ == "__main__":
    main()

