CREATE TABLE coins(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) UNIQUE NOT NULL,
    name_id VARCHAR(50) UNIQUE NOT NULL,
    symbol VARCHAR(10) UNIQUE NOT NULL,
    first_coin_emitted_on DATE
);
INSERT INTO coins (name, name_id, symbol, first_coin_emitted_on)
    VALUES ('TestCoin.22 (The new one)', 'testcoin-22', 'TST22', '2022-05-31');
INSERT INTO coins (name, name_id, symbol) VALUES ('TestCoin.20', 'testcoin', 'TST');
CREATE DATABASE web_test;