TOTAL SALES
=SUM(Daily_Data!D:D)

TODAY SALES
=SUMIFS(Daily_Data!D:D,Daily_Data!A:A,TODAY())

YESTERDAY SALES
=SUMIFS(Daily_Data!D:D,Daily_Data!A:A,TODAY()-1)

BRANCH SALES – Yara New
=SUMIF(Daily_Data!B:B,"Yara New",Daily_Data!D:D)

BRANCH SALES – Yara Shopping
=SUMIF(Daily_Data!B:B,"Yara Shopping",Daily_Data!D:D)

DEPARTMENT SALES (Example Grocery)
=SUMIF(Daily_Data!C:C,"Grocery",Daily_Data!D:D)

CURRENT MONTH SALES
=SUMPRODUCT((MONTH(Daily_Data!A:A)=MONTH(TODAY()))*(YEAR(Daily_Data!A:A)=YEAR(TODAY()))*(Daily_Data!D:D))

LAST MONTH SALES
=SUMPRODUCT((MONTH(Daily_Data!A:A)=MONTH(EOMONTH(TODAY(),-1)))*(YEAR(Daily_Data!A:A)=YEAR(EOMONTH(TODAY(),-1)))*(Daily_Data!D:D))

MONTHLY SALES – Yara New
=SUMPRODUCT((Daily_Data!B:B="Yara New")*(MONTH(Daily_Data!A:A)=MONTH(TODAY()))*(YEAR(Daily_Data!A:A)=YEAR(TODAY()))*(Daily_Data!D:D))

MONTHLY SALES – Yara Shopping
=SUMPRODUCT((Daily_Data!B:B="Yara Shopping")*(MONTH(Daily_Data!A:A)=MONTH(TODAY()))*(YEAR(Daily_Data!A:A)=YEAR(TODAY()))*(Daily_Data!D:D))

DAILY TARGET
=MonthlyTarget/DAY(EOMONTH(TODAY(),0))

ACHIEVEMENT %
=ActualSales/Target*100

GROWTH %
=(CurrentMonth-LastMonth)/LastMonth*100

AVERAGE DAILY SALES
=AVERAGE(Daily_Data!D:D)

HIGHEST SALES
=MAX(Daily_Data!D:D)

LOWEST SALES
=MIN(Daily_Data!D:D)
