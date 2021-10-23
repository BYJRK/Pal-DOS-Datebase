import asyncio
from playwright.async_api import async_playwright
import json

HOST = 'http://www.whistlerwmz.my-place.us/'


async def to_dict(context, url):
    page = await context.new_page()
    while True:
        try:
            await page.goto(url)
            await page.wait_for_selector('#table6')
            break
        except:
            print('retry:', url)
            continue

    info = [
        await f.text_content()
        for f in await page.query_selector_all('font[face="新宋体"]')
    ]
    name = await page.title()
    print(name)
    return {
        'name': name,
        'lv': int(info[20]),
        'hp': int(info[2]),
        'exp': int(info[3]),
        'money': int(info[4]),
        'item': [info[6].strip(), int(info[7])],
        'gourd': int(info[5]),
        'resis': [int(n) for n in info[26:34]],
    }


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(HOST + 'enemy.htm')
        await asyncio.sleep(2)
        enemy_list = await page.query_selector_all(r'a[href^="enemy"]')

        hrefs = [await r.get_attribute('href') for r in enemy_list]
        tasks = []
        for href in hrefs:
            tasks.append(
                asyncio.create_task(to_dict(await browser.new_context(), HOST + href))
            )

        res = await asyncio.gather(*tasks)

        with open('enemies.json', 'w', encoding='utf-8') as f:
            json.dump(res, f)

        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
