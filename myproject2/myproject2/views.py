# from django.shortcuts import render

# def hello(request):
#     return render(request, "hello.html")

# from django.shortcuts import render
# import requests
# from bs4 import BeautifulSoup

# def home(request):
#     content = None

#     if request.method == "POST":
#         url = "https://en.wikipedia.org/wiki/Virat_Kohli"  # target website
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#         }
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, "html.parser")

#         # Example: scrape page title
#         if soup.title:
#             content = soup.title.get_text()
#         else:
#             content = "Title not found"


#     return render(request, "home.html", {"content": content})
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):
    content = None

    if request.method == "POST":
        url = "https://en.wikipedia.org/wiki/Virat_Kohli"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Wikipedia main content
        content_div = soup.find("div", id="mw-content-text")

        if content_div:
            # Get first meaningful paragraph
            for p in content_div.find_all("p"):
                text = p.get_text(strip=True)
                if text:
                    content = text
                    break
        else:
            content = "Content not found"

    return render(request, "home.html", {"content": content})
