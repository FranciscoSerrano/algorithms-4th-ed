'''
What does the following program print?
'''

'''java
int f = 0;
int g = 1;
for (int i = 0; i <= 15; i++){
    StdOut.println(f);
    f = f + g;
    g = f - g;
}
'''

#python implimentation
f = 0
g = 1
for i in range(16):
    print(f)
    f = f + g
    g = g - f
# > 0110-1-10110...