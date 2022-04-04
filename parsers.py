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
