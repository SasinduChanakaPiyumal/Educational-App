score = input("Enter Score: ")
try:
    score = float(score)
  #  if score > 0 ||  score < 10
except:
    print("Enter score in number format")
    quit()
if score < 0.0 or score > 1.0 :
    print('The score should be between 0.0 and 1.0')
    quit()
elif score >= 0.9 :
    print ('A')
elif score >= 0.8 :
    print ('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
else:
    print('F')




    