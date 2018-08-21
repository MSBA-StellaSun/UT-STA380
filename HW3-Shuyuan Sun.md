

```python
from pandas import Series, DataFrame
import pandas as pd
%pylab inline
```

    Populating the interactive namespace from numpy and matplotlib
    

[Q1 10 points] Read in data


```python
gold=pd.read_csv('gold.txt',
                 sep='\t',
                 header=None,
                 names=['url', 'category'])
labels=pd.read_csv('labels.txt',
                 sep='\t',
                 header=None,
                 names=['turk','url', 'category'])
print labels[:5]
print len(labels)
print gold[:5]
print len(gold)
```

                 turk            url category
    0  A1OT3A29R9N1DG  http://000.cc        P
    1  A1PXXEOGQ76RNJ  http://000.cc        G
    2  A1PXXEOGQ76RNJ  http://000.cc        G
    3  A21US576U8SCO4  http://000.cc        G
    4  A2LGX47NN7C5D3  http://000.cc        G
    92721
                                          url category
    0               http://0800-horoscope.com        G
    1                      http://18games.net        X
    2                    http://1pixelout.net        G
    3  http://1porno.com/004/teens/index.html        X
    4   http://1stpussy.com/005/16/index.html        X
    1517
    

[Q2 10 points] Split into two DataFrames


```python
labels_on=labels.merge(gold,
                           left_on='url',
                           right_on='url',
                           suffixes=('','_g'))
labels_on_gold=labels_on.drop('category_g',1)
print labels_on_gold[:5],
print len(labels_on_gold)
```

                 turk                        url category
    0  A1253FXHCZ9CWM  http://0800-horoscope.com        G
    1  A153PKAL7OAY36  http://0800-horoscope.com        G
    2  A1FV9SAPL5C6KY  http://0800-horoscope.com        G
    3  A1JTOT0DWM6QGL  http://0800-horoscope.com        G
    4  A1PXXEOGQ76RNJ  http://0800-horoscope.com        G 3324
    


```python
labels_unknown=labels[~labels.url.isin(labels_on_gold.url)]
print labels_unknown[:5]
print len(labels_unknown)
```

                 turk            url category
    0  A1OT3A29R9N1DG  http://000.cc        P
    1  A1PXXEOGQ76RNJ  http://000.cc        G
    2  A1PXXEOGQ76RNJ  http://000.cc        G
    3  A21US576U8SCO4  http://000.cc        G
    4  A2LGX47NN7C5D3  http://000.cc        G
    89397
    

[Q3 10 points] Compute accuracies of turks


```python
labels_on['accuracy']=labels_on['category']==labels_on['category_g']
rater_goodness=labels_on.groupby('turk')['accuracy'].agg(['count','mean'])
rater_goodness.columns=['no_of_ratings','acc_of_ratings']
print rater_goodness[:10]
print len(rater_goodness)
```

                    no_of_ratings  acc_of_ratings
    turk                                         
    A112DVP1KG4QZU              1        1.000000
    A1253FXHCZ9CWM             29        0.517241
    A12CY1Q7XKJJDE              1        1.000000
    A12RE8G66WTO8B             20        0.750000
    A12Y1GTGIQDGRA              3        0.333333
    A13CEW9JGDWGX1              1        1.000000
    A13OE9GBRJ0S2U              4        0.750000
    A14IQ4GLNWNPOJ              1        1.000000
    A153PKAL7OAY36            148        0.722973
    A1554ZM0CLKSG5              1        1.000000
    269
    

[Q4 10 points] Odds ratios


```python
rater_goodness['odds']=rater_goodness['acc_of_ratings']/(1.001-rater_goodness['acc_of_ratings'])
print rater_goodness[:10]
print len(rater_goodness)
```

                    no_of_ratings  acc_of_ratings         odds
    turk                                                      
    A112DVP1KG4QZU              1        1.000000  1000.000000
    A1253FXHCZ9CWM             29        0.517241     1.069214
    A12CY1Q7XKJJDE              1        1.000000  1000.000000
    A12RE8G66WTO8B             20        0.750000     2.988048
    A12Y1GTGIQDGRA              3        0.333333     0.499251
    A13CEW9JGDWGX1              1        1.000000  1000.000000
    A13OE9GBRJ0S2U              4        0.750000     2.988048
    A14IQ4GLNWNPOJ              1        1.000000  1000.000000
    A153PKAL7OAY36            148        0.722973     2.600369
    A1554ZM0CLKSG5              1        1.000000  1000.000000
    269
    

[Q5 10 points] Most accurate turks


