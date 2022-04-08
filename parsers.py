import requests
import bs4
from bs4 import BeautifulSoup


def parse_terrakot18():
    url = "https://terrakot18.ru/1491_puffy/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []
    price = soup.find("div", class_="priceItem")
    price = float(price.text.split(" ")[0].replace(",", ".")) if price else None
    price_one = soup.find("div", class_="priceOneItem")
    price_one = float(price_one.text.split(" ")[0].replace(",", ".")) if price_one else price_one

    items = soup.find_all("div", class_="items_div")
    for item in items:
        code_name = item.find("p", "text5")
        code_name = code_name.text.split(" ") if code_name else None
        code = int(code_name[0]) if code_name else None
        name = " ".join(code_name[1:]) if code_name else None
        balance = item.find("p", class_="text6")
        balance = int(balance.text.split(" ")[1]) if balance else None

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_optwool():
    url = "https://optwool.ru/pryazha/puffy/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    price = soup.find("div", class_="gmsinglprice")
    price = float(price.text.split(" ")[0].replace(",", ".")) if price else None
    price_one = price / 5 if price else None

    items = soup.find("ul", class_="griddmva")
    items = items.find_all("li") if isinstance(items, bs4.Tag) else []

    for item in items:
        code_name = item.find("p", "text2")
        code_name = code_name.text.split(" ") if code_name else None
        code = int(code_name[0]) if code_name else None
        name = " ".join(code_name[1:]) if code_name else None
        balance = [elem for elem in item.find_all("p") if "остаток" in elem.text][0]
        balance = int(balance.text.split(" ")[1]) if balance else None

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_2676270():
    url = "https://2676270.ru/catalog/yarn/92/29313/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    price = soup.find("div", class_="price")
    price = float(price.text.split(" ")[0].replace(",", ".")) if price else None
    price_one = price / 5 if price else None

    items = soup.find("ul", class_="colors")
    items = items.find_all("li") if isinstance(items, bs4.Tag) else []

    for item in items:
        code_name = item.find("div", class_="name")
        code_name = code_name.text.split(" ") if code_name else None
        code = int(code_name[0].replace("\n", "")) if code_name else None
        name = " ".join(code_name[1:]).strip() if code_name else None
        # balance = [elem for elem in item.find_all("p") if "остаток" in elem.text][0]
        # balance = int(balance.text.split(" ")[1]) if balance else None
        balance = None

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result

# нужно залогиниться
def parse_supernitki():
    url = "https://supernitki.ru/catalog/puffy"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # print(page.text)

    result = []

    price = soup.find("div", class_="product__price")
    # price = price.find("span") if price else None
    # price = float(price.text.split(" ")[0].replace(",", ".")) if isinstance(price, bs4.Tag) else None
    # price_one = price / 5 if price else None
    # print(price)

    items = soup.find_all("div", class_="product-color")
    # items = items.find_all("li") if isinstance(items, bs4.Tag) else []

    # for item in items:
    #     code_name = item.find("div", class_="name")
    #     code_name = code_name.text.split(" ") if code_name else None
    #     code = int(code_name[0].replace("\n", "")) if code_name else None
    #     name = " ".join(code_name[1:]).strip() if code_name else None
    #     # balance = [elem for elem in item.find_all("p") if "остаток" in elem.text][0]
    #     # balance = int(balance.text.split(" ")[1]) if balance else None
    #     balance = None

    #     result.append({
    #         "code": code, 
    #         "name": name,
    #         "balance": balance, 
    #         "price": price, 
    #         "price_one": price_one,
    #         "url": url
    #     })

    # return result


