
def get_capacity(T, P, U=48):
    """
    принимает время в часах и нагрузку в кВт
    возвращает емкость АКБ для 12Вольт
    """            
    C_gen = (P*1000 * T) / (U * get_K())
    return C_gen

def get_bat_cap(C, N):
    """
    Принимаем общую емкость и число батарей
    возвращает емкость
    """
    C_bat = C / N
    return C_bat

def get_work_time(C_bat, N, P):
    """
    Принимаем емкость батареи, число батарей, нагрузку
    возвращает время автономной работы в часах
    """
    C_gen = C_bat * N
    U = 12
    T = (U * get_K() * C_gen  ) / ( P*1000 )
    return T

def get_K(K=0.9, K_gr=0.7, K_de = 0.8 ):
    """
    Принимает коэфициенты такие как
    K - КПД инвертора
    K_gr - глубина разряда АКБ
    K_de - коэфициент доступной емкости зависит температуры и времени разряда   
    """
    return K * K_gr * K_de

def main():
    T = int(input("Введите время автономной работы в часах: "))
    P = float(input("Введите необходимую мощность нагрузки в кВт: "))
    N = int(input("Введите число АКБ в ИБП: "))
    C_gen = get_capacity(T, P)
    C_bat = get_bat_cap(C_gen, N)
    print("Общая емкость должна быть: {:02.2f}".format(C_gen))
    print("Емкость одной батареи должна быть: {:02.2f}".format(C_bat))

if __name__ == "__main__":
    print("{:02.2f}".format(get_work_time(100, 8, 0.6)))
    print("{:02.2f}".format(get_capacity(4, 8), 48))