VALID_COIN = {"name": "TestCoin.20 (The new one)", "name_id": "testcoin-20", "symbol": "TST2"}
VALID_COIN_WITH_DATE = {"name": "TestCoin.22 (The new one)",
                        "name_id": "testcoin-22",
                        "symbol": "TST22",
                        "first_coin_emitted_on": "2022-05-31"}
INVALID_COIN = {"name": "TestCoin 666 (The evil one)", "name_id": "Test COIN .666", "symbol": "test coin!666"}
NAME_MISSING = {"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"}
NAMEID_MISSING = {"loc": ["body", "name_id"], "msg": "field required", "type": "value_error.missing"}
NAMEID_INVALID = {
                    "loc": ["body", "name_id"],
                    "msg": 'string does not match regex "^[a-z0-9-]*$"',
                    "type": "value_error.str.regex",
                    "ctx": {"pattern": "^[a-z0-9-]*$"}
                }
SYMBOL_MISSING = {"loc": ["body", "symbol"], "msg": "field required", "type": "value_error.missing"}
SYMBOL_INVALID = {
                    "loc": ["body", "symbol"],
                    "msg": 'string does not match regex "^[A-Z0-9]*$"',
                    "type": "value_error.str.regex",
                    "ctx": {"pattern": "^[A-Z0-9]*$"}
                }