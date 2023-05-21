
import play


play.set_backdrop("light blue")




@play.when_program_starts#Функція для початку програми 
def start():
    global player, speech
    text1 = play.new_text(words="г - гладити, з - зіграти, с - спати ", x=0, y=270, font_size=40)
    text2 = play.new_text(words="к - кормити, п- прибрати, пробіл - піти", x=0, y=240, font_size=40)
    player = play.new_image(image="download (2).jpg", x=0, y=0, size=100)
    speech = play.new_text(words="привіт стіч ", x=0, y=-250 )
@play.repeat_forever#повторення завжди(ігровий цикл)
async def do():
    if play.key_is_pressed("г") or play.key_is_pressed("г"):
        player.image = "download.jpg"
        speech.words = "хазяяєн погладь мене "
        await play.timer(2.0)
        player.image = "d7cd5f42-a37e565c7344e21d614a7c7e06b8ba32.jpg"
        speech.words = "ладно давай "
        await play.timer(2.0)
        player.image = "download.jpg"
        speech.words = "ой як преємно "
    if play.key_is_pressed("г") or play.key_is_pressed("з"):
        player.image = "download.png"
        speech.words = "ладно я дрихнути  пішов "
        await play.timer(2.0)

    if play.key_is_pressed("г") or play.key_is_pressed("с"):  
        player.image = "download (4).jpg"
        speech.words = "Goodbye"
        speech.words = "I will think"
        await play.timer(2.0)


play.start_program()#запуск програми






