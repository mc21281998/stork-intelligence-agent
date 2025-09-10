import numpy as np
import pandas as pd
from scipy.stats import benford
import schedule
import time
import sqlite3
import requests
from datetime import datetime

# --- 章节一: 投资者画像引擎 ---
def risk_profile(age: int, principal: float, experience_level: int, goal: str, horizon: int) -> dict:
    """根据用户输入计算风险画像评分和资产配置建议。"""
    weights = {'age': 0.15, 'principal': 0.1, 'experience': 0.3, 'goal': 0.3, 'horizon': 0.15}
    age_score = max(0, 100 - (age - 18) * 2)
    principal_score = min(100, principal / 1000000 * 100)
    experience_score = experience_level * 20
    horizon_score = min(100, horizon * 10)
    goal_map = {'capital_preservation': 20, 'steady_growth': 60, 'high_return': 100}
    goal_score = goal_map.get(goal, 60)
    total_score = (age_score * weights['age'] + principal_score * weights['principal'] + experience_score * weights['experience'] + goal_score * weights['goal'] + horizon_score * weights['horizon'])
    if total_score < 40: asset_allocation = "保守型: 权益类 20%, 固收类 80%"
    elif total_score < 70: asset_allocation = "稳健型: 权益类 50%, 固收类 50%"
    else: asset_allocation = "激进型: 权益类 80%, 固收类 20%"
    return {"risk_score": round(total_score, 2), "asset_allocation": asset_allocation}

# --- 其他核心函数... (此为摘要) ---
print("Stock Agent Script Initialized.")
