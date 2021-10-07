import datetime
nome = 'Isaac'
email = 'isaac@gmail.com'
senha = 'isaac'
horas = "0,0,1,1,3,2,1"
nome_plano = 'Plano 01'
nome_mtd = 'Metodologia 01'
expiracao = 1

assuntos = [{'ass_nome': 'AAAAAAAAAAAAAAAAAAA',
             'ass_coment': u'Ler livros', 'tempo': 45, 'ordem': 2},
            {'ass_nome': 'BBBBBBBBBBBBBBBBBB',
                'ass_coment': 'Ler mais livros', 'tempo': 30, 'ordem': 2},
            {'ass_nome': 'CCCCCCCCCCCCCCCCCC',
                'ass_coment': 'Ler mais livros', 'tempo': 30, 'ordem': 2},
            {'ass_nome': 'DDDDDDDDDDDDDDDDDD',
                'ass_coment': 'Ler mais livros', 'tempo': 30, 'ordem': 2},
            {'ass_nome': 'EEEEEEEEEEEEEEEEEEE',
                'ass_coment': 'Ler mais livros', 'tempo': 30, 'ordem': 2},
            ]


cexerc = [3, 9, 15]
crevi = [2, 4, 8]

tmp = []


def hourDay(day):
    days = {
        # 0 eh segunda 6 eh domingo
        0: int(horas.split(",")[0]),
        1: int(horas.split(",")[1]),
        2: int(horas.split(",")[2]),
        3: int(horas.split(",")[3]),
        4: int(horas.split(",")[4]),
        5: int(horas.split(",")[5]),
        6: int(horas.split(",")[6]),
    }

    return days[day]*60


today = datetime.datetime.now()

# gera 31 dias dentro de tmp
for i in range(0, 200):
    add = datetime.timedelta(days=i)
    currentDay = today + add
    tmp.append({
        "date": currentDay.strftime('%d/%m/%Y'),
        "time": hourDay(currentDay.weekday()),
        "ass": [],
        "status": ""
    })


adicionado = []


def typeAss(ass, type):
    types = {
        0: 'estudo',
        1: 'revisao',
        2: 'exercicio',
    }
    return {
        'ass_nome': ass["ass_nome"],
        'ass_coment': ass["ass_coment"],
        'tempo': ass["tempo"],
        'type': types[type],
        'ordem': ass["ordem"]
    }


def hisTime(ass, day):
    atual = day.get('time')
    assunto = ass.get('tempo')
    if atual <= 0 or assunto > atual:
        return False
    return True


def hisRevi(ass, idx):
    if tmp[idx]["time"] == 0 or adicionado.append(ass):
        return False

    ass_time = ass.get('tempo')

    while tmp[idx]["time"] - ass_time < 0:
        idx += 1
    # TODO: ass.update type = estudo nao eh adicionado no primeiro giro
    tmp[idx].update({'time': (tmp[idx]["time"] - ass_time)})
    tmp[idx]["ass"].append(typeAss(ass, 0))

    for i in crevi:
        while tmp[idx + i]["time"] - ass_time < 0:
            idx += 1
        tmp[idx + i].update({'time': (tmp[idx + i]["time"] - ass_time)})
        tmp[idx + i]["ass"].append(typeAss(ass, 1))

    for i in cexerc:
        while tmp[idx + i]["time"] - ass_time < 0:
            idx += 1
        tmp[idx + i].update({'time': (tmp[idx + i]["time"] - ass_time)})
        tmp[idx + i]["ass"].append(typeAss(ass, 2))


for ass in assuntos:
    for index in range(len(tmp)):
        if not hisTime(ass, tmp[index]):
            continue
        elif hisTime(ass, tmp[index]):
            if ass not in adicionado:
                hisRevi(ass, index)
            continue


for r in range(20):
    print(tmp[r])
