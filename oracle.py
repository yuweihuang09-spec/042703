#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
隨機占卜工具 - 書中翻頁模擬器
"""

import random

# 預設的占卜句子列表
oracle_sentences = [
    "是的",
    "現在還不是時候",
    "你需要更多資訊",
    "相信直覺",
    "結果會出乎意料",
    "保持耐心",
    "這是個好機會",
    "重新評估你的選擇",
    "跟隨你的心",
    "改變即將到來"
]

def get_random_oracle():
    """
    隨機選擇一個占卜句子
    """
    return random.choice(oracle_sentences)

def main():
    print("歡迎使用隨機占卜工具！")
    print("請在心裡默念一個問題（可以用「是／否」或方向來回答的問題），然後按 Enter 來獲取答案。")
    input("按 Enter 繼續...")
    
    answer = get_random_oracle()
    print(f"\n你的答案是：{answer}")
    print("\n記住，這只是個有趣的工具，用來引導你的思考和直覺。")

if __name__ == "__main__":
    main()