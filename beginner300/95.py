'''
095 딕셔너리 keys() 메서드
다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
'''

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys()) # 순회가능한 키들을 보여주는 dict_keys() 를 반환한다. 아주 큰 딕셔너리에 유용하다.
# 실제 리스트에 쓰고 싶다면 list() 를 호출해서 dict_keys 객체를 리스트로 변환 가능
print(ice)