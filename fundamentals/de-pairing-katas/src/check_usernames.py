def check_usernames(user_name: str):
    flag = 0
    if len(user_name)>=5 and len(user_name)<=20:
        for char in user_name:
            if char.islower() or char.isdigit() or char=='_':
                flag+=1
    if flag==len(user_name):
        return True
    return False
