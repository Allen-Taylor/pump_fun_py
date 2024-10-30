from solders.pubkey import Pubkey  # type: ignore
from spl.token.instructions import get_associated_token_address
from construct import Padding, Struct, Int64ul, Flag
from config import client
from constants import PUMP_FUN_PROGRAM

def get_virtual_reserves(bonding_curve: Pubkey):
    bonding_curve_struct = Struct(
        Padding(8),
        "virtualTokenReserves" / Int64ul,
        "virtualSolReserves" / Int64ul,
        "realTokenReserves" / Int64ul,
        "realSolReserves" / Int64ul,
        "tokenTotalSupply" / Int64ul,
        "complete" / Flag
    )
    
    try:
        account_info = client.get_account_info(bonding_curve)
        data = account_info.value.data
        parsed_data = bonding_curve_struct.parse(data)
        return parsed_data
    except Exception:
        return None

def derive_bonding_curve_accounts(mint_str: str):
    try:
        mint = Pubkey.from_string(mint_str)
        bonding_curve, _ = Pubkey.find_program_address(
            ["bonding-curve".encode(), bytes(mint)],
            PUMP_FUN_PROGRAM
        )
        associated_bonding_curve = get_associated_token_address(bonding_curve, mint)
        return bonding_curve, associated_bonding_curve
    except Exception:
        return None, None

def get_coin_data(mint_str: str):
    bonding_curve, associated_bonding_curve = derive_bonding_curve_accounts(mint_str)
    if bonding_curve is None or associated_bonding_curve is None:
        return None

    virtual_reserves = get_virtual_reserves(bonding_curve)
    if virtual_reserves is None:
        return None

    try:
        virtual_token_reserves = int(virtual_reserves.virtualTokenReserves)
        virtual_sol_reserves = int(virtual_reserves.virtualSolReserves)
        token_total_supply = int(virtual_reserves.tokenTotalSupply)
        complete = bool(virtual_reserves.complete)
        
        return {
            "mint": mint_str,
            "bonding_curve": str(bonding_curve),
            "associated_bonding_curve": str(associated_bonding_curve),
            "virtual_token_reserves": virtual_token_reserves,
            "virtual_sol_reserves": virtual_sol_reserves,
            "token_total_supply": token_total_supply,
            "complete": complete
        }
    except Exception:
        return None
