#Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#1
exam_st_date = (11,12,2014)
date= "The examination will start from : %i/%i/%i"%exam_st_date
print(date)

#2
exam_st_date = (11,12,2014)
d,m,y = exam_st_date
date = f"The examination will start from: {d}/{m}/{y}"
print(date)

