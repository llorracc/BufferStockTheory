---
title: Theoretical Foundations of Buffer Stock Saving
subject: Economics
short_title: BufferStockTheory
authors:
- name: Christopher D Carroll
- name: Akshay Shanker
keywords:
- Precautionary saving
- buffer stock saving
- marginal propensity to consume
- permanent income hypothesis
- income fluctuation problem
abstract: "This paper builds foundations for rigorous and intuitive understanding of ‘buffer stock’ saving behaviour that can emerge in Bewley (1977)-like economies.\n After describing conditions under which a consumption function exists, the paper articulates stricter ‘Growth Impatience’ conditions sufficient to guarantee the existence of a buffer-stock target --- either at the population level, or for individual consumers.\n Together, these analytical results, along with the included numerical illustrations, constitute a comprehensive toolkit for understanding buffer stock saving."
jel_codes:
- D81
- D91
- E21
links:
  remark: https://econ-ark.org/materials/bufferstocktheory
  html: https://llorracc.github.io/BufferStockTheory/
  pdf: https://github.com/llorracc/BufferStockTheory/blob/master/BufferStockTheory.pdf
  slides: https://github.com/llorracc/BufferStockTheory/blob/master/LaTeX/BufferStockTheory-Slides.pdf
  github: https://github.com/llorracc/BufferStockTheory
  dashboard: https://econ-ark.org/materials/bufferstocktheory
acknowledgements: "The paper’s results [can be automatically reproduced](https://llorracc.github.io/nbreproduce) using the Econ-ARK toolkit by executing the [notebook](https://econ-ark.org/materials/bufferstocktheory); for reference to the toolkit itself see [Acknowledging Econ-ARK](https://econ-ark.org/acknowledging). Thanks to the [Consumer Financial Protection Bureau](https://consumerfinance.gov) for funding the original creation of the Econ-ARK toolkit; and to the [Sloan Foundation](https://sloan.org) for funding Econ-ARK’s [extensive further development](https://sloan.org/grant-detail/8071) that brought it to the point where it could be used for this project. The toolkit can be cited with its digital object identifier, <https://doi.org/10.5281/zenodo.1001067>, as is done in the paper’s own references as [(Christopher D. Carroll, Alexander M. Kaufman,\n Jacqueline L. Kazil, Nathan M. Palmer, and Matthew\n N. White, 2018)](#cite-carroll_et_al-proc-scipy-2018). Thanks to Will Du, James Feigenbaum, Joseph Kaboski, Miles Kimball, Qingyin Ma, Misuzu Otsuka, Damiano Sandri, John Stachurski, David Stern, Adam Szeidl, Alexis Akira Toda, Metin Uyanik, Mateo Velásquez-Giraldo, Weifeng Wu, Jiaxiong Yao, and Xudong Zheng for comments on earlier versions of this paper, John Boyd for help in applying his weighted contraction mapping theorem, Ryoji Hiraguchi for extraordinary mathematical insight that improved the paper greatly, David Zervos for early guidance to the literature, and participants in a seminar at the Johns Hopkins University, a presentation at the 2009 meetings of the Society of Economic Dynamics for their insights, and at a presentation at the Australian National University. Shanker gratefully acknowledges research support from the Australian Research Council (ARC LP190100732) and ARC Centre of Excellence in Population Ageing Research (CE17010005)."
---

(keywords)=

# Introduction 

(sec-intro)=

