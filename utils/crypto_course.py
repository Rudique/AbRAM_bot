from pycoingecko import CoinGeckoAPI


async def get_currency():
    result = ''
    cg = CoinGeckoAPI()
    result += f"BTC = {cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']} USD\n"
    result += f"ETH = {cg.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']} USD\n"
    result += f"DOGE = {cg.get_price(ids='dogecoin', vs_currencies='usd')['dogecoin']['usd']} USD\n"
    return result


