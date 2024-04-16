%{
In this script we calibrate the pressure sensor MPXV7002DP KKW822A.

Data: (air in tube)
# - h(mm)
7 - 0 - 11.8
8 - 2 - 11.6
9 - 4 - 11.4
10 - 6 - 11.2
11 - 8 - 11.0
12 - 10 - 10.8
13 - 12 - 10.6
14 - 14 - 10.4
15 - 16 - 10.2
16 - 18 - 10.0
17 - 20 - 9.8
18 - 22 - 9.6
19 - 24 - 9.4
20 - 26 - 9.2
21 - 28 - 9.0
22 - 30 - 8.8
23 - 32 - 8.6
24 - 34 - 8.4
25 - 36 - 8.2
26 - 38 - 8.0
27 - 40 - 7.8
28 - 42 - 7.6
29 - 44 - 7.4
30 - 46 - 7.2
31 - 48 - 7.0
32 - 50 - 6.8
33 - 52 - 6.6
34 - 54 - 6.4
35 - 56 - 6.2
36 - 58 - 6.0
37 - 60 - 5.8
%}

%%
for i = 7: 37
    pressure(i).data = eval(sprintf("Dev3_%d", i));
end

%%
for i = 1: 31
    pressure_air(i).data = pressure(i+6).data;
end

%% volt
for i = 1: 31
    volt(i) = mean(pressure_air(i).data.that)
end

%% pressure
h = 0: 2: 60
pres = 997 * 9.8 * h * 1e-3

%%
scatter(pres, volt, "DisplayName", "calibration data")
xlabel("Differential pressure, P-P_0 (Pa)")
ylabel("voltage (V)")

%% Fit with a linear line
f = fit(pres', volt', "poly1");

%%
hold on;
plot(pres, f.p1*pres+f.p2, "DisplayName", "linear fit");
hold off;
legend