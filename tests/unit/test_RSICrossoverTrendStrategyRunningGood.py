import pytest
from RSICrossoverTrendStrategy import RSICrossoverTrendStrategy
from freqtrade.strategy.interface import IStrategy
from freqtrade.persistence import Trade
from pandas import DataFrame
from datetime import datetime
import talib.abstract as ta
import pandas_ta as pta

#只测试本用例命令：pytest /Users/guoyingcheng/gyc/code_git/NostalgiaForInfinity/tests/unit/test_RSICrossoverTrendStrategyRunningGood.py
# 使用 pytest fixture 创建一个模拟的 config 对象
@pytest.fixture
def mock_config():
    return {
        # 这里可以根据实际需求添加更多的配置项
        "exchange": {
            "name": "binance",
            "ccxt_config": {},
            "pair_whitelist": ["BTC/USDT"]
        },
        "stake_currency": "USDT",
        "stake_amount": 100,
        "dry_run": True
    }

# 为测试函数添加标记
@pytest.mark.strategy
# 测试策略类是否继承自 IStrategy
def test_strategy_inheritance(mock_config):
    # 使用 mock_config 创建策略实例
    strategy = RSICrossoverTrendStrategy(mock_config)
    assert isinstance(strategy, IStrategy)

# 为测试函数添加标记
@pytest.mark.strategy
# 测试策略的最小 ROI 配置
def test_minimal_roi(mock_config):
    # 使用 mock_config 创建策略实例
    strategy = RSICrossoverTrendStrategy(mock_config)
    assert strategy.minimal_roi == {"0": 1}

# 后续的测试函数也都需要使用 mock_config 创建策略实例
# ...

# 运行所有测试
if __name__ == '__main__':
    pytest.main()