# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define l = Character('Elizabeth', color="#EC0033", image='lize')
define m = Character('Mike', color='#4671D5', image='mike')
define w = Character('Waiter', color='#4D6C3B', image='waiter')
define n = Character('Noname', color='#BF6B30', image='noname')
define g1 = Character('Woman', color='#34C6CD')
define m1 = Character('Man', color='#2F3584')

default flowers = False # не приняла цветы от М

default about_set = set()
default about_women_set = set()

init:
    $ left_2 = Position(xalign=0.2, yalign=1.0)
    $ right_2 = Position(xalign=0.8, yalign=1.0)

# Игра начинается здесь:
label start:
    play music 'birds_song.mp3' fadeout 1

    scene bg room

    'Утро. За окном солнечная погода. 21 градус по Цельсию.'

    show lize school surprised with dissolve

    l '{color=#EC0033}...{/color}'

    play sound 'idea.ogg'
    show lize school embarrassed with vpunch

    l '{color=#EC0033}Вот чёрт, я опаздываю!{/color}'

    hide lize
    with dissolve
    with vpunch

    show lize school smile with dissolve

    l '{color=#EC0033}..{/color}'
    show lize school surprised
    play sound 'idea.ogg'
    extend '{color=#FF4040}!{/color}'

    show lize school embarrassed2
    'Эту прелесную девушку зовут Элиза, и сегодня у неё свидание с парнем, которого она никогда не видела.'
    l school smile '{color=#EC0033}Вообще никогда. {w}Мы познакомились{/color} {color=#FF4040}несколько месяцев назад{/color} {color=#EC0033}в одном приложении.{/color}'

    'Не перебивай рассказчика. Так вот, {w}п'

    show lize school surprised
    play sound 'vibration.ogg'
    '{cps=0}Дзынь-дзынь-дзынь. {w}{cps=20}Получено 1 новое сообщение.'
    play sound 'idea.ogg'
    l '{color=#FF4040}!{/color}'

    'Лёгок на помине. И что же ты сделаешь, {color=#FF4040}Элли?{/color}'

    menu:
        '{cps=0}Получено 1 новое сообщение.'

        'Ответить':
            jump answer

        'Проигнорировать':
            jump ignor

    return

