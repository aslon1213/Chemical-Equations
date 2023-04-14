def biologival_reactions():

    r_1 = []
    print("Stage 1")
    for i in range(4):
        for j in range(4):
            if i != j and i < j and i > 0 and j > 0:
                A  = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0], [0,0,0], [0,0,0]]
                A[0][0] = i
                A[1][0] = j
                A[6][2] = 1
                r_1.append(A)
                A[6][2] = 0
                A[6][1] = 1
                r_1.append(A)

                A  = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0], [0,0,0], [0,0,0]]
                A[0][1] = i
                A[1][1] = j
                A[6][2] = 1
                r_1.append(A)
                A[6][2] = 0
                A[6][0] = 1
                r_1.append(A)

                A  = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0], [0,0,0], [0,0,0]]
                A[0][2] = i
                A[1][2] = j
                A[6][0] = 1
                r_1.append(A)
                A[6][0] = 0
                A[6][1] = 1
                r_1.append(A)

    print('Stage 2')
    r_2 = []
    for i in range(4):
        for j in range(4):
            for r in r_1:
                if r[1][0] > 0 and i > 0 and j > 0:
                    r[3][2] = i
                    r[5][1] = j
                    r_2.append(r)
                    r[3][2] = j
                    r[5][1] = i
                    r_2.append(r)
                if r[1][1] > 0 and i > 0 and j > 0:
                    r[3][2] = i
                    r[5][0] = j
                    r_2.append(r)
                    r[3][2] = j
                    r[5][0] = i
                    r_2.append(r)
                if r[1][2] > 0 and i > 0 and j > 0:
                    r[3][0] = i
                    r[5][1] = j
                    r_2.append(r)
                    r[3][0] = j
                    r[5][1] = i
                    r_2.append(r)

    print("Stage 3")
    r_3 = []
    for i in range(3):
        for j in range(4):
            for k in range(4):
                for r in r_2:
                    max_for_x = r[1][0] + r[3][0] + r[5][0] - r[6][0] - r[0][0]
                    max_for_y = r[1][1] + r[3][1] + r[5][1] - r[6][1] - r[0][1]
                    max_for_z = r[1][2] + r[3][2] + r[5][2] - r[6][2] - r[0][2]
                    if i <= max_for_x and j <= max_for_y and k <= max_for_z and (i + j + k) <(9 - r[6][0] - r[6][1] - r[6][2] - r[0][0] - r[0][1] - r[0][2] - 1):

                        r[2][0] = i
                        r[2][1] = j
                        r[2][2] = k
                        r_3.append([r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]])
    print("Stage 4")                    
    r_4 = []
    for i in range(3):
        for j in range(4):
            for k in range(4):
                for r in r_3:
                    max_for_x = r[1][0] + r[3][0] + r[5][0] - r[6][0] - r[0][0] - r[2][0]
                    max_for_y = r[1][1] + r[3][1] + r[5][1] - r[6][1] - r[0][1] - r[2][1]
                    max_for_z = r[1][2] + r[3][2] + r[5][2] - r[6][2] - r[0][2] - r[2][2]
                    if i <= max_for_x and j <= max_for_y and k <= max_for_z:

                        r[4][0] = i
                        r[4][1] = j
                        r[4][2] = k
                        r_4.append([r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]])
    print("writing")
    r_5 = []
    for i in r_4:
        if i not in r_5:
            r_5.append(i)
    r_4 = r_5[:]
    with open("reactions_2.txt", "w") as f:
        for r in r_4:
            st_1 = "A"
            dictt = {
                0: "X",
                1: "Y",
                2: "Z", }
            for i in range(3):
                if(r[0][i] != 0):
                    if i != 0:
                        st_1 += "+" + str(r[0][i]) + dictt[i] + " "
                    else:
                        st_1 += str(r[0][i]) + dictt[i] + " "
            st_1 += "-> "
            for i in range(3):
                if(r[1][i] != 0):
                    st_1 += str(r[1][i]) + dictt[i] + ""
            f.write(st_1)
            f.write("\n")
            st_1 = ""
            for i in range(3):
                if(r[2][i] != 0):
                    if i != 0:
                        st_1 += "+" + str(r[2][i]) + dictt[i] + ""
                    else:
                        st_1 += str(r[2][i]) + dictt[i] + ""
            st_1 += " -> "
            for i in range(3):
                if(r[3][i] != 0):
                    if i != 0:
                        st_1 += str(r[3][i]) + dictt[i] + " "
                    else:
                        st_1 += str(r[3][i]) + dictt[i] + ""
            f.write(st_1)
            f.write("\n")
            st_1 = ""
            print(r[4])
            for i in range(3):
                if(r[4][i] != 0):
                    if(i != 0):
                        st_1 += "+" + str(r[4][i]) + dictt[i] + " "
                    else:
                        st_1 += str(r[4][i]) + dictt[i] + " "
            st_1 += " -> "
            for i in range(3):
                if(r[5][i] != 0):
                    st_1 += str(r[5][i]) + dictt[i] + " "
            f.write(st_1)
            f.write("\n")
            st_1 = ""
            for i in range(3):
                if(r[6][i] != 0):
                    st_1 += str(r[6][i]) + dictt[i ] + " "
            st_1 += "-> B"
            
            f.write(st_1)
            f.write("\n")
            f.write("#############################################################")
            f.write("\n")                 

biologival_reactions()

    