import json
import time
from typing import Optional, Union
import requests
from solana.transaction import Signature
from config import RPC, payer_keypair, client
from coin_data import get_coin_data

def find_data(data: Union[dict, list], field: str) -> Optional[str]:
    if isinstance(data, dict):
        if field in data:
            return data[field]
        else:
            for value in data.values():
                result = find_data(value, field)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = find_data(item, field)
            if result is not None:
                return result
    return None

def get_token_balance(mint_str: str):
    try:
        pubkey_str = str(payer_keypair.pubkey())
        headers = {"accept": "application/json", "content-type": "application/json"}

        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "getTokenAccountsByOwner",
            "params": [
                pubkey_str,
                {"mint": mint_str},
                {"encoding": "jsonParsed"},
            ],
        }
        
        response = requests.post(RPC, json=payload, headers=headers)
        ui_amount = find_data(response.json(), "uiAmount")
        return float(ui_amount)
    except Exception as e:
        return None

def confirm_txn(txn_sig: Signature, max_retries: int = 20, retry_interval: int = 3) -> bool:
    retries = 1
    
    while retries < max_retries:
        try:
            txn_res = client.get_transaction(txn_sig, encoding="json", commitment="confirmed", max_supported_transaction_version=0)
            txn_json = json.loads(txn_res.value.transaction.meta.to_json())
            
            if txn_json['err'] is None:
                print("Transaction confirmed... try count:", retries)
                return True
            
            print("Error: Transaction not confirmed. Retrying...")
            if txn_json['err']:
                print("Transaction failed.")
                return False
        except Exception as e:
            print("Awaiting confirmation... try count:", retries)
            retries += 1
            time.sleep(retry_interval)
    
    print("Max retries reached. Transaction confirmation failed.")
    return None

def get_token_price(mint_str: str) -> float:
    try:
        coin_data = get_coin_data(mint_str)
        
        if not coin_data:
            print("Failed to retrieve coin data...")
            return None
        
        virtual_sol_reserves = coin_data['virtual_sol_reserves'] / 10**9
        virtual_token_reserves = coin_data['virtual_token_reserves'] / 10**6

        token_price = virtual_sol_reserves / virtual_token_reserves
        print(f"Token Price: {token_price:.20f} SOL")
        
        return token_price

    except Exception as e:
        print(f"Error calculating token price: {e}")
        return None