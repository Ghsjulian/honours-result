import requests
from bs4 import BeautifulSoup
import color
import os 

os.system("clear")
os.system("\n\n")
os.system('figlet -f small "Honours Result"|lolcat')


# url = f"http://nubd.info/results/result_show.php?reg_no={reg_no}&exm_code={exm_code}&exam_year={exm_year}"
def get_result(reg,exm_code,exm_year):
  results = []
  string = ""
  grade = ""
  url = f"http://nubd.info/results/result_show.php?reg_no={reg}&exm_code={exm_code}&exam_year={exm_year}"
  response = requests.get(url) 
  soup = BeautifulSoup(response.content, 'html.parser')
  tr = soup.find_all('table')
  first = tr[2].find_all('tr')
  second = tr[3].find_all('tr')
  grade = second[1]
  data = first
  for tr in data:
    string += str(tr)
  grade_tr = f'<tr align="center"><td height="26"><strong>Course-wise LetterGrade/Marks </strong></td><td>{grade.text}</td></tr>'
  ghs = '<tr><td class="ghs">Made By : </td><td class="name">Ghs Julian</td></tr>'
  f = open("config/data.txt", "a")
  f.write('<table class="tb--">'+string+grade_tr+ghs+'</table>')
  f.close()

exm_code = "2201"
exm_year = '2022'
main = '212110853'
index = 48

reg = input(color.YELLOW+color.BOLD+"[+] Enter Registration Number : "+color.LIGHT_CYAN+color.BOLD)

get_result(reg,exm_code,exm_year)


"""

for i in range(50):
  reg_no = main+str(index)
  get_result(reg_no,exm_code,exm_year)
  index+= i
  print(color.YELLOW+color.BOLD+f"[+] Getting Results...({color.LIGHT_CYAN+color.BOLD+str(i)})",end="\r")
"""

with open("config/data.txt", 'r', encoding='utf-8') as f:
  html_content = f.read()
  html = f"""
  <!doctype html>
  <html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Electric Bill Information</title>
        <link rel="stylesheet" type="text/css" href="./index.css" />
    </head>
    <body>
        <h2>Honours First Year Results</h2>
        <table>
        {html_content}
        </table>
    </body>
  </html>
  """
  f = open("config/index.html", "w")
  f.write(html)
  f.close()
print(color.GREEN+color.BOLD+"\n\nAll Results Has Saved Successfully \n")
