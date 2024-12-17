# pump_fun_py

Python library to trade on pump.fun. 

Updated: 12/8/2024

solana Version: 0.35.0

solders Version: 0.21.0

Clone the repo, and add your Private Key (Base58 string) and RPC to the config.py.

**If you can - please support my work and donate to: 3pPK76GL5ChVFBHND54UfBMtg36Bsh1mzbQPTbcK89PD**

### Contact

My services are for **hire**. Contact me if you need help integrating the code into your own project. 

-PF Token Launchers (Bundler or Self-Sniper)

-Bump Bot

-gRPC Detection (Mints, Buys, Migrations)

-Vanity Address Generator

-Rust implementations of PF code

I am not your personal tech support. READ THE FAQS BEFORE CONTACTING ME. 

Telegram: @AL_THE_BOT_FATHER

### FAQS

**What format should my private key be in?** 

The private key should be in the base58 string format, not bytes. 

**Why are my transactions being dropped?** 

You get what you pay for. Don't use the main-net RPC, just spend the money for Helius or Quick Node.

**How do I change the fee?** 

Modify the UNIT_BUDGET and UNIT_PRICE in the config.py. 

**Does this code work on devnet?**

No. 

### Example

```
from pump_fun import buy

# Buy Example
mint_str = "pump_token_address"
sol_in = .1
slippage = 5
buy(mint_str, sol_in, slippage)
```

```
from pump_fun import sell

# Sell Example
mint_str = "pump_token_address"
percentage = 100
slippage = 5
sell(mint_str, percentage, slippage)
```