```python
at_least_20=rater_goodness[rater_goodness['no_of_ratings']>=20]
at_least_20.sort_values(by='acc_of_ratings',ascending=False)[:10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>no_of_ratings</th>
      <th>acc_of_ratings</th>
      <th>odds</th>
    </tr>
    <tr>
      <th>turk</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A2U0R4X38GUKZE</th>
      <td>20</td>
      <td>0.950000</td>
      <td>18.627451</td>
    </tr>
    <tr>
      <th>A22C0PJUBFJTI0</th>
      <td>36</td>
      <td>0.916667</td>
      <td>10.869565</td>
    </tr>
    <tr>
      <th>A23YQUBXZPKILZ</th>
      <td>24</td>
      <td>0.875000</td>
      <td>6.944444</td>
    </tr>
    <tr>
      <th>ATVALOQVDCMZW</th>
      <td>103</td>
      <td>0.854369</td>
      <td>5.826657</td>
    </tr>
    <tr>
      <th>A1HIXWH4OXT8S4</th>
      <td>40</td>
      <td>0.825000</td>
      <td>4.687500</td>
    </tr>
    <tr>
      <th>A3220HG1O83HQ4</th>
      <td>22</td>
      <td>0.818182</td>
      <td>4.475385</td>
    </tr>
    <tr>
      <th>A32W20KGQXS0LL</th>
      <td>25</td>
      <td>0.800000</td>
      <td>3.980100</td>
    </tr>
    <tr>
      <th>A20PWAB7G3HDHU</th>
      <td>20</td>
      <td>0.800000</td>
      <td>3.980100</td>
    </tr>
    <tr>
      <th>AJSJVK40F5HM6</th>
      <td>28</td>
      <td>0.785714</td>
      <td>3.649635</td>
    </tr>
    <tr>
      <th>A31OCN4MNHUQ6W</th>
      <td>184</td>
      <td>0.777174</td>
      <td>3.472222</td>
    </tr>
  </tbody>
</table>
</div>



[Q6 10 points] Rating counts versus accuracy


```python
import statsmodels.api as sm
from patsy import dmatrices

y, X = dmatrices('acc_of_ratings ~ no_of_ratings', rater_goodness, return_type='dataframe')
result = sm.OLS(y, X).fit()

slope = result.params['no_of_ratings']
intercept = result.params['Intercept']
print 'acc_of_ratings = {:.4f} + {:.4f} * no_of_ratings'.format(intercept, slope)
```

    acc_of_ratings = 0.6431 + 0.0007 * no_of_ratings
    


```python
predicted = rater_goodness['no_of_ratings'] * slope + intercept
regression_predictions = Series(predicted.values,
                                index=rater_goodness['no_of_ratings'])
```


```python
plot(rater_goodness['no_of_ratings'], rater_goodness['acc_of_ratings'], marker='o', color='blue', linestyle='None')
xlabel('no_of_ratings')
ylabel('acc_of_ratings')
title('Rating counts versus accuracy')
regression_predictions.plot(label='Regression', color='red',linewidth=2)
legend(numpoints=1, loc='best')
show()
#There seems only a slight linear relationship between the number of ratings by a turker on gold set URLs and his or her accuracy.
```


![png](output_15_0.png)



```python
rater_goodness['no_of_ratings'].corr(rater_goodness['acc_of_ratings'])
#The correlation coefficient indicates that the number of ratings by a turker on gold set URLs and his or her accuracy is not much correlated.
```




    0.04529238280484695



[Q7 13 points] Overall predicted odds


```python
over_75p=rater_goodness[(rater_goodness['no_of_ratings']>rater_goodness['no_of_ratings'].quantile(0.75))]
```


```python
labels_over_75p=labels_unknown.merge(over_75p,
                                    left_on='turk',
                                    right_on='turk',
                                    suffixes=['_l','_75'])
