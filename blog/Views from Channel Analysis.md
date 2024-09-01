2024.8.17
##### Asset Pricing
$$P_{t} = Trend_{t} + Cycle_{t} + Fluctuate_{t}$$
from PB.ROE valuation frame: 
$$\begin{matrix}  
  E(R)_{t} & = & E(\frac{\Delta P_{t}}{P_{t}}) & = & E(ROE)_{t} & + & E(\frac{\Delta(\frac{P}{B})_{t}}{(\frac{P}{B})_{t}})\\
  & & & & \downarrow & & \downarrow \\
  & & & & ^{Business}_{Trend} & & ^{Cycle+}_{Fluctuate}
\end{matrix}$$
##### Channel Model
![[IBM_Channel_BrianMillard_p204.JPG]]
where: 
```
1st Cap and Floor: C and F; 1st MidLine: M = Trend
2nd Cap and Floor: c and f; 2nd MidLine: m = Cycle
```
For the long term,
$$ Trend_{t} \longleftarrow E(R)_{t} = E(ROE)_{t} = E(\frac{\Delta P_{t}}{P_{t}}) \longrightarrow E(\frac{\Delta M_{t}}{M_{t}}) $$
And for cycle,
$$ Cycle_{t} = E(\frac{\Delta m_{t}}{m_{t}}) $$
And for fluctuate,
$$ N(0,\sigma) \longrightarrow \sigma = \frac{c-f}{m} \div n$$
n value would infer the probability of price with c and f, according to below rules
![[3-Sigma.png]]
