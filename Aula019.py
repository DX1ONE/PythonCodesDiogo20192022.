pessoas = {'nome': 'Diogo', 'sexo': 'M', 'idade': 18}
pessoas['peso'] = 58.1
print(f'O {pessoas["nome"]} tem {pessoas ["idade"] } anos.')
for k, v in pessoas.items():
    print(f'{k} = {v}')