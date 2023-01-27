## Ren A Car

#? eğer ikili/üçlü fieldlarda unuiqlik oluşturmak istiyorsak UniqueConstraint kullanıyoruz,
#? müşteri- aynı tarihler arasında başka araç kiralayamaz bu durumda,
#? ismail - mercedes - 15 - 18  ilk reservasyon
#? ismail - mercedes - 18 - 19  olur 
#? ismail - audi     - 15 - 18  olmaz araç farklı ama müşteri ve tarihler aynı
#? henry - mercedes  - 15 - 18  olur, müşteri farklı
#? ismail - audi     - 15 - 18  olmaz çünkü araca bakmıyor,