label answer:
    'Элли решила ответить на сообщение.'

    'mi_10_ke_8: {color=#14D100}Доброе утро! Всё в силе?{/color}'

    play sound 'phone_typing.mp3'
    show lize school embarrassed2
    l '{color=#14D100}Доброе! {w}Да ^_^{/color}'
    stop sound

    play sound 'vibration.ogg'
    'mi_10_ke_8: {color=#14D100}Буду ждать <3{/color}'
    stop sound

    l school smile '{color=#EC0033}Пора идти!{/color}'

    hide lize school surprised with moveoutright

    'И отправилась она на поиски своего счастья или не за этим ходят на свидания?'

    scene bg street with fade

    play music 'street.mp3' fadeout 1

    '''
    День. 24 градуса по Цельсию.

    Звуки мягко доносились из разных мест: машины проезжали, люди куда-то спешили, птицы продолжали свою песнь.

    Медленно солнце прогревало остывший за ночь мир.

    Наша Элиза шла по улице, улыбаясь встречным людям, слушала запахи из начинающих работу пекарен, и не могла не нарадоваться новым днём.
    '''

    show lize school smile with moveinright

    l '{color=#EC0033}«По-моему, это место должно быть где-то рядом.»{/color}'

    hide lize

    'Элиза оглянулась по сторонам, ища какие-то ориентиры, а может знаки свыше, но в нашей реальности «знак» подаёт только пролетающая птичка.'

    show lize school embarrassed with_
    with vpunch

    l '{color=#EC0033}Ой!{/color}'
    show lize school sad with_
    extend ' {color=#EC0033}Чёрт, вот неповезло.{/color}'

    'Девушка постаралась аккуратно оттереть пятно, но выходило паршиво.'

    l '{color=#EC0033}Ух{/color}'

    l school embarrassed with_ '{color=#EC0033}Надеюсь, хоть к деньгам.{/color}'
    hide lize with fade

    'И она зашла в нужное кафе, стараясь сделать вид, что пятно на воротнике было задумано.'

    scene bg cafe with fade
    play music 'classic in cafe.mp3' fadeout 1

    show lize school smile with_

    l school embarrassed with_ '{color=#EC0033}«Хм, никого похожего я пока не вижу.»{/color}'
    l '{color=#EC0033}«Может, проблемы возникли.»{/color}'
    hide lize

    'В связи с тем, что кавалер оказался ещё больше непунктуальным, чем героиня, та решила занять угловой столик и подождать.'

    'К ней подошёл официант.'

    show waiter with dissolve

    w '{color=#4D6C3B}Добрый день. Вы будете одна?{/color}'
    hide waiter

    play sound 'idea.ogg'
    show lize school surprised with_

    l '{color=#EC0033}Здравствуйте!'
    show lize school embarrassed2 with_
    extend ' Я жду молодого человека.'

    'Девушка смущенно улыбнулась официанту.'
    hide lize

    show waiter

    w '{color=#4D6C3B}Поняла Вас. Тогда я принесу ещё одно меню.'

    hide waiter
    with fade

    '''Прошло около семи минут. Элиза уже успела оттереть пятно (не без помощи официанта) и скучающе смотрела на сад и других посетителей.

    Вот птица села на ветку стоящего неподалеку от столика дерева.

    Приятная на вид дама изящными пальчиками взялась за ножку небольшой кружки, из которой пила чай.{w}
    А её собеседница слегка надкусила печенье, что принес официант в виде {color=#FF9700}комплемента{/color}.
    '''

    show lize school upset
    l '{color=#EC0033}Ох...'

    'Судьба не спешит появляться. Зря спешили, но это уже какое-то полнейшее неуважение!'

    menu:
        'Что будешь делать?'

        'Быть упёртой':
            jump wait

        'Забить и уйти':
            jump no_wait

    return

label ignor:

    'Сообщение осталось проигнорированным.'

    centered '{size=+20}{color=#29467F}{b}ОДИНОКАЯ КОНЦОВКА'

    return

label no_wait:

    'Элиза решает уйти, недождавшись парня.'

    hide lize
    with fade

    'Спустя ещё некоторое время.'

    show mike norm with dissolve

    m '{color=#4671D5}...'

    play music 'street.mp3' fadeout 1
    scene bg street no_wait
    with fade

    show lize school upset

    '''Девушка была расстроена и зла, что потратила своё время на бесполезное занятие.
    Поэтому она шла, не обращая ни на что внимания, в направлении дома, желая вернуться к компьютеру и домашнему уюту.
    '''

    show lize school surprised
    play sound 'idea.ogg'
    'Но вдруг на её пути кто-то появляется. {w}Она поднимает голову...'

    hide lize

    show noname
    play sound 'idea.ogg'

    n '{color=#BF6B30}Добрый день. Не разрешите порадовать Вас такой {color=#FF4040}прекраснейшей{/color} компанией, как моя?'

    hide noname with fade

    '''От отчаяния (или последней надежды?) Элли согласилась.

    Парень оказался богатым, статным, любезным, целеустремлённым, но холодным и эгоцентричным.

    Спустя год они сыграли пышную свадьбу.

    Спустя ещё пару лет родился ребёнок{w}, однако Элиза не была по-настоящему счастлива и умерла в глубокой старости со слезами сожаления.

    '''

    centered '{size=+20}{color=#000000}{b}БОГАТАЯ, НО НЕСЧАСТЛИВАЯ КОНЦОВКА'

    return

