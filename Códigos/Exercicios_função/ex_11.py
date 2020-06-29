def media_nota(a, b, c, rank):
    if rank == 'A':
        media = a + b + c / 3
        return round(media, 2)
    else:
        media_p = ((a * 5 + b * 3 + c * 2) / (10))
        return media_p


print(media_nota(3, 9, 8, rank='A'))
