# coding=UTF-8

wersja_qrLM = 'Beta 20.0702'
ile_zetonow_dziennie_max = '2'
dostawcy=('wyszdr','kntuss')
pietra=('3b','4a','5a','5b','6b')
id_zetonu=randomString(8).replace('q','k')
data_zetonu=datetime.datetime.now().strftime("%Yq%mq%d")
wiersz_godz=('w1','w2','w3','w4','w5')  # odpowiadają kolejno godzinom 0900-0910, 0910-0920, 0920-0930,0930-0940,0940-0950
tydzien= ('','','','','')
tydzien_pon= {"3b":"w3","4a":"w4","5a":"w5","5b":"w2","6b":"w1"}
tydzien_wto= {"3b":"w2","4a":"w3","5a":"w4","5b":"w1","6b":"w5"}
tydzien_sro= {"3b":"w5","4a":"w2","5a":"w1","5b":"w4","6b":"w3"}
tydzien_czw= {"3b":"w1","4a":"w5","5a":"w2","5b":"w3","6b":"w4"}
tydzien_ptk= {"3b":"w4","4a":"w1","5a":"w3","5b":"w5","6b":"w2"}