label wait:

    'Элиза решила ещё подождать.{w} Какая упёртая!'
    with fade

    play sound 'idea.ogg'
    show lize school surprised
    'Девушка заметила в саду кафе спорящих о чем-то девушку и парня. {w}Делали они это не очень громко, но достаточно было прислушаться, чтобы разобрать слова.'

    hide lize

    with vpunch
    m1 '{color=#2F3584}Мне кажется, что мы слишком разные.'

    with vpunch
    g1 '{color=#34C6CD}То, что я пытаюсь обсудить все недомолвки и проблемы, которые у нас возникают, говорит лишь о том, что я {color=#FF4040}дорожу этими отношениями{/color}.'

    with vpunch
    m1 '{color=#2F3584}У нас разные взгляды на жизнь, привычки, принципы. Мы для различного живём!'

    with vpunch
    g1 '{color=#34C6CD}Взаимоотношения строятся на разногласиях. {w}А отношения - на принятии этих разногласий, милый.'

    play sound 'idea.ogg'
    show mike fl with dissolve

    m '{color=#4671D5}З-здравствуй!'

    'Опоздавший выглядел запыхавшимся и смущенным. {w}В руках он держал букет чуть помятых роз (видимо, те были не готовы к такому краш-тесту).'

    hide mike with fade

    show lize school surprised at left_2
    show mike fl at right_2

    show lize school upset at left_2

    l '{color=#EC0033}Привет. {w}Ты очень сильно опоздал.'

    'Девушка выглядела раздраженной. {w}Ещё бы! Она любила пунктуальность, хоть и сама иногда ей не страдала.'

    m '{color=#4671D5}Прошу меня простить!'
    pause 3.0

    play sound 'idea.ogg'
    show lize school surprised at left_2
    extend ' {color=#4671D5}Э-это тебе...'

    'Он протянул букет замечательно пахнущих цветов Элизе.'

    menu:
        'Принять?'

        'Да':
            'Элли взяла вкусно пахнущий букет, и в этот момент появился официант с заготовленной вазой с водой.'

            $ flowers = True

        'Нет':
            show lize school upset at left_2

            'Элиза нахмурилась. {w}Но цветы взяла.'

            show mike norm at right_2

            l '{color=#EC0033}Спасибо, но мне неинтересны цветы, и я в принципе не вижу смысла в букетах, которые завянут через пару дней. {w}Я лучше подарю их кому-то другому.'

            hide lize with fade

            'Элиза подошла к столику с дамами, за которыми только недавно наблюдала, и {color=#FF4040}миленько{/color} преподнесла им букет.'
            show lize school smile at left_2 with dissolve
            extend ' {w}Затем вернулась.'

            'Майк выглядит раздосадованным.'

    hide mike with fade
    hide lize with fade

    'Наконец, они уселись за столик'

    if flowers:
        show mike shy at right_2
        m '{color=#4671D5}Я очень рад, что ты взяла цветы. {w}С моей стороны было неосмотрительно покупать их тебе, у тебя могла быть на них аллергия, но хорошо, что это не так.'
        m '{color=#4671D5}По правде говоря, из-за них я и опоздал. {w}Не мог определиться с выбором, а потом чуть на красный не пошёл.'

        play sound 'idea.ogg'
        show lize school surprised at left_2
        l '{color=#EC0033}Ты чуть не попал под машину? {w}Какой ужас! На следующем свидании, пожалуйста, не нужно цветов. {w}Приди просто целым.'

        m norm '{color=#4671D5}«С-следующем!»'

    'Спустя некоторое время подошёл официант и взял заказ.'

    hide lize
    hide mike

    with fade

    show lize school embarrassed2

    l '{color=#EC0033}.{cps=1}.{cps=1}.'
    hide lize

    show mike shy

    m '{color=#4671D5}.{cps=1}.{cps=1}.'

    show mike shy at right_2 with moveinright
    show lize school embarrassed2 at left_2 with moveinleft

    '.{cps=1}.{cps=1}.'

    play sound 'idea.ogg'
    'И ДОЛГО ВЫ БУДЕТЕ МОЛЧАТЬ, ВЛЮ{color=#FF4040}БЛИН{/color}ЧКИ?'

    'Ладно, поменяем настрой!'
    play music 'romantic_music.mp3' fadeout 1
    show lize school surprised at left_2
    extend ' А точнее музыку!!! {w}Эх, молодость...'

    m talk '{color=#4671D5}... {w}Думаю, что пора представиться полноценно. {w}Меня зовут Майк, мы общались с тобой в Интернете пару месяцев.'

    show mike norm at right_2

    l smile '{color=#EC0033}Приятно познакомиться! {w}Моё имя Элиза. Расскажешь о себе что-нибудь?'

    m talk '{color=#4671D5}Конечно! Что ты хочешь узнать?'

    menu choice: # выбор с исчезающими полями

        set about_set

        'Что ты хочешь узнать?'

        'О тебе':
            jump you

        'О твоих увлечениях':
            jump hobby

        'О твоих взглядах на жизнь':
            jump life

        'Больше ничего не спрашивать':
            pass

    m talk '{color=#4671D5}Можешь рассказать что-то и о себе?'

    menu choice2:

        set about_women_set

        'О чём ты хочешь рассказать?'

        'О себе':
            jump about_lize

        'Об увлечениях':
            jump hobby_lize

        'Больше ничего не рассказывать':
            pass

    'Ещё чуть-чуть смущаясь и четырхаясь, они поговорили про обстановку вокруг и погоду на ближайшие дни.'

    'Время выносить {color=#FF4040}вердикт{/color}!'

    menu:
        'Продолжить общение?'

        'Да, остаться':
            jump stay

        'Нет, уйти':
            jump no_wait_2

    return