def parse_rukodelie_online():
    url = "https://rukodelie-online.ru/catalog/puffy-alize.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    items = soup.find_all("div", class_="colour_card")
    for item in items:
        code_name = item.find("div", class_="name")
        code_name = code_name.text.split(" ") if code_name else None
        code = int(code_name[0].replace("\n", "")) if code_name else None
        name = " ".join(code_name[1:]).strip() if code_name else None
        balance = item.find("input", class_="numberfield input floatl")
        # balance = int(float(balance.get("max")) / 5) if balance else None
        balance = balance.get("data-real-max") if balance else None
        balance = float(balance) / 5 if balance else None
        price_one = item.find("span", class_="fs30")
        price_one = float(price_one.text)
        price = price_one * 5

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_klubok_store():
    url = "https://klubok.store/catalog/pryazha/alize/alize_osnovnoe/puffy/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    price = soup.find("span", class_="price_value")
    price = float(price.text.split(" ")[0].replace(",", ".")) if price else None
    price_one = soup.find("div", class_="one-price")
    price_one = float(price_one.text.split(" ")[-2].replace(",", ".")) if price_one else None

    items = soup.find("ul", class_="tabs_slider RECOMENDATION_slides slides catalog_block")
    items = items.find_all("li") if isinstance(items, bs4.Tag) else []

    for item in items:
        code = item.find("span", class_="color-number")
        code = int(code.text) if code else None
        name = item.find("span", class_="color-name")
        name = name.text if name else None
        balance = None

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_pryazhaoptom():
    url = "https://pryazhaoptom.ru/shop/pryazha-alize-puffi-alize-puffy/?wmc-currency=RUB"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    price = soup.find("span", class_="woocommerce-Price-amount amount")
    price = float(price.text.split("\xa0")[0].replace(",", ".")) if price else None
    price_one = price / 5 if price else None

    items = soup.find("form", class_="variations_form cart")
    items = items.find("select")  if isinstance(items, bs4.Tag) else None
    items = items.find_all("option") if isinstance(items, bs4.Tag) else []
    
    for item in items:
        if item.text == "Выбрать опцию":
            continue
        code = int(item.text)
        name = None
        balance = None

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_yarn_ural():
    url = "https://xn----7sbbv2athd0a0j.xn--p1ai/catalogue//catalogue/vse-towary/532-puffy"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    items = soup.find_all("li", class_="js-price-item")
    
    for item in items:
        code_name = item.find("div", class_="title-")
        code_name = code_name.text.split(" ") if code_name else None
        code = int(code_name[0].replace("\n", "")) if code_name else None
        name = " ".join(code_name[1:]).strip() if code_name else None
        balance = item.find("input", class_="qty-input js-qty-input")
        balance = int(balance.get("max")) if balance else None
        price = item.find("span", class_="js-sum")
        price = float(price.text)
        price_one = price / 5

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_nopt():
    url = "https://n-opt.ru/shop/alize-alize-optom/puffy"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []

    items = soup.find_all("div", class_="list-item")
    
    for item in items:
        code_name = [a for a in item.find_all("a") if "Пуффи" in a.text]
        code_name = code_name[0].text.split(" ")[1:] if code_name else None
        code = int(code_name[0].replace("\n", "")) if code_name else None
        name = " ".join(code_name[1:]).strip() if code_name else None
        balance = None
        price = [span for span in item.find_all("span") if "руб" in span.text]
        price = float(price[0].text.split("руб")[0])
        price_one = price / 5

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result


def parse_airis_spb():
    url = "https://airis.spb.ru/catalog/vyazanie/pryazha_i_nitochnye_izdeliya/pryazha_alize/1146394_pryazha_alize_puffy_100g_9m_100_mikropoliester_/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    print(page.text)
    result = []

    items = soup.find_all("div", class_="choice-color__color col-12 col-md-4 col-xxl-4 col-exl-4 item")
    print(items)
    for item in items:
        code_name = item.find("div", class_="color__title")
        code_name = code_name[0].text.strip().split(" ")[1:] if code_name else None
        code = int(code_name[0].replace("\n", "")) if code_name else None
        name = " ".join(code_name[1:]).strip() if code_name else None
        balance = None
        price_one = item.find("div", class_="main-card__in-cart formula")
        price_one = float(price_one.text.strip().split(" ")[-1])
        price = price_one * 5

        result.append({
            "code": code, 
            "name": name,
            "balance": balance, 
            "price": price, 
            "price_one": price_one,
            "url": url
        })

    return result
