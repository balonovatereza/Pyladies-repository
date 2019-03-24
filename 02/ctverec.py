
# program pocita obvod a obsah ctverce, a obvod a obsah kruhu o
# stejnem polomeru.
a = 356  # v centimetrech
pi = 3.1415926
obvodctverce = 4*a
obsahctverce = a**2
obvodkruhu = 2*pi*a
obsahkruhu = pi*a**2
print("Obvod ctverce o hrane ", a, " je ", obvodctverce, "cm")
print("Obsah ctverce o hrane ", a, " je ", obsahctverce, "cm2")
print("Obvod kruhu o polomeru ", a, " je ", obvodkruhu, "cm")
print("Obsah kruhu o polomeru ", a, " je ", obsahkruhu, "cm2")

# Spo49t8 obvod a obsah ctverce podle zadane hodnoty aod uzivatele
strana = float(input("Zadej delku strany ctverce v cm, ze ktere chces vypocitat obvod a obsah: "))
obvodctverce2 = 4*strana
obsahctverce2 = strana**2
print("Obvod ctverce o hrane ", strana, " je ", obvodctverce2, "cm")
print("Obsah ctverce o hrane ", strana, " je ", obsahctverce2, "cm2")
