# -*- coding: utf-8 -*-

import math
def sockerkaka(antal):
    egg = str(int(math.ceil((antal*3.0/4))))+" egg(s)\n"
    sugar = str(antal*3.0/4)+" dl sugar\n"
    vanilla = str(antal*2.0/4)+" tbs vanilla\n"
    bakingsoda = str(antal*2.0/4)+" tbs bakingsoda\n"
    flour = str(antal*3.0/4)+" dl flour\n"
    butter = str(antal*75.0/4)+" g butter\n"
    water = str(antal*1.0/4)+" dl water\n"
    recept = ("Recipe for "+str(antal)+" people\n"\
    +egg+sugar+vanilla+bakingsoda+flour+butter+water)
    return(recept)


print(sockerkaka(1)+"\n"+sockerkaka(7))
