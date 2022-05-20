#!/usr/bin/env bash

firstNameList=('Felix' 'Kaitlin' 'Chantelle' 'Joel' 'Gabriella')
lastNameList=('Hoffman' 'Harris' 'Blair' 'Frank' 'Owen' 'Elliott')
yearlist=('1951' '1962' '1987' '1977' '1988' '1986' '2000' '1977')
monthList=('01' '02' '03' '04' '05' '06' '07' '08' '09' '10' '11' '12')
daylist=('01' '02' '03' '04' '05' '06' '07' '08' '09' '10' '11' '12' 
'13' '14' '15' '16' '17' '18' '19' '20' '21' '22' '23' '24' '25' '26' '27' '28')
genderlist=('M' 'F')
adress1=('1214' '1215' '1216' '1217' '1218' '1219' '1220' '1312' '1313' '1314' '1315')
adress2=('ROWELL' 'POWELL' 'GROMELL' 'BOWELY' 'GOMEDLY' 'GOHWELL' 'KOWELL' 'STOWELL')
adress3=('AVE' 'STR' 'PR' 'HALL' 'LA' 'WER')
adress4=('JOLIET' 'BOLIET' 'GROLIET' 'SDOLIET' 'PROLIET')
adress5=('IL' 'QW' 'ER' 'RT' 'TY' 'UI' 'IO' 'OP' 'AS' 'SD')
adress6=('60433' '60412' '60937' '60142' '60679' '60902')

headers='VOC.1.1,VOC.2.1,VOC.5.1,VOC.5.2,VOC.7.1,VOC.8.1,VOC.11.1,VOC.11.3,VOC.11.4,VOC.11.5, VOC.13.1'

echo -n "Enter number of rows: "
read row

pin=$(date +%Y%m%d-%H%M%S)
CSVfile=VOC_${pin}_${row}.csv
echo $headers > $CSVfile

for (( i=1; i <= $row; i++ ))
do
voc11=$i${adress1[RANDOM%${#adress1[@]}]}${adress6[RANDOM%${#adress6[@]}]}
voc21=$i${adress6[RANDOM%${#adress6[@]}]}${adress1[RANDOM%${#adress1[@]}]}
voc51=${firstNameList[RANDOM%${#firstNameList[@]}]}
voc52=${lastNameList[RANDOM%${#lastNameList[@]}]}
voc71=${yearlist[RANDOM%${#yearlist[@]}]}${monthList[RANDOM%${#monthList[@]}]}${daylist[RANDOM%${#daylist[@]}]}
voc81=${genderlist[RANDOM%${#genderlist[@]}]}
voc111="${adress1[RANDOM%${#adress1[@]}]} ${adress2[RANDOM%${#adress2[@]}]} ${adress3[RANDOM%${#adress3[@]}]}"
voc113=${adress4[RANDOM%${#adress4[@]}]}
voc114=${adress5[RANDOM%${#adress5[@]}]}
voc115=${adress6[RANDOM%${#adress6[@]}]}
voc131="test+$voc51$voc52$voc21@gmail.com"

echo $voc11,$voc21,$voc51,$voc52,$voc71,$voc81,$voc111,$voc113,$voc114,$voc115,$voc131 >> $CSVfile
done

echo "done"
