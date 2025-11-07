strings23='''  
"Email: john.doe@example.com",
    "Contact: +91-9876543210",
    "TransactionID_12345_DONE",
    "Username: user_2025!",
    "Invoice #INV-00458",
    "Order placed on 2025-11-04",
    "Visit our site: https://www.learnregex.com",
    "Temp reading: 37.6°C",
    "Address: 42B Baker Street, London",
    "Note—check at 10:30am tomorrow!",
    "HELLO_world_Regex123",
    "E-mail: support@company.co.in",
    "Total Amount = $1499.75",
    "CustomerID: CUST_0098",
    "Alert! Invalid password entered 3 times",
    "Task Completed? Yes/No",
    "FlightNo: AI-202",
    "Marks: 78, 82, 91, 65",
    "Ref: #ABCDEF12345",
    "ZIP Code: 560034",
    "File saved as report_v2.1.pdf",
    "Email-Me@Now.org",
    "St",
    "Sot",
    "Soot",
    "st",
    "PASSWORD: My$ecret@123",
    "Meeting scheduled on Monday, 9th Dec",
    "Tag: <regex> is powerful </regex>",
    "User said: 'I love learning REGEX!'",
    "item-1, item_2, ITEM#3",
    "Room Temp: -5°C",
    "IP Address: 192.168.0.1",
    "Mask",
    "Lask",
    "aask",
    "5GB",
    "1TB",
    "11GB",
    " 123 ","Tasmd",
    "[pdf]",
    "[video]","Tog","kog","mog",
    "UUID: 550e8400-e29b-41d4-a716-446655440000"'''
import re  
pattern=r'So*t'
pattern2=r'[sS]o*[tT]'
pattern3=r"[A-Za-z]ask"
pattern4=r"\s\d{3}\s"                                    # \b is for word boundary
pattern5=r"[A-Z]\w{1,}"
pattern6=r"...."
pattern7=r"\[\w+\]"                                      #  "[[]\w+]"         \[ and \] are used to match the literal square brackets in the string.
pattern8=r"[^Tk]og"
pattern9=r"^Ta\w+"
pattern10=r"(\d+)(GB|TB)"
pattern11=r"(\d+)(GB|TB)(\w{0,})"



matches=re.findall(pattern10,strings23)                  # findall returns a list of all matches in the string
# matches=re.finditer(pattern10,strings23)                 # finditer returns an iterator yielding match objects
# matches=re.search(pattern10,strings23)                   # search returns a match object if there is a match anywhere in the string for only 1st occurence
# print(matches)                                           # prints the match object


# for match in matches:
#     print(match.group())                                 # group() returns the part of the string where there is a match for respective group number


# for ele in strings23:
#     match=re.finditer(pattern9,ele)
#     if match:
#         print(ele)

new_list=[]
for tup in matches:
    if tup[1]=='TB':
        new_num=int(tup[0])*1024
        new_list.append(new_num)
    else:
        new_list.append(tup[0])
print(new_list)