The precautionary motive to save springs from the fact that extra resources improve a consumer’s ability to buffer spending against shocks.
A consumer who, in the absence of shocks, would be impatient enough to plan to spend down their resources, will (when shocks are present) experience an intensifying precautionary motive as their buffering capacity shrinks.
The result of this competition between impatience and ‘prudence’ [(Kimball, 1990)](#cite-kimball-smallandlarge) has been described, starting with [(Deaton, 1991)](#cite-deatonLiqConstr), as ‘buffer stock saving,’ with a ‘target’ defined[^1] as the point where the precautionary motive to accumulate becomes exactly strong enough to counter the impatience motive to decumulate.

The logic of buffer stock saving underpins key findings in heterogeneous-agent (HA) macroeconomics.
For example, it can explain why, during the Great Recession, middle-class consumers cut spending more than the poor or the rich [(Krueger, Mitman, and Perri, 2016)](#cite-kmpHandbook).
Buffer stock saving also can explain why consumption growth tracks income growth over much of the life cycle,[^2] rather than being determined solely by preferences and interest rates as Irving [(Fisher, 1930)](#cite-fisherInterestTheory) had proposed.

Buffer stock saving models are neither a subset nor a superset of the closely-related class of [(Bewley, 1977)](#cite-bewleyPIH) models (or, more generically, ‘income fluctuation’ problems [(Schectman, 1976)](#cite-schectman-fluctuation); we will use the terms ‘Bewley model’ and ‘income fluctuation problem’ interchangeably).
That is, not all Bewley models with fluctuating income exhibit buffer stock saving, and not all models that exhibit buffer stock saving satisfy the mathematical assumptions that guarantee boundedness of marginal marginal utility imposed by Schectman or Bewley (and inherited by almost all of the subsequent literature through to the recent contributions of [(Ma, Stachurski, and Toda, 2020; Ma, Stachurski, and Toda, 2022a)](#cite-maUnboundedDP)).

The purpose of this paper is to provide a comprehensive statement and explanation of the conditions under which buffer stock saving arises in a class of problems broader in important respects than Bewley models. Specifically, we consider the problem of an agent who is subject to a Friedman-Muth(-Zeldes) income process incorporating permanent shocks to noncapital income [(Friedman, 1957; Muth, 1960; Zeldes, 1989)](#cite-zeldesStochastic) in addition to the transitory shocks traditionally examined in the income fluctuation literature,[^3]
and who does not face an ‘artificial’ borrowing constraint (a constraint that prohibits borrowing even when the loan could certainly be repaid).

In the course of proving our main theoretical results, we define a variety of alternative measures of ‘patience’ – an intuitive term that nonetheless has had multiple interpretations in the literature. Different measures of impatience guarantee two kinds of theoretical results: The existence of a nondegenerate limiting consumption function, and the existence of a buffer stock ‘target’.

#### Patience Requirements for Nondegeneracy 

We will define the ‘limiting’ consumption function as the limit of the sequence of consumption rules constructed by iterating backward from a terminal period $T$, and we will say that this limiting function is ‘nondegenerate’ if it exists, is real-valued, and is strictly positive for every reachable circumstance the consumer could be in.

When an artificial borrowing constraint is imposed and noncapital income is stationary – it is subject to no permanent shocks and exhibits no long-term growth
– our problem coincides with a standard ‘income fluctuation problem.’ But our new proof methods in this paper’s first main contribution, allows us also to solve models where permanent income is unbounded above and below and there is no artificial constraint.

As noted by [(Szeidl, 2013)](#cite-szeidlInvariant), the impatience condition $(\Rfree \DiscFac) < 1$ that is commonly imposed in Bewley models to guarantee existence and stability of the stochastic distributions is in general not necessary nor sufficient for ensuring the existence of a non-degenerate limiting solution.

For instance, in the unconstrained perfect foresight version of our problem, one type of degeneracy arises if permanent income perpetually grows faster than the rate at which it is discounted: With no limiting upper bound to the PDV of future income and no borrowing constraint, there is no upper bound to limiting consumption. Imposition of a ‘Finite Human Wealth’ condition ($\PermGroFac < \Rfree$), where the growth factor of permanent income ($\PermGroFac$) is strictly dominated by the discount factor ($\Rfree$), is required to prevent this. Another type of degeneracy arises if preferences fail the ‘return impatience’ condition: $\APFacRaw/\Rfree < 1$, where $\CRRA$ is the coefficient of relative risk aversion. Without return impatience, the limiting consumption function is zero everywhere. Thus, both of these conditions are necessary for the existence of a nondegenerate limiting consumption function.

Intuition would suggest that, by activating the precautionary saving motive, introduction of the Friedman-Muth stochastic income process might necessitate a stronger degree of impatience to avoid degeneracy. In fact, we show that the required impatience condition is *weaker*, for reasons that follow from the lack of an artificial borrowing constraint and the presence of a ‘natural’ borrowing constraint,[^4] (which has the additional effect of eliminating the need to impose the Finite Human Wealth condition). We further demonstrate that the artificial constraint emerges as the limit, as a certain parameter goes to zero, of the natural constraint. This provides an intuitive conceptual bridge between the two.

In the existing literature going all the way back to [(Fisher, 1930)](#cite-fisherInterestTheory),[^5] time preference ‘$\DiscFac$’ and patience have often been treated as synonymous.

However, we show that, in the presence of nonstationary permanent income, the corresponding generalized mathematical steps yield a [‘finite value of autarky’](#FVAC) condition that incorporates both $\DiscFac$ and characteristics of the income growth process. The fact that the generalized condition involves terms other than $\DiscFac$ undermines the temptation to identify ‘patience’ solely with the pure time preference factor. We therefore propose that henceforth the literature should deprecate use of the term ‘patience’ unadorned with any adjective identifying precisely which *kind* of patience is under consideration.

One such kind of patience is [absolute patience](#APFac), $\APFacRaw$, which is the rate at which the consumer is willing to move consumption forward without any precautionary saving motive (under perfect foresight). Importantly, we show that for a consumer to have a non-degenerate value function in the limit as the planning horizon recedes, [absolute patience](#APFac) cannot exceed *both* the market return factor $\Rfree$ and the expected income growth factor $\PermGroFac.$
(Growth impatience must hold if return impatience fails and vice-versa.)
When both growth impatience and return impatience fail, the limiting consumption function is either $\cFunc=0$ or $\cFunc=\infty$.

#### Patience Requirements and the Existence of Buffer Stock Targets 

Once we have established the existence of a non-degenerate solution, the second (and more important) main result of the paper is to identify conditions under which buffer stock ‘targets’ exist, for individual consumers or in the aggregate.

The appropriate definition of a buffer stock ‘target’ turns out to depend on whether we are interested in the microeconomic behavior of individual consumers, or the aggregate behavior of the entire population of consumers.
The requirement for the existence of an individual target is [‘strong growth impatience,’](#GICMod) ($\Ex[\APFacRaw/\PermGroFacRnd] < 1$) which prevents the ratio of a household’s market resources $(\mLvl)$ to permanent income $(\pLvl)$ (‘normalized market resources’ $\mNrm = \mLvl/\pLvl$) from growing without bound.
Specifically, strong growth impatience guarantees that at some large-enough value $\mNrm = \acute{\mNrm}$ it must be the case that the expectation of next period’s $\mNrm$ is less than this period’s: (if $\mNrm_{t} > \acute{m}$, then $\Ex_{t}[\mNrm_{t+1}] < \mNrm_{t}$).
This turns out to guarantee that normalized market resources eventually revert back toward a target.

A weaker requirement, [‘growth impatience,’](#GICRaw) ensures the existence of an aggregate buffer stock target even when individual target ratios are unbounded.
Growth impatience requires the ratio of [absolute patience](#APFac) to the *expected* growth factor of permanent income to be less than one: $\APFacRaw/\PermGroFac < 1$.

As [(Harmenberg, 2021a)](#cite-harmenbergInvariant) points out, a stationary distribution of market resources, weighted by permanent income still exists under growth impatience.
The trick to understanding how there can be an aggregate target even when there is no individual target is to realize that one reason that $\mLvl/\pLvl$ can grow is that individuals can have negative shocks to $\pLvl$. But the people whose ratio grows because their $\pLvl$ shrinks by definition account for a smaller portion of the *level* of aggregate permanent income. That is, even as their $\mNrm$ rises they become smaller contributors to the aggregate economy.
[^6]

Thus in the aggregate, even with a fixed interest rate that differs from the time preference rate, a small open economy populated by buffer stock consumers has a balanced growth path in which growth rates of consumption, income, and market resources match the exogenous growth rate of aggregate permanent income (equivalent, here, to productivity growth).
In the terms of [(Schmitt-Grohé and Uribe, 2003)](#cite-schmitt2003closing), buffer stock saving is an appealing method of ‘closing’ a small open economy model, because it requires no *ad-hoc* assumptions.
Not even borrowing constraints.

(cfLiterature)=


#### Relationship to Literature 

Although the elements of buffer stock saving behavior were informally articulated by [(Friedman, 1957)](#cite-friedmanATheory), the term was introduced to the literature by [(Deaton, 1991)](#cite-deatonLiqConstr) to describe the behavior of liquidity-constrained impatient consumers with transitory income shocks.[^7] [(Carroll, 1992)](#cite-carroll-brookings) showed (numerically) that buffer stock saving could arise even in the absence of borrowing constraints, and defined the individual buffer stock ‘target’ as the point where a measure of normalized resources is expected to stay the same.

Traditional Bellman approaches to showing existence rely on assumptions that guarantee the boundedness of utility and marginal utility [(Stokey, Lucas, and Prescott, 1989)](#cite-slpMethods).[^8]
The results by [(Ma, Stachurski, and Toda, 2020; Ma, Stachurski, and Toda, 2022a)](#cite-maUnboundedDP) are the most general we are aware of that tackle income fluctuation problems, and can be specialized to show existence in a model one step away from our normalized model with a stochastic rate of return and stochastic effective discount factor. The discrepant step is that they impose an artificial constraint and positive minimum value of income; this bounds utility from below (it can never be lower than the marginal utility of consumption) and thus cannot be applied here.

Our approach to constructing the weighted-norm space of value functions uses results on unbounded dynamic programming by [(Boyd, 1990)](#cite-jboydWeighted).[^9] Our approach differs from previous approaches in its use of limiting marginal propensities to consume to construct per-period bounds on the Bellman operator.
Moreover, our patience restrictions are grounded in intuitive economic ideas (rather than abstract mathematical assumptions) that arise naturally in the presence of permanent income uncertainty and growth.
To the best of our knowledge, these economic mechanisms have not been explored elsewhere.

Our discussion of aggregate results builds on [(Szeidl, 2013)](#cite-szeidlInvariant) and [(Harmenberg, 2021a)](#cite-harmenbergInvariant) who give results on the existence and convergence of stationary wealth distributions that apply to the model presented here.
While their conditions for stationarity relate to [growth impatience](#GICRaw) and [strong growth impatience,](#GICMod) our objective is to establish existence of stable buffer stock targets, which is relatively easily tested empirically, rather than to establish stationarity of distributions, which is much harder to imagine testing with empirical data.

(defun my-tex-command-expand-options ()
(let ((opts (TeX-command-expand-options)))
(replace-regexp-in-string " -interaction=nonstopmode" "" opts)))

(setq TeX-expand-list-builtin
(mapcar (lambda (item)
(if (equal (car item) "mode")
’("mode" my-tex-command-expand-options)
item))
TeX-expand-list-builtin))

(The-Problem)=

# Theoretical Foundations 

(sec-Theory)=

This section formalizes the consumer income fluctuation problem and proves the existence of a limiting non-degenerate solution. In doing so, we also introduce our consumer patience conditions and use them to derive the consumer’s MPCs. The MPCs are formulae, for any period $t$ earlier than the terminal period $T$, for the maximum and minimum MPCs as wealth approaches zero and infinity. If the environment is that of an infinite-horizon ‘income fluctuation problem,’ our formulae yield the limiting upper and lower bounds of the limiting non-degenerate solution.

We first state the finite horizon problem and then define the limiting solution as the limit of finite horizon solutions as the terminal period becomes arbitrarily distant. This way, the economic intuition of limiting consumer behaviour can be directly linked to consumer behaviour in life-cycle models (see [(Gourinchas and Parker, 2002)](#cite-gpLifeCycle) for an instance where buffer stock saving is discussed in the context of a life-cycle model). Nonetheless for the class of problems we consider, a non-degenerate limiting solution, if it exists, is mathematically equivalent ([(Bertsekas, 2012)](#cite-bertsekas2012dynamic), Ch. 1.) to a stationary solution to an infinite stochastic sequence problem commonly used in the literature (for example, [(Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct)).

(sec-Foundations)=

## Setup 

(subsec-Setup)=

We start by stating the consumer problem with permanent income growth in levels and then normalize by permanent income. The normalized problem then becomes the subject of our formal results in the paper.

Our time index $t$ can take on values in $\{T,T-1,T-2,\dots \}$. We assume that our consumer has a Constant Relative Risk Aversion (CRRA) per-period utility function, $\uFunc(c)=\frac{c^{1-\CRRA}}{1-\CRRA}$, where $\CRRA>1$. The term $\DiscFac$ is the (strictly positive) discount factor. In each period $t$, the consumer faces independently and identically distributed (iid) income shocks, with the permanent shock given by $\permShk_{t} \in \Reals_{++}$ and the transitory shock by $\tranShkAll_{t} \in \Reals_{+}$.[^10]

In each $t$, the finite horizon value function for the problem in levels will be denoted by $\vFuncLvl_{t}$, with $\vFuncLvl_{t}\colon \Reals_{++}^{2}\rightarrow \Reals$. Value, $\vFunc_{t}(\mLvl_{t}, \permLvl_{t})$, depends on two strictly positive state variables: ‘market resources’ $\mLvl_{t}$ and permanent income $\permLvl_{t}$.
After the terminal period, we assume the consumer cannot die in debt:

(eq-NoDebtAtDeath)=
$$
\cLvl_{T} \leq  \mLvl_{T} .$$

Letting $\vFuncLvl_{T+1} = 0$, it follows that the value function for the terminal period satisfies $\vFuncLvl_{T} = \uFunc(\mNrm_{T})$.
For $t<T$, the finite-horizon value functions are recursively defined by:

(eq-levelRecProblem)=
$$\begin{gathered}\begin{aligned}
    \vFuncLvl_{t}(\mLvl_{t}, \permLvl_{t})\colon & = \max_{0 < \cLvl_{t} \leq \mLvl_{t}} \uFunc(\cLvl_{t}) + \DiscFac \Ex_{t}\vFuncLvl_{t+1}(\mLvl_{t+1}, \permLvl_{t+1}), \qquad (\mLvl_{t}, \permLvl_{t})\in \Reals_{++}^{2} 
  \end{aligned}\end{gathered}
\tag{$\mathscr{P}_{L}$}$$

where i) $\cLvl_{t}$ is the level of consumption at time $t$, ii) $\Ex_{t}$ is the expectation operator over the shocks $\permShk_{t+1}$ and $\tranShkAll_{t+1}$
(checkRestrictions)=

, and iii) $\mLvl_{t+1}$ is determined from this period’s $\mLvl_{t}$ and choice of $\cLvl_{t}$ as follows:[^11]

(eq-DBCparts)=
$$ 
    \begin{aligned}
      \aLvl_{t}     & = \mLvl_{t}-\cLvl_{t}  \\
      \kLvl_{t+1}   & = \aLvl_{t} \notag \\
      \permLvl_{t+1}  & = \permLvl_{t} \underbrace{\PermGroFac\permShk_{t+1}}_{:= \Rnd{\PermGroFac}_{t+1}} \notag \\
      \mLvl_{t+1}  & =   \underbrace{\Rfree \kLvl_{t+1}}_{:= \bLvl_{t+1}}  +\underbrace{\permLvl_{t+1}\tranShkAll_{t+1}}_{:= \Rnd{\yLvl}_{t+1}}. \notag
    \end{aligned}$$

The consumer’s assets at the end of $t$, $\aLvl_{t}$, translate one-for-one into capital $\kLvl_{t+1}$ at the beginning of the next period.
In turn, $\kLvl_{t+1}$ is augmented by a fixed interest factor $\Rfree$ to become the consumer’s financial (‘bank’) balances $\bLvl_{t+1} = \Rfree \kLvl_{t+1}$. ‘Market resources,’ $\mLvl_{t+1}$, are the sum of financial wealth $\Rfree \kLvl_{t+1}$ and noncapital income $\yLvl_{t+1}=\permLvl_{t+1}\tranShkAll_{t+1}$ (permanent noncapital income $\permLvl_{t+1}$ multiplied by the transitory shock $\tranShkAll_{t+1}$).
Permanent noncapital income $\permLvl_{t+1}$ is derived from $\permLvl_{t}$ by application of a growth factor $\PermGroFac$,[^12] modified by the permanent income shock $\permShk_{t+1}$,[^13] and the resulting idiosyncratic growth factor for permanent income is written as $\Rnd{\PermGroFac}_{t+1}$.

Letting $n$ denote the planning horizon, the finite-horizon problems furnish a sequence of value functions $\{\vFuncLvl_{T},\vFuncLvl_{T-1},\ldots,\vFuncLvl_{T-n}\}$ and associated consumption functions $\{\cFuncLvl_{T},\cFuncLvl_{T-1},\ldots,\cFuncLvl_{T-n}\}$.
The limiting consumption function, denoted by $\usual{\cFuncLvl}(\mLvl,\permLvl) = \lim\limits_{n \rightarrow \infty} \cFuncLvl_{T-n}(\mLvl,\permLvl)$, will be called a ‘non-degenerate limiting solution’ if neither $\usual{\cFuncLvl}=0$ everywhere (for all $(\mLvl,\permLvl)$) nor $\usual{\cFuncLvl}=\infty$ everywhere.

Before turning to the normalized problem, we present the income process and its implications for the consumer problem.
The following assumption defines the income process.

(ass-shocks)=
:::{prf:assumption} Friedman-Muth Income Process
:label: ass-shocks

For each $t$:

1.  The permanent shock, $\permShk_{t}$, satisfies $\Ex[{\permShk}_{t}]=1$ and $\permShk_{t}\in [\permShkIndMin,\permShkIndMax]$ s.t. $0 < \permShkIndMin \leq 1$ and $1 \leq \permShkIndMax < \infty$.

2.  The transitory shock, $\tranShkAll_{t}$, satisfies:
(eq-TranShkDef)=
$$\tranShkAll_{t}=
        \begin{cases}
          0\phantom{_{t+1}/\pNotZero} & \text{with probability $\pZero > 0$} \\
          \tranShkEmp_{t}/\pNotZero      & \text{with probability $\pNotZero  $}, 
        \end{cases} $$

    for iid random variable $\tranShkEmp_{t}$, with $\Ex[{\tranShkEmp}_{t}]=1$ and $\tranShkEmp_{t} \in [\Min{\tranShkEmp}, \bar{\tranShkEmp}]$ s.t.
    $\tranShkEmpMin >0$ and $\Min{\tranShkEmp} \leq 1 \leq \Max{\tranShkEmp} < \infty$.

:::

Following [(Zeldes, 1989)](#cite-zeldesStochastic), the income process incorporates a small probability $\pZero$ that income will be zero (a ‘zero-income event’).
At date $T-1$, the (strictly positive) probability $q$ of zero income in period $T$ will prevent the consumer from spending all resources, because saving nothing would mean arriving in the following period with zero bank balances and thus facing the possibility of being required to consume 0, which would yield utility of $-\infty$.
This logic holds recursively from $T-1$ back, so the consumer will never spend everything, giving rise to what [(Aiyagari, 1994)](#cite-aiyagari-ge) dubbed a ‘natural borrowing constraint.’[^14] (Thus, the upper-bound constraint on consumption in the problem [](#eq-levelRecProblem) will not bind.)

(PDV)=

The model looks more special than it is.
In particular, a positive probability of zero-income events may seem objectionable (despite empirical support).
However, a nonzero minimum value of $\tranShkAll$ (motivated, say, by the existence of unemployment insurance) could be handled by capitalizing the present discounted value (PDV) of minimum income into current market assets,[^15] and transforming that model back into this one.
And no key results would change if the transitory shocks were persistent but mean-reverting (instead of iid). Also, the assumption of a positive point mass for the worst realization of the transitory shock is inessential, but simplifies the proofs and is a powerful aid to intuition.

(The-Problem-Can-Be-Rewritten-in-Ratio-Form)=


### Normalized Problem 

(subsubsec-ratio)=

Let nonbold variables be the boldface counterpart normalized by $\permLvl_{t}$, allowing us to reduce the number of states from two ($\mLvl$ and $\permLvl$) to one $(\mNrm = \mLvl/\permLvl)$.
Now, in a one-time deviation from the notational convention established in the last sentence, define nonbold ‘normalized value’ not as $\vLvl_{t}/\permLvl_{t}$ but as $\vNrm_{t} = \vLvl_{t}/\permLvl_{t}^{1-\CRRA}$, because this allows us to write nonbold $\vFunc_{t}$, with $\vFunc_{t}\colon \Reals_{++}\rightarrow \Reals$, to denote the ‘normalized value function’:

(eq-veqnNrmRecBellman)=
$$
  \begin{aligned}
    \vFunc_{t}(\mNrm_{t})  & = \max_{0<\cNrm_{t}< \mNrm_{t}}~  \uFunc(\cNrm_{t}) +\DiscFac \Ex_{t}[\Rnd{\PermGroFac}_{t+1}^{1-\CRRA}\vFunc_{t+1}({\mNrm}_{t+1})],\qquad  \mNrm_{t}\in \Reals_{++}\\
    & s.t.
    \\ {\aNrm}_{t}  & = \mNrm_{t}-c_{t}
    \\ {\bNrm}_{t+1} & = \aNrm_{t} \Rfree/\Rnd{\PermGroFac}_{t+1} = ~  \RNrmByGRnd_{t+1}\aNrm_{t} 
    \\ \mNrm_{t+1}  & = \bNrm_{t+1} +\tranShkAll_{t+1} ,
  \end{aligned}  \tag{$\mathscr{P}_{N}$}$$
where $\RNrmByGRnd_{t+1}:= (\Rfree/\PermGroFacRnd_{t+1})$ is a ‘permanent-income-growth-normalized’ return factor.[^16]
(Appendix [](#sec-recoverLevels) explains how the solution to the original problem in levels can be recovered from the normalized problem.)

The time $t$ normalized consumption *policy function* for the finite-horizon problem, $\cFunc_{t}$, is defined by:

(eq-cfunceq1)=
$$
  \begin{aligned}
    \cFunc_{t}(\mNrm_{t})\colon & = \argmax_{0<\cNrm_{t}< \mNrm_{t}}~  \uFunc(\cNrm_{t}) +\DiscFac \Ex_{t}[\Rnd{\PermGroFac}_{t+1}^{1-\CRRA}\vFunc_{t+1}(\mNrm_{t+1} )].
  \end{aligned}$$

The normalized problem’s first order condition becomes:
(eq-scaledeuler)=
$$\begin{gathered}\begin{aligned}
  c_{t}^{-\CRRA}  & = \Rfree \DiscFac \Ex_{t}[ \Rnd{\PermGroFac}_{t+1}^{-\CRRA} \cNrm_{t+1}^{-\CRRA}].  
\end{aligned}\end{gathered}$$

(sensible)=



Since our main results pertain to the normalized problem, we define the limiting non-degenerate solution to the normalized problem formally.

(def-nondegeneracy)=
:::{prf:definition} Non-degenerate Limiting Solution
:label: def-nondegeneracy

[](#eq-veqnNrmRecBellman) has a non-degenerate limiting solution if there exists $\usual{\cFunc}$, with $\usual{\cFunc}\colon \Reals_{++}\rightarrow \Reals_{++}$, and $\usual{\vFunc}$, with $\usual{\vFunc}\colon \Reals_{++}\rightarrow \Reals$, such that:

$$\begin{gathered}\begin{aligned}
  \usual{\cFunc}(\mNrm) =  \lim_{n \rightarrow \infty} \cFunc_{T-n}(\mNrm), \quad \usual{\vFunc}(\mNrm)  =  \lim_{n \rightarrow \infty} \vFunc_{T-n}(\mNrm), \qquad \mNrm \in \Reals_{++} \notag.
\end{aligned}\end{gathered}$$

:::

(Stationary-Bellman-Operator)=

We use $\TMap$ to denote the stationary Bellman operator for the normalized problem.
To define $\TMap$, let $\RNrmByGRnd := \Rfree/\PermGroFacRnd$ and let $\TMap$ denote the mapping $\vFunc_{t+1} \mapsto \vFunc_{t}$ given by Problem [](#eq-veqnNrmRecBellman):

(eq-maintmap)=
$$
  \TMap \vFunc_{t+1}(\mNrm) = \max_{\cNrm \in (0, \mNrm) }  \left\{
    \uFunc(c) + \DiscFac\Ex\Rnd{\PermGroFac}^{1-\CRRA}\vFunc_{t+1}(\RNrmByGRnd(m - c) + \tranShkAll)
  \right\}, \quad m \in \Reals_{++}.$$

The mapping $\mNrm\mapsto (0, \mNrm)$ defines the feasibility correspondence.
To define $\TMap$, we excluded the boundary of the feasible values that consumption can take ($0$ and $\mNrm$) to ensure the maximand above is real-valued for all feasible values of consumption.
It is straightforward to show (using the Bellman Principle of Optimality) that a finite valued solution, $\vFunc$, to the functional equation $\TMap\vFunc = \vFunc$ defines a [limiting non-degenerate solution](#sensible).
However, because the feasibility correspondence does not include the boundary of feasible consumption, existing dynamic programming arguments cannot be used to show that such a solution (a fixed point to $\TMap$) exists.

### Dynamic Programming Challenges 

(subsubsec-challengesDP)=
 
 Standard dynamic programming [(Stachurski, 2022)](#cite-stachurski2022) works by showing that $\TMap$ is a well-defined contraction map on a Banach space, which would allow us to conclude that the sequence of value functions given by Problem [](#eq-veqnNrmRecBellman) converges to a fixed point of $\TMap$, a non-degenerate solution.
At first, we must contend with the fact that both $\uFunc$ and $\vFunc$ are unbounded below.
We resolve unboundedness by constructing a weighted-norm (see below).
Setting aside unboundedness, the natural liquidity constraint introduces a more pernicious challenge related to continuity: $\TMap$ will not a be well defined self-map on a vector space of continuous functions.
In particular, we cannot assert $\TMap$ maps continuous functions to continuous functions since the feasiblility correspondence $\mNrm\mapsto (0, \mNrm)$ is not compact-valued.

(remark-notCompact)=
:::{prf:remark}
:label: remark-notCompact

Since the correspondence $\mNrm\mapsto (0, \mNrm)$ is not compact valued, the conditions of Berge’s Maximum Theorem (Lemma 1, [(Jaśkiewicz and Nowak, 2011)](#cite-Jaskiewicz2011)) fail and $\TMap \fFunc$ may not be continuous for continuous $\fFunc$.

:::

If we reintroduce the boundary points $0$ and $\mNrm$ to the feasibility correspondence, the operator $\TMap$ will be able to map upper semicontinuous functions to upper semicontinuous functions (Lemma 1, [(Jaśkiewicz and Nowak, 2011)](#cite-Jaskiewicz2011)).
However, $\vFunc$ must now be defined on $\Reals_{+}$ and take on values in $\mathbb{R}_{+}\cup\{-\infty\}$ and spaces of such functions will not be a vector space.
The approach taken by [(Ma, Stachurski, and Toda, 2022b)](#cite-Ma2022) is to impose an artificial liquidity constraint, which yields a real-valued continuation value, even if $\cNrm= \mNrm$, and forces the value function to be bounded below as a function of end-of-period assets.
This allows [(Ma, Stachurski, and Toda, 2022b)](#cite-Ma2022) to define a functional operator operator within which the feasibiltiy correspondence is the compact interval $[0, \mNrm]$.
Without an artificial constraint, no such strategy is possible.[^17]

A related approach, which uses Euler operators is used by [(Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct).
While [(Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct) also assume an artificial liquidity constraint to bound the marginal utility of consumption, it is useful to consider how the structure of our model relates to theirs once the artificial liquidity constraint is imposed.

(remark-stochdiscMST)=
:::{prf:remark}
:label: remark-stochdiscMST

If $\pZero=0$, [](#eq-veqnNrmRecBellman) becomes a special case of [(Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct), with $\RNrmByGRnd_{t+1}=\Rfree/\Rnd{\PermGroFac}_{t+1}$ corresponding to the stochastic rate of return on capital and $\DiscFac \Rnd{\PermGroFac}_{t+1}^{1-\CRRA}$ corresponding to the stochastic discount factor.

:::

Notwithstanding Remark [](#remark-stochdiscMST), there are important economic consequences relating consumer patience to buffer stock saving due to the fact that in our problem $\RNrmByGRnd_{t+1}=\Rfree/\Rnd{\PermGroFac}_{t+1}$ is tightly tied to the ‘normalized stochastic discount factor,’ $\DiscFac \Rnd{\PermGroFac}_{t+1}^{1-\CRRA}$; these will become apparent as we proceed.

(GICTheorySetup)=


## Consumer Patience Conditions 

(subsec-GICTheorySetup)=

In order to have a central reference point for them, we now collect conditions relating consumer discounting and patience to the rate of return and income growth that underpin results in the remainder of the paper.
Assumptions [](#FVAC) - [](#ass-RIC) (finite value of autarky, return impatience and weak return impatience) will be used to prove the existence of limiting solutions in Section [](#subsec-limSolExists), and Assumptions [](#GICRaw) - [](#GICMod) (growth impatience and strong growth impatience) are required for existence of alternative definitions of a stable target buffer stock in Section [](#sec-individStability).

We start by generalizing the standard $\DiscFac<1$ condition to our setting with permanent income growth and uncertainty.[^18] The updated condition requires that the expected net discounted value of utility from consumption is finite under our definition of ‘autarky’ – where consumption is always equal to permanent income.
A finite value of autarky helps guarantee that as the horizon extends, discounted value remains finite along *any* consumption path the consumer might choose.
(See Appendix [](#sec-ApndxConcaveCFunc)).

(FVAC)=

(ass-FVAC)=
:::{prf:assumption} Finite Value of Autarky
:label: ass-FVAC

$0 < \DiscFac \PermGroFac^{1-\CRRA}\Ex(\permShk^{1-\CRRA}) < 1$.

:::

We now turn to consumer patience and start with ‘absolute (im)patience.’
We will say that an unconstrained perfect foresight consumer exhibits absolute impatience if they optimally choose to spend so much today that their consumption must decline in the future.
The growth factor for consumption implied by the Euler equation of a perfect foresight model is $\cLvl_{t+1}/\cLvl_{t} = {(\Rfree\DiscFac)}^{1/\CRRA}$,[^19] which motivates our definition of an ‘absolute patience factor’ whose centrality (to everything that is to come later) justifies assigning to it a special symbol; we have settled on the archaic letter [‘thorn’](https://en.wikipedia.org/wiki/Thorn_(letter)):

(APFac)=


(eq-APFac)=
$$
    \APFac := {(\Rfree\DiscFac)}^{1/\CRRA}.$$

We will say that (in the perfect foresight problem) ‘an absolutely impatient’ consumer is one for whom $\APFac < 1$; that is an absolutely impatient consumer prefers to consume more today than tomorrow (and vice versa for an ‘absolutely patient’ consumer, whose consumption will grow over time):

(AIC)=

(ass-AIC)=
:::{prf:assumption} *Absolute Impatience*
:label: ass-AIC

$\APFac  < 1$.

:::

A consumer who is absolutely impatient, $\APFac<1$, satisfies the standard impatience condition commonly used in the income fluctuation literature, $\DiscFac\Rfree<1$, which guarantees the existence of a stable asset distribution when there is no permanent income growth.
However, as pointed out by [(Szeidl, 2013)](#cite-szeidlInvariant) and [(Ma, Stachurski, and Toda, 2022a)](#cite-maUnboundedDP), $\DiscFac\Rfree<1$ is not necessary for an infinite-horizon solution.

(RIC)=


Recall now our earlier requirement that the limiting consumption function $\cFunc(\mNrm)$ in our model must be ‘sensible.’
We will show below that for the perfect foresight unconstrained problem this requires

(ass-RIC)=
:::{prf:assumption} *Return Impatience*
:label: ass-RIC

$\RPFac  < 1$.

:::

Return impatience can be best understood as the tension between the income effect of capital income and the substitution effect.
As we show below in Section [](#subsec-PFBbenchmark), in the perfect foresight model, it is straightforward to derive the MPC out of overall (human plus nonhuman) wealth that would result in next period’s wealth being identical to the current period’s wealth.
The answer turns out to be an MPC (‘$\MPC$’) of $\MPC=(1-\APFac/\Rfree)$.
The interesting point here is that $\MPC$ depends both on our absolute patience factor $\APFac$ and on the return factor.
This is the manifestation in this context of the interaction of the income effect (higher wealth yields higher interest income if $\Rfree>1$) and the substitution effect (which we have already captured with $\APFac$).

Next, consider the weaker condition of a consumer whose [absolute patience factor](#APFac) is suitably adjusted to take account of the probability of zero income is less than the market return.

(WRIC)=

(ass-WRIC)=
:::{prf:assumption} *Weak Return Impatience*
:label: ass-WRIC

$\underbrace{\frac{(\pZero \Rfree \DiscFac)^{1/\CRRA}}{\Rfree}}_{ = \frac{\pZero^{1/\CRRA} \APFac}{\Rfree}} < 1. \phantom{\text{{\WRIC}:~~}}$

:::

This condition is ‘weak’ (relative to the plain return impatience) because the probability of the zero income events $\pZero$ is strictly less than 1.
The role of $\pZero$ in this equation is related to the fact that a consumer with zero end-of-period assets today has a probability $\pZero$ of having no income and no assets to finance consumption (and $\mNrm_{t+1}=0$ would yield negative infinite utility).
In the case with no artificial constraint, our main results below, in Section [](#subsec-limSolExists), show weak return impatience and finite value of autarky are sufficient to guarantee a sensible (non-degenerate) solution.

Weak return impatience cannot be relaxed further without an artificial liquidity constraint.
Even though $\pZero^{1/\CRRA} \RPFac\rightarrow 0$ as $\pZero\rightarrow 0$ the weak return impatience condition *does not* approach irrelevance as the possibility of the zero income event approaches zero.
Instead, we show below in Section [](#subsubsec-deatonIsLimit) that the limiting consumption function with a natural constraint approaches the solution to a model with an artificial constraint.

Now that we have finished discussing the requirements for a non-degenerate solution, we turn to assumptions required for stability.

(GPFacRawDefn)=

We will call the ratio of the $\APFac$ to the expected growth factor for permanent income $\PermGroFac = \Ex[\PermGroFac \permShk])$
the :
(eq-GPFacRaw)=
$$
    \GPFacRaw := \APFac/\PermGroFac$$
as exhibiting ‘growth impatience:’

We speak of a consumer whose [absolute patience factor](#APFac) is less than the expected growth factor for their permanent income $\PermGroFac = \Ex[\PermGroFac \permShk])$ as exhibiting ‘growth impatience:’

(GICRaw)=

(ass-GICRaw)=
:::{prf:assumption} *Growth Impatience*
:label: ass-GICRaw

$\GPFacRaw  < 1$.

:::

A final useful definition is ‘strong growth impatience’

(eq-GPFacMod)=
$$
    \Ex[\APFac/\PermGroFacRnd] < 1$$

which holds for a consumer for whom the expectation of the *ratio* of the [absolute patience factor](#APFac) to the (stochastic) growth factor of permanent income is less than one,

(GICMod)=

(ass-GICMod)=
:::{prf:assumption} *Strong Growth Impatience*
:label: ass-GICMod

$\Ex\left[\frac{\APFac}{\PermGroFac \permShk}\right] = \GPFacMod  < 1.$

:::

(The difference between growth impatience and strong growth impatience is that the first is the ratio of an expectation to an expectation, while the latter is the expectation of the ratio.
With non-degenerate mean-one stochastic shocks to permanent income, the expectation of the ratio is strictly larger than the ratio of the expectations).

Since $\CRRA>1$, note that strong growth impatience is weaker than the impatience condition $\DiscFac \Rnd{\PermGroFac}_{t+1}^{1-\CRRA}\RNrmByGRnd<1$ used by [(Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct) to guarantee stability. Moreover, while neither growth impatience nor return impatience will by themselves be required for the existence of a limiting solution, the finite value of autarky condition stops individuals from becoming *both* growth and return patient.

(VAFacDefn)=

(claim-noRICGIC)=
:::{prf:property}
:label: claim-noRICGIC

If [growth impatience](#GICRaw) fails ($\GPFacRaw  \geq 1$) and [return impatience](#RIC) fails ($\RPFac \geq 1$), then [finite value of autarky](#FVAC) fails ($\DiscFac \PermGroFac^{1-\CRRA}\Ex(\permShk^{1-\CRRA})\geq 1$).

:::

:::{prf:proof}

Since $\RPFac  > 1$, $\RPFac$ satisfies:

$$\RPFac = \frac{\left(\Rfree\DiscFac\right)^{\frac{1}{\CRRA}}}{\Rfree}\geq 1.$$

Multiplying both sides by $\Rfree\PermGroFac^{1-\CRRA}$ gives us:

$$\DiscFac\PermGroFac^{1-\CRRA}\Rfree^{\frac{1}{\CRRA}}\DiscFac^{\frac{1-\CRRA}{\CRRA}}{}\geq\Rfree \PermGroFac^{1-\CRRA} \Rightarrow \DiscFac\PermGroFac^{1-\CRRA}\geq\left(\frac{\APFac}{\PermGroFac}\right)^{\CRRA-1}.$$

Finally, since $\CRRA>1$, applying $\GPFacRaw  \geq 1$ gives us the result.

:::

We discuss further intuition for the consumer patience conditions below when they are used in the main results.

The relationship between the conditions and their implications for consumption behaviour will also be be discussed in detail in Section [](#sec-GICdiscussion).

(Perfect-Foresight-Benchmarks)=

## Perfect Foresight Benchmarks 

(subsec-PFBbenchmark)=

To understand the economic implications of the patience conditions, we begin with the perfect foresight case.

Below, when we say we assume perfect foresight, what we mean mathematically is:

(ass-pfincome)=
:::{prf:assumption} Perfect Foresight Income Process
:label: ass-pfincome

$\pZero=0$ and $\tranShkEmpMin=\tranShkEmpMax=\bar{\tranShkEmp}=\permShkIndMin=\permShkIndMax=1$

:::

Throughout this sub-section, we assume Assumption [](#ass-pfincome) remains in force.

Under perfect foresight, [finite value of autarky](#FVAC) reduces to a ‘perfect foresight finite value of autarky’ condition:

(PFFVAC)=

(eq-PFFVAC)=
$$\begin{gathered}\begin{aligned}  
         \DiscFac \PermGroFac^{1-\CRRA}  & <  1.  
\end{aligned}\end{gathered}$$

### Perfect Foresight without Liquidity Constraints 

(subsubsec-PFUncon)=

Consider the familiar analytical solution to the perfect foresight model without liquidity constraints.
In this case, the consumption Euler Equation always holds as an equality; with $\uP(\cLvl)=\cLvl^{-\CRRA}$ and $\uFunc^{\prime}(\cLvl_{t})=\Rfree\DiscFac\uFunc^{\prime}(\cLvl_{t+1})$, we have:

(eq-cGroFac)=
$$\begin{gathered}\begin{aligned}
  \cLvl_{t+1}/\cLvl_{t}  & = {(\Rfree\DiscFac)}^{1/\CRRA}. 
\end{aligned}\end{gathered}$$

Recalling $\RNrmByG  = \Rfree/\PermGroFac$, ‘human wealth’, is the present discounted value of income:

(eq-HDef)=
$$\begin{gathered}\begin{aligned}
  \hLvl_{t}  & = \permLvl_{t}+\RNrmByG^{-1} \permLvl_{t} + \RNrmByG^{-2} \permLvl_{t} + \cdots + \RNrmByG^{t-T} \permLvl_{t} \notag
  \\  & = \underbrace{\left(\frac{1-\RNrmByG^{-(T-t+1)}}{1-\RNrmByG^{-1}}\right)}_{ = \colon \hNrm_{t}}\permLvl_{t} .
\end{aligned}\end{gathered}$$

For human wealth to have finite value, we must have:

(ass-FHWC)=
:::{prf:assumption} Finite Human Wealth
:label: ass-FHWC

(eq-FHWC2)=
$$\begin{gathered}\begin{aligned}
   \RNrmByG^{-1} = \PermGroFac/\Rfree  & < 1. \phantom{\text{{\FHWC}:~~}}
\end{aligned}\end{gathered}$$

:::

If $\RNrmByG^{-1}$ is less than one, human wealth will be finite in the limit as $T \rightarrow \infty$ because (noncapital) income growth is smaller than the interest rate at which that income is being discounted.

Under these conditions we can define a normalized finite-horizon perfect foresight consumption function (see Appendix [](#subsec-ApndxUCPF) for details) as follows:
(MPCminDefn)=

$$\begin{gathered}\begin{aligned}
  \bar{\cFunc}_{T-n}(\mNrm_{T-n})  & = (\overbrace{\mNrm_{T-n}-1}^{
                                     = \colon  \bNrm_{T-n}}+\hNrm_{T-n})\MPCmin_{t-n}
\end{aligned}\end{gathered}$$

where $\MPCmin_{t}$ is the marginal propensity to consume (MPC) and satisfies:

(eq-PFMPCminInv)=
$$\begin{gathered}\begin{aligned}
\MPCmin_{T-n}^{-1}  = 1+\left(\MPSmax\right) \MPCmin_{T-n+1}^{-1}.
\end{aligned}\end{gathered}$$

Let $\MPCmin = \lim\limits_{n\rightarrow\infty}\MPCmin_{T-n}$.
For $\Min{\MPC}$ to be strictly positive, we must impose [return impatience](#RIC).
The limiting consumption function then becomes:

(eq-cFuncPFUnc)=
$$\begin{gathered}\begin{aligned}
  \bar{\cFunc}(\mNrm)  & = (\mNrm+\hNrm-1)\MPCmin,
\end{aligned}\end{gathered}$$

where, under return impatience, the limiting MPC becomes:

(eq-MPCminDef)=
$$
\MPCmin := 1-\RPFac.$$

In order to rule out the degenerate limiting solution in which $\bar{\cFunc}(\mNrm) = \infty$, we also require (in the limit as the horizon extends to infinity) that human wealth remain bounded (that is, we require [‘finite human wealth’](#ass-FHWC)).
Thus, while [return impatience](#RIC) prevents a consumer from saving everything in the limit, [‘finite limiting human wealth’](#ass-FHWC) prevents infinite borrowing (against infinite human wealth) in the limit.

The following two results consider the normalized problem without liquidity constraints and with perfect foresight income (Assumption [](#ass-pfincome)).

(prop-pfUCFHWC)=
:::{prf:proposition}
:label: prop-pfUCFHWC

A non-degenerate limiting solution exists if and only if [finite limiting human wealth](#ass-FHWC) ($\RNrmByG^{-1}<1$) and [return impatience](#RIC) (Assumption [](#ass-RIC)) hold.

:::

:::{prf:proof}

See Appendix [](#subsec-ApndxUCPF) for the proof.

:::

(claim-PFConspC)=
:::{prf:property}
:label: claim-PFConspC

Assume [finite human wealth](#ass-FHWC) ($\RNrmByG^{-1}<1$). If [growth impatience](#GICRaw) (Assumption [](#GICRaw)) holds, then [finite value of autarky](#FVAC) (Assumption [](#FVAC)) holds. If [finite value of autarky](#FVAC) (Assumption [](#FVAC)) holds, then [return impatience](#RIC) (Assumption [](#ass-RIC)) holds.

:::

:::{prf:proof}

See Appendix [](#subsec-PFBProofs) for the proof.

:::

The claim implies that if we impose [finite limiting human wealth](#ass-FHWC), then [growth impatience](#GICRaw) is sufficient for nondegeneracy since [finite value of autarky](#FVAC) and [return impatience](#RIC) follow.
However, there are circumstances under which [return impatience](#RIC) and [finite limiting human wealth](#ass-FHWC) can hold while the [finite value of autarky](#FVAC) fails.
For example, if $\PermGroFac=0$, the problem is a standard ‘cake-eating’ problem with a non-degenerate solution under [return impatience](#RIC).

### Perfect Foresight with Liquidity Constraints 

Our ultimate interest is in the unconstrained problem with uncertainty.
Here, we show that the perfect foresight constrained solution defines a useful limit for the unconstrained problem with uncertainty.

Consider that if a liquidity constraint requiring $\aNrm_{t} \geq 0$ binds at any $\mNrm_{t}$, it must bind at the lowest possible level of $\mNrm_{t}$, $\mNrm_{t}=1$, defined by the lower bound of having arrived into the period with $\bNrm_{t}=0$ (if the constraint were binding at any higher $\mNrm_{t}$, it would certainly be binding here, because $\uFunc^{\prime\prime}<0$ and $\cFunc^{\prime}>0$).
At $\mNrm_{t}=1$ the constraint binds if the marginal utility from spending all of today’s resources $c_{t}=m_{t}=1$, exceeds the marginal utility from doing the same thing next period, $\cNrm_{t+1}=1$; that is, if such choices would violate the Euler equation, Equation  [](#eq-scaledeuler), yielding
(eq-LiqConstrBinds)=
$$\begin{gathered}\begin{aligned}
  1^{-\CRRA}  & > \Rfree \DiscFac \PermGroFac^{-\CRRA}1^{-\CRRA},  
\end{aligned}\end{gathered}$$
which is just a restatement of [growth impatience](#GICRaw).
So, the constraint is relevant if and only if [growth impatience](#GICRaw) holds.

For the following result, consider the normalized perfect foresight problem with a liquidity constraint (that is, assume $\cNrm_{t}\leq \mNrm_{t}$ for each $t$.)

(prop-PFCExist)=
:::{prf:proposition}
:label: prop-PFCExist

If [return impatience](#RIC) (Assumption [](#ass-RIC)) holds, then a non-degenerate solution exists. Moreover, if [return impatience](#RIC) does not hold, then a non-degenerate solution exists if and only if [growth impatience](#GICRaw) (Assumption [](#GICRaw)) holds.

:::

The proof for the result follows from the discussion in Section [](#subsec-PFCon), which outlines the cases under which perfect foresight liquidity constraint solutions are non-degenerate.

Importantly, if [return impatience](#RIC) fails ($\Rfree\leq \APFac$) and [growth impatience](#GICRaw) holds ($\APFac<\PermGroFac$), then [finite human wealth](#ass-FHWC) also fails $(\Rfree \leq \PermGroFac)$.
Despite the unboundedness of human wealth as the horizon extends arbitrarily, for any finite horizon the relevant liquidity constraint prevents borrowing.
Similarly, when uncertainty is present, the natural borrowing constraint plays an analogous role in permitting a finite limiting solution with unbounded limiting human wealth – we discuss the various parametric cases in Section [](#sec-GICdiscussion).

(limsolexists)=

## Main Results for Problem with Uncertainty 

(subsec-limSolExists)=

We are now ready to return to our primary interest, the model with permanent and transitory income shocks.
Throughout this section, we assume the Friedman-Muth income process (Assumption [](#ass-shocks) holds) and examine the normalized problem, Problem [](#eq-veqnNrmRecBellman).

### Limiting MPCs 

(subsubsec-cFuncBounds)=

We first establish results regarding the shape of the consumption function.[^20]

(prop-cfuncprop)=
:::{prf:proposition}
:label: prop-cfuncprop

For each $t$, $\cFunc_{t}$ is twice continuously differentiable, increasing and strictly concave.

:::

:::{prf:proof}

See Appendix [](#sec-MPCiterproofs) for the proof.

:::

Next, we note that the ratio of optimal consumption to market resources ($\cNrm/\mNrm$) is bounded by the minimal and maximal marginal propensities to consume (MPCs).
Recall that the MPCs answer the question ‘if the consumer had an extra unit of resources, how much more spending would occur?’, The minimal and maximal MPCs are the limits of the MPC as $\mNrm \rightarrow \infty$ and $\mNrm \rightarrow 0$, which we denote by $\MPCmin_{t}$ and $\MPCmax_{t}$ respectively.
Since the consumer spends everything in the terminal period, $\MPCmin_{T}=1$ and $\MPCmax_{T}=1$.
Furthermore, Proposition [](#prop-cfuncprop) will imply:[^21]

(eq-cBounds)=
$$\begin{gathered}\begin{aligned}
  \MPCmin_{t} \mNrm_{t} ~ \leq & ~  \usual{\cFunc}_{t}(\mNrm_{t})  \leq  ~ \MPCmax_{t} \mNrm_{t} .
\end{aligned}\end{gathered}$$

We define:

(MPCmaxDefn)=

(eq-MPCminDefn)=
$$\MPCmin := \max\{0,1- \RPFac\}, $$
(eq-MPCmaxDefn)=
$$\MPCmax := 1 - \pZero^{1/\gamma}\RPFac, $$
as the ‘limiting minimal and maximal MPCs’.
The following result verifies that the consumption share is bounded each period by the minimal and maximal MPCs, that the consumption function is asymptotically linear and that the MPCs converge to the limiting MPCs as the terminal period recedes.[^22]

(cFuncBounds)=

(lemm-MPC)=
:::{prf:lemma} Limiting MPCs
:label: lemm-MPC

If [weak return impatience](#WRIC) (Assumption [](#WRIC)) holds, then:

1.  For each $n$:

(eq-MPCminInv)=
$$
    \MPCmin_{T-n}^{-1}  = 1+\left(\MPSmax\right) \MPCmin_{T-n+1}^{-1}, \qquad \MPCmax_{T-n}^{-1}   = 1+\left(\MPSmin\right) \MPCmax_{T-n+1}^{-1}.$$

2.  We have $\lim\limits_{n \rightarrow \infty }\MPCmax_{T-n} = \MPCmax>0$.
    Moreover, if [return impatience](#RIC) (Assumption [](#ass-RIC)) holds, then $\lim\limits_{n \rightarrow  \infty}\MPCmin_{T-n} = \MPCmin = 1- \RPFac>0$.

:::

:::{prf:proof}

See Appendix [](#sec-MPCiterproofs) for the proof.

:::

The MPC bound as market resources approach infinity is easy to understand.
Recall that $\bar{\cFunc}$ from the perfect foresight case will be an upper bound in the problem with uncertainty; analogously, $\MPCmin$ becomes the MPC’s lower bound.
As the *proportion* of consumption that will be financed out of human wealth approaches zero, the proportional difference between the solution to the model with uncertainty and the perfect foresight model shrinks to zero.

To understand the maximal limiting MPC, the essence of the argument is that as market resources approach zero, the overriding consideration that limits consumption is the (recursive) fear of the zero-income events — this is why the probability of the zero income event $\pZero$ appears in the expression for the maximal MPC.
[Weak return impatience](#WRIC) is too weak to guarantee a lower bound on the share of consumption to market resources; it merely prevents the upper bound on the share of consumption to market resources from approaching zero.
Weak return impatience thereby prevents a situation where *everyone* consumes an arbitrarily small share of current market resources as the terminal period recedes.
This insight plays a key role in the proof for the existence of a non-degenerate solution in what follows.

(Conditions-Under-Which-the-Problem-Defines-a-Contraction-Mapping)=

### Existence of Limiting Non-degenerate Solution 

(subsubsec-eventuallyCauchy)=

Let $\mathcal{C}(\Reals_{++},\Reals)$ be the space of continuous functions from $\Reals_{++}$ to $\Reals$.
To address the challenges posed by unbounded state-spaces, Boyd [((1990))](#cite-jboydWeighted) provided a weighted contraction mapping theorem.
Our strategy is to use this approach to first show that while the [stationary operator](#Stationary-Bellman-Operator) $\TMap$ may be undefined on a suitable Banach space (recall Remark [](#remark-notCompact)), operators defining each period’s problem (which we define below) will be contractions on a space of continuous functions with a finite weighted norm.
We then show the sequence of finite horizon value functions given by Problem [](#eq-veqnNrmRecBellman) generates a Cauchy sequence; since the weighted norm space is complete, the sequence of value functions converges to a non-degenerate solution in $\mathcal{C}(\Reals_{++},\Reals)$.

:::{prf:definition}

Fix $\fFunc$ such that $\fFunc \in \mathcal{C}(\Reals_{++},\Reals)$ and let $\boundFunc$ be a function such that $\boundFunc\in \mathcal{C}(\Reals_{++},\Reals)$ and $\boundFunc >0$. The function $\fFunc$ will be $\boundFunc$-bounded if the $\boundFunc$-norm of $\fFunc$, given by
(eq-phinorm)=
$$\Vert \fFunc\Vert _{\boundFunc }=\sup_{s\in \Reals_{++}}\left[ \frac{|\fFunc(s)|}{\boundFunc (s)}\right],
    $$
is finite.
We will call $\mathcal{C}_{\boundFunc}(\Reals_{++},\Reals)$ the subspace of functions in $\mathcal{C}(\Reals_{++},\Reals)$ that are $\boundFunc$-bounded.

:::

We define the weighting function as

$$\boundFunc(x) = \zeta + x^{1-\gamma},$$

where $\zeta \in \Reals_{++}$ is a constant derived from the model primitives and the upper and lower bound on the consumption share (see Claim [](#rem-shnkrdef) in Appendix [](#sec-Tcontractionmapping) for the parametrization of $\zeta$).

Next, for any lower bound $\MPCminInf$ and upper-bound $\MPCmaxInf$ on the share of consumption to market resources, define the ‘MPC bounded Bellman operator’ $\TMap^{\MPCminInf, \MPCmaxInf}$, with *$\TMap^{\MPCminInf, \MPCmaxInf}:\mathcal{C}_{\boundFunc }\left( \Reals_{++},\Reals\right) \rightarrow \mathcal{C}_{\boundFunc }\left( \Reals_{++},\Reals\right)$*, as:

$$\begin{gathered}
\TMap^{\MPCminInf, \MPCmaxInf} \fFunc(m) \\  = \max_{\cNrm \in
    [\MPCminInf \mNrm, \MPCmaxInf \mNrm]
  }  \left\{\uFunc(c) + \DiscFac\Ex\Rnd{\PermGroFac}^{1-\CRRA}\fFunc(\RNrmByGRnd(m - c) + \tranShkAll)\right\}, \,\,  \mNrm\in \Reals_{++}, \fFunc\in \mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right).
\end{gathered}$$

The value functions defined by Problem [](#eq-veqnNrmRecBellman) will satisfy $\vFunc_{t} = \TMap^{\MPCmin_{t}, \MPCmax_{t}}\vFunc_{t+1}$ for each period $t$, since consumption shares are bounded by the minimal and maximal MPCs (Lemma [](#cFuncBounds) and Equation [](#eq-cBounds)).
We now show the operator $\TMap^{\MPCminInf, \MPCmaxInf}$ is a contraction on $\mathcal{C}_{\boundFunc }\left( \Reals_{++},\Reals\right)$ for a suitably narrow interval $[\MPCminInf, \MPCmaxInf]$.

(thm-cmap)=
:::{prf:theorem} Contraction Mapping Under Consumption Bounds
:label: thm-cmap

If [weak return impatience](#WRIC) (Assumption [](#WRIC)) and [finite value of autarky](#FVAC) (Assumption [](#FVAC)) hold, then there exists $k$ and $\alpha\in (0,1)$ such that for all $[\MPCminInf, \MPCmaxInf]$ with $\MPCmax_{T-k}\geq \MPCmaxInf> \MPCminInf>0$, $\TMap^{\MPCminInf, \MPCmaxInf}$ is a contraction with modulus $\alpha$.

:::

:::{prf:proof}

See Appendix [](#sec-Tcontractionmapping) for the proof.

:::

The theorem says eventually the maximal MPCs will be small enough such that the Bellman operators generating the sequence of finite horizon value functions given by [](#eq-veqnNrmRecBellman) are contraction maps.

We can now relate the sequence of contraction maps to the limiting solution defined in Section [](#subsubsec-ratio).

(Sufficient-Conditions-For-non-degenerate-Solution)=

(thm-convgtobellman)=
:::{prf:theorem} Existence of Non-degenerate Solution
:label: thm-convgtobellman

If [weak return impatience](#WRIC) (Assumption [](#WRIC)) and [finite value of autarky](#FVAC) (Assumption [](#FVAC)) hold, then:

1.  There exists $k\in \mathbb{N}$ such that a) for all $n>k$ and $\MPCminInf$ with $0<\MPCminInf<\MPCmax_{T-n}$, $\TMap^{\MPCminInf, \MPCmax_{T-n}}$ is a contraction with modulus $\Shrinker<1$ and b) the sequence $\left\{\vFunc_{T-n}\right\}_{n=0}^{\infty}$ converges point-wise to $\vFunc \in \mathcal{C}_{\boundFunc}(\Reals_{++},\Reals)$.

2.  The function $\vFunc$ is a fixed point of $\TMap$ and there exists a measurable policy function, $\cFunc$, such that $\cFunc\colon \Reals_{++}\rightarrow \Reals$ and:
(eq-stationarybellman)=
$$
    \TMap\vFunc(m) =  \uFunc(\cFunc(m)) + \DiscFac\Ex \Rnd{\PermGroFac}^{1-\CRRA}\vFunc(\RNrmByGRnd(m-\cFunc(m)) + \tranShkAll) , \qquad m\in \Reals_{++}.$$

3.  The sequence $\left\{\cFunc_{T-n}\right\}_{n=0}^{\infty}$ converges point-wise to $\cFunc$ and $\cFunc$ and $\vFunc$ are a [limiting non-degenerate solution](#def-nondegeneracy).

:::

:::{prf:proof}

Item (i.)(a.) follows from Theorem [](#thm-cmap), since $0<\MPCminInf<\MPCmax_{T-n}$ and for each $t$, $\MPCmax_{T-n}\leq \MPCmax_{T-k}$ by Lemma [](#cFuncBounds).
We now prove Item (i.)(b.), that $\left\{\vFunc_{T-n}\right\}_{n=0}^{\infty}$ converges point-wise to a [limiting non-degenerate solution](#def-nondegeneracy) $\vFunc$.
In the proof, to streamline the notation, we define $t_{n}:= T - n$.
Now, for all $n>k+2$, $\vFunc_{t_{n}} = \TMap^{\MPCmin_{t_{n}}, \MPCmax_{t_{n}}}\vFunc_{t_{n-1}}$ holds by definition of Problem [](#eq-veqnNrmRecBellman).
Moreover, since $\MPCmax_{t_{n-1}}\geq \MPCmax_{t_{n}}$ by Lemma [](#cFuncBounds), we have:

$$\vFunc_{t_{n}} = \TMap^{\MPCmin_{t_{n}}, \MPCmax_{t_{n-1}}}\vFunc_{t_{n-1}},$$

and since $\MPCmin_{t_{n}}\leq \MPCmin_{t_{n-1}}$, we have:

$$\begin{gathered}\begin{aligned}
\vFunc_{t_{n-1}} &  = \TMap^{\MPCmin_{t_{n-1}}, \MPCmax_{t_{n-1}}}\vFunc_{n-2}\\ &  = \TMap^{\MPCmin_{t_{n}}, \MPCmax_{t_{n-1}}}\vFunc_{t_{n-2}}. 
\end{aligned}\end{gathered}$$

Next, take the $\boundFunc$-norm distance between $\vFunc_{t_{n}}$ and $\vFunc_{t_{n-1}}$, and note $\TMap^{\MPCmin_{t_{n}}, \MPCmax_{t_{n-1}}}$ is a contraction.
As such, the sequence of finite horizon value functions satisfy:

$$\Vert\vFunc_{t_{n}} - \vFunc_{t_{n-1}}\Vert_{\boundFunc} = \Vert\TMap^{\MPCmin_{t_{n}}, \MPCmax_{t_{n-1}}}\vFunc_{t_{n-1}} - \TMap^{\MPCmin_{t_{n}}, \MPCmax_{t_{n-1}}}\vFunc_{t_{n-2}}\Vert_{\boundFunc} \leq \Shrinker \Vert \vFunc_{t_{n-1}} - \vFunc_{t_{n-2}}\Vert_{\boundFunc}.$$

As such, $\Vert \vFunc_{t_{n}} - \vFunc_{t_{n-1}}\Vert_{\boundFunc } \leq \Shrinker \Vert \vFunc_{t_{n-1}} - \vFunc_{t_{n-2}}\Vert_{\boundFunc }$; because $n$ is arbitrary and $\alpha$ holds for all $n$ by Theorem [](#thm-cmap), this is a sufficient condition for $\left\{\vFunc_{T-n}\right\}_{n=k+2}^{\infty}$ to be a Cauchy sequence.

Since $\mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right)$ is a complete metric space, and $\vFunc_{t_{n-2}} \in \mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right)$ for each $n$, $\vFunc_{t_{n}}$ converges to $v$, with $v\in \mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right)$.
The proof for Item (i) and Item (ii) is continued in Appendix [](#sec-Tcontractionmapping).)

:::

The proof above shows that the sequence of value functions produced by the iteration of the per-period Bellman operators $\TMap^{\MPCmin_{T-n}, \MPCmax_{T-n}}$ will be a Cauchy sequence converging to the limiting solution.
Due to [weak return impatience](#WRIC), the upper bound on the per-period consumption converges to a strictly positive share of market resources, preventing consumption from converging to zero.

:::{prf:remark}

Under [return impatience](#RIC), $\MPCmin_{T-n}\geq \MPCmin>0$ for all $n$, and thus for $k\in \mathbb{N}$ large enough, $\TMap^{\MPCmin, \MPCmax_{T-k}}$ will be a stationary contraction map and we will have $\vFunc_{T-n} = \TMap^{\MPCmin, \MPCmax_{T-k}}\vFunc_{T-n+1}$ for all $n>k$. However, without [return impatience](#RIC), $\MPCmin = 0$ and $\TMap^{0, \MPC_{T-k}}$ will not be a well-defined operator from $\mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right)$ to $\mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right)$, even for $k$ large enough (recall Section [](#subsubsec-challengesDP)).

:::

Finite value of autarky is the second assumption required to show existence of limiting solutions and guarantees the value is finite (in levels) for a consumer who spent exactly their permanent income every period (see Section [](#subsec-TheModelUncertainty)).
The intuition for the finite value of autarky condition is that, with an infinite-horizon, with any strictly positive initial amount of bank balances $\bNrm_{0}$, in the limit your value can always be made greater than you would get by consuming exactly the sustainable amount (say, by consuming $(\rfree/\Rfree)\bNrm_{0}-\epsilon$ for some arbitrarily small $\epsilon>0$).

(remark-cStatStrctPos)=
:::{prf:remark}
:label: remark-cStatStrctPos

Since $\MPCmax m \geq \cFunc_{T-n}(\mNrm)\geq \MPCmin m$ and $\cFunc_{T-n}$ converges point-wise to $\cFunc$, $\MPCmax m \geq \cFunc(\mNrm)\geq \MPCmin m$. Moreover, since $\cFunc$ satisfies Equation [](#eq-stationarybellman) and $\vFunc \in \mathcal{C}_{\boundFunc }\left(\Reals_{++},\Reals\right)$, $\cFunc(\mNrm)>0$ for $\mNrm>0$.

:::

Finally, we verify that the converged non-degenerate consumption functions satisfies the same marginal propensities to consume the per-period consumption functions.

(lemma-MPCBoundsConvg)=
:::{prf:lemma}
:label: lemma-MPCBoundsConvg

If [weak return impatience](#WRIC) (Assumption [](#WRIC)) holds, then $\lim\limits_{m\rightarrow \infty} \cFunc (m)/m =\MPCmin m$ and $\lim\limits_{m\rightarrow 0} \cFunc (m)/m =\MPCmax m$.

:::

:::{prf:proof}

See Appendix [](#sec-ApndxConcaveCFunc) for the proof.

:::

(The-Liquidity-Constrained-Solution-as-a-Limit)=

### The Liquidity Constrained Solution as a Limit 

(subsubsec-deatonIsLimit)=

Recall the common assumption [(Deaton, 1991; Aiyagari, 1994; Li and Stachurski, 2014; Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct) of a strictly positive minimum value of income and a non-trivial artificial liquidity constraint, namely $\aNrm_{t}\geq 0$.
We will refer to the set-up from Section [](#subsec-Setup), with Assumption [](#Sufficient-Conditions-For-non-degenerate-Solution) modified so $\pZero=0$ as the “liquidity constrained problem.” Let $\cFunc_{t}(\bullet;\pZero)$ be the consumption function for a problem where Assumption [](#ass-shocks) holds for a given fixed $\pZero$, with $\pZero>0$.
Moreover, let $\cnstr{\cFunc}_{t}$ be the limiting consumption function for the liquidity constrained problem (note that the liquidity constraint $\cNrm_{t}\leq \mNrm_{t}$, or $\aNrm_{t}\geq 0$, becomes relevant only when $\pZero= 0$).
The discussion in Appendix [](#sec-LiqConstrAsLimit) shows how an finite-horizon solution to the liquidity constrained problem, $\cnstr{\cFunc}_{t}$ , is the limit of the problems as the probability $\pZero$ of the zero-income event approaches zero.

Intuitively, if we impose the artificial constraint without changing $\pZero$ and maintain $\pZero>0$, it would not affect behavior.
This is because the possibility of earning zero income over the remaining horizon already prevents the consumer from ending the period with zero assets.
For precautionary reasons, the consumer will save something.
However, the *extent* to which the consumer feels the need to make this precautionary provision depends on the *probability* that it will turn out to matter.
As $\pZero \rightarrow 0$, the precautionary saving induced by the zero-income events approaches zero, and “zero” is the amount of precautionary saving that would be induced by a zero-probability event by the impatient liquidity constrained consumer.
See Appendix [](#sec-LiqConstrAsLimit) for the formal proof.

(Analysis-of-the-Converged-Consumption-Function)=

# Individual Buffer Stock Stability 

(sec-individStability)=

In this section we analyse two notions of stability which will be useful for studying either an individual or a population of individuals who behave according to the converged consumption rule.
Consider an individual who at time $t$ holds normalized market resources $\mNrm_{t}$, and market resources in levels $\mLvl_{t}$, and follows the converged decision function $\cFunc$.
The time-$t$ consumption for the consumer will be $\cNrm_{t} = \cFunc(\mNrm_{t})$ and normalized market resources in time $t+1$ will be a random variable $\mNrm_{t+1} = \RNrmByGRnd_{t+1}(\mNrm_{t} - \cFunc(\mNrm_{t})) + \tranShkAll_{t+1}$.[^23]

Our first notion of stability concerns the existence of a unique ‘buffer stock target’ for the individual; we are interested in whether the current level of normalized market resources is above or below a ‘target’ level such that the magnitude of the precautionary motive (which causes a consumer to save) exactly balances the impatience motive (which makes them want to dissave).
At the individual target, expected normalized market resources in the next period, *conditioned on current normalized market resources*, will be the same as in the current period.
The intensifying strength of the precautionary motive with decreasing market resources can ensure stability of the target.
Below the target, the urgency to save due to the precautionary motive leads to an expected rise in market resources.
Conversely, above the target, impatience prevails, leading to an expected reduction of market resources.

Our second, weaker, notion of stability gives conditions for the invidiual such that an aggregate balanced growth path exists. To motivate this notion, consider Figure [](#fig-cNrmTargetFig) which shows the expected growth factors for consumption, the level of market resources, and normalized market resources, $\Ex_{t}[\cLvl_{t+1}/\cLvl_{t}]$, $\Ex_{t}[\mLvl_{t+1}/\mLvl_{t}]$, and $\Ex_{t}[\mNrm_{t+1}/\mNrm_{t}]$.[^24]
Begin by noting how the figure shows that as $\mNrm_{t} \rightarrow \infty$ the expected consumption growth factor goes to ${\APFac}$, indicated by the lower bound in Figure [](#fig-cNrmTargetFig).
Moreover, as $\mNrm_{t}$ approaches zero, the consumption growth factor approaches $\infty$.
(Proposition [](#subsec-AppxCgrowthFac) in Appendix [](#subsec-AppxCgrowthFac) establishes the asymptotic growth factors formally.)

Next, consider the implications of Figure [](#fig-cNrmTargetFig) for individual stability.
The figure shows a buffer stock target for normalized market resources, $\mNrm_{t} = \mBalLvl$, at which the expected growth factor of the level of market resources $\mLvl$ matches the expected growth factor of permanent income $\PermGroFac$.
A distinct and larger target ratio, $\mTrgNrm$, also exists.
At this ratio, $\Ex_{t}[\mNrm_{t+1}/\mNrm_{t}]=1$, and the expected growth factor of consumption is less than $\PermGroFac$.
Importantly, conditioned on an individual’s time $t$ state, this model does not have a single $\mNrm$ at which $\permLvl$, $\mLvl$ and $\cLvl$ are all expected to grow at the same rate.
Yet, when we aggregate across individuals, balanced growth paths can exist.
Importantly, balanced growth paths can exist even if a buffer stock target, where $\Ex_{t}[\mNrm_{t+1}/\mNrm_{t}]=1$, does not exist.
What we require for aggregate stability is the weaker notion of a ‘pseudo-target’ target, namely that there is some ${\mBalLvl}$ such that if $\mNrm_{t}>{\mBalLvl}$, then $\Ex_{t}[\mLvl_{t+1}/\mLvl_{t}] < \PermGroFac$.

(fig-cNrmTargetFig)=

:::{figure} Figures/cNrmTargetFig.png
:name: fig-cNrmTargetFig
:width: 80%

Buffer Stock Target and Pseudo-Target
:::

(onetarget)=


## Existence of Target and Pseudo-Target 

(subsec-onetarget)=


For both results below, consider the problem defined in Section [](#subsec-Setup).
The first stabiltiy result guarantees the existence of a buffer stock target $\mTrgNrm$ such that if $\mNrm_{t}=\mTrgNrm$, then $\Ex_{t}[\mNrm_{t+1}]=\mNrm_{t}$.
Existence of such a target requires [strong growth impatience](#GICMod).

(thm-target)=
:::{prf:theorem} Buffer Stock Target
:label: thm-target

If [weak return impatience](#WRIC) (Assumption [](#WRIC)), [finite value of autarky](#FVAC) (Assumption [](#FVAC)) and [strong growth impatience](#GICMod) (Assumption [](#GICMod)) hold, then there exists $\mTrgNrm$, with $\mTrgNrm>0$, such that:
(eq-mTarget)=
$$\Ex_t [{\mNrm}_{t+1}/\mNrm_t] = 1 ~if~ \mNrm_t = \mTrgNrm, 
      $$
and,
(eq-stability)=
$$ 
      \begin{aligned}
        \forall {\mNrm}_t\in(0,\mTrgNrm),      \,\,& \Ex_t [{\mNrm}_{t+1}] > {\mNrm}_t  \\
        \forall {\mNrm}_t\in(\mTrgNrm,\infty), \,\,& \Ex_t [{\mNrm}_{t+1}] < {\mNrm}_t.
      \end{aligned}$$

:::

:::{prf:proof}

See Appendix [](#subsubsec-AppxIndividTarget) for the proof.

:::

(mTargImplicit)=

Since $\mNrm_{t+1}= (\mNrm_{t}-\cFunc(\mNrm_{t}))\RNrmByGRnd_{t+1}  +\tranShkAll_{t+1}$, the implicit equation for $\mTrgNrm$ becomes:

(eq-mTargImplicit)=
$$
  \begin{aligned}
    \Ex_{t} [(\mTrgNrm-\cFunc(\mTrgNrm))\RNrmByGRnd_{t+1}+\tranShkAll_{t+1}] & = \mTrgNrm     \\   (\mTrgNrm-\cFunc(\mTrgNrm))\underbrace{\RNrmByG\Ex_{t}[\permShk^{-1}]}_{:= \bar{\RNrmByGRnd}}+1 & = \mTrgNrm .
  \end{aligned}$$

(Collective-Stability)=


The second, and less restrictive, definition of a target derives from a traditional aggregate question in macro models: whether or not there is a ‘balanced growth’ path in which aggregate variables (income, consumption, market resources) all grow by the same factor $\PermGroFac$.
In particular, if [growth impatience](#GICRaw) holds, the problem will exhibit a ‘pseudo-target’, by which we mean that there is some ${\mBalLvl}$ such that if $\mNrm_{t}>{\mBalLvl}$, then $\Ex_{t}[\mLvl_{t+1}/\mLvl_{t}] < \PermGroFac$.
(balgrostable)=


Conversely if $\mNrm_{t}<{\mBalLvl}$ then $\Ex_{t}[\mLvl_{t+1}/\mLvl_{t}] > \PermGroFac$.
The pseudo-target $\mBalLvl$ will be such that $\mLvl$ growth matches $\PermGroFac$, allowing us to write the implicit equation for $\mBalLvl$ as follows:

(eq-balgrostable)=
$$
  \begin{aligned}
    \Ex_{t}[\mLvl_{t+1}]/\mLvl_{t} & =\Ex_{t}[\permLvl_{t+1}]/\permLvl_{t}
    \\  \Ex_{t}[\mNrm_{t+1}\PermGroFac\permShk_{t+1}\permLvl_{t}]/(\mNrm_{t}\permLvl_{t}) & =\Ex_{t}[\permLvl_{t}\PermGroFac\permShk_{t+1}]/\permLvl_{t}
    \\ \Ex_{t}\left[\permShk_{t+1}\underbrace{\left((\mNrm_{t}-\usual{\cFunc}(\mNrm_{t})\Rfree/(\PermGroFac\permShk_{t+1}))+\tranShkAll_{t+1}\right)}_{\mNrm_{t+1}}\right]/\mNrm_{t} & = 1
    \\ 
    \Ex_{t}\left[(\mBalLvl-\usual{\cFunc}(\mBalLvl))\overbrace{\Rfree/\PermGroFac}^{\RNrmByG}+\permShk_{t+1}\tranShkAll_{t+1}\right] & = \mBalLvl
    \\  (\mBalLvl-\usual{\cFunc}(\mBalLvl))\RNrmByG + 1 & = \mBalLvl .
  \end{aligned}$$

The only difference between [](#eq-balgrostable) and [](#eq-mTargImplicit) is the substitution of $\RNrmByG$ for $\bar{\RNrmByGRnd}$.[^25]$^{,}$

Under the weaker [growth impatience](#GICRaw) condition, we can verify the existence of this pseudo-target, $\mBalLvl$.

(thm-MSSBalExists)=
:::{prf:theorem} ‘Pseudo-Target’
:label: thm-MSSBalExists

If [weak return impatience](#WRIC) (Assumption [](#WRIC)), [finite value of autarky](#FVAC) (Assumption [](#FVAC)) and [growth impatience](#GICRaw) (Assumption [](#GICRaw)) hold, then there exists a unique $\mBalLvl$, with $\mBalLvl>0$ such that:
(eq-mBalLvl)=
$$\Ex_t [\permShk_{t+1}{\mNrm}_{t+1}/\mNrm_t] = 1 ~if~ \mNrm_t = \mBalLvl.
      $$
Moreover,
(eq-stabilityStE)=
$$
      \begin{aligned}
        \forall {\mNrm}_t\in(0,\mBalLvl),      \,\,& \Ex_{t}[\mLvl_{t+1}]/\mLvl_{t} > \PermGroFac \\
        \forall {\mNrm}_t\in(\mBalLvl,\infty), \,\,& \Ex_{t}[\mLvl_{t+1}]/\mLvl_{t} < \PermGroFac.
      \end{aligned}$$

:::

:::{prf:proof}

See Appendix [](#subsubsec-AppxPseudoSS) for the proof.

:::

## Example With Balanced-Growth $\mBalLvl$ But No Target $\mTrgNrm$ 

Because the equations defining the buffer stock target and pseudo-target, [](#eq-mTargImplicit) and [](#eq-balgrostable), differ only by substitution of $\RNrmByG$ for $\bar{\RNrmByGRnd}=\RNrmByG \Ex[\permShk^{-1}]$, if there are no permanent shocks ($\permShk \equiv 1$), the conditions are identical.
For many parameterizations (e.g., under the baseline parameter values used for constructing figure [](#fig-cNrmTargetFig)), $\mTrgNrm$ and $\mBalLvl$ will not differ much.

(GICModFailsButGICRawHolds)=

(fig-GICModFailsButGICRawHolds)=

:::{figure} Figures/GICModFailsButGICRawHolds.png
:name: fig-GICModFailsButGICRawHolds
:width: 6in

Finite value of autarky and growth impatience hold but strong growth impatience fails: No Individaul Target Exists But Aggregate Target Does
:::

An illuminating exception is exhibited in Figure [](#GICModFailsButGICRawHolds), which modifies the baseline parameter values by quadrupling the variance of the permanent shocks, enough to cause failure of [strong growth impatience](#GICMod); now there is no target level of market resources $\mTrgNrm$.
Nonetheless, the pseudo-target still exists because it turns off realizations of the permanent shock.
It is tempting to conclude that the reason target $\mTrgNrm$ does not exist is that the increase in the size of the shocks induces a precautionary motive that increases the consumer’s effective patience.
The interpretation is not correct because as market resources approach infinity, precautionary saving against noncapital income risk becomes negligible (as the proportion of consumption financed out of such income approaches zero).

(PermGroFacAdj)=
The correct explanation is more prosaic: The increase in uncertainty boosts the expected uncertainty-modified rate of return factor from $\RNrmByG$ to $\bar{\RNrmByGRnd}>\RNrmByG$ which reflects the fact that in the presence of uncertainty the expectation of the inverse of the growth factor increases: $\PermGroFacAdj < \PermGroFac$.
That is, in the limit as $\mNrm \rightarrow \infty$ the increase in effective impatience reflected in $\GPFacMod > \GPFacRaw$ is entirely due to the elevation of the expected normalized return factor under uncertainty, not to a (limiting) change in precaution.
In fact, the next section will show that an aggregate balanced growth equilibrium will exist even when realizations of the permanent shock are not turned off: The required condition for aggregate balanced growth is the regular [growth impatience](#GICRaw), which ignores the magnitude of permanent shocks.[^26]

Before we get to the formal arguments, the key insight can be understood by considering an economy that starts, at date $t$, with the entire population at $\mNrm_{t}=\mBalLvl$, but then evolves according to the model’s assumed dynamics between $t$ and $t+1$.
Equation [](#eq-balgrostable) will still hold, so for this first period, at least, the economy will exhibit balanced growth: the growth factor for aggregate $\MLvl$ will match the growth factor for permanent income $\PermGroFac$.
It is true that there will be people for whom the financial balances ratio, $\bNrm_{t+1}$, where $\bNrm_{t+1} = \aNrm_{t}\Rfree/(\PermGroFac\permShk_{t+1})$, is boosted by a small draw of $\permShk_{t+1}$.
However, their contribution to the *level* of the aggregate variable is given by $\bLvl_{t+1}=\bNrm_{t+1}\pLvl_{t}\PermGroFac\permShk_{t+1}$, so their $\bNrm_{t+1}$ is reweighted by an amount that exactly unwinds that divisor-boosting.
This means that it is possible for the consumption-to-permanent-income ratio for every consumer to be small enough that their market resources ratio is expected to rise, and yet for the economy as a whole to exhibit a balanced growth equilibrium with a finite aggregate balanced growth steady state $\BalGroFac{\MNrm}$ (this is not numerically the same as the individual [pseudo-target](#Collective-Stability) ratio $\mBalLvl$ because the problem’s nonlinearities have consequences when aggregated).[^27]

(The-Aggregate-and-Idiosyncratic-Relationship-Between-Consumption-Growth-and-Income-Growth)=

# Aggregate Invariant Relationships 

In this section, we move from characterizing the individual decision rule to properties of a distribution of individuals following the converged non-degenerate consumption rule $\cFunc$.
Assume a continuum of *ex ante* identical buffer-stock households, with constant total mass normalized to one and indexed by $i$.
Szeidl [((2013))](#cite-szeidlInvariant) proved that such a population, following the consumption rule $\cFunc$, will be characterized by invariant distributions of $\mNrm$, $\cNrm$, and $\aNrm$ under the log growth impatience condition:[^28]

(GICSdl)=

(eq-GICSdl)=
$$\begin{gathered}\begin{aligned}
   \log~\GPFacRaw & < \Ex [\log \permShk] 
\end{aligned}\end{gathered}$$
which is stronger than our [growth impatience](#GICRaw) ($\GPFacRaw < 1$), but weaker than our [strong growth impatience](#GICMod) ($\GPFacMod < 1$).[^29]

(Growth-Rates-of-Aggregate-Income-and-Consumption)=

[(Harmenberg, 2021a)](#cite-harmenbergInvariant) substitutes a clever change of probability-measure into Szeidl’s proof, with the implication that under [growth impatience](#GICRaw), invariant *permanent-income-weighted* distributions of $\mNrm$ and $\cNrm$ exist (see Section [](#sec-AppxHarmImpGIC) in the Appendix).
In particular, let $\CDF_{\mNrm_{t},\permLvl_{t}}$ be the joint CDF of normalized market resources and permanent income at time $t$.[^30] The permanent-income-weighted CDF of $\mNrm_{t}$, $\Harm{\CDF}_{\mNrm_{t}}$, will be:

(eq-HarmCDF)=
$$
\Harm{\CDF}_{\mNrm_{t}}(x) = \PermGroFac^{-t}\int_{0}^{x}\int_{0}^{\infty} \permLvl\CDF_{\mNrm_{t},\permLvl_{t}}(d\mNrm,d\permLvl)$$

Simply put, the permanent-income-weighted CDF shows how the total ‘mass’ of permanent income is distributed along normalized market resources. The change of variables allows [(Harmenberg, 2021a)](#cite-harmenbergInvariant) to prove a conjecture from an earlier draft of this paper ([(Carroll, 2019, Submitted)](#cite-BufferStockTheoryQESubmit)) that under [growth impatience](#GICRaw), aggregate consumption grows at the same rate $\PermGroFac$ as aggregate noncapital income in the long run (with the corollary that aggregate assets and market resources grow at that same rate).
(test-Harmenbergs-method)=
 [(Harmenberg, 2021a)](#cite-harmenbergInvariant) also shows how the reformulation can reduce costs of calculation by over a factor of 100.[^31] The remainder of this section draws out the implications of these points for aggregate balanced growth factors.

(Growth-Rates-of-Individual-Income-and-Consumption)=

## Aggregate Balanced Growth of Income, Consumption, and Wealth 

(subsec-cGroEqPermGroFacQ)=

Define $\Mean$ to yield the expected value operator with respect to the empirical distribution of a variable across the population (as distinct from the operator $\Ex$ which represents beliefs about the future for a given individual).[^32] Using boldface capitals for aggregates, the growth factor for aggregate noncapital income becomes:
$$\YLvl_{t+1}/\YLvl_{t}  = \Mean\left[\tranShkAll_{t+1}\PermGroFac \permShk_{t+1}\permLvl_{t}\right]/\Mean\left[\permLvl_{t}\tranShkAll_{t}\right] = \PermGroFac$$
because of the independence assumptions we have made about the shocks $\tranShkAll$ and $\permShk$.

Consider an economy that satisfies the Szeidl impatience condition [](#GICSdl) and has existed for long enough by date $t$ that we can consider it as Szeidl-converged.
In such an economy a microeconomist with a population-representative panel dataset could calculate the growth factor of consumption for each individual household, and take the average:
(eq-MeanDeltaLogC)=
$$
  \begin{aligned}
    \Mean\left[\Delta \log \cLvl_{t+1}\right]  & = \Mean\left[ \log {\cNrm}_{t+1}\permLvl_{t+1} - \log c_{t}\permLvl_{t}\right]  \\
    & = \Mean\left[ \log \permLvl_{t+1}- \log \permLvl_{t}\right] + \Mean\left[ \log {\cNrm}_{t+1} - \log c_{t}\right].
  \end{aligned}$$

Because this economy is Szeidl-converged, distributions of $\cNrm_{t}$ and $\cNrm_{t+1}$ will be identical, so that the second term in [](#eq-MeanDeltaLogC) disappears; hence, mean cross-sectional growth factors of consumption and permanent income are the same:
(eq-MeanDeltaLogCeqMeanDeltaLogP)=
$$\begin{gathered}\begin{aligned}
  \Mean\left[\Delta \log \cLvl_{t+1}\right]  & = \Mean\left[ \Delta \log \permLvl_{t+1}\right] = \log \PermGroFac .
\end{aligned}\end{gathered}$$

In a Harmenberg-invariant economy (and therefore also any Szeidl-invariant economy), a similar proposition holds in the cross-section as a direct implication of the fact that a constant proportion of total permanent income is accounted for by the successive sets of consumers with any particular $\mNrm$ (recall Equation [](#eq-HarmCDF)).
This fact is one way of interpreting Harmenberg’s definition of the density of the permanent-income-weighted invariant distribution of $\mNrm$; call this density $\Harm{f}$.
To understand $\Harm{f}$, we can see how total aggregate market resources held by people with given $\mNrm$ will be:

$$\MLvl_{t}=\PermLvlAgg_{t}\Harm{f}(m)m$$

By implication of Theorem [](#thm-MSSBalExists), $\MLvl_{t}$ grows at a rate $\PermGroFac$.
We will now use this property of $\Harm{f}$ to show that aggregate consumption also grows at rate $\PermGroFac$.
Call $\CLvl_{t}(\mNrm)$ the total amount of consumption at date $t$ by persons with market resources $\mNrm$, and note that in the invariant economy this is given by the converged consumption function $\cFunc(\mNrm)$ multiplied by the amount of permanent income accruing to such people $\Harm{f}(\mNrm)\PermLvlAgg_{t}$.
Since $\Harm{f}(\mNrm)$ is invariant and aggregate permanent income grows according to $\PermLvlAgg_{t+1} = \PermGroFac \PermLvlAgg_{t}$, for any $\mNrm$, the following characterizes the growth of total consumption:

$$\begin{aligned}
    \log \CLvl_{t+1} - \log \CLvl_{t} &  \notag
    = \log \cFunc(\mNrm) \Harm{f}(\mNrm)\PermLvlAgg_{t+1} - \log \cFunc(\mNrm)\Harm{f}(\mNrm)\PermLvlAgg_{t} \\
    & = \log \PermGroFac.
  \end{aligned}$$

(Balanced-Growth-Of-Covariances)=

## Aggregate Balanced Growth and Idiosyncratic Covariances 

(subsec-Covariances)=

Harmenberg shows that the covariance between the individual consumption ratio $\cNrm$ and the idiosyncratic component of permanent income $\permLvl$ does not shrink to zero; thus, covariances are another potential measurement for construction of microfoundations.

Consider a date-$t$ Harmenberg-converged economy, and define the mean value of the consumption ratio as $\cNrmAvg_{t+n} \equiv \Mean[\cNrm_{t+n}]$.
Normalizing period-$t$ aggregate permanent income to $\PermLvlAgg_{t}=1$, total consumption at $t+1$ and $t+2$ are
(eq-atp2vsatp1)=
$$
  \begin{aligned}
        
    \CLvl_{t+1} & = \Mean[\cNrm_{t+1}\permLvl_{t+1}] = \cNrmAvg_{t+1}\PermGroFac^{1} + \cov_{t+1}(\cNrm_{t+1}, \permLvl_{t+1})
    \\  \CLvl_{t+2} & = \Mean[\cNrm_{t+2}\permLvl_{t+2}] = \cNrmAvg_{t+2}\PermGroFac^{2} + \cov_{t+2}(\cNrm_{t+2}, \permLvl_{t+2})
  \end{aligned}$$
and Harmenberg’s proof that $\CLvl_{t+2}-\PermGroFac \CLvl_{t+1}=0$ allows us to obtain:
(eq-cNrmvsCov)=
$$\begin{aligned}
        
    \left(\cNrmAvg_{t+2} - \cNrmAvg_{t+1}\right)\PermGroFac^{2} & = \PermGroFac \cov_{t+1} - \cov_{t+2} .
  \end{aligned}$$

In a Szeidl-invariant economy, $\cNrmAvg_{t+2} = \cNrmAvg_{t+1}$, so the economy exhibits balanced growth in the covariance:
$$\begin{gathered}\begin{aligned}
  \cov_{t+2} & = \PermGroFac \cov_{t+1}.
\end{aligned}\end{gathered}$$

The more interesting case is when the economy is Harmenberg- but not Szeidl-invariant.
In that case, if the $\cov$ and the $\cNrmAvg$ terms have constant growth factors $\GroFac_{\cov}$ and $\GroFac_{\cNrmAvg}$,[^33] an equation corresponding to [](#eq-cNrmvsCov) will hold in $t+n$:
(eq-aNrmGrovsCovGronm1)=
$$
  \begin{aligned}
    (\overbrace{\GroFac_{\cNrmAvg}^{n}\cNrmAvg_{t}}^{\cNrmAvg_{t+n}}-\GroFac^{n-1}_{\cNrmAvg}\cNrmAvg_{t})\PermGroFac^{n} & = \left(\PermGroFac\GroFac_{\cov}^{n-1} -\GroFac_{\cov}^{n}\right)\cov_{t}
    \\ (\GroFac_{\cNrmAvg}\PermGroFac)^{n-1} (\GroFac_{\cNrmAvg}-1)\cNrmAvg_{t}\PermGroFac & = \GroFac_{\cov}^{n-1}(\PermGroFac - \GroFac_{\cov}) \cov_{t}
  \end{aligned}$$
so for the LHS and RHS to grow at the same rates we need
(eq-aNrmGrovscovGro)=
$$\begin{gathered}\begin{aligned}
  \GroFac_{\cov}  & = \GroFac_{\cNrmAvg}\PermGroFac .
\end{aligned}\end{gathered}$$
This is intuitive: In the Szeidl-invariant economy, it just reproduces our result above that the covariance exhibits balanced growth because $\GroFac_{\cNrmAvg}=1$.
The revised result just says that in the Harmenberg case where the mean value $\cNrmAvg$ of the consumption ratio $\cNrm$ can grow, the covariance must rise in proportion to any ongoing expansion of $\cNrmAvg$ (as well as in proportion to the growth in $\permLvl$).

(microfounding-macro-needs-ergodicity)=

## Implications for Microfoundations 

(subsec-microfoundations)=

Thus we have microeconomic propositions, for both growth factors and for covariances of observable variables,[^34] that can be tested in either cross-section or panel microdata to judge (and calibrate) the microfoundations that should hold for any macroeconomic analysis that requires balanced growth for its conclusions.

At first blush, these points are reassuring; one of the most persuasive arguments for the agenda of building microfoundations of macroeconomics is that newly available ‘big data’ allow us to measure cross-sectional covariances with great precision, so that we can use microeconomic natural experiments to disentangle questions that are hopelessly entangled in aggregate time-series data.
Knowing that such covariances ought to be a stable feature of a stably growing economy is therefore encouraging.

But this discussion also highlights an uncomfortable point: In the model as specified, permanent income does not have a limiting distribution; it becomes ever more dispersed as the economy with infinite-horizon consumers continues to exist indefinitely.

A few microeconomic data sources permit direct measurement of ‘permanent income’; among the best (in data quality and span) is data from the Norwegian national registry, which has a long span of well-measured data for millions of Norwegians. Recent work by [(Crawley, Holm, and Tretvoll, 2022)](#cite-crawleyParsimonious) demonstrates that these data point strongly to the presence of a component of income shocks that is either truly permanent, or so extremely highly serially correlated as to be indistinguishable from permanent shocks. Using IRS tax data, [(DeBacker, Heim, Panousi, Ramnath, and Vidangos, 2013)](#cite-dhprvInequality) similarly find a large permanent (or very nearly permanent) component to income shocks. In quite a different exercise [(Carroll, Sla{}calek, To{}ku{}o{}ka, and White, 2017)](#cite-cstwMPC) show that their calibration of the magnitude of permanent shocks (and mortality; see below) yield a simulated distribution of permanent income that matches answers in the U.S. *Survey of Consumer Finances* (‘SCF’) to a question designed to elicit a direct measure of respondents’ permanent income.

For macroeconomists who want to build microfoundations by comparing the microeconomic implications of their models to micro data (directly – not in ratios to difficult-to-meaure ‘permanent income’), it would be something of a challenge to determine how to construct empirical-data-comparable simulated results from a model with no limiting distribution of permanent income.

Death can solve this problem.

(Mortality)=

## Mortality Yields Invariance 

(sec-Mortality)=


Most heterogeneous-agent models incorporate a constant positive probability of death, following [(Blanchard, 1985)](#cite-blanchardFinite) and [(Yaari, 1965)](#cite-yaari1965uncertain).
In the Blanchardian model, if the probability of death exceeds a threshold that depends on the size of the permanent shocks, [(Carroll, Sla{}calek, To{}ku{}o{}ka, and White, 2017)](#cite-cstwMPC) show that the limiting distribution of permanent income has a finite variance.
[(Blanchard, 1985)](#cite-blanchardFinite) assumes a universal annuitization scheme in which estates of dying consumers are redistributed to survivors in proportion to survivors’ wealth, giving the recipients a higher effective rate of return.
This treatment has considerable analytical advantages, most notably that the effect of mortality on the time preference factor is the exact inverse of its effect on the (effective) interest factor.
That is, if the ‘pure’ time preference factor is $\DiscFacRaw$ and probability of remaining alive (not dead) is $\Alive$, then the assumption that no utility accrues after death makes the effective discount factor $\DiscFacLiv=\DiscFacRaw\Alive$ while the enhancement to the rate of return from the annuity scheme yields an effective interest factor $\RfreeEff=\Rfree/\Alive$ (recall that because of white-noise mortality, the average wealth of the two groups is identical).
Combining these, the effective patience factor in the new economy $\DiscFacLiv \RfreeEff$ is unchanged from its value in the infinite-horizon model:
$$\DiscFacLiv \RfreeEff = {\left(\DiscFac \Alive \Rfree / \Alive\right)}^{1/\CRRA} = {\left(\Rfree \DiscFacRaw\right)}^{1/\CRRA} = \APFac.$$

The only adjustments this requires to the analysis above are therefore to the few elements that involve a role for the interest factor distinct from its contribution to $\APFac$ (principally, the RIC, which becomes $\APFac/\RfreeEff$).

(Modigliani-Lives)=

[(Blanchard, 1985)](#cite-blanchardFinite)’s innovation was valuable not only for the insight it provided but also because when he wrote, the principal alternative, the Life Cycle model of [(Modigliani, 1966)](#cite-modiglianiWealth), was computationally challenging given then-available technologies.
Despite its (considerable) conceptual value, Blanchard’s analytical solution is now rarely used because essentially all modern modeling incorporates uncertainty, constraints, and other features that rule out analytical solutions anyway.

The simplest alternative to Blanchard is to follow Modigliani in constructing a realistic description of income over the life cycle and assuming that any wealth remaining at death occurs accidentally (not implausible, given the robust finding that for the great majority of households, bequests amount to less than 2 percent of lifetime earnings, [(Hendricks, 2001; Hendricks, 2016)](#cite-hendricksSmallBequests)).

Even if bequests are accidental, a macroeconomic model must make some assumption about how they are disposed of: As windfalls to heirs, estate tax proceeds, etc.
We again consider the simplest choice, because it represents something of a polar alternative to Blanchard.
Without a bequest motive, there are no behavioral effects of a 100 percent estate tax; we assume such a tax is imposed and that the revenues are effectively thrown in the ocean: The estate-related wealth effectively vanishes from the economy.

The chief appeal of this approach is the simplicity of the change it makes in the condition required for the economy to exhibit a balanced growth equilibrium (for consumers without a life cycle income profile).
If $\Alive$ is the probability of remaining alive, the condition changes from the plain [growth impatience](#GICRaw) to a looser mortality-adjusted version of [growth impatience](#GICRaw):

(GICLivModDefn)=

(eq-GICLivMod)=
$$\begin{gathered}\begin{aligned}
  \Alive  \APFac_{\PermGroFac} & < 1. 
\end{aligned}\end{gathered}$$

With no income growth, what is required to prohibit unbounded growth in aggregate wealth is the condition that prevents the per-capita wealth-to-permanent-income ratio of surviving consumers from growing faster than the rate at which mortality diminishes their collective population.
With income growth, the aggregate wealth-to-income ratio will head to infinity only if a cohort of consumers is patient enough to make the desired rate of growth of wealth fast enough to counteract combined erosive forces of mortality and productivity.

(Discussion-Growth-Impatience)=

# Consumer Patience and Limiting Consumption 

(sec-GICdiscussion)=

(fig-cFuncsConverge)=

:::{figure} Figures/cFuncsConverge.png
:name: fig-cFuncsConverge
:width: 5.25in

Convergence of the Consumption Rules
:::

Having established our formal results, we are ready to describe how the various patience conditions determine the characteristics of the limiting consumption function.
To fix ideas, we start with a quantitative example using the familiar benchmark case where [return impatience](#RIC), [growth impatience](#GICRaw) and [finite human wealth](#ass-FHWC) all hold, shown by Figure [](#sec-GICdiscussion).
The figure depicts the successive consumption rules that apply in the last period of life $(\cFunc_{T})$, the second-to-last period, and earlier periods under parameter values listed in Table [](#Symbols).
(The 45 degree line is $\cFunc_{T}(\mNrm) = m$ because in the last period of life it is optimal to spend all remaining resources.)

Under the same parameter values, Figures [](#mpclimits)–[](#fig-cFuncBounds) capture the theoretical bounds and MPCs of the converged consumption rule.
In Figure [](#mpclimits), as $\mNrm$ rises, the marginal propensity to consume approaches $\MPCmin=(1-\RPFac)$ as $m \rightarrow \infty$, the same as the perfect foresight MPC.
Moreover, as $\mNrm$ approaches zero, the MPC approaches $\MPCmax=(1-\pZero^{1/\CRRA}\RPFac)$.

(mpclimits)=


(fig-mpclimits)=

:::{figure} Figures/MPCLimits.png
:name: fig-mpclimits
:width: 6in

Limiting MPC’s
:::

(fig-cFuncBounds)=

:::{figure} Figures/cFuncBounds.png
:name: fig-cFuncBounds
:width: 6in

Upper and Lower Bounds on the Consumption Function
:::

While in the presence of a constraint neither [return impatience](#RIC) nor [growth impatience](#GICRaw) is individually necessary for nondegeneracy of $\cFunc(m)$, a key conclusion of this section is that if *both* [return impatience](#RIC) and [growth impatience](#GICRaw) fail, the consumption function *will* be degenerate (limiting either to $\cFunc(m)=0$ or $c(\mNrm)=\infty$ as the horizon recedes).
So, for a useful solution, at least one of these conditions must hold.[^35] The case with [growth impatience](#GICRaw) but [return *patience*](#RIC) is particularly surprising, because it is not immediately clear what prevents our earlier conclusion (in other circumstances) that return patience leads $\cFunc(m)$ to asymptote to zero.
The trick is to note that if return patience holds, $\Rfree < \APFac$, while failure of growth impatience means $\APFac < \PermGroFac$; together these inequalities tell us that $\Rfree < \PermGroFac$ so (limiting) human wealth is infinite.[^36]
But, if at any $\mNrm$ human wealth is unbounded, what prevents $\cFunc$ from asymptoting to $\cFunc(m)=\infty$ as the horizon gets arbitrarily long?
This is where the natural borrowing constraint comes in.
We will show that [growth impatience](#GICRaw) is sufficient, at any fixed $\mNrm$, to guarantee an upper bound to $\cFunc(m)$.
The insight is best understood by first abstracting from uncertainty and studying the perfect foresight case (with and without constraints).

## Model with Perfect Foresight 

(subsec-PFBdiscussion)=



Claims [](#VAFacDefn)-[](#claim-PFConspC) established the relationship between the [finite value of autarky](#PFFVAC), [return impatience](#RIC) and [growth impatience](#GICRaw) in the context of a model with uncertainty.
The easiest way to grasp the relations among these conditions is by studying Figure [](#RelatePFGICFHWCRICPFFVAC).
Each node represents a quantity defined above.
The arrow associated with each inequality imposes the condition, which is defined by the originating quantity being smaller than the arriving quantity.
For example, one way we wrote the 

finite value of autarky (under perfect foresight) in Equation [](#PFFVAC) is $\APFac < \Rfree^{1/\CRRA} \PermGroFac^{1-1/\CRRA}$, so imposition of 

finite value of autarky is captured by the diagonal arrow connecting $\APFac$ and $\Rfree^{1/\CRRA}\PermGroFac^{1-1/\CRRA}$.
Traversing the boundary of the diagram clockwise starting at $\APFac$ involves imposing first [growth impatience](#GICRaw) ($\APFac < \PermGroFac$) then 

finite human wealth ($\PermGroFac < \PermGroFac(\Rfree/\PermGroFac)^{1/\CRRA} \longleftrightarrow \PermGroFac < \Rfree$), and the consequent arrival at the bottom right node tells us that these two conditions jointly imply 

perfect-foresight-finite-value-of-autarky.
Reversal of a condition reverses the arrow’s direction; so, for example, the bottom-most arrow going rightwards to $\Rfree^{1/\CRRA}\PermGroFac^{1-1/\CRRA}$ implies 

finite human wealth fails; but we can cancel the cancellation and reverse the arrow.
This would allow us to traverse the diagram clockwise from $\APFac$ through $\PermGroFac$ to $\Rfree^{1/\CRRA}\PermGroFac^{1-1/\CRRA}$ to $\Rfree$, revealing that imposition of [growth impatience](#GICRaw) and 

finite human wealth (and, redundantly, 

finite human wealth again) let us conclude that [return impatience](#RIC) holds because the starting point is $\APFac$ and the endpoint is $\Rfree$ (and we have traversed a chain of ‘is greater than’ relations).[^37]

(RelatePFGICFHWCRICPFFVAC)=

(fig-RelatePFGICFHWCRICPFFVAC)=

:::{figure} Figures/RelatePFGICFHWCRICPFFVAC.svg
:name: fig-RelatePFGICFHWCRICPFFVAC
:width: 5in

Perfect Foresight Relation of Consumer Patience Conditions
:::

In the unconstrained case, [finite human wealth](#ass-FHWC) was necessary since, without constraints, only this condition could prevent infinite borrowing in the limit (Proposition [](#prop-pfUCFHWC)).
Looking at Figure [](#RelatePFGICFHWCRICPFFVAC), following the diagonal from $\APFac$ to the bottom-right corner corresponds to the direct of imposition of the [finite value of autarky](#PFFVAC), which implies that the existence of a non-degenerate solution *requires* [return impatience](#RIC) to hold.
To see why, if [return impatience](#RIC) failed, proceeding clockwise from the bottom left node of $\Rfree$ would lead to $\Rfree> \Rfree^{1/\CRRA}\PermGroFac^{1-1/\CRRA}$, (equivalently $(\PermGroFac/\Rfree)^{1-{1/\CRRA}}<1$) which corresponds to failure of [finite human wealth](#ass-FHWC) (see also Case 3 in Section [](#subsubsec-casesUC)).

We can understand how failure of [finite human wealth](#ass-FHWC) leads to infinite borrowing thinking about [growth impatience](#GICRaw).
From Figure [](#RelatePFGICFHWCRICPFFVAC), let [finite value of autarky](#PFFVAC) hold (traverse the diagonal from $\APFac$) and then reverse the downward arrow from $\PermGroFac$, signifying the failure of [finite human wealth](#ass-FHWC), so that as the horizon extends and income grows faster than the rate at which it is discounted, there is no upper bound to the present discounted value of future income (cf. Equation [](#eq-LiqConstrBinds)).
But the cancellation of [finite human wealth](#ass-FHWC) also indirectly implies that [growth impatience](#GICRaw) holds $\APFac > \Rfree^{1/\CRRA}\PermGroFac^{1-\CRRA} > \PermGroFac$ which tells us that this is a consumer who wants to spend out of their human wealth.
And therefore, at any fixed level of market resources, there is no upper bound to how much the consumer would choose to borrow as the horizon recedes.

Thus, in the perfect foresight unconstrained model, [return impatience](#RIC) is the only condition at our disposal that can prevent consumption from limiting to zero as the terminal period recedes.
However, when we impose a liquidity constraint, the range of admissible parameters becomes more interesting.

(PF-Constrained-Solution)=


### Perfect Foresight Constrained Solution 

(subsec-PFCon)=

We now sketch the perfect foresight constrained solution and demonstrate that a solution can exist either under [return impatience](#RIC) or without [return impatience](#RIC) but with [growth impatience](#GICRaw) (Proposition [](#prop-PFCExist)).
Our discussion proceeds by examining implications of possible configurations of the patience conditions.
(Tables [](#Factors-Defined-And-Compared) and [](#Required) codify.)

#### Case 1: Growth impatience fails and return impatience holds. 

If [growth impatience](#GICRaw) fails but [return impatience](#RIC) holds, Appendix [](#sec-ApndxLiqConstr) shows that, for some $\mNrm_{\#}$, with $0 < \mNrm_{\#} < 1$, an unconstrained consumer behaving according to the perfect foresight solution [](#eq-cFuncPFUnc) would choose $\cNrm < \mNrm$ for all $\mNrm > \mNrm_{\#}$.
In this case the solution to the constrained consumer’s problem is simple; for any $\mNrm \geq \mNrm_{\#}$ the constraint does not bind (and will never bind in the future).
For such $\mNrm$ the constrained consumption function is identical to the unconstrained one.
If the consumer were somehow[^38] to arrive at an $\mNrm_{\#}$ such that $\mNrm < \mNrm_{\#} < 1$ the constraint would bind and the consumer would consume $\cNrm=\mNrm$.
Using $\cnstr{\cFunc}$ for the perfect foresight consumption function in the presence of constraints (and analogously for all other functions):
$$\cnstr{\cFunc}(\mNrm)=
  \begin{cases}
    \mNrm & \text{if $\mNrm < \mNrm_{\#}$} \\
    \bar{\cFunc}(\mNrm)  & \text{if $\mNrm \geq \mNrm_{\#}$}
  \end{cases}$$
where $\bar{\cFunc}(\mNrm)$ is the unconstrained perfect foresight solution.

#### Case 2: Growth impatience holds and return impatience holds. 

When [return impatience](#RIC) and [growth impatience](#GICRaw) both hold, Appendix [](#sec-ApndxLiqConstr) shows that the limiting constrained consumption function is piecewise linear, with $\cnstr{\cFunc}(\mNrm)=\mNrm$ up to a first ‘kink point’ at $\mNrm_{\#}^{0}>1$, and with discrete declines in the MPC at a set of kink points $\{\mNrm_{\#}^{1},\mNrm_{\#}^{2},\ldots\}$.
As $\mNrm \rightarrow \infty$ the constrained consumption function $\cnstr{\cFunc}(\mNrm)$ becomes arbitrarily close to the unconstrained $\bar{\cFunc}(\mNrm)$, and the marginal propensity to consume, $\cnstr{\cFunc}^{\prime}(\mNrm)$, limits to $\MPCmin$.[^39]
Similarly, the value function $\cnstr{\vFunc}(\mNrm)$ is non-degenerate and limits to the value function of the unconstrained consumer.

This logic holds even when [finite human wealth fails](#ass-FHWC), because the constraint prevents the (limiting) consumer[^40] from borrowing against unbounded human wealth to finance unbounded current consumption.
Under these circumstances, the consumer who starts with any $\bNrm_{t} > 0$ will, over time, run those resources down so that after some finite number of periods $\tau$ the consumer will reach $\bNrm_{t+\tau} = 0$, and thereafter will set $\cLvl = \permLvl$ for eternity (which 

finite value of autarky says yields finite value).
Using the same steps as for Equation [](#eq-ValuePFAnalyticalAutarky), value of the interim program is also finite: 

$$\begin{gathered}\begin{aligned}
  \vLvl_{t+\tau} 
  & = \PermGroFac^{\tau(1-\CRRA)} \uFunc(\permLvl_{t})\left(\frac{1-{(\DiscFac \PermGroFac^{1-\CRRA})}^{T-(t+\tau)+1}}{1-\DiscFac \PermGroFac^{1-\CRRA}}\right).
\end{aligned}\end{gathered}$$

So, even when [finite human wealth fails](#ass-FHWC), the limiting consumer’s value for any finite $\mNrm$ will be the sum of two finite numbers: One due to the unconstrained choice made over the finite-horizon leading up to $\bNrm_{t+\tau} = 0$, and one reflecting the value of consuming $\permLvl_{t+\tau}$ thereafter.

(RICandFHWCFail)=

#### Case 3: Growth impatience holds and return impatience fails. 

The most peculiar possibility occurs only when [return impatience](#RIC) fails.
As noted above, this possibility is unavailable to us without a constraint.
Without return impatience, [finite human wealth](#ass-FHWC) must also fail (Appendix [](#sec-ApndxLiqConstr)), and the constrained consumption function is (surprisingly) non-degenerate.
(See appendix Figure [](#PFGICHoldsFHWCFailsRICFails) for a numerical example).
Even though human wealth is unbounded at any given level of $\mNrm$, since borrowing is ruled out, consumption cannot become unbounded at that $\mNrm$ in the limit as the horizon recedes.
However, the failure of return impatience does have some power: It means that as $\mNrm$ rises without bound, the MPC approaches zero ( $\lim\limits_{m \rightarrow \infty} \cnstr{\cFunc}^{\prime}(\mNrm) = 0$).
Nevertheless $\cnstr{\cFunc}(\mNrm)$ is finite, strictly positive, and strictly increasing in $\mNrm$.
This result reconciles the conflicting intuitions from the unconstrained case, where failure of [return impatience](#RIC) would suggest a degenerate limit of $\cnstr{\cFunc}(\mNrm)=0$ while failure of [finite human wealth](#ass-FHWC) would suggest a degenerate limit of $\cnstr{\cFunc}(\mNrm)=\infty$.

(model-with-uncertainty)=

## Model with Uncertainty 

(subsec-TheModelUncertainty)=

We now examine the case with uncertainty but without constraints, which we argued was a close parallel to the model with constraints but without uncertainty (recall Section [](#subsubsec-deatonIsLimit)).

:::{table} Microeconomic Model Calibration
:name: Calibration

| Calibrated Parameters |  |  |  |  |
|:--:|:--:|:--:|:---|:--:|
| Description | Parameter | Value | Source |  |
| Permanent Income Growth Factor | $\PermGroFac$ | 1.03 | PSID: Carroll (1992) |  |
| Interest Factor | $\Rfree$ | 1.04 | Conventional |  |
| Time Preference Factor | $\beta$ | 0.96 | Conventional |  |
| Coefficient of Relative Risk Aversion | $\CRRA$ | 2 | Conventional |  |
| Probability of Zero Income | $\pZero$ | 0.005 | PSID: Carroll (1992) |  |
| Std Dev of Log Permanent Shock | $\sigma_{\permShk}$ | 0.1 | PSID: Carroll (1992) |  |
| Std Dev of Log Transitory Shock | $\sigma_{\theta}$ | 0.1 | PSID: Carroll (1992) |  |

:::


:::{table}
:name: Symbols

|  |  |  |  |  |
|:--:|:--:|:--:|:---|:--:|
|  |  |  |  | Approximate |
|  |  |  |  | Calculated |
| Description | Symbol and Formula |  |  | Value |
| [Finite Human Wealth Factor](#FHWFacDefn) | $\RNrmByGRnd^{-1}$ | $\equiv$ | $\PermGroFac/\Rfree$ | 0.990 |
| [PF Value of Autarky Factor](#VAFacDefn) | $\beth$ | $\equiv$ | $\DiscFac \PermGroFac^{1-\CRRA}$ | 0.932 |
| [Growth Compensated Permanent Shock](#InvEPermShkEInv) | $\InvEPermShkInv$ | $\equiv$ | $(\EPermShkInv)^{-1}$ | 0.990 |
| [Uncertainty-Adjusted Growth](#PermGroFacAdj) | $\PermGroFacAdj$ | $\equiv$ | $\PermGroFac \InvEPermShkInv$ | 1.020 |
| [Utility Compensated Permanent Shock](#uInvEuPermShk) | $\uInvEuPermShk$ | $\equiv$ | $(\Ex[\permShk^{1-\CRRA}])^{1/(1-\CRRA)}$ | 0.990 |

:::

| 
(PermGroFacAdjU)=
[Utility Compensated Growth](#PermGroFacAdjU) | $\PermGroFacAdjU$ | $\equiv$ | $\PermGroFac \uInvEuPermShk$ | 1.020 |
| [Absolute Patience Factor](#APFac) | $\APFac_{\phantom{\Rfree}}$ | $\equiv$ | $(\Rfree \DiscFac)^{1/\CRRA}$ | 0.999 |
| [Return Patience Factor](#RIC) | $\RPFac$ | $\equiv$ | $\APFac/\Rfree$ | 0.961 |
| [Growth Patience Factor](#GPFacRawDefn) | $\GPFacRaw$ | $\equiv$ | $\APFac/\PermGroFac$ | 0.970 |
| [Modified Growth Patience Factor](#GPFacRawDefn) | $\GPFacMod$ | $\equiv$ | $\APFac/\PermGroFacAdj$ | 0.980 |
| [Value of Autarky Factor](#VAFacDefn) | $\DiscAltuAdj$ | $\equiv$ | $\DiscFac \PermGroFac^{1-\CRRA}\uInvEuPermShk^{1-\CRRA}$ | 0.941 |
| [Weak Return Impatience Factor](#WRIC) | $\pZero^{1/\CRRA} \APFac$ | $\equiv$ | $(\pZero \DiscFac \Rfree)^{1/\CRRA}$ | 0.071 |

: Model Characteristics Calculated from Parameters

Tables [](#Calibration) and [](#Symbols) present calibrations and values of model conditions in the case with uncertainty, where [return impatience](#RIC), [growth impatience](#GICRaw) and [finite value of autarky](#FVAC) all hold.
The full relationship among conditions is represented in Figure [](#fig-Inequalities).
Though the diagram looks complex, it is merely a modified version of the earlier simple diagram (Figure [](#RelatePFGICFHWCRICPFFVAC)) with further (mostly intermediate) inequalities inserted.
(Arrows with a “because” now label relations that always hold under the model’s assumptions.)[^41]

(fig-Inequalities)=

:::{figure} Figures/Inequalities.svg
:name: fig-Inequalities
:width: 6in

Relation of All Inequality Conditions
:::

Beyond [finite value of autarky](#FVAC),
the additional condition sufficient for contraction, [weak return impatience](#WRIC), can be seen to be weak by asking ‘under what circumstances would the [finite value of autarky](#FVAC) hold but the [weak return impatience](#WRIC) fail?’ Algebraically, the requirement becomes:

(eq-WRICandFVAC)=
$$\begin{gathered}\begin{aligned}
  \DiscFac \PermGroFac^{1-\CRRA}\uInvEuPermShk^{1-\CRRA} & < ~ 1 ~ <  {(\pZero \DiscFac)}^{1/\CRRA}/\Rfree^{1-1/\CRRA}. 
\end{aligned}\end{gathered}$$

(uInvEuPermShk)=

where $\uInvEuPermShk := (\Ex[\permShk^{1-\CRRA}])^{1/(1-\CRRA)} < 1$.
If we require $\Rfree \geq 1$, the [weak return impatience](#WRIC) is ‘redundant’ because now $\DiscFac <1<\Rfree^{\CRRA-1}$, so that (with $\CRRA > 1$ and $\DiscFac<1$) [return impatience](#RIC) (and [weak return impatience](#WRIC)) must hold.
But neither theory nor evidence demand that $\Rfree \geq 1$.
We can therefore approach the question of the relevance of [weak return impatience](#WRIC) by asking just how low $\Rfree$ must be for the condition to be relevant.
Suppose for illustration that $\CRRA=2$, $\uInvEuPermShk^{1-\CRRA}=1.01$, $\PermGroFac^{1-\CRRA}=1.01^{-1}$ and $\pZero = 0.10$.
In that case [](#eq-WRICandFVAC) reduces to:
$$\begin{gathered}\begin{aligned}
  \DiscFac  & < 1 < {(0.1 \DiscFac/\Rfree)}^{1/2},
\end{aligned}\end{gathered}$$
but since $\DiscFac < 1$ by assumption, the binding requirement becomes:
$$\begin{gathered}\begin{aligned}
  \Rfree  & < \DiscFac/10, \notag
\end{aligned}\end{gathered}$$
so that for example if $\DiscFac=0.96$ we would need $\Rfree < 0.096$ (that is, a perpetual riskfree rate of return of worse than -90 percent a year) in order for [weak return impatience](#WRIC) to be nonredundant.

Perhaps the best way of thinking about this is to note that the space of parameter values for which the [weak return impatience](#WRIC) remains relevant shrinks out of existence as $\pZero \rightarrow 0$, which Section [](#subsubsec-deatonIsLimit) showed was the precise limiting condition under which behavior becomes arbitrarily close to the liquidity constrained solution (in the absence of other risks).
On the other hand, when $\pZero = 1$, the consumer has no noncapital income (so [finite human wealth](#ass-FHWC) holds) and with $\pZero=1$ [weak return impatience](#WRIC) is identical to [weak return impatience](#WRIC).
However, [weak return impatience](#WRIC) is the only condition required for a solution to exist for a perfect foresight consumer with no noncapital income.
Thus [weak return impatience](#WRIC) forms a sort of ‘bridge’ between the liquidity constrained and the unconstrained problems as $\pZero$ moves from 0 to 1.

### Behavior Under Cases of Conditions 

(subsubsec-casesUC)=


#### Case 1: Return impatience fails and growth impatience holds 

In the unconstrained perfect foresight problem (Section [](#subsec-PFBbenchmark)), [return impatience](#RIC) was necessary for existence of a non-degenerate solution.
It is surprising, therefore, that in the presence of uncertainty, the much weaker [weak return impatience](#WRIC) is sufficient for nondegeneracy (assuming that [finite value of autarky](#FVAC) holds).
Given [finite value of autarky](#FVAC), we can derive the features the problem must exhibit for [return impatience](#RIC) to fail (that is, $\Rfree < {(\Rfree \DiscFac)}^{1/\CRRA}$) (given that growth impatience holds) as follows:

(eq-RICimplies)=
$$
  \begin{aligned}
    \Rfree   & < {(\Rfree \DiscFac)}^{1/\CRRA} ~ < ~ {(\Rfree {(\PermGroFac \uInvEuPermShk)}^{\CRRA-1})}^{1/\CRRA}
    \\ \Rightarrow \Rfree   & < {(\Rfree/\PermGroFac)}^{1/\CRRA}\PermGroFac \uInvEuPermShk^{1-1/\CRRA}
    \\  \qquad\qquad\qquad \Rightarrow  \Rfree/\PermGroFac  & < \uInvEuPermShk
  \end{aligned}$$

but since $\uInvEuPermShk < 1$ (for $\CRRA>1$ and non-degenerate $\permShk$), this requires $\Rfree/\PermGroFac < 1$.
Thus, given [finite value of autarky](#FVAC), [return impatience](#RIC) can fail only if human wealth is unbounded and [growth impatience](#GICRaw) holds.[^42]

As in the perfect foresight constrained problem, unbounded limiting human wealth here does not lead to a degenerate limiting consumption function (finite human wealth is not required for Theorem [](#Sufficient-Conditions-For-non-degenerate-Solution)).
But, from equation [](#eq-PFMPCminInv) and the discussion surrounding it, an implication of the failure of [return impatience](#RIC) is that $\lim\limits_{m \rightarrow \infty} \usual{\cFunc}^{\prime}(\mNrm) = 0$.
Thus, interestingly, in this case (unavailable in the perfect foresight unconstrained) model the presence of uncertainty both permits unlimited human wealth (in the $n\rightarrow\infty$ limit) and at the same time prevents unlimited human wealth from resulting in (limiting) infinite consumption (at any finite $\mNrm$).
Intuitively, the utility-imposed ‘natural constraint’ that arises from the possibility of a zero income event prevents infinite borrowing and at the same time allows infinite human wealth to prevent patience from resulting, as it does under other conditions, in the degenerate $\usual{\cFunc}(\mNrm)=0$ as the terminal period recedes.
Thus, in presence of uncertainty of the kind we assume, pathological patience (which in the perfect foresight model results in a limiting consumption function of $\usual{\cFunc}(\mNrm)=0$) plus unbounded human wealth (which the perfect foresight model prohibits because it leads to a limiting consumption function $\usual{\cFunc}(\mNrm)=\infty$ for any finite $\mNrm$) combine to yield a unique finite limiting (as $n \rightarrow \infty$) level of consumption and MPC for any finite value of $\mNrm$.

Note the close parallel to the conclusion in the perfect foresight liquidity constrained model in the case where [return impatience](#RIC) fails (Case 3 in Section [](#subsec-PFCon)).
There, too, the tension between infinite human wealth and pathological patience was resolved with a non-degenerate consumption function whose limiting MPC was zero.[^43]

(When-the-RIC-Holds)=

#### Case 2: Return impatience holds and growth impatience holds with finite human wealth 

This is the benchmark case we presented at the start of the Section.
If [return impatience](#RIC) and [finite human wealth](#ass-FHWC) both hold, a perfect foresight solution exists (Section [](#subsec-PFBbenchmark)).
As $\mNrm \rightarrow \infty$ the limiting $\cFunc$ and $\vFunc$ functions become arbitrarily close to those in the perfect foresight model, because human wealth pays for a vanishingly small portion of spending (Section [](#subsubsec-cFuncBounds)).

(PFFVAF)=

#### Case 3: Return impatience holds and growth impatience holds with infinite human wealth 

The more exotic case is where [finite human wealth](#ass-FHWC) fails but both [growth impatience](#GICRaw) and [return impatience](#RIC) also hold.
In the unconstrained perfect foresight model, this is the degenerate case with limiting $\bar{\cFunc}(\mNrm)=\infty$.
Here, [infinite human wealth](#ass-FHWC) and [finite value of autarky](#FVAC) implies that [(perfect foresight) finite value of autarky](#PFFVAC) holds and that $\APFac < \PermGroFac$.
To see why, traverse Figure [](#fig-Inequalities) clockwise from $\APFac$ by imposing [perfect foresight finite value of autarky](#PFFVAC) to reach the [PF-FVAF](#PFFVAF) node.
Because the bottom arrow pointing to the right, connecting the $\Rfree$ and [perfect foresight finite value of autarky](#PFFVAC) nodes, imposes the failure of finite human wealth (and here we are assuming that condition holds), we can reverse the bottom arrow and traverse the resulting clockwise path from FVAC to see that

$$\begin{gathered}\begin{aligned}
  & \APFac < {(\Rfree/\PermGroFac)}^{1/\CRRA}\PermGroFac \Rightarrow  \APFac < \PermGroFac
\end{aligned}\end{gathered}$$

where the transition from the first to the second lines is justified because failure of [finite human wealth](#ass-FHWC) implies $\Rightarrow {(\Rfree/\PermGroFac)}^{1/\CRRA}<1$.
So, under [return impatience](#RIC) and [finite human wealth](#ass-FHWC), we must have [growth impatience](#GICRaw).

(InvEPermShkEInv)=

However, we are not entitled to conclude that [strong growth impatience](#GICMod) holds: $\APFac < \PermGroFac$ does not imply $\APFac < \InvEPermShkInv \PermGroFac$ where $\InvEPermShkInv<1$.

We have now established the principal points of comparison between the perfect foresight solutions and the solutions under uncertainty; these are codified in the remaining parts of Tables [](#Factors-Defined-And-Compared) and [](#Required).

(Factors-Defined-And-Compared)=


\|c\|c\|
Perfect Foresight Versions & Uncertainty Versions  
  
$\PermGroFac/\Rfree < 1$ & $\PermGroFac/\Rfree < 1$  
&  
&  
&  
&  
  
$\APFac < 1$ & $\APFac < 1$  
&  
&  
&  
&  
$\cLvl_{t+1} < \cLvl_{t}$ & $\displaystyle \lim_{m_{t} \rightarrow \infty} \Ex_{t} [\cLvl_{t+1}] < \cLvl_{t}$  
&  
  
&  
$\APFac/\Rfree < 1$ & $\pZero^{1/\CRRA}\APFac/\Rfree < 1$  
&  
&  
&  
&  
&  
$\cFunc^{\prime}(m) = 1-\APFac/\Rfree < 1$ & $\cFunc^{\prime}(m) < 1-\pZero^{1/\CRRA}\APFac/\Rfree < 1$  
&  
  
&  
$\APFac/\PermGroFac < 1$ & $\APFac\Ex[\permShk^{-1}]/\PermGroFac < 1$  
&  
&  
&  
&  
& $\displaystyle \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[\mNrm_{t+1}/\mNrm_{t}] = \GPFacMod$  
&  
  
&  
$\beta \PermGroFac^{1-\CRRA} < 1$ & $\beta \PermGroFac^{1-\CRRA}\Ex[\permShk^{1-\CRRA}] < 1$  
equivalently $\APFac  < \Rfree^{1/\CRRA}\PermGroFac^{1-1/\CRRA}$ &  
&  
&  
&  
&  

:::{table} Sufficient Conditions for Nondegenerate$^{\ddagger}$ Solution
:name: Required

| Consumption Model(s) | Conditions | Comments |
|:---|:---|:---|
| $\bar{\cFunc}(m)$: PF Unconstrained | RIC, FHWC$^{\circ}$ | RIC$\Rightarrow |\vFunc(\mNrm)|< \infty$; FHWC$\Rightarrow 0 < |\vFunc(\mNrm)|$ |
| $\underline{\cFunc}(m)=\MPCmin \mNrm$ |  | PF model with no human wealth ($h=0$) |
|  |  |  |
| [Section [](#subsubsec-PFUncon):](#Unconstrained-Solution) |  | RIC prevents  $\bar{\cFunc}(\mNrm)=\underline{\cFunc}(\mNrm)=0$ |
| [Section [](#subsubsec-PFUncon):](#Unconstrained-Solution) |  | FHWC prevents $\bar{\cFunc}(\mNrm)=\infty$ |
| Eq [](#eq-FHWCandPFFVACimplyRIC) in [Appendix [](#subsec-PFBProofs)](#subsec-PFBProofs): |  | PF-FVAC+FHWC $\Rightarrow$ RIC |
| Eq [](#eq-GICandFHWCimplyPFFVAC) in [Appendix [](#subsec-PFBProofs)](#subsec-PFBProofs): |  | \+FHWC $\Rightarrow$ PF-FVAC |
| $\cnstr{\cFunc}(m)$: PF Constrained | , RIC | FHWC holds $(\PermGroFac < \APFac < \Rfree \Rightarrow \PermGroFac < \Rfree)$ |
| [Section [](#subsec-PFCon):](#PF-Constrained-Solution) |  | $\cnstr{\cFunc}(\mNrm)=\bar{\cFunc}(\mNrm)$ for $\mNrm > \mNrm_{\#} < 1$ |
|  |  | ( would yield $\mNrm_{\#}=0$ so $\cnstr{\cFunc}(\mNrm)=0$) |
| 2-3 | ,RIC | $\lim_{\mNrm \rightarrow \infty} \cnstr{\cNrm}(\mNrm)=\bar{\cNrm}(\mNrm), \lim\limits_{\mNrm \rightarrow \infty} \cnstr{\MPCFunc}(\mNrm)=\MPCmin$ |
|  |  | kinks where horizon to $b=0$ changes$^{\ast}$ |
| 2-3 | , | $\lim\limits_{\mNrm \rightarrow \infty}  \cnstr{\MPCFunc}(\mNrm)=0$ |
|  |  | kinks where horizon to $b=0$ changes$^{\ast}$ |
| $\usual{\cFunc}(\mNrm)$: [Friedman/Muth](#GICTheorySetup) | Section [](#subsubsec-cFuncBounds) & [](#subsubsec-eventuallyCauchy) | $\underline{\cFunc}(\mNrm) < \usual{\cFunc}(\mNrm) < \bar{\cFunc}(\mNrm)$ |
|  |  | $\underline{\vFunc}(\mNrm) < \usual{\vFunc}(\mNrm) < \bar{\vFunc}(\mNrm)$ |
| 2-3 | FVAC, WRIC | Sufficient for Contraction |
| Section [](#subsec-TheModelUncertainty): |  | WRIC is weaker than RIC |
| Figure [](#fig-Inequalities): |  | FVAC is stronger than PF-FVAC |
| Section [](#subsubsec-casesUC): Case 3 |  | \+RIC $\Rightarrow$$, \lim\limits_{\mNrm \rightarrow \infty} \usual{\MPCFunc}(\mNrm)=\MPCmin$ |
| Section [](#subsubsec-casesUC): Case 1 |  | $\Rightarrow$$, \lim\limits_{\mNrm \rightarrow \infty} \usual{\MPCFunc}(\mNrm)=0$ |
| 3-3 |  | “Buffer Stock Saving” Conditions |
| Theorem [](#thm-target): |  | $\Rightarrow  \exists\phantom{~}\mBalLvl \phantom{~}\text{s.t.}\phantom{~} 0 < \mBalLvl < \infty$ |
| Theorem [](#thm-MSSBalExists): |  | GIC-Mod $\Rightarrow \exists \phantom{~} \mTrgNrm \phantom{~} \text{s.t.}\phantom{~} 0 < \mTrgNrm < \infty$ |
|  |  |  |

:::


$^{\ddagger}$For feasible $\mNrm$ satisfying $0 < \mNrm < \infty$, a nondegenerate limiting consumption function defines a unique optimal value of $\cNrm$ satisfying $0 < \cNrm(m) < \infty$; a nondegenerate limiting value function defines a corresponding unique value of $-\infty < \vFunc(\mNrm) < 0$ .  
  $^{\circ}$RIC, FHWC are necessary as well as sufficient for the perfect foresight case.  $^{\ast}$That is, the first kink point in $\cNrm(\mNrm)$ is $\mNrm_{\#}$ s.t.
for $\mNrm < \mNrm_{\#}$ the constraint will bind now, while for $\mNrm > \mNrm_{\#}$ the constraint will bind one period in the future.
The second kink point corresponds to the $\mNrm$ where the constraint will bind two periods in the future, etc.  
  $^{\ast\ast}$In the Friedman/Muth model, the RIC+FHWC are sufficient, but *not* necessary for nondegeneracy

(Conclusions)=

# Conclusions 

Numerical solutions to optimal consumption problems, in both life cycle and infinite-horizon contexts, have become standard tools since the first reasonably realistic models were constructed in the late 1980s.
One contribution of this paper is to show that finite-horizon (‘life cycle’) versions of the simplest such models, with assumptions about income shocks (transitory and permanent) dating back to [(Friedman, 1957)](#cite-friedmanATheory) and standard specifications of preferences — and without plausible (but computationally and mathematically inconvenient) complications like liquidity constraints — have attractive properties (like continuous differentiability of the consumption function, and analytical limiting MPC’s as resources approach their minimum and maximum possible values).

The main focus of the paper, though, is on the limiting solution of the finite-horizon model as the time horizon approaches infinity.
This simple model has other appealing features: A [‘Finite Value of Autarky’](#FVAC) condition guarantees convergence of the consumption function, under the mild additional requirement of a [‘Weak Return Impatience Condition’](#WRIC) that will never bind for plausible parameterizations, but provides intuition for the bridge between this model and models with explicit liquidity constraints.
The paper also provides a roadmap for the model’s relationships to the perfect foresight model without and with constraints.
The constrained perfect foresight model provides an upper bound to the consumption function (and value function) for the model with uncertainty, which explains why the conditions for the model to have a non-degenerate solution closely parallel those required for the perfect foresight constrained model to have a non-degenerate solution.

The main use of infinite-horizon versions of such models is in heterogeneous-agent macroeconomics.
The paper articulates intuitive ‘Growth Impatience Conditions’ under which populations of such agents, with Blanchardian (tighter) or Modiglianian (looser) mortality will exhibit balanced growth.
Finally, the paper provides the analytical basis for many results about buffer-stock saving models that are so well understood that even without analytical foundations researchers uncontroversially use them as explanations of real-world phenomena like the cross-sectional pattern of consumption dynamics in the Great Recession.

(Appendices)=

# Appendix for Section [](#sec-Theory) 

(sec-ApndxConcaveCFunc)=

## Recovering the Non-Normalized Problem 

(sec-recoverLevels)=

Letting nonbold variables be the boldface counterpart normalized by $\permLvl_{t}$ (as with $\mNrm=\mLvl/\permLvl$), consider the problem in the second-to-last period:
(eq-vBold)=
$$
  \begin{aligned}
    \vFuncLvl_{T-1}(\mLvl_{T-1},\permLvl_{T-1})
    & =  \max_{0< \cNrm_{T-1}< \mNrm_{T-1}}~
    \uFunc(\permLvl_{T-1}\cNrm_{T-1}) + \DiscFac  \Ex_{t}[\uFunc(\permLvl_{T}{\mNrm}
    _{T})]  \\
    & = \permLvl_{T-1}^{1-\CRRA}
    \left\{\max_{0<\cNrm_{T-1}\leq \mNrm_{T-1}}~ \uFunc(\cNrm_{T-1}) + \DiscFac \Ex_{t}[ \uFunc( {\PermGroFacRnd}_{T}
      {\mNrm}_{T}) ] \right\}.
  \end{aligned}$$

(The-Related-Problem)=

Since $\vFunc_{T}(\mNrm_{T}) = \uFunc(\mNrm_{T})$, defining $\vFunc_{T-1}(\mNrm_{T-1})$ from Problem  [](#eq-veqnNrmRecBellman), we obtain:
$$\begin{aligned}
  \vFuncLvl_{T-1}(\mLvl_{T-1},\permLvl_{T-1})  & = \permLvl_{T-1}^{1-\CRRA} \vFunc_{T-1}(\underbrace{\mLvl_{T-1}/\permLvl_{T-1}}_{=\mNrm_{T-1}}).
\end{aligned}$$

This logic induces to earlier periods; if we solve the normalized one-state-variable problem [](#eq-veqnNrmRecBellman), we will have solutions to the original problem for any $t<T$ from:
$$\begin{aligned}
  \vFuncLvl_{t}(\mLvl_{t},\permLvl_{t})  & = \permLvl_{t}^{1-\CRRA}\vFunc_{t}(\mNrm_{t}),
  \\ \cLvl_{t}(\mLvl_{t},\permLvl_{t})  & = \permLvl_{t}\cFunc_{t}(\mNrm_{t}).
\end{aligned}$$

## Perfect Foresight Benchmarks 

(subsec-PFBProofs)=


:::{prf:proof} **Proof of Claim [](#claim-PFConspC)**

First we show that if [finite limiting human wealth](#ass-FHWC) (Assumption [](#ass-FHWC)) and [growth impatience](#GICRaw) (Assumption [](#GICRaw)) are both satisfied, [perfect foresight finite value of autarky](#PFFVAC) (Equation [](#PFFVAC)) holds.
In particular, note that:

(eq-GICandFHWCimplyPFFVAC)=
$$
  \begin{aligned}
    \APFac & < \PermGroFac < \Rfree
    \\   \RPFac & < \PermGroFac/\Rfree < {(\PermGroFac/\Rfree)}^{1-1/\CRRA} < 1.
  \end{aligned}$$

The last line above holds because [finite human wealth](#ass-FHWC) implies $0 \leq (\PermGroFac/\Rfree) < 1$ and $\CRRA > 1 \Rightarrow 0 < 1-1/\CRRA < 1$.

Next, we show that if [finite limiting human wealth](#ass-FHWC) is satisfied, [perfect foresight finite value of autarky](#PFFVAC) (Equation [](#PFFVAC)) implies [return impatience](#RIC) (Assumption [](#ass-RIC)).
To see why, divide both sides of the second inequality in Equation [](#PFFVAC) by $\Rfree$, and after some straightforward algebra, arrive at:

(eq-FHWCandPFFVACimplyRIC)=
$$\begin{gathered}\begin{aligned}
    \APFac/\Rfree & < {(\PermGroFac/\Rfree)}^{1-1/\CRRA}  .
  \end{aligned}\end{gathered}$$
Due to [finite limiting human wealth](#ass-FHWC), the RHS above is strictly less than $1$ because $(\PermGroFac/\Rfree) < 1$ (and the RHS is raised to a positive power (because $\CRRA>1$)).

:::

## Properties of the Consumption Function and Limiting MPCs 

(sec-MPCiterproofs)=

For the following, a function with $k$ continuous derivatives is called a $\mathbf{C}^{k}$ function.

(lemm-consC2)=
:::{prf:lemma}
:label: lemm-consC2

Let $t<T$.
If $\vFunc_{t}$ is strictly negative, strictly increasing, strictly concave, $\mathbf{C}^{3}$ and satisfies $\lim\limits_{\mNrm\rightarrow 0}~\vFunc_{t}(\mNrm) =-\infty$, then $\cFunc_{t}$ is $\mathbf{C}^{2}$.

:::

:::{prf:proof}

(BoroCnstNat)=

Start by defining an end-of-period value function $\mathfrak{v}_{t}$ as:

(eq-vfFrackdefn)=
$$
  \mathfrak{v}_{t}(a):=\DiscFac \Ex_{t}\left[{\PermGroFacRnd}_{t+1}^{1-\CRRA}\vFunc_{t+1}\left({\RNrmByGRnd}_{t+1} a+{\tranShkAll}_{t+1}\right) \right], \qquad a\in \mathbb{R}_{++}.$$

Since there is a positive probability that $\tranShkAll_{t+1}$ will
attain its minimum of zero and since ${\RNrmByGRnd}_{t+1}>0$, we will have that $\lim\limits_{\aNrm \rightarrow 0} \mathfrak{v}_{t}(a) = -\infty$.
Moreover, note that
$\mathfrak{v}_{t}(a)$ is real-valued iff $\aNrm>0$.
As such, by Leibniz Rule, $\mathfrak{v}_{t}$ will be $\mathbf{C}^{3}$.

Next, define $\underline{\vFunc}_{t}(\mNrm,\cNrm)$ as:

$$\underline{\vFunc}_{t}(\mNrm,\cNrm):=\uFunc(c)+\mathfrak{v}_{t}(\mNrm-c), \qquad (\mNrm,\cNrm)\in \Reals_{++}.$$

Note that for fixed $\mNrm$, $\cNrm \mapsto \underline{\vFunc}_{t}(\mNrm,\cNrm)$ is $\mathbf{C}^{3}$ on $(0, \mNrm)$ since $\mathfrak{v}_{t}$ and $\uFunc$ are both
$\mathbf{C}^{3}$.
Observe that the value function defined
by Problem [](#eq-veqnNrmRecBellman) can be written as:

$$\begin{gathered}\begin{aligned}
      \vFunc_{t}(\mNrm) & =  \max_{0<\cNrm<\mNrm}~\underline{\vFunc}_{t}(\mNrm,\cNrm), \qquad \mNrm\in \Reals_{++}
    \end{aligned}\end{gathered}$$

where the function $\underline{\vFunc}_{t}$ is real-valued if and only if $0<c<m$.
Furthermore,
$\lim\limits_{c \rightarrow
  0}\underline{\vFunc}_{t}(\mNrm,\cNrm)=\lim\limits_{c\rightarrow m} \underline{\vFunc}_{t}(\mNrm,\cNrm)=-\infty$, $\frac{\partial ^{2}\underline{\vFunc}_{t}(\mNrm,\cNrm)}{\partial c^{2}}
<0$, $\lim\limits_{\cNrm \rightarrow 0}\frac{\partial \underline{\vFunc}_{t}(\mNrm,\cNrm)}{\partial c}
=+\infty$, and $\lim\limits_{\cNrm\rightarrow m} \frac{\partial \underline{\vFunc}_{t}(\mNrm,\cNrm)}{
  \partial c}=-\infty$.

Letting $\underline{\vFunc}_{t}(\mNrm,0) = -\infty$ and $\underline{\vFunc}_{t}(\mNrm,\mNrm) = -\infty$, consider that $\cFunc_{t}(\mNrm)$ is given by:

$$\begin{gathered}\begin{aligned}
      \cFunc_{t}(\mNrm)  & = \underset{0<c<m}{\arg \max }~\underline{\vFunc}_{t}(\mNrm,\cNrm)= \underset{0\leq c \leq m}{\arg \max }~\underline{\vFunc}_{t}(\mNrm,\cNrm)
    \end{aligned}\end{gathered}$$
where the maximizer exists, is unique and an interior solution.
As such, note that $\cFunc_{t}$ satisfies the first order condition:

(eq-uprimcFOC)=
$$
  \uFunc^{\prime }(\cFunc_{t}(\mNrm))=\mathfrak{v}_{t}^{\prime }(\mNrm-\cFunc_{t}(\mNrm)).$$

By the Implicit Function Theorem, $\cFunc_{t}$ is continuous and differentiable and:

(eq-derivativeConsFunc)=
$$\begin{gathered}\begin{aligned}
      \cFunc_{t}^{\prime }(\mNrm)  & = \frac{\mathfrak{v}_{t}^{\prime \prime }({\aFunc}_{t}(\mNrm))  }{\uFunc^{\prime \prime }(\cFunc_{t}(\mNrm))+\mathfrak{v}_{t}^{\prime \prime }({\aFunc}_{t}(\mNrm))},
    \end{aligned}\end{gathered}$$

where the function $\aFunc_{t}$ is defined by the evaluation $\aFunc_{t}(\mNrm) = m- \cFunc_{t}(\mNrm)$.
Since both $\uFunc$ and $\mathfrak{v}_{t}$ are
three times continuously differentiable and $\cFunc_{t}$ is continuous, the RHS of the above equation is continuous and we can conclude that
$\cFunc_{t}^{\prime }$ is continuous and $\cFunc_{t}$ is in $\mathbf{C}^{1}$.

Finally, $\cFunc_{t}^{\prime }(\mNrm)$ is differentiable because
$\mathfrak{v}_{t}^{\prime \prime }$ is $\mathbf{C}^{1}$, $\cFunc_{t}(\mNrm)$
is $\mathbf{C}^{1}$ and $\uFunc^{\prime \prime
}(\cFunc_{t}(\mNrm))+\mathfrak{v}_{t}^{\prime \prime }\left( {\aFunc}_{t}(\mNrm)\right)
<0$.
The second derivative $\cFunc_{t}^{\prime \prime }(\mNrm)$ will then be given by:

$$\cFunc_{t}^{\prime \prime }(\mNrm)=\frac{{\aFunc}_{t}^{\prime }(\mNrm)\mathfrak{v}_{t}^{\prime \prime
      \prime }({\aNrm}_{t})\left[ \uFunc^{\prime \prime }(c_{t})+\mathfrak{v}_{t}^{\prime \prime }({\aNrm}_{t})
    \right] -\mathfrak{v}_{t}^{\prime \prime }({\aNrm}_{t})\left[ \cFunc_{t}^{\prime }(\mNrm)\uFunc^{\prime \prime
        \prime }(c_{t})+{\aFunc}_{t}^{\prime }(\mNrm)\mathfrak{v}_{t}^{\prime \prime \prime }({\aNrm}_{t})\right] }{
    {\left[ \uFunc^{\prime \prime }(c_{t})+\mathfrak{v}_{t}^{\prime \prime }({\aNrm}_{t})\right]}^{2}},$$

where $\aNrm_{t} = \aFunc_{t}(\mNrm)$ in the equation above.
Since $\mathfrak{v}_{t}^{\prime \prime }({\aFunc}_{t}(\mNrm))$ is continuous,
$\cFunc_{t}^{\prime \prime }(\mNrm)$ is also continuous.

:::

(prop-vfc3)=
:::{prf:property}
:label: prop-vfc3

For each $t$, $\vFunc_{t}$ is strictly negative, strictly increasing, strictly concave, $\mathbf{C}^{3}$ and satisfies $\lim\limits_{\mNrm\rightarrow 0}~\vFunc_{t}(\mNrm) =-\infty$.

:::

:::{prf:proof}

We will say a function is ‘nice’ if it satisfies the properties stated by the Proposition.
Assume that for some $t+1$, $\vFunc_{t+1}$ is nice.
Our objective is to show that this
implies $\vFunc_{t}$ is also nice; this is sufficient to establish that
$\vFunc_{t-n}$ is nice by induction for all $n > 0$ because $\vFunc_{T}(\mNrm)
=\uFunc(\mNrm)$ and $\uFunc$, where $\uFunc(\mNrm)=\mNrm^{1-\CRRA}/(1-\CRRA)$, is nice by inspection.
By Lemma [](#lemm-consC2), if $\vFunc_{t+1}$ is nice, $\cNrm_{t}$ is in $\mathbf{C}^{2}$.
Next, since both $\uFunc$ and $\mathfrak{v}_{t}$ are strictly concave, both
$\cFunc_{t}$ and $\aFunc_{t}$, where $\aFunc_{t}(\mNrm)=\mNrm-\cFunc_{t}(\mNrm)$,
are strictly increasing (Recall Equation [](#eq-derivativeConsFunc)).
This implies that
$\vFunc_{t}(\mNrm)$ is nice, since
$\vFunc_{t}(\mNrm)=\uFunc(\cFunc_{t}(\mNrm))+\mathfrak{v}_{t}({\aFunc}_{t}(\mNrm))$.

:::

(cFunc-is-Twice-Continuously-Differentiable)=

:::{prf:proof} ***Proof for Proposition [](#prop-cfuncprop)***

By Claim [](#prop-vfc3), each $\vFunc_{t}$ is strictly negative, strictly increasing, strictly concave, $\mathbf{C}^{3}$ and satisfies $\lim\limits_{\mNrm\rightarrow 0}~\vFunc_{t}(\mNrm) =-\infty$.
As such, apply Lemma [](#lemm-consC2) to conclude that $\cFunc_{t}$ is in $\mathbf{C}^{2}$.
To see that $\cFunc_{t}$ is strictly increasing, note [](#eq-derivativeConsFunc).
To see that $\cFunc_{t}$ is strictly concave, see Theorem 1.
in [(Carroll and Kim{}ball, 1996)](#cite-ckConcavity).

:::

:::{prf:proof} **Proof of Lemma [](#cFuncBounds) (Limiting MPCs)**

*Part (1.): Minimal MPCs*

Fix any $t$ and for any $\mNrm_{t}$ with $\mNrm_{t}>0$, we can define $\eFunc_{t}(\mNrm_{t})=\cFunc_{t}(\mNrm_{t})/\mNrm_{t}$ and $\aFunc_{t}(\mNrm_{t})= \mNrm_{t} -\cFunc_{t}(\mNrm_{t})$.
The Euler equation, Equation [](#eq-scaledeuler), can be rewritten as:

(eq-eFuncEuler)=
$$\begin{gathered}\begin{aligned}
 \eFunc_{t}{(\mNrm_{t})}^{-\CRRA}  & = \DiscFac \Rfree \Ex_{t}{\left(\eFunc_{t+1}({\mNrm}_{t+1})\left(\frac{\overbrace{\Rfree \aFunc_{t}(\mNrm_{t})+{\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}}^{={\mNrm}_{t+1} \PermGroFacRnd_{t+1}}}{\mNrm_{t}}\right)\right)}^{-\CRRA }
\end{aligned}\end{gathered}$$

where ${\mNrm}_{t+1} = \RNrmByGRnd_{t+1}(\mNrm_{t} -\cFunc_{t}(\mNrm_{t})) +\tranShkAll_{t+1}$.
The minimal MPC’s are obtained by letting where $\mNrm_{t} \rightarrow \infty$.
Note that $\lim\limits_{\mNrm_{t}\rightarrow \infty} \mNrm_{t+1} = \infty$ almost surely and thus $\lim\limits_{\mNrm_{t}\rightarrow \infty}\eFunc_{t+1}({\mNrm}_{t+1}) = \MPCmin_{t+1}$ almost surely.
Turning to the second term inside the marginal utility on the RHS, we can write:

$$\begin{gathered}\begin{aligned}
\lim_{\mNrm_{t}\rightarrow \infty}\frac{\Rfree \aFunc_{t}(\mNrm_{t})+{\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}}{\mNrm_{t}} &  = \lim_{\mNrm_{t}\rightarrow \infty}\frac{\Rfree \aFunc_{t}(\mNrm_{t})}{\mNrm_{t}} + \lim_{\mNrm_{t}\rightarrow \infty}\frac{{\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}}{\mNrm_{t}} \\
            & = \Rfree (1- \MPCmin_{t}) + 0, 
\end{aligned}\end{gathered}$$
since ${\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}$ is bounded.
Thus, we can assert:

$$\lim_{\mNrm_{t}\rightarrow \infty}{\left(\eFunc_{t+1}({\mNrm}_{t+1})\left(\frac{\Rfree \aFunc_{t}(\mNrm)+{\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}}{\mNrm_{t}}\right)\right)}^{-\CRRA } = (\Rfree\MPCmin_{t+1}(1-\MPCmin_{t}))^{-\CRRA},$$

almost surely.
Next, the term inside the expectation operator at Equation [](#eq-eFuncEuler) is bounded above by $\left(\Rfree\MPCmin_{t+1}(1-\MPCmax_{t})\right)^{-\CRRA}$.
Thus, by the Dominated Convergence Theorem, we have:

(eq-eFuncEulerMPCmaxDCT)=
$$
\lim_{\mNrm_{t}\rightarrow \infty}{\DiscFac \Rfree \Ex_{t}\left(\eFunc_{t+1}({\mNrm}_{t+1})\left(\frac{\Rfree \aFunc_{t}(\mNrm_{t})+{\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}}{\mNrm_{t}}\right)\right)}^{-\CRRA } = \DiscFac \Rfree(R\MPCmin_{t+1}(1-\MPCmin_{t}))^{-\CRRA}.$$

Again applying L’Hôpital’s rule to the LHS of Equation [](#eq-eFuncEuler), letting $\lim\limits_{\mNrm \rightarrow \infty} \eFunc_{t}(\mNrm) = \MPCmin_{t}$ and equating limits to the RHS, we arrive at: 
(MPCnvrs)=

$$\MPSmax \MPCmin_{t}  =  (1-\MPCmin_{t}) \MPCmin_{t+1}$$

Thus the minimal marginal propensity to consume satisfies the following recursive formula:
(eq-MPCminInvApndx)=
$$\begin{gathered}\begin{aligned}
 \MPCmin_{t}^{-1}  & = 1+\MPCmin_{t+1}^{-1}\MPSmax,  
\end{aligned}\end{gathered}$$

which implies $\{\MPCmin_{T-n}^{-1}\}_{n=0}^{\infty}$ is an increasing sequence.
Define:
$$\begin{gathered}\begin{aligned}
\MPCmin^{-1} := &\lim_{n \rightarrow \infty} \MPC_{T-n}^{-1}  
\end{aligned}\end{gathered}$$
as the limiting (inverse) marginal MPC.
If [return impatience](#RIC)(Assumption [](#ass-RIC)) does *not* hold, then $\lim\limits_{n \rightarrow \infty} \MPCmin_{T-n}^{-1} = \infty$
and so the limiting MPC is $\MPCmin = 0$.
Otherwise if [return impatience](#RIC) (Assumption [](#ass-RIC)) holds, then $\MPCmin > 0$.

*Part (2.): Maximal MPCs*

The Euler Equation [](#eq-scaledeuler) can be rewritten as:

(eq-eFuncEulerMPCmax)=
$$\begin{gathered}\begin{aligned}
 \eFunc_{t}{(\mNrm_{t})}^{-\CRRA}  & = \DiscFac \Rfree \Ex_{t}\left[{\left(\eFunc_{t+1}({\mNrm}_{t+1})\left(\frac{\overbrace{\Rfree \aFunc_{t}(\mNrm)+{\PermGroFacRnd}_{t+1}{\tranShkAll}_{t+1}}^{={\mNrm}_{t+1} \PermGroFacRnd_{t+1}}}{\mNrm_{t}}\right)\right)}^{-\CRRA }\right] 
\\  & = \phantom{ + }\pNotZero \DiscFac \Rfree \mNrm_{t}^{\CRRA} \Ex_{t}\left[ {\left(\eFunc_{t+1}({\mNrm}_{t+1} ) {\mNrm}_{t+1} \PermGroFacRnd_{t+1}\right)}^{-\CRRA} \big\vert ~ \tranShkAll_{t+1}>0 \right] 
\\ & \qquad  + \pZero  \DiscFac \Rfree^{1-\CRRA} \Ex_{t}\left[{\left(\eFunc_{t+1}(\RNrmByGRnd_{t+1}\aFunc_{t}(\mNrm))\frac{\mNrm_t-\cFunc_{t}(\mNrm)}{\mNrm_{t}}\right)}^{-\CRRA} \big\vert~ \tranShkAll_{t+1} = 0 \right]  
\end{aligned}\end{gathered}$$

Now consider the first conditional expectation in the second line of Equation  [](#eq-eFuncEulerMPCmax).
Recall that if $\tranShkAll_{t+1}>0$, then $\tranShkAll_{t+1} =
\tranShkEmp_{t+1}/\pNotZero$ by Assumption [](#ass-shocks).
Since $\lim\limits_{\mNrm_{t} \rightarrow 0}
\aFunc_{t}(\mNrm_{t}) = 0$,
$\Ex_{t}[{(\eFunc_{t+1}({\mNrm_{t+1}} ){\mNrm_{t+1}} \PermGroFacRnd_{t+1})}^{-\CRRA}~|~\tranShkAll_{t+1}>0]$
is contained in the bounded interval
$[{(\eFunc_{t+1}(\underline{\tranShkEmp}/\pNotZero) \PermGroFac\underline{\permShk}
\underline{\tranShkEmp}/\pNotZero)}^{-\CRRA}, {(\eFunc_{t+1}(\bar{\tranShkEmp}/\pNotZero) \PermGroFac\bar{\permShk}
\bar{\tranShkEmp}/\pNotZero)}^{-\CRRA}]$.
As such, the first term after the second equality above converges to zero as
$\mNrm_{t}^{\CRRA}$ converges to zero.

Turning to the second term after the second equality above, once again apply Dominated Convergence Theorem as noted above at Equation [](#eq-eFuncEulerMPCmaxDCT).
As $\mNrm_{t} \rightarrow 0$,
the expectation converges to $\MPCmax _{t+1}^{-\CRRA
}{(1-\MPCmax _{t})}^{-\CRRA }$.

Equating the limits on the LHS and RHS of Equation [](#eq-eFuncEulerMPCmax), we have $\MPCmax_{t}^{-\CRRA }=\DiscFac
\pZero\Rfree^{1-\CRRA }\MPCmax_{t+1}^{-\CRRA }{(1-\MPCmax
_{t})}^{-\CRRA }$.
Exponentiating by $\CRRA$ on both sides, we can conclude:

(eq-mpcmaxiter)=
$$\begin{gathered}\begin{aligned}
\MPCmax_{t} & = \pZero^{-1/\CRRA} {(\DiscFac
\Rfree)}^{-1/\CRRA}\Rfree(1-\MPCmax _{t})\MPCmax _{t+1} \notag
\end{aligned}\end{gathered}$$

and,

(eq-MPSminDef)=
$$\underbrace{\pZero^{1/\CRRA}\overbrace{{\Rfree}^{-1}{(\DiscFac
    \Rfree)}^{1/\CRRA}}^{\RPFac}}_{\equiv \MPSmin} \MPCmax_{t}  = (1-\MPCmax _{t})\MPCmax _{t+1} $$

The equation above yields a recursive formula for the maximal marginal propensity to consume after some algebra:

(eq-MPCmaxInvApndxIter)=
$$\begin{gathered}\begin{aligned}
  {(\MPSmin \MPCmax_{t})}^{-1}  & = {(1-\MPCmax_{t})}^{-1}\MPCmax_{t+1}^{-1}  \notag
\\ \Rightarrow \MPCmax_{t}^{-1}(1-\MPCmax_{t})  & = \MPSmin \MPCmax_{t+1}^{-1}   \notag
\\ \Rightarrow  \MPCmax_{t}^{-1}  & = 1+\MPSmin \MPCmax_{t+1}^{-1} 
\end{aligned}\end{gathered}$$

As noted in the main text, we need [weak return impatience](#WRIC)(Assumption [](#WRIC)) for this to be a convergent sequence:
(eq-WRICapndx)=
$$\begin{gathered}\begin{aligned}
  0 \leq & ~\pZero^{1/\CRRA} \RPFac < 1 ,
\end{aligned}\end{gathered}$$

Since $\MPCmax_{T}=1$, iterating [](#eq-MPCmaxInvApndxIter) backward to
infinity, we obtain:
(eq-MPCmaxDef)=
$$\begin{gathered}\begin{aligned}
\lim_{n\rightarrow\infty}\MPCmax_{T-n} 
& = \MPCmax \equiv 1-\pZero^{1/\CRRA}\RPFac  
\end{aligned}\end{gathered}$$

:::

(It-Is-A-Contraction-Mapping)=

## Existence of Limiting Solutions 

(sec-Tcontractionmapping)=

We state Boyd’s contraction mapping Theorem (Boyd,1990) for completeness.

(thm-Boyd)=
:::{prf:theorem} Boyd’s Contraction Mapping
:label: thm-Boyd

Let $\mathbb{B}:\mathcal{C}_{\boundFunc }\left( S,Y\right)
  \rightarrow \mathcal{C}_{\boundFunc }\left(S,Y\right)$ with $S\subset \Reals$ and $Y\subset \Reals$.

If,

1.  the operator $\mathbb{B}$ is non-decreasing, i.e. $\xFunc \leq \yFunc \Rightarrow\mathbb{B}{\xFunc } \leq \mathbb{B}{\yFunc}$,

2.  we have $\mathbb{B}\mathbf{0}\in ~ \mathcal{C}_{\boundFunc }\left(S,Y\right)$, where $\mathbf{0}$ is the null vector,

3.  there exists $\alpha$ with $0 < \alpha < 1$ such that for all $\lambda$ with $\lambda > 0$, we have:
    $$\mathbb{B}({\xFunc } +\lambda\boundFunc ) \leq \mathbb{B}{\xFunc } +\lambda\alpha \boundFunc,$$

then $\mathbb{B}$ defines a contraction with a unique fixed point.

:::

(claim-MPCMAXKleq1)=
:::{prf:property}
:label: claim-MPCMAXKleq1

If [weak return impatience](#WRIC) (Assumption [](#WRIC)) holds, then there exists $k$ such that for all $0\leq\MPCmaxInf\leq \MPCmax_{T-k}$, we have:

(eq-MPCMAXKleq1)=
$$
  \pZero \DiscFac {(\Rfree (1-\MPCmaxInf))}^{1-\CRRA}   < 1$$

:::

:::{prf:proof}

By straightforward algebra and Equation [](#eq-MPCmaxDefn) from the main text, we have:

$$\begin{gathered}\begin{aligned}
\pZero \DiscFac {(\Rfree (1-\MPCmax))}^{1-\CRRA}  & = \pZero\DiscFac\Rfree^{1-\CRRA}{\left(\pZero^{1/\CRRA}\frac{{(\Rfree\DiscFac)}^{1/\CRRA}}{\Rfree}\right)}^{1-\CRRA} \\\notag
& = \pZero^{1/\CRRA}\frac{{(\Rfree\DiscFac)}^{1/\CRRA}}{\Rfree} <1 \notag,
\end{aligned}\end{gathered}$$

where the inequality holds by [weak return impatience](#WRIC) (Assumption [](#WRIC)).
Finally, the expression $\MPCmaxInf\mapsto \pZero \DiscFac {(\Rfree (1-\MPCmaxInf))}^{1-\CRRA}$ is continuous and increasing in $\MPCmaxInf$, and we have $1>\bar{\kappa}>0$ and $\MPCmax_{T-n} \rightarrow \MPCmax$ as $n\rightarrow\infty$.
As such, there exists $k$ such that $\pZero \DiscFac {(\Rfree (1-\MPCmax_{T-k}))}^{1-\CRRA}<1$ and Equation [](#eq-MPCMAXKleq1) holds for all $\MPCmaxInf\leq \MPCmax_{T-n}$.

:::

(rem-shnkrdef)=
:::{prf:remark}
:label: rem-shnkrdef

By the [finite value of autarky](#FVAC) (Assumption [](#FVAC)) and for $k$ large enough, fix $\Shrinker$ such that:

(eq-shnkrdef)=
$$
\Shrinker = \max\{\pZero \DiscFac {(\Rfree (1-\MPCmax_{k}))}^{1-\CRRA},\beta\Ex\PermGroFacRnd^{1-\CRRA}\}<1$$

Note that this implies

(eq-shrnkrCond)=
$$
\Shrinker(1- \Shrinker^{-1}\DiscFac \Ex\PermGroFacRnd^{1-\CRRA })>0.$$

We define the constant $\zeta$ as follows:

(eq-Mbarddef)=
$$
\zeta = \frac{\DiscFac \Ex \PermGroFacRnd^{1-\CRRA }\pNotZero^{\CRRA}\underline{\tranShkEmp}^{1-\CRRA}}{\Shrinker(1- \Shrinker^{-1}\DiscFac \Ex \PermGroFacRnd^{1-\CRRA })},$$

and the bounding function, $\boundFunc$, as follows $\boundFunc(x) = \zeta +  x^{1-\CRRA}$.

:::

(clm-hiraguchi_cont)=
:::{prf:property}
:label: clm-hiraguchi_cont

If $\xFunc\in  \mathcal{C}_{\boundFunc }\left( S,Y\right)$, then $\TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}\in \mathcal{C}_{\boundFunc }\left(\Reals_{++}, \Reals_{+}\right)$.

:::

:::{prf:proof}

By definition, we have

$$\begin{gathered}\begin{aligned}
  \TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}(\mNrm_{t}) & = \underset{\cNrm_{t} \in
                                            [\MPCminInf \mNrm_{t}, \MPCmaxInf \mNrm_{t}]
                                            }\max \left\{
                                            \uFunc(c_{t})+\DiscFac \Ex\left[ {\PermGroFacRnd}^{1-\CRRA }{\mathfrak{\xFunc}}
                                            \left( {\mNrm}_{t+1}\right) \right] \right\}, \qquad \mNrm_{t}\in \Reals_{++}  
\end{aligned}\end{gathered}$$

where ${\mNrm}_{t+1} = \RNrmByGRnd\left(\mNrm_{t} - \cNrm_{t}\right) + \tranShkAll$.

First we verify that the mapping $\cNrm_{t}\mapsto \Ex\left[ {\PermGroFacRnd}^{1-\CRRA }{\mathfrak{\xFunc}}
                                            \left( {\mNrm}_{t+1}\right) \right]$, which we denote as $\gFunc$, is continuous.
To proceed define the mapping $\tilde{\gFunc}\colon \Reals_{++}\times\Omega\rightarrow \Reals$ by $\cNrm, \omega \mapsto\left[ {\PermGroFacRnd}(\omega)^{1-\CRRA }{\mathfrak{\xFunc}}
                                            \left( \RNrmByGRnd(\omega)\left(\mNrm_{t} - \cNrm_{t}\right) + \tranShkAll(\omega)\right) \right]$ and the mapping $\gFunc\colon \Reals_{++}\times[\permShkIndMin,\permShkIndMax]\times [0,\Max{\tranShkEmp}] \rightarrow \Reals$ by $\cNrm, \permShk,\tranShkAll \mapsto\left[ {\PermGroFacRnd}^{1-\CRRA }{\mathfrak{\xFunc}}
                                            \left( \RNrmByGRnd\left(\mNrm_{t} - \cNrm_{t}\right) + \tranShkAll\right) \right]$.
Fix $\cNrm$ and note that for any compact interval $[\bar{\cNrm},\underline{\cNrm}]$ such that $\cNrm\in [\bar{\cNrm},\underline{\cNrm}]\subset \Reals_{++}$, $\cNrm\in \Reals_{++}$, $\gFunc(\cNrm,\bullet,\bullet)$ is continuous on $[\bar{\cNrm},\underline{\cNrm}]\times[\permShkIndMin,\permShkIndMax]\times [0,\Max{\tranShkEmp}]$.
Thus, $\gFunc$ is bounded above and below by $\bar{\Xi}$ and $\underline{\Xi}$ for any $\cNrm\in [\bar{\cNrm},\underline{\cNrm}]$ (where $\bar{\Xi}$ and $\underline{\Xi}$ do not depend on $\cNrm$).
To show continuity of $\Ex \tilde{\gFunc}(\cNrm,\bullet)$ for any $\cNrm \in \Reals_{++}$, note there exists $[\bar{\cNrm},\underline{\cNrm}]$ such that $\cNrm\in [\bar{\cNrm},\underline{\cNrm}]\subset \Reals_{++}$.
Thus consider $\{\cNrm^{i}\}_{i}$, let $\cNrm^{i}\rightarrow \cNrm$ and we can assume $\cNrm^{i}\in [\bar{\cNrm},\underline{\cNrm}]$ for all $i$.
Since for each $i$, $\tilde{\gFunc}(\cNrm^{i},\omega)$ is bounded above and below by $\bar{\Xi}$ and $\underline{\Xi}$, by the Dominated Convergence Theorem, we must have $\lim\limits_{i\rightarrow \infty}\Ex \tilde{\gFunc}(\cNrm_{i},\bullet) = \Ex \tilde{\gFunc}(\cNrm,\bullet)$.

Next, by Berge’s Maximum Theorem (Theorem 17.31 in [(Aliprantis and Border, 2006)](#cite-Aliprantis2005)), since the feasibilty correspondence $\mNrm_{t}\mapsto [\MPCminInf \mNrm_{t}, \MPCmaxInf \mNrm_{t}]$ has a closed graph and is and compact valued, $\TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}$ must be continuous.

Finally, to show that $\Vert \TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}\Vert_{\boundFunc}<\infty$.
We have:

$$\begin{gathered}\begin{aligned}
\Vert \TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}\Vert_{\boundFunc} & = \sup_{\mNrm} \left\{\frac{\left| \uFunc(\cFunc(\mNrm)) + \DiscFac \Ex\left[ {\PermGroFacRnd}^{1-\CRRA }{\mathfrak{\xFunc}} \left( {\mNrm^{\nxt}}\right) \right] \right|}{\zeta + \mNrm^{1-\CRRA}}\right\} \\
& \leq  \sup_{\mNrm} \left\{\frac{\left| \frac{\mNrm^{1-\CRRA}}{1-\CRRA} + \DiscFac \Ex\left[ {\PermGroFacRnd}^{1-\CRRA }{\mathfrak{\xFunc}} \left( {\mNrm^{\nxt}}\right) \right] \right|}{\zeta + \mNrm^{1-\CRRA}}\right\} \\ 
& \leq \sup_{\mNrm} \left\{\frac{\frac{\mNrm^{1-\CRRA}}{1-\CRRA}}{\zeta + \mNrm^{1-\CRRA}}\right\} + \sup_{\mNrm} \left\{\frac{\DiscFac \Ex\left[ {\PermGroFacRnd}^{1-\CRRA }{\vert \mathfrak{\xFunc}} \left( {\mNrm}\right)\vert  \right]}{\zeta + \mNrm^{1-\CRRA}}\right\}\\
& <\infty, 
\end{aligned}\end{gathered}$$

where ${\mNrm}^{\nxt} = \RNrmByGRnd\left(\mNrm - \cNrm\right) + \tranShkAll$ and the final inequality follows from the triangle inequality and the fact that $\xFunc$ is $\boundFunc$-bounded.

:::

:::{prf:proof} **Proof of Theorem [](#thm-cmap)**

Fix $k$ such that Equation [](#eq-MPCMAXKleq1) holds.
By Claim [](#clm-hiraguchi_cont), $\TMap^{\MPCminInf, \MPCmaxInf}$ $\TMap^{\MPCminInf, \MPCmaxInf}$ maps from $\mathcal{C}_{\boundFunc}(\Reals_{++},\Reals)$ to $\mathcal{C}_{\boundFunc}(\Reals_{++},\Reals)$.
We now verify conditions (1)-(3) of Boyd’s Theorem ([](#thm-Boyd)).

By definition of $\TMap^{\MPCminInf, \MPCmaxInf}$, we have:
(eq-condition1)=
$$\begin{gathered}\begin{aligned}
  \TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}(\mNrm_{t}) & = \underset{\cNrm_{t} \in
                                            [\MPCminInf \mNrm_{t}, \MPCmaxInf \mNrm_{t}]
                                            }\max \left\{
                                            \uFunc(c_{t})+\DiscFac \Ex\left[ {\PermGroFacRnd}^{1-\CRRA }{\mathfrak{\xFunc}}
                                            \left( {\mNrm}_{t+1}\right) \right] \right\},    
\end{aligned}\end{gathered}$$

where ${\mNrm}_{t+1} = \RNrmByGRnd\left(\mNrm_{t} - \cNrm_{t}\right) + \tranShkAll$.
As such, ${\mathfrak{\xFunc}} \leq {\mathfrak{\yFunc}}$ implies $\TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\xFunc}}(\mNrm_{t}) \leq \TMap^{\MPCminInf, \MPCmaxInf}{\mathfrak{\yFunc}} (\mNrm_{t})$ by inspection.

Condition (2.) requires that $\TMap^{\MPCminInf, \MPCmaxInf}\mathbf{0}\in \mathcal{C}_{\boundFunc}\left(\mathscr{A},\mathscr{B}\right)$.
By definition,
$$\TMap^{\MPCminInf, \MPCmaxInf} \mathbf{0}(\mNrm_{t}) = \max_{\cNrm_{t} \in
    [\MPCminInf \mNrm_{t}, \MPCmaxInf \mNrm_{t}]
  }\left\{ \left( \frac{\cNrm_{t}^{1-\CRRA }}{1-\CRRA }\right) +\DiscFac 0\right\}$$
the solution to which implies
$\TMap^{\MPCminInf, \MPCmaxInf} \mathbf{0}(\mNrm_{t}) = \uFunc(\MPCmaxInf \mNrm_{t})$.
Thus, Condition (2)
will hold if ${(\MPCmaxInf \mNrm_{t})}^{1-\CRRA}$ is $\boundFunc$-bounded, which it is if we use the
bounding function

defined in Remark [](#rem-shnkrdef).

Finally, we turn to condition (3), which requires us to show $\TMap^{\MPCminInf, \MPCmaxInf}({\zFunc} +\lambda\boundFunc
)(\mNrm_{t}) \leq\TMap^{\MPCminInf, \MPCmaxInf}{\zFunc}(\mNrm_{t}) +\lambda \Shrinker
\boundFunc(\mNrm_{t})$ for $0<\Shrinker<1$ and $\lambda>0$.

To proceed, define
$\breve{\cFunc}$ as the consumption
function[^44]
associated with $\TMap^{\MPCminInf, \MPCmaxInf}{\zFunc}$ and $\hat{\cFunc}$ as the consumption function associated with $\TMap^{\MPCminInf, \MPCmaxInf}({\zFunc+\zeta
  \boundFunc})$; using this notation, Condition (3.) can be rewritten as:
$$\begin{aligned}
  \uFunc(\hat{\cFunc})+\DiscFac \Ex {\PermGroFacRnd}^{1-\CRRA }(\zFunc+\zeta \boundFunc)\circ \hat{\mFunc}^{\nxt}  & \leq  \uFunc(\breve{\cFunc})+\DiscFac\Ex {\PermGroFacRnd}^{1-\CRRA }\zFunc\circ\breve{\mFunc}^{\nxt}  + \zeta \Shrinker \boundFunc,
\end{aligned}$$

where $\breve{\mFunc}^{\nxt}(\mNrm) = \RNrmByGRnd(\mNrm - \breve{\cFunc}(\mNrm)) +\tranShkAll$ and $\hat{\mFunc}^{\nxt}(m) = \RNrmByGRnd(m - \hat{\cFunc}(m))+\tranShkAll$.
If we now force the consumer facing $\zFunc$ as the next period value function to consume the amount optimal for the consumer facing $\zFunc+\zeta \boundFunc$, the value for the $\zFunc$ consumer must be weakly lower.
That is,

$$\begin{aligned}
  \uFunc(\hat{\cFunc})+\DiscFac \Ex{\PermGroFacRnd}^{1-\CRRA } \zFunc \circ \hat{\mFunc}^{\nxt}  & \leq \uFunc(\breve{\cFunc})+\DiscFac \Ex {\PermGroFacRnd}^{1-\CRRA }\zFunc\circ\breve{\mFunc}^{\nxt}.                                 
\end{aligned}$$

Thus, condition (3.) will certainly hold under the stronger condition
(eq-reqCondWeak)=
$$\begin{gathered}\begin{aligned}
  \uFunc\circ \hat{\cFunc} +\DiscFac \Ex\PermGroFacRnd^{1-\CRRA } (\zFunc+\lambda \boundFunc) \circ \hat{\mFunc}^{\nxt}  & \leq  \uFunc\circ \hat{\cFunc} + \DiscFac \Ex\PermGroFacRnd^{1-\CRRA } \zFunc\circ\hat{\mFunc}^{\nxt}  + \lambda \Shrinker \boundFunc \notag
  \\ \Leftrightarrow \DiscFac\Ex\PermGroFacRnd^{1-\CRRA }(\zFunc +\lambda \boundFunc) \circ\hat{\mFunc}^{\nxt}  & \leq  \DiscFac \Ex\PermGroFacRnd^{1-\CRRA }\zFunc\circ \hat{\mFunc}^{\nxt}  + \lambda \Shrinker \boundFunc \notag
  \\ \Leftrightarrow  \DiscFac\lambda \Ex\PermGroFacRnd^{1-\CRRA }\boundFunc\circ\hat{\mFunc^{\nxt}}  & \leq  \lambda \Shrinker \boundFunc \notag
  \\ \Leftrightarrow  \DiscFac \Ex\PermGroFacRnd^{1-\CRRA }\boundFunc \circ \hat{\mFunc}^{\nxt}  & \leq  \Shrinker \boundFunc      
\end{aligned}\end{gathered}$$

To show [](#eq-reqCondWeak) holds, recall by Claim [](#claim-MPCMAXKleq1) that $\pZero \DiscFac {(\Rfree (1-\MPCmax_{T-k}))}^{1-\CRRA}   < 1$ for $k$ large enough.
As such, define $\Shrinker$ by Equation [](#eq-shnkrdef) and note that $\pZero \DiscFac {(\Rfree (1-\MPCmax_{k}))}^{1-\CRRA} < \alpha < 1$ and $\alpha\geq \beta\Ex\PermGroFacRnd^{1-\CRRA}$.
Letting $\hat{\aNrm} = \mNrm - \hat{\cFunc}(\mNrm)$, Equation [](#eq-reqCondWeak) will be satisfied if:

$$\begin{aligned}
  \DiscFac \Ex [{\PermGroFacRnd^{1-\CRRA }}{(\hat{\aNrm}\RNrmByGRnd+\tranShkAll)}^{1-\CRRA}]-\Shrinker\mNrm^{1-\CRRA}  & < \alpha\zeta(1-\alpha^{-1}\DiscFac\Ex {\PermGroFacRnd^{1-\CRRA }}),
\end{aligned}$$

which, by imposing [finite value of autarky](#FVAC) (Assumption [](#FVAC)) and Equation [](#eq-shrnkrCond) can be rewritten as:

(eq-KeyCondition)=
$$\begin{gathered}\begin{aligned}
      \zeta >\frac{\DiscFac \Ex\left[\PermGroFacRnd^{1-\CRRA}{(\hat{\aNrm}\RNrmByGRnd +\tranShkAll)}^{1-\CRRA}\right]- \Shrinker\mNrm^{1-\CRRA}}{\Shrinker(1-\alpha^{-1}\DiscFac\Ex {\PermGroFacRnd^{1-\CRRA }})}= \colon\bar{\bar{M}} .
    \end{aligned}\end{gathered}$$

Thus, the proof reduces to showing Equation [](#eq-KeyCondition) holds.
To proceed, consider that the numerator of [](#eq-KeyCondition) is bounded above as follows:

$$\begin{aligned}
      \DiscFac \Ex\left[\PermGroFacRnd^{1-\CRRA}{(\hat{\aNrm}\RNrmByGRnd +\tranShkAll)}^{1-\CRRA}\right]- \Shrinker\mNrm^{1-\CRRA} &= \pNotZero\DiscFac\Ex\left[\PermGroFacRnd^{1-\CRRA }{(\hat{\aNrm}\RNrmByGRnd+\tranShkEmp/\pNotZero)}^{1-\CRRA}\right] \\
      &\quad +\pZero\DiscFac\Ex\left[\PermGroFacRnd^{1-\CRRA }{(\hat{\aNrm}\RNrmByGRnd)}^{1-\CRRA}\right]-\Shrinker\mNrm^{1-\CRRA} \\
      &\leq \pNotZero\DiscFac\Ex\left[\PermGroFacRnd^{1-\CRRA }{((1-\MPCmaxInf)\mNrm\RNrmByGRnd+\tranShkEmp/\pNotZero)}^{1-\CRRA}\right] \\
      &\quad +\pZero\DiscFac\Rfree^{1-\CRRA}{((1-\MPCmaxInf)\mNrm)}^{1-\CRRA}- \Shrinker\mNrm^{1-\CRRA} \\
      &= \pNotZero\DiscFac\Ex\left[\PermGroFacRnd^{1-\CRRA }{((1-\MPCmaxInf)\mNrm\RNrmByGRnd+\tranShkEmp/\pNotZero)}^{1-\CRRA}\right] \\
      &\quad +\mNrm^{1-\CRRA}\left(\underbrace{\pZero \DiscFac {(\Rfree (1-\MPCmaxInf))}^{1-\CRRA}}_{<\Shrinker ~\text{by Claim claim-MPCMAXKleq1}}-\Shrinker \right) \\
      &< \pNotZero\DiscFac\Ex\left[\PermGroFacRnd^{1-\CRRA }{(\underline{\tranShkEmp}/\pNotZero)}^{1-\CRRA}\right] \\ & =\DiscFac\Ex \PermGroFacRnd^{1-\CRRA }\pNotZero^{\CRRA}\underline{\tranShkEmp}^{1-\CRRA} .
\end{aligned}$$

Using Claim [](#claim-MPCMAXKleq1), we have that $\pZero \DiscFac {(\Rfree (1-\MPCmaxInf))}^{1-\CRRA}< \Shrinker$ since $\Shrinker = \max\{\pZero \DiscFac {(\Rfree (1-\MPCmax_{T-k}))}^{1-\CRRA},\beta\Ex\PermGroFacRnd^{1-\CRRA}\}$ and $\MPCmaxInf\leq\MPCmax_{k}$.
We can thus conclude that equation [](#eq-KeyCondition) will hold since we have
$$\begin{gathered}\begin{aligned}
      \zeta \geq \frac{\DiscFac \Ex \PermGroFacRnd^{1-\CRRA }\pNotZero^{\CRRA}\underline{\tranShkEmp}^{1-\CRRA}}{\Shrinker(1- \Shrinker^{-1}\DiscFac \Ex \PermGroFacRnd^{1-\CRRA })}> \bar{\bar{M}}. 
    \end{aligned}\end{gathered}$$

The proof that $\TMap^{\MPCminInf, \MPCmaxInf}$ defines a contraction mapping under the
conditions [](#WRIC) and [](#FVAC) is
now complete.

:::

:::{prf:proof} **Proof of Theorem [](#Sufficient-Conditions-For-non-degenerate-Solution) (continued)**

We next establish the point-wise convergence of consumption the functions $\left\{ \cFunc_{t_{n}}\right\}_{n=0}^{\infty}$ along a sub-sequence.
Fix any $\mNrm\in S$ and consider a convergent subsequence $\{\cFunc_{t_{n(i)}}(\mNrm)\}_{i=0}^{\infty}$ of $\left\{ \cFunc_{t_{n}}(\mNrm) \right\}_{n=0}^{\infty}$.
Let the function $\cFunc$ denote the mapping from $\mNrm$ to the limit of $\{\cFunc_{t_{n(i)}}(\mNrm)\}_{i=0}^{\infty}$.
Since $\cFunc_{t_{n(i)}}(\mNrm)$ solves the time $t_{n(i)}$ finite horizon problem, we have:

$$\begin{aligned}
\uFunc(\cFunc_{t_{n(i)}}(\mNrm)) + & \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc_{t_{n(i)+1}}(\mNrm_{t_{n(i)+1}}) \right] \\ 
& \geq \uFunc(\cNrm) + \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc_{t_{n(i)}+1}(\hat{\mNrm}^{\nxt}) \right], 
\end{aligned}$$

for any $\cNrm \in (0, \MPCmax \mNrm]$, where $\mNrm_{t_{n(i)}+1} = \RNrmByGRnd(\mNrm - \cFunc_{t_{n(i)}}(\mNrm)) + \tranShkAll_{t_{n(i)}+1}$ and $\hat{\mNrm}^{\nxt} = \RNrmByGRnd(\mNrm - \cNrm) + \tranShkAll_{t_{n(i)}+1}$.

Allowing $n(i)$ to tend to infinity, the left-hand side converges to:

$$\uFunc(\cFunc(m)) + \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc(\mNrm^{\nxt}) \right],$$

where $\mNrm^{\nxt} = \RNrmByGRnd(\mNrm - \cFunc(\mNrm)) + \tranShkAll$.
Moreover, the right-hand side converges to:

$$\uFunc(\cNrm) + \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc(\hat{\mNrm}^{\nxt}) \right].$$

Hence, as $n(i)$ tends to infinity, the following inequality is implied:
$$\uFunc(\cFunc(\mNrm)) + \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc(\mNrm^{\nxt}) \right] \geq \uFunc(\cNrm) + \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc(\hat{\mNrm}^{\nxt}) \right].$$

Since the $\cNrm$ above was arbitrary, we have:
(eq-statCbellman)=
$$
\cFunc(\mNrm) \in \underset{\cNrm \in (0, \MPCmax \mNrm]}{\arg \max} \left\{ \uFunc(\cNrm) + \DiscFac \Ex \left[ {\PermGroFacRnd}^{1 - \CRRA} \vFunc(\hat{\mNrm}^{\nxt}) \right] \right\}.$$

Next, since $\cFunc_{t_{n(i)}}\rightarrow \cFunc$ pointwise, and $\vFunc_{t_{n(i)}}\rightarrow \vFunc$ pointwise, we have:

(eq-convgcvftni)=
$$
\vFunc(\mNrm) = \lim_{i\rightarrow \infty}\left[\uFunc(\cFunc_{t_{n(i)}}(\mNrm)) + \DiscFac\Ex\PermGroFacRnd^{1 - \CRRA}\vFunc_{t_{n(i)}+1}(\mNrm_{t_{n(i)}+1})\right] = \uFunc(\cFunc(\mNrm)) + \DiscFac\Ex\PermGroFacRnd^{1 - \CRRA}\vFunc(\mNrm^{\nxt}).$$

where $\mNrm_{t_{n}} = \RNrmByGRnd(\mNrm - \cFunc_{t_{n}}(\mNrm))$ and $\mNrm^{\nxt} = \RNrmByGRnd(\mNrm - \cFunc(\mNrm))$.
The first equality stems form the fact that $\vFunc_{t_{n}}\rightarrow \vFunc$ pointwise, and because pointwise convergence implies pointwise convergence along a sub-sequence.
To see why $\lim
\limits_{i\rightarrow \infty} \uFunc(\cFunc_{t_{n(i)}}(\mNrm)) =   \uFunc(\cFunc(\mNrm))$, note the continuity of $\uFunc$ and the convergence of $\cFunc_{t_{n(i)}}$ to $\cFunc$ point-wise.
Turning to the second inequality, to see why $\lim\limits_{i\rightarrow \infty}\Ex\PermGroFacRnd^{1 - \CRRA}\vFunc_{t_{n(i)}+1}(\mNrm_{t_{n(i)}+1}) = \Ex\PermGroFacRnd^{1 - \CRRA}\vFunc(\mNrm^{\nxt})$, note that $\vFunc_{t_{n(i)}+1}$ converges in the $\boundFunc$-norm, hence converges uniformly over compact sets in $\mathbb{R}_{++}$ (Fact [](#fact-normimpliescompact), Appendix [](#sec-realanalysis)).
Thus, by Fact [](#fact-compactnt) in Appendix [](#sec-realanalysis), $\vFunc_{t_{n(i)}+1}(\mNrm_{t_{n(i)}+1})$ converges almost surely.
Applying Dominated Convergence Theorem gives us $\lim\limits_{i\rightarrow \infty}\Ex\PermGroFacRnd^{1 - \CRRA}\vFunc_{t_{n(i)}+1}(\mNrm_{t_{n(i)}+1}) = \Ex\PermGroFacRnd^{1 - \CRRA}\vFunc(\mNrm^{\nxt})$.

This completes the proof of part (ii) of the Theorem.

The limits at Equation [](#eq-convgcvftni) immediately imply:

$$\vFunc(\mNrm) = \lim_{n\rightarrow \infty}\left[\uFunc(\cFunc_{t_{n}}(\mNrm)) + \DiscFac\Ex\PermGroFacRnd^{1 - \CRRA}\vFunc_{t_{n}+1}(\mNrm_{t_{n}+1})\right] = \uFunc(\cFunc(\mNrm)) + \DiscFac\Ex\PermGroFacRnd^{1 - \CRRA}\vFunc(\mNrm^{\nxt}),$$

since a real valued sequence can have at most one limit.

Finally, applying Fact [](#sec-realanalysis) from Appendix [](#sec-realanalysis), we get $\cFunc_{t_{n}}(\mNrm)\rightarrow  \cFunc(\mNrm)$, thus establishing that $\cFunc_{t_{n}}$ converges point-wise to $\cFunc$.
Since $\vFunc\in \mathcal{C}_{\boundFunc}(\Reals_{++},\Reals)$, we must have that $\cFunc(\mNrm)>0$ for any $\mNrm>0$, allowing us to conclude that $\vFunc$ and $\cFunc$ is a non-degenerate limiting solution.

:::

## Properties of the Converged Consumption Function 

(subsec-Properties)=

Let $\cFunc$ be the limiting non-degenerate consumption function.

(eq-EuelrStatC)=
:::{prf:property}
:label: eq-EuelrStatC

If [weak return impatience](#WRIC) (Assumption [](#WRIC)) holds, then $\cFunc$ satisfies $\cFunc(\mNrm)^{-\CRRA}   = \Rfree \DiscFac \Ex_{t}[ \Rnd{\PermGroFac}_{t+1}^{-\CRRA} \cFunc(\mNrm^{\nxt})^{-\CRRA}]$, where ${\mNrm}^{\nxt} = \RNrmByGRnd(\mNrm -\cFunc(\mNrm)) +\tranShkAll$.

:::

:::{prf:proof}

By Theorem [](#Sufficient-Conditions-For-non-degenerate-Solution), $\cFunc_{T-n}$ converges point-wise to $\cFunc$ as $n\rightarrow \infty$.
Since $\cFunc_{T-n}$ is the optimal consumption function for time $T-n$, $\cFunc_{T-n}(\mNrm)^{-\CRRA}   = \Rfree \DiscFac \Ex_{t}[ \Rnd{\PermGroFac}_{t+1}^{-\CRRA} \cFunc_{T-n+1}(\mNrm_{t+1})^{-\CRRA}]$, where ${\mNrm}_{t+1} = \RNrmByGRnd(\mNrm -\cFunc_{T-n}(\mNrm)) +\tranShkAll$.
Fixing $\mNrm>0$, $\RNrmByGRnd(\mNrm -\cFunc_{T-n}(\mNrm)) +\tranShkAll$ converges almost surely to $\RNrmByGRnd(\mNrm -\cFunc(\mNrm)) +\tranShkAll$.
Making use of the Dominated Converge (see proof of Claim [](#clm-hiraguchi_cont)), $\Rfree \DiscFac \Ex_{t}[ \Rnd{\PermGroFac}_{t+1}^{-\CRRA} \cFunc_{T-n+1}(\mNrm_{t+1})^{-\CRRA}]$ converges to $\Rfree \DiscFac \Ex_{t}[ \Rnd{\PermGroFac}_{t+1}^{-\CRRA} \cFunc(\mNrm^{\nxt})^{-\CRRA}]$.
Since $\cFunc_{T-n}(\mNrm)^{-\CRRA}$ converges to $\cFunc(\mNrm)$ and $\mNrm\in \Reals_{++}$, the result follows.

:::

:::{prf:proof} **Proof of Lemma [](#lemma-MPCBoundsConvg)**

First, we verify $\cFunc$ is concave.
Since [weak return impatience](#WRIC) (Assumption [](#WRIC)) holds, by Theorem [](#Sufficient-Conditions-For-non-degenerate-Solution), $\cFunc_{T-n}\rightarrow \cFunc$ point-wise on $\Reals_{++}$ as $n\rightarrow \infty$.
Moreover, since $\Reals_{++}$ is open, we can apply Theorem 10.8 by [(Rockafellar, 1972)](#cite-Rockafellar1972), which confirms that $\cFunc$ is concave on $\Reals_{++}$.

Next, note that $\cFunc(\mNrm)>0$ on $\Reals_{++}$ (recall Remark [](#remark-cStatStrctPos)).
Thus, we must have that $\frac{\cFunc(\mNrm)}{\mNrm}$ is non-increasing (see Claim [](#claim-rationondec) in Appendix [](#sec-realanalysis)) and since $\cFunc(\mNrm)$ is feasible (Equation [](#eq-statCbellman)), $0 \leq \frac{\cFunc(\mNrm)}{\mNrm}\leq 1$.
Because $\frac{\cFunc(\mNrm)}{\mNrm}$ is non-increasing and bounded above and below on $\Reals_{++}$, we can define $\MPCmaxmax:= \lim\limits_{\mNrm\downarrow 0}\frac{\cFunc(\mNrm)}{\mNrm}$ and $\MPCminmin := \lim\limits_{\mNrm\rightarrow \infty}\frac{\cFunc(\mNrm)}{\mNrm}$ where $0 \leq \MPCminmin \leq \MPCmaxmax\leq 1$.

We fist show $\MPCmaxmax = \MPCmax$ and then show $\MPCminmin = \MPCmin$.
Since $\cFunc$ satisfies the Euler equation by Claim [](#eq-EuelrStatC), we have

(eq-eFuncEulerStat)=
$$\begin{gathered}\begin{aligned}
 \eFunc{(\mNrm)}^{-\CRRA}  & = \DiscFac \Rfree \Ex_{t}{\left(\eFunc({\mNrm})\left(\frac{\overbrace{\Rfree \aFunc(\mNrm)+{\PermGroFacRnd}{\tranShkAll}}^{={\mNrm} \PermGroFacRnd}}{\mNrm}\right)\right)}^{-\CRRA }
\end{aligned}\end{gathered}$$

where ${\mNrm}^{\nxt} = \RNrmByGRnd(\mNrm -\cFunc(\mNrm)) +\tranShkAll$.
The minimal MPC’s are obtained by letting $\mNrm \rightarrow \infty$.
Note that $\lim\limits_{\mNrm_{t}\rightarrow \infty} \mNrm^{\nxt} = \infty$ almost surely and thus $\lim\limits_{\mNrm_{t}\rightarrow \infty}\eFunc_{t+1}({\mNrm}_{t+1}) = \MPCminmin$ almost surely.
Turning to the second term inside the marginal utility on the RHS, we can write

$$\begin{gathered}\begin{aligned}
\lim_{\mNrm\rightarrow \infty}\frac{\Rfree \aFunc(\mNrm)+{\PermGroFacRnd}{\tranShkAll}}{\mNrm_{t}} &  = \lim_{\mNrm \rightarrow \infty}\frac{\Rfree \aFunc(\mNrm)}{\mNrm} + \lim_{\mNrm\rightarrow \infty}\frac{{\PermGroFacRnd}{\tranShkAll}}{\mNrm} \\
            & = \Rfree (1- \MPCminmin) + 0, 
\end{aligned}\end{gathered}$$
since ${\PermGroFacRnd}{\tranShkAll}$ is bounded.
Thus, as $\mNrm$ tends to $\infty$, we have

$$\begin{gathered}\begin{aligned} 
 \lim\limits_{\mNrm\rightarrow \infty}\eFunc{(\mNrm)}^{-\CRRA}  & =  \MPCminmin^{-\CRRA} = \beta\Rfree\MPCminmin^{-\CRRA}\Rfree^{-\CRRA} (1- \MPCminmin) ^{-\CRRA}. 
\end{aligned}\end{gathered}$$

Re-arranging the terms above gives us $\MPCminmin =1-  \APFac/\Rfree =  \MPCmin$ as required.
Finally, analogously following the steps before Equation [](#eq-mpcmaxiter) and noting $\MPCmaxmax = \lim\limits_{\mNrm\downarrow 0}\frac{\cFunc(\mNrm)}{\mNrm}$, we can conclude $\MPCmaxmax  = \pZero^{-1/\CRRA} {(\DiscFac
\Rfree)}^{-1/\CRRA}\Rfree(1-\MPCmaxmax)\MPCmaxmax$.
Whence $\MPCmaxmax = 1- \pZero^{1/\CRRA}\APFac/\Rfree = \MPCmax$.

:::

## The Liquidity Constrained Solution as a Limit 

(sec-LiqConstrAsLimit)=

Formally, suppose we change the description of the problem by making
the following two assumptions:
(eq-liqconstr)=
$$\begin{aligned}
  \pZero   & = 0
  \\  c_{t} & \leq  \mNrm_{t} ,
\end{aligned}$$
and we designate the solution to this consumer’s problem $\cnstr{\cFunc}_{t}(\mNrm)$.
We will henceforth refer to this as the problem of the ‘restrained’ consumer (and, to avoid a common confusion, we will refer to the consumer as ‘constrained’ only in circumstances when the constraint is actually binding).

Redesignate the consumption function that emerges from our original problem for a given fixed $\pZero$ as $\cFunc_{t}(\mNrm;\pZero)$ where we separate the arguments by a semicolon to distinguish between $\mNrm$, which is a state variable, and $\pZero$, which is not.
The proposition we wish to demonstrate is
(eq-RestrEqUnrestr)=
$$\begin{gathered}\begin{aligned}
      \lim_{\pZero \downarrow 0} \cFunc_{t}(\mNrm;\pZero)  & = \cnstr{\cFunc}_{t}(\mNrm).  
    \end{aligned}\end{gathered}$$

We will first examine the problem in period $T-1$, then argue that the desired result propagates to earlier periods.
For simplicity, suppose that the interest, growth, and time-preference factors are $\DiscFac = \Rfree = \PermGroFac = 1$, and there are no permanent shocks, $\permShk=1$; the results below are easily generalized to the full-fledged version of the problem.

The solution to the restrained consumer’s optimization problem can be obtained as follows.
Assuming that the consumer’s behavior in period $T$ is given by $\cFunc_{T}(\mNrm)$ (in practice, this will be $\cFunc_{T}(\mNrm)=m$), consider the unrestrained optimization problem
(eq-vUnconstr)=
$$\begin{gathered}\begin{aligned}
      \cnstr{\aFunc}^{*}_{T-1}(\mNrm)  & = \underset{\aNrm}{\arg \max} \left\{\uFunc(\mNrm-\aNrm) +  \int_{\underline{\tranShkEmp}}^{\bar{\tranShkEmp}} \vFunc_{T}(a+\tranShkEmp) d\CDF_{\tranShkEmp} \right\}. 
    \end{aligned}\end{gathered}$$

As usual, the envelope theorem tells us that $\vFunc_{T}^{\prime}(\mNrm)=\uP(\cFunc_{T}(\mNrm))$ so the expected marginal value of ending period $T-1$ with assets $\aNrm$ can be defined as
$$\begin{gathered}\begin{aligned}
      \cnstr{\mathfrak{v}}_{T-1}^{\prime}(a)  & \equiv  \int_{\underline{\tranShkEmp}}^{\bar{\tranShkEmp}} \uP(\cFunc_{T}(a+\tranShkEmp)) d\CDF_{\tranShkEmp}, \notag
    \end{aligned}\end{gathered}$$
and the solution to [](#eq-vUnconstr) will satisfy
(eq-uPConstr)=
$$\begin{gathered}\begin{aligned}
      \uP(\mNrm-\aNrm)  & =  \cnstr{\mathfrak{v}}_{T-1}^{\prime}(a) .
    \end{aligned}\end{gathered}$$

$\cnstr{\aFunc}_{T-1}^{*}(\mNrm)$ therefore answers the question “With what level of assets would the restrained consumer like to end period $T-1$ if the constraint $c_{T-1} \leq \mNrm_{T-1}$ did not exist?” (Note that the restrained consumer’s income process remains different from the process for the unrestrained consumer so long as $\pZero>0$.)
The restrained consumer’s actual asset position will be
$$\begin{gathered}\begin{aligned}
      \cnstr{\aFunc}_{T-1}(\mNrm)  & = \max[0,\cnstr{\aFunc}^{*}_{T-1}(\mNrm)], \notag
    \end{aligned}\end{gathered}$$
reflecting the inability of the restrained consumer to spend more than current resources, and note (as pointed out by [(Deaton, 1991)](#cite-deatonLiqConstr)) that
$$\begin{gathered}\begin{aligned}
      \mNrm^{1}_{\#}  & = {\left( \cnstr{\mathfrak{v}}_{T-1}^{\prime}(0)\right)}^{-1/\CRRA} \notag
    \end{aligned}\end{gathered}$$
is the cusp value of $\mNrm$ at which the constraint makes the
transition between binding and non-binding in period $T-1$.

Analogously to [](#eq-uPConstr), defining
(eq-vFrakPrime)=
$$\begin{gathered}\begin{aligned}
      \mathfrak{v}_{T-1}^{\prime}(a;\pZero)  & \equiv  \left[\pZero \aNrm^{-\CRRA}+\pNotZero\int_{\underline{\tranShkEmp}}^{\bar{\tranShkEmp}} {\left(\cFunc_{T}(a+\tranShkEmp/\pNotZero)\right)}^{-\CRRA} d\CDF_{\tranShkEmp}\right], 
    \end{aligned}\end{gathered}$$
the Euler equation for the original consumer’s problem implies
(eq-uPUnconstr)=
$$\begin{gathered}\begin{aligned}
      {(\mNrm-\aNrm)}^{-\CRRA}  & = \mathfrak{v}_{T-1}^{\prime}(a;\pZero) 
    \end{aligned}\end{gathered}$$
with solution $\aFunc_{T-1}^{*}(\mNrm;\pZero)$.
Now note that for any fixed $\aNrm>0$, $\lim_{\pZero \downarrow 0} \mathfrak{v}_{T-1}^{\prime}(a;\pZero) = \cnstr{\mathfrak{v}}_{T-1}^{\prime}(a)$.
Since the LHS of [](#eq-uPConstr) and [](#eq-uPUnconstr) are identical, this means that $\lim_{\pZero \downarrow 0} \aFunc_{T-1}^{*}(\mNrm;\pZero) = \cnstr{\aFunc}_{T-1}^{*}(\mNrm)$.
That is, for any fixed value of $\mNrm > \mNrm^{1}_{\#}$ such that the consumer subject to the restraint would voluntarily choose to end the period with positive assets, the level of end-of-period assets for the unrestrained consumer approaches the level for the restrained consumer as $\pZero \downarrow 0$.
With the same $\aNrm$ and the same $\mNrm$, the consumers must have the same $c$, so the consumption functions are identical in the limit.

Now consider values $\mNrm\leq \mNrm^{1}_{\#}$ for which the restrained consumer is constrained.
It is obvious that the baseline consumer will never choose $\aNrm \leq 0$ because the first term in [](#eq-vFrakPrime) is $\lim_{\aNrm \downarrow 0} \pZero \aNrm^{-\CRRA} = \infty$, while $\lim_{\aNrm \downarrow 0} {(\mNrm-\aNrm)}^{-\CRRA}$ is finite (the marginal value of end-of-period assets approaches infinity as assets approach zero, but the marginal utility of consumption has a finite limit for $\mNrm>0$).
The subtler question is whether it is possible to rule out strictly positive $\aNrm$ for the unrestrained consumer.

The answer is yes.
Suppose, for some $\mNrm < \mNrm^{1}_{\#}$, that the unrestrained consumer is considering ending the period with any positive amount of assets $\aNrm=\delta > 0$.
For any such $\delta$ we have that $\lim_{\pZero \downarrow 0} \mathfrak{v}_{T-1}^{\prime}(a;\pZero)=\cnstr{\mathfrak{v}}_{T-1}^{\prime}(a)$.
But by assumption we are considering a set of circumstances in which $\cnstr{\aFunc}_{T-1}^{*}(\mNrm) < 0$, and we showed earlier that $\lim_{\pZero \downarrow 0} \aFunc_{T-1}^{*}(\mNrm;\pZero) = \cnstr{\aFunc}_{T-1}^{*}(\mNrm)$.
So, having assumed $\aNrm = \delta > 0$, we have proven that the consumer would optimally choose $\aNrm < 0$, which is a contradiction.
A similar argument holds for $\mNrm = \mNrm^{1}_{\#}$.

These arguments demonstrate that for any $\mNrm>0$, $\lim_{\pZero \downarrow 0} \cFunc_{T-1}(\mNrm;\pZero) = \cnstr{\cFunc}_{T-1}(\mNrm)$ which is the period $T-1$ version of [](#eq-RestrEqUnrestr).
But given equality of the period $T-1$ consumption functions, backwards recursion of the same arguments demonstrates that the limiting consumption functions in previous periods are also identical to the constrained function.

Note finally that another intuitive confirmation of the equivalence between the two problems is that our formula [](#eq-MPCmaxDef) for the maximal marginal propensity to consume satisfies
$$\begin{aligned}
  \lim_{\pZero \downarrow 0} \MPCmax  & = 1,
\end{aligned}$$
which makes sense because the marginal propensity to consume for a constrained restrained consumer is 1 by our definitions of ‘constrained’ and ‘restrained.’

(ApndxMTargetIsStable)=

# Appendix for Section [](#sec-individStability) 

(sec-ApndxMTargetIsStable)=

## Asymptotic Consumption Growth Factors 

(subsec-AppxCgrowthFac)=

(prop-convgGrowth)=
:::{prf:proposition}
:label: prop-convgGrowth

We have $\lim\limits_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[\cLvl_{t+1}/\cLvl_{t}] =  {\APFac}$ and $\lim\limits_{\mNrm_{t} \rightarrow  0} \Ex_{t}[\cLvl_{t+1}/\cLvl_{t}] =  \infty$.

:::

:::{prf:proof} **Proof for Proposition [](#subsec-AppxCgrowthFac)**

For consumption growth, as $\mNrm \rightarrow 0$ we have:

(eq-consGrowth)=
$$\begin{gathered}\begin{aligned}
  \lim_{\mNrm_{t} \rightarrow 0} \Ex_{t}\left[\left(\frac{\cFunc({\mNrm}_{t+1})}{\cFunc(\mNrm_t)}\right){\PermGroFacRnd}_{t+1}\right]
  & > \lim_{\mNrm_{t} \rightarrow 0} \Ex_{t}\left[\left(\frac{\Min{\cFunc}(\RNrmByGRnd_{t+1}\aFunc(\mNrm_{t})+{
    \tranShkAll}_{t+1})}{\MPCmax \mNrm_{t}}\right){\PermGroFacRnd}_{t+1}\right]  \notag \\
  & = \pZero \lim_{\mNrm_{t} \rightarrow 0} \Ex_{t}\left[\left(\frac{\Min{\cFunc}(\RNrmByGRnd_{t+1}\aFunc(\mNrm_{t}))}{\MPCmax \mNrm_{t}}\right){\PermGroFac}_{t+1}\right] \\
  & ~~~~~~ + \pNotZero \lim_{\mNrm_{t} \rightarrow 0}  \Ex_{t}\left[\left(\frac{\Min{\cFunc}(\RNrmByGRnd_{t+1}\aFunc(\mNrm_{t})+
    \tranShkEmp_{t+1}/\pNotZero)}{\MPCmax \mNrm_{t}}\right){\PermGroFacRnd}_{t+1}\right]  \\\notag
  & > \pNotZero \lim_{\mNrm_{t} \rightarrow 0} \Ex_{t}\left[\left(\frac{\Min{\cFunc}(
    \tranShkEmp_{t+1}/\pNotZero)}{\MPCmax \mNrm_{t}}\right){\PermGroFacRnd}_{t+1}\right] \\
  & = \infty \nonumber
\end{aligned}\end{gathered}$$

where the second-to-last line follows because $\lim_{\mNrm_{t} \rightarrow 0} \Ex_{t}\left[\left(\frac{\Min{\cFunc}(\RNrmByGRnd_{t+1}\aFunc(\mNrm_{t}))}{\MPCmax \mNrm_{t}}\right){\PermGroFacRnd}_{t+1}\right]$ is positive, and the last line follows because the minimum possible realization of $\tranShkEmp_{t+1}$ is $\Min{\tranShkEmp}>0$ so the minimum possible value of expected next-period consumption is positive.

Next we establish the limit of the expected consumption growth factor as $\mNrm_{t} \rightarrow \infty$:

$$\begin{aligned}
  \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[
  \cLvl_{t+1}/\cLvl_{t}]  & = \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[
                            {\PermGroFacRnd}_{t+1} {\cNrm}_{t+1}/c_{t}].
\end{aligned}$$

But
$$\begin{aligned}
  \Ex_{t}[{\PermGroFacRnd}_{t+1} {\Min{\cNrm}}_{t+1}/\bar{\cNrm}_{t}] \leq \Ex_{t}[{\PermGroFacRnd}_{t+1} {\cNrm}_{t+1}/\cNrm_{t}] \leq \Ex_{t}[{\PermGroFacRnd}_{t+1} {\bar{\cNrm}}_{t+1}/\Min{\cNrm}_{t}]
\end{aligned}$$
and
(eq-xttoinfty)=
$$
  \lim_{\mNrm_t \rightarrow \infty} \PermGroFacRnd_{t+1}\Min{\cFunc}(\mNrm_{t+1})/\bar{\cFunc}(\mNrm_t) =
  \lim_{\mNrm_{t} \rightarrow \infty} \PermGroFacRnd_{t+1}\bar{\cFunc}(\mNrm_{t+1})/\Min{\cFunc}(\mNrm_t) =
  \lim_{\mNrm_{t} \rightarrow \infty}\PermGroFacRnd_{t+1} \mNrm_{t+1}/\mNrm_t,$$
while (for convenience defining $\aFunc(\mNrm_{t})=\mNrm_{t}-\usual{\cFunc}(\mNrm_{t})$), 
(xtp1toinfty)=

(eq-xtp1toinfty)=
$$\begin{gathered}\begin{aligned}  
  \lim_{\mNrm_{t} \rightarrow \infty} \PermGroFacRnd_{t+1} \mNrm_{t+1}/\mNrm_t  & = \lim_{\mNrm_{t} \rightarrow \infty}
                                                                            \left(\frac{\Rfree \aFunc(\mNrm_t)+{\PermGroFacRnd}_{t+1}\tranShkAll_{t+1}}{\mNrm_t}\right)
  \\  & = {(\Rfree \DiscFac)}^{1/\CRRA} = \APFac \notag
\end{aligned}\end{gathered}$$
because $\lim\limits_{\mNrm_{t}\rightarrow \infty} \aFunc^{\prime}(\mNrm)=\RPFac$[^45] and $\PermGroFacRnd_{t+1}\tranShkAll_{t+1}/\mNrm_{t} \leq (\PermGroFac \bar{\permShk} \bar{\tranShkEmp}/\pNotZero )/\mNrm_{t}$ which goes to zero as $\mNrm_{t}$ goes to infinity.
Hence we have:

$${\APFac}  \leq \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[\cLvl_{t+1}/\cLvl_{t}] \leq {\APFac}$$

so as cash goes to infinity, consumption growth approaches its value $\APFac$ in the perfect foresight model.

:::

This appendix proves Theorems [](#thm-target)-[](#thm-MSSBalExists) and:

(lemma-orderingPartOne)=
:::{prf:lemma}
:label: lemma-orderingPartOne

If $\BalGroFac{\mNrm}$ and $\TargetNrm{\mNrm}$ both exist, then $\BalGroFac{\mNrm} \leq \TargetNrm{\mNrm}$.

:::

## Existence of Buffer Stock Target 

### Existence of Individual Buffer Stock Target 

(subsubsec-AppxIndividTarget)=

:::{prf:proof} **Proof of Theorem [](#thm-target)**

First, observe that $\Ex_{t}[{\mNrm}_{t+1}/\mNrm_t] = \frac{\Ex_{t}\left((\mNrm_t - \cFunc(\mNrm_t)) \RNrmByGRnd_{t+1} + \tranShkAll_{t+1}\right)}{\mNrm_t}$.
Note that $\cFunc$ is continuous since $\cFunc$ is concave on $\Reals_{++}$ by Lemma [](#lemma-MPCBoundsConvg).
Thus for any convergent sequence $\left\{\mNrm_t^{j}\right\}_{j=0}^{\infty}$, with $\mNrm_t^{j}\in \Reals_{++}$, $(\mNrm_t^{j} - \cFunc(\mNrm_t^{j})) \RNrmByGRnd_{t+1} + \tranShkAll_{t+1}$ will be bounded above and below.
It follows that, using the Dominated Convergence Theorem, $\Ex_{t}[{\mNrm}_{t+1}/\mNrm_t]$ will be continuous in $\mNrm_t$.

The remainder of the proof proceeds as follows.
To establish Equation [](#eq-mTarget), we will show (i) that there exists a point $\breve{\mNrm}_{t}$ where $\Ex_t [\breve{\mNrm}_{t+1}^{\star}/\breve{\mNrm}_{t}^{\star}] < 1$ and (ii) a point $\grave{\mNrm}$ where $\Ex_t [\grave{\mNrm}_{t+1}/\grave{\mNrm}_{t}] > 1$.
By continuity of $\Ex[{\mNrm}_{t+1}/\mNrm_t]$ in $\mNrm_t$ and the Intermediate Value Theorem, there will exist $\mTrgNrm$ such that $\Ex_t [{\mTrgNrm}_{t+1}/\hat{\mNrm}_{t}] = 1$.
In turn, to establish that $\mTrgNrm$ is a point of stability, Equation [](#eq-stability), we will show that (iii) $\Ex_t [{\mNrm}_{t+1}]-\mNrm_{t}$ is decreasing.

To proceed, first suppose [return impatience](#RIC) holds and take the steps analogous to those leading to Equation [](#xtp1toinfty) in the proof of proof for Proposition [](#subsec-AppxCgrowthFac), but dropping the $\PermGroFac_{t+1}$ from the RHS:

(eq-emgro)=
$$\begin{gathered}\begin{aligned}
  \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[{\mNrm}_{t+1}/\mNrm_{t}]  & =   
                                                                       \lim_{\mNrm_{t} \rightarrow \infty} 
                                                                       \Ex_{t}\left[\frac{\RNrmByGRnd_{t+1}(\mNrm_{t}-\cFunc(\mNrm_{t}))+{\tranShkAll}_{t+1}}{\mNrm_{t}}\right] \notag 
  \\  & = \Ex_{t}[(\Rfree/{\PermGroFacRnd}_{t+1})\RPFac]  \notag
  \\  & = \Ex_{t}[{\APFac}/{\PermGroFacRnd}_{t+1}]  
  \\  & < 1, \notag
\end{aligned}\end{gathered}$$

where the inequality follows from [strong growth impatience](#GICMod).
By continuity of $\Ex_{t}[{\mNrm}_{t+1}/\mNrm_t]$ in $\mNrm_t$, there exists $\breve{\mNrm}_{t}$ large enough such that $\Ex_t [\breve{\mNrm}_{t+1}/\breve{\mNrm}_t] < 1$.

Next, suppose [return impatience](#RIC) fails.
The fact that $\lim\limits_{\mNrm_{t} \rightarrow \infty} \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}} = 0$ (Lemma [](#lemma-MPCBoundsConvg)) means the limit of the RHS of [](#eq-emgro) as $\mNrm_{t} \rightarrow \infty$ is $\bar{\RNrmByGRnd}=\Ex_{t}[\RNrmByGRnd_{t+1}]$.
Equations [](#eq-GICStrRICfailst1)-[](#eq-GICStrRICfailst2) below show that when [strong growth impatience](#GICMod) holds and [return impatience](#RIC) fails $\bar{\RNrmByGRnd} < 1$.

Thus, we have $\lim\limits_{\mNrm \rightarrow \infty} \Ex[\mNrm_{t+1}/\mNrm_{t}] < 1$ whether the [return impatience](#RIC) holds or fails.

Analogous to Equation [](#eq-consGrowth), the ratio of $\Ex_{t}[\mNrm_{t+1}]$ to $\mNrm_{t}$ is unbounded above as $\mNrm_{t} \rightarrow 0$ because $\lim\limits_{\mNrm_{t}\rightarrow 0} \Ex[\mNrm_{t+1}] > 0$.
Thus, if $\Ex_t [{\mNrm}_{t+1}/\mNrm_t]$ is continuous in $\mNrm_t$, and takes on values above and below one at $\grave{\mNrm}_{t}$ and $\breve{\mNrm}_{t}$, by the Intermediate Value Theorem, there must be at least one point at which it is equal to one.

Finally to show $\Ex_t [{\mNrm}_{t+1}] -\mNrm_t$ is strictly decreasing $\mNrm_t$, define $\difFunc(\mNrm_t) := 
\Ex_t[\mNrm_{t+1}] - \mNrm_t$ and note that:

(eq-difNrmioEquiv)=
$$\begin{gathered}\begin{aligned}
  \difFunc(\mNrm_t) < 0 &\leftrightarrow \Ex_t[{\mNrm}_{t+1}/\mNrm_t] < 1 
                          \nonumber\\
  \difFunc(\mNrm_t) = 0 &\leftrightarrow \Ex_t[{\mNrm}_{t+1}/\mNrm_t] = 1\\
  \difFunc(\mNrm_t) > 0 &\leftrightarrow \Ex_t[{\mNrm}_{t+1}/\mNrm_t] > 
                          1,\nonumber,
\end{aligned}\end{gathered}$$

so that $\difFunc(\mTrgNrm)=0$.
Our goal is to prove that $\difFunc(\bullet)$ is strictly decreasing on $(0,\infty)$.
Let $\Delta_{\epsilon}$ be the finite forward difference for spacing $\epsilon>0$.
Fixing $\epsilon>0$, we will have:

(eq-finiteDiff2)=
$$\begin{gathered}\begin{aligned}
  \Delta_{\epsilon}\difFunc(\mNrm_{t}) &            = \Ex_{t}\left[\Delta_{\epsilon} \left( {\RNrmByGRnd}(\mNrm_{t}-\cFunc(\mNrm_{t}))+
                                                                       {\tranShkAll}_{t+1} - {\mNrm}_t\right) \right] \notag \\
                                                  & =  \bar{\RNrmByGRnd}\left( \epsilon-
                                                       \Delta_{\epsilon}\cFunc({\mNrm}_t)\right) - \epsilon = \epsilon\left( \bar{\RNrmByGRnd}\left[1-
                                                       \frac{\Delta_{\epsilon}\cFunc({\mNrm}_t)}{\epsilon}\right]- 1\right). 
\end{aligned}\end{gathered}$$

Notice that $\frac{\Delta_{\epsilon}\cFunc({\mNrm}_t)}{\epsilon} \leq \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}}<1$ since $\frac{\cFunc(\mNrm_{t})}{\mNrm_{t}}$ is decreasing in $\mNrm_{t}$ by Claim [](#claim-rationondec) in Appendix [](#sec-realanalysis).
Consider the case when [return impatience](#RIC) holds.
Equation [](#eq-MPCminDef) and Lemma [](#lemma-MPCBoundsConvg) indicate $0 < \MPCmin \leq \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}} < 1$.

It follows that:

$$\begin{aligned}
  \bar{\RNrmByGRnd}\left[1-\frac{\Delta_{\epsilon}\cFunc^{\prime}({\mNrm}_t)}{\epsilon}\right]- 1 & \leq  \bar{\RNrmByGRnd}(1-\underbrace{(1-\RPFac)}_{\MPCmin}) - 1  \\
                                                            & = \bar{\RNrmByGRnd}\RPFac - 1 \\
                                                            & = \Ex_{t}\left[\frac{\Rfree}{\PermGroFac \permShk_{t+1}}\frac{\APFac}{\Rfree}\right] - 1 \\
                                                            & = \underbrace{\Ex_{t}\left[\frac{\APFac}{\PermGroFac \permShk_{t+1}}\right]}_{= \GPFacMod} - 1 
\end{aligned}$$

which is negative because the [strong growth impatience](#GICMod) says $\GPFacMod < 1$.
Conversely, when [return impatience](#RIC) holds fails, recall $\lim\limits_{\mNrm_{t} \rightarrow \infty} \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}} = 0$.
This means $\Delta_{\epsilon}\difFunc(\mNrm_{t})$ from [](#eq-finiteDiff2) is guaranteed to be negative if:

(eq-RbarBelowOne)=
$$\begin{gathered}\begin{aligned}
  \bar{\RNrmByGRnd} = \Ex_{t}\left[\frac{\Rfree}{\PermGroFac \permShk_{t+1}}\right] & < 1  .
\end{aligned}\end{gathered}$$

But the combination of the [strong growth impatience](#GICMod) holding and the [return impatience](#RIC) failing can be written:

(eq-GICStrRICfailst1)=
$$\begin{gathered}\begin{aligned}
  \overbrace{\Ex_{t}\left[\frac{\APFac}{\PermGroFac \permShk_{t+1}}\right]}^{\GPFacMod} & < 1 < \overbrace{\frac{\APFac}{\Rfree}}^{{\RPFac}},
\end{aligned}\end{gathered}$$

and multiplying all three elements by $\Rfree/\APFac$ gives:

(eq-GICStrRICfailst2)=
$$\begin{gathered}\begin{aligned}
  \Ex_{t}\left[\frac{\Rfree}{\PermGroFac \permShk_{t+1}}\right] & < \Rfree/\APFac < 1,
\end{aligned}\end{gathered}$$

which satisfies our requirement in [](#eq-RbarBelowOne), thus completing the proof.
 

:::

### Existence of Pseudo-Steady-State 

(subsubsec-AppxPseudoSS)=

:::{prf:proof} **Proof of Theorem [](#thm-MSSBalExists)**

Since by assumption $0 < \Min{\permShk} \leq \permShk_{t+1} \leq \bar{\permShk} < \infty$, our proof in [](#subsubsec-AppxIndividTarget) that demonstrated existence and continuity of $\Ex[\mNrm_{t+1}/\mNrm_{t}]$ implies existence and continuity of $\Ex[\permShk_{t+1}\mNrm_{t+1}/\mNrm_{t}]$.

Since by assumption $0 < \Min{\permShk} \leq \permShk_{t+1} \leq \bar{\permShk} < \infty$, our proof in Subsection [](#subsubsec-AppxIndividTarget) that the ratio of $\Ex[\mNrm_{t+1}]$ to $\mNrm_{t}$ is unbounded as $\mNrm_{t} \rightarrow 0$ implies that the ratio $\Ex[\permShk_{t+1}\mNrm_{t+1}]$ to $\mNrm_{t}$ is unbounded as $\mNrm_{t} \rightarrow 0$.
The limit of the expected ratio as $\mNrm_{t}\rightarrow \infty$ goes to infinity is can be found as follows:

(eq-emgro2)=
$$\begin{gathered}\begin{aligned}
  \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}[\permShk_{t+1}\mNrm_{t+1}/\mNrm_{t}]  & =   
                                                                  \lim_{\mNrm_{t} \rightarrow \infty} 
                                                                  \Ex_{t}\left[\frac{\PermGroFacRnd_{t+1}\left((\Rfree/\PermGroFacRnd_{t+1})\aFunc(\mNrm_{t})+{\tranShkAll}_{t+1}\right)/\PermGroFac}{\mNrm_{t}}\right] \notag 
  \\   & =   \lim_{\mNrm_{t} \rightarrow \infty} \Ex_{t}\left[
         \frac{(\Rfree/\PermGroFac)\aFunc(\mNrm_{t})+\permShk_{t+1}{\tranShkAll}_{t+1}}{\mNrm_{t}}
         \right] \notag 
  \\   & =   \lim_{\mNrm_{t} \rightarrow \infty} \left[
         \frac{(\Rfree/\PermGroFac)\aFunc(\mNrm_{t})+1}{\mNrm_{t}}
         \right] \notag 
  \\  & = (\Rfree/\PermGroFac)\RPFac 
  \\  & = \GPFacRaw \notag
  \\  & < 1, \notag
\end{aligned}\end{gathered}$$

where the last two lines are merely a restatement of [growth impatience](#GICRaw).

To conclude Part (i) of the proof, the Intermediate Value Theorem says that if $\Ex[\permShk_{t+1}\mNrm_{t+1}/\mNrm_t]$ is continuous, and takes on values above and below 1, there must be at least one point at which it is equal to one.

Define $\difFunc(\mNrm_t) := 
\Ex_t[\permShk_{t+1}\mNrm_{t+1}] - \mNrm_t$ and note that:
(eq-difLvlEquiv)=
$$\begin{gathered}\begin{aligned}
  \difFunc(\mNrm_t) < 0 &\leftrightarrow \Ex_t[\permShk_{t+1}\mNrm_{t+1}/\mNrm_{t}] < 1 
                          \nonumber\\
  \difFunc(\mNrm_t) = 0 &\leftrightarrow \Ex_t[\permShk_{t+1}\mNrm_{t+1}/\mNrm_{t}] = 1\\
  \difFunc(\mNrm_t) > 0 &\leftrightarrow \Ex_t[\permShk_{t+1}\mNrm_{t+1}/\mNrm_{t}] > 
                          1,\nonumber
\end{aligned}\end{gathered}$$
so that $\difFunc(\mTrgNrm)=0$.
Our goal is to prove that $\difFunc(\bullet)$ is strictly
decreasing on $(0,\infty)$.
Letting $\Delta_{\epsilon}$ be the forward difference operator, we have:

(eq-finiteDiff)=
$$\begin{gathered}\begin{aligned}
  \Delta_{\epsilon}\difFunc(\mNrm_{t}) &            = \Ex\left[
                                                                                              \Delta_{\epsilon} \left( 
                                                                                               \frac{\Rfree}{\PermGroFac}(\mNrm_{t}-\cFunc(\mNrm_{t}))+
                                                                                               {\permShk}_{t+1}{\tranShkAll}_{t+1} - {\mNrm}_t\right) \right] \notag \\
                                                                                             & = \frac{\Rfree}{\PermGroFac}\left( \epsilon-
                                                       \Delta_{\epsilon}\cFunc^{\prime}({\mNrm}_t)\right) - \epsilon = \epsilon\left(  \frac{\Rfree}{\PermGroFac}\left[1-
                                                       \frac{\Delta_{\epsilon}\cFunc({\mNrm}_t)}{\epsilon}\right]- 1\right). 
\end{aligned}\end{gathered}$$

for any given $\epsilon>0$.
Notice that $\frac{\Delta_{\epsilon}\cFunc^{\prime}({\mNrm}_t)}{\epsilon} \leq \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}}<1$ since $\frac{\cFunc(\mNrm_{t})}{\mNrm_{t}}$ is decreasing in $\mNrm_{t}$ by Claim [](#claim-rationondec) in Appendix.
Now, we show that $\difFunc(\mNrm)$ is decreasing when [return impatience](#RIC) holds and when [return impatience](#RIC) fails.
When [return impatience](#RIC) holds, Equation [](#eq-MPCminDef) and Lemma [](#lemma-MPCBoundsConvg) indicate that $\MPCmin >0$ and $0 < \MPCmin \leq \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}} < 1$.
It follows that:

$$\begin{aligned}
   \frac{\Rfree}{\PermGroFac}\left(1-\cFunc^{\prime}({\mNrm}_t)\right) - 1 & <   \frac{\Rfree}{\PermGroFac}(1-\underbrace{(1-\RPFac)}_{\MPCmin}) - 1  \\
                                                      & = (\Rfree/\PermGroFac)\RPFac - 1, 
\end{aligned}$$

which is negative because [growth impatience](#GICRaw) says $\GPFacRaw < 1$.
Conversely, when [return impatience](#RIC) holds fails, recall $\lim\limits_{\mNrm_{t} \rightarrow \infty} \frac{\cFunc(\mNrm_{t})}{\mNrm_{t}} = 0$.
In turn, this means $\Delta_{\epsilon}\difFunc(\mNrm_{t})$ from [](#eq-finiteDiff) is guaranteed to be negative if:

(eq-FHWCFails)=
$$\begin{gathered}\begin{aligned}
  (\Rfree/\PermGroFac) & < 1  .
\end{aligned}\end{gathered}$$

But we showed in Section [](#subsubsec-PFUncon), Equation [](#eq-RICimplies), that the only circumstances under which the problem has a non-degenerate solution while [return impatience](#RIC) fails were ones where the [finite limiting human wealth](#ass-FHWC) also fails.
Thus, $(\Rfree/\PermGroFac) < 1$, completing the proof.

:::

(ApndxBalancedGrowthcNrmAndCov)=

# Appendix for Section 4 

## Growth Impatience Implies Harmenberg Impatience 

(sec-AppxHarmImpGIC)=

We show here that [growth impatience](#GICRaw) implies the condition imposed by [(Harmenberg, 2021b)](#cite-harmenbergAggregating) to guarantee
the existence of a permanent income weighted distribution of normalized market resources.
Letting $f$ denote the density of the permanent income shock $\permShk$, the impatience condition imposed by [(Harmenberg, 2021b)](#cite-harmenbergAggregating) is

(eq-HarmImp)=
$$
  \log \left( \APFac \right) < \int \log(\PermGroFac\permShk) \permShk f(\permShk)\,d\permShk .$$

:::{prf:property}

If [growth impatience](#GICRaw) holds, then [](#eq-HarmImp) holds.

:::

:::{prf:proof}

Since $\permShk\mapsto \log(\PermGroFac\permShk) \permShk$ is convex, Jensen’s inequality implies

(eq-Jensen)=
$$
  \int \log(\PermGroFac\permShk) \permShk f(\permShk)\,d\permShk \geq \log(\PermGroFac\mathbb{E}\permShk) \mathbb{E}\permShk = \log(\PermGroFac)$$

Since [growth impatience](#GICRaw) implies $\PermGroFac > \APFac$ and $\log$ is strictly monotone increasing, the result follows.

:::

## Apparent Balanced Growth in $\cNrmAvg$ and $\cov(\cNrm,\permLvl)$ 

(sec-ApndxBalancedGrowthcNrmAndCov)=

Section [](#subsec-Covariances) demonstrates some propositions under the assumption that, when an economy satisfies the , there will be constant growth factors $\GroFac_{\cNrmAvg}$ and $\GroFac_{\cov}$ respectively for $\cNrmAvg$ (the average value of the consumption ratio) and $\cov(\cNrm,\permLvl)$. In the case of a Szeidl-invariant economy, the main text shows that these are $\GroFac_{\cNrmAvg}=1$ and $\GroFac_{\cov}=\PermGroFac$. If the economy is Harmenberg- but not Szeidl-invariant, no proof is offered that these growth factors will be constant.

## $\log \cNrm$ and $\log \cov(\cNrm,\permLvl)$ Grow Linearly 

Figures [](#fig-logcNrm) and [](#fig-logcov) plot the results of simulations of an economy that satisfies Harmenberg- but not Szeidl-invariance with a population of 4 million agents over the last 1000 periods (of a 2000 period simulation).[^46] The first figure shows that $\log \cNrmAvg$ increases apparently linearly. The second figure shows that $\log (-\cov(\cNrm,\permLvl))$ also increases apparently linearly. (These results are produced by the notebook [`ApndxBalancedGrowthcNrmAndCov.ipynb`](https://github.com/econ-ark/BufferStockTheory/blob/master/Code/Python/ApndxBalancedGrowthcNrmAndCov.ipynb)).

(fig-logcNrm)=

:::{figure} Figures/logcNrm.png
:name: fig-logcNrm
:width: 90%

Appendix: log  𝔠 Appears to Grow Linearly
:::

(fig-logcov)=

:::{figure} Figures/logcov.png
:name: fig-logcov
:width: 90%

Appendix: $\log ~(-\cov(\cNrm,\permLvl))$ Appears to Grow Linearly
:::

(see [](#eq-DBCparts))

(ApndxLiqConstr)=

# Appendix for Section 5 

(sec-ApndxLiqConstr)=

In this appendix, we use the following acronyms to refer to the consumer patience conditions identified in Section [](#subsec-GICTheorySetup) using the acronyms from Table [](#Factors-Defined-And-Compared).

(Autarky-Value)=

We briefly interpret FVAC before turning to how all the conditions relate under uncertainty. Analogously to [](#eq-ValuePFAnalyticalAutarky), the value for a consumer who spent exactly their permanent income every period would reflect the product of the expectation of the (independent) future shocks to permanent income:
(uInvEuPermShkDefn)=

$$\begin{aligned}
  
             & = \uFunc(\permLvl_{t})\left(\frac{1-{(\DiscFac \PermGroFac^{1-\CRRA}\Ex[\permShk^{1-\CRRA}])}^{T-t+1}}{1-\DiscFac \PermGroFac^{1-\CRRA} \Ex[\permShk^{1-\CRRA}]}\right),
\end{aligned}$$

The function $\vFuncLvl_{t}$ will be finite as $T$ approaches $\infty$ if the FVAC holds.
In the case without uncertainty, Because $\uFunc(xy) = x^{1-\CRRA}\uFunc(y)$, the value the consumer would achieve is:

(eq-ValuePFAnalyticalAutarky)=
$$\begin{gathered}\begin{aligned}  
      \vFuncLvl_{t}^{\text{autarky}}  & = \uFunc(\permLvl_{t})+\DiscFac \uFunc(\permLvl_{t}\PermGroFac)+\DiscFac^{2} \uFunc(\permLvl_{t} \PermGroFac^{2})+\ldots 
      \\  & = \uFunc(\permLvl_{t})\left(\frac{1-{(\DiscFac \PermGroFac^{1-\CRRA})}^{T-t+1}}{1-\DiscFac \PermGroFac^{1-\CRRA}}\right) \notag
    \end{aligned}\end{gathered}$$
which (for $\PermGroFac>0$) asymptotes to a finite number as $n$, with $n=T-t$, approaches $+\infty$.

## Perfect Foresight Unconstrained Solution 

(subsec-ApndxUCPF)=

The first result relates to the perfect foresight case without liquidity constraints.

:::{prf:proof} **Proof of Proposition [](#prop-pfUCFHWC)**

Consider a sequence of consumption $\{\cLvl_{T-n}\}_{n= t}^{T}$ and a sequence of income $\{\permLvl_{T-n}\}_{n= t}^{T}$ and let $\mathrm{PDV}_{t}^{T}(\cLvl)$ and $\mathrm{PDV}_{t}^{T}(\permLvl)$ denote the present discounted value of the consumption sequence and permanent income sequence respectively.
The dynamic budget constraint, strictly positive marginal utility, and the can’t-die-in-debt condition, Equation [](#eq-NoDebtAtDeath), imply an exactly-holding intertemporal budget constraint (IBC):

(eq-IBCFinite)=
$$\begin{gathered}\begin{aligned}
  \mathrm{PDV}_{t}^{T}(\cLvl)  & = \overbrace{\mLvl_{t}-\permLvl_{t}}^{\bLvl_{t}}+\overbrace{\mathrm{PDV}_{t}^{T}(\permLvl)}^{\hLvl_{t}}, 
\end{aligned}\end{gathered}$$ 
(FHWFacDefn)=


where $\bLvl$ is beginning-of-period ‘market’ balances; with $\RNrmByGRnd := \Rfree/\PermGroFac$ ‘human wealth’ can be written as:

(eq-HDefAppx)=
$$\begin{gathered}\begin{aligned}
  \hLvl_{t}  & = \permLvl_{t}+\RNrmByGRnd^{-1} \permLvl_{t} + \RNrmByGRnd^{-2} \permLvl_{t} + \cdots + \RNrmByGRnd^{t-T} \permLvl_{t} \notag
  \\  & = \underbrace{\left(\frac{1-\RNrmByGRnd^{-(T-t+1)}}{1-\RNrmByGRnd^{-1}}\right)}_{\equiv \hNrm_{t}}\permLvl_{t} .
\end{aligned}\end{gathered}$$

Let $\hNrm$ denote the limiting value of normalized human wealth as the planning horizon recedes, we have $\hNrm := \lim\limits_{n \rightarrow \infty} \hNrm_{t_{n}}$.

Next, since consumption is growing by $\APFac$ but discounted by $\Rfree$:
$$\begin{aligned}
  \mathrm{PDV}_{t}^{T}(\cLvl)  & = \left(\frac{1-\RPFac^{T-t+1}}{1-\RPFac}\right)\cLvl_{t}
\end{aligned}$$
from which the IBC [](#eq-IBCFinite) implies
(eq-WDef)=
$$\begin{gathered}\begin{aligned}
  \cLvl_{t}  & = \overbrace{\left(\frac{1-\RPFac}{1-\RPFac^{T-t+1}}\right)}^{\equiv \MPCmin_{t}}
               (\bLvl_{t}+\hLvl_{t})   
\end{aligned}\end{gathered}$$
defining a normalized finite-horizon perfect foresight consumption function:

$$\begin{aligned}
  \bar{\cFunc}_{T-n}(\mNrm_{T-n})  & = (\overbrace{\mNrm_{T-n}-1}^{
                                     \equiv\bNrm_{T-n}}+\hNrm_{T-n})\MPCmin_{t-n}
\end{aligned}$$

where $\MPCmin_{t}$ is the marginal propensity to consume (MPC).
(The overbar signifies that $\bar{\cFunc}$ will be an upper bound as we modify the problem to incorporate constraints and uncertainty; analogously, $\MPCmin$ is the MPC’s lower bound).

The horizon-exponentiated term in the denominator of [](#eq-WDef) is why, for $\underline{\MPC}$ to be strictly positive as $n$ goes to infinity, we must impose the RIC.
The RIC thus implies that the consumer cannot be so pathologically patient as to wish, in the limit as the horizon approaches infinity, to spend nothing today out of an increase in current wealth (the RIC rules out the degenerate limiting solution $\bar{\cFunc}(\mNrm)=0$).

(Unconstrained-Solution)=


Given that the RIC holds, and (as before) defining limiting objects by the absence of a time subscript, the limiting upper bound consumption function will be
(eq-cFuncPFUncAppx)=
$$\begin{gathered}\begin{aligned}
  \bar{\cFunc}(\mNrm)  & = (\mNrm+\hNrm-1)\MPCmin,
\end{aligned}\end{gathered}$$
and so in order to rule out the degenerate limiting solution $\bar{\cFunc}(\mNrm) = \infty$ we need $\hNrm$ to be finite; that is, we must impose the Finite Human Wealth Condition (FHWC), Assumption [](#ass-FHWC).

:::

## Perfect Foresight Liquidity Constrained Solutions 

Under perfect foresight in the presence of a liquidity constraint requiring $\bNrm \geq 0$, this appendix taxonomizes the varieties of the limiting consumption function $\cnstr{\cFunc}(\mNrm)$ that arise under various parametric conditions.

:::{table} Appendix: Perfect Foresight Liquidity Constrained Taxonomy
:name: table-LiqConstrScenarios

| For constrained $\cnstr{c}$ and unconstrained $\bar{\cFunc}$ consumption functions |  |  |  |  |
|:---|---:|:--:|:---|:---|
| Main Condition |   |  |  |  |
|     Subcondition | Math |  |  | Outcome, Comments or Results |
|  | $\phantom{\APFac/\Rfree}$ | $\phantom{~<~}1        {~<~}$ | ${\APFac/\PermGroFac}$ | Constraint never binds for $\mNrm \geq 1$ |
|      and RIC  | ${\APFac/\Rfree}$ | ${~<~}1\phantom{~<~}$ | $\phantom{\APFac/\PermGroFac}$ |    FHWC holds ($\Rfree > \PermGroFac$); |
|  |  |  | $\phantom{\APFac/\PermGroFac}$ |    $\cnstr{\cFunc}(\mNrm) = \bar{\cFunc}(\mNrm)$ for $\mNrm \geq 1$ |
|      and | $\phantom{\APFac/\Rfree}$ | $\phantom{~<~}1        {~<~}$ | ${\APFac/\Rfree}$ |    $\cnstr{\cFunc}(\mNrm)$ is degenerate: $\cnstr{\cFunc}(\mNrm)=0$ |
|   | ${\APFac/\PermGroFac}$ | ${~<~}1\phantom{~<~}$ | $\phantom{\APFac/\Rfree}$ | Constraint binds in finite time $\forall~\mNrm$ |
|      and RIC  | ${\APFac/\Rfree}$ | ${~<~}1\phantom{~<~}$ | $\phantom{\APFac/\PermGroFac}$ |     FHWC may or may not hold |
|      |  |  |  |        $\lim_{m \uparrow \infty}\bar{\cFunc}(\mNrm) - \cnstr{\cFunc}(\mNrm) = 0$ |
|      |  |  |  |        $\lim_{m \uparrow \infty}\cnstr{\MPCFunc}(\mNrm) = \MPCmin$ |
|      and |  | $\phantom{~<~}1         ~<~$ | $\APFac/\Rfree$ | $\cncl{\FHWC}$ |
|        |  |  |  |      $\lim_{\mNrm \uparrow \infty} \cnstr{\MPCFunc}(\mNrm) =  0$ |

:::


  
Conditions are applied from left to right; for example, the second row indicates conclusions in the case where and RIC both hold, while the third row indicates that when the  and the RIC both fail, the consumption function is degenerate; the next row indicates that whenever the holds, the constraint will bind in finite time.

Results are summarized in table [](#table-LiqConstrScenarios).

### If GIC Fails 

A consumer is ‘growth patient’ if the perfect foresight growth
impatience condition fails (, $1 < \APFac/\PermGroFac$).
Under
the constraint does not bind at the lowest feasible value of $\mNrm_{t}=1$ because
$1 < {(\Rfree\DiscFacRaw)}^{1/\CRRA}/\PermGroFac$ implies that spending
everything today (setting $\cNrm_{t}=\mNrm_{t}=1$) produces lower
marginal utility than is obtainable by reallocating a marginal unit of
resources to the next period at return $\Rfree$:[^47]
(eq-EulerGICRawFailsEnd)=
$$\begin{gathered}\begin{aligned}
  1  & < {(\Rfree \DiscFacRaw)}^{1/\CRRA}\PermGroFac^{-1}    \notag
  \\ 1  & < \Rfree \DiscFacRaw \PermGroFac^{-\CRRA} \notag
  \\  \uFunc^{\prime}(1)  & < \Rfree \DiscFacRaw \uFunc^{\prime}(\PermGroFac)   .
\end{aligned}\end{gathered}$$

Similar logic shows that under these circumstances the constraint will never bind at $\mNrm=1$ for a constrained consumer with a finite horizon of $n$ periods, so for $\mNrm \geq 1$ such a consumer’s consumption function will be the same as for the unconstrained case examined in the main text.

(cnclGICRawcnclRICFHWC)=

*RIC fails, FHWC holds.* If the RIC fails ($1 < \RPFac$) while the finite human wealth condition
holds, the limiting value of this consumption function as $n \rightarrow
\infty$ is the degenerate function
$$\begin{gathered}\begin{aligned}
  \cnstr{\cFunc}_{T-n}(\mNrm)  & = 0 (\bNrm_{t}+\hNrm).
\end{aligned}\end{gathered}$$
(that is, consumption is zero for any level of human or nonhuman wealth).

(cnclGICRawcnclRICcnclFHWC)=

*RIC fails, FHWC fails*.
implies that human wealth limits to $\hNrm =
\infty$ so the consumption function limits to either
$\cnstr{\cFunc}_{T-n}(\mNrm) = 0$ or
$\cnstr{\cFunc}_{T-n}(\mNrm) = \infty$ depending on the relative
speeds with which the MPC approaches zero and human wealth approaches
$\infty$.[^48]

Thus, the requirement that the consumption function be nondegenerate
implies that for a consumer satisfying we must impose
the RIC (and the FHWC can be shown to be a consequence of and RIC).
In
this case, the consumer’s optimal behavior is easy to describe.
We
can calculate the point at which the unconstrained consumer would
choose $\cNrm = \mNrm$ from Equation [](#eq-cFuncPFUnc):
$$\begin{gathered}\begin{aligned}
  \mNrm_{\#}  & = (\mNrm_{\#}-1+\hNrm)\MPCmin
  \\ \mNrm_{\#}(1-\MPCmin)  & = (\hNrm - 1)\MPCmin
  \\ \mNrm_{\#}  & = (\hNrm - 1)\left(\frac{\MPCmin}{1-\MPCmin}\right)
\end{aligned}\end{gathered}$$
which (under these assumptions) satisfies $0 < \mNrm_{\#} < 1$.[^49]
For
$\mNrm < \mNrm_{\#}$ the unconstrained consumer would choose to
consume more than $\mNrm$; for such $\mNrm$, the constrained consumer
is obliged to choose $\cnstr{\cFunc}(\mNrm) = \mNrm$.[^50]
For
any $\mNrm > \mNrm_{\#}$ the constraint will never bind and the
consumer will choose to spend the same amount as the unconstrained
consumer, $\bar{\cFunc}(\mNrm)$.

([(Stachurski and Toda, 2019)](#cite-StachurskiToda2019JET) obtain a similar lower bound on consumption and use it to study the tail behavior of the wealth distribution.)

### If GIC Holds 

Imposition of the  reverses the inequality in [](#eq-EulerGICRawFailsEnd), and thus reverses the conclusion: A consumer who starts with $\mNrm_{t}=1$ will desire to consume more than 1.
Such a consumer will be constrained, not only in period $t$, but perpetually thereafter.

Now define $\bNrm_{\#}^{n}$ as the $\bNrm_{t}$ such that an unconstrained consumer holding $\bNrm_{t}=\bNrm_{\#}^{n}$ would behave so as to arrive in period $t+n$ with $\bNrm_{t+n}=0$ (with $\bNrm_{\#}^{0}$ trivially equal to 0); for example, a consumer with $\bNrm_{t-1}=\bNrm_{\#}^{1}$ was on the ‘cusp’ of being constrained in period $t-1$: Had $b_{t-1}$ been infinitesimally smaller, the constraint would have been binding (because the consumer would have desired, but been unable, to enter period $t$ with negative, not zero, $b$).
Given
the , the constraint certainly binds in period $t$ (and thereafter) with resources of $\mNrm_{t}=\mNrm_{\#}^{0}=1+\bNrm_{\#}^{0}=1$: The consumer cannot spend more (because constrained), and will not choose to spend less (because impatient), than $c_{t}=\cNrm_{\#}^{0}=1$.

We can construct the entire ‘prehistory’ of this consumer leading up to $t$ as follows.
Maintaining the assumption that the constraint has never bound in the past,
$\cNrm$ must have been growing according to $\GPFacRaw$, so consumption $n$ periods in the past must have been
(eq-cPreHist)=
$$\begin{gathered}\begin{aligned}
  \cNrm_{\#}^{n}  & = \GPFacRaw^{-n} \cNrm_{t} = \GPFacRaw^{-n}. 
\end{aligned}\end{gathered}$$

The PDV of consumption from $t-n$ until $t$ can thus be computed as
(PDVc)=
$$\begin{gathered}\begin{aligned}
  \mathbb{C}_{t-n}^{t}  & = \cNrm_{t-n}(1+\APFac/\Rfree+ \cdots + {(\APFac/\Rfree)}^{n}) \notag
  \\  & = \cNrm_{\#}^{n}(1+\RPFac+ \cdots + \RPFac^{n}) \notag
  \\  & = \GPFacRaw^{-n}\left(\frac{1-\RPFac^{n+1}}{1-\RPFac}\right) 
  \\  & = \left(\frac{\GPFacRaw^{-n}-\RPFac}{1-\RPFac}\right) 
\end{aligned}\end{gathered}$$
and note that the consumer’s human wealth between $t-n$ and $t$ (the relevant
time horizon, because from $t$ onward the consumer will be constrained
and unable to access post-$t$ income) is
$$\begin{gathered}\begin{aligned}
  \hNrm_{\#}^{n}  & = 1+ \cdots +\RNrmByGRnd^{-n}
\end{aligned}\end{gathered}$$
while the intertemporal budget constraint says
$$\begin{aligned}
  \mathbb{C}_{t-n}^{t}  & = \bNrm_{\#}^{n}+\hNrm_{\#}^{n}
\end{aligned}$$
from which we can solve for the $\bNrm_{\#}^{n}$ such that
the consumer with $\bNrm_{t-n} = \bNrm_{\#}^{n}$ would
unconstrainedly plan (in period $t-n$) to arrive in period $t$ with
$\bNrm_{t}=0$:
(eq-bPound)=
$$\begin{gathered}\begin{aligned}
  \bNrm_{\#}^{n} & =  \mathbb{C}_{t-n}^{t} - \overbrace{\left(\frac{1-\RNrmByGRnd^{-(n+1)}}{1-\RNrmByGRnd^{-1}}\right)}^{\hNrm_{\#}^{n}} .
\end{aligned}\end{gathered}$$

Defining $\mNrm_{\#}^{n}=\bNrm_{\#}^{n}+1$, consider the function
$\cnstr{\cFunc}(\mNrm)$ defined by linearly connecting the points
$\{\mNrm_{\#}^{n},\cNrm_{\#}^{n}\}$ for integer values of $n \geq 0$
(and setting $\cnstr{\cFunc}(\mNrm)=\mNrm$ for $\mNrm<1$).
This
function will return, for any value of $\mNrm$, the optimal value of
$\cNrm$ for a liquidity constrained consumer with an infinite horizon.
The function is piecewise linear with ‘kink points’ where the slope
discretely changes; for infinitesimal $\epsilon$ the MPC of a
consumer with assets $\mNrm=\mNrm_{\#}^{n}-\epsilon$ is discretely
higher than for a consumer with assets $\mNrm=\mNrm_{\#}^{n}+\epsilon$
because the latter consumer will spread a marginal dollar over more
periods before exhausting it.

In order for a unique consumption function to be defined by this sequence [](#eq-bPound) for the entire domain of positive real values of $b$, we need $\bNrm_{\#}^{n}$ to become arbitrarily large with $n$.
That is, we need
(eq-bToInfty)=
$$\begin{gathered}\begin{aligned}
  \lim_{n \rightarrow \infty} \bNrm_{\#}^{n} = \infty. 
\end{aligned}\end{gathered}$$

#### If FHWC Holds 

The FHWC requires $\RNrmByGRnd^{-1} < 1$, in which case the second term in [](#eq-bPound) limits to a constant as $n \rightarrow \infty$, and [](#eq-bToInfty) reduces to a requirement that
$$\begin{aligned}
  \lim_{n \rightarrow \infty} \left(\frac{\GPFacRaw^{-n}-{(\RPFac/\GPFacRaw)}^{n}\RPFac}{1-\RPFac}\right)  & = \infty
  \\  \lim_{n \rightarrow \infty} \left(\frac{\GPFacRaw^{-n}-\RNrmByGRnd^{-n}\RPFac}{1-\RPFac}\right)  & = \infty
  \\  \lim_{n \rightarrow \infty} \left(\frac{\GPFacRaw^{-n}}{1-\RPFac}\right)  & = \infty.
\end{aligned}$$
Given the  $\GPFacRaw^{-1}>1$, this will hold iff the RIC holds, $\RPFac < 1$.
But given that the FHWC $\Rfree > \PermGroFac$ holds, the is stronger (harder to satisfy) than the RIC; thus, the FHWC and the  together imply the RIC, and so a well-defined solution exists.
Furthermore, in the limit as $n$ approaches infinity, the difference between the limiting constrained consumption function and the unconstrained consumption function becomes vanishingly small, because the date at which the constraint binds becomes arbitrarily distant, so the effect of that constraint on current behavior shrinks to nothing.
That is,
$$\begin{gathered}\begin{aligned}
  \lim_{m \rightarrow \infty}\cnstr{\cFunc}(m) - \bar{\cFunc}(m) = 0.
\end{aligned}\end{gathered}$$

#### If FHWC Fails 

If the FHWC fails, matters are a bit more complex.

Given failure of FHWC, [](#eq-bToInfty) requires
(eq-FHWCfails)=
$$\begin{gathered}\begin{aligned}
  \lim_{n \rightarrow \infty} \left(\frac{\RNrmByGRnd^{-n}\RPFac-\GPFacRaw^{-n}}{\RPFac-1}\right) + \left(\frac{1-\RNrmByGRnd^{-(n+1)}}{\RNrmByGRnd^{-1}-1}\right)  & = \infty \notag
  \\   \lim_{n \rightarrow \infty} \left(\frac{\RPFac}{\RPFac-1}-\frac{\RNrmByGRnd^{-1}}{\RNrmByGRnd^{-1}-1}\right)\RNrmByGRnd^{-n}-\left(\frac{\GPFacRaw^{-n}}{\RPFac-1}\right)  & = \infty  
\end{aligned}\end{gathered}$$

(PFGICHoldsFHWCFailsRICFailsDiscuss)=

**If RIC Holds**.
When the RIC holds, rearranging [](#eq-FHWCfails) gives
$$\begin{aligned}
  \lim_{n \rightarrow \infty} \left(\frac{\GPFacRaw^{-n}}{1-\RPFac}\right)-\RNrmByGRnd^{-n}\left(\frac{\RPFac}{1-\RPFac}+\frac{\RNrmByGRnd^{-1}}{\RNrmByGRnd^{-1}-1}\right)  & = \infty
\end{aligned}$$
and for this to be true we need
$$\begin{aligned}
  \GPFacRaw^{-1}  & > \RNrmByGRnd^{-1}
  \\ \PermGroFac/\APFac  & > \PermGroFac/\Rfree
  \\ 1  & > \APFac/\Rfree
\end{aligned}$$
which is merely the RIC again.
So the problem has a solution if the RIC holds.
Indeed,
we can even calculate the limiting MPC from
(eq-MPCConstrLim)=
$$\begin{gathered}\begin{aligned}
  \lim_{n \rightarrow \infty} \MPC^{n}_{\#}  & = \lim_{n \rightarrow \infty} \left(\frac{\cNrm_{\#}^{n}}{\bNrm_{\#}^{n}}\right) 
\end{aligned}\end{gathered}$$
which with a bit of algebra[^51] can be shown to asymptote to the MPC in the perfect foresight model:[^52]
$$\begin{gathered}\begin{aligned}
  \lim_{m \rightarrow \infty} \cnstr{\pmb{\MPC}}(\mNrm)  & = 1-\RPFac.
\end{aligned}\end{gathered}$$

**If RIC Fails**.
Consider now the case, $\RPFac > 1$.
We can rearrange [](#eq-FHWCfails) as
$$\begin{aligned}
  \lim_{n \rightarrow \infty} \left(\frac{\RPFac(\RNrmByGRnd^{-1}-1)}{(\RNrmByGRnd^{-1}-1)(\RPFac-1)}-\frac{\RNrmByGRnd^{-1}(\RPFac-1)}{(\RNrmByGRnd^{-1}-1)(\RPFac-1)}\right)\RNrmByGRnd^{-n}-\left(\frac{\GPFacRaw^{-n}}{\RPFac-1}\right)  & = \infty.  
\end{aligned}$$
which makes clear that with $\cncl{\FHWC} \Rightarrow \RNrmByGRnd^{-1} > 1$ and $\cncl{\RIC} \Rightarrow \RPFac > 1$ the numerators and denominators of both terms multiplying $\RNrmByGRnd^{-n}$ can be seen transparently to be positive.
So, the terms multiplying
$\RNrmByGRnd^{-n}$ in [](#eq-FHWCfails) will be positive if
$$\begin{aligned}
  \RPFac \RNrmByGRnd^{-1} - \RPFac  & > & \RNrmByGRnd^{-1}\RPFac-\RNrmByGRnd^{-1}
  \\ \RNrmByGRnd^{-1}  & > & \RPFac
  \\ \PermGroFac  & > & \APFac
\end{aligned}$$
which is merely the  which we are maintaining.
So the first term’s limit is $+\infty$.
The
combined limit will be $+\infty$ if the term involving $\RNrmByGRnd^{-n}$
goes to $+\infty$ faster than the term involving $-\GPFacRaw^{-n}$ goes to
$-\infty$; that is, if
$$\begin{aligned}
  \RNrmByGRnd^{-1}  & > & \GPFacRaw^{-1}
  \\ \PermGroFac/\Rfree  & > & \PermGroFac/\APFac
  \\ \APFac/\Rfree  & > & 1
\end{aligned}$$
which merely confirms the starting assumption that the RIC fails.

What is happening here is that the $\cNrm_{\#}^{n}$ term is increasing backward in time at rate dominated in the limit by $\PermGroFac/\APFac$ while the $\bNrm_{\#}$ term is increasing at a rate dominated by $\PermGroFac/\Rfree$ term and
$$\begin{aligned}
  \PermGroFac/\Rfree & > & \PermGroFac/\APFac 
\end{aligned}$$
because $\cncl{\RIC} \Rightarrow \APFac > \Rfree$.

Consequently, while $\lim_{n \rightarrow \infty} \bNrm_{\#}^{n} = \infty$, the limit of the *ratio* $\cNrm_{\#}^{n}/\bNrm_{\#}^{n}$ in [](#eq-MPCConstrLim) is zero.
Thus, surprisingly, the problem has a well defined solution with
infinite human wealth if the RIC fails.
It remains true that
implies a limiting MPC of zero,
$$\begin{gathered}\begin{aligned}
  \lim_{\mNrm \rightarrow \infty} \cnstr{\pmb{\MPC}}(\mNrm)   & = 0,
\end{aligned}\end{gathered}$$
but that limit is approached gradually, starting from a positive value, and consequently the consumption function is *not* the degenerate $\cnstr{\cFunc}(\mNrm)=0$.
(Figure [](#PFGICHoldsFHWCFailsRICFails) presents an example for $\CRRA=2$, $\Rfree=0.98$, $\DiscFacRaw = 1.00$, $\PermGroFac = 0.99$; note that the horizontal axis is bank balances $\bNrm = \mNrm-1$; the part of the consumption function below the depicted points is uninteresting — $\cNrm = \mNrm$ — so not worth plotting).

(PFGICHoldsFHWCFailsRICFails)=

(fig-PFGICHoldsFHWCFailsRICFails)=

:::{figure} Figures/PFGICHoldsFHWCFailsRICFails.png
:name: fig-PFGICHoldsFHWCFailsRICFails
:width: 6in

Appendix: Nondegenerate $\cFunc$ Function with and
:::

We can summarize as follows.
Given that the  holds, the interesting question is whether the FHWC holds.
If so, the RIC automatically holds, and the solution limits into the solution to the unconstrained problem as $\mNrm \rightarrow \infty$.
But even if the FHWC fails, the problem has a well-defined and nondegenerate solution, whether or not the RIC holds.

Although these results were derived for the perfect foresight case, we know from work elsewhere in this paper and in other places that the perfect foresight case is an upper bound for the case with uncertainty.
If the upper bound of the MPC in the perfect foresight case is zero, it is not possible for the upper bound in the model with uncertainty to be greater than zero, because for any $\kappa > 0$ the level of consumption in the model with uncertainty would eventually exceed the level of consumption in the absence of uncertainty.

[(Ma and Toda, 2020)](#cite-maTodaRich) characterize the limits of the MPC in a more general framework that allows for capital and labor income risks in a Markovian setting with liquidity constraints, and find that in that much more general framework the limiting MPC is also zero.

(ApndxConditionDiagrams)=

# Relational Diagrams for the Inequality Conditions 

(sec-ApndxConditionDiagrams)=

This appendix explains in detail the paper’s ‘inequalities’ diagrams (Figures [](#RelatePFGICFHWCRICPFFVAC), [](#fig-Inequalities)).

(InequalityPFGICFHWCRIC)=

(fig-InequalityPFGICFHWCRIC)=

:::{figure} Figures/InequalityPFGICFHWCRIC.svg
:name: fig-InequalityPFGICFHWCRIC
:width: 4in

Appendix: Inequality Conditions for Perfect Foresight Model
:::

## The Unconstrained Perfect Foresight Model 

A simple illustration is presented in Figure [](#InequalityPFGICFHWCRIC), whose three nodes represent values of the absolute patience factor $\APFac$, the permanent-income growth factor $\PermGroFac$, and the riskfree interest factor $\Rfree$.
The arrows represent imposition of the labeled inequality condition (like, the uppermost arrow, pointing from $\APFac$ to $\PermGroFac$, reflects imposition of the condition (clicking should take you to its definition; definitions of other conditions are also linked below)).[^53]
Annotations inside parenthetical expressions containing $\equiv$ are there to make the diagram readable for someone who may not immediately remember terms and definitions from the main text.
(Such a reader might also want to be reminded that $\Rfree, \DiscFac,$ and $\Gamma$ are all in $\Reals_{++}$, and that $\CRRA>1$).

Navigation of the diagram is simple: Start at any node, and deduce a chain of inequalities by following any arrow that exits that node, and any arrows that exit from successive nodes.
Traversal must stop upon arrival at a node with no exiting arrows.
So, for example, we can start at the $\APFac$ node and impose the and then the FHWC, and see that imposition of these conditions allows us to conclude that $\APFac < \Rfree$.

One could also impose $\APFac < \Rfree$ directly (without imposing $\GICRaw$ and $\FHWC$) by following the downward-sloping diagonal arrow exiting $\APFac$.
Although alternate routes from one node to another all justify the same core conclusion ($\APFac < \Rfree$, in this case), $\neq$ symbol in the center is meant to convey that these routes are not identical in other respects.
This notational convention is used in [category theory diagrams](https://en.wikipedia.org/wiki/Diagram_(category_theory)),[^54] to indicate that the diagram is not [commutative](https://en.wikipedia.org/wiki/Commutative_diagram).[^55]

Negation of a condition is indicated by the reversal of the corresponding arrow.
For example, negation of the RIC, $\cncl{\RIC} \equiv \APFac > \Rfree$, would be represented by moving the arrowhead from the bottom right to the top left of the line segment connecting $\APFac$ and $\Rfree$.

If we were to start at $\Rfree$ and then impose $\cncl{\FHWC}$, that would reverse the arrow connecting $\Rfree$ and $\PermGroFac$, but the $\PermGroFac$ node would then have no exiting arrows so no further deductions could be made.
However, if we *also* reversed $\GICRaw$ (that is, if we imposed $\cncl{\GICRaw}$), that would take us to the $\APFac$ node, and we could deduce $\Rfree > \APFac$.
However, we would have to stop traversing the diagram at this point, because the arrow exiting from the $\APFac$ node points back to our starting point, which (if valid) would lead us to the conclusion that $\Rfree > \Rfree$.
Thus, the reversal of the two earlier conditions (imposition of $\cncl{\FHWC}$ and $\cncl{\GICRaw}$) requires us also to reverse the final condition, giving us $\cncl{\RIC}$.[^56]

Under these conventions, Figure [](#RelatePFGICFHWCRICPFFVAC) [in the main text](#RelatePFGICFHWCRICPFFVAC) presents a modified version of the diagram extended to incorporate the PF-FVAC.

This diagram can be interpreted, for example, as saying that, starting at the $\APFac$ node, it is possible to derive the $\PFFVAC$[^57] by imposing both the and the FHWC; or by imposing RIC and .
Or, starting at the $\PermGroFac$ node, we can follow the imposition of the FHWC (twice — reversing the arrow labeled $\cncl{\FHWC}$) and then $\cncl{\RIC}$ to reach the conclusion that $\APFac < \PermGroFac$.
Algebraically,
(eq-cnclGICRaw)=
$$\begin{gathered}\begin{aligned}
  {\FHWC}:~~~ \PermGroFac & < \Rfree 
  \\ \cncl{\RIC}:~~~ \Rfree & < \APFac 
  \\ \PermGroFac & < \APFac 
\end{aligned}\end{gathered}$$
which leads to the negation of both of the conditions leading into $\APFac$.
is obtained directly as the last line in [](#eq-cnclGICRaw) and follows if we start by multiplying the Return Patience Factor (=$\APFac/\Rfree$) by the (=$\PermGroFac/\Rfree$) raised to the power $1/\CRRA-1$, which is negative since we imposed $\CRRA > 1$.
FHWC implies $< 1$ so when is raised to a negative power the result is greater than one.
Multiplying the (which exceeds 1 because ) by another number greater than one yields a product that must be greater than one:
(eq-cnclFHWFacDefnAndcnclRICImplycnclPFFVAC)=
$$\begin{gathered}\begin{aligned}
  1  & < \overbrace{\left(\frac{{(\Rfree \DiscFac)}^{1/\CRRA}}{\Rfree}\right)}^{>1 \text{~from~}\cncl{\RIC}}\overbrace{{\left(\PermGroFac/\Rfree\right)}^{1/\CRRA-1}}^{\phantom{\ldots}>1~\text{~from~} \FHWC} \notag
  \\ 1  & < \left(\frac{{(\Rfree \DiscFac)}^{1/\CRRA}}{{(\Rfree/\PermGroFac)}^{1/\CRRA}\Rfree\PermGroFac/\Rfree}\right) 
  \\ \Rfree^{1/\CRRA}\PermGroFac^{1 - 1/\CRRA} = {(\Rfree/\PermGroFac)}^{1/\CRRA} \PermGroFac  & < \APFac \notag
\end{aligned}\end{gathered}$$
which is one way of writing $\cncl{\PFFVAC}$.

The complexity of this algebraic calculation illustrates the usefulness of the diagram, in which one merely needs to follow arrows to reach the same result.

After the warmup of constructing these conditions for the perfect foresight case, we can represent the relationships between all the conditions in both the perfect foresight case and the case with uncertainty as shown in Figure [](#fig-Inequalities) in the paper (reproduced here).

(fig-InequalitiesApp)=

:::{figure} Figures/Inequalities.svg
:name: fig-InequalitiesApp
:width: 6in

Appendix: Relation of All Inequality Conditions
:::

Finally, the next diagram substitutes the values of the various objects in the diagram under the baseline parameter values and verifies that all of the asserted inequality conditions hold true.

(fig-InequalitiesAppNumer)=

:::{figure} Figures/Inequalities-numer.svg
:name: fig-InequalitiesAppNumer
:width: 6in

Appendix: Numerical Relation of All Inequality Conditions
:::

# Additional Standard Results 

(sec-realanalysis)=

(fact-xnconvgf)=
:::{prf:proposition}
:label: fact-xnconvgf

Let $\fFunc: \Reals_{++} \to \Reals_{+}$ be a continuous function. Consider sequences $x^{n}$ in $\Reals_{++}$ and $\fFunc^n(x^{n})$ in $\Reals_{+}$. If $\fFunc^{n}(x^{n}) \to \fFunc(x)$ as $n \to \infty$, then $x^{n} \to x$ as $n \to \infty$.

:::

:::{prf:proof}

Given that $\fFunc$ is continuous at $x$ (with $x \in \Reals_{++}$), for every $\epsilon > 0$, there exists a $\delta > 0$ such that for all $y$ in $\Reals_{++}$ with $\vert y - x\vert < \delta$, we have $\vert \fFunc(y) - \fFunc(x)\vert  < \epsilon$.

Given $\fFunc^{n}(x^{n}) \to \fFunc(x)$, for the above $\epsilon$, there exists an $N$ such that for all $n > N$, $\vert \fFunc^{n}(x^{n}) - \fFunc(x)\vert < \epsilon$.

Assume for the sake of contradiction that $x^{n}$ doesn’t converge to $x$.
This implies that there exists a $\delta > 0$ such that for infinitely many terms of the sequence $x^{n}$, $\vert x^{n} - x\vert  \geq \delta$.

By the continuity of $\fFunc$ at $x$, if $\vert x^{n} - x\vert  \geq \delta$ for infinitely many $n$, then $\vert \fFunc^{n}(x^{n}) - \fFunc(x)\vert  \geq \epsilon$ for those $n$, contradicting our assumption that $\fFunc^{n}(x^{n}) \to \fFunc(x)$.

Therefore, our assumption for contradiction is false, and it follows that $x^{n} \to x$ as $n \to \infty$.

:::

(fact-normimpliescompact)=
:::{prf:remark}
:label: fact-normimpliescompact

Let $\gFunc: X \to \Reals_{+}$ be a continuous function, where $X \subseteq \Reals^{n}$ is an open convex set.
Define the weighted supremum norm $\Vert\cdot \Vert_{\gFunc}$ of a real-valued function $\fFunc: X \to \Reals$ by
$$\Vert \fFunc \Vert_\gFunc := \sup_{x \in X} \frac{\vert \fFunc(x)\vert }{\gFunc(x)}.$$
If $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc^{\star} \Vert_\gFunc = 0$, $\fFunc_n$ converges to $\fFunc^{\star}$ uniformly on compact sets.

:::

:::{prf:proof}

Let $\tilde{X}$ be an arbitrary compact subset of $X$.
Since $\tilde{X}$ is compact, there exists a positive lower bound for $\gFunc$ on this subset, denoted as
$$\bar{\gFunc} = \min_{x \in \tilde{X}} \gFunc(x) > 0.$$
Hence, on $\tilde{X}$, if $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc^{\star} \Vert_\gFunc = 0$, then $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc^{\star} \Vert_\infty = 0$ on $\tilde{X}$, where $\Vert \cdot \Vert_\infty$ denotes the supremum norm.

Now, let $K$ be a compact subset of $X$.
Given the continuity of $\gFunc$, there exists a positive maximum value for $\gFunc$ on $K$, denoted as $M_K$.
Then, we have
$$\sup_{x \in K} \vert \fFunc_n(x) - \fFunc(x)\vert  \leq M_K \sup_{x \in K} \frac{\vert \fFunc_n(x) - \fFunc(x)\vert }{\gFunc(x)} \leq M_K \sup_{x \in X} \frac{\vert \fFunc_n(x) - \fFunc(x)\vert }{\gFunc(x)}.$$
Thus, $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc \Vert_  = 0$ implies that $\fFunc_n$ converges uniformly to $\fFunc$ on the compact set $K$.
It’s also worth noting that the convexity and openness of $X$ aren’t strictly necessary for this argument.

:::

(fact-compactnt)=
:::{prf:remark}
:label: fact-compactnt

Let $\{\fFunc_n\}$ be a sequence of continuous functions defined on a subset of the real line and converging uniformly to a function$\fFunc$ on compact sets.
If$\{x_n\}$ is a convergent sequence of real numbers with limit $x$, then $\fFunc_n(x_n)$ converges to $\fFunc(x)$.

:::

:::{prf:proof}

Let $\tilde{X}$ be an arbitrary compact subset of $X$.
Since $\tilde{X}$ is compact, there exists a positive lower bound for $\gFunc$ on this subset, denoted as
$$\bar{\gFunc} = \min_{x \in \tilde{X}} \gFunc(x) > 0.$$
Hence, on $\tilde{X}$, if $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc^{\star} \Vert_\gFunc = 0$, then $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc^{\star} \Vert_\infty = 0$ on $\tilde{X}$, where $\Vert \cdot \Vert_\infty$ denotes the supremum norm.

Now, let $K$ be a compact subset of $X$.
Given the continuity of $\gFunc$, there exists a positive maximum value for $\gFunc$ on $K$, denoted as $M_K$.
Then, we have
$$\sup_{x \in K} \vert \fFunc_n(x) - \fFunc(x)\vert  \leq M_K \sup_{x \in K} \frac{\vert \fFunc_n(x) - \fFunc(x)\vert }{\gFunc(x)} \leq M_K \sup_{x \in X} \frac{\vert \fFunc_n(x) - \fFunc(x)\vert }{\gFunc(x)}.$$
Thus, $\lim_{n \to \infty} \Vert \fFunc_n - \fFunc \Vert_  = 0$ implies that $\fFunc_n$ converges uniformly to $\fFunc$ on the compact set $K$.
It’s also worth noting that the convexity and openness of $X$ aren’t strictly necessary for this argument.

:::

(claim-rationondec)=
:::{prf:property}
:label: claim-rationondec

If $\fFunc$ is convex and $\fFunc < 0$ on $(0, \lambda)$, then $\frac{\fFunc(s)}{s}$ is increasing on $(0, \lambda)$.

:::

:::{prf:proof}

Let $\fFunc$ be convex on $(0, \lambda)$ and $\fFunc < 0$ on $(0, \lambda)$.
Let $x_1$ and $x_2$ be two points in $(0, \lambda)$.
Choose $0 < \alpha < x_1$.
Then, any point (in particular, $x_1$) in $(\alpha, x_2)$ can be written as $x_1 = t \alpha + (1 - t) x_2$ for some $0 < t < 1$.

Now, define a new function $F$ on $[\alpha, x_2]$ as:
$$F(x) = \fFunc(x) - \fFunc(\alpha).$$
Since $\fFunc$ is convex, $F(x)$ is also convex on $[\alpha, x_2]$.
To see this, observe that:
$$F(t\alpha + (1-t)x_2) = \fFunc(t\alpha + (1-t)x_2) - \fFunc(\alpha) \leq t \fFunc(\alpha) + (1-t) \fFunc(x_2) - \fFunc(\alpha) = t F(\alpha) + (1-t) F(x_2).$$
Since $F(\alpha) = 0$, the inequality simplifies to $F(x_1) \leq (1-t) F(x_2)$.
This implies that $\frac{F(s)}{s}$ is increasing.
And thus, if $y_1 \leq y_2$, then:
$$\frac{F(y_1)}{y_1} \leq \frac{F(y_2)}{y_2}.$$
Now, using the definition of $F(x)$, we have:
$$\frac{\fFunc(y_1)}{y_1} = \frac{F(y_1)}{y_1} + \frac{\fFunc(\alpha)}{y_1}.$$
Similarly, for $y_2$:
$$\frac{\fFunc(y_2)}{y_2} = \frac{F(y_2)}{y_2} + \frac{\fFunc(\alpha)}{y_2}.$$
Since $\frac{F(y_1)}{y_1} \leq \frac{F(y_2)}{y_2}$ and $\fFunc(\alpha) < 0$, we conclude that:
$$\frac{\fFunc(y_1)}{y_1} \leq  \frac{\fFunc(y_2)}{y_2}.$$

Thus, $\frac{\fFunc(s)}{s}$ is increasing on $(0, \lambda)$, completing the proof.

:::

[^1]: In [(Carroll, 1992)](#cite-carroll-brookings).

[^2]: [(Carroll, 1997)](#cite-carrollBSLCPIH), [(Gourinchas and Parker, 2002)](#cite-gpLifeCycle)

[^3]: It is our view that the principal reason much of the literature has incorporated extremely ‘persistent’ but not completely permanent shocks is that the theoretical foundations for the case with permanent shocks have not previously been available.

[^4]: The ‘natural’ constraint arises as a consequence of the budget constraint and the CRRA utility function which implies that the utility of consuming zero is negative infinity. Its implications were first explored by [(Zeldes, 1989)](#cite-zeldesStochastic) in a life cycle context. [(Carroll, 1992)](#cite-carroll-brookings) analyzed the infinite horizon case, and [(Aiyagari, 1994)](#cite-aiyagari-ge) coined the term ‘natural borrowing constraint.’

[^5]: [(Fisher, 1930)](#cite-fisherInterestTheory) in Ch. IV, Section 3 states "I shall treat the two terms (impatience and time preference) as synonymous".

[^6]: The paper’s insights are instantiated in the Econ-ARK toolkit, whose [buffer stock saving module](https://hark.readthedocs.io/en/stable/reference/ConsumptionSaving/ConsIndShockModel.html) flags parametric choices under which a problem is degenerate or under which stable ratios of wealth to income may not exist.

[^7]: [(Deaton, 1991)](#cite-deatonLiqConstr) also showed that impatient consumers facing only permanent shocks would end up remaining on the borrowing constraint forever, an insight that informs the work of [(Kaplan, Violante, and Weidner, 2014)](#cite-kvwWealthyH2m).

[^8]: Our CRRA utility function does not satisfy Bewley’s assumption that $\uFunc(0)$ is well-defined, or that $\uP(0)$ is bounded above.
    Our approach differs from that of Schechtman and Escudero [((1977))](#cite-seIncFluct) because they impose an artificial borrowing constraint and positive minimum income.
    It differs from Deaton [((1991))](#cite-deatonLiqConstr) because he imposes liquidity constraints; we accommodate separate transitory and permanent shocks; and our transitory shocks occasionally cause income to reach zero.
    Papers by Scheinkman and Weiss [((1986))](#cite-scheinkman-weiss-borrowing), Clarida [(Clarida, 1987)](#cite-claridaErgodic), and others [(Chamberlain and Wilson, 2000)](#cite-cwcUnderUncert) all differ from ours for reasons resembling those articulated above.

    [(Alvarez and Stokey, 1998)](#cite-asHomogeneous) relaxed boundedness of the utility function, but they address only the deterministic case; [(Martins-da Rocha and Vailakis, 2010)](#cite-mvExistence)’s correction to [(Rincón-Zapatero and
  Rodríguez-Palmero, 2003)](#cite-rrExistence) only addresses the deterministic case.
    [(Matkowski and Nowak, 2011)](#cite-mnUnique) assume a framework with compact action sets and real-valued utility which cannot handle relative risk aversion greater than 1.

    Two approaches do allow relative risk aversion greater than 1: A literature employing time iteration operators defined by Euler equations [(Deaton, 1991; Li and Stachurski, 2014; Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct), and one that employs transformations of the Bellman equation [(Rincón-Zapatero, 2024)](#cite-rinconZapatero2024), but in all of these cases an artificial borrowing constraint is present (or its moral equivalent, as in Bewley).

[^9]: [(Alvarez and Stokey, 1998)](#cite-asHomogeneous) showed how the approach could be used to address the homogeneous case (of which CRRA is an example) in a deterministic framework; later, [(Durán, 2003)](#cite-duranDiscounting) showed how to extend the [(Boyd, 1990)](#cite-jboydWeighted) approach to the stochastic case.
    See also the exposition by [(Stachurski, 2022)](#cite-stachurski2022), Ch 12.

[^10]: Formally, we assume $\left\{\permShk_{t},\tranShkAll_{t}\right\}_{t=-\infty}^{T}$ is a sequence of iid random variables defined on a common probability space $(\Omega, \Sigma, \mathbb{P})$. When used without the time subscript, $\permShk$ and $\tranShkAll$ are the canonical random variables with distributions $\mathbb{P}\circ \permShk_{0}^{-1}$ and $\mathbb{P}\circ \tranShkAll_{0}^{-1}$, respectively.

[^11]: For maximal clarity, we have separately described every step in the dynamic budget evolution.
    The steps are broken down also so that the notation of the paper will correspond exactly to the variable names in the [t](https://github.com/econ-ark/HARK)oolkit, because it is required for solving life cycle problems.

[^12]: A time-varying $\PermGroFac$ has straightforward consequences for the analysis below; this is an option allowed for in the [HARK](https://econ-ark.org) toolkit.

[^13]: While much of the literature employs an income process that is persistent but not permanent, evidence of the presence and large size of permanent (or very nearly permanenent) shocks has long been observed in micro data.
    ([(Lillard and Weiss, 1979)](#cite-lwComponents), MaCurdy [((1982))](#cite-macurdyTimeseries); Abowd and Card [((1989))](#cite-acCovariance); Carroll and Samwick [((1997))](#cite-csNature); Jappelli and Pistaferri [2000](#cite-jpCins); et. seq.)
    [(Daly, Hryshko, and Manovskii, 2016)](#cite-dhmImproving) show that when measurement problems are handled correctly, administrative data yield serial correlation coefficients $0.98-1.00$; and [(Hryshko and Manovskii, 2020)](#cite-dmHowMuch) suggests that survey data support the same conclusion. Most recently [(Crawley, Holm, and Tretvoll, 2022)](#cite-crawleyParsimonious) use data from the Norwegian national registry that encompass millions of observations over along time span, and argue that the parsimonious specification with permanent shocks is preferable to one that allows a persistent shock with a serial correlation coefficient very close to 1.

[^14]: We specify zero as the lowest-possible-income event without loss of generality [(Aiyagari, 1994)](#cite-aiyagari-ge).

[^15]: So long as unemployment benefits are proportional to $\permLvl_{t}$; see the discussion in Section [](#subsubsec-ratio).

[^16]: We omit $\kNrm$ from this transition because our assumption that $\kLvl_{t+1}=\aLvl_{t}$ could lead to confusion about whether do denote $\kNrm_{t+1}=\aNrm_{t}$ or $\kNrm_{t+1}=a_{t}/\PermGroFacRnd_{t+1}$.

[^17]: The challenge of continuity and compactness remains unresolved in a general setting [(Rincón-Zapatero, 2024)](#cite-rinconZapatero2024).
    Relevant results include [(Feinberg, Kasyanov, and Zadoianchuk, 2012)](#cite-Feinberg2012), who generalize the requirement of continuity of feasibility correspondences to K-Inf-Compactness of the Bellman operator, yielding a mapping from semi-continuous to semi-continuous functions.
    [(Shanker, 2017)](#cite-Shanker2017a) introduces a generalization, mild-Sup-compactness, which can be verified in the weak topology generated on the infinite dimensional product space of feasible random variables controlled by the consumers.
    Our approach, by contrast, has the advantage that it can be used to verify existence using more standard tools.

[^18]: In light of Remark [](#remark-stochdiscMST), [(Ma, Stachurski, and Toda, 2020)](#cite-mstIncFluct) Assumption 2.1 is a generalization of this discount condition, albeit in a context with artificial liquidity constraints.

[^19]: See [](#eq-cGroFac) below.

[^20]: [(Carroll and Kim{}ball, 1996)](#cite-ckConcavity) proved concavity but not continuous differentiability.

[^21]: Note $\usual{\cFunc}_{t}^{\prime}$ is positive, bounded above by 1 and decreasing, then apply L’Hôpital’s Rule.

[^22]: [(Benhabib, Bisin, and Zhu, 2015)](#cite-benhabibWealth) show that the consumption function becomes linear as wealth approaches infinity in a model with capital income risk and liquidity constraints; [(Ma and Toda, 2020)](#cite-maTodaRich) show that these results generalize to the limits derived here if capital income is added to the model.

[^23]: None of the arguments in either of the two prior sections depended on the assumption that the consumption functions had converged.
    With more cumbersome notation, each derivation could have been replaced by the corresponding finite-horizon versions.
    This strongly suggests that it should be possible to extend the circumstances under which the problem can be shown to define a contraction mapping to the union of the parameter values under which {RIC,FHWC} hold and {FVAC,WRIC} hold.
    That extension is not necessary for our purposes here, so we leave it for future work.

[^24]: The figure is generated using parameters discussed in Section [](#sec-GICdiscussion), Table [](#Symbols).

[^25]: A third ‘stable point’ is the $\mBalLog$ where $\Ex_{t}[\log \mLvl_{t+1}] = \log \PermGroFac \mLvl_{t}$; this can be conveniently rewritten as $\Ex_{t}\left[\log\left((\mBalLog-\usual{\cFunc}(\mBalLog))\RNrmByGRnd+\permShk_{t+1}\tranShkAll_{t+1}\right)\right]  = \log \mBalLog_{t}$.
    Because the expectation of the log of a stochastic variable is less than the log of the expectation, if a solution for $\mBalLog$ exists it will satisfy $\mBalLog > \mBalLvl$; in turn, if $\mTrgNrm$ exists, $\mTrgNrm>\mBalLog$.
    The target $\mBalLog$ is guaranteed to exist when the [log growth impatience](#GICSdl) condition is satisfied (see below).
    For our purposes, little would be gained by an analysis of this point parallel to those of the other points of stability; but to accommodate potential practical uses, the Econ-ARK toolkit computes the value of this point (when it exists) as `mBalLog`.

[^26]: [(Szeidl, 2013)](#cite-szeidlInvariant)’s impatience condition, discussed below, also tightens as uncertainty increases, but this is also not a consequence of a precaution-induced increase in patience – it represents an increase in the tightness of the requirements of the ‘mixing condition’ used in his proof.

[^27]: Still, the pseudo-target can be calculated from the policy function without any simulation, and therefore serves as a low-cost starting point for the numerical simulation process; see [Harmenberg-Aggregation](https://econ-ark.org/materials/harmenberg-aggregation?launch) for an example.

[^28]: [(Szeidl, 2013)](#cite-szeidlInvariant)’s equation (9), in our notation, is:
    $$\begin{gathered}\begin{aligned}
        \Ex \log \Rfree (1-\MPC) & < \Ex \log \PermGroFac \permShk
        \\  \Ex \log \Rfree \RPFac  &  < \Ex \log \PermGroFac \permShk
        \\ \log \GPFacRaw & < \Ex \log \permShk
      \end{aligned}\end{gathered}$$
    which, exponentiated, yields [](#GICSdl).

[^29]: Under our default (though not required) assumption that $\log \permShk \sim \mathcal{N}(-\sigma^{2}_{\permShk}/2,\sigma^{2}_{\permShk})$; [strong growth impatience](#GICMod) in this case, is $\GPFacRaw < \exp(-\sigma^{2})$, so if [strong growth impatience](#GICMod) holds then Szeidl’s condition will hold.

[^30]: In the notation in [(Harmenberg, 2021a)](#cite-harmenbergInvariant), the *permanent-income-weighted* measures are denoted as $\tilde{\psi}^{\mNrm}$.

[^31]: The Harmenberg method is implemented in the Econ-ARK; see the last part of [`test_Harmenbergs_method.sh`](https://github.com/econ-ark/BufferStockTheory/blob/master/Code/Python/test_Harmenbergs_method.sh).
    Confirming the computational advantage of Harmenberg’s method, [this notebook](https://econ-ark.org/materials/harmenberg-aggregation) finds that the Harmenberg method reduces the simulation size required for a given degree of accuracy by two orders of magnitude under the baseline parameter values defined above.

[^32]: Formally, fix an individual $i$ and let $\{\tilde{c}^{i}_{t}\}_{t=0}^{\infty}$ and $\{\tilde{m}^{i}_{t}\}_{t=0}^{\infty}$ be a stochastic recursive sequence generated by the converged consumption rule as follows, $\tilde{c}^{i}_{t} = \cFunc(\tilde{\mNrm}^{i}_{t})$ and $\tilde{\mNrm}^{i}_{t+1} = \RNrmByGRnd^{i}_{t+1}(\tilde{\mNrm}^{i}_{t} -\cFunc(\tilde{\mNrm}^{i}_{t})) + \tranShkAll^{i}_{t+1}$, where the sequence of exogenous shocks are each defined on a *theoretical probability space* $(\Omega, \Sigma, \mathbb{P})$.
    Integration with respect to the measure $\mathbb{P}$ in the expected value operator $\Ex$ will be equivalent to *empirical* integration $\mathbb{M}$ with respect to a suitable measure of agents on a nonatomic agent space.
    In particular, for all $j$, $\Ex\gFunc(\tilde{\cNrm}_{t}^{j})  = \int \tilde{\cNrm}_{t}\,d\mathbb{P} =  \Mean\gFunc(\tilde{c}_{t}):= \int \gFunc(\tilde{\cNrm}_{t}^{i}) \lambda(di)$, where $\lambda$ is the measure of agents and for any measurable function $\gFunc$.
    For technical steps required to assert this claim, see [(Shanker, 2017)](#cite-Shanker2017a), which utilizes relatively recent results by [(Sun and Zhang, 2009)](#cite-Sun2009) and also the detailed construction by [(Cao, 2020)](#cite-Cao2020).

[^33]: This ‘if’ is a conjecture, not something proven by Harmenberg (or anyone else).
    But see appendix [](#sec-ApndxBalancedGrowthcNrmAndCov) for an example of a Harmenberg-invariant economy in which simulations suggest this proposition holds.

[^34]: Parallel results to those for consumption can be obtained for other measures like market assets.

[^35]: Recall Claim [](#VAFacDefn) showing that a double-impatience failure implies autarky value is not finite; and see

[^36]: This logic holds even if both $\Rfree$ and $\PermGroFac$ are less than one – in this case, because the agent can *borrow* at a negative interest rate and always repay with income that shrinks more slowly than their debt.

[^37]: Consult Appendix [](#sec-ApndxConditionDiagrams) for an exposition of diagrams of this type, which are a simple application of Category Theory ([(Riehl, 2017)](#cite-riehl2017category)).

[^38]: “Somehow” because $\mNrm<1$ could only be obtained by entering the period with $\bNrm < 0$ which the constraint forbids.

[^39]: See [(Carroll, Holm, and Kimball, 2019)](#cite-chkLiqConstr) for details.

[^40]: That is, one obeying $\cFunc(\mNrm) = \lim\limits_{n \rightarrow \infty} \cFunc_{t-n}(\mNrm)$.

[^41]: Again, readers unfamiliar with such diagrams should see Appendix [](#sec-ApndxConditionDiagrams) for a more detailed exposition.

[^42]: This algebraically complicated conclusion could be easily reached diagrammatically in Figure [](#fig-Inequalities) by starting at the $\Rfree$ node and imposing the failure of [return impatience](#RIC), which reverses the [return impatience](#RIC) arrow and lets us traverse the diagram along any clockwise path to the [perfect foresight finite value of autarky](#PFFVAC) node at which point we realize that we *cannot* impose [finite human wealth](#ass-FHWC) because that would let us conclude $\Rfree > \Rfree$.

[^43]: [(Ma and Toda, 2020)](#cite-maTodaRich) derive conditions under which the limiting MPC is zero in an even more general case where there is also capital income risk.

[^44]: Note that the maximand on the RHS of Equation [](#eq-condition1) is continuous (Claim [](#clm-hiraguchi_cont)) and the feasible set of consumption choices is compact-valued.
    As such, a solution to the maximization problem exists for any $\mNrm_{t}$.
    Thus, letting $\Theta$ be the solution correspondence for the maximization problem, $\Theta(\mNrm_{t})$ will be non-empty and will admit a selector function $\breve{\cFunc}$.
    See Section 17.11 in [(Aliprantis and Border, 2006)](#cite-Aliprantis2005).

[^45]: $\displaystyle \lim\limits_{\mNrm_{t}\rightarrow \infty} \aFunc(\mNrm_{t})/\mNrm_{t}=1-\lim_{\mNrm_{t}\rightarrow \infty} \usual{\cFunc}(\mNrm_{t})/\mNrm_{t}=1-\lim_{\mNrm_{t}\rightarrow \infty}\usual{\cFunc}^{\prime}(\mNrm_{t})=\RPFac$.

[^46]: For an exposition of our implementation of Harmenberg’s method, see [this supplemental appendix.](https://github.com/econ-ark/BufferStockTheory/blob/master/Appendices/ApndxHarKmenberg.pdf)

[^47]: The point at
    which the constraint would bind (if that point could be attained) is
    the $\mNrm=\cNrm$ for which $\uFunc^{\prime}(\cNrm_{\#}) = \Rfree
      \DiscFacRaw \uFunc^{\prime}(\PermGroFac)$ which is $\cNrm_{\#} =
      \PermGroFac/{(\Rfree \DiscFacRaw)}^{1/\CRRA}$ and the consumption function
    will be defined by
    $\cnstr{\cFunc}(\mNrm)=\min[\mNrm,\cNrm_{\#}+(\mNrm-\cNrm_{\#})\MPCmin
      ]$.

[^48]: The knife-edge case is where $\APFac = \PermGroFac$, in
    which case the two quantities counterbalance and the limiting
    function is $\cnstr{\cFunc}(\mNrm)=\min[\mNrm,1]$.

[^49]: Note that $0 < \mNrm_{\#}$ is implied by RIC and $\mNrm_{\#}<1$ is implied by .

[^50]: As an
    illustration, consider a consumer for whom $\APFac = 1$, $\Rfree
      =1.01$ and $\PermGroFac = 0.99$.
    This consumer will save the amount
    necessary to ensure that growth in market wealth exactly offsets the
    decline in human wealth represented by $\PermGroFac < 1$; total wealth
    (and therefore total consumption) will remain constant, even as
    market wealth and human wealth trend in opposite directions.

[^51]: Calculate the limit of
    $$\begin{gathered}\begin{aligned}
        \left(\frac{\GPFacRaw^{-n}}{\GPFacRaw^{-n}/(1-\RPFac) - (1-\RNrmByGRnd^{-1}\RNrmByGRnd^{-n})/(1-\RNrmByGRnd^{-1})}\right)  & = \left(\frac{1}{1/(1-\RPFac) + \RNrmByGRnd^{-n}\RNrmByGRnd^{-1}/(1-\RNrmByGRnd^{-1})}\right)
      \end{aligned}\end{gathered}$$

[^52]: For an example of this configuration of parameters, see the notebook `doApndxLiqConstr.nb` in the Mathematica software archive.

[^53]: For convenience, the equivalent ($\equiv$) mathematical statement of each condition is expressed nearby in parentheses.

[^54]: For a popular introduction to category theory, see [(Riehl, 2017)](#cite-riehl2017category).

[^55]: But the rest of our notation does not necessarily abide by the other conventions of category theory diagrams.

[^56]: The corresponding algebra is
(eq-cnclRIC)=
$$\begin{gathered}\begin{aligned}
      \cncl{\FHWC}:~~~~  \Rfree & < \PermGroFac \notag  
      \\ \cncl{\GICRaw}:~~~~ \PermGroFac & < \APFac 
                                    
      \\ \Rightarrow \cncl{\RIC}:~~~~\Rfree & < \APFac \notag,
    \end{aligned}\end{gathered}$$.

[^57]: in the form $\APFac < {(\Rfree/\PermGroFac)}^{1/\CRRA}\PermGroFac$

## References

(cite-acCovariance)=
Abowd, John M., and David Card (1989): “On the Covariance Structure of Earnings and Hours Changes,” *Econometrica*, 57, 411–445

(cite-aiyagari-ge)=
Aiyagari, S. Rao (1994): “Uninsured Idiosyncratic Risk and Aggregate Saving,” *Quarterly Journal of Economics*, 109, 659–684

(cite-Aliprantis2005)=
Aliprantis, Charalambos D., and Kim C Border (2006): *Infinite Dimensional Analysis: A Hitchhiker's Guide*. Springer-Verlag, Berlin, 3 edn

(cite-asHomogeneous)=
Alvarez, Fernando, and Nancy L Stokey (1998): “Dynamic programming with homogeneous functions,” *Journal of economic theory*, 82(1), 167–189

(cite-benhabibWealth)=
Benhabib, Jess, Alberto Bisin, and Shenghao Zhu (2015): “The wealth distribution in Bewley economies with capital income risk,” *Journal of Economic Theory*, 159, 489–515, Available at <https://www.nber.org/papers/w20157.pdf>

(cite-bertsekas2012dynamic)=
Bertsekas, D. (2012): *Dynamic Programming and Optimal Control: Volume II; Approximate Dynamic Programming*, Athena Scientific optimization and computation series. Athena Scientific

(cite-bewleyPIH)=
Bewley, Truman (1977): “The Permanent Income Hypothesis: A Theoretical Formulation,” *Journal of Economic Theory*, 16, 252–292

(cite-blanchardFinite)=
Blanchard, Olivier J. (1985): “Debt, Deficits, and Finite Horizons,” *Journal of Political Economy*, 93(2), 223–247

(cite-jboydWeighted)=
Boyd, John H. (1990): “Recursive Utility and the Ramsey Problem,” *Journal of Economic Theory*, 50(2), 326–345

(cite-Cao2020)=
Cao, Dan (2020): “Recursive equilibrium in Krusell and Smith (1998),” *Journal of Economic Theory*, 186, 104978

(cite-carroll-brookings)=
Carroll, Christopher D. (1992): “The Buffer-Stock Theory of Saving: Some Macroeconomic Evidence,” *Brookings Papers on Economic Activity*, 1992(2), 61–156

(cite-carrollBSLCPIH)=
———{} (1997): “Buffer Stock Saving and the Life Cycle/Permanent Income Hypothesis,” *Quarterly Journal of Economics*, CXII(1), 1–56

(cite-BufferStockTheoryQESubmit)=
———{} (2019, Submitted): “Theoretical Foundations of Buffer Stock Saving,” *Quantitative Economics*

(cite-ckConcavity)=
Carroll, Christopher D., and Miles S. Kimball (1996): “On the Concavity of the Consumption Function,” *Econometrica*, 64(4), 981–992, <https://www.econ2.jhu.edu/people/ccarroll/concavity.pdf>

(cite-csNature)=
Carroll, Christopher D., and Andrew A. Samwick (1997): “The Nature of Precautionary Wealth,” *Journal of Monetary Economics*, 40(1), 41–71

(cite-chkLiqConstr)=
Carroll, Christopher D., Martin Holm, and Miles S. Kimball (2019): “Liquidity Constraints and Precautionary Saving,” *\href{https://www.econ2.jhu.edu/people/ccarroll/papers/LiqConstr}{Manuscript, Johns Hopkins University}*, <https://www.econ2.jhu.edu/people/ccarroll/papers/LiqConstr>

(cite-cstwMPC)=
Carroll, Christopher D., Jiri Slacalek, Kiichi Tokuoka, and Matthew N. White (2017): “The Distribution of Wealth and the Marginal Propensity to Consume,” *Quantitative Economics*, 8(3), 977–1020, At <https://llorracc.github.io/cstwMPC>

(cite-cwcUnderUncert)=
Chamberlain, Gary, and Charles A. Wilson (2000): “Optimal Intertemporal Consumption Under Uncertainty,” *Review of Economic Dynamics*, 3(3), 365–395

(cite-carroll_et_al-proc-scipy-2018)=
Christopher D. Carroll, Alexander M. Kaufman, Jacqueline L. Kazil, Nathan M. Palmer, and Matthew N. White (2018): “The Econ-ARK and HARK: Open Source Tools for Computational Economics,” in *Proceedings of the 17th Python in Science Conference*, ed. by Fatih Akici, David Lippa, Dillon Niederhut, and M Pacer, pp. 25–30

(cite-claridaErgodic)=
Clarida, Richard H. (1987): “Consumption, Liquidity Constraints, and Asset Accumulation in the Face of Random Fluctuations in Income,” *International Economic Review*, XXVIII, 339–351

(cite-crawleyParsimonious)=
Crawley, E, Martin B Holm, and Hå{}kon Tretvoll (2022): “{A parsimonious model of idiosyncratic income},” *Finance and economics discussion series*

(cite-dhmImproving)=
Daly, Moira, Dmytro Hryshko, and Iourii Manovskii (2016): “Improving the measurement of earnings dynamics,” Discussion paper, National Bureau of Economic Research

(cite-deatonLiqConstr)=
Deaton, Angus S. (1991): “Saving and Liquidity Constraints,” *Econometrica*, 59, 1221–1248, <https://www.jstor.org/stable/2938366>

(cite-dhprvInequality)=
DeBacker, Jason, Bradley Heim, Vasia Panousi, Shanthi Ramnath, and Ivan Vidangos (2013): “Rising Inequality: Transitory or Persistent? New Evidence from a Panel of U.S. Tax Returns,” *Brookings Papers on Economic Activity*, Spring, 67–122

(cite-duranDiscounting)=
Durán, Jorge (2003): “Discounting long run average growth in stochastic dynamic programs,” *Economic Theory*, 22(2), 395–413

(cite-Feinberg2012)=
Feinberg, Eugene A, Pavlo O Kasyanov, and Nina V Zadoianchuk (2012): “{Average Cost Markov Decision Processes with Weakly Continuous Transition Probabilities},” *Mathematics of Operations Research*, 37, 591–607

(cite-fisherInterestTheory)=
Fisher, Irving (1930): *The Theory of Interest*. MacMillan, New York

(cite-friedmanATheory)=
Friedman, Milton A. (1957): *A Theory of the Consumption Function*. Princeton University Press

(cite-gpLifeCycle)=
Gourinchas, Pierre-Olivier, and Jonathan Parker (2002): “Consumption Over the Life Cycle,” *Econometrica*, 70(1), 47–89

(cite-harmenbergInvariant)=
Harmenberg, Karl (2021a): “Aggregating heterogeneous-agent models with permanent income shocks,” *Journal of Economic Dynamics and Control*, 129, 104185

(cite-harmenbergAggregating)=
———{} (2021b): “Aggregating heterogeneous-agent models with permanent income shocks,” *Journal of Economic Dynamics and Control*, 129, 104185

(cite-hendricksBequests)=
Hendricks, Lutz (2001): *Bequests and Retirement Wealth in the United States*. University of Arizona

(cite-hendricksSmallBequests)=
———{} (2016): “Wealth Distribution and Bequests,” *Lecture Notes, Economics 821, University of North Carolina*

(cite-dmHowMuch)=
Hryshko, Dmytro, and Iourii Manovskii (2020): “How much consumption insurance in the US?,” *Manuscript, University of Alerta*

(cite-jpCins)=
Jappelli, Tullio, and Luigi Pistaferri (2000): “Intertemporal Choice and Consumption Mobility,” *Econometric Society World Congress 2000 Contributed Paper Number 0118*

(cite-Jaskiewicz2011)=
Jaśkiewicz, Anna, and Andrzej S. Nowak (2011): “{Discounted dynamic programming with unbounded returns: Application to economic models},” *Journal of Mathematical Analysis and Applications*, 378(2), 450–462

(cite-kvwWealthyH2m)=
Kaplan, Greg, Gianluca Violante, and Justin Weidner (2014): “The Wealthy Hand-to-Mouth,” *Brookings Papers on Economic Activity*, Spring, 77–138

(cite-kimball-smallandlarge)=
Kimball, Miles S. (1990): “Precautionary Saving in the Small and in the Large,” *Econometrica*, 58, 53–73

(cite-kmpHandbook)=
Krueger, Dirk, Kurt Mitman, and Fabrizio Perri (2016): “Macroeconomics and household heterogeneity,” in *Handbook of Macroeconomics*, vol. 2, pp. 843–921. Elsevier

(cite-lsIncFluct)=
Li, Huiyu, and John Stachurski (2014): “Solving the income fluctuation problem with unbounded rewards,” *Journal of Economic Dynamics and Control*, 45, 353–365

(cite-lwComponents)=
Lillard, Lee A., and Yoram Weiss (1979): “Components of Variation in Panel Earnings Data: American Scientists 1960-70,” *Econometrica*, 47(2), 437–454

(cite-maTodaRich)=
Ma, Qingyin, and Alexis Akira Toda (2020): “A Theory of the Saving Rate of the Rich,” *arXiv*

(cite-mstIncFluct)=
Ma, Qingyin, John Stachurski, and Alexis Akira Toda (2020): “The income fluctuation problem and the evolution of wealth,” *Journal of Economic Theory*, 187

(cite-maUnboundedDP)=
———{} (2022a): “Unbounded dynamic programming via the Q-transform,” *Journal of Mathematical Economics*, 100, 102652

(cite-Ma2022)=
———{} (2022b): “{Unbounded dynamic programming via the Q-transform},” *Journal of Mathematical Economics*, 100, 102652

(cite-macurdyTimeseries)=
MaCurdy, Thomas (1982): “The Use of Time Series Processes to Model the Error Structure of Earnings in a Longitudinal Data Analysis,” *Journal of Econometrics*, 18(1), 83–114

(cite-mvExistence)=
Martins-da Rocha, V Filipe, and Yiannis Vailakis (2010): “Existence and uniqueness of a fixed point for local contractions,” *Econometrica*, 78(3), 1127–1141

(cite-mnUnique)=
Matkowski, Janusz, and Andrzej S. Nowak (2011): “On Discounted Dynamic Programming With Unbounded Returns,” *Economic Theory*, 46, 455–474

(cite-modiglianiWealth)=
Modigliani, Franco (1966): “The Life Cycle Hypothesis, the Demand for Wealth, and the Supply of Capital,” *Social Research*, 33, 160–217

(cite-muthOptimal)=
Muth, John F. (1960): “Optimal Properties of Exponentially Weighted Forecasts,” *Journal of the American Statistical Association*, 55(290), 299–306

(cite-riehl2017category)=
Riehl, Emily (2017): *Category theory in context*. Courier Dover Publications

(cite-rinconZapatero2024)=
Rincón-Zapatero, Juan Pablo (2024): “{Existence and uniqueness ofsolutions to the Bellman equation in stochastic dynamic programming},” *Theoretical Economics*, 19(3), 184–197

(cite-rrExistence)=
Rincón-Zapatero, Juan Pablo, and Carlos Rodríguez-Palmero (2003): “Existence and uniqueness of solutions to the Bellman equation in the unbounded case,” *Econometrica*, 71(5), 1519–1555

(cite-Rockafellar1972)=
Rockafellar, R. Tyrrell (1972): *Convex Analysis*. Princeton University Press

(cite-seIncFluct)=
Schechtman, Jack, and Vera Escudero (1977): “Some results on `An Income Fluctuation Problem',” *Journal of Economic Theory*, 16, 151–166

(cite-schectman-fluctuation)=
Schectman, Jack (1976): “An Income Fluctuation Problem,” *Journal of Economic Theory*, XII, 218–41

(cite-scheinkman-weiss-borrowing)=
Scheinkman, José, and Laurence Weiss (1986): “Borrowing Constraints and Aggregate Economic Activity,” *Econometrica*, 54(1), 23–46

(cite-schmitt2003closing)=
Schmitt-Grohé, Stephanie, and Martın Uribe (2003): “Closing small open economy models,” *Journal of international Economics*, 61(1), 163–185

(cite-Shanker2017a)=
Shanker, Akshay (2017): “{Existence of Recursive Constrained Optima in the Heterogenous Agent Neoclassical Growth Model},” *SSRN Working Paper 3011662*

(cite-stachurski2022)=
Stachurski, J. (2022): *Economic Dynamics, second edition: Theory and Computation*. MIT Press

(cite-StachurskiToda2019JET)=
Stachurski, John, and Alexis Akira Toda (2019): “An Impossibility Theorem for Wealth in Heterogeneous-Agent Models with Limited Heterogeneity,” *Journal of Economic Theory*, 182, 1–24

(cite-slpMethods)=
Stokey, Nancy L., Robert E. Lucas, and Edward C. Prescott (1989): *Recursive Methods in Economic Dynamics*. Harvard University Press

(cite-Sun2009)=
Sun, Yeneng, and Yongchao Zhang (2009): “{Individual Risk and Lebesgue Extension Without Aggregate Uncertainty},” *Journal of Economic Theory*, 144, 432–443

(cite-szeidlInvariant)=
Szeidl, Adam (2013): “Stable Invariant Distribution in Buffer-Stock Saving and Stochastic Growth Models,” *Manuscript, Central European University*

(cite-yaari1965uncertain)=
Yaari, Menahem E (1965): “Uncertain lifetime, life insurance, and the theory of the consumer,” *The Review of Economic Studies*, 32(2), 137–150

(cite-zeldesStochastic)=
Zeldes, Stephen P. (1989): “Optimal Consumption with Stochastic Income: Deviations from Certainty Equivalence,” *Quarterly Journal of Economics*, 104(2), 275–298
