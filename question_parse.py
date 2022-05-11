def parse_question(question: str):
    if question[:59] == "A child is attempting to build a pillow fort in their home.":
        return "pillow"
    elif question[:41] == "A worker is capable of pushing a box with":
        return "workerpush"
    elif question[:23] == "A bulldozer pushes on a":
        return "bulldozerpush"
    elif question[-6:] == "m/s^2.":
        return "hockey"
    elif question[9:78] == "dumpster needs to be moved so it can be picked up by waste management":
        return "dumpster"
    else:
        return "curling"

def answer_question(question: str, qtype: str):

    if qtype == "pillow":
        mass = int(question[72:74])
        news = int(question[99:102])
        mewstatic = float(question[161:165])
        mewkinetic = float(question[-5:-1])

        print(mass, news, mewstatic, mewkinetic)
        
        if (mass * 9.8) * mewstatic > news:
            return 0
        else:
            push_speed = (mass * 9.8) * mewkinetic
            return round(news - push_speed, 2)

    if qtype == "workerpush":
        force = int(question[42:45])
        mew = float(question[-5:-1])

        return round(((force / mew) / 9.8), 2)

    if qtype == "bulldozerpush":
        mass = int(question[24:27])
        force = int(question[60:66].replace(",", ""))

        print(mass, force)

        return round(force / (mass * 9.8), 2)

    if qtype == "hockey":
        mass = int(question[2:5])
        decel = float(question[-11:-7])

        decel_fc = decel * mass

        nforce = mass * 9.8

        return round(decel_fc / nforce, 2)

    if qtype == "dumpster":
        mass = int(question[2:5])
        mew = float(question[-5:-1])
        return round((mass * 9.8) * mew, 2)

    if qtype == "curling":
        mass = int(question[2:4])
        mew = float(question[-5:-1])
        return round((mass * 9.8) * mew, 2)

prob = "A 24 kg curling stone is sliding across the ice after having been thrown.  The coefficient of kinetic friction between the stone and the ice is 0.22."

print(answer_question(prob, "curling"))
