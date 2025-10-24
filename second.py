score = input("Enter Score: ")
try:
    score = float(score)
  #  if score > 0 ||  score < 10
except ValueError:
    print("Enter score in number format")
    quit()
if score < 0 :
    print ('The score should between o & 10')
elif score > 10 :
    print ('The score should between o & 10')
else:
    if score >= 0.9 :
        print ('A')
    elif score >= 0.8 :
        print ('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    elif score < 0.6:
        print('F')




    