overall_odds=labels_over_75p.groupby(['url','category'])['odds'].prod()
print overall_odds[:10]
print len(overall_odds)
```

    url                                                       category
    http://0-101.net                                          G            2.155963
    http://000.cc                                             G            1.460583
    http://0000.jp                                            G           14.488244
    http://000relationships.com                               G            5.681060
                                                              P            1.851852
    http://000vitamins.com                                    G            3.784982
    http://000webhost.com                                     G           11.159502
    http://003my.com                                          G            4.912040
    http://007absolutehardcore.com/early_cumshots/index.html  P            3.346522
                                                              R           12.290450
    Name: odds, dtype: float64
    13983
    

[Q8 13 points] Predicted categories


```python
overall_odds_unstack=overall_odds.unstack().fillna(0)
result_75=pd.DataFrame(index=labels_over_75p['url'].drop_duplicates(),columns=['top_category','top_odds'])
overall_odds_unstack['max_odds']=overall_odds_unstack.T.apply(max)
overall_odds_unstack['max_odds_category']=overall_odds_unstack.T.idxmax()
result_75['top_odds']=overall_odds_unstack['max_odds']
result_75['top_category']=overall_odds_unstack['max_odds_category']
print result_75[:10]
print len(result_75)
```

                                top_category   top_odds
    url                                                
    http://000.cc                          G   1.460583
    http://0000.jp                         G  14.488244
    http://000relationships.com            G   5.681060
    http://007swz.cn                       G   1.393883
    http://01768.com                       G   1.393883
    http://0198.cc                         G   2.947446
    http://01house.cn                      G   3.874200
    http://01yyy.com                       G   3.874200
    http://020dna.com                      G   5.054597
    http://020shenghuo.com                 G   1.393883
    10610
    

[Q9 14 points] Predicted categories using more turks


```python
#Q7 for above 25%
over_25p=rater_goodness[(rater_goodness['no_of_ratings']>rater_goodness['no_of_ratings'].quantile(0.25))]

labels_over_25p=labels_unknown.merge(over_25p,
                                    left_on='turk',
                                    right_on='turk',
                                    suffixes=['_l','_25'])
overall_odds_25=labels_over_25p.groupby(['url','category'])['odds'].prod()
print overall_odds_25[:10]
print len(overall_odds_25)
```

    url                          category
    http://0-101.net             G           2.155963e+00
    http://000.cc                G           2.181050e+03
                                 P           9.980040e-01
    http://0000.jp               G           2.877556e+07
    http://000relationships.com  G           0.000000e+00
                                 P           1.851852e+00
                                 R           3.328895e-01
    http://000vitamins.com       G           5.014149e+00
    http://000webhost.com        G           1.113723e+07
    http://003my.com             G           4.912040e+00
    Name: odds, dtype: float64
    16690
    


```python
#Q8 for above 25%
overall_odds25_unstack=overall_odds_25.unstack().fillna(0)
result_25=pd.DataFrame(index=labels_over_25p['url'].drop_duplicates(),columns=['top_category','top_odds'])
result_25['top_odds']=overall_odds25_unstack.T.apply(max)
result_25['top_category']=overall_odds25_unstack.T.idxmax()
print result_25.sort_index()[:10]
print len(result_25)
```

                                                       top_category      top_odds
    url                                                                          
    http://0-101.net                                              G  2.155963e+00
    http://000.cc                                                 G  2.181050e+03
    http://0000.jp                                                G  2.877556e+07
    http://000relationships.com                                   P  1.851852e+00
    http://000vitamins.com                                        G  5.014149e+00
    http://000webhost.com                                         G  1.113723e+07
    http://003my.com                                              G  4.912040e+00
    http://007absolutehardcore.com/early_cumshots/i...            X  5.847515e+02
    http://007swz.cn                                              G  1.391101e+00
    http://01768.com                                              G  1.393883e+00
    10700
    


```python
url_merge=result_75.merge(result_25,
                         left_on='url',
                         right_on='url',
                         suffixes=['_75','_25'])
compare=pd.crosstab(index=url_merge['top_category_75'],columns=url_merge['top_category_25'],values=url_merge['top_category_25'],aggfunc=len)
compare
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>top_category_25</th>
      <th>G</th>
      <th>P</th>
      <th>R</th>
      <th>X</th>
    </tr>
    <tr>
      <th>top_category_75</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>G</th>
      <td>8327</td>
      <td>574</td>
      <td>186</td>
      <td>216</td>
    </tr>
    <tr>
      <th>P</th>
      <td>189</td>
      <td>328</td>
      <td>47</td>
      <td>19</td>
    </tr>
    <tr>
      <th>R</th>
      <td>21</td>
      <td>34</td>
      <td>128</td>
      <td>25</td>
    </tr>
    <tr>
      <th>X</th>
      <td>27</td>
      <td>6</td>
      <td>26</td>
      <td>457</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most error occurs when:
#top_category_75 is G while top_category_25 is P;
#top_category_75 is P while top_category_25 is G;
#top_category_75 is R while top_category_25 is P;
#top_category_75 is X while top_category_25 is G;
#top_category_75 is G while top_category_25 is R;
#top_category_75 is G while top_category_25 is X;
```
