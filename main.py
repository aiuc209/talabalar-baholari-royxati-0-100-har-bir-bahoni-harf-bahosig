def baholarni_harfga_aylantir(baholar):
    harf_baholar = []
    for baho in baholar:
        if baho >= 90:
            harf_baholar.append('A')
        elif baho >= 80:
            harf_baholar.append('B')
        elif baho >= 70:
            harf_baholar.append('C')
        elif baho >= 60:
            harf_baholar.append('D')
        else:
            harf_baholar.append('F')
    return harf_baholar

baholar = [85, 90, 78, 92, 88, 76, 95, 89, 91, 82]
print(baholarni_harfga_aylantir(baholar))
