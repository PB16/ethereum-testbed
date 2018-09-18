%%
k = 100;
m = 100;
firstPart = factorial(k)/(factorial(m)*factorial(k-m));
stored = 0;
final = [];
x = [];
for n = 101:2000
    x = [x n];
    stored = 0;
    for i = 0:100
        secondPart = ((-1)^i)*((factorial(m)/(factorial(i)*factorial(m-i)))*((m-i)/k)^n);
        stored = stored + secondPart;
    end
    result = firstPart * stored;
    final = [final result]; 
end
plot(x, final)

%%
n = 1024;
m = 100;
stored = 0;
final = [];
x = [];
line = [];
for k = 0:10000
    x = [x k];
    line = [line n];
    result = n*(1-((n-1)/n)^k);
    final = [final result]; 
end
hold on
plot(x, final, 'b')
plot(x,line, 'r')
xlabel('values drawn')
ylabel('Expected number of unique values')
hold off
