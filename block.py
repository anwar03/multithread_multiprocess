emails = ['dermaproclinica@gmail.com', 'dermaproclinica@yahoo.com', 'dermaproclinica@wix.com']
block_email = ['yahoo.com', 'wix.com']
filtered_emails = set()
# for email in emails:
#     if email.split('@')[1] not in block_email:
#         print('email = ', email)
li = [email for email in emails if email.split('@')[1] not in block_email]
print('email', li)
filtered_emails = set(li)
print('email', filtered_emails)