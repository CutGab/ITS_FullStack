import lepre
import tartaruga

def corsa():
    while True:
        track = ["_"] * 70

        tartaruga.tartaruga_step()
        lepre.lepre_step()

        if lepre.lepre >= 69:
            print("HARE WINS || YUCH!!!")
            break

        if tartaruga.tartaruga >= 69:
            print("TORTOISE WINS! || YAY!!!")
            break

        if lepre.lepre == tartaruga.tartaruga:
            track[lepre.lepre] = "OUCH!!!"

        else:
            track[lepre.lepre] = "L"
            track[tartaruga.tartaruga] = "T"

        print("".join(track))

        if lepre.lepre >= 69 or tartaruga.tartaruga >= 69:
            break
