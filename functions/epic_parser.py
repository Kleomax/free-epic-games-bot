import requests


def get_games() -> list:
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9',
        'dnt': '1',
        'origin': 'https://store.epicgames.com',
        'priority': 'u=1, i',
        'referer': 'https://store.epicgames.com/ru/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "YaBrowser";v="25.2", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'locale': 'ru',
        'country': 'RU',
        'allowCountries': 'RU',
    }

    response = requests.get(
        'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions',
        params=params,
        headers=headers,
    ).json()



    games = response["data"]["Catalog"]["searchStore"]["elements"]

    games_list = []

    for game in games:
        try:

            title = game["title"]

            start_date = game["promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["startDate"].split("T")[0]
            end_date = game["promotions"]["upcomingPromotionalOffers"][0]["promotionalOffers"][0]["endDate"].split("T")[0]

            price = game["price"]["totalPrice"]["fmtPrice"]["discountPrice"]

            link = f"https://store.epicgames.com/ru/p/{game['productSlug']}"
            
            image = game["keyImages"][0]["url"]

            games_list.append([title, start_date, end_date, price, link, image])

        except TypeError as ex:
            print(ex)

    return games_list

