def conversor_seg(hora, min, seg):
    segundos = hora * 3600 + min * 60 + seg
    return(f'O horário {hora}:{min}:{seg} possui {segundos} segundos')


print(conversor_seg(10, 39, 25))
