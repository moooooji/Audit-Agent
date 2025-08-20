# Berachain 문서

*이 문서는 모든 Berachain 문서를 하나의 종합적인 참조로 결합합니다.*

## 목차

1. [Compound Protocol](#doc_1)
2. [Dripper Specification](#doc_2)
3. [scenario/Types](#doc_3)

---

<a id="doc_1"></a>

## Compound Protocol

*파일 경로: compound.md*

#### [​ Final ​] Version 2. 1

### Constants

```
Constant Description
liquidationIncentive A multiplier representing the excess percent value that a user calling
liquidate receives, e.g. 1.05 for a 5% bonus. This discount applies to
the asset being seized (that is, what was used as collateral).
collateralFactor A multiplier represtsenting the amount you can borrow against your
collateral, e.g. .9 to allow borrowing 90% of collateral value. Must be
between 0 and 1.
closeFactor A number greater than 0.05 and less than or equal to 0.9 which is
multiplied by a given asset's ​ borrowCurrent ​ to calculate the maximum
repayAmount ​ when liquidating a borrow for an underwater account.
maxAssets The max number of assets a single account can participate in (borrow
or use as collateral). This does not affect accounts which mint,
redeem or transfer without borrowing.
reserveFactor The portion of accrued interest that goes into reserves, between [0, 1],
and likely below 0.10.
```
### Key Terms

```
Value Description
borrowCurrent The user’s borrow of a given asset, including accrued interest as of
the current block. This is the user's stored principal, times the
market's current interest index divided by the user's stored interest
index.
sumCollateral The collateral value of a user's supplied assets, including accrued
interest, in terms of ether. This is the sum over all assets of user's
token balance, times the (stored) underlying exchange rate of that
token, times the value of that asset in terms of eth, times the the
asset's ​ collateralFactor ​.
Note: we use the stored exchange rate here, instead of calculating a
new exchange rate for each collateral asset. The delta should be small
```

```
and this is only used for account liquidity checks.
```
sumBorrow The value of a users borrowed assets, including accrued interest, in
Ether. That is, the sum of ​borrowCurrent​ for each of a user's assets.

accountLiquidity The ​sumCollateral​ value of a user’s account, denominated in Ether,
minus the sumBorrow (for the case where ​sumCollateral ​≥
sumBorrow​). This number may be below zero for unhealthy
accounts.

maxCloseValue A user’s borrow balance in a given asset, multiplied by the
closeFactor; how much value can be repaid by a liquidator.

seizeTokens The number of cTokens to transfer from the liquidated user to the
liquidator. This is the ​ _seizeAmount_ ​, times the liquidation incentive,
times the ratio of the oracle prices for the given asset pair, divided by
the exchange rate of the collateral asset.

totalBorrowBalance The total borrow balance, with accrued interest, across all accounts
in a money market, as of the current block.

```
Note: totalBorrowBalance will be strictly larger than totalBorrows from
v1, so the result of interest rate calculations will be different if we use
the same interest rate models.
```
assets​account A set of markets that an account has participated in with a max size of
maxAssets

blocks When calculating simple interest, blocks refers to the number of
blocks that have elapsed since the last time the interest index was
calculated. That most recent block is stored as
interestBlockNumberasset and is stored whenever an interest index is
stored, and blocks is calculated as the current block's number minus
interestBlockNumberasset.

rate When calculating simple interest, rate refers to the current interest
rate of the market. This was the previous rate that's been "in effect"
for ​blocks​ blocks.

Exchange Rate Stored The last stored exchange rate for cTokens to underlying assets. This
value does not include borrowing interest since the last interest
accrual in this market.

Exchange Rate Current The current exchange rate (including all trued up borrowing interest)
between cTokens and the underlying asset.


### Exceptional States

We assume that in ​ _any_ ​ error condition, either a) the protocol exits gracefully with an event
describing the error if no side-effects have yet occurred, or b) the transaction fails
completely. Any exceptions to this rule are noted, except as below.
A number of functions are split into two commands: accrue interest and a ​ _fresh_ ​action. The
goal is to separate two discrete events which should occur. First, every time we accrue
interest for a market, we help true up balances (and turn simple interest into compound
interest) for that market. Second, the fresh functions are only correct if the market's interest
has been fully accumulated as of this block. With updated interest, however, these fresh
functions have divergent concerns (often, significantly unrelated to interest accrual). We thus
build these functions as the sum of two actions to simplify the understanding and modelling
of these two separate acts. In practice, this means that even when a method fails gracefully,
the transaction may still accrue interest for that market (this is a good thing!).

### Interest Rate Model Contract

For each asset, there is an interest index. We effectively track the growth of principal of an
arbitrary account over time. We use the ratio of that account's interest versus initial principal
to calculate the growth of any given account's interest over a subset of that time interval. The
interest model contract specifies the simple interest rate at any moment (which, when
compounded for each transaction becomes compound interest). We force this interest rate
model to be a pure function over the cash, borrows, and reserves of an asset in the market.
For more information, see ​ **Interest Index Calculation Appendix** ​.

**borrowRate(​address​ cToken, ​amount ​cash, ​amount ​borrows, ​amount ​reserves) returns ​uint**

```
● Return the current interest rate for the market
● Note: cToken is the Compound cToken contract, not the underlying asset address.
```
### Price Oracle Contract

The Compound Protocol uses prices from a smart contract called a price oracle. The
Comptroller and Liquidate Borrow functions reference the prices in this oracle. Multiple
oracles may exist for the different Compound markets.

**getUnderlyingPrice( ​CToken​ cToken) returns ​uint**

```
● Return price of the underlying asset (as a mantissa)
```

### cToken Contract

cTokens act as ERC-20 interfaces and will be the primary location where users interact with
the Compound Protocol. When a user mints, redeems, borrows, repays borrows, liquidates a
borrow, or transfers cTokens, she will do so on the cToken contract itself. The only actions
that a user performs on another contract are entering and exiting assets via the Comptroller
(see below for the ​ **Comptroller contract** ​).

cTokens each reference an ​ _underlying_ ​. This is usually the underlying ERC-20 contract, though
it may be Ether itself or a complex asset. cTokens are the ultimate holders of that underlying
asset balance and each call to take in or send out assets originates in the cToken contract.
Initially, cEth (Compound Ether token) will be a unique asset, interacting with Ether instead
of ERC-20 assets.

#### Note about cToken Money Markets

The Money Market was the core monolith of the Compound Protocol in the first version. The
functions that used to exist in the Money Market now exist in the cTokens, and the old ​ _Market_
struct is flattened in to each cToken Market. Functions related to Policies and Liquidity are
deferred to the Comptroller contract.

#### Market Functions

**borrowRatePerBlock()**

```
● Returns the current per-block borrow interest rate mantissa for this cToken
```
**supplyRatePerBlock()**

```
● We calculate the supply rate:
○ underlying=totalSupply × exchangeRate
○ borrowsPer=totalBorrows ÷ underlying
○ supplyRate=borrowRate × ( 1 −reserveFactor) × borrowsPer
● Returns the current per-block supply interest rate mantissa for this cToken
```
**Accrue Interest()**

We accrue interest and update the borrow index on every operation. This increases
compounding, approaching the true value, regardless of whether the rest of the operation
succeeds or not.


```
● totalCash=invoke getCashPrior()
○ Note: likely makes an external call
● We get the interest rate (that was in effect since the last update):
○ borrowRate=call interestModel.borrowRate(this,totalCash,totalBorrows,totalReserves)
○ simpleInterestFactor=Δblocks ×borrowRate
● We updateborrowIndex:
○ borrowIndexNew= borrowIndex×( 1 +simpleInterestFactor)
● We calculate the interest accrued:
○ interestAccumulated=totalBorrows×simpleInterestFactor
● We update borrows and reserves:
○ totalBorrowsNew=totalBorrows+interestAccumulated
○ totalReservesNew=totalReserves+interestAccumulated×reserveFactor
● We store the updates back to the blockchain:
○ Set accrualBlockNumber=getBlockNumber()
○ Set borrowIndex=borrowIndexNew
○ Set totalBorrows=totalBorrowsNew
○ Set totalReserves=totalReservesNew
● Emit an ​ AccrueInterest ​ event
```
**[CErc20] ​Mint(​uint​ mintAmount)**

```
● Checkinvoke Accrue Interest()= 0
● Return invoke Mint Fresh(msg.sender, mintAmount)
```
**[CEther] ​Mint() payable**

```
● Checkinvoke Accrue Interest()= 0
● Return invoke Mint Fresh(msg.sender, msg.value)
```
**[​Internal​] Mint Fresh(​address​ minter, ​uint​ mintAmount)**

User supplies assets from her own address into the market and receives a balance of cTokens
in exchange.
● Fail if call comptroller.mintAllowed(this, minter, mintAmount) =/ 0
● Verify market's ​ _block number_ ​ equals current block number
● Fail if​ _invoke checkTransferIn(minter, mintAmount)_ ​ fails
● We get the current exchange rate and calculate the number of cTokens to be minted:
○ exchangeRate=invoke Exchange Rate Stored()
○ mintTokens=mintAmount ÷exchangeRate


```
■ Note: divisions are rounded, as necessary, toward zero, thus it is possible
to mint 0 tokens
● We calculate the new total supply of cTokens and ​ minter ​ token balance:
○ totalSupplyNew = totalSupply+mintTokens
■ Fails on overflow
○ accountTokensNewminter = accountTokensminter+mintTokens
■ Fails on overflow
● We have finished calculations ​. (If any calculations failed with an error, we have
already returned with a failure code). Now we can begin effects.
● We invoke ​ doTransferIn ​ for the ​ minter ​ and the ​ mintAmount
○ Note: The cToken must handle variations between ERC-20 and ETH underlying.
○ On success, the cToken holds an additional ​ mintAmount ​ of cash
○ If ​ doTransferIn ​ fails despite the fact we checked pre-conditions, we revert
because we can't be sure if side effects occurred
● We write previously calculated values into storage:
○ Set totalSupply = cTokenSupplyNew
○ Set accountTokensminter=accountTokensNewminter
● Emit a ​ Mint ​ event with minter, mintAmount, mintTokens
● Emit a ​ Transfer ​ event from ​ this ​to ​ minter
● call comptroller.mintVerify(this, minter, mintAmount, mintTokens)
```
**Redeem(​uint​ redeemTokens)**

```
● Checkinvoke Accrue Interest()= 0
● Return invoke Redeem Fresh(msg.sender, redeemTokens, 0 )
```
**Redeem Underlying(​uint​ redeemAmount)**

```
● Checkinvoke Accrue Interest()= 0
● Return invoke Redeem Fresh(msg.sender, 0 , redeemAmount)
```
**[​Internal​] Redeem Fresh(​address​ redeemer, ​uint​ redeemTokensIn, ​uint​ redeemAmountIn)**

User relinquishes cTokens and receives the underlying ERC-20 asset from the protocol into
her own wallet.
● exchangeRate =invoke Exchange Rate Stored()
● If redeemTokensIn> 0 :
○ We get the current exchange rate and calculate the amount to be redeemed:
■ redeemTokens = redeemTokensIn
■ redeemAmount = redeemTokensIn×exchangeRate
● Else:


```
○ We get the current exchange rate and calculate the amount to be redeemed:
■ redeemTokens = redeemAmountIn÷exchangeRate
■ redeemAmount = redeemAmountIn
● Fail if call comptroller.redeemAllowed(this, redeemer, redeemTokens) =/ 0
● Verify market's ​ block number ​ equals current block number
● We calculate the new total supply and ​ redeemer ​ token balance:
○ totalSupplyNew= totalSupply−redeemTokens
■ Fails if redeemTokens > totalSupply
○ accountTokensNewredeemer=accountTokensredeemer−redeemTokens
■ Fails if redeemTokens > accountTokensredeemer
● Fail gracefully if protocol has insufficient cash
● We have finished calculations ​. (If any calculations failed with an error, we have
already returned with a failure code). Now we can begin side effects.
● We invoke ​ doTransferOut ​ for the ​ redeemer ​ and the ​ redeemAmount
○ Note: The cToken must handle variations between ERC-20 and ETH underlying.
○ On success, the cToken has ​ redeemAmount ​ less of cash
○ If ​ doTransferOut ​ fails despite the fact we checked pre-conditions, we revert
because we can't be sure if side effects occurred
● We write previously calculated values into storage
○ Set totalSupply = totalSupplyNew
○ Set accountTokensredeemer=accountTokensNewredeemer
● Emit a ​ Redeem ​ event with redeemer, redeemAmount, redeemTokens
● Emit a ​ Transfer ​ event from ​ redeemer ​to ​ this
● call comptroller.redeemVerify(this, redeemer, redeemAmount, redeemTokens)
```
**Borrow(​uint​ borrowAmount)**

```
● Checkinvoke Accrue Interest()= 0
● Return invoke Borrow Asset Fresh(msg.sender, borrowAmount)
```
**[​Internal​] BorrowFresh(​address​ borrower, ​uint​ borrowAmount)**

User borrows assets from the protocol.
● Fail if call comptroller.borrowAllowed(this, borrower, borrowAmount) =/ 0
● Verify market's ​ _block number_ ​ equals current block number
● We calculate the new borrower and total borrow balances:
○ accountBorrows=invoke Borrow Balance Stored(borrower)
○ accountBorrowsNew=accountBorrows+borrowAmount
■ Fails on overflow


```
○ totalBorrowsNew=totalBorrows+borrowAmount
■ Fails on overflow
● Fail gracefully if protocol has insufficient cash
● We have finished calculations ​. (If any calculations failed with an error, we have
already returned with a failure code). Now we can begin side effects.
● We invoke ​ doTransferOut ​ for the ​ borrower ​ and the ​ borrowAmount
○ Note: The cToken must handle variations between ERC-20 and ETH underlying
○ On success, the cToken has ​ borrowAmount ​ less of underlying cash
○ If ​ doTransferOut ​ fails despite the fact we checked pre-conditions, we revert
because we can't be sure if side effects occurred
● We write the previously calculated values into storage:
○ Set accountBorrowsborrower={accountBorrowsNew, borrowIndex}
○ Set totalBorrows = totalBorrowsNew
● Emit a ​ Borrow ​ event with borrower, borrowAmount, accountBorrowsNew ,
totalBorrowsNew
● call comptroller.borrowVerify(this, borrower, borrowAmount)
```
**[CErc20] ​Repay Borrow(​uint​ repayAmount)**

```
● Checkinvoke Accrue Interest()= 0
● return invoke Repay Borrow Fresh(msg.sender, msg.sender, repayAmount)
```
**[CEther] ​Repay Borrow() payable**

```
● Checkinvoke Accrue Interest()= 0
● return invoke Repay Borrow Fresh(msg.sender, msg.sender, msg.value)
```
**[CErc20] ​Repay Borrow Behalf(​address​ borrower, ​uint​ repayAmount)**

Repays a borrow on behalf of another user. The message sender is still the payer, but you can
specify a different account to pay against.
● Checkinvoke Accrue Interest()= 0
● Return invoke Repay Borrow Fresh(msg.sender, borrower, repayAmount)

**[CEther] ​Repay Borrow Behalf(​address​ borrower) payable**

Repays a borrow on behalf of another user. The message sender is still the payer, but you can
specify a different account to pay against.
● Checkinvoke Accrue Interest()= 0
● Return invoke Repay Borrow Fresh(msg.sender, borrower, msg.value)


**[​Internal​] Repay Borrow Fresh(​address​ payer, ​address​ borrower, ​uint​ repayAmount)**

Borrows are repaid by the ​ _payer_ ​ (possibly the same as the ​ _borrower_ ​).
● Fail ifcall comptroller.repayBorrowAllowed(this,payer,borrower,repayAmount) =/ 0
● Verify market's ​ _block number_ ​ equals current block number
● We fetch the amount the ​ _borrower_ ​ owes, with accumulated interest:
○ accountBorrows=invoke Borrow Balance Stored(borrower)
● If repayAmount=− 1
○ repayAmount=accountBorrows
● Fail if​ _checkTransferIn(underlying, payer, repayAmount)_ ​ fails
● We calculate the new borrower and total borrow balances:
○ accountBorrowsNew=accountBorrows −repayAmount
■ Fails if repayAmount>accountBorrows
○ totalBorrowsNew=totalBorrows−repayAmount
■ Fails if repayAmount>totalBorrows
● **We have finished calculations** ​. (If any calculations failed with an error, we have
already returned with a failure code). Now we can begin effects.
● We call ​ _doTransferIn_ ​ for the ​ _payer_ ​ and the ​ _repayAmount_
○ Note: The cToken must handle variations between ERC-20 and ETH underlying
○ On success, the cToken holds an additional ​ _repayAmount_ ​ of cash
○ If ​ _doTransferIn_ ​ fails despite the fact we checked pre-conditions, we revert
because we can't be sure if side effects occurred
● We write the previously calculated values into storage:
○ Set accountBorrowsborrower={accountBorrowsNew, borrowIndex}
○ Set totalBorrows=totalBorrowsNew
● Emit ​ **RepayBorrow** ​ event with payer, borrower, repayAmount, accountBorrowsNew,
totalBorrowsNew
● call comptroller.repayBorrowVerify(this, payer, borrower, repayAmount)

**[CErc20] ​Liquidate Borrow(​address​ borrower, ​CToken ​cTokenCollateral, ​uint​ repayAmount)**

```
● Checkinvoke Accrue Interest()= 0
● Checkcall cTokenCollateral.Accrue Interest()= 0
● return
invoke Liquidate Borrow Fresh(msg.sender, borrower, repayAmount, cTokenCollateral)
```
**[CEther] ​Liquidate Borrow(​address​ borrower, ​CToken ​cTokenCollateral) payable**

```
● Checkinvoke Accrue Interest()= 0
```

```
● Checkcall cTokenCollateral.Accrue Interest()= 0
● return
invoke Liquidate Borrow Fresh(msg.sender, borrower, msg.value, cTokenCollateral)
```
**[​Internal​] Liquidate Borrow Fresh(​address​ liquidator, ​address​ borrower, ​uint​ repayAmount,
CToken ​cTokenCollateral)**

The liquidator repays an amount of the underlying asset in this market, on behalf of an
underwater borrower, and seizes the appropriate number of tokens in the collateral market.
● Fail ifcall comptroller.liquidateBorrowAllowed(this,...arguments) =/ 0
● Verify market's ​ _block number_ ​ equals current block number
● Verify ​ _cTokenCollateral_ ​ market's ​ _block number_ ​ equals current block number
○ Fail ifcall cTokenCollateral.accrualBlockNumber()=/block.number
● Fail if liquidator=borrower
● Fail if repayAmount= 0
● Fail if repayAmount=− 1
● We calculate the number of collateral tokens that will be seized:
○ seizeTokens=call comptroller.liquidateCalculateSeizeTokens
(this, cTokenCollateral, repayAmount)
● Fail if seizeTokens>cTokenCollateral.balanceOf(borrower)
● Fail ifinvoke Repay Borrow Fresh(liquidator, borrower, repayAmount) ≠ 0
● Revert if call cTokenCollateral.seize(liquidator, borrower, seizeTokens) ≠ 0
● Emit a​ ​ **LiquidateBorrow** ​ ​event with liquidator, borrower, repayAmount,
cTokenCollateral , seizeTokens
● call comptroller.liquidateBorrowVerify(this, ...arguments, ...state)

**seize(​address​ liquidator, ​address​ borrower, ​uint​ seizeTokens) returns ​uint**

```
● Fail if
call comptroller.seizeAllowed(this, msg.sender,liquidator,borrower,seizeTokens) =/ 0
○ Note: It’s critical that the collateral contract uses ​ msg.sender ​as the address of
the borrowed CToken which it verifies with the Comptroller. If a parameter
were used, then anyone would be able to spoof this call.
● Fail if borrower=liquidator
● We calculate the new borrower and liquidator token balances:
○ borrowerTokensNew=accountTokens[borrower]−seizeTokens
■ Fail on underflow
○ liquidatorTokensNew=accountTokens[liquidator]+seizeTokens
■ Fail on overflow
● We write the previously calculated values into storage:
```

```
○ accountTokens[borrower]=borrowerTokensNew
○ accountTokens[liquidator]=liquidatorTokensNew
● Emit a ​ Transfer ​ event
● call comptroller.seizeVerify(this, msg.sender,liquidator,borrower, seizeTokens)
```
#### Administrative Functions

**constructor(​EIP20​ underlying,​address​ interestRateModel, ​address​ comptroller, scaled
initialExchangeRate)**

```
● Set ​ admin ​ to msg.sender
● Set underlying to ​ underlying
● Set initialExchangeRate to ​ initialExchangeRate
● Set marketBlockNumber to block number
● Set market borrow index to 1e
● Set reserve factor to 0
● invoke _setMarketInterestRateModelFresh(interestRateModel)
● invoke _setMarketComptroller(comptroller)
```
**_setReserveFactor(​scaled​ newReserveFactor)**

```
● Checkinvoke Accrue Interest()= 0
● Return ​ _setReserveFactorFresh(newReserveFactor)
```
**[​Internal​] _setReserveFactorFresh(​scaled​ newReserveFactor)**

```
● Check caller is ​ admin
● We verify market's ​ block number ​ equals current block number
● Check newReserveFactor ≤ maxReserveFactor
● Store ​ reserveFactor ​ with value ​ newReserveFactor
● Emit ​ NewReserveFactor ​ (oldReserveFactor, newReserveFactor)
```
**_reduceReserves(​uint​ amount)**

```
● Checkinvoke Accrue Interest()= 0
● Return ​ _reduceReservesFresh(amount)
```
**[​Internal​] _reduceReservesFresh(​uint​ reduceAmount)**

```
● Check caller is ​ admin
● We verify market's ​ block number ​ equals current block number
● Check ​ amount ​ ≤ reservesn
```

```
● Fail gracefully if protocol has insufficient underlying cash
● Store reservesn+ 1 = reservesn − reduceAmount
● invoke doTransferOut(underlying, reduceAmount, admin)
○ Note: we revert on the failure of this command
● Emit ​ NewReserves ​(​ admin ​, reduceAmount, reservesn+ 1 )
```
**_setPendingAdmin(​address​ newPendingAdmin)**

```
● Check caller is ​ admin
● Store ​ pendingAdmin ​ with value ​ newPendingAdmin
● Emit​ ​ NewPendingAdmin ​ (oldPendingAdmin, newPendingAdmin)
```
**_acceptAdmin()**

```
● Check caller is ​ pendingAdmin ​ and ​ pendingAdmin ​ ≠ address(0)
● Store ​ admin ​ with value ​ pendingAdmin
● Unset ​ pendingAdmin
● Emit ​ NewAdmin ​ (oldAdmin, newAdmin)
● Emit ​ NewPendingAdmin ​ (oldPendingAdmin, 0)
```
**_setInterestRateModel(​address​ newInterestRateModel)**

```
● Checkinvoke Accrue Interest()= 0
● return ​ _setFreshInterestModelFresh(newInterestRateModel)
```
**[​Internal​] _setInterestRateModelFresh(​address​ newInterestRateModel)**

```
● Check caller is ​ admin
● We assert market's ​ block number ​ equals current block number
● Track the market's current interest rate model
● Ensurecall newInterestRateModel.isInterestRateModel() returns true
● Set the interest rate model to ​ newInterestRateModel
● Emit ​ NewInterestRateModel ​(​ oldInterestRateModel ​, ​ newInterestRateModel ​)
```
**_setComptroller(​address​ newComptroller)**

```
● Check caller is ​ admin
● Track asset's current comptroller as ​ oldComptroller
● Ensure call comptroller.isComptroller()returns true
● Set comptroller to ​ newComptroller
● Emit ​ NewComptroller ​(​ oldComptroller ​, ​ newComptroller ​)
```

#### Token Functions

**name() returns ​string**

```
● Return ​ name
```
**symbol() returns ​string**

```
● Return ​ symbol
```
**decimals() returns ​uint**

```
● Return ​ decimals
```
**[​External​] getCash() returns ​uint**

```
● Return call getCashPrior()
```
**transfer(​address​ to, ​uint​ amount) returns ​bool**

```
● invoke transferTokens(msg.sender, msg.sender, to, amount)
○ Revert if not successful
○ Emit ​ Transfer ​ (msg.sender, to, tokens)
```
**transferFrom(​address​ from, ​address​ to, ​uint​ amount) returns ​bool**

```
● invoke transferTokens(msg.sender, from, to, amount)
○ Revert if not successful
○ Emit ​ Transfer ​ (from, to, tokens)
```
**[​Internal​] transferTokens(​address ​spender, ​address ​src, ​address ​dst, ​uint ​amount) returns ​uint**

Transfer ​ _amount_ ​ cTokens from ​ _source_ ​ to ​ _dest._
● Fail if call comptroller.redeemAllowed(this, src, amount)returns false
● Fail unless ​ _spender_ ​ is ​ _source_ ​ or cTokenAllowed[src][spender]≥amount
● Fail if accountTokens[src]<amount
● accountTokens[src]−=amount
○ Underflow is impossible due to check above
● accountTokens[dst]+=amount
○ Fail on overflow
● Unless spender=src ⋁cTokenAllowed[src][spender]=maxUint
○ cTokenAllowed[src][spender]−=amount


**totalSupply() returns ​uint**

```
● Return totalSupply
```
**allowance(​address​ owner, ​address​ spender) returns ​uint**

```
● Return cTokenAllowed[owner][spender]
```
**balanceOf(​address​ account) returns ​uint**

```
● Return accountTokens[account]
```
**balanceOfUnderlying(​address​ account) returns ​uint**

```
● Return accountTokens[account] × invoke Exchange Rate Current()
```
**approve(​address​ spender, ​uint256​ amount) returns ​bool**

```
● Overwrite cTokenAllowed[msg.sender][spender] = amount
● Emit ​ Approval ​ (msg.sender, spender, amount)
```
#### Exchange Rates

**Exchange Rate Current() returns ​uint**

```
● invoke Accrue Interest()
● return invoke Exchange Rate Stored()
```
**Exchange Rate Stored()**

```
● Note: we do not assert that the market is up to date.
● If there are no tokens minted:
○ exchangeRate=initial exchange rate
● Otherwise:
○ totalCash =invoke getCash()
■ Note: likely makes an external call
○ exchangeRate = totalCash^ +tottaoltBaolSrruopwplsy− totalReserves^
● Return exchangeRate
```
#### Borrow Balances

**Total Borrows Current(​address​ account) returns ​uint**

```
● invoke Accrue Interest()
```

```
● return totalBorrows
```
**Borrow Balance Current(​address​ account) returns ​uint**

```
● invoke Accrue Interest()
● return invoke Borrow Balance Stored()
```
**Borrow Balance Stored(​address​ borrower)**

```
● Note: we do not assert that the market is up to date.
● We get from storage from the cToken:
○ borrowBalanceborrower=accountBorrows[borrower]
○ borrowIndexborrower=accountBorrowIndex[borrower]
● If borrowBalanceborrower= 0 then borrowIndexborroweris likely also 0. Rather than
failing the calculation with a division by 0, we immediately return 0 in this case.
● recentBorrowBalanceborrower= borrowBalbaonrcreobworIronwdeer×xbboorrrorwoewrIndexstored
● Return recentBorrowBalanceborrower
```
#### Safe Token

**[​Internal​] checkTransferIn(​address​ account, ​uint​ underylingAmount) returns ​uint**

```
● call EIP 20 (underlying).allowance(account, address(this)))
○ Fail if result is less than ​ underlyingAmount
● call EIP 20 (underlying).balanceOf(account))
○ Fail if result is less than ​ underlyingAmount
● Return 👍
```
**[​Internal​] doTransferIn(​address​ account, ​uint​ underlyingAmount)**

```
● Revert if msg.value> 0 since there is no valid use case for sending value by default
● call EIP 20 (underlying).transferFrom(account, address(this), underlyingAmount)
○ Revert unless true
○ *Note: should handle ​non-standard ERC-20 tokens
```
**[​Internal​] getCashPrior() returns ​uint**

```
● Returncall EIP 20 (underlying).balanceOf(address(this)))
```
**[​Internal​] doTransferOut(​address​ account, ​uint​ underlyingAmount)**

```
● call EIP 20 (underlying).transfer(account, underlyingAmount)
○ Revert unless true
```

```
○ *Note: should handle ​non-standard ERC-20 tokens
```
#### Safe Token (cETH)

In order to implement cETH, we add a fallback function that does invoke mint(msg.value).
In addition, we override the Safe Token methods as follows:

**[​Internal​] checkTransferIn(​address​ account, ​uint​ underylingAmount) returns ​uint**

```
● Fail if msg.sender ≠ account
● Fail if msg.value ≠ underlyingAmount
● Return👍
```
**[​Internal​] doTransferIn(​address​ account, ​uint​ underlyingAmount)**

```
● Fail if msg.value ≠ underlyingAmount
○ We just sanity check, ​ checkTransferIn ​ should have already been called
```
**[​Internal​] getCashPrior() returns ​uint**

```
● Returnthis.balance−msg.value
○ Ensure we avoid underflow
```
**[​Internal​] doTransferOut(​address​ account, ​uint​ underlyingAmount)**

```
● invoke account.transfer(underlyingAmount)
○ Ensure minimum gas is attached to transfer
```
### Comptroller Contract

The Comptroller implements the Liquidity Checker API specification. Most important of these
areliquidityChecker. _redeemAllowed(),_ liquidityChecker. _borrowAllowed(),_ ​and
liquidityChecker. _liquidateBorrowAllowed()_ ​.

The Comptroller also implements a defense hook mechanism to protect against unforeseen
future vulnerabilities. These ​ _*Verify_ ​ functions are currently no-ops, but provide a last resort
to potentially revert any protocol transaction which would violate the intended behavior of
the protocol and therefore put user assets at risk.

Note: In order to seamlessly upgrade the Comptroller without changing the Comptroller
address referenced by the cToken markets, we sometimes use a technique known as
_delegate calls_ ​.


#### User Market Functions

These two functions (enter markets and exit market) will be called by the end-users directly.
This will only be a requirement for users who wish to borrow. That is, token holders that do
not borrow will not need to (and should not) call these functions.

**Enter Markets(​address[]​ cTokens) returns ​bool[]**

The sender includes a list of asset addresses that should be used when calculating account
liquidity. Before borrowing an asset, one or more supplied assets must be added in this way
to provide collateral. Any asset to be borrowed must be added in this way before borrowing
is allowed. The return value is a list of mapping the assets passed in to whether the user is
ultimately in that market.

```
● For each cToken given as an argument:
○ We check if the user is already in the cToken, if so, collect true, otherwise,
proceed
○ We check if the user has reached maxAssets, if so, collect false, otherwise,
proceed
○ We check if the cToken is listed, if not, collect false, otherwise, proceed.
○ We check oraclePriceasset≠ 0
○ We add the asset to assets​user ​, by pushing it into user’s assets list and setting
membershipscToken,user to true, and collect true
○ Proceed to the next asset, noting that the size of the list was increased if the
previous item added to the list and the maxAssets comparison must occur
against storage
○ Emit ​ MarketEntered ​(​ cToken, msg.sender ​)
● Return the collected answers of whether the user is currently in the passed cTokens
```
**Exit Market(​address​ cToken) returns ​bool**

The sender provides an asset that they no longer wish to be included in account liquidity
calculations. Since all borrowed assets ​ **must** ​ be included, the purpose of the function is to
remove an asset from the user’s collateral list. The return value is a boolean indicating if the
user is not in the market after the call.

```
● Get sender ​ tokensHeld ​ and ​ amountOwed ​underlying from the cToken
● Fail if the sender has a borrow balance
○ i.e.amountOwed ≠ 0
● Fail if the sender is not permitted to redeem all of their tokens
```

```
○ i.e. invoke redeemAllowed(cToken, msg.sender, tokensHeld)=/ 0
● Return true if the sender is not already ‘in’ the market
● Set ​ cToken ​ account membership to false
● Delete ​ cToken ​ from the account’s list of assets
● Emit ​ MarketExited ​(​ cToken, msg.sender ​)
● Return true, indicating the user is no longer in the market
```
#### Policy Hook Functions

These functions are core to verifying if a given action by a user is allowed. This should be
based on a combination of factors. One or more of the factors will be checked by the
following functions.

1. cToken must be a known "supported" asset. ​ **This applies to all functions and must**
    **always be checked.**
2. User must remain sufficiently liquid after the function were to complete. For instance,
    a user cannot redeem tokens if she has too many outstanding borrows.
3. User must declare all assets she intends to borrow (and use as collateral).
4. User must pass all KYC-type checks and other policy rules.
5. For liquidation, caller must be the asset itself ( the borrowed cToken contract ).

**mintAllowed(​CToken​ cToken, ​address​ minter, ​uint​ mintAmount) returns ​uint**

```
● Fail if ​ cToken ​ not listed
● *may include Policy Hook-type checks
● Return ​👍 ​otherwise
```
**mintVerify(​CToken​ cToken, ​address​ minter, ​uint​ mintAmount, ​uint​ mintTokens) returns
uint**

```
● Does nothing, but could revert in the future as a defense hook
```
**redeemAllowed(​CToken​ cToken, ​address​ redeemer, ​uint​ redeemTokens) returns ​uint**

```
● Fail​ ​if ​ cToken ​ not listed
● *may include Policy Hook-type checks
● Return ​👍​ if ​ redeemer ​ does not have membership in asset
● Let (error, liquidity, shortfall) =
invoke getHypotheticalAccountLiquidityInternal(redeemer, cToken, redeemTokens, 0 )
● Fail if error=/ 0 or​ ​if​ shortfall> 0
● Return ​👍 ​otherwise
```

**redeemVerify(​CToken​ cToken, ​address​ redeemer, ​uint​ redeemAmount, ​uint​ redeemTokens)
returns ​uint**

```
● Does nothing, but could revert in the future as a defense hook
```
**borrowAllowed(​CToken​ cToken, ​address​ borrower, ​uint​ borrowAmount) returns ​uint**

```
● Fail​ if cToken not listed
● *may include Policy Hook-type checks
● Fail if ​ borrower ​ does not have membership in asset
● Fail if oraclePriceasset= 0
● Let (error, liquidity, shortfall) =
invoke getHypotheticalAccountLiquidityInternal(borrower, cToken, 0 , borrowAmount)
● Fail if error=/ 0 or​ shortfall> 0
● Return ​👍 ​otherwise
```
**borrowVerify(​CToken​ cToken, ​address​ borrower, ​uint​ borrowAmount)**

```
● Does nothing, but could revert in the future as a defense hook
```
**repayBorrowAllowed(​CToken​ cToken, ​address​ payer, ​address​ borrower, ​uint​ repayAmount)
returns ​uint**

```
● Fail if ​ cToken ​ not listed
● *may include Policy Hook-type checks
● Return ​👍 ​otherwise
```
**repayBorrowVerify(​CToken​ cToken, ​address​ payer, ​address​ borrower, ​uint​ repayAmount)**

```
● Does nothing, but could revert in the future as a defense hook
```
**liquidateBorrowAllowed( ​CToken​ cTokenBorrowed, ​CToken​ cTokenCollateral, ​address
borrower, ​address​ liquidator, ​uint​ repayAmount) returns ​uint**

```
● Fail​ ​if ​ cTokenBorrowed ​ or ​ cTokenCollateral ​ not listed
● *may include Policy Hook-type checks
● Let (error, liquidity, shortfall) =invoke getAccountLiquidityInternal(borrower)
● Fail if error=/ 0 or​ shortfall= 0
○ The borrower must have shortfall in order to be liquidatable
● borrowBalanceaccount=call cTokenBorrowed.Borrow Balance Stored()
○ This value is strictly up-to-date due to accumulating interest prior to this call
● We calculate ​ maxCloseValue ​, the total that can be closed for this borrow:
○ maxCloseValue = borrowBalanceaccount⋅closeFactor
```

```
● Fail if repayAmount >maxCloseValue
● Return ​👍 ​otherwise
```
**liquidateBorrowVerify(​CToken​ cTokenBorrowed, ​CToken​ cTokenCollateral, ​address
borrower, ​address​ liquidator, ​uint​ repayAmount, ​uint​ seizeTokens)**

```
● Does nothing, but could revert in the future as a defense hook
```
**seizeAllowed(​CToken​ cTokenCollateral, ​CToken​ cTokenBorrowed, ​address​ borrower,
address​ liquidator, ​uint​ seizeTokens) returns ​uint**

```
● Fail​ ​if​ ​ cTokenCollateral ​ ​or ​ cTokenBorrowed ​is not listed
● *may include Policy Hook-type checks
● Failcall cTokenCollateral.comptroller()=/call cTokenBorrowed.comptroller()
● Return ​👍 ​otherwise
```
**seizeVerify(​CToken​ cTokenCollateral, ​CToken​ cTokenBorrowed, ​address​ borrower, ​address
liquidator, ​uint​ seizeTokens)**

```
● Does nothing, but could revert in the future as a defense hook
```
**transferAllowed(​CToken​ cToken, ​address​ src, ​address​ dst, ​uint​ transferTokens) returns ​uint**

```
● ReturnredeemAllowed(cToken, src, transferTokens)
```
**transferVerify(​CToken​ cToken, ​address​ src, ​address​ dst, ​uint​ transferTokens)**

```
● Does nothing, but could revert in the future as a defense hook
```
#### Liquidity / Liquidation Calculations

**getAssetsIn(​address​ account) returns ​address[]**

```
● Return list of assets you are in
```
**checkMembership(​address​ account, ​CToken​ cToken) returns ​bool**

```
● Returns true if user is in asset
```
**getAccountLiquidity(​address​ account) returns ​int**

```
● Return invoke getHypotheticalAccountLiquidity(account, CToken( 0 ), 0 , 0 )
```

**getHypotheticalAccountLiquidity( ​address​ account, ​CToken​ cToken, ​uint​ redeemTokens, ​uint
borrowAmount) returns (uint, uint)**

```
● Let assetsaccount be the active list of assets (from storage) that a user has entered
● We calculate the user’s sumCollateral and sumBorrowPlusEffects
○ Note that we calculate the ​ exchangeRateStored ​ for each collateral cToken
using stored data, without calculating accumulated interest
● Initialize sumCollatera= 0 , sumBorrowPlusEffects= 0
● For each asset ∈assetsaccount:
○ We get:
■ cTokenBalanceaccount=call cToken.balanceOf(account)
■ borrowBalanceaccount= call cToken.Borrow Balance Stored(account)
■ exchangeRate=call cToken.Exchange Rate Stored()
■ collateralFactor =markets[asset].collateralFactor
■ oraclePrice=call oracle.getUnderlyingPrice(asset)
● Fail if oraclePrice= 0
○ tokensToDollars=collateralFactor·exchangeRate·oraclePrice
○ sumCollateral+=tokensToDollars·cTokenBalanceaccount
○ sumBorrowPlusEffects+= oraclePrice ·borrowBalanceaccount
○ If asset =cToken(i.e. looking at the affected market):
■ Account for the potential effect of redeeming:
● sumBorrowPlusEffects += tokensToDollars·redeemTokens
■ Account for the potential effect of borrowing:
● sumBorrowPlusEffects += oraclePrice ·borrowAmount
● If sumCollateral > sumBorrowPlusEffects
○ liquidity =sumCollateral − sumBorrowPlusEffects
○ shortfall = 0
● Else
○ liquidity = 0
○ shortfall =sumBorrowPlusEffects − sumCollateral
● Return two unsigned values, liquidity and shortfall
```
**liquidateCalculateSeizeTokens( ​CToken​ cTokenBorrowed, ​CToken​ cTokenCollateral, ​uint
repayAmount) returns ​uint**

```
● Read oracle prices for borrowed and collateral markets:
○ priceborrowed=call oracle.getUnderlyingPrice(cTokenBorrowed)
○ pricecollateral=call oracle.getUnderlyingPrice(cTokenCollateral)
```

```
○ Fail if either priceborrowed= 0 or pricecollateral= 0
● Get the exchange rate and calculate the number of collateral tokens to seize:
○ exchangeRatecollateral=call cTokenCollateral.Exchange Rate Stored()
○ seizeAmount = repayAmount×liquidationIncentivestored×pprriicceecboolrlarotewreadl
○ seizeTokens = seizeAmount ÷ exchangeRatecollateral
● Return seizeTokens
```
#### Comptroller Admin Functions

**constructor()**

```
● Set admin to caller
```
**_setPendingAdmin(​address​ newPendingAdmin) returns ​uint**

```
● Check caller is admin
● Store pendingAdmin with value newPendingAdmin
● Emit ​ NewPendingAdmin ​(oldPendingAdmin, newPendingAdmin)
```
**_acceptAdmin() returns ​uint**

```
● Check caller is pendingAdmin and pendingAdmin ≠ address(0)
● Store admin with value pendingAdmin
● Unset pendingAdmin
● Emit ​ NewAdmin ​ (oldAdmin, newAdmin)
● Emit ​ NewPendingAdmin ​ (oldPendingAdmin, 0)
```
**_setPriceOracle(​address​ newOracle)**

```
● Check caller is ​ admin ​OR caller is ​ currentImplementation ​and origin is​ admin
● Ensureinvoke newOracle.isPriceOracle()returns true
● Set the comptroller's oracle to ​ newOracle
● Emit ​ NewPriceOracle ​(​ oldOracle ​, ​ newOracle ​)
```
**_setLiquidationIncentive(​scaled​ newIncentive)**

```
● Check caller is ​ admin ​OR caller is ​ currentImplementation ​and origin is​ admin
● Check de-scaled 1 ≤ ​ newLiquidationDiscount ​ ≤ 1.5
● Set liquidation incentive to ​ newIncentive
● Emit ​ NewLiquidationIncentive ​(oldIncentive, newIncentive)
```

**_setCollateralFactor(​CToken​ cToken, ​scaled​ newFactor) returns ​uint**

```
● Check caller is ​ admin ​OR caller is ​ currentImplementation ​and origin is​ admin
● Verify market is listed
● Check ​ newFactor ​ ≤ 0.9
● If ​ newFactor ​ > 0, fail iforacle.getUnderlyingPrice(cToken)≠ 0
● Set market's collateral factor to ​ newFactor
● Emit ​ NewCollateralFactor ​(​ cToken ​, ​ oldFactor ​, ​ newFactor)
```
**_setCloseFactor(​scaled​ newCloseFactor) returns ​uint**

```
● Check caller is ​ admin ​OR caller is ​ currentImplementation ​and origin is​ admin
● Check 0.05 < ​ newCloseFactor ​ ≤ 0.9
● Set close factor to ​ newCloseFactor
● Emit ​ NewCloseFactor ​(old​ CloseFactor ​, ​ newCloseFactor)
```
**_setMaxAssets(​uint​ newMaxAssets) returns ​uint**

```
● Check caller is ​ admin ​OR caller is ​ currentImplementation ​and origin is​ admin
● Set maxAssets to ​ newMaxAssets
● Emit ​ NewMaxAssets ​ (oldMaxAssets, newMaxAssets)
```
**_supportMarket(​CToken​ cToken) returns ​uint**

```
● Check caller is admin
● Verify asset is not isListed
● Ensure call cToken.isCToken()returns true
● Set market is listed to true
● Append cToken to ​ markets ​ list.
● Emit ​ MarketListed ​(cToken)
```
#### Implementation Upgrade Functions

The comptroller is designed as an upgradeable proxy inspired by patterns described by
zeppelinOS​. In short, the pattern is

1. Deploy new implementation
2. call comptroller._setPendingImplementation(newImplementation)
3. call newImplementation.becomeBrains(comptroller, ...)

**_setPendingImplementation(​address​ newPendingImplementation) returns ​uint**

```
● Check caller is admin
```

```
● Store ​ pendingComptrollerImplementation ​ with value ​ newPendingImplementation
● Emit ​ NewPendingImplementation ​(​ oldPendingAdminImplementation ​,
newPendingImplementation ​)
```
**_acceptImplementation() returns ​uint**

```
● Check ​ caller ​ is ​ pendingComptrollerImplementation ​ and
pendingComptrollerImplementation ​ ≠ ​ address(0)
● Store ​ comptrollerImplementation ​ with value ​ pendingComptrollerImplementation
● Unset ​ pendingComptrollerImplementation
● Emit ​ NewImplementation ​ (oldImplementation, newImplementation)
● Emit ​ NewPendingImplementation ​ (oldPendingImplementation, 0)
```
**Note: _becomeBrains is called on the implementation address, where the other functions are
all called on the active comptroller.**

**_becomeBrains(​address​ unitroller, ​address​ oracle, ​uint​ closeFactor, ​uint​ maxAssets) returns
uint**

```
● Check caller is admin of unitroller
● Ensure call unitroller._acceptImplementation()returns true
● Ensurecall unitroller._setMarketPriceOracle(oracle)= 0
● Ensurecall unitroller._setCloseFactor(closeFactor)= 0
● Ensurecall unitroller._setMaxAssets(maxAssets)= 0
● Ensurecall unitroller._setLiquidationIncentive(liquidationIncentiveMinMantissa)= 0
```
### Maximillion Contract

For cErc20 contracts, we support repaying a borrow fully using the special ‘-1’ amount. Since
the CToken contract is approved to transfer what it needs, it can determine the borrow
amount and then transfer the exact amount, post-interest accrual, directly within the
repayBorrow function.

For cEther, things work a bit differently. Since ‘-1’ is actually UINT_MAX, it’s practically
impossible for anyone to transfer this amount to the repay function. In order to completely
repay a borrow in cEther, we deploy a separate contract to handle the details of collecting
more than enough Ether to repay the borrow plus recent interest, and then refunding the
overpay amount.


**Repay Behalf(​address​ borrower) payable**

```
● Remember the amount of Ether received:
○ received=msg.value
● Read the current borrow balance with interest accrued:
○ borrows =invoke cEther.borrowBalanceCurrent(borrower)
● If received>borrows, repay the exact borrow balance and refund:
○ invoke cEther.repayBorrowBehalf.value(borrows)(borrower)
○ Refund received−borrows
● Otherwise, just repay the amount of Ether provided:
○ invoke cEther.repayBorrowBehalf.value(received)(borrower)
```
### Appendix

#### Market States

A given asset may be in one of four states, which affect which functions are available and
how the asset is utilized above.

```
● Unsupported - An asset is not part of the “listedAssets” set. It is not used when
calculating sumCollateral and all operations, aside of “supportMarket” for that asset
should fail.
● Listed - An asset is part of the “listedAssets” set. It is not used when calculating
sumCollateral and only “supply”, “withdraw” and “repayBorrow” operations on that
asset should functional normally. The asset must have an interest rate model
associated with it.
● Borrow - An asset is part of the “listedAssets” set. It is not used when calculating
sumCollateral and all operations on that asset should functional normally. The asset
must have a non-zero price and interest rate model associated with it. A listed market
with non-zero price allows that market to be borrowed from.
● Collateral - An asset is part of the “listedAssets” set. It is used when calculating
sumCollateral and all operations on that asset should functional normally. The asset
must have a non-zero price, non-zero collateral factor and interest rate model
associated with it. A borrow market with a non-zero collateral factor is both
borrowable and can be used as collateral.
```
Regarding membership, listed⊆borrow⊆collateral and (listed ⋂unsupported) = ⊘
Regarding available functionality, listed⊇borrow⊇collateral and unsupported = ⊘


#### Interest Index Calculation

The interest index tracks the interest owed on $1 (or some constant initial amount) of debt
since the protocol’s deployment. That is, the interest on a fixed amount of the borrowed
asset over time.

Whenever the interest rate changes, the index applies the simple interest formula, to
snapshot the effect of the prior interest rate since that time:

```
index 0 =c, c > 0
indexi+△blocks=indexi⋅ ( 1 + △blocks×ratei)
```
Whenever the index is updated, we also update the total borrow (and reserves) amount, to
capture the effect on all the currently borrowed (reserved) units of the asset since the last
update:

```
borrowsi+△blocks=borrowsi ⋅ ( 1 + △blocks×ratei)
```
The total borrow amount is used to manage the market’s ledger, and is updated often to
maintain accurate current information. On the other hand, each individual borrow is only
updated when an action related to that specific borrow is taken.

When a borrow is created, we store with it the principal amount and the interest index at that
time. Whenever an action which affects the principal of the borrow is initiated, we first
calculate a new principal, based on the interest that has accumulated since the last event.

In order to determine how much interest has accumulated, we take the current index value
and compare it to the interest index at the time of the last event which was stored in the
borrow balance. The ratio of these values yields the change in $1 of debt since the principal
was last recorded, for which we then calculate a new principal amount to store with the new
index.

The ratio borrowIndexi+b/borrowIndexi is the simple interest rate over the period, which we
apply for the whole period in order to accrue interest on the principal:

```
effectiveRate=borrowIndexi+△blocks / borrowIndexi
principali+△blocks=principali ⋅ ( 1 + △blocks ⋅ effectiveRate) + ∆
```

```
borrowIndexi+△blocks=borrowIndexi
```
#### Mint / Redeem exchange rate remains the same when minting and redeeming

#### coins

Let
A = assets = cash + borrows held by the protocol
L = liabilities = tokens minted and not redeemed
dA = change in assets = cash supplied|withdrawn or borrows sent|repaid
dL = change in liabilities = tokens to mint|redeem
R = exchange rate = A / L
A′ = next assets = A + dA
L′ = next liabilities = L + dL
R′ = next exchange rate = A′ / L′

Prove that R′ = R , whenever there is a change in dA, where dA / dL = R = A / L.

dL = dA / R= L (^) * dA / A
R′ = A′ / L′
= (A + dA) / (L + dL)
= (A + dA) / (L + L (^) * dA / A)
= (A + dA) / (L (^) * ( 1 + dA / A))
= (A + dA) / (L (^) * (A / A + dA / A))
= (A + dA) / (L (^) * (A + dA) / A)
= 1 / L / A
= A / L
= R
q.e.d.

---

<a id="doc_2"></a>

## Dripper Specification

*파일 경로: dripper.md*

### Compound Engineering

### Overview

Comp will be distributed to the community through the Flywheel mechanism in the Comptroller.
To prevent the community from making a proposal to speed up the Flywheel (or simply gift the
Comp to some other address), we propose a Dripper that will give the Comptroller its Comp
tokens over a period of years. The Dripper will be a separate smart contract with a large Comp
balance and a mechanism to transfer that Comp to the Flywheel given some constraint on the
rate of transfer. We aim to make this contract as simple as possible.

### Mechanism

We propose a mechanism that simply tracks how much Comp has been moved versus an
immutable rate function. Effectively, we take the following graph and track our previous
y-coordinate (​ _Dripped_ ​). For each call to Drip(), we look at our expected y-coordinate (​ _DripTotal_ ​),
subtract the previous Dripped value, and send that delta amount of Comp to the Flywheel.
This graph shows how much Comp should have been Dripped from some starting point (here
we start at block 10MM and we drip 2 Comp/Block).


### Algorithm

Static Configuration:
● DripStart: A block number when dripping should start
● DripRate: Amount of Comp which should be dripped per block
● Token: Address of Token to Distribute
● Target: Target of Dripper
State:
● Dripped: Amount of Token that has already been transferred to Flywheel
Externals:
● Token.balanceOf(Dripper): Dripper's own Token balance
● Token.transfer(Target, amount): Side-effecting function to transfer Token to Target
● Block(): Current Ethereum block number
d
Define Initialize(DripRate*, Token*, Target)
SET Dripped= 0
SET DripStart = Block()
SET DripRate=DripRate*
SET Token = Token*
SET Target = Target *
Define Drip()
DripTotal =DripRate×(Block()−DripStart)
DeltaDrip =DripTotal −Dripped
ToDript=min(CALL Token.balanceOf(Dripper), DeltaDrip)
Assert ToDrip ≥ 0
SET Dripped=Dripped+ToDrip
CALL Token.transfer(Target, ToDrip)

### Correctness

To prove the previous algorithm correct, first we note that DripTotal is always the exact amount
that should have been dripped since the start of the contract as it matches the equation listed
above. Assume, for the moment, Dripper's balance of Comp is sufficiently large. We break into
an inductive proof. In the base case, Dripped is zero and we transfer exactly DripTotal tokens,
which is the correct amount. In the inductive case, we have already transferred Dripped tokens,
which we assert from inductive was the correct amount that should have been dripped. We are


now calculating the amount owed since the beginning and subtracting the amount we have
dripped. This is the exact amount we need to transfer to match DripTotal. This is thus also
correct and completes our proof.

#### A Quick Aside

First, we note that our inductive case will succeed ​ _even if_ ​ Dripped was not the correct amount to
be dripped previously, so long as Dripped is less than or equal to DripTotal. That is, it doesn't
matter how much we previously dripped, so long as we haven't dripped too much, since the next
call to Drip will correct any issues.

#### With a Variable Comp Balance

Now we consider the case where the Comp balance is less than sufficient in some cases. Here,
we revise our proof using the aside above to realize that the proof still holds so long as we can
show that Dripped is never greater than DripTotal in our inductive case. We show this by our
_min_ ​ statement, which says that we never set ToDrip to be greater than DeltaDrip, though it may
be less than DeltaDrip. Finally, we relax the constraint in our proof that we always Drip to the
correct DripTotal and instead say that "given a sufficient Comp balance, we always Drip to the
correct DripTotal." This completes our (modified) proof.

#### Assertions

```
● Block() ≥DripStart - Blocks always increase
● DripRate×(Block()−DripStart)does not overflow
● Note: DripTotal+ToDripcannot overflow since it is strictly less than or equal to
DripTotal.
```

---

<a id="doc_3"></a>

## 📁 scenario / Types

*파일 경로: scenario/SCENARIO.md*

* `name:<Type>` - Helper to describe arguments with names, not actually input this way
* `<Bool>` - `True` or `False`
* `<Number>` - A standard number (e.g. `5` or `6.0` or `10.0e18`)
* `<CToken>` - The local name for a given cToken when created, e.g. `cZRX`
* `<User>` - One of: `Admin, Bank, Geoff, Torrey, Robert, Coburn, Jared`
* `<String>` - A string, may be quoted but does not have to be if a single-word (e.g. `"Mint"` or `Mint`)
* `<Address>` - TODO
* `<Assertion>` - See assertions below.

## Events

### Core Events

* "History n:<Number>=5" - Prints history of actions
  * E.g. "History"
  * E.g. "History 10"
* `Read ...` - Reads given value and prints result
  * E.g. `Read CToken cBAT ExchangeRateStored` - Returns exchange rate of cBAT
* `Assert <Assertion>` - Validates given assertion, raising an exception if assertion fails
  * E.g. `Assert Equal (Erc20 BAT TokenBalance Geoff) (Exactly 5.0)` - Returns exchange rate of cBAT
* `FastForward n:<Number> Blocks` - For `CTokenScenario`, moves the block number forward n blocks. Note: in `CTokenScenario` the current block number is mocked (starting at 100000). Thus, this is the only way for the protocol to see a higher block number (for accruing interest).
  * E.g. `FastForward 5 Blocks` - Move block number forward 5 blocks.
* `Inspect` - Prints debugging information about the world
* `Debug message:<String>` - Same as inspect but prepends with a string
* `From <User> <Event>` - Runs event as the given user
  * E.g. `From Geoff (CToken cZRX Mint 5e18)`
* `Invariant <Invariant>` - Adds a new invariant to the world which is checked after each transaction
  * E.g. `Invariant Static (CToken cZRX TotalSupply)`
* `WipeInvariants` - Removes all invariants.
* `Comptroller <ComptrollerEvent>` - Runs given Comptroller event
  * E.g. `Comptroller _setReserveFactor 0.5`
* `CToken <CTokenEvent>` - Runs given CToken event
  * E.g. `CToken cZRX Mint 5e18`
* `Erc20 <Erc20Event>` - Runs given Erc20 event
  * E.g. `Erc20 ZRX Facuet Geoff 5e18`
* `InterestRateModel ...event` - Runs given interest rate model event
  * E.g. `InterestRateModel Deployed (Fixed 0.5)`
* `PriceOracle <PriceOracleEvent>` - Runs given Price Oracle event
  * E.g. `PriceOracle SetPrice cZRX 1.5`

### Comptroller Events

* "Comptroller Deploy ...comptrollerParams" - Generates a new Comptroller
  * E.g. "Comptroller Deploy Scenario (PriceOracle Address) 0.1 10"
* `Comptroller SetPaused action:<String> paused:<Bool>` - Pauses or unpaused given cToken function (e.g. Mint)
  * E.g. `Comptroller SetPaused Mint True`
* `Comptroller SupportMarket <CToken>` - Adds support in the Comptroller for the given cToken
  * E.g. `Comptroller SupportMarket cZRX`
* `Comptroller EnterMarkets <User> <CToken> ...` - User enters the given markets
  * E.g. `Comptroller EnterMarkets Geoff cZRX cETH`
* `Comptroller SetMaxAssets <Number>` - Sets (or resets) the max allowed asset count
  * E.g. `Comptroller SetMaxAssets 4`
* `CToken <cToken> SetOracle oracle:<Contract>` - Sets the oracle
  * E.g. `Comptroller SetOracle (Fixed 1.5)`
* `Comptroller SetCollateralFactor <CToken> <Number>` - Sets the collateral factor for given cToken to number
  * E.g. `Comptroller SetCollateralFactor cZRX 0.1`
* `FastForward n:<Number> Blocks` - Moves the block number forward `n` blocks. Note: in `CTokenScenario` and `ComptrollerScenario` the current block number is mocked (starting at 100000). This is the only way for the protocol to see a higher block number (for accruing interest).
  * E.g. `Comptroller FastForward 5 Blocks` - Move block number forward 5 blocks.

### cToken Events

* `CToken Deploy name:<CToken> underlying:<Contract> comptroller:<Contract> interestRateModel:<Contract> initialExchangeRate:<Number> decimals:<Number> admin:<Address>` - Generates a new comptroller and sets to world global
  * E.g. `CToken Deploy cZRX (Erc20 ZRX Address) (Comptroller Address) (InterestRateModel Address) 1.0 18`
* `CToken <cToken> AccrueInterest` - Accrues interest for given token
  * E.g. `CToken cZRX AccrueInterest`
* `CToken <cToken> Mint <User> amount:<Number>` - Mints the given amount of cToken as specified user
  * E.g. `CToken cZRX Mint Geoff 1.0`
* `CToken <cToken> Redeem <User> amount:<Number>` - Redeems the given amount of cToken as specified user
      * E.g. `CToken cZRX Redeem Geoff 1.0e18`
* `CToken <cToken> Borrow <User> amount:<Number>` - Borrows the given amount of this cToken as specified user
      * E.g. `CToken cZRX Borrow Geoff 1.0e18`
* `CToken <cToken> ReduceReserves amount:<Number>` - Reduces the reserves of the cToken
      * E.g. `CToken cZRX ReduceReserves 1.0e18`
* `CToken <cToken> SetReserveFactor amount:<Number>` - Sets the reserve factor for the cToken
      * E.g. `CToken cZRX SetReserveFactor 0.1`
* `CToken <cToken> SetInterestRateModel interestRateModel:<Contract>` - Sets the interest rate model for the given cToken
  * E.g. `CToken cZRX SetInterestRateModel (Fixed 1.5)`
* `CToken <cToken> SetComptroller comptroller:<Contract>` - Sets the comptroller for the given cToken
  * E.g. `CToken cZRX SetComptroller Comptroller`
* `CToken <cToken> Mock variable:<String> value:<Number>` - Mocks a given value on cToken. Note: value must be a supported mock and this will only work on a CTokenScenario contract.
  * E.g. `CToken cZRX Mock totalBorrows 5.0e18`
  * E.g. `CToken cZRX Mock totalReserves 0.5e18`

### Erc-20 Events

* `Erc20 Deploy name:<Erc20>` - Generates a new ERC-20 token by name
  * E.g. `Erc20 Deploy ZRX`
* `Erc20 <Erc20> Approve <User> <Address> <Amount>` - Adds an allowance between user and address
  * E.g. `Erc20 ZRX Approve Geoff cZRX 1.0e18`
* `Erc20 <Erc20> Faucet <Address> <Amount>` - Adds an arbitrary balance to given user
  * E.g. `Erc20 ZRX Facuet Geoff 1.0e18`

### Price Oracle Events

* `Deploy` - Generates a new price oracle (note: defaults to (Fixed 1.0))
  * E.g. `PriceOracle Deploy (Fixed 1.0)`
  * E.g. `PriceOracle Deploy Simple`
  * E.g. `PriceOracle Deploy NotPriceOracle`
* `SetPrice <CToken> <Amount>` - Sets the per-ether price for the given cToken
  * E.g. `PriceOracle SetPrice cZRX 1.0`

### Interest Rate Model Events

### Deploy

* `Deploy params:<String[]>` - Generates a new interest rate model (note: defaults to (Fixed 0.25))
  * E.g. `InterestRateModel Deploy (Fixed 0.5)`
  * E.g. `InterestRateModel Deploy Whitepaper`

## Values

### Core Values

* `True` - Returns true
* `False` - Returns false
* `Zero` - Returns 0
* `Some` - Returns 100e18
* `Little` - Returns 100e10
* `Exactly <Amount>` - Returns a strict numerical value
  * E.g. `Exactly 5.0`
* `Exp <Amount>` - Returns the mantissa for a given exp
  * E.g. `Exp 5.5`
* `Precisely <Amount>` - Matches a number to given number of significant figures
  * E.g. `Exactly 5.1000` - Matches to 5 sig figs
* `Anything` - Matches anything
* `Nothing` - Matches nothing
* `Default value:<Value> default:<Value>` - Returns value if truthy, otherwise default. Note: this does short-circuit
* `LastContract` - Returns the address of last constructed contract
* `User <...>` - Returns User value (see below)
* `Comptroller <...>` - Returns Comptroller value (see below)
* `CToken <...>` - Returns CToken value (see below)
* `Erc20 <...>` - Returns Erc20 value (see below)
* `InterestRateModel <...>` - Returns InterestRateModel value (see below)
* `PriceOracle <...>` - Returns PriceOracle value (see below)

### User Values

* `User <User> Address` - Returns address of user
  * E.g. `User Geoff Address` - Returns Geoff's address

### Comptroller Values

* `Comptroller Liquidity <User>` - Returns a given user's trued up liquidity
  * E.g. `Comptroller Liquidity Geoff`
* `Comptroller MembershipLength <User>` - Returns a given user's length of membership
  * E.g. `Comptroller MembershipLength Geoff`
* `Comptroller CheckMembership <User> <CToken>` - Returns one if user is in asset, zero otherwise.
  * E.g. `Comptroller CheckMembership Geoff cZRX`
* "Comptroller CheckListed <CToken>" - Returns true if market is listed, false otherwise.
  * E.g. "Comptroller CheckListed cZRX"

### CToken Values
* `CToken <CToken> UnderlyingBalance <User>` - Returns a user's underlying balance (based on given exchange rate)
  * E.g. `CToken cZRX UnderlyingBalance Geoff`
* `CToken <CToken> BorrowBalance <User>` - Returns a user's borrow balance (including interest)
  * E.g. `CToken cZRX BorrowBalance Geoff`
* `CToken <CToken> TotalBorrowBalance` - Returns the cToken's total borrow balance
  * E.g. `CToken cZRX TotalBorrowBalance`
* `CToken <CToken> Reserves` - Returns the cToken's total reserves
  * E.g. `CToken cZRX Reserves`
* `CToken <CToken> Comptroller` - Returns the cToken's comptroller
  * E.g. `CToken cZRX Comptroller`
* `CToken <CToken> PriceOracle` - Returns the cToken's price oracle
  * E.g. `CToken cZRX PriceOracle`
* `CToken <CToken> ExchangeRateStored` - Returns the cToken's exchange rate (based on balances stored)
  * E.g. `CToken cZRX ExchangeRateStored`
* `CToken <CToken> ExchangeRate` - Returns the cToken's current exchange rate
  * E.g. `CToken cZRX ExchangeRate`

### Erc-20 Values

* `Erc20 <Erc20> Address` - Returns address of ERC-20 contract
  * E.g. `Erc20 ZRX Address` - Returns ZRX's address
* `Erc20 <Erc20> Name` - Returns name of ERC-20 contract
  * E.g. `Erc20 ZRX Address` - Returns ZRX's name
* `Erc20 <Erc20> Symbol` - Returns symbol of ERC-20 contract
  * E.g. `Erc20 ZRX Symbol` - Returns ZRX's symbol
* `Erc20 <Erc20> Decimals` - Returns number of decimals in ERC-20 contract
  * E.g. `Erc20 ZRX Decimals` - Returns ZRX's decimals
* `Erc20 <Erc20> TotalSupply` - Returns the ERC-20 token's total supply
  * E.g. `Erc20 ZRX TotalSupply`
  * E.g. `Erc20 cZRX TotalSupply`
* `Erc20 <Erc20> TokenBalance <Address>` - Returns the ERC-20 token balance of a given address
  * E.g. `Erc20 ZRX TokenBalance Geoff` - Returns a user's ZRX balance
  * E.g. `Erc20 cZRX TokenBalance Geoff` - Returns a user's cZRX balance
  * E.g. `Erc20 ZRX TokenBalance cZRX` - Returns cZRX's ZRX balance
* `Erc20 <Erc20> Allowance owner:<Address> spender:<Address>` - Returns the ERC-20 allowance from owner to spender
  * E.g. `Erc20 ZRX Allowance Geoff Torrey` - Returns the ZRX allowance of Geoff to Torrey
  * E.g. `Erc20 cZRX Allowance Geoff Coburn` - Returns the cZRX allowance of Geoff to Coburn
  * E.g. `Erc20 ZRX Allowance Geoff cZRX` - Returns the ZRX allowance of Geoff to the cZRX cToken

### PriceOracle Values

* `Address` - Gets the address of the global price oracle
* `Price asset:<Address>` - Gets the price of the given asset

### Interest Rate Model Values

* `Address` - Gets the address of the global interest rate model

## Assertions

* `Equal given:<Value> expected:<Value>` - Asserts that given matches expected.
  * E.g. `Assert Equal (Exactly 0) Zero`
  * E.g. `Assert Equal (CToken cZRX TotalSupply) (Exactly 55)`
  * E.g. `Assert Equal (CToken cZRX Comptroller) (Comptroller Address)`
* `True given:<Value>` - Asserts that given is true.
  * E.g. `Assert True (Comptroller CheckMembership Geoff cETH)`
* `False given:<Value>` - Asserts that given is false.
  * E.g. `Assert False (Comptroller CheckMembership Geoff cETH)`
* `Failure error:<String> info:<String> detail:<Number?>` - Asserts that last transaction had a graceful failure with given error, info and detail.
  * E.g. `Assert Failure UNAUTHORIZED SUPPORT_MARKET_OWNER_CHECK`
  * E.g. `Assert Failure MATH_ERROR MINT_CALCULATE_BALANCE 5`
* `Revert` - Asserts that the last transaction reverted.
* `Success` - Asserts that the last transaction completed successfully (that is, did not revert nor emit graceful failure).
* `Log name:<String> ((key:<String> value:<Value>) ...)` - Asserts that last transaction emitted log with given name and key-value pairs.
  * E.g. `Assert Log Minted (("account" (User Geoff address)) ("amount" (Exactly 55)))`

---

*병합된 문서의 끝*
