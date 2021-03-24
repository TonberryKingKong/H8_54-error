def selamat_sore(guru,*murid):
    selamat = "selamat sore"
    selamat = selamat + " " + guru
    for m in murid :
            selamat = selamat + "," + m
    return selamat