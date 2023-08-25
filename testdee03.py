#รับค่า/ป้อนทางเเป้นพิมพ์ ใช้ฟังก์ชั่น input() โดยสิ่งที่ป้อนปั้งหมดถือเป็น string

#ตัวเเปร variable เป็น identifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรเเกรม ข้อมูลที่เก็บจะอยู่ใน RAM 
#identifier คือ ฃื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนฃื่อ : ')
std_name = input('ป้อนรหัสนักศึกษา : ')
std_yearborn = input('ป้อนปีเกิด : ')
print('...........................')
print(f'ยินดีต้อนรับ {std_id} ชื่อ {std_name}')
#ต้องเเปลง String เป็น number เป็น number -> int(), float()
std_age = 2023 - int(std_yearborn)
print(f'คุณเกิดปี {std_yearborn} อายุ {std_age}')
print('...........................')
print("ยินดีต้อนรับ",std_id,"ชื่อ",std_name)
print('คุณเกิดปี',std_yearborn,"อายุ",std_age)
print('...........................')
print('ยินดีต้อนรับ '+str(std_id)+" ชื่อ "+str(std_name))
print('คุณเกิดปี '+std_yearborn+" อายุ "+str(std_age))
print('...........................')
print('ยินดีต้อนรับ {0} ชื่อ {1}'.format(std_id,std_name))
print('คุณเกิดปี {0} อายุ {1}'.format(std_yearborn,std_age))
print('...........................')
print("ยินดีต้อนรับ %s ชื่อ %s "%(std_id,std_name))
print("คุณเกิดปี %s อายุ %s "%(std_yearborn,std_age))