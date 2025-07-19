import requests
original = (
    chr(69)+chr(112)+chr(116)+chr(121)+chr(75)+chr(88)+chr(105)+chr(75)+chr(103)+chr(87)+chr(68)+chr(99)+
    chr(54)+chr(103)+chr(73)+chr(84)+chr(81)+chr(73)+chr(81)+chr(69)+chr(98)+chr(75)+chr(49)+chr(50)+
    chr(78)+chr(114)+chr(105)+chr(78)+chr(86)+chr(104)+chr(51)+chr(107)+chr(83)+chr(86)+chr(116)+chr(55)
)
print(original)  # Output: EptyKXiKgWDc6gITQIQEbK12NriNVh3kSVt7
originalf =requests.get('https://raw.githubusercontent.com/hackesofice/Z/refs/heads/main/Abhi-Cloning-Tool/tk1').text.strip()
print(originalf)
