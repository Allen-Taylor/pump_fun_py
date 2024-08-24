# pump_fun_py

Python library to trade on pump.fun. 

Updated: 8/24/2024

Clone the repo, and add your Private Key (Base58 string) and RPC to the config.py.

**Please support my work and donate to: 3pPK76GL5ChVFBHND54UfBMtg36Bsh1mzbQPTbcK89PD**

### Contact

My services are for **hire**. Contact me if you need help integrating the code into your own project. 

Telegram: @AL_THE_BOT_FATHER

### FAQS

**What format should my private key be in?** 

The private key should be in the base58 string format, not bytes. 

**Why are my transactions being dropped?** 

You get what you pay for. If you use the public RPC, you're going to get rekt. Spend the money for Helius or Quick Node. Also, play around with the compute limits and lamports.

### Example

```
from pump_fun import buy

#BUY
buy(mint_str="token_to_buy", sol_in=.1, slippage=25)

```
```
from pump_fun import sell
from utils import get_token_balance

#SELL
mint_str = "token_to_sell"
token_balance = get_token_balance(mint_str)
sell(mint_str=mint_str, token_balance=token_balance, slippage=25, close_token_account=True)
```
