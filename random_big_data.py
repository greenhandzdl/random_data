import sys
import random
from faker import Faker

fake = Faker("zh_CN")

def generate_profile(sex=None):
    profile = fake.profile(fields=['name', 'sex', 'phone_number', 'birthdate', 'ssn', 'job', 'company', 'mail', 'address'], sex=sex)
    row = "| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
        profile['name'],
        "男" if profile['sex'] == 'M' else "女",
        fake.phone_number(),
        profile['birthdate'],
        profile['ssn'],
        profile['job'],
        profile['company'],
        profile['mail'],
        profile['address']
    )
    print(row)

# Print table header
header = "| 名字 | 性別 | 电话号码 | 出生年月日 | 身份证号码 | 工作单位 | 公司 | 电子邮件 | 地址 |"
separator = "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"
print(header)
print(separator)

# Generate profiles
if len(sys.argv) > 1:
    sex = sys.argv[1]
    if sex == 'M':
        generate_profile(sex='M')
    elif sex == 'F':
        generate_profile(sex='F')
    else:
        print("无效的选项. 请输入 'M' 或 'F'.")
else:
    sex = random.choice(['M', 'F'])
    generate_profile(sex=sex)