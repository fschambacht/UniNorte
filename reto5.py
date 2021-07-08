
def leer_ciudad():

    data = []
    with open('./data.csv', 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip().split(','))

    ciudad = input()
    acidez = []
    mat_org = []
    no_apto = 0
    marginalmente_apto = 0
    moderadamente_apto = 0
    sumamente_apto = 0

    for line in data:
        if line[0] == ciudad:

            acidez.append(float(line[2]))
            mat_org.append(float(line[3]))

            if line[6] == 'no apto':
                no_apto += 1
            elif line[6] == 'marginalmente apto':
                marginalmente_apto += 1
            elif line[6] == 'moderadamente apto':
                moderadamente_apto += 1
            elif line[6] == 'sumamente apto':
                sumamente_apto += 1
    
    cat = {
        'marginalmente apto': marginalmente_apto,
        'moderadamente apto': moderadamente_apto,
        'no apto': no_apto,
        'sumamente apto': sumamente_apto
            }
    
    cat_ord = sorted(cat.items(), key=lambda x: x[1], reverse=True)
    
    prom_acidez = sum(acidez) / len(acidez)
    prom_mat_org = sum(mat_org) / len(mat_org)


    print(f'{prom_acidez:.2f} {prom_mat_org:.2f}')
    print(f'{min(acidez)} {min(mat_org)}')
    print(f'{max(acidez)} {max(mat_org)}')

    for i in cat_ord:
        print(*i)


if __name__ == '__main__':
    leer_ciudad()