label you:

    m shy '{color=#4671D5}Обо мне отзывались, как о добром, любезном, стеснительном парне. Однако мне тяжело говорить о своих чувствах. {w}Но я думаю, что могу поддержать в трудной ситуации, развеселить, ещё я {color=#FF4040}анекдоты{/color} знаю.'

    l '{color=#EC0033}Какой например?'

    m talk '{color=#4671D5}.{cps=1}.{cps=1}.'
    m '{color=#4671D5}Совокупление - процесс покупки совы.'

    show lize school surprised

    'ХАХ! А мне понравилось. Парень не потерян для общества!'

    show mike norm
    play sound 'drums.mp3'

    jump choice

label hobby:

    m talk '{color=#4671D5}Недавно я смог устроиться на подработку в магазине, поэтому свободного времени значительно меньше, но, когда оно всё же есть, я программирую, читаю бизнес-литературу или сплю.'
    m '{color=#4671D5}.{cps=1}.{cps=1}.'

    show lize school embarrassed2

    m shy '{color=#4671D5}Во время стресса люблю готовить, чтобы отвлечься.'

    jump choice

label life:

    m '{color=#4671D5}Сложный вопрос... {w}Я считаю, что для хорошей жизни у человека должен быть любимый человек, и ты должен быть трудолюбивым.'

    l school embarrassed '{color=#EC0033}Для тебя работа - это самое главное?'

    m '{color=#4671D5}Она является весомой частью, но не самой главной для меня. Вообще, любимый человек и работа равны для меня.'

    jump choice

label about_lize:

    l smile '{color=#EC0033}Как я уже говорила, я учусь в 12 классе. Есть парочка друзей в школе и за пределами. Меня называют милой и приятной девушкой'
    show lize school embarrassed2
    extend ', но я пугливая и вспыльчивая временами.'

    l smile '{color=#EC0033}Люблю больше кошек, чем собак ^^'
    show lize school embarrassed2
    play sound 'idea.ogg'
    extend ' Кстати, а ты?'

    m talk '{color=#4671D5}Короткие видео с котиками - моя слабость (^ω^)'
    show mike norm

    jump choice2

label hobby_lize:

    l '{color=#EC0033}Я люблю играть в теннис, а ещё мне нравится вышивать время от времени.'

    m talk '{color=#4671D5}Что уже вышивала?'
    show mike norm

    l embarrassed2 '{color=#EC0033}Небольшие игрушки, шарф и плед ^v^'

    m talk '{color=#4671D5}Это очень круто!'

    l smile '{color=#EC0033}Спасибо!'

    jump choice2


