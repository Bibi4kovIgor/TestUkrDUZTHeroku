class Vremya:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def raznost(self, vrem):           #знаходження різниці двох моментів часу в секундах
        s1_sec = (self.h*3600)+(self.m*60)+self.s
        s2_sec = (vrem.h*3600)+(vrem.m*60)+vrem.s
        res_sec = s2_sec-s1_sec
        return res_sec

    def slog(self):              #додавання до часу однієї секунди
        s1_sec = (self.h*3600)+(self.m*60)+self.s
        res = s1_sec+1
        res1 = res//3600
        res2 = (res%3600)//60
        res3 = (res%3600)%60
        print ("После добавления одной сек: ", res1, "h", res2, "m", res3)

    def poriv(self,vrem):         #порівняння двох часів (однакові або ні).
        s1_sec = (self.h*3600)+(self.m*60)+self.s
        s2_sec = (vrem.h*3600)+(vrem.m*60)+vrem.s
        if s1_sec == s2_sec:
            print("Времена равны")
        else:
            print("Времена не равны")


if __name__ == '__main__':
    vrem1 = Vremya(13, 25, 37)
    vrem2 = Vremya(13, 30, 37)


    vrem3 = Vremya.slog(vrem1)
    vrem4 = Vremya.raznost(vrem1, vrem2)
    print("Разница в секундах: ", vrem4)
    Vremya.poriv(vrem1, vrem2)