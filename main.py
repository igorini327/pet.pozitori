
import play


play.set_backdrop("light blue")




@play.when_program_starts#Функція для початку програми 
def start():
    text1 = play.new_text(words="г - гладити, з - зіграти, с - спати ", x=0, y=270, font_size=40)
    text2 = play.new_text(words="к - кормити, п- прибрати, пробіл - піти", x=0, y=240, font_size=40)
    text3 = play.new_image(image="download (2).jpg" , x=0, y=0, size=100)
@play.repeat_forever#повторення завжди(ігровий цикл)
def do():
    pass


play.start_program()#запуск програми






