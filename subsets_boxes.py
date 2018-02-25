# This function computes all subsets of a list
def subsets (a, b, lo, d):
  hi = len(a)
  if (lo == hi):
    if b != []:
      if (len(b) == 4):
        for i in range(len(a)):
          if (does_fit(a[i],a[i+1])):
            print(b)
        #d.append(b)
          return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1, d)
    subsets (a, b, lo + 1, d)

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

#def print_sets(d):
#    print(d)

def main():
  a = [[14, 27, 62],[16, 40, 90],[27, 50, 89],[53, 56, 91],[60, 60, 66]]
  #a = [[14, 27, 62], [15, 85, 92], [16, 40, 90], [22, 39, 56], [23, 61, 78], [23, 70, 90], [25, 93, 98], [27, 50, 89], [29, 62, 64], [32, 38, 50], [37, 43, 66], [46, 93, 95], [48, 56, 99], [49, 67, 95], [51, 52, 96], [53, 56, 91], [57, 82, 94], [60, 60, 66], [70, 74, 91], [79, 89, 91]]
  b = []
  d = []
  subsets (a, b, 0, d)


  #for i in range len(b):
  #  for j in range len(i):
  #    for k in range (3):
  #      for m in range (2):
  #        if(does_fit(d[i[j[k]]],d[i[j[k+1]]]))
  #print_sets(d)

main()
