txt = '''20 22
PSY Coming back (이리 오너라)
Long time no see huh?
오래간만이지 huh?
우리 다시 웃고 울고 지지고 볶고
Let's get loco
Pandemic's over uh
그래 기분이 오져 uh
다시 그분이 오죠 uh
Everybody say
뻑적지근해
걸쩍지근해
시끌벅적거리네
너무 좋아 북적거리네
동서남북 Aye
강남강북 Aye
싹 다 모여 Throw yo hands in the air
I say yeah
Can you feel it?
Can you feel it?
Oh oh woo yeah Oh woo oh
Can you feel it?
Can you feel it?
Oh oh woo yeah Ah
준비하시고 (Go) 쏘세요 (Oh)
That that I like that (Like that)
기분 좋아 Babe (Babe)
흔들어 좌 우 위 아래로 (Sing it)
One two three to the four (Sing it)
That that I like that
That that I like that babe
That that I like that
It's like that that yo
That that I like that
That that I like that babe
That that I like that
It's like that
야 내가 뭐 하는 사람인지 까먹었지?
That that I like that (Like that)
시간이 지나도 변함없이
That that I like that (Like that)
I don't care I don't care that I like that
That that I like that (Like that)
내가 바라보고 바라왔던 사람들아
모두 다 Ready set go
되려 늘어난 맷집 때리던 분이 불편하겠지
너네 바람대로 망할 거라 고사 지낸
사람들을 모아다가 가볍게 때찌
적당히 하라고 Oh oh oh
그냥 닥치고 다 같이 놀아보자고 Oh oh oh
민윤기와 박재상
Can you feel it?
Can you feel it?
Oh oh woo yeah Oh woo oh
Can you feel it?
Can you feel it?
Oh oh woo yeah Ah
준비하시고 (Go) 쏘세요 (Oh)
That that I like that (Like that)
기분 좋아 Babe (Babe)
흔들어 좌 우 위 아래로 (Sing it)
One two three to the four (Sing it)
That that I like that
That that I like that babe
That that I like that
It's like that that yo
That that I like that
That that I like that babe
That that I like that
It's like that that yo
Do what you wanna
Say what you wanna
Do what you wanna (Say what?)
That that I like that babe
Do what you wanna
Say what you wanna
Do what you wanna (Say what?)
That that I like that babe
That that I like that'''

find = input("찾을 단어를 입력하세요: ")
find_cap_word = find.capitalize()

find_word = txt.find(find)+1
find_word2 = txt.find(find_cap_word)+1

print(f"이 노래가사의 {find}는 {txt.count(find)}번 쓰였고,")
print(f"{find_word}번째 처음 등장합니다.")

print(f"이 노래가사의 {find_cap_word}는 {txt.count(find_cap_word)}번 쓰였고,")
print(f"{find_word2}번째 처음 등장합니다.")