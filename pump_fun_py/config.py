from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore

PRIV_KEY = "base58_priv_str_here"
RPC = "rpc_url_here"
UNIT_BUDGET =  100_000
UNIT_PRICE =  1_000_000
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)