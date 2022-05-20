import os
from datetime import datetime
import random

firstNameList = ('Felix', 'Kaitlin', 'Chantelle', 'Joel', 'Gabriella')
lastNameList = ('Hoffman', 'Harris', 'Blair', 'Frank', 'Owen', 'Elliott')
yearlist = ('1951', '1962', '1987', '1977', '1988', '1986', '2000', '1977')
monthList = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
daylist = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28')
genderlist = ('M', 'F')
adress1 = ('1214', '1215', '1216', '1217', '1218', '1219', '1220', '1312', '1313', '1314', '1315')
adress2 = ('ROWELL', 'POWELL', 'GROMELL', 'BOWELY', 'GOMEDLY', 'GOHWELL', 'KOWELL', 'STOWELL')
adress3 = ('AVE', 'STR', 'PR', 'HALL', 'LA', 'WER')
adress4 = ('JOLIET', 'BOLIET', 'GROLIET', 'SDOLIET', 'PROLIET')
adress5 = ('IL', 'QW', 'ER', 'RT', 'TY', 'UI', 'IO', 'OP', 'AS', 'SD')
adress6 = ('60433', '60412', '60937', '60142', '60679', '60902')


def date_marker():
    today = datetime.today()
    date_marker = today.strftime("%Y%m%d_%H%M%S")
    return date_marker


def create_file(filename, row):
    file = open(filename, "w")
    file.write(row)
    file.close()


def create_xml():
    rows = int(input("Enter number of files: "))
    i = 0
    while i < rows:
        i += 1
        voc11 = f"{i}{random.choice(adress1)}{random.choice(adress6)}"
        voc21 = f"{i}{random.choice(adress6)}{random.choice(adress1)}"
        voc51 = f"{random.choice(firstNameList)}"
        voc52 = f"{random.choice(lastNameList)}"
        voc71 = f"{random.choice(yearlist)}{random.choice(monthList)}{random.choice(daylist)}"
        voc81 = f"{random.choice(genderlist)}"
        voc111 = f"{random.choice(adress1)} {random.choice(adress2)} {random.choice(adress3)}"
        voc113 = f"{random.choice(adress4)}"
        voc114 = f"{random.choice(adress5)}"
        voc115 = f"{random.choice(adress6)}"
        voc131 = f"test+{voc51}{voc52}{voc21}@gmail.com"
        filename = f"VOC_{date_marker()}{voc52}{voc51}_{voc21}.xml"
        d_row = f"<?xml version='1.0' encoding='UTF-8' ?><HL7Message><voc><VOC.1><VOC.1.1>{voc11}</VOC.1.1></VOC.1>" \
                f"<VOC.2><VOC.2.1>{voc21}</VOC.2.1></VOC.2><VOC.3/><VOC.4/><VOC.5><VOC.5.1>{voc51}</VOC.5.1>" \
                f"<VOC.5.2>{voc52}</VOC.5.2><VOC.5.3/></VOC.5><VOC.6/><VOC.7><VOC.7.1>{voc71}</VOC.7.1></VOC.7>" \
                f"<VOC.8><VOC.8.1>{voc81}</VOC.8.1></VOC.8><VOC.9/><VOC.10/><VOC.11><VOC.11.1>{voc111}</VOC.11.1>" \
                f"<VOC.11.2/><VOC.11.3>{voc113}</VOC.11.3><VOC.11.4>{voc114}</VOC.11.4><VOC.11.5>60433</VOC.11.5>" \
                f"</VOC.11><VOC.12/><VOC.13><VOC.13.1>{voc131}</VOC.13.1></VOC.13><VOC.14/><VOC.15/><VOC.16/><VOC.17/>" \
                f"<VOC.18/><VOC.19/><VOC.20/></voc></HL7Message>"
        create_file(filename, d_row)


if __name__ == '__main__':
    create_xml()
    print("done")
