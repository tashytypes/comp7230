with open("academics.txt", "r") as fin:
    with open("formattedacademics.txt", "w") as fout:
        for name in fin:
            p = name.find(",")
            if(p == -1): continue
            ln = name[0:p].strip().title()
            #first letter cap, rest small caps with title
            fn = name[p+1:].strip()
            fout.write("{0}. {1}\n".format(fn[0], ln))