label stay:

    play music 'classic in cafe.mp3' fadeout 1

    show mike norm

    'Элли понравился парень и его ответы.'

    'Майк в свою очередь слушал с улыбкой очень внимательно, иногда задавая уточняющие вопросы.'

    with fade

    show lize school embarrassed2
    show mike talk

    'Так они просидели еще час уже более раскрепощённо. {w}{color=#FF4040}Голубки{/color} делились историями из жизни, парень травил анекдоты (ну, некоторые из них были неплохи, признаю), девушка веселилась.'

    show lize school smile
    show mike norm

    hide lize
    hide mike

    with fade

    play sound 'idea.ogg'
    'Внезапно подошёл официант.'

    show waiter with dissolve

    w 'Прошу прощения, что отвлекаю. {w}В нашем кафе начались часы, когда посетители могут выбрать музыкальное сопровождение в заведении. Скажите, есть ли у вас какая-то любимая композиция?'

    hide waiter

    'Они переглянулись.'

    show mike talk
    m '{color=#4671D5}Выбирай ты, Элиза.'

    hide mike
    show lize school surprised

    'Какую музыку поставить?'

    menu:
        '{cps=0}Какую музыку поставить?'

        'Ed Sheeran - Perfect':
            play music 'Ed Sheeran - Perfect.mp3' fadeout 1

        'Tom Odell - Another Love':
            play music 'Tom Odell - Another Love.mp3' fadeout 1

        'Billie Eilish f Khalid - Lovely':
            play music 'Billie Eilish f Khalid - Lovely.mp3' fadeout 1

    hide lize
    show mike shy

    m '{color=#4671D5}Моя любимая композиция.'

    hide mike

    'Залы и сад наполнились прекрасной музыкой.'

    'Люди, сидевшие одни, отвлеклись от своих занятий, начали оглядываться. Кто спорил - понизили тон или вовсе прекратили. Кто не мог отвлечься - просто заулыбался.'

    show mike norm with dissolve
    play sound 'idea.ogg'

    m '{color=#4671D5}...'

    pause 2.0

    m shy '{color=#4671D5}Н-не хочешь потанцевать вместе?'

    hide mike with dissolve
    show lize school surprised with dissolve

    l '{color=#EC0033}!'

    l school embarrassed2 '{color=#EC0033}Я непротив.'
    hide lize

    '''
    Музыка текла по помещению. {w}Некоторые пары повставали со своих мест и, смеясь или улыбаясь друг другу, медленно закружились в центре.

    Наша же {color=#FF4040}парочка{/color} не стремилась в самый центр - они остались недалеко от своего столика, но так, чтобы случайно его не задеть (оба не славились великими танцорами).

    {b}И всё то время, что они медленно танцевали, они осознавали, как им чертовски приятно находиться в компании друг друга. {w}Чувствовали, что в будущем сложности будут, но они смогут с ними справиться.

    {b}Человек напротив сможет поддержать, сберечь и развеселить.

    {b}Так ещё два человека нашли друг друга.

    '''

    centered '{size=+20}{color=#7A207D}{b}ИСТИННАЯ КОНЦОВКА'

    return

label no_wait_2:

    'Элиза решает уйти. Извинившись и попрощавшись, она вышла из кафе.'

    hide lize
    with fade

    play music 'street.mp3' fadeout 1
    scene bg street no_wait
    with fade

    show lize school sad

    '''Девушка была расстроена, что парень не оправдал её ожиданий, но, возможно, она {color=#FF4040}поторопилась{/color} с выбором?

    В любом случае она шла, не обращая ни на что внимания, в направлении дома, желая вернуться к компьютеру и домашнему уюту.
    '''

    show lize school surprised
    play sound 'idea.ogg'
    'Но вдруг на её пути кто-то появляется. {w}Она поднимает голову...'

    hide lize

    show noname
    play sound 'idea.ogg'

    n '{color=#BF6B30}Добрый день. Не разрешите порадовать Вас такой {color=#FF4040}прекраснейшей{/color} компанией, как моя?'

    hide noname with fade

    '''От отчаяния (или последней надежды?) Элли согласилась.

    Парень оказался богатым, статным, любезным, целеустремлённым, но холодным и эгоцентричным.

    Спустя год они сыграли пышную свадьбу.

    Спустя ещё пару лет родился ребёнок{w}, однако Элиза не была по-настоящему счастлива и умерла в глубокой старости со слезой сожаления.

    '''

    centered '{size=+20}{color=#000000}{b}НЕСЧАСТЛИВАЯ КОНЦОВКА'

    return

