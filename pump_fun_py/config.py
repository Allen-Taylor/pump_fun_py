from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore

PUB_KEY = "" # WALLET ADDRESS
PRIV_KEY = "" # BASE58 STRING FORMAT
RPC = "https://api.mainnet-beta.solana.com" # Use Helius or Quicknode for better performance
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)
