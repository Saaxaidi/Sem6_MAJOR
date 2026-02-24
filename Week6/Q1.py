MathsMarks =float(input("enter the internal assesmnet score for maths subject : "))
SciencesMarks =float(input("enter the internal assesmnet score for Science subject : "))
EnglishMarks =float(input("enter the internal assesmnet score for English subject : "))

if(MathsMarks >SciencesMarks) and (MathsMarks >EnglishMarks):
    print(MathsMarks, " is the highst marks")
if (SciencesMarks > MathsMarks) and (SciencesMarks >EnglishMarks):
    print(SciencesMarks," is the highest marks ")
if (EnglishMarks > MathsMarks) and (EnglishMarks > SciencesMarks):
    print(EnglishMarks," is the highest marks")
