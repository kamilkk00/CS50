
# Debt Master

## Video Demo:  
[Debt Master](https://youtu.be/Gaczve8AV4w)

## Description:

My final python project is designed to determine the optimal interest rate for loans or bonds issued by companies.

In the initial phase, the person who will represent this company is asked to answer several important questions.

This entity must indicate the specific amount it wants to borrow, in which country its company is located, what is the level of interest rates set by the central bank in these countries. In addition, the currency in which the liability will be incurred is important, so the survey also includes questions about the currency in which the loan will be granted and what is the current interest rate of the central bank that issues the currency.

In addition, the company is asked whether the currency is the currency of the country in which the company is established. In the case of a negative answer, an additional 2 percentage points of interest rate per annum are added. This is very important because if a given entity obtains revenues in currency X and has liabilities in currency Y (for various reasons, for example, a lower interest rate resulting from the stability of a given currency and the monetary policy of the central bank), it is this entity that is exposed to additional currency risk. In the event of high exchange rate fluctuations between the currency in which the company generates revenues and the currency of repayment of the liability, there may be insolvency of a given entity, so at the same time the risk of insolvency increases.

The situations presented above are good practices used by the largest entities setting investment ratings (e.g. Moody's, Standard & Poor's, or Fitch), as well as investment funds that purchase such securities for investment purposes on their own behalf for the profit of their clients.

Next, the entity must provide its investment grade. An investment grade is intended to demonstrate the probability of an entity's insolvency.

Investment ratings can be determined both by analysts of a company or an investor who wants to buy a given security, as well as specialized companies, including special companies that have recognition around the world (slightly smaller after the 2008 crisis, when they incorrectly determined investment ratings for mortgage loans in the USA, which had very negative effects on most countries in the world), i.e. Moody, S&P, Fitch.

Investment grades in their basic form are divided according to the probability of bankruptcy of a given company and have the following values: AAA, AA, A, BBB, BB, B, CCC, CC, C, D. The most solvent entities or countries have an AAA rating, which allows them to incur liabilities at the best interest rate. Next are in terms of the attractiveness of interest rates AA, A, BBB and so on. In my model, on the basis of which the interest rate is determined, I assigned an appropriate value of the additional premium to the interest rate, depending on the investment grade, and so the AA rating has a premium of 1.5 percentage points, and B rating has a premium of 8 percentage points.

Another variable added to the model is the amount of the period for which a given entity wants to incur debt. In my model and code, I have included incurring debt up to 1 year, up to 5 years to 10 and 20 years. The amount of the bonus increases by 1 percentage point each time the length of the liability increases to the next level (i.e. from 1 year to 5 years and so on).

Based on all the information collected, the presented code is able to calculate the optimal interest rate for a given security or bank loan.

Calculations of the amount of interest as they are found in the function total_cost.

