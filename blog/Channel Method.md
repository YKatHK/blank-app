2024.8.17
##### Channel Model
![[IBM_Channel_BrianMillard_p204.JPG]]

1st Cap and Floor: C and F, MidLine: M
2nd Cap and Floor: c and f, MidLine: m
##### Estimate implied ROE and C/B, F/B
assume between C and F, $$ E[\frac{\Delta(\frac{P}{B})_{t}}{(\frac{P}{B})_{t}}] \longrightarrow 0 $$then for a long term, get the implied ROE
$$ E(R)_{t} = E(\frac{\Delta P_{t}}{P_{t}}) \longrightarrow E(ROE)_{t} = E(\frac{\Delta M_{t}}{M_{t}}) $$
apply the latest B value to estimate C/B and F/B
$$ B_{t} = (1+E(ROE)_{t}) \cdot B_{t-1} $$
$$ (\frac{C}{B})_{t} = \frac{C_{t}}{B_{t}} $$
$$ (\frac{F}{B})_{t} = \frac{F_{t}}{B_{t}} $$
##### Forecase the single asset
in a long term view, asset price as
$$f(P)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(P-\mu)^{2}}{2 \sigma^{2}}}$$
$$\mu = E(R) = E(\frac{\Delta M}{M}) $$
$$ \sigma = \sigma(R) = \frac{C-F}{M} \div n$$
n value would infer the probability of price with C and F
![[3-Sigma.png]]
in Pool, if E(ROE) > 0, means E(R) > 0 and M in a uptrend
if you have a different view on E(ROE), you might get your alpha
in channel chart, M <- E(ROE), C <- P/B = Cap/B, F <- P/B = Floor/B
##### Tactic Model
$$ \frac{\Delta(\frac{P}{B})_{t}}{(\frac{P}{B})_{t}} = f(\frac{\Delta m_{t}}{m_{t}}) + N(0,\sigma) $$
$$ E[\frac{\Delta(\frac{P}{B})_{t}}{(\frac{P}{B})_{t}}] = E[f(\frac{\Delta m_{t}}{m_{t}})] $$
$$ \sigma = \frac{c-f}{m} \div n $$
import cycle function for m
$$ f(\frac{\Delta m_{t}}{m_{t}}) = cycle(\frac{\Delta m_{t}}{m_{t}}) $$
apply the cylce function to estimate top and bottom at next T, then infer E(R) at T, ultimately select best one or ones
##### Allocate multi assets (Portfolio)
for asset price P1 and P2, forecast m1 and m2 (remark as fm1 and fm2)
to estimate correlation, select t0 and unitify + detrend, then calculate Cov(R1,R2)
###### Process
```
hierarchical clustering classifies assets based on historical m, 
select uptrend's clusters
make decisions on sell, hold and buy, based on fm, fc, ff and T
```
##### When and what if the forecast is wrong, or cap/floor is broken

```python
from langchain_ollama import OllamaLLM, ChatOllama

model = OllamaLLM(model="llama3.1:latest")
response = model.invoke("Come up with 10 names for a song about parrots")
print(response)
```