import sys
import random
from faker import Faker

fake = Faker("zh_CN")

def generate_profile(sex=None):
    profile = fake.profile(fields=['name', 'sex', 'phone_number', 'birthdate', 'ssn', 'job', 'company', 'mail', 'address'], sex=sex)
    print("名字:", profile['name'])
    print("性別:", "男" if profile['sex'] == 'M' else "女")
    print("电话号码:", fake.phone_number())
    print("出生年月日:", profile['birthdate'])
    print("身份证号码:", profile['ssn'])
    print("工作单位:", profile['job'])
    print("公司:", profile['company'])
    print("电子邮件:", profile['mail'])
    print("地址:", profile['address'])

if len(sys.argv) > 1:
    sex = sys.argv[1]
    if sex == 'M':
        print("男性资料:")
        generate_profile(sex='M')
    elif sex == 'F':
        print("\n女性资料:")
        generate_profile(sex='F')
    else:
        print("无效的选项. 请输入 'M' 或 'F'.")
else:
    sex = random.choice(['M', 'F'])
    if sex == 'M':
        print("男性资料:")
        generate_profile(sex='M')
    else:
        print("\n女性资料:")
        generate_profile(sex='F')