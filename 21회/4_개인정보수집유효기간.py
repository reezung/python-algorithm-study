def change_to_day(y, m, d):
    return y * 336 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    today_to_day = change_to_day(today[0], today[1], today[2])

    dic = dict()
    for t in terms:
        type, month = t.split()
        dic[type] = int(month)

    for i in range(len(privacies)):
        date, type = privacies[i].split()
        y, m, d = map(int, date.split('.'))
        end_to_day = change_to_day(y, m + dic[type], d - 1)

        if today_to_day > end_to_day:
            answer.append(i + 1)

    return answer
