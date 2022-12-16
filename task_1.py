# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# абвестмри, абв, нспмвабвгане, неумпрмабв, некмвпа, екывспыв

with open('file1.txt', 'r+', encoding='utf-8') as data:
    #new_str = [i for i in str if "абв" not in i]
    # new_str = list(filter(lambda i: not 'абв' in i, data.readline().split()))
    # print(new_str)
    data.write('\n' + ''.join(list(filter(lambda i: not 'абв' in i, data.readline().split()))))


