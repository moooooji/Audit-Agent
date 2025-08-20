# Berachain 문서

*이 문서는 모든 Berachain 문서를 하나의 종합적인 참조로 결합합니다.*

## 목차

1. [Table of Contents](#doc_1)
2. [Aave Protocol Overview](#doc_2)
3. [Concepts | Aave Protocol Documentation](#doc_3)
4. [concepts/Borrow | Aave Protocol Documentation](#doc_4)
5. [concepts/Flash Loans | Aave Protocol Documentation](#doc_5)
6. [concepts/Liquidations | Aave Protocol Documentation](#doc_6)
7. [concepts/Liquidity Protocol | Aave Protocol Documentation](#doc_7)
8. [concepts/Repay | Aave Protocol Documentation](#doc_8)
9. [concepts/Risks | Aave Protocol Documentation](#doc_9)
10. [concepts/Supply | Aave Protocol Documentation](#doc_10)
11. [concepts/Withdraw | Aave Protocol Documentation](#doc_11)
12. [developers/Aave V3 | Aave Protocol Documentation](#doc_12)
13. [developers/Credit Delegation | Aave Protocol Documentation](#doc_13)
14. [developers/Flash Loans | Aave Protocol Documentation](#doc_14)
15. [developers/GHO | Aave Protocol Documentation](#doc_15)
16. [developers/Governance | Aave Protocol Documentation](#doc_16)
17. [developers/Legacy Versions | Aave Protocol Documentation](#doc_17)
18. [developers/Safety Module | Aave Protocol Documentation](#doc_18)
19. [developers/Smart Contracts | Aave Protocol Documentation](#doc_19)
20. [developers/Testing & Debugging | Aave Protocol Documentation](#doc_20)
21. [developers/legacy_versions/Aave V1 | Aave Protocol Documentation](#doc_21)
22. [developers/legacy_versions/Aave V2 | Aave Protocol Documentation](#doc_22)
23. [developers/smart_contracts/ACL Manager | Aave Protocol Documentation](#doc_23)
24. [developers/smart_contracts/Incentives | Aave Protocol Documentation](#doc_24)
25. [developers/smart_contracts/Interest Rate Strategy | Aave Protocol Documentation](#doc_25)
26. [developers/smart_contracts/L2 Pool | Aave Protocol Documentation](#doc_26)
27. [developers/smart_contracts/Oracles | Aave Protocol Documentation](#doc_27)
28. [developers/smart_contracts/Pool Addresses Provider | Aave Protocol Documentation](#doc_28)
29. [developers/smart_contracts/Pool Configurator | Aave Protocol Documentation](#doc_29)
30. [developers/smart_contracts/Pool | Aave Protocol Documentation](#doc_30)
31. [developers/smart_contracts/Switch Adapters | Aave Protocol Documentation](#doc_31)
32. [developers/smart_contracts/Tokenization | Aave Protocol Documentation](#doc_32)
33. [developers/smart_contracts/View Contracts | Aave Protocol Documentation](#doc_33)
34. [developers/smart_contracts/Wrapped Token Gateway | Aave Protocol Documentation](#doc_34)
35. [primitives/AAVE Token | Aave Protocol Documentation](#doc_35)
36. [primitives/GHO Token | Aave Protocol Documentation](#doc_36)
37. [primitives/Governance | Aave Protocol Documentation](#doc_37)
38. [primitives/Incentives | Aave Protocol Documentation](#doc_38)
39. [primitives/Liquidity Pool | Aave Protocol Documentation](#doc_39)
40. [primitives/Oracle | Aave Protocol Documentation](#doc_40)
41. [primitives/Reserve | Aave Protocol Documentation](#doc_41)
42. [primitives/Safety Module | Aave Protocol Documentation](#doc_42)
43. [resources/Access Controls Dashboard | Aave Protocol Documentation](#doc_43)
44. [resources/Addresses Dashboard | Aave Protocol Documentation](#doc_44)
45. [resources/Changelog | Aave Protocol Documentation](#doc_45)
46. [resources/Code Licensing | Aave Protocol Documentation](#doc_46)
47. [resources/Glossary | Aave Protocol Documentation](#doc_47)
48. [resources/Parameters Dashboard | Aave Protocol Documentation](#doc_48)
49. [resources/Web3 | Aave Protocol Documentation](#doc_49)

---

<a id="doc_1"></a>

## Table of Contents

*파일 경로: TABLE_OF_CONTENTS.md*

- [Aave Documentation](./index.md)
  - [Concepts](./concepts.md)
    - [Borrow](./concepts/borrow.md)
    - [Flash Loans](./concepts/flash-loans.md)
    - [Liquidations](./concepts/liquidations.md)
    - [Liquidity Protocol](./concepts/liquidity-protocol.md)
    - [Repay](./concepts/repay.md)
    - [Risks](./concepts/risks.md)
    - [Supply](./concepts/supply.md)
    - [Withdraw](./concepts/withdraw.md)
  - developers
    - [Aave V3](./developers/aave-v3.md)
    - [Credit Delegation](./developers/credit-delegation.md)
    - [Flash Loans](./developers/flash-loans.md)
    - [GHO](./developers/gho.md)
    - [Governance](./developers/governance.md)
    - [Legacy Protocol Versions](./developers/legacy-versions.md)
      - [Aave v1](./developers/legacy-versions/v1.md)
      - [Aave v2](./developers/legacy-versions/v2.md)
    - [Safety Module](./developers/safety-module.md)
    - [Smart Contracts](./developers/smart-contracts.md)
      - [ACLManager](./developers/smart-contracts/acl-manager.md)
      - [Incentives](./developers/smart-contracts/incentives.md)
      - [Interest Rate Strategy](./developers/smart-contracts/interest-rate-strategy.md)
      - [L2Pool](./developers/smart-contracts/l2-pool.md)
      - [AaveOracle](./developers/smart-contracts/oracles.md)
      - [Pool](./developers/smart-contracts/pool.md)
      - [PoolAddressesProvider](./developers/smart-contracts/pool-addresses-provider.md)
      - [Pool Configurator](./developers/smart-contracts/pool-configurator.md)
      - [Switch Adapters](./developers/smart-contracts/switch-adapters.md)
      - [Tokenization](./developers/smart-contracts/tokenization.md)
      - [View Contracts](./developers/smart-contracts/view-contracts.md)
      - [Wrapped Token Gateway](./developers/smart-contracts/wrapped-token-gateway.md)
    - [Testing & Debugging](./developers/testing-and-debugging.md)
  - primitives
    - [AAVE](./primitives/aave.md)
    - [GHO](./primitives/gho.md)
    - [Governance](./primitives/governance.md)
    - [Incentives](./primitives/incentives.md)
    - [Liquidity Pool](./primitives/liquidity-pool.md)
    - [Oracle](./primitives/oracle.md)
    - [Reserve](./primitives/reserve.md)
    - [Safety Module](./primitives/safety-module.md)
  - resources
    - [Aave Protocol Access Controls](./resources/access-controls.md)
    - [Aave Protocol Deployed Contracts](./resources/addresses.md)
    - [Changelog](./resources/changelog.md)
    - [Code Licensing](./resources/code-licensing.md)
    - [Aave Docs Glossary](./resources/glossary.md)
    - [Aave Protocol Parameter Dashboard](./resources/parameters.md)
    - [Web3](./resources/web3.md)

---

<a id="doc_2"></a>

## Aave Protocol Overview

*파일 경로: docs.md*

Source: https://aave.com/docs

[

GHO

The Aave-native stablecoin.

Learn More

](https://aave.com/gho)

## Aave Documentation

[](#aave-documentation)

Aave is a decentralised non-custodial liquidity protocol where users can participate as suppliers or borrowers. Suppliers provide liquidity to the market while earning interest, and borrowers can access liquidity by providing collateral that exceeds the borrowed amount.

### Get Familiar with Aave

[](#get-familiar-with-aave)

[

Concepts

Learn the basics.



](/docs/concepts)

[

Governance

Community governance process.



](/docs/primitives/governance)

[

Addresses

Protocol smart contracts.



](/docs/resources/addresses)

[

Parameters

View market parameters.



](/docs/resources/parameters)

[

Security

Security audits and resources.

](https://aave.com/security)

### Use Aave

[](#use-aave)

[

App

Supply, borrow, vote, and more.

](https://app.aave.com)

[

GHO

Learn about the GHO stablecoin.



](/docs/primitives/gho)

[

Next

**Concepts**

](/docs/concepts)

---

<a id="doc_3"></a>

## Concepts | Aave Protocol Documentation

*파일 경로: concepts.md*

Source: https://aave.com/docs/concepts

## Concepts

[](#concepts)

### Aave Protocol

[](#aave-protocol)

Basics to know when building on the Aave Protocol.

[

Liquidity Protocol

Overcollateralised borrowing.



](/docs/concepts/liquidity-protocol)

[

Supply

Supply tokens to earn interest.



](/docs/concepts/supply)

[

Borrow

Use collateral to borrow tokens.



](/docs/concepts/borrow)

[

Repay

Repay borrow positions.



](/docs/concepts/repay)

[

Withdraw

Redeem supplied tokens.



](/docs/concepts/withdraw)

[

Liquidations

Manage liquidation risks.



](/docs/concepts/liquidations)

[

Risks

Review protocol risks.



](/docs/concepts/risks)

[

Flashloans

Access instant liquidity.



](/docs/concepts/flash-loans)

[

Previous

**Overview**

](/docs)[

Next

**Liquidity Protocol**

](/docs/concepts/liquidity-protocol)

---

<a id="doc_4"></a>

## 📁 concepts / Borrow | Aave Protocol Documentation

*파일 경로: concepts/borrow.md*

Source: https://aave.com/docs/concepts/borrow

## Borrow

[](#borrow)

BorrowersLiquidity Pools

Borrowing tokens from the Aave Protocol allows users to access liquidity by using their supplied tokens as collateral, unlocking capital without selling their assets. However, borrowers face liquidation risk if the value of their collateral falls below the required threshold. Interest rates are determined dynamically, influenced by protocol factors and governance decisions, and can change over time based on community input. Interest accrues based on the utilisation rate, which reflects the percentage of supplied liquidity that is borrowed. Higher utilisation rates lead to higher interest rates, adjusting with demand. Each reserve has specific parameters designed to incentivize both borrowers and suppliers.

To maintain a healthy ratio and avoid liquidation risk, borrowers should actively monitor their collateralization level, keeping their health factor in check, to assure their borrow positions remain overcollateralised even as market conditions change or interest accrues.

[

Previous

**Supply**

](/docs/concepts/supply)[

Next

**Repay**

](/docs/concepts/repay)

---

<a id="doc_5"></a>

## 📁 concepts / Flash Loans | Aave Protocol Documentation

*파일 경로: concepts/flash_loans.md*

Source: https://aave.com/docs/concepts/flash-loans

## Flash Loans

[](#flash-loans)

Liquidity PoolFlash LoanReceiver

Flash Loans are special transactions that allow users to borrow an asset for a single block, provided they repay the borrowed amount and a fee within that same block time. Sometimes these actions are also referred to as “One Block Borrows.” Flash Loans do not require any collateral upfront. There is no direct real-world analogy to Flash Loans, so it requires some basic understanding of how state is managed within blocks in blockchains.

There are tools allowing users to utilise Flash Loans to access liquidity in the background for advanced features such as repay with collateral, collateral switch, and more.

Example interfaces that integrate Flash Loans are [DeFi Saver](https://defisaver.com), [Instadapp](https://instadapp.io/), and [Furucombo](https://furucombo.app/).

Flash Loans let users borrow from a pool’s reserves (if borrowing is enabled) for one transaction, provided they repay the amount taken plus a fee (0.07% in Aave V2, 0.05% in Aave V3) or open a borrow position within the same transaction.

Due to the technical knowledge required to execute a Flash Loan, the feature is designed for developers. To do a Flash Loan, users will need to build a contract that requests a Flash Loan. For more information on integrating flash loans, see the [developers' guide](/docs/developers/flash-loans).

[

Previous

**Risks**

](/docs/concepts/risks)[

Next

**Liquidity Pool**

](/docs/primitives/liquidity-pool)

---

<a id="doc_6"></a>

## 📁 concepts / Liquidations | Aave Protocol Documentation

*파일 경로: concepts/liquidations.md*

Source: https://aave.com/docs/concepts/liquidations

## Liquidations

[](#liquidations)

The **health factor** is a critical metric within the Aave Protocol that measures the safety of a borrow position. It is calculated as:

Health Factor = (Total Collateral Value \* Weighted Average Liquidation Threshold) / Total Borrow Value

The health factor measures a borrow position’s stability. A health factor below 1 risks liquidation. The liquidation threshold, set by Aave Governance for each asset, determines the maximum percentage of value that can be borrowed against the asset. For example, if a user supplies $10,000 in ETH with an 80% liquidation threshold and borrows $6,000 in GHO, the health factor would be 1.333.

A health factor above 1 represents a position that is above the liquidation threshold. Regular monitoring is essential, as the health factor fluctuates based on both the value of collateral and borrowed assets. To improve the health factor, users can either supply more collateral or repay part of the borrow position. The health factor is directly tied to collateral value. If the value rises, the health factor improves; if it falls, the health factor declines, increasing the risk of liquidation.

However, there is no universally "safe" health factor. The health factor depends on the volatility and correlation of the assets. Lower health factors may be acceptable, for example, with correlated assets, such as stablecoins or assets closely tied to ETH.

Liquidation happens when a borrower's health factor drops below 1, meaning their collateral is insufficient to cover the borrowed amount. This can occur when the value of collateral decreases or the borrowing amount is increased. When a liquidation occurs, up to 50% of the borrower's debt is repaid by a liquidator. A liquidation fee is also levied against the borrower's collateral. Liquidations are permissionless, meaning any participant within the network can initiate the liquidation of an eligible borrow position.

Liquidations are highly competitive, requiring a deep understanding of the protocol and technical proficiency. Liquidators closely monitor borrow positions, react swiftly to market changes, and prioritise liquidation transactions to be the first to execute the liquidation.

### Tools for Managing Health Factor

[](#tools-for-managing-health-factor)

*   Simulate health factor changes: [DeFi Simulator](https://defisim.xyz/)
    
*   Auto-repay borrow position: [DeFi Saver](https://defisaver.com/)
    

For more information on participating as a liquidator, see the [developer guide](/docs/developers/liquidations).

[

Previous

**Withdraw**

](/docs/concepts/withdraw)[

Next

**Risks**

](/docs/concepts/risks)

---

<a id="doc_7"></a>

## 📁 concepts / Liquidity Protocol | Aave Protocol Documentation

*파일 경로: concepts/liquidity_protocol.md*

Source: https://aave.com/docs/concepts/liquidity-protocol

## Liquidity Protocol

[](#liquidity-protocol)

A **liquidity protocol** is a decentralised system of smart contracts that facilitates the transfer of digital assets. As a leading liquidity protocol that operates on a supply and borrow model, Aave enables users to supply their assets to liquidity pools and, in return, allows other participants to borrow from those pools using their own collateral. The protocol operates across multiple blockchain networks, making it highly accessible to users across different ecosystems.

One of the key features of a decentralised liquidity protocol is its non-custodial nature, meaning users maintain control over their assets at all times. Interaction with the protocol happens through self-custodial wallets, allowing users to supply or borrow funds directly, without relying on intermediaries. All of this is managed through publicly accessible and permissionless smart contracts, which execute and verify transactions based on predefined conditions, such as collateral ratios and market parameters, providing a transparent and trustless experience.

Aave is governed by AAVE token holders. This decentralised governance model further enhances the protocol’s adaptability and accessibility. Governance token holders can propose, vote, and implement changes to the protocol, including adjusting interest rates and collateral requirements as well as other key parameters that impact both borrowers and suppliers. This decentralised management structure means that the protocol can evolve in response to the needs of its community without requiring centralised control.

As a decentralised finance (DeFi) platform, Aave includes a range of features, from its native GHO stablecoin to periphery contracts that simplify complex actions like asset swaps and repayments. The flexibility of a liquidity protocol like Aave highlights the potential of DeFi to offer more open, transparent, and equitable financial services to anyone with access to a blockchain network.

[

Previous

**Concepts**

](/docs/concepts)[

Next

**Supply**

](/docs/concepts/supply)

---

<a id="doc_8"></a>

## 📁 concepts / Repay | Aave Protocol Documentation

*파일 경로: concepts/repay.md*

Source: https://aave.com/docs/concepts/repay

## Repay

[](#repay)

SuppliersLiquidity Pools

Repaying borrowed tokens in the Aave Protocol is an important step for managing borrow positions. Borrowers can repay using the same tokens they borrowed, or repay with aTokens (collateral tokens) of the same underlying token. In addition, there are [periphery contracts](https://github.com/aave/aave-v3-periphery) available that simplify the process by allowing repayment with other tokens, such as other collateral assets, without the need to manually convert them beforehand. This flexibility makes it easier for borrowers to manage and close their positions when needed.

Repayment increases the collateralisation ratio, ensuring adequate collateralization and preventing liquidation. By boosting the collateral relative to what is borrowed, repayment prevents assets from being liquidated and allows borrowers to safely withdraw part of their collateral.

[

Previous

**Borrow**

](/docs/concepts/borrow)[

Next

**Withdraw**

](/docs/concepts/withdraw)

---

<a id="doc_9"></a>

## 📁 concepts / Risks | Aave Protocol Documentation

*파일 경로: concepts/risks.md*

Source: https://aave.com/docs/concepts/risks

## Risks

[](#risks)

The Aave Protocol offers decentralised access to liquidity but is not without risks. Robust risk management measures, including smart contract audits and governance frameworks, are in place to help mitigate risks. Below is an overview of key risks and mitigation efforts.

### Smart Contract Risk

[](#smart-contract-risk)

Smart contracts can contain software bugs or other vulnerabilities within the protocol code and the underlying reserve tokens. To mitigate these risks, Aave’s code is publicly available for audit and has undergone multiple external third-party professional audits. Any proposed changes to the protocol code are thoroughly reviewed and approved prior to implementation by the Aave community. Additionally, the protocol runs a continuous bug bounty program to incentivize external developers to identify and report any issues they may find so they can be fixed.

### Oracle Risk

[](#oracle-risk)

Aave relies on third-party oracles for price feeds and external data, such as redemption ratios for liquid staking tokens. This reliance introduces potential risks such as incorrect valuations if an oracle fails or is compromised. To reduce this risk, Aave uses decentralised oracles like Chainlink, which provide tamper-resistant data feeds, greater reliability, and security measures.

### Collateral Risk

[](#collateral-risk)

The Aave DAO also engages risk service providers who track collateral performance and market stability. The value and liquidity of assets used as collateral can fluctuate, leading to the risk of under collateralisation or bad debt. Aave mitigates these risks by setting key risk parameters such as loan-to-value (LTV) ratios and liquidation thresholds. These parameters are continuously monitored by risk service providers and can be adjusted by Aave governance to respond to market conditions.

### Network / Bridge Risk

[](#network-bridge-risk)

Aave operates across multiple blockchain networks and bridges, each with potential risks such as congestion, censorship, or security vulnerabilities. To address these types of risks, Aave Governance has a robust network onboarding framework that thoroughly vets new networks and bridges before they are integrated into the protocol. Community oversight during the governance process is an important step to validate adoption of secure and reliable systems, minimising risk.

For additional information on Aave Protocol risk management, see [Security & Audits](https://aave.com/security).

[

Previous

**Liquidations**

](/docs/concepts/liquidations)[

Next

**Flash Loans**

](/docs/concepts/flash-loans)

---

<a id="doc_10"></a>

## 📁 concepts / Supply | Aave Protocol Documentation

*파일 경로: concepts/supply.md*

Source: https://aave.com/docs/concepts/supply

## Supply

[](#supply)

SuppliersLiquidity Pools

Supplying tokens to the Aave Protocol allows users to earn interest on their digital assets and utilise supplied tokens as collateral. When tokens are supplied, they are transferred to the Aave liquidity pool, a system of smart contracts that facilitates overcollateralised borrowing of tokens. In Aave, supplied tokens automatically accrue interest based on the current market supply rate. As the balance of supplied tokens increases, interest is accrued dynamically, reflecting the current rate allocated to suppliers.

Interest rates for supplied tokens are determined by the borrow utilisation rate, which measures the proportion of assets currently borrowed against the total supplied in the pool, and by governance parameters that can be adjusted through community decisions. These parameters, including collateralisation requirements and interest rates for suppliers and borrowers, are influenced by onchain inputs such as token balances, oracle prices, and the borrow utilisation ratio. As liquidity is supplied, borrowed, repaid, or withdrawn from the pool, the interest rates are updated accordingly.

[

Previous

**Liquidity Protocol**

](/docs/concepts/liquidity-protocol)[

Next

**Borrow**

](/docs/concepts/borrow)

---

<a id="doc_11"></a>

## 📁 concepts / Withdraw | Aave Protocol Documentation

*파일 경로: concepts/withdraw.md*

Source: https://aave.com/docs/concepts/withdraw

## Withdraw

[](#withdraw)

BorrowersLiquidity Pools

Aave Protocol allows suppliers to withdraw their supplied tokens, including accrued interest, as long as there is sufficient unborrowed liquidity in the reserve. The withdrawal amount is limited by the available underlying assets, and that the user’s ability to maintain a sufficient collateral ratio for their borrow position. Periphery contracts with features such as withdraw and switch, allow users to redeem their supplied liquidity in a different token, providing more options for efficient asset management.

When withdrawing with an active borrow position, it’s crucial to maintain a healthy collateralisation ratio to avoid liquidation. Reducing collateral can lower the health factor, increasing the risk of liquidation. To remain safe, after the withdrawal, the account must stay above the liquidation threshold parameters. Therefore, withdrawals require careful management and consideration of the overall borrow positions to avoid liquidation.

[

Previous

**Repay**

](/docs/concepts/repay)[

Next

**Liquidations**

](/docs/concepts/liquidations)

---

<a id="doc_12"></a>

## 📁 developers / Aave V3 | Aave Protocol Documentation

*파일 경로: developers/aave_v3.md*

Source: https://aave.com/docs/developers/aave-v3

## Aave V3

[](#aave-v3)

SuppliersBorrowersWalletsDappsVariable ratesInterest bearing tokensFlash loansReserve liquidity pools

### Features

[](#features)

The Aave Protocol is a decentralised non-custodial liquidity protocol where users can participate as suppliers, borrowers, or liquidators. Suppliers provide liquidity to a market and can earn interest on the crypto assets provided, while borrowers are able to borrow in an overcollateralized fashion. Borrowers can also engage in one-block borrow transactions (”flash loans”), which do not require overcollateralization.

V3 of the Aave Protocol augments the core concepts of the Aave Protocol (aTokens, instant liquidity, credit delegation, etc.) with new features in the following areas.

#### Capital Efficiency

[](#features-capital-efficiency)

V3 allows users to optimise their assets supplied to the Aave Protocol in terms of yield generation and borrowing power.

#### Efficiency Mode (E-Mode)

[](#features-efficiency-mode-e-mode)

The High Efficiency Mode, or eMode, allows borrowers to extract the highest borrowing power out of their collateral when supplied and borrowed assets are correlated in price, particularly when both are derivatives of the same underlying asset (e.g., stablecoins pegged to USD).

This can enable a wave of new use cases such as high leverage forex trading, highly efficient yield farming (for example, deposit ETH staking derivatives to borrow ETH), and diversified risk management.

#### Isolation Mode

[](#features-isolation-mode)

New assets can be listed as isolated in Aave Protocol V3. Borrowers supplying an isolated asset as collateral cannot supply other assets as collateral (though they can still supply to capture yield). Borrowers using an isolated collateral can only borrow stablecoins that have been configured by Aave governance to be borrowable in isolation mode, up to a specified debt ceiling.

View debt ceiling and borrowable in isolation mode parameters on the [parameter dashboard](/docs/resources/parameters).

NormalUser suppliesNon-isolated tokenCan Borrow:Any AssetCan Supply:Any AssetIsolation ModeUser suppliesisolated tokenCan borrow:TetherUSDTDaiDAIUSD CoinUSDCCan Supply:Any Asset

#### Siloed Borrowing

[](#features-siloed-borrowing)

Siloed Borrowing allows certain assets to be treated as isolated within the protocol. Borrowers using these assets as collateral can only borrow stablecoins configured for siloed assets, with strict borrowing limits defined by the Aave governance. This structure reduces the systemic risk for assets that are highly volatile or less liquid by limiting their borrowing capacities and containing the exposure to siloed assets.

View debt ceiling and siloed assets parameters on the [parameter dashboard](/docs/resources/parameters).

#### Portals

[](#features-portals)

This feature allows the flow of liquidity between Aave V3 markets across different networks. Protocol V3 allows governance-approved bridges to burn aTokens on the source network while instantly minting them on the destination network. The underlying assets can then be supplied to Aave on the destination network in a deferred manner, by passing them to the pool after they have been moved through a bridge.

Aave V3 provides a new system role - BRIDGE - granting permission to leverage the Portal feature. Only addresses with the BRIDGE\_ROLE can move the supplied liquidity in Aave V3.

Aave Governance holds the ability to grant BRIDGE\_ROLE to any cross-chain protocol.

This can help bridging protocols like Connext, Hop Protocol, Anyswap, xPollinate, and novel solutions specifically built to leverage Portal, tap into Aave Protocol liquidity to facilitate seamless cross-chain interactions.

In order to support Portal, the following three additional features are required by the protocol:

*   Mint Unbacked Tokens: Allows addresses with BRIDGE role permission to mint unbacked aTokens to the onBehalfOf address.
    
*   Back Unbacked Tokens: Allows contracts with BRIDGE role permission to back the currently unbacked aTokens with the amount of underlying asset and pay a fee.
    
*   Whitelist Bridges: Allows the Bridge Role Admin to add/remove addresses for BRIDGE\_ROLE.
    

### Integrations

[](#integrations)

#### Live Data

[](#integrations-live-data)

For reliable live data integrations, the recommended approach is to query directly from protocol [view contracts](/docs/developers/smart-contracts/view-contracts) such as the UiPoolDataProvider. This enables you to access all reserve information and user positions efficiently.

To simplify the process of querying Aave Protocol data through a blockchain RPC, you can use the Aave Utilities SDK, which is an extension of ethers v5. It streamlines data fetching and formatting, making it easier to interact with the protocol.

You can learn how to fetch data by following the instructions in the [Fetch Data](https://github.com/aave/aave-utilities#data-methods-setup) section of the SDK documentation. After fetching the data, you might need to format it for your application; the [Format Data](https://github.com/aave/aave-utilities#formatreserves) guide provides detailed instructions on how to format reserves and other relevant data structures. For a practical implementation example, you can refer to this [code sample](https://github.com/WeAreNewt/config.fyi/blob/master/pages/api/aave.ts), which demonstrates how to use the Aave Utilities SDK in a demo NextJS application.

#### Historical Data

[](#integrations-historical-data)

If you're interested in historical data for parameters, rates, and balances, you can query contract events directly or use indexed data sources. A comprehensive breakdown of all core protocol events can be found in the documentation.

The Aave Protocol subgraphs are an example of an indexed data source that maps contract events to a GraphQL endpoint, allowing for efficient querying of historical data. For example, you can explore [queries of an address's transaction history](https://github.com/aave/protocol-subgraphs?tab=readme-ov-file#user-transaction-history) using these subgraphs.

#### Smart Contracts

[](#integrations-smart-contracts)

For detailed information on interacting with the protocol's smart contracts, please refer to the [Pool Methods](/docs/developers/smart-contracts/pool) documentation. Additionally, the [Testing & Debugging](/docs/developers/testing-and-debugging) guides offer valuable insights into developing and troubleshooting smart contract integrations.

[

Previous

**GHO**

](/docs/primitives/gho)[

Next

**Smart Contracts**

](/docs/developers/smart-contracts)

---

<a id="doc_13"></a>

## 📁 developers / Credit Delegation | Aave Protocol Documentation

*파일 경로: developers/credit_delegation.md*

Source: https://aave.com/docs/developers/credit-delegation

## Credit Delegation

[](#credit-delegation)

Credit delegation allows a supplier to contribute liquidity to the Aave protocol to earn interest, and delegate borrowing power (i.e. their credit) to other users. The enforcement of the borrow position and its terms are agreed upon between the supplier and borrowers, which can be either offchain via legal agreements or onchain via smart contracts.

This enables:

*   The supplier (aka delegator) to earn extra yield on top of the yield they already earn from the protocol.
    
*   The borrowers (aka delegatees) to access uncollateralized liquidity.
    

Borrow by *delegatee* must be consistent with *delegator* eMode category. For eg. if a delegator eMode category is STABLECOINS, then

*   Delegator can only borrow STABLECOINS eMode category asset.
    
*   In case *delegator* approve credit to *delegatee* for non STABLECOINScategory (for eg. weth), then borrow would revert.
    

The *delegatee* cannot abuse credit approval to liquidate *delegator* i.e. if the borrow puts *delegator's* position in HF < HEALTH\_FACTOR\_LIQUIDATION\_THRESHOLD, then borrow will fail.

### Approving the delegation

[](#approving-the-delegation)

The approveDelegation or delegationWithSig function on the [VariableDebtToken](/docs/developers/smart-contracts/tokenization#variabledebttoken) contract must be called by the supplier (delegator), approving the borrower (delegatee) a certain amount.

This is done for each debt token that needs to be delegated.

The delegator does not need to already have supplied funds in the protocol to approveDelegation. However, **before** the delegatee executes borrow, there must be sufficient collateral supplied by delegator in the protocol.

### Borrowing the credit

[](#borrowing-the-credit)

The borrower (delegatee) calls the borrow function on the [Pool](/docs/developers/smart-contracts/pool), using the supplier's (delegator's) address in final parameter onBehalfOf.

The borrower's available credit is reduced by the borrowed amount.

### Repaying the credit

[](#repaying-the-credit)

Anyone can repay the borrow position *OnBehalf* of the user, by calling one of the following [Pool](/docs/developers/smart-contracts/pool) functions - repay or repayWithPermit. The supplier (aka creditor) can also use the repayWithATokens function to repay a borrow position with their *aTokens* of the underlying asset in the same pool.

[

Previous

**Flash Loans**

](/docs/developers/flash-loans)[

Next

**Legacy Versions**

](/docs/developers/legacy-versions)

---

<a id="doc_14"></a>

## 📁 developers / Flash Loans | Aave Protocol Documentation

*파일 경로: developers/flash_loans.md*

Source: https://aave.com/docs/developers/flash-loans

## Flash Loans

[](#flash-loans)

Flash Loans are special transactions that allow the borrowing of an asset, as long as the borrowed amount (and a fee) is returned before the end of the transaction (also called One Block Borrows). These transactions do not require a user to supply collateral prior to engaging in the transaction. There is no real world analogy to Flash Loans, so it requires some basic understanding of how state is managed within blocks in blockchains.

Flash Loans are an advanced concept aimed at developers. You must have a good understanding of EVM, programming, and smart contracts to be able to use this feature.

### Overview

[](#overview)

Flash-loan allows users to access liquidity of the pool (only for reserves for which borrow is enabled) for one transaction as long as the amount taken plus fee is returned or (if allowed) debt position is opened by the end of the transaction.

Aave V3 offers two options for flash loans:

*   [flashLoan()](/docs/developers/smart-contracts/pool#flashloan): Allows borrower to access liquidity of ***multiple reserves*** in single *flashLoan* transaction. The borrower also has an option to open variable rate borrow position backed by supplied collateral or credit delegation in this case.  
    NOTE: *flash loan fee* is waived for approved flashBorrowers (managed by [ACLManager](/docs/developers/smart-contracts/acl-manager))
    
*   [flashLoanSimple()](/docs/developers/smart-contracts/pool#flashloansimple): Allows borrower to access liquidity of *single reserve* for the transaction. In this case flash loan fee is not waived nor can borrower open any debt position at the end of the transaction. This method is gas efficient for those trying take advantage of simple flash loan with single reserve asset.
    

#### Execution Flow

[](#overview-execution-flow)

For developers, a helpful mental model to consider when developing your solution:

1.  Your contract calls the [Pool](/docs/developers/smart-contracts/pool) contract, requesting a Flash Loan of a certain amount(s) of reserve(s) using [flashLoanSimple()](/docs/developers/smart-contracts/pool#flashloansimple) or [flashLoan()](/docs/developers/smart-contracts/pool#flashloan).
    
2.  After some sanity checks, the [Pool](/docs/developers/smart-contracts/pool) transfers the requested amounts of the reserves to your contract, then calls executeOperation() on receiver contract .
    
3.  Your contract, now holding the flash loaned amount(s), executes any arbitrary operation in its code.
    
    *   If you are performing a **flashLoanSimple**, then when your code has finished, you approve Pool for flash loaned amount + fee.
        
    *   If you are performing **flashLoan,** then for all the reserves either depending on interestRateMode passed for the asset, either the Pool must be approved for flash loaned amount + fee or must or sufficient collateral or credit delegation should be available to open debt position.
        
    *   If the amount owed is not available (due to a lack of balance or approval or insufficient collateral for debt), then the transaction is reverted.
        
    
4.  All of the above happens in 1 transaction (hence in a single ethereum block).
    

#### Applications of Flash Loans

[](#overview-applications-of-flash-loans)

Aave Flash Loans are already used with Aave V3 for liquidity switch feature. Other examples in the wild include:

*   Arbitrage between assets, without needing to have the principal amount to execute the arbitrage.
    
*   Liquidating borrow positions, without having to repay the debt of the positions and using discounted collateral claimed to payoff flashLoan amount + fee.
    

#### Flash loan fee

[](#overview-flash-loan-fee)

The flash loan fee is initialized at deployment to 0.05% and can be updated via Governance Vote. Use [FLASHLOAN\_PREMIUM\_TOTAL](/docs/developers/smart-contracts/pool#flashloan_premium_total) to get current value.

Flashloan fee can be shared by the LPs (liquidity providers) and the protocol treasury. The [FLASHLOAN\_PREMIUM\_TOTAL](/docs/developers/smart-contracts/pool#flashloan_premium_total) represents the total fee paid by the borrowers of which:

*   Fee to LP: [FLASHLOAN\_PREMIUM\_TOTAL](/docs/developers/smart-contracts/pool#flashloan_premium_total) - [FLASHLOAN\_PREMIUM\_TO\_PROTOCOL](/docs/developers/smart-contracts/pool#flashloan_premium_to_protocol)
    
*   Fee to Protocol: [FLASHLOAN\_PREMIUM\_TO\_PROTOCOL](/docs/developers/smart-contracts/pool#flashloan_premium_to_protocol)
    

At initialization, [FLASHLOAN\_PREMIUM\_TO\_PROTOCOL](/docs/developers/smart-contracts/pool#flashloan_premium_to_protocol) is set to 0.

### Step by step

[](#step-by-step)

#### 1\. Setting Up

[](#step-by-step-section-1-setting-up)

Your contract that receives the flash loaned amounts **must** conform to the [IFlashLoanSimpleReceiver](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/misc/flashloan/interfaces/IFlashLoanSimpleReceiver.sol) or [IFlashLoanReceiver](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/misc/flashloan/interfaces/IFlashLoanReceiver.sol) interface by implementing the relevant executeOperation() function.

Also note that since the owed amounts will be *pulled* from your contract, your contract must give allowance to the [Pool](/docs/developers/smart-contracts/pool) to pull those funds to pay back the flash loan amount + premiums.

#### 2\. Calling flashLoan() or flashLoanSimple()

[](#step-by-step-section-2-calling-flashloan-or-flashloansimple)

To call either of the two flash loan methods on the Pool, we need to pass in the relevant parameters. There are 3 ways you can do this.

1.  From an EOA ('normal' ethereum account)
    
    To use an EOA, send a transaction to the relevant [Pool](/docs/developers/smart-contracts/pool) calling the [flashLoan()](/docs/developers/smart-contracts/pool#flashloan) or [flashLoanSimple()](/docs/developers/smart-contracts/pool#flashloansimple) function. See the [Pool](/docs/developers/smart-contracts/pool) docs for parameter details, ensuring you use your contract address from [step 1](/docs/developers/flash-loans#1-setting-up) for the receiverAddress.
    
2.  From a different contract
    
    Similar to sending a transaction from an EOA as above, ensure the receiverAddress is your contract address from [step 1](/docs/developers/flash-loans#1-setting-up).
    
3.  From the *same* contract
    
    If you want to use the same contract as in step 1, use address(this) for the receiverAddress parameter in the flash loan method.
    

Never keep funds permanently on your [FlashLoanReceiverBase](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/flashloan/base/FlashLoanReceiverBase.sol) contract as they could be exposed to a ['griefing' attack](https://ethereum.stackexchange.com/a/92457/19365), where the stored funds are used by an attacker.

#### Completing the flash loan

[](#step-by-step-completing-the-flash-loan)

Once you have performed your logic with the flash loaned assets (in your executeOperation() function), you will need to pay back the flash loaned amounts if you used [flashLoanSimple()](/docs/developers/smart-contracts/pool#flashloansimple) or interestRateModes = 0 in [flashLoan()](/docs/developers/smart-contracts/pool#flashloan) for any of the assets in modes parameter.

*   #### Paying back a flash loaned asset
    
    [](#step-by-step-completing-the-flash-loan-paying-back-a-flash-loaned-asset)
    
    Ensure your contract has the relevant amount + premium to payback the borrowed asset. You can calculate this by taking the sum of the relevant entry in the amounts and premiums array passed into the executeOperation() function.
    
    You **do not** need to transfer the owed amount back to the [Pool](/docs/developers/smart-contracts/pool). The funds will be automatically *pulled* at the conclusion of your operation.
    
*   #### Incurring a debt (i.e. not immediately paying back)
    
    [](#step-by-step-completing-the-flash-loan-incurring-a-debt-ie-not-immediately-paying-back)
    
    If you initially used a mode=1 or mode=2 for any of the assets in the modes parameter, then the address passed in for onBehalfOf will incur the debt **if** the onBehalfOf address has previously approved the msg.sender to incur debts on their behalf.
    
    This means that you can have some assets that are paid back immediately, while other assets incur a debt.
    

[

Previous

**Safety Module**

](/docs/developers/safety-module)[

Next

**Credit Delegation**

](/docs/developers/credit-delegation)

---

<a id="doc_15"></a>

## 📁 developers / GHO | Aave Protocol Documentation

*파일 경로: developers/gho.md*

Source: https://aave.com/docs/developers/gho

## GHO

[](#gho)

Aave V3 MarketFlash MintGHO Stability ModuleCross-chain•••Aave GovernanceGHOOwnsFacilitators

GHO is an ERC-20 token deployed on Ethereum that operates through a facilitator model. Facilitators are contracts approved by Aave Governance with the ability to mint and burn GHO, each subject to a governance-defined mint cap. This model allows for flexibility in expanding GHO's functionality while maintaining decentralized control over the supply.

### Deployed Contracts

[](#deployed-contracts)

#### Ethereum Mainnet

[](#deployed-contracts-ethereum-mainnet)

Contract

Address

GhoToken

[0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f](https://etherscan.io/address/0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f)

GHOAToken (facilitator)

[0x00907f9921424583e7ffBfEdf84F92B7B2Be4977](https://etherscan.io/address/0x00907f9921424583e7ffBfEdf84F92B7B2Be4977)

GHOVariableDebtToken

[0x786dBff3f1292ae8F92ea68Cf93c30b34B1ed04B](https://etherscan.io/address/0x786dBff3f1292ae8F92ea68Cf93c30b34B1ed04B)

GhoOracle

[0xD110cac5d8682A3b045D5524a9903E031d70FCCd](https://etherscan.io/address/0xD110cac5d8682A3b045D5524a9903E031d70FCCd)

GhoInterestRateStrategy

[0x9ec6F08190DeA04A54f8Afc53Db96134e5E3FdFB](https://etherscan.io/address/0x9ec6F08190DeA04A54f8Afc53Db96134e5E3FdFB)

GhoDiscountRateStrategy

[0x4C38Ec4D1D2068540DfC11DFa4de41F733DDF812](https://etherscan.io/address/0x4C38Ec4D1D2068540DfC11DFa4de41F733DDF812)

GhoFlashMinter

[0xb639D208Bcf0589D54FaC24E655C79EC529762B8](https://etherscan.io/address/0xb639D208Bcf0589D54FaC24E655C79EC529762B8)

UiGhoDataProvider

[0x379c1EDD1A41218bdbFf960a9d5AD2818Bf61aE8](https://etherscan.io/address/0x379c1EDD1A41218bdbFf960a9d5AD2818Bf61aE8)

GSMRegistry

[0x167527DB01325408696326e3580cd8e55D99Dc1A](https://etherscan.io/address/0x167527DB01325408696326e3580cd8e55D99Dc1A)

GSMFixedFeeStrategy

[0xD4478A76aCeA81D3768A0ACB6e38f25eEB6Eb1B5](https://etherscan.io/address/0xD4478A76aCeA81D3768A0ACB6e38f25eEB6Eb1B5)

GSMUSDC

[0x0d8eFfC11dF3F229AA1EA0509BC9DFa632A13578](https://etherscan.io/address/0x0d8eFfC11dF3F229AA1EA0509BC9DFa632A13578)

GSMUSDT

[0x686F8D21520f4ecEc7ba577be08354F4d1EB8262](https://etherscan.io/address/0x686F8D21520f4ecEc7ba577be08354F4d1EB8262)

GSMUSDCFixedPriceStrategy

[0x430BEdcA5DfA6f94d1205Cb33AB4f008D0d9942a](https://etherscan.io/address/0x430BEdcA5DfA6f94d1205Cb33AB4f008D0d9942a)

GSMUSDTFixedPriceStrategy

[0x4c707764cbFB4FFa078e169e6b8A6AdbE7526a2c](https://etherscan.io/address/0x4c707764cbFB4FFa078e169e6b8A6AdbE7526a2c)

GSMUSDCOracleSwapFreezer

[0xef6beCa8D9543eC007bceA835aF768B58F730C1f](https://etherscan.io/address/0xef6beCa8D9543eC007bceA835aF768B58F730C1f)

GSMUSDTOracleSwapFreezer

[0x71381e6718b37C12155CB961Ca3D374A8BfFa0e5](https://etherscan.io/address/0x71381e6718b37C12155CB961Ca3D374A8BfFa0e5)

GHOCCIPTokenPoolEthereum

[0x5756880B6a1EAba0175227bf02a7E87c1e02B28C](https://etherscan.io/address/0x5756880B6a1EAba0175227bf02a7E87c1e02B28C)

#### Arbitrum

[](#deployed-contracts-arbitrum)

Contract

Address

GHOToken

[0x7dfF72693f6A4149b17e7C6314655f6A9F7c8B33](https://arbiscan.io/address/0x7dfF72693f6A4149b17e7C6314655f6A9F7c8B33)

GHOCCIPTokenPool

[0xB94Ab28c6869466a46a42abA834ca2B3cECCA5eB](https://arbiscan.io/address/0xB94Ab28c6869466a46a42abA834ca2B3cECCA5eB)

GHOAaveCoreSteward

[0xd2D586f849620ef042FE3aF52eAa10e9b78bf7De](https://arbiscan.io/address/0xd2D586f849620ef042FE3aF52eAa10e9b78bf7De)

GHOBucketSteward

[0xa9afaE6A53E90f9E4CE0717162DF5Bc3d9aBe7B2](https://arbiscan.io/address/0xa9afaE6A53E90f9E4CE0717162DF5Bc3d9aBe7B2)

GHOCCIPSteward

[0xCd5ab470AaC5c13e1063ee700503f3346b7C90Db](https://arbiscan.io/address/0xCd5ab470AaC5c13e1063ee700503f3346b7C90Db)

#### Base

[](#deployed-contracts-base)

Contract

Address

GHOToken

[0x6Bb7a212910682DCFdbd5BCBb3e28FB4E8da10Ee](https://basescan.org/address/0x6Bb7a212910682DCFdbd5BCBb3e28FB4E8da10Ee)

GHOCCIPTokenPool

[0x98217A06721Ebf727f2C8d9aD7718ec28b7aAe34](https://basescan.org/address/0x98217A06721Ebf727f2C8d9aD7718ec28b7aAe34)

GHOAaveCoreSteward

[0xC5BcC58BE6172769ca1a78B8A45752E3C5059c39](https://basescan.org/address/0xC5BcC58BE6172769ca1a78B8A45752E3C5059c39)

GHOBucketSteward

[0x3c47237479e7569653eF9beC4a7Cd2ee3F78b396](https://basescan.org/address/0x3c47237479e7569653eF9beC4a7Cd2ee3F78b396)

GHOCCIPSteward

[0xB94Ab28c6869466a46a42abA834ca2B3cECCA5eB](https://basescan.org/address/0xB94Ab28c6869466a46a42abA834ca2B3cECCA5eB)

#### Sepolia (Testnet)

[](#deployed-contracts-sepolia-testnet)

Contract

Address

GhoToken

[0xc4bF5CbDaBE595361438F8c6a187bDc330539c60](https://sepolia.etherscan.io/address/0xc4bF5CbDaBE595361438F8c6a187bDc330539c60)

GhoATokenImpl

[0xD4BDb51fB96996CA24a5C49E7b57f94a1850Fa30](https://sepolia.etherscan.io/address/0xD4BDb51fB96996CA24a5C49E7b57f94a1850Fa30)

GhoDiscountRateStrategy

[0x19cdecE64EDE475ba0EB114ff4E319d64Ef8ECCf](https://sepolia.etherscan.io/address/0x19cdecE64EDE475ba0EB114ff4E319d64Ef8ECCf)

GhoInterestRateStrategy

[0x521247B4d0a51E71DE580dA2cBF99EB40a44b3Bf](https://sepolia.etherscan.io/address/0x521247B4d0a51E71DE580dA2cBF99EB40a44b3Bf)

GhoOracle

[0x00f7fecFAEbEd9499e1f3f9d04E755a21E5fc47C](https://sepolia.etherscan.io/address/0x00f7fecFAEbEd9499e1f3f9d04E755a21E5fc47C)

GhoStableDebtTokenImpl

[0x2aa7819F2e88aF4cfF8FD0869ABdB97E336101Ee](https://sepolia.etherscan.io/address/0x2aa7819F2e88aF4cfF8FD0869ABdB97E336101Ee)

GhoVariableDebtTokenImpl

[0xd4FEA5bD40cE7d0f7b269678541fF0a95FCb4b68](https://sepolia.etherscan.io/address/0xd4FEA5bD40cE7d0f7b269678541fF0a95FCb4b68)

GhoFlashMinter

[0xB5d0ef1548D9C70d3E7a96cA67A2d7EbC5b1173E](https://sepolia.etherscan.io/address/0xB5d0ef1548D9C70d3E7a96cA67A2d7EbC5b1173E)

UiGhoDataProvider

[0x69B9843A16a6E9933125EBD97659BA3CCbE2Ef8A](https://sepolia.etherscan.io/address/0x69B9843A16a)

### GHO Token

[](#gho-token)

#### transfer

[](#gho-token-transfer)

The simplest method for transferring ERC-20 tokens is transfer which can be used to send tokens to any address without a prior token approval. The limitation of transfer is that it must be executed directly by the token holder, so it cannot be used within a smart contract function call to retrieve funds from a user (EOA).

#### transferFrom

[](#gho-token-transferfrom)

To transfer tokens within a smart contract function, transferFrom is the method that is used. The transferFrom function requires the sender to have approved the spender address for at least the transfer amount. There are two methods which can be used to perform the approval:

#### approve

[](#gho-token-approve)

The standard ERC-20 approve requires an on-chain transaction from the token holder to a approve a specified spender and amount.

#### permit

[](#gho-token-permit)

EIP-2612 permit is a type of token approval which requires two components:

*   A signed approval message from the token holder which encodes: owner, spender, amount, nonce, deadline, DOMAIN\_SEPARATOR
    
*   An on-chain permit transaction which can be executed from any address
    

The advantages to using permit in place of approve are that the gas cost of the transaction can be paid for by an address other than the token owner, and can reduce the number of transactions by batching the permit call with another action, an example of this is [supplyWithPermit](https://github.com/aave-dao/aave-v3-origin/blob/ec33f4fcc5546710c0faca5208af1775c761ac9c/src/contracts/protocol/pool/Pool.sol#L154) from Aave Protocol V3.

### Facilitators

[](#facilitators)

#### Aave V3 Ethereum Market

[](#facilitators-aave-v3-ethereum-market)

Interacting with GHO via the Aave Pool Facilitator is very similar to interacting with a typical Aave reserve asset with two key differences:

*   GHO is minted, not supplied, therefore interest rate and available liquidity calculations are based on custom interest rate strategy and facilitator caps respectively
    
*   GHO has a discounted borrow rate for stkAAVE holders
    

Below are the technical guides for all GHO actions along with their contract references.

##### Minting

[](#facilitators-aave-v3-ethereum-market-minting)

Minting occurs through the borrow function of the Aave V3 Ethereum market. To mint GHO, the process is nearly identical to borrowing any other reserve. To mint, an address must have sufficient collateral which is performed by approving and then calling supply on the Aave Pool with an eligible collateral asset. Once an address has sufficient collateral, it is able to borrow up to a maximum collateral factor determined by its collateral asset composition.

Since GHO is created and not borrowed from suppliers, GHO is not subject to restrictions on available liquidity, and instead, the Facilitator cap and collateralization requirements define the limits to which GHO can be minted as calculated below.

availableFacilitatorCap = ghoReserveData.aaveFacilitatorButcketMaxCapacity - ghoReserveData.aaveFacilitatorBucketLevel

See [core functions](/docs/developers/smart-contracts/pool) for more information on integrating Aave borrow functionality.

##### Repay

[](#facilitators-aave-v3-ethereum-market-repay)

GHO is repaid just like any other asset, by approving the Pool contract to spend GHO tokens (by approval transaction or signed permit and repayWithPermit).

What is different about GHO is the calculation of accrued interest. See the discount dynamics section for more info on how accrued interest affects balances for repayment.

See [core functions](/docs/developers/smart-contracts/pool) for more information on integrating Aave repay functionality.

#### Liquidation

[](#facilitators-liquidation)

When an address has a GHO borrow position, they are eligible to be liquidated under the same conditions as any other collateralized address. If the health factor of a GHO borrow falls below one, which occurs when the sum of borrow value exceeds the weighted average of liquidation thresholds of collateral assets, then any address is eligible to make a liquidationCall on the Pool contract.

The liquidationCall repays up to 100% of the GHO borrow position in exchange for an equivalent USD valuation of the collateral plus a liquidation bonus.

See the developers [liquidation guide](/docs/developers/liquidations) for more information.

#### Flash Mint

[](#facilitators-flash-mint)

Since GHO is not borrowed like a typical Aave reserve, a separate Facilitator is used in place to replicate the flashloan functionality of the Aave Pool.

The FlashMinter Facilitator has a separate minting cap from the Aave Pool. Since all FlashMint transactions are returned in a single transaction, no GHO is ever minted against this Facilitator and the cap is applied to each transaction.

FlashMint is useful for a variety of applications such as liquidations, debt switches, and peg arbitrage. The GhoFlashMinter smart contract implements the following functions:

```
function maxFlashLoan(address token) external view override returns (uint256)
```

```
function getFee() external view override returns (uint256)
```

```
function flashLoan(    IERC3156FlashBorrower receiver,    address token,    uint256 amount,    bytes calldata data) external override returns (bool)
```

See the developers [flash loan guide](/docs/developers/flash-loans) for more information on developing flash loan integrations.

#### Stability Module

[](#facilitators-stability-module)

A Peg Stability Module (PSM) is a contract that enables the conversion of two tokens at a predetermined ratio. The GHO Stability Module (GSM) leverages the benefits of existing PSM models while innovating upon them in several ways to help further maintain GHO’s peg. The GSM is designed to facilitate conversions between GHO and governance-approved tokens, underpinned by a suite of features designed for flexible operations and risk management.

##### GSMRegistry

[](#facilitators-stability-module-gsmregistry)

The GSMRegistry is a smart contract that stores a list of all GSM instances. This contract is owned by the Aave Governance Short Executor.

##### GSM

[](#facilitators-stability-module-gsm)

Each token pairing in the stability module has a GSM or GSM4626 contract instance that acts as the GHO facilitator and entry-point for buy and sell functionality.

The GSM4626 contract is a special instance of the GSM that supports ERC-4626 tokenized vault shares as the exogenous token.

The parameters and periphery contracts that dictate module operations are detailed below:

##### Price Strategy

[](#facilitators-stability-module-price-strategy)

The GSM introduces a flexible Price Strategy framework, enabling the module to adapt its pricing mechanism based on market conditions or strategic objectives. This system supports both fixed and dynamic pricing strategies, allowing for adjustments in response to real-time market data or predetermined conditions. The initial implementation focuses on a fixed 1:1 pricing strategy for simplicity and stability, with provisions for future adaptation to dynamic strategies as dictated by DAO governance.

##### Fee Strategy

[](#facilitators-stability-module-fee-strategy)

Each GSM instance has a FeeStrategy contract that determines a percentage fee for buy and sell conversions that is allocated to the Aave DAO treasury.

##### Exposure Cap

[](#facilitators-stability-module-exposure-cap)

The exposure cap is a parameter determined by Aave DAO Governance that sets the maximum amount of an exogenous token the stability module can hold.

##### Conversion Freezes and Oracle Price Bounds

[](#facilitators-stability-module-conversion-freezes-and-oracle-price-bounds)

In case the price of the exogenous token deviates from a determined ratio, the freeze role can be utilized by the Aave DAO or assigned to an entity (autonomous agents or contracts) to respond and halt conversions.

An implementation of the freeze role is the OracleSwapFreezer contract. This contract utilizes Chainlink oracles and price bounds determined by Aave Governence to freeze/unfreeze based on oracle conditions.

##### Last Resort Liquidations

[](#facilitators-stability-module-last-resort-liquidations)

In case of a rapid increase in risk in an exogenous token, the GSM features Last Resort Liquidations to liquidate the exogenous token. This contract role allows in the worst-case scenarios for the DAO to pause GSM functionality and liquidate the underlying balance of exogenous tokens.

#### Cross-Chain

[](#facilitators-cross-chain)

All GHO tokens are originated on Ethereum mainnet. GHO is made available to access on other networks using an infrastructure of cross-chain messaging.

The Chainlink CCIP protocol has been approved by Aave Governance as the messaging bridge to facilitate the transfer of GHO between networks.

GHO is transferred by between networks by initiating a lock (Ethereum mainnet) or burn (other networks) action on the source network, and a release (Ethereum mainnet) or mint (other networks) action occurs on the destination chain after the cross-chain message has been validated.

The GHOCCIPTokenPoolEthereum contract facilitates the locking and burning of GHO on Ethereum and other chains, enabling GHO's presence across multiple DeFi ecosystems.

**CCIP Subgraph**: Track GHO's cross-chain activity through subgraphs for Ethereum and Arbitrum:

*   [CCIP Ethereum Subgraph](https://thegraph.com/explorer/subgraphs/E11p8T4Ff1DHZbwSUC527hkUb5innVMdTuP6A2s1xtm1?view=Query&chain=arbitrum-one)
    
*   [CCIP Arbitrum Subgraph](https://thegraph.com/explorer/subgraphs/GPpZfiGoDChLsiWoMG5fxXdRNEYrsVDrKJ39moGcbz6i?view=Query&chain=arbitrum-one)
    

See the [Aave Labs interface bridging integration](https://github.com/aave/interface/tree/main/src/components/transactions/Bridge) as a reference for token bridging.

[

Previous

**Switch Adapters**

](/docs/developers/smart-contracts/switch-adapters)[

Next

**Governance**

](/docs/developers/governance)

---

<a id="doc_16"></a>

## 📁 developers / Governance | Aave Protocol Documentation

*파일 경로: developers/governance.md*

Source: https://aave.com/docs/developers/governance

## Governance

[](#governance)

The Aave Protocol is governed by the AAVE token holder community through procedures, voting, and smart contract execution, collectively known as **Aave Governance**.

All instances of the Aave Protocol are governed by the AAVE, stkAAVE, and aAAVE token holders on **Ethereum mainnet**. [Aave Governance V3](https://github.com/bgd-labs/aave-governance-v3), developed by [BGD Labs](https://bgdlabs.com/), introduces the ability to vote on lower transaction fee networks such as Polygon POS and Avalanche C-Chain while token balances remain on Ethereum mainnet.

### Architecture

[](#architecture)

Aave Governance V3 is designed with a modular architecture to meet the comprehensive needs of an on-chain DAO like Aave. The system is divided into three main components, each corresponding to different stages in the proposal lifecycle:

*   **Core Network**: Acts as the settlement and security layer where voting power resides. It handles high-level validations on proposals and manages governance token balances. Ethereum Mainnet serves as the Core Network.
    
*   **Voting Networks**: Environments where voting occurs based on storage proofs. These networks are typically lower-cost environments like Polygon POS and Avalanche C-Chain, enabling users to vote without migrating funds from the Core Network.
    
*   **Execution Networks**: Networks where proposal payloads are registered and executed. They handle the execution of approved proposals across various networks, including all Voting Networks and the Core Network.
    

Communication between these components is facilitated by the [Aave Delivery Infrastructure](https://governance.aave.com/t/bgd-a-di-aave-delivery-infrastructure/13951) (a.DI), providing secure and efficient cross-chain interactions. Additionally, the [Aave Robot](https://governance.aave.com/t/bgd-aave-robot-v1/13091) automates permissionless actions in Aave Governance such as queueing and executing proposals.

### Voting

[](#voting)

In Governance V3, each proposal specifies a voting network and all voting for the proposal occurs on this network. The Governance V3 activation enables Polygon POS, Avalanche C-Chain, and Ethereum Mainnet (backup) as initial voting networks.

Voters do not need to migrate funds to the voting network, all governance token balances and delegations are still stored on Ethereum mainnet, and are validated on the voting network using storage proofs.

Voting is performing by calling the submitVote() function on the VotingMachine of the corresponding proposal’s voting network.

An [aave-cli](https://github.com/bgd-labs/aave-cli/blob/main/README.md) has been developed to generate the necessary storage proof parameters, or voting can performed with the [GovernanceV3Helpers](https://github.com/bgd-labs/aave-helpers?tab=readme-ov-file#govv3helpers) Foundry script.

#### Voting Power

[](#voting-voting-power)

AAVE, stkAAVE (AAVE staked in protocol safety module), and aAAVE (aToken representing AAVE supplied to Ethereum V3 market) token holders receive governance powers proportional to the sum of their balances on Ethereum mainnet.

There are two powers associated with each governance token:

*   The **proposal power** that gives access to creating a proposal.
    
*   The **voting power** which is used to vote for or against active proposals.
    

Governance powers can be either jointly or separately delegated to any Ethereum address.

#### Voting Representatives

[](#voting-voting-representatives)

Smart contract wallets cannot sign messages for storage proof voting and may not exist on all networks, this creates a challenge to interact with the cross-chain voting contracts.

To accommodate cross-chain voting for smart contract wallets and allow greater flexibility for all governance participants, wallets have the ability to link a representative address on other chains.

To choose a representative, an address in Ethereum should call the updateRepresentativesPerChain() function on the GovernanceCore smart contract.

This representative address is able to vote on the specified network, using the delegators balances and received delegations on Ethereum Mainnet. An address can be the representative of multiple other addresses.

#### Storage Proofs

[](#voting-storage-proofs)

Aave Governance V3 uses block hashes on the Core network (Ethereum Mainnet) as the source of information for voting balances, and storage proofs as the core mechanism for validation.

For any proposal, the system takes a “snapshot” (block hash of the block before activateVote method gets called) of voting token balances/delegations on the Core network, forwards it to an Aave Voting Network and sets it as the main source of balances/delegation to validate against whenever an address submits a vote there.

Ethereum block hashes contain the state tree of the network, which in turn contains all the data of all the smart contracts at that exact block. Amongst those contracts: AAVE, stkAAVE, and other voting assets are present, and within them, the balances and delegations of all Ethereum addresses.

Storage proofs are a mechanism allowing to cryptographically prove that a piece of data is contained in a tree. In this case, they allow proving that a specific address has voting balance/delegation on the state tree of an Ethereum block.

What happens in practice when an address votes is that the voter inputs the balance of the voting assets they hold at the proposal's Ethereum block, together with a storage proof over the Ethereum block hash for that proposal. The Voting Network then cryptographically verifies the storage proof against the Ethereum block data, along with all additional validations (e.g., no double-voting), and stores the results accordingly.

### Proposal Lifecycle

[](#proposal-lifecycle)

1.  **Payload Registration**: Proposal payloads containing executable logic are deployed and registered on the PayloadsController of the target Execution Network. This process is permissionless.
    
2.  **Proposal Creation**: A proposer with sufficient proposal power creates the proposal on the Core Network (Ethereum Mainnet) by interacting with the Governance contract. The proposer specifies the payload IDs and target networks.
    
3.  **Proposal Activation**: After a cooldown period (coolDownBeforeVotingStart), the proposal is activated. This involves taking a snapshot of the Core Network's state and forwarding it to the specified Voting Network using a.DI.
    
4.  **Voting Setup**: On the Voting Network, the necessary data (Ethereum block hash, state tree, voting asset roots) is settled in the DataWarehouse contract. This step is permissionless and can be performed by any address.
    
5.  **Voting Period**: Voting occurs on the Voting Network. Voters submit their votes by calling submitVote() on the VotingMachine, providing their token balances at the snapshot block along with storage proofs.
    
6.  **Vote Closure**: After the voting duration (votingDuration) elapses, voting is closed. The VotingMachine contract sends the voting results (YES and NO counts) back to the Core Network via a.DI.
    
7.  **Result Validation**: The Governance contract on the Core Network validates the voting results against success metrics, such as minimum thresholds and vote differentials.
    
8.  **Proposal Queuing**: If the proposal meets the success criteria, it is forwarded to the PayloadsController on the Execution Network, where it is queued in a timelock mechanism.
    
9.  **Proposal Execution**: After the timelock expires, any address can execute the proposal by calling executePayload() on the PayloadsController, which forwards it to the appropriate Executor for execution.
    

### Deployed Contracts

[](#deployed-contracts)

#### Ethereum

[](#deployed-contracts-ethereum)

Name

Address

CrossChainController

[0xEd42a7D8559a463722Ca4beD50E0Cc05a386b0e1](https://etherscan.io/address/0xEd42a7D8559a463722Ca4beD50E0Cc05a386b0e1)

Governance

[0x9AEE0B04504CeF83A65AC3f0e838D0593BCb2BC7](https://etherscan.io/address/0x9AEE0B04504CeF83A65AC3f0e838D0593BCb2BC7)

PayloadsController

[0xdAbad81aF85554E9ae636395611C58F7eC1aAEc5](https://etherscan.io/address/0xdAbad81aF85554E9ae636395611C58F7eC1aAEc5)

VotingMachine

[0x617332a777780F546261247F621051d0b98975Eb](https://etherscan.io/address/0x617332a777780F546261247F621051d0b98975Eb)

VotingPortalEthEth

[0xf23f7De3AC42F22eBDA17e64DC4f51FB66b8E21f](https://etherscan.io/address/0xf23f7De3AC42F22eBDA17e64DC4f51FB66b8E21f)

VotingPortalEthAvax

[0x33aCEf7365809218485873B7d0d67FeE411B5D79](https://etherscan.io/address/0x33aCEf7365809218485873B7d0d67FeE411B5D79)

VotingPortalEthPol

[0x9b24C168d6A76b5459B1d47071a54962a4df36c3](https://etherscan.io/address/0x9b24C168d6A76b5459B1d47071a54962a4df36c3)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://etherscan.io/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

GovernanceDataHelper

[0x971c82c8316aD611904F95616c21ce90837f1856](https://etherscan.io/address/0x971c82c8316aD611904F95616c21ce90837f1856)

VotingDataHelper

[0x77976B51569896523EE215962Ee91ff236Fa50E8](https://etherscan.io/address/0x77976B51569896523EE215962Ee91ff236Fa50E8)

MetaDelegateHelper

[0x94363B11b37BC3ffe43AB09cff5A010352FE85dC](https://etherscan.io/address/0x94363B11b37BC3ffe43AB09cff5A010352FE85dC)

EmergencyRegistry

[0x73C6Fb358dDA8e84D50e98A98F7c0dF32e15C7e9](https://etherscan.io/address/0x73C6Fb358dDA8e84D50e98A98F7c0dF32e15C7e9)

GovernancePowerStrategy

[0xa198Fac58E02A5C5F8F7e877895d50cFa9ad1E04](https://etherscan.io/address/0xa198Fac58E02A5C5F8F7e877895d50cFa9ad1E04)

GranularGuardian

[0x4457cA11E90f416Cc1D3a8E1cA41C0cdEcC251d4](https://etherscan.io/address/0x4457cA11E90f416Cc1D3a8E1cA41C0cdEcC251d4)

ExecutorLvl1

[0x5300A1a15135EA4dc7aD5a167152C01EFc9b192A](https://etherscan.io/address/0x5300A1a15135EA4dc7aD5a167152C01EFc9b192A)

ExecutorLvl2

[0x17Dd33Ed0e3dD2a80E37489B8A63063161BE6957](https://etherscan.io/address/0x17Dd33Ed0e3dD2a80E37489B8A63063161BE6957)

VotingStrategy

[0x5642A5A5Ec284B4145563aBF319620204aCCA7f4](https://etherscan.io/address/0x5642A5A5Ec284B4145563aBF319620204aCCA7f4)

DataWarehouse

[0x1699FE9CaDC8a0b6c93E06B62Ab4592a0fFEcF61](https://etherscan.io/address/0x1699FE9CaDC8a0b6c93E06B62Ab4592a0fFEcF61)

#### Arbitrum

[](#deployed-contracts-arbitrum)

Name

Address

CrossChainController

[0xCbFB78a3Eeaa611b826E37c80E4126c8787D29f0](https://arbiscan.io/address/0xCbFB78a3Eeaa611b826E37c80E4126c8787D29f0)

PayloadsController

[0x89644CA1bB8064760312AE4F03ea41b05dA3637C](https://arbiscan.io/address/0x89644CA1bB8064760312AE4F03ea41b05dA3637C)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://arbiscan.io/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

GranularGuardian

[0x4922093c476CfbCF903C7C4082d2D64bAE8A37cE](https://arbiscan.io/address/0x4922093c476CfbCF903C7C4082d2D64bAE8A37cE)

ExecutorLvl1

[0xFF1137243698CaA18EE364Cc966CF0e02A4e6327](https://arbiscan.io/address/0xFF1137243698CaA18EE364Cc966CF0e02A4e6327)

#### Avalanche

[](#deployed-contracts-avalanche)

Name

Address

CrossChainController

[0x27FC7D54C893dA63C0AE6d57e1B2B13A70690928](https://snowtrace.io/address/0x27FC7D54C893dA63C0AE6d57e1B2B13A70690928)

EmergencyOracle

[0x41185495Bc8297a65DC46f94001DC7233775EbEe](https://snowtrace.io/address/0x41185495Bc8297a65DC46f94001DC7233775EbEe)

VotingMachine

[0x9b6f5ef589A3DD08670Dd146C11C4Fb33E04494F](https://snowtrace.io/address/0x9b6f5ef589A3DD08670Dd146C11C4Fb33E04494F)

PayloadsController

[0x1140CB7CAfAcC745771C2Ea31e7B5C653c5d0B80](https://snowtrace.io/address/0x1140CB7CAfAcC745771C2Ea31e7B5C653c5d0B80)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://snowtrace.io/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

VotngDataHelper

[0x77976B51569896523EE215962Ee91ff236Fa50E8](https://snowtrace.io/address/0x77976B51569896523EE215962Ee91ff236Fa50E8)

GranularGuardian

[0xc1162BCb2E5E3ca4725512008c7522dF8C8B7B65](https://snowtrace.io/address/0xc1162BCb2E5E3ca4725512008c7522dF8C8B7B65)

ExecutorLvl1

[0x3C06dce358add17aAf230f2234bCCC4afd50d090](https://snowtrace.io/address/0x3C06dce358add17aAf230f2234bCCC4afd50d090)

VotingStrategy

[0x690C218668B440204F369Af1541245d367cc805C](https://snowtrace.io/address/0x690C218668B440204F369Af1541245d367cc805C)

DataWarehouse

[0x9626F9d60CC0B7e1c9a0A47b7f0bd618fb6f40ff](https://snowtrace.io/address/0x9626F9d60CC0B7e1c9a0A47b7f0bd618fb6f40ff)

#### BNB

[](#deployed-contracts-bnb)

Name

Address

CrossChainController

[0x9d33ee6543C9b2C8c183b8fb58fB089266cffA19](https://bscscan.com/address/0x9d33ee6543C9b2C8c183b8fb58fB089266cffA19)

EmergencyOracle

[0xcabb46FfB38c93348Df16558DF156e9f68F9F7F1](https://bscscan.com/address/0xcabb46FfB38c93348Df16558DF156e9f68F9F7F1)

PayloadsController

[0xE5EF2Dd06755A97e975f7E282f828224F2C3e627](https://bscscan.com/address/0xE5EF2Dd06755A97e975f7E282f828224F2C3e627)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://bscscan.com/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

GranularGuardian

[0xe4FB5e3F506BE0095f38004f993D16fdA8224383](https://bscscan.com/address/0xe4FB5e3F506BE0095f38004f993D16fdA8224383)

ExecutorLvl1

[0x9390B1735def18560c509E2d0bc090E9d6BA257a](https://bscscan.com/address/0x9390B1735def18560c509E2d0bc090E9d6BA257a)

#### Base

[](#deployed-contracts-base)

Name

Address

CrossChainController

[0x529467C76f234F2bD359d7ecF7c660A2846b04e2](https://basescan.org/address/0x529467C76f234F2bD359d7ecF7c660A2846b04e2)

PayloadsController

[0x2DC219E716793fb4b21548C0f009Ba3Af753ab01](https://basescan.org/address/0x2DC219E716793fb4b21548C0f009Ba3Af753ab01)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://basescan.org/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

GranularGuardian

[0xa1c6aF35E0205f42256382C05243C543FEDBf4bB](https://basescan.org/address/0xa1c6aF35E0205f42256382C05243C543FEDBf4bB)

ExecutorLvl1

[0x9390B1735def18560c509E2d0bc090E9d6BA257a](https://basescan.org/address/0x9390B1735def18560c509E2d0bc090E9d6BA257a)

#### Binance

[](#deployed-contracts-binance)

Name

Address

CrossChainController

[0x9d33ee6543C9b2C8c183b8fb58fB089266cffA19](https://bscscan.com/address/0x9d33ee6543C9b2C8c183b8fb58fB089266cffA19)

EmergencyOracle

[0xcabb46FfB38c93348Df16558DF156e9f68F9F7F1](https://bscscan.com/address/0xcabb46FfB38c93348Df16558DF156e9f68F9F7F1)

PayloadsController

[0xE5EF2Dd06755A97e975f7E282f828224F2C3e627](https://bscscan.com/address/0xE5EF2Dd06755A97e975f7E282f828224F2C3e627)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://bscscan.com/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

ExecutorLvl1

[0x9390B1735def18560c509E2d0bc090E9d6BA257a](https://bscscan.com/address/0x9390B1735def18560c509E2d0bc090E9d6BA257a)

#### Gnosis

[](#deployed-contracts-gnosis)

Name

Address

CrossChainController

[0x8Dc5310fc9D3D7D1Bb3D1F686899c8F082316c9F](https://gnosisscan.io/address/0x8Dc5310fc9D3D7D1Bb3D1F686899c8F082316c9F)

EmergencyOracle

[0xF937ffAeA1363e4Fa260760bDFA2aA8Fc911F84D](https://gnosisscan.io/address/0xF937ffAeA1363e4Fa260760bDFA2aA8Fc911F84D)

PayloadsController

[0x9A1F491B86D09fC1484b5fab10041B189B60756b](https://gnosisscan.io/address/0x9A1F491B86D09fC1484b5fab10041B189B60756b)

PayloadDataHelper

[0xF1c11BE0b4466728DDb7991A0Ac5265646ec9672](https://gnosisscan.io/address/0xF1c11BE0b4466728DDb7991A0Ac5265646ec9672)

GranularGuardian

[0x4A9F571E3C1f2F13567bb59e38988e74d7d72602](https://gnosisscan.io/address/0x4A9F571E3C1f2F13567bb59e38988e74d7d72602)

ExecutorLvl1

[0x1dF462e2712496373A347f8ad10802a5E95f053D](https://gnosisscan.io/address/0x1dF462e2712496373A347f8ad10802a5E95f053D)

#### Metis

[](#deployed-contracts-metis)

Name

Address

CrossChainController

[0x6fDaFb26915ABD6065a1E1501a37Ac438D877f70](https://explorer.metis.io/address/0x6fDaFb26915ABD6065a1E1501a37Ac438D877f70)

PayloadsController

[0x2233F8A66A728FBa6E1dC95570B25360D07D5524](https://explorer.metis.io/address/0x2233F8A66A728FBa6E1dC95570B25360D07D5524)

PayloadDataHelper

[0x81d32B36380e6266e1BDd490eAC56cdB300afBe0](https://explorer.metis.io/address/0x81d32B36380e6266e1BDd490eAC56cdB300afBe0)

GranularGuardian

[0x61BE97d3a0550549f67CA7421725fA73Fa2036B5](https://explorer.metis.io/address/0x61BE97d3a0550549f67CA7421725fA73Fa2036B5)

ExecutorLvl1

[0x6fD45D32375d5aDB8D76275A3932c740F03a8718](https://explorer.metis.io/address/0x6fD45D32375d5aDB8D76275A3932c740F03a8718)

#### Optimism

[](#deployed-contracts-optimism)

Name

Address

CrossChainController

[0x48A9FE90bce5EEd790f3F4Ce192d1C0B351fd4Ca](https://optimistic.etherscan.io/address/0x48A9FE90bce5EEd790f3F4Ce192d1C0B351fd4Ca)

PayloadsController

[0x0E1a3Af1f9cC76A62eD31eDedca291E63632e7c4](https://optimistic.etherscan.io/address/0x0E1a3Af1f9cC76A62eD31eDedca291E63632e7c4)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://optimistic.etherscan.io/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

GranularGuardian

[0x6c5264C380C7022e54f585c4E354ffb6f221a03b](https://optimistic.etherscan.io/address/0x6c5264C380C7022e54f585c4E354ffb6f221a03b)

ExecutorLvl1

[0x746c675dAB49Bcd5BB9Dc85161f2d7Eb435009bf](https://optimistic.etherscan.io/address/0x746c675dAB49Bcd5BB9Dc85161f2d7Eb435009bf)

#### Polygon

[](#deployed-contracts-polygon)

Name

Address

CrossChainController

[0xF6B99959F0b5e79E1CC7062E12aF632CEb18eF0d](https://polygonscan.com/address/0xF6B99959F0b5e79E1CC7062E12aF632CEb18eF0d)

EmergencyOracle

[0xDAFA1989A504c48Ee20a582f2891eeB25E2fA23F](https://polygonscan.com/address/0xDAFA1989A504c48Ee20a582f2891eeB25E2fA23F)

VotingMachine

[0xc8a2ADC4261c6b669CdFf69E717E77C9cFeB420d](https://polygonscan.com/address/0xc8a2ADC4261c6b669CdFf69E717E77C9cFeB420d)

PayloadsController

[0x401B5D0294E23637c18fcc38b1Bca814CDa2637C](https://polygonscan.com/address/0x401B5D0294E23637c18fcc38b1Bca814CDa2637C)

PayloadDataHelper

[0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A](https://polygonscan.com/address/0xE3B770Dc4ae3f8bECaB3Ed12dE692c741603e16A)

VotingDataHelper

[0x77976B51569896523EE215962Ee91ff236Fa50E8](https://polygonscan.com/address/0x77976B51569896523EE215962Ee91ff236Fa50E8)

GranularGuardian

[0x0D2CccD3dD420dC6DE2f24DB44aA22fADE290a02](https://polygonscan.com/address/0x0D2CccD3dD420dC6DE2f24DB44aA22fADE290a02)

ExecutorLvl1

[0xDf7d0e6454DB638881302729F5ba99936EaAB233](https://polygonscan.com/address/0xDf7d0e6454DB638881302729F5ba99936EaAB233)

VotingStrategy

[0x59e6CAD5d7E7b9A26a45a1d1E74C7aF008170042](https://polygonscan.com/address/0x59e6CAD5d7E7b9A26a45a1d1E74C7aF008170042)

DataWarehouse

[0xf41193E25408F652AF878c47E4401A01B5E4B682](https://polygonscan.com/address/0xf41193E25408F652AF878c47E4401A01B5E4B682)

#### Scroll

[](#deployed-contracts-scroll)

Name

Address

CrossChainController

[0x03073D3F4769f6b6604d616238fD6c636C99AD0A](https://scrollscan.com/address/0x03073D3F4769f6b6604d616238fD6c636C99AD0A)

PayloadsController

[0x6b6B41c0f8C223715f712BE83ceC3c37bbfDC3fE](https://scrollscan.com/address/0x6b6B41c0f8C223715f712BE83ceC3c37bbfDC3fE)

PayloadDataHelper

[0xf438e33dCCEE260ee4371F9dceF408b0d7DBe424](https://scrollscan.com/address/0xf438e33dCCEE260ee4371F9dceF408b0d7DBe424)

GranularGuardian

[0xa835707d28e6C37C49d661742f2Fb5987367cEd4](https://scrollscan.com/address/0xa835707d28e6C37C49d661742f2Fb5987367cEd4)

ExecutorLvl1

[0xc1ABF87FfAdf4908f4eC8dc54A25DCFEabAE4A24](https://scrollscan.com/address/0xc1ABF87FfAdf4908f4eC8dc54A25DCFEabAE4A24)

#### ZkSync

[](#deployed-contracts-zksync)

Name

Address

CrossChainController

[0x800813f4714BC7A0a95310e3fB9e4f18872CA92C](https://era.zksync.network/address/0x800813f4714BC7A0a95310e3fB9e4f18872CA92C)

PayloadsController

[0x2E79349c3F5e4751E87b966812C9E65E805996F1](https://era.zksync.network/address/0x2E79349c3F5e4751E87b966812C9E65E805996F1)

PayloadDataHelper

[0xe28A3235DCF1Acb8397B546bd588bAAFD7081505](https://era.zksync.network/address/0xe28A3235DCF1Acb8397B546bd588bAAFD7081505)

GranularGuardian

[0xe0e23196D42b54F262a3DE952e6B34B197D1A228](https://era.zksync.network/address/0xe0e23196D42b54F262a3DE952e6B34B197D1A228)

GovernanceGuardian

[0x4257bf0746D783f0D962913d7d8AFA408B62547E](https://era.zksync.network/address/0x4257bf0746D783f0D962913d7d8AFA408B62547E)

ExecutorLvl1

[0x04cE39789e11a49595cD0ECEf6f4Bd54ABF4d020](https://era.zksync.network/address/0x04cE39789e11a49595cD0ECEf6f4Bd54ABF4d020)

#### Linea

[](#deployed-contracts-linea)

Name

Address

CrossChainController

[0x0D3f821e9741C8a8Bcac231162320251Db0cdf52](https://lineascan.build/address/0x0D3f821e9741C8a8Bcac231162320251Db0cdf52)

PayloadsController

[0x3BcE23a1363728091bc57A58a226CF2940C2e074](https://lineascan.build/address/0x3BcE23a1363728091bc57A58a226CF2940C2e074)

PayloadDataHelper

[0x6d4F341d8Bb3Dc5ABe822Aa940F1884508C13f99](https://lineascan.build/address/0x6d4F341d8Bb3Dc5ABe822Aa940F1884508C13f99)

GranularGuardian

[0xc1cd6faF6e9138b4e6C21d438f9ebF2bd6F6cA16](https://lineascan.build/address/0xc1cd6faF6e9138b4e6C21d438f9ebF2bd6F6cA16)

GovernanceGuardian

[0x056E4C4E80D1D14a637ccbD0412CDAAEc5B51F4E](https://lineascan.build/address/0x056E4C4E80D1D14a637ccbD0412CDAAEc5B51F4E)

ExecutorLvl1

[0x8c2d95FE7aeB57b86961F3abB296A54f0ADb7F88](https://lineascan.build/address/0x8c2d95FE7aeB57b86961F3abB296A54f0ADb7F88)

[

Previous

**GHO**

](/docs/developers/gho)[

Next

**Safety Module**

](/docs/developers/safety-module)

---

<a id="doc_17"></a>

## 📁 developers / Legacy Versions | Aave Protocol Documentation

*파일 경로: developers/legacy_versions.md*

Source: https://aave.com/docs/developers/legacy-versions

## Legacy Protocol Versions

[](#legacy-protocol-versions)

Aave has undergone multiple iterations to optimize the functionality, gas efficiency, and modularity of the contract codebase. The following guides provide references and explain architectural changes for legacy protocol versions:

[

Aave V1

Documentation for Aave V1.



](/docs/developers/legacy-versions/v1)

[

Aave V2

Documentation for Aave V2.



](/docs/developers/legacy-versions/v2)

[

Previous

**Credit Delegation**

](/docs/developers/credit-delegation)[

Next

**V1**

](/docs/developers/legacy-versions/v1)

---

<a id="doc_18"></a>

## 📁 developers / Safety Module | Aave Protocol Documentation

*파일 경로: developers/safety_module.md*

Source: https://aave.com/docs/developers/safety-module

## Safety Module

[](#safety-module)

The Aave Safety Module serves as a safeguard for the Aave Protocol against potential shortfall events. By staking AAVE, GHO, or AAVE / wstETH Balancer Pool tokens, participants contribute to the security of the protocol and earn incentives in return. The staked tokens may be slashed in the event of a shortfall to cover any protocol deficits.

The Safety Module operates by allowing users to stake their ERC-20 tokens into StakeToken contracts, which are also ERC-20 tokens. These StakeToken contracts handle the distribution of rewards and manage the slashing mechanism. The implementation details of the StakeToken contracts are available on [GitHub](https://github.com/bgd-labs/aave-stk-gov-v3).

The [Umbrella](https://governance.aave.com/t/bgd-aave-safety-module-umbrella/18366) governance proposal outlines potential changes to the Safety Module, including automated slashing, replacing stkAAVE and stkABPT with aToken staking, and new incentives design, subject to community approval.

### Staking

[](#staking)

Users stake tokens by calling the stake function on the StakeToken contract with the amount they wish to stake. In exchange, they receive staked tokens adjusted by the current exchange rate, representing their share in the Safety Module.

```
function stake(address to, uint256 amount) external;
```

### Unstaking

[](#unstaking)

Before withdrawing their staked tokens, users must initiate a cooldown period by invoking the cooldown() function. After the cooldown period, defined by \_cooldownSeconds, has elapsed, there is a limited window (UNSTAKE\_WINDOW) during which users can redeem their staked tokens by calling the redeem function. If this window is missed, the cooldown process must be restarted.

```
function cooldown() external;function redeem(address to, uint256 amount) external;
```

Actions involving staked tokens can affect the cooldown period:

*   **Staking More Tokens**: Adding more tokens to your stake during an active cooldown doesn't impact the existing cooldown. The new tokens will require a separate cooldown period before they can be unstaked.
    
*   **Unstaking Tokens**: Once the cooldown period has passed, only the tokens that were in cooldown can be unstaked. Unstaking resets the cooldown for the withdrawn amount, and any remaining staked tokens will need a new cooldown period for future withdrawals.
    
*   **Claiming Rewards**: Collecting earned incentives doesn't affect the cooldown period. Users can claim rewards at any time without influencing their cooldown status.
    
*   **Transferring Staked Tokens**: Sending staked tokens to another address doesn't alter the sender's cooldown. The recipient must initiate their own cooldown period to unstake those tokens, as the cooldown is not transferred along with the tokens.
    

After the cooldown period concludes, users have a two-day window to unstake their tokens. Failing to do so within this timeframe means they must initiate the cooldown process again, waiting the full duration before being able to unstake.

### Exchange Rate Mechanism

[](#exchange-rate-mechanism)

The exchange rate determines how staked tokens convert back to the underlying assets. Initially set to a 1:1 ratio (1e18), the exchange rate adjusts in response to slashing events or when additional funds are added to the module. This mechanism determines the value of staked tokens to reflect the total assets within the Safety Module after such events. The exchange rate is calculated using the formula:

```
exchangeRate = (totalAssets * EXCHANGE_RATE_UNIT) / totalShares;
```

### Rewards

[](#rewards)

Participants earn rewards over time based on emission rates set by Aave Governance. The AaveDistributionManager contract manages the calculation and distribution of these incentives. Rewards are proportional to the amount staked and the duration of staking.

The formula for calculating accrued rewards is:

```
Accrued Rewards = (User's Stake * (Asset Index - User Index))
```

*   **Asset Index**: A cumulative value representing the total rewards per unit staked, updated regularly based on the emission rate and total staked tokens.
    
*   **User Index**: The index value recorded during the user's last interaction with the staking contract.
    

### Claiming Rewards

[](#claiming-rewards)

Users can claim their accumulated rewards at any time by calling the claimRewards function:

```
function claimRewards(address to, uint256 amount) external;
```

Claimed rewards are transferred to the user's wallet. This action does not affect the staking status or the cooldown period. Users with the appropriate permissions can also claim rewards on behalf of others using claimRewardsOnBehalf. Additionally, there's an option to claim rewards and immediately restake them in one transaction using claimRewardsAndStake, allowing users to compound rewards.

### Slashing

[](#slashing)

Slashing is a mechanism designed to cover losses in the event of a protocol shortfall by utilizing a portion of the staked funds. Only addresses with the SLASH\_ADMIN\_ROLE (held by [Aave Governance](/docs/primitives/governance)) can initiate a slashing event by calling the slash function:

```
function slash(address destination, uint256 amount) external onlySlashingAdmin returns (uint256);
```

The maximum slashing amount is determined per-asset by \_maxSlashablePercentage, a predefined limit set by the SLASH\_ADMIN\_ROLE.

After a slashing event, the exchange rate is updated to reflect the reduced total assets, proportionally affecting all stakers. The module then enters a post-slashing period during which:

*   New staking is temporarily disabled to prevent dilution of existing stakers' shares.
    
*   Stakers can redeem their tokens without waiting for a cooldown period, allowing them to exit the module promptly.
    
*   No further slashing events can occur until the current one is settled.
    

To conclude the post-slashing period and resume normal operations, the SLASH\_ADMIN\_ROLE must call:

```
function settleSlashing() external onlySlashingAdmin;
```

### Deployed Contracts

[](#deployed-contracts)

Name

Address

**AAVE**

[0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9](https://etherscan.io/address/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9)

**AAVE\_ORACLE**

[0x547a514d5e3769680Ce22B2361c10Ea13619e8a9](https://etherscan.io/address/0x547a514d5e3769680Ce22B2361c10Ea13619e8a9)

**STK\_AAVE**

[0x4da27a545c0c5B758a6BA100e3a049001de870f5](https://etherscan.io/address/0x4da27a545c0c5B758a6BA100e3a049001de870f5)

**GHO**

[0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f](https://etherscan.io/address/0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f)

**GHO\_ORACLE**

[0x3f12643d3f6f874d39c2a4c9f2cd6f2dbac877fc](https://etherscan.io/address/0x3f12643d3f6f874d39c2a4c9f2cd6f2dbac877fc)

**STK\_GHO**

[0x1a88Df1cFe15Af22B3c4c783D4e6F7F9e0C1885d](https://etherscan.io/address/0x1a88Df1cFe15Af22B3c4c783D4e6F7F9e0C1885d)

**STK\_AAVE\_WSTETH\_BALANCER\_POOL\_V2**

[0x9eDA81C21C273a82BE9Bbc19B6A6182212068101](https://etherscan.io/address/0x9eDA81C21C273a82BE9Bbc19B6A6182212068101)

**STK\_AAVE\_WSTETH\_BALANCER\_POOL\_V2\_ORACLE**

[0xADf86b537eF08591c2777E144322E8b0Ca7E82a7](https://etherscan.io/address/0xADf86b537eF08591c2777E144322E8b0Ca7E82a7)

**STK\_AAVE\_WSTETH\_BALANCER\_POOL\_V2\_MIGRATOR**

[0xecD4bd3121F9FD604ffaC631bF6d41ec12f1fafb](https://etherscan.io/address/0xecD4bd3121F9FD604ffaC631bF6d41ec12f1fafb)

**STK\_AAVE\_ETH\_BALANCER\_POOL\_V1** (deprecated)

[0xa1116930326D21fB917d5A27F1E9943A9595fb47](https://etherscan.io/address/0xa1116930326D21fB917d5A27F1E9943A9595fb47)

**STK\_AAVE\_ETH\_BALANCER\_POOL\_V1** (deprecated)

[0x209Ad99bd808221293d03827B86cC544bcA0023b](https://etherscan.io/address/0x209Ad99bd808221293d03827B86cC544bcA0023b)

[

Previous

**Governance**

](/docs/developers/governance)[

Next

**Flash Loans**

](/docs/developers/flash-loans)

---

<a id="doc_19"></a>

## 📁 developers / Smart Contracts | Aave Protocol Documentation

*파일 경로: developers/smart_contracts.md*

Source: https://aave.com/docs/developers/smart-contracts

## Smart Contracts

[](#smart-contracts)

Liquidity PoolsSafety ModuleTokensGovernance

The source code of the Aave V3 Protocol contracts is available on [GitHub](https://github.com/aave-dao/aave-v3-origin). Contract addresses can be imported as Solidity or JavaScript package with the [Aave Address Book](https://github.com/bgd-labs/aave-address-book).

The core contracts fall into the following categories in the GitHub repository:

*   Pool
    
*   Configuration
    
*   Logic
    
*   Tokenization
    
*   Helpers
    
*   Misc
    

### Pool

[](#pool)

#### Pool

[](#pool-pool)

The [Pool](/docs/developers/smart-contracts/pool) is the main entry point into the Aave Protocol. Most user interactions with the Aave Protocol occur via the Pool contract. Pool is owned by the PoolAddressesProvider of the specific market. All admin functions are callable by the PoolConfigurator contract, which is defined in PoolAddressesProvider.

#### L2Pool

[](#pool-l2pool)

The [L2Pool](/docs/developers/smart-contracts/l2-pool) is a modification of the Pool contract for L2 rollups, with gas-optimized user methods that takes byte encoded input arguments. It is a calldata optimized extension of the Pool contract allowing users to pass compact calldata representations to reduce transaction costs on rollups.

#### PoolConfigurator

[](#pool-poolconfigurator)

The [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) provides configuration methods for the Pool contract. The write methods of this contract can only be called by addresses with corresponding permissioned system roles that are managed by ACLManager.

### Configuration

[](#configuration)

#### ACLManager

[](#configuration-aclmanager)

The [ACLManager](/docs/developers/smart-contracts/acl-manager) contract is the main registry of system roles and permissions.

#### PoolAddressesProvider

[](#configuration-pooladdressesprovider)

The [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider) is a registry of various components of the protocol, including the ACLManager and Pool contracts, and has the ability to update pointers or update the implementation of proxy contracts.

### Logic

[](#logic)

[Libraries](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/logic/) that implement the base logic for various actions and functions.

### Tokenization

[](#tokenization)

#### AToken

[](#tokenization-atoken)

[ATokens](/docs/developers/smart-contracts/tokenization) are yield-generating tokens that are minted and burnt upon supply and withdraw of assets to Aave Pool.

#### VariableDebtToken

[](#tokenization-variabledebttoken)

[VariableDebtTokens](/docs/developers/smart-contracts/tokenization) are non-transferable interest accruing tokens representing variable borrow rate positions.

### Helpers

[](#helpers)

#### L2Encoder

[](#helpers-l2encoder)

The [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) is a helper contract to encode calldata that is passed to the L2Pool. It is used to optimize calldata size in L2Pool for transaction cost reduction. It is only intended to help generate calldata for users/frontends.

#### AaveProtocolDataProvider

[](#helpers-aaveprotocoldataprovider)

The [AaveProtocolDataProvider](/docs/developers/smart-contracts/view-contracts) is a peripheral contract to collect and pre-process information from the Pool.

### Misc

[](#misc)

#### AaveOracle

[](#misc-aaveoracle)

The [AaveOracle](/docs/developers/smart-contracts/oracles) is the registry of reserve oracle to get asset prices and manage price sources.

#### DefaultReserveInterestRateStrategy

[](#misc-defaultreserveinterestratestrategy)

The [DefaultReserveInterestRateStrategy](/docs/developers/smart-contracts/interest-rate-strategy) implements the calculation of the interest rates depending on the reserve state. This contract holds the information needed to calculate and update the yield relating to specific liquidity pools.

#### PriceOracleSentinel

[](#misc-priceoraclesentinel)

The [PriceOracleSentinel](/docs/developers/smart-contracts/oracles) validates if operations are allowed depending on the PriceOracle health. Once the PriceOracle gets up after an outage or downtime, users can make their positions healthy during a grace period.

[

Previous

**Aave V3**

](/docs/developers/aave-v3)[

Next

**Pool**

](/docs/developers/smart-contracts/pool)

---

<a id="doc_20"></a>

## 📁 developers / Testing & Debugging | Aave Protocol Documentation

*파일 경로: developers/testing_and_debugging.md*

Source: https://aave.com/docs/developers/testing-and-debugging

## Testing & Debugging

[](#testing-debugging)

This guide provides comprehensive instructions on how to test and debug Aave protocol integrations.

### Testing

[](#testing)

There are two primary methods for testing the Aave protocol: using a **testnet** or creating **fork networks**.

#### Testnet

[](#testing-testnet)

The Aave protocol is available for testing on the Sepolia testnet. You can access the Sepolia V3 testnet market by visiting [app.aave.com](https://app.aave.com) and enabling testnet mode in the top right corner.

To get started:

1.  Visit the test market on [app.aave.com](https://app.aave.com).
    
2.  Use the **Faucet** tab to acquire test tokens available in the market.
    
3.  Supply these tokens to the protocol.
    
4.  Perform operations such as borrowing, repaying, and withdrawing to test different functionalities.
    

#### Fork Networks

[](#testing-fork-networks)

A fork network replicates the state of a blockchain, allowing you to interact with it in a sandbox environment. This is especially useful for testing scenarios that depend on contracts and states existing on the mainnet.

##### Creating a Fork Network

[](#testing-fork-networks-creating-a-fork-network)

Several tools can help you create a fork network:

*   **[Tenderly](https://docs.tenderly.co/simulations-and-forks/forks)**: Debugging toolkit with fork networks, simulations, and online dashboard.
    
*   **[Foundry](https://book.getfoundry.sh/forge/fork-testing)**: Smart contract development framework.
    
*   **[Hardhat](https://hardhat.org/hardhat-network/docs/guides/forking-other-networks)**: Smart contract development framework.
    

To acquire tokens on a fork network, you can impersonate an address that holds the desired tokens (holders can be found using block explorers) and transfer them to your address.

##### Connecting the Fork Network to the UI

[](#testing-fork-networks-connecting-the-fork-network-to-the-ui)

The [app.aave.com](https://app.aave.com) interface can be configured to connect to a fork network. By setting specific variables via the browser console, you can enable this functionality. Refer to [this guide](https://github.com/aave/interface/blob/main/CONTRIBUTING.md#running-against-a-chain-fork) for detailed instructions.

### Debugging

[](#debugging)

When interacting with the Aave protocol, you may encounter smart contract errors. This section helps you understand how to interpret error codes, use debugging tools, and resolve common issues.

#### Error Codes

[](#debugging-error-codes)

The Aave protocol uses specific error codes to indicate why a transaction failed. Understanding these codes is essential for debugging. The error codes for each Aave protocol version are defined in their respective Errors.sol files:

*   **Aave V3 Error Codes**: [Errors.sol](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/helpers/Errors.sol)
    
*   **Aave V2 Error Codes**: [Errors.sol](https://github.com/aave/protocol-v2/blob/master/contracts/protocol/libraries/helpers/Errors.sol)
    

#### Debugging Tools

[](#debugging-debugging-tools)

To effectively debug transactions, you can use tools like **Tenderly**, **Hardhat**, and **Foundry**. These tools allow you to simulate transactions, inspect state changes, and step through execution to identify issues.

##### Tenderly

[](#debugging-debugging-tools-tenderly)

Tenderly allows you to simulate transactions and debug them step-by-step. By inputting the transaction details (to, from, data, and value), you can simulate the call and identify the cause of any revert, including error codes and stack traces.

##### Hardhat

[](#debugging-debugging-tools-hardhat)

Hardhat provides a local Ethereum environment for testing and debugging. It offers features like console logs in Solidity, detailed stack traces, and the ability to fork mainnet state for testing.

##### Foundry

[](#debugging-debugging-tools-foundry)

Foundry is a fast, portable, and modular toolkit for Ethereum application development. It includes tools like Forge for testing and debugging smart contracts, allowing you to simulate and debug transactions effectively.

##### Understanding "Gas Estimation Failed"

[](#debugging-debugging-tools-understanding-gas-estimation-failed)

The "Gas estimation failed" error is a generic message indicating that the transaction would fail if executed. To diagnose this issue:

1.  Use the transaction's to, from, data, and value fields.
    
2.  Simulate the transaction using one of the debugging tools mentioned above.
    
3.  Identify the specific error code or exception causing the failure.
    
4.  Examine the stack trace to pinpoint the issue.
    

#### Common Errors

[](#debugging-common-errors)

##### Aave V3 Pool

[](#debugging-common-errors-aave-v3-pool)

When interacting with the Aave V3 Pool, you may encounter issues related to token approvals, insufficient collateral, or reaching protocol limits.

###### ERC-20 Token Approval for Supply and Repay

Before supplying or repaying tokens, ensure that you have granted the Aave Pool contract an allowance to transfer tokens. This is performed by calling the approve function on the ERC-20 token contract to authorize the Pool as the spender.

###### Insufficient Collateral

If you're unable to borrow assets, it may be due to insufficient collateral or not meeting the required Loan-to-Value (LTV) ratios. Ensure that you have supplied enough collateral and that it satisfies the protocol's requirements.

###### Borrow Cap Reached

Sometimes, you may not be able to borrow a specific asset because the borrow cap has been reached. In this case, you may need to wait for borrowers to repay or supply more liquidity to the pool.

For more detailed explanations of potential revert cases, refer to this [DeFi Integration Guide](https://github.com/Walodja1987/DeFi-Integration-Guide/blob/main/AaveV3.1.md).

###### Loan To Value = 0%

When an Aave [reserve](/docs/primitives/reserve) has a Loan To Value (LTV) parameter configured to 0%, commonly referred to as **LTV0**, it impacts reserve interactions in several ways:

*   **Borrowing power**: Any existing collateral of this asset will no longer contribute to borrowing power.
    
*   **Collateral status**: The asset can no longer be enabled as collateral.
    
*   **Transfers**: If received via transfer, the asset will not be automatically enabled as collateral.
    
*   **Withdrawals**: Assets with LTV0 must be disabled as collateral (using Pool.setUserUseReserveAsCollateral or by fully withdrawing the supplied balance) before other assets can be withdrawn.
    

##### WrappedTokenGateway

[](#debugging-common-errors-wrappedtokengateway)

When interacting with Ether (ETH) in the Aave protocol, the WrappedTokenGateway is used to wrap ETH into WETH and vice versa. Common issues may include not sending ETH with the transaction when required or using incorrect functions for depositing or withdrawing ETH.

For detailed usage and potential revert causes, refer to the [WrappedTokenGateway documentation](/docs/developers/smart-contracts/wrapped-token-gateway).

[

Previous

**V2**

](/docs/developers/legacy-versions/v2)[

Next

**Security & Audits**

](https://aave.com/security)

---

<a id="doc_21"></a>

## 📁 developers/legacy_versions / Aave V1 | Aave Protocol Documentation

*파일 경로: developers/legacy_versions/v1.md*

Source: https://aave.com/docs/developers/legacy-versions/v1

## Aave v1

[](#aave-v1)

### Resources

[](#resources)

*   [Whitepaper](https://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf)
    
*   [Source Code](https://github.com/aave/aave-protocol)
    
*   [Contract Addresses](https://github.com/bgd-labs/aave-address-book/blob/main/src/AaveV1.sol)
    
*   [Interface](https://github.com/aave/aave-protocol)
    

### Key differences

[](#key-differences)

The following are key architectural differences between Aave v1 and subsequent protocol versions:

*   **Tokenization**: In V1, positions were not tokenized, meaning users had to manually calculate their supply & borrow balances by querying individual contracts.
    
*   **PoolCore**: V1 used a separate contract, PoolCore, to hold protocol assets, which added complexity for users and developers. In V2, this was replaced, and assets are held directly by aTokens.
    
*   **ETH -> WETH**: In V1, the protocol used ETH directly, but Aave V2 switched to WETH for consistency.
    
*   **Interest Redirection**: V1 allowed users to redirect earned interest to another address, a feature removed in V2.
    
*   **Batch Flash Loans**: V1 introduced flash loans, but they were limited to single transactions. V2 expanded this to batch flash loans and added new modes for flash loans with deferred repayment.
    
*   **Withdraw aTokens**: In V1, users had to redeem or withdraw their aTokens through the aToken contract. V2 migrated this action to the Pool contract.
    

### Architecture

[](#architecture)

#### Pool Core

[](#architecture-pool-core)

The PoolCore contract holds the state of every reserve and all assets supplied, as well as the basic logic (e.g. calculations using the stored data).

#### PoolAddressesProvider

[](#architecture-pooladdressesprovider)

The PoolAddressesProvider is a global addresses register of the protocol. This contract is immutable and the address will never change.

#### Pool Data Provider

[](#architecture-pool-data-provider)

The PoolDataProvider contract performs calculations and provides data for the Pool contract, specifically:

*   Calculates the ETH equivalent of a user's balance to assess the borrow limit of a user and the health factor of their positions.
    
*   Aggregates data from PoolCore to provide high level information to the Pool.
    
*   Calculates the Average Loan to Value and Average Liquidation Ratio.
    

#### Pool

[](#architecture-pool)

The Pool contract uses both the PoolCore and PoolDataProvider to interact with the reserves. This is the main contract developers should interface with. See the Pool section of the documentation.

The Pool also manages the tokenization of users' supply position via aTokens.

#### Pool Configurator

[](#architecture-pool-configurator)

The PoolConfigurator contract provides configuration functions for the Pool and PoolCore contracts. It also has a number of important functions:

*   Activates / Deactivates reserves,
    
*   Enables / Disables borrowing for a reserve,
    
*   Enables / Disables using a reserve as collateral,
    
*   Enables / Disables stable rate borrowing for a reserve,
    
*   Freezes / Unfreezes reserves,
    
*   Updates a reserve's Loan to Value,
    
*   Updates a reserve's liquidation threshold,
    
*   Updates a reserve's liquidation bonus,
    
*   Updates a reserve's decimals,
    
*   Updates a reserve's interest rate strategy address.
    

For all of the above functions, relevant events are emitted to the blockchain. Anyone can monitor these changes to know when values have been modified or added/removed.

The contract is owned by the PoolManager, as defined in the PoolAddressProvider.

#### Interest Rate Strategy

[](#architecture-interest-rate-strategy)

The InterestRateStrategy contract holds the information needed to calculate and update the interest rates of specific reserves.

Each contract stores the optimised base curves using the corresponding parameters of each currency. This means that there is a mathematical function which determines the interest rate of each asset pool, with the interest rate changing based on the amount of borrowed funds and the total liquidity (i.e. utilisation) of the asset pool.

The parameters for the optimised base curves are:

*   baseVariableBorrowRate
    
*   variableRateSlope1
    
*   variableRateSlope2
    
*   stableRateSlope1
    
*   stableRateSlope2
    

The interest rates are calculated depending on the available liquidity and the total borrowed amount.

Every reserve has a corresponding InterestRateStrategy contract.

[

Previous

**Legacy Versions**

](/docs/developers/legacy-versions)[

Next

**V2**

](/docs/developers/legacy-versions/v2)

---

<a id="doc_22"></a>

## 📁 developers/legacy_versions / Aave V2 | Aave Protocol Documentation

*파일 경로: developers/legacy_versions/v2.md*

Source: https://aave.com/docs/developers/legacy-versions/v2

## Aave v2

[](#aave-v2)

### Resources

[](#resources)

*   [Contract Addresses](/docs/resources/addresses)
    
*   [Source Code](https://github.com/aave/protocol-v2)
    
*   [Subgraphs](https://github.com/aave/protocol-subgraphs)
    
*   [JavaScript SDK](https://github.com/aave/aave-utilities)
    
*   [Interface](https://app.aave.com)
    
*   [Whitepaper](https://github.com/aave/protocol-v2/blob/master/aave-v2-whitepaper.pdf)
    

### Architecture

[](#architecture)

#### Pool

[](#architecture-pool)

The main entry point into the Aave Protocol. Most interactions with Aave will happen via the Pool, including:

*   deposit()
    
*   borrow()
    
*   repay()
    
*   setUserUseReserveAsCollateral()
    
*   withdraw()
    
*   flashloan()
    
*   liquidationCall()
    

#### PoolAddressesProvider

[](#architecture-pooladdressesprovider)

The main addresses register of the protocol, for particular markets. The latest contract addresses should be retrieved from this contract by making the appropriate calls.

#### PoolAddressesProviderRegistry

[](#architecture-pooladdressesproviderregistry)

Contains a list of active PoolAddressesProvider addresses, for different markets.

#### aTokens

[](#architecture-atokens)

The yield-generating, tokenized representation of supplies used throughout the Aave protocol. They implement most of the standard EIP-20/ERC20 token methods with slight modifications, as well as Aave-specific methods including:

*   scaledBalanceOf()
    
*   getScaledUserBalanceAndSupply()
    
*   scaledTotalSupply()
    

All aTokens also implement EIP-2612, which via the permit() function enables single transaction approve + actions.

#### Variable Debt Tokens

[](#architecture-variable-debt-tokens)

The tokenized borrow positions used throughout the Aave protocol. Most of the standard EIP-20/ERC20 methods are disabled since debt tokens are non-transferrable.

#### Supporting Contracts

[](#architecture-supporting-contracts)

The following contracts should generally not be interacted with directly, but are used throughout the Aave Protocol via contract calls.

##### PoolCollateralManager

[](#architecture-supporting-contracts-poolcollateralmanager)

Using delegatecall via the Pool contract, the PoolCollateralManager implements actions involving the management of collateral in the protocol, including:

*   liquidationCall()
    

This function should only be called via the main Pool contract.

##### Pool Configurator

[](#architecture-supporting-contracts-pool-configurator)

Provides configuration functions for the Pool contracts. It has a number of important functions, such as:

*   Activates / Deactivates reserves
    
*   Enables / Disables borrowing for a reserve
    
*   Enables / Disables using a reserve as collateral
    
*   Enables / Disables stable rate borrowing for a reserve
    
*   Freezes / Unfreezes reserves
    
*   Updates a reserve's Loan to Value
    
*   Updates a reserve's liquidation threshold
    
*   Updates a reserve's liquidation bonus
    
*   Updates a reserve's decimals
    
*   Updates a reserve's interest rate strategy address
    
*   Activates / Deactivates all functions of a Pool in emergencies
    

For all of the above functions, relevant events are emitted to the blockchain. Anyone can monitor these changes to know when values have been modified or added/removed.

##### Interest Rate Strategy

[](#architecture-supporting-contracts-interest-rate-strategy)

Holds the information needed to calculate and update the interest rates of specific reserves. Each contract stores the optimized base curves using the corresponding parameters of each currency. The parameters for the optimized base curves are:

*   baseVariableBorrowRate
    
*   variableRateSlope1
    
*   variableRateSlope2
    
*   stableRateSlope1
    
*   stableRateSlope2
    

The interest rates are calculated depending on the available liquidity and the total borrowed amount.

[

Previous

**V1**

](/docs/developers/legacy-versions/v1)[

Next

**Testing & Debugging**

](/docs/developers/testing-and-debugging)

---

<a id="doc_23"></a>

## 📁 developers/smart_contracts / ACL Manager | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/acl_manager.md*

Source: https://aave.com/docs/developers/smart-contracts/acl-manager

## ACLManager

[](#aclmanager)

The Access Control List Manager (ACLManager) is the main registry of system roles and permissions.

The Aave Protocol implements an access control list to segregate powers and/or benefits that can be allocated to different entities on the protocol. The ACL\_MANAGER contract is managed by the [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider) contract.

ACLManager keeps track of the individual roles and its holders, and allows a *Role Admin* to manage roles. *Role Admin* is itself a role that is managed by the DEFAULT\_ADMIN\_ROLE.

The DEFAULT\_ADMIN\_ROLE is held by the [ACL\_ADMIN](/docs/developers/smart-contracts/acl-manager#acl_admin), and should be initialized in the [PoolAddressesProvider](/docs/developers/smart-contracts/poola-ddresses-provider) beforehand.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/configuration/ACLManager.sol).

### Roles

[](#roles)

Below we outline the responsibilities/powers of the roles and the specific methods that are only accessible to the holders of these roles.

The [FLASH\_BORROWER](/docs/developers/smart-contracts/acl-manager#flash_borrower) and [BRIDGE](/docs/developers/smart-contracts/acl-manager#bridge) roles have few direct responsibilities and can primarily access specific features of the protocol, while ADMIN roles have the power and responsibility to handle risk or configuration parameters.

#### FLASH\_BORROWER

[](#roles-flash-borrower)

Holders of this role will have the premium on flash loans waived (this does not include the simple flash loan).

##### Methods Accessible:

[](#roles-flash-borrower-methods-accessible)

**[Pool](/docs/developers/smart-contracts/pool)**:

*   [flashLoan()](/docs/developers/smart-contracts/pool#flashloan)
    

#### BRIDGE

[](#roles-bridge)

Holders can leverage the [Portals](/docs/developers/aave-v3#features-portals) feature.

##### Methods Accessible:

[](#roles-bridge-methods-accessible)

**[Pool](/docs/developers/pool)**:

*   [mintUnbacked()](/docs/developers/smart-contracts/pool#mintunbacked)
    
*   [backUnbacked()](/docs/developers/smart-contracts/pool#backunbacked)
    

#### ASSET\_LISTING\_ADMIN

[](#roles-asset-listing-admin)

Holders of this role can:

*   Update asset oracle sources and the fallback oracle.
    
*   Add new assets to the Aave market.
    

##### Methods Accessible:

[](#roles-asset-listing-admin-methods-accessible)

**[AaveOracle](/docs/developers/smart-contracts/oracles)**:

*   [setAssetSources()](/docs/developers/smart-contracts/oracles#write-methods-setassetsources)
    
*   [setFallbackOracle()](/docs/developers/smart-contracts/oracles#write-methods-setfallbackoracle)
    

**[PoolConfigurator](/docs/developers/smart-contracts/pool-configurator)**:

*   [initReserves()](/docs/developers/smart-contracts/pool-configurator#initreserves)
    

#### RISK\_ADMIN

[](#roles-risk-admin)

Holders of this role can:

*   Update the grace period of Oracle Sentinels.
    
*   Update reserve parameters such as reserve factor, caps, E-Mode category, borrowing enabled, freeze/unfreeze, LTV, liquidation threshold, liquidation bonus (cannot pause/unpause or activate/deactivate a reserve).
    
*   Create new and update existing E-Mode categories (not category 0).
    
*   Update unbacked mint cap and liquidation protocol fee.
    

##### Methods Accessible:

[](#roles-risk-admin-methods-accessible)

**[PoolConfigurator](/docs/developers/smart-contracts/pool-configurator)**:

*   [setReserveBorrowing()](/docs/developers/smart-contracts/pool-configurator#setreserveborrowing)
    
*   [configureReserveAsCollateral()](/docs/developers/smart-contracts/pool-configurator#configurereserveascollateral)
    
*   [setReserveFreeze()](/docs/developers/smart-contracts/pool-configurator#setreservefreeze)
    
*   [setBorrowableInIsolation()](/docs/developers/smart-contracts/pool-configurator#setborrowableinisolation)
    
*   [setReserveFactor()](/docs/developers/smart-contracts/pool-configurator#setreservefactor)
    
*   [setDebtCeiling()](/docs/developers/smart-contracts/pool-configurator#setdebtceiling)
    
*   [setSiloedBorrowing()](/docs/developers/smart-contracts/pool-configurator#setsiloedborrowing)
    
*   [setBorrowCap()](/docs/developers/smart-contracts/pool-configurator#setborrowcap)
    
*   [setSupplyCap()](/docs/developers/smart-contracts/pool-configurator#setsupplycap)
    
*   [setLiquidationProtocolFee()](/docs/developers/smart-contracts/pool-configurator#setliquidationprotocolfee)
    
*   [setEModeCategory()](/docs/developers/smart-contracts/pool-configurator#setemodecategory)
    
*   [setAssetCollateralInEMode()](/docs/developers/smart-contracts/pool-configurator#setassetcollateralinemode)
    
*   [setUnbackedMintCap()](/docs/developers/smart-contracts/pool-configurator#setunbackedmintcap)
    
*   [setReserveInterestRateStrategyAddress()](/docs/developers/smart-contracts/pool-configurator#setreserveinterestratestrategyaddress)
    
*   [setReserveInterestRateData()](/docs/developers/smart-contracts/pool-configurator#setreserveinterestratedata)
    
*   [disableLiquidationGracePeriod()](/docs/developers/smart-contracts/pool-configurator#disableliquidationgraceperiod)
    
*   [setReserveFlashLoaning()](/docs/developers/smart-contracts/pool-configurator#setreserveflashloaning)
    

**[PriceOracleSentinel](/docs/developers/smart-contracts/oracles)**:

*   setGracePeriod()
    

#### ACL\_ADMIN

[](#roles-acl-admin)

Holders of this role manage the role admins in the ACLManager. The DEFAULT\_ADMIN\_ROLE is held by the ACL\_ADMIN, and should be initialized in the PoolAddressesProvider beforehand.

##### Methods Accessible:

[](#roles-acl-admin-methods-accessible)

**[ACLManager](/docs/developers/smart-contracts/acl-manager)**:

*   [setRoleAdmin()](/docs/developers/smart-contracts/acl-manager#setroleadmin)
    
*   [addPoolAdmin()](/docs/developers/smart-contracts/acl-manager#addpooladmin)
    
*   [removePoolAdmin()](/docs/developers/smart-contracts/acl-manager#removepooladmin)
    
*   [addEmergencyAdmin()](/docs/developers/smart-contracts/acl-manager#addemergencyadmin)
    
*   [removeEmergencyAdmin()](/docs/developers/smart-contracts/acl-manager#removeemergencyadmin)
    
*   [addRiskAdmin()](/docs/developers/smart-contracts/acl-manager#addriskadmin)
    
*   [removeRiskAdmin()](/docs/developers/smart-contracts/acl-manager#removeriskadmin)
    
*   [addFlashBorrower()](/docs/developers/smart-contracts/acl-manager#addflashborrower)
    
*   [removeFlashBorrower()](/docs/developers/smart-contracts/acl-manager#removeflashborrower)
    
*   [addBridge()](/docs/developers/smart-contracts/acl-manager#addbridge)
    
*   [removeBridge()](/docs/developers/smart-contracts/acl-manager#removebridge)
    
*   [addAssetListingAdmin()](/docs/developers/smart-contracts/acl-manager#addassetlistingadmin)
    
*   [removeAssetListingAdmin()](/docs/developers/smart-contracts/acl-manager#removeassetlistingadmin)
    

#### EMERGENCY\_ADMIN

[](#roles-emergency-admin)

Holders of this role can pause and unpause the pool or an individual reserve.

##### Methods Accessible:

[](#roles-emergency-admin-methods-accessible)

**[PoolConfigurator](/docs/developers/smart-contracts/pool-configurator)**:

*   [setReservePause()](/docs/developers/smart-contracts/pool-configurator#setreservepause)
    
*   [setPoolPause()](/docs/developers/smart-contracts/pool-configurator#setpoolpause)
    
*   [setReserveActive()](/docs/developers/smart-contracts/pool-configurator#setreserveactive)
    
*   [setReserveFreeze()](/docs/developers/smart-contracts/pool-configurator#setreservefreeze)
    

#### POOL\_ADMIN

[](#roles-pool-admin)

Holders of this role can update token implementations, drop, (un)pause and (de)activate reserves, update premiums along with everything the [ASSET\_LISTING\_ADMIN](/docs/developers/smart-contracts/acl-manager#asset_listing_admin) and [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager#risk_admin) can do.

All deployers have resigned their [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) roles. All instances of the [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) role, across all V3 networks, are now governed by the \[Guardians multisig\] or by the [Governance Bridge executors](https://github.com/aave/governance-crosschain-bridges).

##### Methods Accessible:

[](#roles-pool-admin-methods-accessible)

All methods accessible to ASSET\_LISTING\_ADMIN.

All methods accessible to RISK\_ADMIN.

**[AToken](/docs/developers/smart-contracts/tokenization)**:

*   [rescueTokens()](/docs/developers/smart-contracts/tokenization)
    

**[Pool](/docs/developers/smart-contracts/pool)**:

*   [rescueTokens()](/docs/developers/smart-contracts/pool#rescuetokens)
    

**[IncentivizedERC20](/docs/developers/smart-contracts/tokenization)**:

*   [setIncentivesController()](/docs/developers/smart-contracts/tokenization)
    

**[PoolConfigurator](/docs/developers/smart-contracts/pool-configurator)**:

*   [dropReserve()](/docs/developers/smart-contracts/pool-configurator#dropreserve)
    
*   [updateAToken()](/docs/developers/smart-contracts/pool-configurator#updateatoken)
    
*   [updateVariableDebtToken()](/docs/developers/smart-contracts/pool-configurator#updatevariabledebttoken)
    
*   [setReserveActive()](/docs/developers/smart-contracts/pool-configurator#setreserveactive)
    
*   [updateBridgeProtocolFee()](/docs/developers/smart-contracts/pool-configurator#updatebridgeprotocolfee)
    
*   [updateFlashloanPremiumTotal()](/docs/developers/smart-contracts/pool-configurator#updateflashloanpremiumtotal)
    
*   [updateFlashloanPremiumToProtocol()](/docs/developers/smart-contracts/pool-configurator#updateflashloanpremiumtoprotocol)
    
*   [setAssetBorrowableInEMode()](/docs/developers/smart-contracts/pool-configurator#setassetborrowableinemode)
    
*   [setReserveInterestRateData()](/docs/developers/smart-contracts/pool-configurator#setreserveinterestratedata)
    
*   [setReserveInterestRateStrategyAddress()](/docs/developers/smart-contracts/pool-configurator#setreserveinterestratestrategyaddress)
    

**[PriceOracleSentinel](/docs/developers/smart-contracts/oracles)**:

*   [setSequencerOracle()](/docs/developers/smart-contracts/oracles#write-methods-setsequenceroracle)
    

### Write Methods

[](#write-methods)

#### setRoleAdmin

[](#write-methods-setroleadmin)

```
function setRoleAdmin(bytes32 role, bytes32 adminRole) external override onlyRole(DEFAULT_ADMIN_ROLE)
```

Sets the role as admin of a specific role. By default, the adminRole for all roles is [DEFAULT\_ADMIN\_ROLE](/docs/developers/smart-contracts/acl-manager#acl_admin).

This method can only be called by an address with [DEFAULT\_ADMIN\_ROLE](/docs/developers/smart-contracts/acl-manager#acl_admin).

##### Input Parameters:

[](#write-methods-setroleadmin-input-parameters)

Name

Type

Description

role

bytes32

The role to be managed by the admin role - keccak256 hash of one of the following: POOL\_ADMIN, EMERGENCY\_ADMIN, RISK\_ADMIN, FLASH\_BORROWER, BRIDGE, ASSET\_LISTING\_ADMIN

adminRole

bytes32

The admin role. 0x00 is reserved for the DEFAULT\_ADMIN\_ROLE

#### addPoolAdmin

[](#write-methods-addpooladmin)

```
function addPoolAdmin(address admin) external override
```

Adds a new admin as *Pool Admin*. The address is added to the list of members with the [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) role. Holders of this role can update token implementations, drop, (un)pause and (de)activate reserves, update premiums and do everything the [ASSET\_LISTING\_ADMIN](/docs/developers/smart-contracts/acl-manager#asset_listing_admin) and [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager#risk_admin) can do.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing the [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) role.

##### Input Parameters:

[](#write-methods-addpooladmin-input-parameters)

Name

Type

Description

admin

address

The address which will be granted the POOL\_ADMIN role

#### removePoolAdmin

[](#write-methods-removepooladmin)

```
function removePoolAdmin(address admin) external override
```

Removes an admin as *Pool Admin*. The given address is removed from the list of members with the [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) role.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing the [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) role.

##### Input Parameters:

[](#write-methods-removepooladmin-input-parameters)

Name

Type

Description

admin

address

The address for which the POOL\_ADMIN role permissions will be removed

#### addEmergencyAdmin

[](#write-methods-addemergencyadmin)

```
function addEmergencyAdmin(address admin) external override
```

Adds a new admin as an *Emergency Admin*. The address is added to the list of members with the [EMERGENCY\_ADMIN](/docs/developers/smart-contracts/acl-manager#emergency_admin) role. Holders of this role can pause and unpause the pool or an individual reserve.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing the [EMERGENCY\_ADMIN](/docs/developers/smart-contracts/acl-manager#emergency_admin) role.

##### Input Parameters:

[](#write-methods-addemergencyadmin-input-parameters)

Name

Type

Description

admin

address

The address which will be granted the EMERGENCY\_ADMIN role

#### removeEmergencyAdmin

[](#write-methods-removeemergencyadmin)

```
function removeEmergencyAdmin(address admin) external override
```

Removes an admin as *Emergency Admin*. The given address is removed from the list of members with the [EMERGENCY\_ADMIN](/docs/developers/smart-contracts/acl-manager#emergency_admin) role.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing the [EMERGENCY\_ADMIN](/docs/developers/smart-contracts/acl-manager#emergency_admin) role.

##### Input Parameters:

[](#write-methods-removeemergencyadmin-input-parameters)

Name

Type

Description

admin

address

The address for which the EMERGENCY\_ADMIN role permissions will be removed

#### addRiskAdmin

[](#write-methods-addriskadmin)

```
function addRiskAdmin(address admin) external override
```

Adds a new admin as a *Risk Admin*. The address is added to the list of members with the [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager#risk_admin) role. Holders of this role can update grace period of Oracle Sentinels, reserve params, unbacked mint cap, liquidation fee and eMode categories.

##### Input Parameters:

[](#write-methods-addriskadmin-input-parameters)

Name

Type

Description

admin

address

The address which will be granted the RISK\_ADMIN role

#### removeRiskAdmin

[](#write-methods-removeriskadmin)

```
function removeRiskAdmin(address admin) external override
```

Removes an admin as *Risk Admin*. The given address is removed from the list of members with the [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager#risk_admin) role.

##### Input Parameters:

[](#write-methods-removeriskadmin-input-parameters)

Name

Type

Description

admin

address

The address for which the RISK\_ADMIN role permissions will be removed

#### addFlashBorrower

[](#write-methods-addflashborrower)

```
function addFlashBorrower(address borrower) external override
```

Adds a new borrower address as *Flash Borrower*. The address is added to the list of members with the [FLASH\_BORROWER](/docs/developers/smart-contracts/acl-manager#flash_borrower) role. Holders of this role do not pay premium for flash loan (does not apply to flashLoanSimple).

##### Input Parameters:

[](#write-methods-addflashborrower-input-parameters)

Name

Type

Description

borrower

address

The address which will be granted the FLASH\_BORROWER role

#### removeFlashBorrower

[](#write-methods-removeflashborrower)

```
function removeFlashBorrower(address borrower) external override
```

Removes an admin as *Flash Borrower*. The given borrower address is removed from the list of members with the [FLASH\_BORROWER](/docs/developers/smart-contracts/acl-manager#flash_borrower) role.

##### Input Parameters:

[](#write-methods-removeflashborrower-input-parameters)

Name

Type

Description

borrower

address

The address for which the FLASH\_BORROWER role permissions will be removed

#### addBridge

[](#write-methods-addbridge)

```
function addBridge(address bridge) external override
```

Adds a new address as [BRIDGE](/docs/developers/smart-contracts/acl-manager#bridge). The contract address is added to the list of *bridges*. Holders of this role can leverage the [Portals](/docs/whats_new/portals) feature to seamlessly move supplied assets across Aave V3 markets on different networks.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing the [BRIDGE](/docs/developers/smart-contracts/acl-manager#bridge) role.

##### Input Parameters:

[](#write-methods-addbridge-input-parameters)

Name

Type

Description

bridge

address

The address which will be granted BRIDGE role

#### removeBridge

[](#write-methods-removebridge)

```
function removeBridge(address bridge) external override
```

Removes an address as [BRIDGE](/docs/developers/smart-contracts/acl-manager#bridge). The given contract address is removed from the list of *bridges*.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing [BRIDGE](/docs/developers/smart-contracts/acl-manager#bridge) role.

##### Input Parameters:

[](#write-methods-removebridge-input-parameters)

Name

Type

Description

bridge

address

The address for which BRIDGE role permissions will be removed

#### addAssetListingAdmin

[](#write-methods-addassetlistingadmin)

```
function addAssetListingAdmin(address admin) external override
```

Adds a new admin as *Asset Listing Admin*. The address is added to the list of members with the [ASSET\_LISTING\_ADMIN](/docs/developers/smart-contracts/acl-manager#asset_listing_admin) role. Holder of this role can update oracles and add new assets to the Aave market.

##### Input Parameters:

[](#write-methods-addassetlistingadmin-input-parameters)

Name

Type

Description

admin

address

The address which will be granted ASSET\_LISTING\_ADMIN role

#### removeAssetListingAdmin

[](#write-methods-removeassetlistingadmin)

```
function removeAssetListingAdmin(address admin) external override
```

Removes an admin as *Asset Listing Admin*. The given address is removed from the list of members with the [ASSET\_LISTING\_ADMIN](/docs/developers/smart-contracts/acl-manager#asset_listing_admin) role.

##### Input Parameters:

[](#write-methods-removeassetlistingadmin-input-parameters)

Name

Type

Description

admin

address

The address for which ASSET\_LISTING\_ADMIN role permissions will be removed

### View Methods

[](#view-methods)

#### isPoolAdmin

[](#view-methods-ispooladmin)

```
function isPoolAdmin(address admin) external view override returns (bool)
```

Returns true if the address has the [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pool_admin) role, false otherwise.

##### Input Parameters:

[](#view-methods-ispooladmin-input-parameters)

Name

Type

Description

admin

address

The address to check

##### Return Values:

[](#view-methods-ispooladmin-return-values)

Type

Description

bool

true if the given address is POOL\_ADMIN, false otherwise

#### isEmergencyAdmin

[](#view-methods-isemergencyadmin)

```
function isEmergencyAdmin(address admin) external view override returns (bool)
```

Returns true if the address has the [EMERGENCY\_ADMIN](/docs/developers/smart-contracts/acl-manager#emergency_admin) role, false otherwise.

##### Input Parameters:

[](#view-methods-isemergencyadmin-input-parameters)

Name

Type

Description

admin

address

The address to check

##### Return Values:

[](#view-methods-isemergencyadmin-return-values)

Type

Description

bool

true if the given address is EMERGENCY\_ADMIN, false otherwise

#### isRiskAdmin

[](#view-methods-isriskadmin)

```
function isRiskAdmin(address admin) external view override returns (bool)
```

Returns true if the address has the [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager#risk_admin) role, false otherwise.

##### Input Parameters:

[](#view-methods-isriskadmin-input-parameters)

Name

Type

Description

admin

address

The address to check

##### Return Values:

[](#view-methods-isriskadmin-return-values)

Type

Description

bool

true if the given address is RISK\_ADMIN, false otherwise

#### isFlashBorrower

[](#view-methods-isflashborrower)

```
function isFlashBorrower(address borrower) external view override returns (bool)
```

Returns true if the address has the [FLASH\_BORROWER](/docs/developers/smart-contracts/acl-manager#flash_borrower) role, false otherwise.

##### Input Parameters:

[](#view-methods-isflashborrower-input-parameters)

Name

Type

Description

borrower

address

The address to check

##### Return Values:

[](#view-methods-isflashborrower-return-values)

Type

Description

bool

true if the given address is FLASH\_BORROWER, false otherwise

#### isBridge

[](#view-methods-isbridge)

```
function isBridge(address bridge) external view override returns (bool)
```

Returns true if the address has [BRIDGE](/docs/developers/smart-contracts/acl-manager#bridge) role, false otherwise.

##### Input Parameters:

[](#view-methods-isbridge-input-parameters)

Name

Type

Description

bridge

address

The address to check

##### Return Values:

[](#view-methods-isbridge-return-values)

Type

Description

bool

true if the given address is BRIDGE, false otherwise

#### isAssetListingAdmin

[](#view-methods-isassetlistingadmin)

```
function isAssetListingAdmin(address admin) external view override returns (bool)
```

Returns true if the address has the [ASSET\_LISTING\_ADMIN](/docs/developers/smart-contracts/acl-manager#asset_listing_admin) role, false otherwise.

##### Input Parameters:

[](#view-methods-isassetlistingadmin-input-parameters)

Name

Type

Description

admin

address

The address to check

##### Return Values:

[](#view-methods-isassetlistingadmin-return-values)

Type

Description

bool

true if the given address is ASSET\_LISTING\_ADMIN, false otherwise

[

Previous

**Interest Rate Strategy**

](/docs/developers/smart-contracts/interest-rate-strategy)[

Next

**Oracles**

](/docs/developers/smart-contracts/oracles)

---

<a id="doc_24"></a>

## 📁 developers/smart_contracts / Incentives | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/incentives.md*

Source: https://aave.com/docs/developers/smart-contracts/incentives

## Incentives

[](#incentives)

The [UiIncentiveDataProvider](/docs/developers/smart-contracts/view-contracts) provides methods to query all active incentive emissions, and claimable user incentives for a particular Aave market.

## RewardsController

[](#rewardscontroller)

RewardsController is the main rewards contract where the user interacts to claim the rewards of their positions. It is an abstract contract template to build Distributors contracts for ERC20 rewards to protocol participants. RewardsController inherits from [RewardsDistributor](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/rewards/RewardsDistributor.sol) to handle the distribution of rewards. The users of the incentivized ERC20 assets will accrue value if they hold their tokens in possession without the need for staking or blocking the assets inside a contract.

The users can claim all the rewards or an individual reward per transaction, with a variety of functions that allow more granularity at claim.

At every transfer, the asset must call the handleAction method to account for the user's rewards.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/rewards/RewardsController.sol).

### Write Methods

[](#write-methods)

#### initialize

[](#write-methods-initialize)

```
function initialize(address) external initializer
```

Initialize RewardsController instance.

##### Input Parameters:

[](#write-methods-initialize-input-parameters)

Type

Description

address

Unused but required due to being initialized by PoolAddressProvider.\_updateImpl()

#### configureAssets

[](#write-methods-configureassets)

```
function configureAssets(RewardsDataTypes.RewardsConfigInput[] memory config) external override onlyEmissionManager
```

Configure assets to incentivize with an emission of rewards per second until the end of distribution.

##### Input Parameters:

[](#write-methods-configureassets-input-parameters)

Name

Type

Description

config

RewardsDataTypes.RewardsConfigInput\[\]

The emission per second following rewards unit decimals

The [RewardsDataTypes.RewardsConfigInput](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/rewards/libraries/RewardsDataTypes.sol) struct is composed of the following fields:

Name

Type

Description

emissionPerSecond

uint88

The emission per second following rewards unit decimals

totalSupply

uint256

The total supply of the asset to incentivize

distributionEnd

uint32

The end of the distribution of the incentives for an asset

asset

address

The asset address to incentivize

reward

address

The reward token address

transferStrategy

ITransferStrategy

The TransferStrategy address with the install hook and claim logic

rewardOracle

IEACAggregatorProxy

The Price Oracle of a reward to visualize the incentives at the UI frontend. Must follow Chainlink Aggregator IEACAggregatorProxy interface to be compatible.

#### setTransferStrategy

[](#write-methods-settransferstrategy)

```
function setTransferStrategy(address reward, ITransferStrategyBase transferStrategy) external onlyEmissionManager
```

Sets a TransferStrategy logic contract that determines the logic of the rewards transfer.

##### Input Parameters:

[](#write-methods-settransferstrategy-input-parameters)

Name

Type

Description

reward

address

The address of the reward token

transferStrategy

address

The address of the TransferStrategy logic contract

#### setRewardOracle

[](#write-methods-setrewardoracle)

```
function setRewardOracle(address reward, IEACAggregatorProxy rewardOracle) external onlyEmissionManager
```

Sets an Aave Oracle contract to enforce rewards with a source of value.

At the moment of reward configuration, the Incentives Controller performs a check to see if the reward asset oracle is compatible with IEACAggregator proxy. This check is enforced for integrators to show incentives at the current Aave UI without needing to set up an external price registry.

##### Input Parameters:

[](#write-methods-setrewardoracle-input-parameters)

Name

Type

Description

reward

address

The address of the reward to set the price aggregator

rewardOracle

IEACAggregatorProxy

The address of price aggregator that follows the IEACAggregatorProxy interface

#### handleAction

[](#write-methods-handleaction)

```
function handleAction(address user, uint256 totalSupply, uint256 userBalance) external override
```

Called by the corresponding asset on transfer hook to update the rewards distribution of a user.

##### Input Parameters:

[](#write-methods-handleaction-input-parameters)

Name

Type

Description

user

address

The address of the user

totalSupply

uint256

The user balance of the asset

userBalance

uint256

The total supply of the asset

#### claimRewards

[](#write-methods-claimrewards)

```
function claimRewards(    address[] calldata assets,    uint256 amount,    address to,    address reward) external override returns (uint256)
```

Claims reward for a user to the desired address, on all the assets of the pool, accumulating the pending rewards. Rewards are received by the to address.

##### Input Parameters:

[](#write-methods-claimrewards-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets to check eligible distributions before claiming rewards. Pass a/s/vToken addresses

amount

uint256

The amount of rewards to claim, expressed in wei. Pass MAX\_UINT to claim the entire unclaimed reward balance

to

address

The address that will be receiving the rewards

reward

address

The address of the reward token (e.g., stkAAVE)

##### Return Values:

[](#write-methods-claimrewards-return-values)

Type

Description

uint256

The amount of rewards claimed for one specific reward

The msg.sender must be an authorized claimer set using the setClaimer() method, via a Governance Vote.

#### claimRewardsOnBehalf

[](#write-methods-claimrewardsonbehalf)

```
function claimRewardsOnBehalf(    address[] calldata assets,    uint256 amount,    address user,    address to,    address reward) external override onlyAuthorizedClaimers(msg.sender, user) returns (uint256)
```

Claims rewards for a user on behalf, on all the assets of the pool, accumulating the pending rewards of the assets passed by the first argument. The caller must be whitelisted via the allowClaimOnBehalf function by the EmissionManager role held by Aave Governance. Rewards are received by the to address.

##### Input Parameters:

[](#write-methods-claimrewardsonbehalf-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets to check eligible distributions before claiming rewards. Pass a/s/vToken addresses

amount

uint256

The amount of rewards to claim, expressed in wei. Pass MAX\_UINT to claim the entire unclaimed reward balance

user

address

The address to check and claim rewards

to

address

The address that will be receiving the rewards

reward

address

The address of the reward token being claimed (e.g., stkAAVE)

##### Return Values:

[](#write-methods-claimrewardsonbehalf-return-values)

Type

Description

uint256

The amount of rewards claimed

#### claimRewardsToSelf

[](#write-methods-claimrewardstoself)

```
function claimRewardsToSelf(address[] calldata assets, uint256 amount, address reward) external override returns (uint256)
```

Claims reward for msg.sender, on all the assets of the pool, accumulating the pending rewards passed by the first input parameter. Rewards are received by msg.sender.

##### Input Parameters:

[](#write-methods-claimrewardstoself-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets to check eligible distributions before claiming rewards. Pass a/s/vToken addresses

amount

uint256

The amount of rewards to claim, expressed in wei. Pass MAX\_UINT to claim the entire unclaimed reward balance

reward

address

The address of the reward token

##### Return Values:

[](#write-methods-claimrewardstoself-return-values)

Type

Description

uint256

The amount of rewards claimed for one specific reward

#### claimAllRewards

[](#write-methods-claimallrewards)

```
function claimAllRewards(address[] calldata assets, address to) external override returns (address[] memory rewardsList, uint256[] memory claimedAmounts)
```

Claims all rewards for a user to the desired address, on all the assets of the pool, accumulating the pending rewards passed by the first input parameter. Rewards are received by the to address.

##### Input Parameters:

[](#write-methods-claimallrewards-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets to check eligible distributions before claiming rewards (aToken or variableDebtToken addresses)

to

address

The address that will be receiving the rewards

##### Return Values:

[](#write-methods-claimallrewards-return-values)

Name

Type

Description

rewardsList

address\[\]

The list of addresses of the reward tokens

claimedAmounts

uint256\[\]

The list that contains the claimed amount per reward, following the same order as rewardsList

#### claimAllRewardsOnBehalf

[](#write-methods-claimallrewardsonbehalf)

```
function claimAllRewardsOnBehalf(    address[] calldata assets,    address user,    address to) external override onlyAuthorizedClaimers(msg.sender, user) returns (address[] memory rewardsList, uint256[] memory claimedAmounts)
```

Claims all rewards for a user on behalf, on all the assets of the pool, accumulating the pending rewards passed by the first input parameter. The caller must be whitelisted via the allowClaimOnBehalf function by the EmissionManager role held by Aave Governance. Rewards are received by the to address.

##### Input Parameters:

[](#write-methods-claimallrewardsonbehalf-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets to check eligible distributions before claiming rewards. Pass a/s/vToken addresses

user

address

The address to check and claim rewards

to

address

The address that will be receiving the rewards

##### Return Values:

[](#write-methods-claimallrewardsonbehalf-return-values)

Name

Type

Description

rewardsList

address\[\]

The list of addresses of the reward tokens

claimedAmounts

uint256\[\]

The list that contains the claimed amount per reward, following the same order as rewardsList

#### claimAllRewardsToSelf

[](#write-methods-claimallrewardstoself)

```
function claimAllRewardsToSelf(address[] calldata assets) external override returns (address[] memory rewardsList, uint256[] memory claimedAmounts)
```

Claims all rewards accrued by msg.sender, on all assets of the pool, accumulating the pending rewards by the first input parameter. Rewards are received by msg.sender.

##### Input Parameters:

[](#write-methods-claimallrewardstoself-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets to check eligible distributions before claiming rewards. Pass a/s/vToken addresses

##### Return Values:

[](#write-methods-claimallrewardstoself-return-values)

Name

Type

Description

rewardsList

address\[\]

The list of addresses of the reward tokens

claimedAmounts

uint256\[\]

The list that contains the claimed amount per reward, following the same order as rewardsList

#### setClaimer

[](#write-methods-setclaimer)

```
function setClaimer(address user, address caller) external override onlyEmissionManager
```

Whitelists an address to claim rewards on behalf of another address. Can only be called by the EmissionManager.

##### Input Parameters:

[](#write-methods-setclaimer-input-parameters)

Name

Type

Description

user

address

The address of the user

caller

address

The address of the claimer

### View Methods

[](#view-methods)

#### getClaimer

[](#view-methods-getclaimer)

```
function getClaimer(address user) external view override returns (address)
```

Returns the whitelisted claimer for a certain address. It returns the 0x0 address if it is not set.

##### Input Parameters:

[](#view-methods-getclaimer-input-parameters)

Name

Type

Description

user

address

The address of the user

##### Return Values:

[](#view-methods-getclaimer-return-values)

Type

Description

address

The claimer address

#### getRewardOracle

[](#view-methods-getrewardoracle)

```
function getRewardOracle(address reward) external view override returns (address)
```

Get the price aggregator oracle address.

Name

Type

Description

reward

address

The address of the reward token

##### Return Values:

[](#view-methods-getrewardoracle-return-values)

Type

Description

address

The address of the reward oracle

#### getTransferStrategy

[](#view-methods-gettransferstrategy)

```
function getTransferStrategy(address reward) external view override returns (address)
```

Returns the Transfer Strategy implementation contract address being used for a reward address.

Name

Type

Description

reward

address

The address of the reward

##### Return Values:

[](#view-methods-gettransferstrategy-return-values)

Type

Description

address

The address of the TransferStrategy contract

### Pure Methods

[](#pure-methods)

```
function getRevision() internal pure override returns (uint256)
```

Returns the revision of the implementation contract.

##### Return Values:

[](#view-methods-gettransferstrategy-return-values)

Type

Description

uint256

The current revision version

[

Previous

**View Contracts**

](/docs/developers/smart-contracts/view-contracts)[

Next

**Tokenization**

](/docs/developers/smart-contracts/tokenization)

---

<a id="doc_25"></a>

## 📁 developers/smart_contracts / Interest Rate Strategy | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/interest_rate_strategy.md*

Source: https://aave.com/docs/developers/smart-contracts/interest-rate-strategy

## Interest Rate Strategy

[](#interest-rate-strategy)

Borrow / WithdrawSupply / RepayBorrow rateSupply rate

Implements the calculation of the interest rates depending on the reserve state. The model of interest rate is based on two slopes, one before the OPTIMAL\_USAGE\_RATIO point of usage and another from that point to 100%.

An instance of this same contract can't be used across different Aave markets due to the caching of the [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider).

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/misc/DefaultReserveInterestRateStrategyV2.sol).

### View Methods

[](#view-methods)

#### getVariableRateSlope1

[](#view-methods-getvariablerateslope1)

```
function getVariableRateSlope1(address reserve) external view returns (uint256)
```

Returns the variable rate slope below the optimal usage ratio for the specified reserve. This is the variable rate when the usage ratio is between 0 and OPTIMAL\_USAGE\_RATIO.

##### Input Parameters:

[](#view-methods-getvariablerateslope1-input-parameters)

Name

Type

Description

reserve

address

The address of the reserve

##### Return Values:

[](#view-methods-getvariablerateslope1-return-values)

Type

Description

uint256

The variable rate slope

#### getVariableRateSlope2

[](#view-methods-getvariablerateslope2)

```
function getVariableRateSlope2(address reserve) external view returns (uint256)
```

Returns the variable rate slope above the optimal usage ratio for the specified reserve. This is the variable rate when the usage ratio is greater than OPTIMAL\_USAGE\_RATIO.

##### Input Parameters:

[](#view-methods-getvariablerateslope2-input-parameters)

Name

Type

Description

reserve

address

The address of the reserve

##### Return Values:

[](#view-methods-getvariablerateslope2-return-values)

Type

Description

uint256

The variable rate slope

#### getBaseVariableBorrowRate

[](#view-methods-getbasevariableborrowrate)

```
function getBaseVariableBorrowRate(address reserve) external view override returns (uint256)
```

Returns the base variable borrow rate for the specified reserve.

##### Input Parameters:

[](#view-methods-getbasevariableborrowrate-input-parameters)

Name

Type

Description

reserve

address

The address of the reserve

##### Return Values:

[](#view-methods-getbasevariableborrowrate-return-values)

Type

Description

uint256

The base variable borrow rate, expressed in ray

#### getMaxVariableBorrowRate

[](#view-methods-getmaxvariableborrowrate)

```
function getMaxVariableBorrowRate(address reserve) external view override returns (uint256)
```

Returns the maximum variable borrow rate for the specified reserve.

##### Input Parameters:

[](#view-methods-getmaxvariableborrowrate-input-parameters)

Name

Type

Description

reserve

address

The address of the reserve

##### Return Values:

[](#view-methods-getmaxvariableborrowrate-return-values)

Type

Description

uint256

The maximum variable borrow rate, expressed in ray

#### calculateInterestRates

[](#view-methods-calculateinterestrates)

```
function calculateInterestRates(    DataTypes.CalculateInterestRatesParams memory params) external view override returns (uint256, uint256)
```

Calculates the interest rates depending on the reserve's state and configurations. This function returns only two values: the liquidity rate and the variable borrow rate.

##### Input Parameters:

[](#view-methods-calculateinterestrates-input-parameters)

Name

Type

Description

params

DataTypes.CalculateInterestRatesParams

The parameters needed to calculate interest rates

The DataTypes.CalculateInterestRatesParams struct is composed of the following fields:

Name

Type

Description

unbacked

uint256

The amount of unbacked tokens

liquidityAdded

uint256

The liquidity added during the operation

liquidityTaken

uint256

The liquidity taken during the operation

totalDebt

uint256

The total borrowed from the reserve

reserveFactor

uint256

The reserve portion of the interest that goes to the treasury of the market

reserve

address

The address of the reserve

usingVirtualBalance

bool

Flag to indicate if the virtual balance is being used

virtualUnderlyingBalance

uint256

The virtual balance of underlying asset used for mintable assets

##### Return Values:

[](#view-methods-calculateinterestrates-return-values)

Name

Type

Description

liquidityRate

uint256

The liquidity rate, expressed in ray

variableBorrowRate

uint256

The variable borrow rate, expressed in ray

[

Previous

**Tokenization**

](/docs/developers/smart-contracts/tokenization)[

Next

**Access Control Manager**

](/docs/developers/smart-contracts/acl-manager)

---

<a id="doc_26"></a>

## 📁 developers/smart_contracts / L2 Pool | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/l2_pool.md*

Source: https://aave.com/docs/developers/smart-contracts/l2-pool

## L2Pool

[](#l2pool)

The main transaction cost on L2 comes from calldata. To minimize this cost, Aave V3 uses a different contract on L2 networks that allows calldata of Pool methods to be compressed.

L2Pool is the contract for the L2 optimized user facing methods of the protocol that takes byte encoded input arguments. It exposes the liquidity management methods that can be invoked using either Solidity or Web3 libraries. The L2Pool contract is a calldata optimized extension of the Pool contract allowing users to pass compact calldata representation to reduce transaction costs on L2 rollups.

Pool methods not exposed in L2Pool.sol (such as flashLoan, setUserEMode etc.) are the same on L2 as on other versions of protocol. Refer to [Pool](/docs/developers/smart-contracts/pool) docs for the rest of the methods.

Since there are a limited set of supported assets that are already given an individual id, we use the 16 bit asset id in the encoded arguments instead of 160 bit asset address.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/pool/L2Pool.sol).

Threre is an additional [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract with view methods to encode transaction params for compressed methods.

### Methods

[](#methods)

#### supply

[](#methods-supply)

```
function supply(bytes32 args) external override
```

Calldata efficient wrapper of the supply function on behalf of the caller. Supplies asset into the protocol, minting the same amount of corresponding aTokens, and transferring them to msg.sender.

You can use data returned from encodeSupplyParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.

##### Input Parameters:

[](#methods-supply-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the supply function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 144-159: uint16 referralCode - used for 3rd party integrations

#### supplyWithPermit

[](#methods-supplywithpermit)

```
function supplyWithPermit(bytes32 args, bytes32 r, bytes32 s) external override
```

Calldata efficient wrapper of the supplyWithPermit function on behalf of the caller. Supply with transfer approval of supplied asset via permit function. This method removes the need for separate approval transaction before supplying asset to the pool.

You can use data returned from encodeSupplyWithPermitParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.

##### Input Parameters:

[](#methods-supplywithpermit-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the supply function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 144-159: uint16 referralCode - used for 3rd party integrations  
bit 160-191: uint32 shortenedDeadline - shortened deadline from the original uint256  
bit 192-199: uint8 permitV - the V parameter of ERC712 permit signature

r

bytes32

The R parameter of ERC712 permit signature

s

bytes32

The S parameter of ERC712 permit signature

#### withdraw

[](#methods-withdraw)

```
function withdraw(bytes32 args) external override returns (uint256)
```

Calldata efficient wrapper of the withdraw function, withdrawing to the caller. Withdraws amount of the underlying asset, i.e. redeems the underlying token and burns the aTokens.

If the user has any existing debt backed by the underlying token, the maximum amount available to withdraw is the amount that will not leave the user with a health factor < 1 after the withdrawal.

You can use data returned from encodeWithdrawParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.

##### Input Parameters:

[](#methods-withdraw-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the withdraw function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max

##### Return Value:

[](#methods-withdraw-return-value)

Name

Type

Description

amount

uint256

The final amount of the underlying asset withdrawn, denominated in the base unit of the asset (e.g., wei for ETH, smallest unit for ERC-20 tokens). This is the amount actually transferred to the caller, accounting for constraints like liquidity and health factor.

#### borrow

[](#methods-borrow)

```
function borrow(bytes32 args) external override
```

Calldata efficient wrapper of the borrow function, borrowing on behalf of the caller. Borrows amount of asset with interestRateMode, sending the amount to msg.sender, with the debt being incurred by onBehalfOf.

You can use data returned from encodeBorrowParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.

##### Input Parameters:

[](#methods-borrow-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the borrow function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 144 - 151: uint8 shortenedInterestRateMode  
bit 152 - 167: uint16 referralCode - used for 3rd party integrations

#### repay

[](#methods-repay)

```
function repay(bytes32 args) external override returns (uint256)
```

Calldata efficient wrapper of the repay function, repaying on behalf of the caller. Repays debt of an asset for the given interestRateMode.

You can use data returned from encodeRepayParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.

##### Input Parameters:

[](#methods-repay-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the repay function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 144 - 151: uint8 shortenedInterestRateMode

##### Return Values:

[](#methods-repay-return-values)

Type

Description

uint256

The final amount repaid

#### repayWithPermit

[](#methods-repaywithpermit)

```
function repayWithPermit(bytes32 args, bytes32 r, bytes32 s) external override returns (uint256)
```

Calldata efficient wrapper of the repayWithPermit function, repaying on behalf of the caller. Repay with transfer approval of borrowed asset via permit function. This method removes the need for separate approval transaction before repaying asset to the pool.

You can use data returned from encodeRepayWithPermitParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.​

##### Input Parameters:

[](#methods-repaywithpermit-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the repayWithPermit function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 144 - 151: uint8 shortenedInterestRateMode  
bit 152-183: uint32 shortenedDeadline - shortened deadline from original uint256  
bit 184-191: uint8 permitV - the V parameter of ERC712 permit signature

r

bytes32

The R parameter of ERC712 permit signature

s

bytes32

The S parameter of ERC712 permit signature

##### Return Values:

[](#methods-repaywithpermit-return-values)

Type

Description

uint256

The final amount repaid

#### repayWithATokens

[](#methods-repaywithatokens)

```
function repayWithATokens(bytes32 args) external override returns (uint256)
```

Calldata efficient wrapper of the repayWithATokens function. Allows user to repay with aTokens of the underlying debt asset without any approvals, for example, Pay DAI debt using aDAI tokens.

You can use data data returned from encodeRepayWithATokensParams() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.

##### Input Parameters:

[](#methods-repaywithatokens-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the repayWithATokens function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16-143: uint128 shortenedAmount - cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 144 - 151: uint8 shortenedInterestRateMode

##### Return Values:

[](#methods-repaywithatokens-return-values)

Type

Description

uint256

The final amount repaid

#### setUserUseReserveAsCollateral

[](#methods-setuserusereserveascollateral)

```
function setUserUseReserveAsCollateral(bytes32 args) external override
```

Calldata efficient wrapper of the setUserUseReserveAsCollateral function. Sets the asset of msg.sender to be used as collateral or not.

You can use data returned from encodeSetUserUseReserveAsCollateral() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.​

##### Input Parameters:

[](#methods-setuserusereserveascollateral-input-parameters)

Name

Type

Description

args

bytes32

Arguments for the setUserUseReserveAsCollateral function packed in one bytes32  
bit 0-15: uint16 assetId - the index of the asset in the reservesList  
bit 16: 0 => enable useAsCollateral, 1 => disable useAsCollateral

#### liquidationCall

[](#methods-liquidationcall)

```
function liquidationCall(bytes32 args1, bytes32 args2) external override
```

Calldata efficient wrapper of the liquidationCall function. Liquidate positions with a health factor below 1.

You can use data returned from encodeLiquidationCall() method in [L2Encoder](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/L2Encoder.sol) helper contract to pass to this method.​

##### Input Parameters:

[](#methods-liquidationcall-input-parameters)

Name

Type

Description

args1

bytes32

Part of the arguments for the liquidationCall function packed in one bytes32  
bit 0-15: uint16 collateralAssetId - the index of the collateral asset in the reservesList  
bit 16-31: uint16 debtAssetId - the index of the debt asset in the reservesList  
bit 32-191: address of the user being liquidated

args2

bytes32

Part of the arguments for the liquidationCall function packed in one bytes32  
bit 0-127: uint128 shortenedDebtToCover is cast to 256 bits at decode time, if type(uint128).max the value will be expanded to type(uint256).max  
bit 128: receiveAToken - 0 => receive aToken, 1 => receive underlying asset

[

Previous

**Pool**

](/docs/developers/smart-contracts/pool)[

Next

**Wrapped Token Gateway**

](/docs/developers/smart-contracts/wrapped-token-gateway)

---

<a id="doc_27"></a>

## 📁 developers/smart_contracts / Oracles | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/oracles.md*

Source: https://aave.com/docs/developers/smart-contracts/oracles

## AaveOracle

[](#aaveoracle)

Contract to get asset prices and manage price sources.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/misc/AaveOracle.sol).

This contract is owned by the Aave Governance.

### Write Methods

[](#write-methods)

#### setAssetSources

[](#write-methods-setassetsources)

```
function setAssetSources(address[] calldata assets, address[] calldata sources) external override onlyAssetListingOrPoolAdmins
```

Sets the price sources for given list of assets.

This method can only be called by a POOL\_ADMIN or ASSET\_LISTING\_ADMIN. Please look at the [ACLManager](/docs/developers/smart-contracts/acl-manager) contract for further details on system roles.

##### Input Parameters:

[](#write-methods-setassetsources-input-parameters)

Name

Type

Description

assets

address\[\]

The addresses of the assets for which source is being set

sources

address\[\]

The address of the source of each asset. Length of assets and sources array should be same

#### setFallbackOracle

[](#write-methods-setfallbackoracle)

```
function setFallbackOracle(address fallbackOracle) external override onlyAssetListingOrPoolAdmins
```

Sets/updates the fallbackOracle.

This method can only be called by a POOL\_ADMIN or ASSET\_LISTING\_ADMIN. Please look at the [ACLManager](/docs/developers/smart-contracts/acl-manager) contract for further details on system roles.

##### Input Parameters:

[](#write-methods-setfallbackoracle-input-parameters)

Name

Type

Description

fallbackOracle

address

The address of the fallback oracle

### View Methods

[](#view-methods)

#### getAssetPrice

[](#view-methods-getassetprice)

```
function getAssetPrice(address asset) public view override returns (uint256)
```

Returns the price of the supported asset in [BASE\_CURRENCY](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/interfaces/IPriceOracleGetter.sol) of the Aave Market in wei.

##### Input Parameters:

[](#view-methods-getassetprice-input-parameters)

Name

Type

Description

asset

address

The address of the asset

##### Return Values:

[](#view-methods-getassetprice-return-values)

Type

Description

uint256

The price of the asset in BASE\_CURRENCY of the Aave market in wei

#### getAssetsPrices

[](#view-methods-getassetsprices)

```
function getAssetsPrices(address[] calldata assets) external view override returns (uint256[] memory)
```

Returns a list of prices from a list of the supported assets addresses in [BASE\_CURRENCY](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/interfaces/IPriceOracleGetter.sol) of the Aave Market. All prices are in wei.

##### Input Parameters:

[](#view-methods-getassetsprices-input-parameters)

Name

Type

Description

assets

address\[\]

The list of assets addresses for which price is being queried

##### Return Values:

[](#view-methods-getassetsprices-return-values)

Type

Description

uint256\[\]

The prices of the given assets in BASE\_CURRENCY of the Aave market in wei

#### getSourceOfAsset

[](#view-methods-getsourceofasset)

```
function getSourceOfAsset(address asset) external view override returns (address)
```

Returns the address of the price source for an asset address.

##### Input Parameters:

[](#view-methods-getsourceofasset-input-parameters)

Name

Type

Description

asset

address

The address of the asset

##### Return Values:

[](#view-methods-getsourceofasset-return-values)

Type

Description

address

The address of the source

#### getFallbackOracle

[](#view-methods-getfallbackoracle)

```
function getFallbackOracle() external view returns (address)
```

Returns the address of the fallback oracle.

##### Return Values:

[](#view-methods-getfallbackoracle-return-values)

Type

Description

address

The address of the fallback oracle

## PriceOracleSentinel

[](#priceoraclesentinel)

The PriceOracleSentinel contract validates if the operations are allowed depending on the PriceOracle health.

This feature introduces a grace period for liquidations and disables borrowing under specific circumstances.

This feature has been specifically designed for L2s to handle eventual downtime of the sequencer (but can be extended to handle other cases, even on L1s, in the future).

Once the PriceOracle gets up after an outage or downtime, users can make their positions healthy during a grace period. The PriceOracle is considered healthy once its completely up and the grace period has passed.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/misc/PriceOracleSentinel.sol).

### Write Methods

[](#write-methods)

#### setSequencerOracle

[](#write-methods-setsequenceroracle)

```
function setSequencerOracle(address newSequencerOracle) external onlyPoolAdmin
```

Updates the address of the sequencer oracle.

This method can only be called by PoolAdmin.

This method can only be called by the *Role Admin*, specified by *Aave Governance*, responsible for managing the [POOL\_ADMIN](/docs/developers/smart-contracts/aclmanager#pool_admin) role.

##### Input Parameters:

[](#write-methods-setsequenceroracle-input-parameters)

Name

Type

Description

newSequencerOracle

address

The address of the new Sequencer Oracle to be set

#### setGracePeriod

[](#write-methods-setgraceperiod)

```
function setGracePeriod(uint256 newGracePeriod) public onlyRiskOrPoolAdmins
```

Updates the duration of the grace period.

Can only be called by PoolAdmin or RiskAdmin.

##### Input Parameters:

[](#write-methods-setgraceperiod-input-parameters)

Name

Type

Description

newGracePeriod

uint256

The duration of new grace period in seconds

### View Methods

[](#view-methods)

#### isBorrowAllowed

[](#view-methods-isborrowallowed)

```
function isBorrowAllowed() external view override returns (bool)
```

Returns true if the borrow operation is allowed. The operation is not allowed when PriceOracle is down or the grace period has not passed.

##### Return Values:

[](#view-methods-isborrowallowed-return-values)

Type

Description

bool

Returns true if the borrow operation is allowed (the PriceOracle is up and grace period has passed), false otherwise

#### isLiquidationAllowed

[](#view-methods-isliquidationallowed)

```
function isLiquidationAllowed() external view override returns (bool)
```

Returns true if the liquidation operation is allowed. The operation is not allowed when PriceOracle is down or the grace period has not passed.

##### Return Values:

[](#view-methods-isliquidationallowed-return-values)

Type

Description

bool

Returns true if the liquidation operation is allowed (the PriceOracle is up and grace period has passed), false otherwise

#### getSequencerOracle

[](#view-methods-getsequenceroracle)

```
function getSequencerOracle() external view returns (address)
```

Returns the SequencerOracle.

##### Return Values:

[](#view-methods-getsequenceroracle-return-values)

Type

Description

address

The address of the sequencer oracle contract

#### getGracePeriod

[](#view-methods-getgraceperiod)

```
function getGracePeriod() external view returns (uint256)
```

Returns the grace period.

##### Return Values:

[](#view-methods-getgraceperiod-return-values)

Type

Description

uint256

The duration of the grace period in seconds

[

Previous

**Access Control Manager**

](/docs/developers/smart-contracts/acl-manager)[

Next

**Pool Addresses Provider**

](/docs/developers/smart-contracts/pool-addresses-provider)

---

<a id="doc_28"></a>

## 📁 developers/smart_contracts / Pool Addresses Provider | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/pool_addresses_provider.md*

Source: https://aave.com/docs/developers/smart-contracts/pool-addresses-provider

## PoolAddressesProvider

[](#pooladdressesprovider)

The PoolAddressesProvider contract is the main registry of addresses that are part of, or connected to the Protocol, including permissioned roles. It acts as a factory of proxies and is the admin of those, and therefore has the right to change its implementations.

The addresses provider manages various protocol modules and has the ability to update pointers (e.g. update the [ACLManager](/docs/developers/smart-contracts/acl-manager) contract) or update the implementation of proxy contracts (e.g. update the [Pool](/docs/developers/smart-contracts/pool) implementation).

It specifies the initial holder of the [DEFAULT\_ADMIN\_ROLE](/docs/developers/smart-contracts/acl-manager), it is immutable, and the address will never change.

Whenever the [Pool](/docs/developers/smart-contracts/pool) contract is needed, we recommended you fetch the correct address from this PoolAddressesProvider smart contract.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/configuration/PoolAddressesProvider.sol).

This contract is owned by the [Aave Governance](https://governance.aave.com/).

### Write Methods

[](#write-methods)

#### setMarketId

[](#write-methods-setmarketid)

```
function setMarketId(string memory newMarketId) external override onlyOwner
```

Updates the identifier of the Aave market by associating an id with a specific PoolAddressesProvider. This can be used to create an on-chain registry of pool addresses providers to identify and validate multiple Aave markets.

##### Input Parameters:

[](#write-methods-setmarketid-input-parameters)

Name

Type

Description

newMarketId

string

The new id of the market

#### setAddress

[](#write-methods-setaddress)

```
function setAddress(bytes32 id, address newAddress) external override onlyOwner
```

Sets the address of the protocol contract stored at the given id, replacing the address saved in the addresses map.

For example, utils.keccak256(utils.toUtf8Bytes("INCENTIVES\_CONTROLLER")), is set to the address of INCENTIVES\_CONTROLLER.

Use this function carefully, as it will do a hard replacement of the current address in the addresses map.

##### Input Parameters:

[](#write-methods-setaddress-input-parameters)

Name

Type

Description

id

bytes32

keccak256 hash of UTF8Bytes string representing contract

newAddress

address

The new address to be set corresponding to the id

#### setAddressAsProxy

[](#write-methods-setaddressasproxy)

```
function setAddressAsProxy(bytes32 id, address newImplementationAddress) external override onlyOwner
```

Updates the implementation address of a proxy contract with a specified id.

If there is no proxy registered, it will instantiate one and set the implementation as the newImplementationAddress.

Use this function carefully, only for ids that do not have an explicit setter function in order to avoid unexpected consequences.

##### Input Parameters:

[](#write-methods-setaddressasproxy-input-parameters)

Name

Type

Description

id

bytes32

The id of the proxy contract

newImplementationAddress

address

The address of new implementation contract corresponding to the proxy

#### setPoolImpl

[](#write-methods-setpoolimpl)

```
function setPoolImpl(address newPoolImpl) external override onlyOwner
```

Updates the implementation of the [Pool](/docs/developers/smart-contracts/pool) contract, or creates a proxy.

##### Input Parameters:

[](#write-methods-setpoolimpl-input-parameters)

Name

Type

Description

newPoolImpl

address

The address of new Pool implementation contract

#### setPoolConfiguratorImpl

[](#write-methods-setpoolconfiguratorimpl)

```
function setPoolConfiguratorImpl(address newPoolConfiguratorImpl) external override onlyOwner
```

Updates the implementation of the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract, or creates a proxy.

##### Input Parameters:

[](#write-methods-setpoolconfiguratorimpl-input-parameters)

Name

Type

Description

newPoolConfiguratorImpl

address

The address of new PoolConfigurator implementation contract

#### setPriceOracle

[](#write-methods-setpriceoracle)

```
function setPriceOracle(address newPriceOracle) external override onlyOwner
```

Updates the address of the price oracle.

##### Input Parameters:

[](#write-methods-setpriceoracle-input-parameters)

Name

Type

Description

newPriceOracle

address

The address of new price oracle

#### setACLManager

[](#write-methods-setaclmanager)

```
function setACLManager(address newAclManager) external override onlyOwner
```

Updates the address of the Access Control List Manager.

##### Input Parameters:

[](#write-methods-setaclmanager-input-parameters)

Name

Type

Description

newAclManager

address

The address of the new ACLManager

#### setACLAdmin

[](#write-methods-setacladmin)

```
function setACLAdmin(address newAclAdmin) external override onlyOwner
```

Updates the address of the Access Control List Admin.

##### Input Parameters:

[](#write-methods-setacladmin-input-parameters)

Name

Type

Description

newAclAdmin

address

The address of new ACLAdmin

#### setPriceOracleSentinel

[](#write-methods-setpriceoraclesentinel)

```
function setPriceOracleSentinel(address newPriceOracleSentinel) external override onlyOwner
```

Updates the address of the price oracle sentinel.

##### Input Parameters:

[](#write-methods-setpriceoraclesentinel-input-parameters)

Name

Type

Description

newPriceOracleSentinel

address

The address of new PriceOracleSentinel

#### setPoolDataProvider

[](#write-methods-setpooldataprovider)

```
function setPoolDataProvider(address newDataProvider) external override onlyOwner
```

Updates the address of the data provider.

##### Input Parameters:

[](#write-methods-setpooldataprovider-input-parameters)

Name

Type

Description

newDataProvider

address

The address of new DataProvider

### View Methods

[](#view-methods)

#### getMarketId

[](#view-methods-getmarketid)

```
function getMarketId() external view override returns (string memory)
```

Returns the market id of the associated Aave market.

##### Return Values:

[](#view-methods-getmarketid-return-values)

Type

Description

string

A string representation of the market id

#### getAddress

[](#view-methods-getaddress)

```
function getAddress(bytes32 id) public view override returns (address)
```

Returns the address of protocol contract stored at the given id. The returned address might be an EOA or a contract, which may be proxied. It will return ZERO if there is no registered address with the given id.

##### Input Parameters:

[](#view-methods-getaddress-input-parameters)

Name

Type

Description

id

bytes32

The id. For example, the Protocol Data Provider uses id 0x1

##### Return Values:

[](#view-methods-getaddress-return-values)

Type

Description

address

The address associated with the id passed

##### Example:

[](#view-methods-getaddress-example)

```
// Get address of incentive controllerimport { utils } from "@ethers/lib/utils";
const id = utils.keccak256(utils.toUtf8Bytes("INCENTIVES_CONTROLLER"));const address = poolAddressProvider.getAddress(id);
```

#### getPool

[](#view-methods-getpool)

```
function getPool() external view override returns (address)
```

Returns the address of the latest Pool proxy contract.

##### Return Values:

[](#view-methods-getpool-return-values)

Type

Description

address

The address of the associated Pool proxy

#### getPoolConfigurator

[](#view-methods-getpoolconfigurator)

```
function getPoolConfigurator() external view override returns (address)
```

Returns the address of the PoolConfigurator proxy. Used for configuration methods, like init reserves or update token implementation etc, of the market.

##### Return Values:

[](#view-methods-getpoolconfigurator-return-values)

Type

Description

address

The PoolConfigurator proxy address

#### getPriceOracle

[](#view-methods-getpriceoracle)

```
function getPriceOracle() external view override returns (address)
```

Returns the address of the Price Oracle used by the market.

##### Return Values:

[](#view-methods-getpriceoracle-return-values)

Type

Description

address

The address of the price oracle used by the associated market

#### getACLManager

[](#view-methods-getaclmanager)

```
function getACLManager() external view override returns (address)
```

Returns the address of the Access Control List Manager (ACLManager) that manages the system role of the market.

##### Return Values:

[](#view-methods-getaclmanager-return-values)

Type

Description

address

The address of the ACLManger contract managing the system role of the associated market

#### getACLAdmin

[](#view-methods-getacladmin)

```
function getACLAdmin() external view override returns (address)
```

Returns the address of the Access Control List Admin (ACLAdmin) of the market which holds the DEFAULT\_ADMIN\_ROLE in ACLManager.

##### Return Values:

[](#view-methods-getacladmin-return-values)

Type

Description

address

The address of the Access Control List admin of the associated market

#### getPriceOracleSentinel

[](#view-methods-getpriceoraclesentinel)

```
function getPriceOracleSentinel() external view override returns (address)
```

Returns the address of the price oracle sentinel.

##### Return Values:

[](#view-methods-getpriceoraclesentinel-return-values)

Type

Description

address

The address of the PriceOracleSentinel of the associated market

#### getPoolDataProvider

[](#view-methods-getpooldataprovider)

```
function getPoolDataProvider() external view override returns (address)
```

Returns the address of latest pool data provider.

##### Return Values:

[](#view-methods-getpooldataprovider-return-values)

Type

Description

address

The address of the pool data provider of the associated market

[

Previous

**Oracles**

](/docs/developers/smart-contracts/oracles)[

Next

**Pool Configurator**

](/docs/developers/smart-contracts/pool-configurator)

---

<a id="doc_29"></a>

## 📁 developers/smart_contracts / Pool Configurator | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/pool_configurator.md*

Source: https://aave.com/docs/developers/smart-contracts/pool-configurator

## Pool Configurator

[](#pool-configurator)

The PoolConfigurator contract implements the configuration methods for the Aave Protocol. The 'write methods' below are grouped by permissioned system roles that are managed by [ACLManager](/docs/developers/smart-contracts/acl-manager).

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/pool/PoolConfigurator.sol).

### Write Methods

[](#write-methods)

### Only Asset Listing Or Pool Admins Methods

[](#only-asset-listing-or-pool-admins-methods)

#### initReserves

[](#only-asset-listing-or-pool-admins-methods-initreserves)

```
function initReserves(ConfiguratorInputTypes.InitReserveInput[] calldata input) external override onlyAssetListingOrPoolAdmins
```

Initializes multiple reserves using the array of initialization parameters as input.

##### Input Parameters:

[](#only-asset-listing-or-pool-admins-methods-initreserves-input-parameters)

Name

Type

Description

input

ConfiguratorInputTypes.InitReserveInput\[\]

The array of initialization parameters

The [ConfiguratorInputTypes.InitReserveInput\[\]](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/types/ConfiguratorInputTypes.sol) struct is composed of the following fields:

Name

Type

Description

aTokenImpl

address

The address of the aToken contract implementation

variableDebtTokenImpl

address

The address of the variable debt token contract

useVirtualBalance

bool

true if reserve is utilising virtual balance accounting

interestRateStrategyAddress

address

The address of the interest rate strategy contract for this reserve

underlyingAsset

address

The address of the underlying asset

treasury

address

The address of the treasury

incentivesController

address

The address of the incentives controller for this aToken

aTokenName

string

The name of the aToken

aTokenSymbol

string

The symbol of the aToken

variableDebtTokenName

string

The name of the variable debt token

variableDebtTokenSymbol

string

The symbol of the variable debt token

params

bytes

A set of encoded parameters for additional initialization

interestRateData

bytes

Encoded interest rate strategy data

### Only Emergency Admin Methods

[](#only-emergency-admin-methods)

#### setPoolPause

[](#only-emergency-admin-methods-setpoolpause)

```
function setPoolPause(bool paused) external override onlyEmergencyOrPoolAdmin
```

Pauses or unpauses all the protocol reserves. In the paused state all the protocol interactions are suspended.

##### Input Parameters:

[](#only-emergency-admin-methods-setpoolpause-input-parameters)

Name

Type

Description

paused

bool

true if the protocol needs to be paused, otherwise false

### Only Emergency Or Pool Admin Methods

[](#only-emergency-or-pool-admin-methods)

#### setReservePause

[](#only-emergency-or-pool-admin-methods-setreservepause)

```
function setReservePause(address asset, bool paused) public override onlyEmergencyOrPoolAdmin
```

Pauses a reserve. A paused reserve does not allow any interaction (supply, borrow, repay, liquidate, atoken transfers).

##### Input Parameters:

[](#only-emergency-or-pool-admin-methods-setreservepause-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

paused

bool

true if pausing the reserve, false if unpausing the reserve

### Only Pool Admin Methods

[](#only-pool-admin-methods)

#### dropReserve

[](#only-pool-admin-methods-dropreserve)

```
function dropReserve(address asset) external override onlyPoolAdmin
```

Drops a reserve entirely.

##### Input Parameters:

[](#only-pool-admin-methods-dropreserve-input-parameters)

Name

Type

Description

asset

address

The address of the reserve to drop

#### updateAToken

[](#only-pool-admin-methods-updateatoken)

```
function updateAToken(ConfiguratorInputTypes.UpdateATokenInput calldata input) external override onlyPoolAdmin
```

Updates the aToken implementation for the reserve. Takes the aToken update parameters as input.

##### Input Parameters:

[](#only-pool-admin-methods-updateatoken-input-parameters)

Name

Type

Description

input

ConfiguratorInputTypes.UpdateATokenInput

The aToken update parameters

The [ConfiguratorInputTypes.UpdateATokenInput](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/types/ConfiguratorInputTypes.sol) struct is composed of the following fields:

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

treasury

address

The address of the treasury

incentivesController

address

The address of the incentives controller for this aToken

name

string

The name of the aToken

symbol

string

The symbol of the aToken

implementation

address

The new aToken implementation

params

bytes

A set of encoded parameters for additional initialization

#### updateVariableDebtToken

[](#only-pool-admin-methods-updatevariabledebttoken)

```
function updateVariableDebtToken(ConfiguratorInputTypes.UpdateDebtTokenInput calldata input) external override onlyPoolAdmin
```

##### Input Parameters:

[](#only-pool-admin-methods-updatevariabledebttoken-input-parameters)

Name

Type

Description

input

ConfiguratorInputTypes.UpdateDebtTokenInput

The variableDebtToken update parameters

The [ConfiguratorInputTypes.UpdateDebtTokenInput](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/types/ConfiguratorInputTypes.sol) struct is composed of the following fields:

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

incentivesController

address

The address of the incentives controller for this variableDebtToken

name

string

The name of the variableDebtToken

symbol

string

The symbol of the variableDebtToken

implementation

address

The new variableDebtToken implementation

params

bytes

A set of encoded parameters for additional initialization

#### setReserveActive

[](#only-pool-admin-methods-setreserveactive)

```
function setReserveActive(address asset, bool active) external override onlyPoolAdmin
```

Activate or deactivate a reserve.

##### Input Parameters:

[](#only-pool-admin-methods-setreserveactive-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

active

bool

true if the reserve needs to be active, false otherwise

#### updateBridgeProtocolFee

[](#only-pool-admin-methods-updatebridgeprotocolfee)

```
function updateBridgeProtocolFee(uint256 newBridgeProtocolFee) external override onlyPoolAdmin
```

Updates the bridge fee collected by the protocol reserves.

##### Input Parameters:

[](#only-pool-admin-methods-updatebridgeprotocolfee-input-parameters)

Name

Type

Description

newBridgeProtocolFee

uint256

The part of the fee sent to the protocol treasury, expressed in bps

#### setReserveFlashLoaning

[](#only-pool-admin-methods-setreserveflashloaning)

```
function setReserveFlashLoaning(address asset, bool enabled) external override onlyRiskOrPoolAdmins
```

Enables or disables flash loans for a reserve.

##### Input Parameters:

[](#only-pool-admin-methods-setreserveflashloaning-input-parameters)

Name

Type

Description

asset

address

Address of the reserve asset

enabled

bool

true to enable, false to disable

#### updateFlashloanPremiumTotal

[](#only-pool-admin-methods-updateflashloanpremiumtotal)

```
function updateFlashloanPremiumTotal(uint128 newFlashloanPremiumTotal) external override onlyPoolAdmin
```

Updates the total flash loan premium. The premium is calculated on the total amount borrowed, and is expressed in bps.

The total flash loan premium consists of two parts:

*   A part is sent to aToken holders as extra balance, and
    
*   A part is collected by the protocol reserves.
    

##### Input Parameters:

[](#only-pool-admin-methods-updateflashloanpremiumtotal-input-parameters)

Name

Type

Description

newFlashloanPremiumTotal

uint128

The total flashloan premium

#### updateFlashloanPremiumToProtocol

[](#only-pool-admin-methods-updateflashloanpremiumtoprotocol)

```
function updateFlashloanPremiumToProtocol(uint128 newFlashloanPremiumToProtocol) external override onlyPoolAdmin
```

Updates the flash loan premium collected by protocol reserves. The premium to protocol is calculated on the total flashloan premium, and is expressed in bps.

##### Input Parameters:

[](#only-pool-admin-methods-updateflashloanpremiumtoprotocol-input-parameters)

Name

Type

Description

newFlashloanPremiumToProtocol

uint128

The part of the flashloan premium sent to the protocol treasury

### Only Risk Or Pool Admins Methods

[](#only-risk-or-pool-admins-methods)

#### setReserveBorrowing

[](#only-risk-or-pool-admins-methods-setreserveborrowing)

```
function setReserveBorrowing(address asset, bool enabled) external override onlyRiskOrPoolAdmins
```

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setreserveborrowing-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

enabled

bool

true if borrowing needs to be enabled, false otherwise

#### configureReserveAsCollateral

[](#only-risk-or-pool-admins-methods-configurereserveascollateral)

```
function configureReserveAsCollateral(    address asset,    uint256 ltv,    uint256 liquidationThreshold,    uint256 liquidationBonus) external override onlyRiskOrPoolAdmins
```

Configures the reserve collateralization parameters. All the values are expressed in bps. A value of 10000 results in 100.00%. The liquidationBonus is always above 100%. A value of 105% means the liquidator will receive a 5% bonus.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-configurereserveascollateral-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

ltv

uint256

The loan to value of the asset when used as collateral

liquidationThreshold

uint256

The threshold at which loans using this asset as collateral will be considered undercollateralized

liquidationBonus

uint256

The bonus liquidators receive to liquidate this asset

#### setReserveFreeze

[](#only-risk-or-pool-admins-methods-setreservefreeze)

```
function setReserveFreeze(address asset, bool freeze) external override onlyRiskOrPoolAdmins
```

Freeze or unfreeze a reserve. A frozen reserve doesn't allow any new supply or borrow but allows repayments, liquidations, rate rebalances and withdrawals.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setreservefreeze-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

freeze

bool

true if the reserve needs to be frozen, false otherwise

#### setBorrowableInIsolation

[](#only-risk-or-pool-admins-methods-setborrowableinisolation)

```
function setBorrowableInIsolation(address asset, bool borrowable) external override onlyRiskOrPoolAdmins
```

Sets the borrowable in isolation flag for the reserve. When this flag is set to true, the asset will be borrowable against isolated collaterals and the borrowed amount will be accumulated in the isolated collateral's total debt exposure. Only assets of the same family (e.g. USD stablecoins) should be borrowable in isolation mode to keep consistency in the debt ceiling calculations.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setborrowableinisolation-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

borrowable

bool

true if the asset should be borrowable in isolation, false otherwise

#### setReserveFactor

[](#only-risk-or-pool-admins-methods-setreservefactor)

```
function setReserveFactor(address asset, uint256 newReserveFactor) external override onlyRiskOrPoolAdmins
```

Updates the reserve factor of a reserve.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setreservefactor-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newReserveFactor

uint256

The new reserve factor of the reserve

#### setDebtCeiling

[](#only-risk-or-pool-admins-methods-setdebtceiling)

```
function setDebtCeiling(address asset, uint256 newDebtCeiling) external override onlyRiskOrPoolAdmins
```

Sets the debt ceiling for an asset.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setdebtceiling-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newDebtCeiling

uint256

The new debt ceiling

#### setSiloedBorrowing

[](#only-risk-or-pool-admins-methods-setsiloedborrowing)

```
function setSiloedBorrowing(address asset, bool newSiloed) external override onlyRiskOrPoolAdmins
```

Sets siloed borrowing for an asset

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setsiloedborrowing-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newSiloed

bool

The new siloed borrowing state - enable or disable siloed borrowing for the reserve

#### setBorrowCap

[](#only-risk-or-pool-admins-methods-setborrowcap)

```
function setBorrowCap(address asset, uint256 newBorrowCap) external override onlyRiskOrPoolAdmins
```

Updates the borrow cap of a reserve. Allows [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager) and [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager) to add/update cap on the total borrow that can be borrowed from the reserve. Once the borrow cap is reached, no more borrow positions for the given reserve asset can be initiated.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setborrowcap-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newBorrowCap

uint256

The new borrow cap of the reserve in whole tokens. A borrow cap of 0 signifies that there is no cap

#### setSupplyCap

[](#only-risk-or-pool-admins-methods-setsupplycap)

```
function setSupplyCap(address asset, uint256 newSupplyCap) external override onlyRiskOrPoolAdmins
```

Updates the supply cap of a reserve. Allows [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager) and [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager) to add/update liquidity supply cap on the reserve. Once the supply cap is reached, no more liquidity for the given reserve asset can be supplied to the pool.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setsupplycap-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newSupplyCap

uint256

The new supply cap of the reserve in whole tokens. A supply cap of 0 signifies that there is no cap

#### disableLiquidationGracePeriod

[](#only-risk-or-pool-admins-methods-disableliquidationgraceperiod)

```
function disableLiquidationGracePeriod(address asset) external override onlyEmergencyOrPoolAdmin
```

Disables the liquidation grace period for a reserve.

##### Input Parameters

[](#only-risk-or-pool-admins-methods-disableliquidationgraceperiod-input-parameters)

Name

Type

Description

asset

address

Address of the reserve asset

#### setLiquidationProtocolFee

[](#only-risk-or-pool-admins-methods-setliquidationprotocolfee)

```
function setLiquidationProtocolFee(address asset, uint256 newFee) external override onlyRiskOrPoolAdmins
```

Updates the liquidation protocol fee of reserve.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setliquidationprotocolfee-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newFee

uint256

The new liquidation protocol fee of the reserve, expressed in bps

#### setEModeCategory

[](#only-risk-or-pool-admins-methods-setemodecategory)

```
function setEModeCategory(    uint8 categoryId,    uint16 ltv,    uint16 liquidationThreshold,    uint16 liquidationBonus,    string calldata label) external override onlyRiskOrPoolAdmins
```

Adds a new efficiency mode (eMode) category. Allows [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager) and [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager) to configure existing or add new eModeCategory

If zero is provided as oracle address, the default asset oracles will be used to compute the overall debt and overcollateralization of the users using this category. The new ltv and liquidation threshold must be greater than the base ltvs and liquidation thresholds of all assets within the eMode category.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setemodecategory-input-parameters)

Name

Type

Description

categoryId

uint8

The id of the category to be configured. categoryId ≠ 0. NOTE: category 0 is reserved for the default category i.e. non-eMode

ltv

uint16

The loan to value for the associated eMode category. It must be less than or equal to the liquidationThreshold

liquidationThreshold

uint16

The liquidation threshold associated with the category

liquidationBonus

uint16

The liquidation bonus associated with the category

label

string

A custom label identifying the category

#### setAssetCollateralInEMode

[](#only-risk-or-pool-admins-methods-setassetcollateralinemode)

```
function setAssetCollateralInEMode(address asset, uint8 categoryId, bool allowed) external override onlyRiskOrPoolAdmins
```

Assign collateral status to an asset for a particular efficiency mode (eMode) category. Allows [RISK\_ADMIN](/docs/developers/smart-contracts/acl-manager) and [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager) to configure eModeCategory of an asset.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setassetcollateralinemode-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

categoryId

uint8

eMode category id to set asset collateral status for

allowed

bool

true if asset is enabled as collateral in designated categoryId

#### setAssetBorrowableInEMode

[](#only-risk-or-pool-admins-methods-setassetborrowableinemode)

```
function setAssetBorrowableInEMode(address asset, uint8 categoryId, bool borrowable) external override onlyRiskOrPoolAdmins
```

Configures if an asset can be borrowed in a specific eMode category.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setassetborrowableinemode-input-parameters)

Name

Type

Description

asset

address

Address of the reserve asset

categoryId

uint8

eMode category ID

borrowable

bool

true to enable, false to disable

#### setUnbackedMintCap

[](#only-risk-or-pool-admins-methods-setunbackedmintcap)

```
function setUnbackedMintCap(address asset, uint256 newUnbackedMintCap) external override onlyRiskOrPoolAdmins
```

Updates the unbacked mint cap of reserve.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setunbackedmintcap-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

newUnbackedMintCap

uint256

The new unbacked mint cap of the reserve

#### setReserveInterestRateData

[](#only-risk-or-pool-admins-methods-setreserveinterestratedata)

```
function setReserveInterestRateData(address asset, bytes calldata rateData) external onlyRiskOrPoolAdmins
```

Sets custom interest rate parameters for a reserve.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setreserveinterestratedata-input-parameters)

Name

Type

Description

asset

address

Address of the reserve asset

rateData

bytes

Encodes rate strategy parameters

#### setReserveInterestRateStrategyAddress

[](#only-risk-or-pool-admins-methods-setreserveinterestratestrategyaddress)

```
function setReserveInterestRateStrategyAddress(address asset, address rateStrategyAddress, bytes calldata rateData) external override onlyRiskOrPoolAdmins
```

Sets the interest rate strategy of a reserve.

##### Input Parameters:

[](#only-risk-or-pool-admins-methods-setreserveinterestratestrategyaddress-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

rateStrategyAddress

address

The address of the interest strategy contract

rateData

bytes

Encoded interst rate strategy data

### Pure Methods

[](#pure-methods)

#### getRevision

[](#pure-methods-getrevision)

```
function getRevision() internal pure virtual override returns (uint256)
```

Returns the revision number of the contract. Needs to be defined in the inherited class as a constant.

Returns 0x1.

##### Return Values:

[](#pure-methods-getrevision-return-values)

Type

Description

uint256

The revision number

[

Previous

**Pool Addresses Provider**

](/docs/developers/smart-contracts/pool-addresses-provider)[

Next

**Switch Adapters**

](/docs/developers/smart-contracts/switch-adapters)

---

<a id="doc_30"></a>

## 📁 developers/smart_contracts / Pool | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/pool.md*

Source: https://aave.com/docs/developers/smart-contracts/pool

## Pool

[](#pool)

This contract is the main user-facing contract. Most user interactions with the Aave Protocol occur via the Pool contract. It exposes the liquidity management methods that can be invoked using either ***Solidity*** or ***Web3*** libraries.

Pool.sol allows users to:

*   Supply
    
*   Withdraw
    
*   Borrow
    
*   Repay
    
*   Enable/disable supplied assets as collateral
    
*   Liquidate positions
    
*   Execute Flash Loans
    

Pool is covered by a proxy contract and is owned by the [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider) of the specific market. All admin functions are callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract defined in the [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider).

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/pool/Pool.sol).

### Write Methods

[](#write-methods)

#### initialize

[](#write-methods-initialize)

```
function initialize(IPoolAddressesProvider provider) external virtual
```

Initializes the Pool.

Function is invoked by the proxy contract when the Pool contract is added to the [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider) of the market.

Caches the address of the [PoolAddressesProvider](/docs/developers/smart-contracts/pool-addresses-provider) in order to reduce gas consumption on subsequent operations.

##### Input Parameters:

[](#write-methods-initialize-input-parameters)

Name

Type

Description

provider

address

The address of the PoolAddressesProvider

#### supply

[](#write-methods-supply)

```
function supply(    address asset,    uint256 amount,    address onBehalfOf,    uint16 referralCode) public virtual override
```

Supplies a certain amount of an asset into the protocol, minting the same amount of corresponding aTokens and transferring them to the onBehalfOf address. For example, if a user supplies 100 USDC and onBehalfOf address is the same as msg.sender, they will get 100 aUSDC in return.

The referralCode is emitted in Supply event and can be for third-party referral integrations. To activate the referral feature and obtain a unique referral code, integrators need to submit a proposal to Aave Governance.

When supplying, the Pool contract must have allowance() to spend funds on behalf of msg.sender for at least the amount for the asset being supplied. This can be done via the standard ERC20 approve() method on the underlying token contract.

Referral supply is currently inactive, you can pass 0 as referralCode. This program may be activated in the future through an Aave governance proposal.

##### Input Parameters:

[](#write-methods-supply-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset being supplied to the pool

amount

uint256

The amount of asset to be supplied

onBehalfOf

address

The address that will receive the corresponding aTokens. This is the only address that will be able to withdraw the asset from the pool. This will be the same as msg.sender if the user wants to receive aTokens into their own wallet, or use a different address if the beneficiary of aTokens is a different wallet

referralCode

uint16

Referral supply is currently inactive, you can pass 0. This code is used to register the integrator originating the operation, for potential rewards. 0 if the action is executed directly by the user, without any middle-men

#### supplyWithPermit

[](#write-methods-supplywithpermit)

```
function supplyWithPermit(    address asset,    uint256 amount,    address onBehalfOf,    uint16 referralCode,    uint256 deadline,    uint8 permitV,    bytes32 permitR,    bytes32 permitS) public virtual override
```

Supply with transfer approval of the asset to be supplied via permit function. This method removes the need for separate approval tx before supplying asset to the pool. See: [https://eips.ethereum.org/EIPS/eip-2612](https://eips.ethereum.org/EIPS/eip-2612).

Permit signature must be signed by msg.sender with spender as Pool address.

Referral program is currently inactive, you can pass 0 as referralCode. This program may be activated in the future through an Aave governance proposal.

##### Input Parameters:

[](#write-methods-supplywithpermit-input-parameters)

Name

Type

Description

asset

address

The address of underlying asset being supplied. The same asset as used in permit v, s, and r

amount

uint256

The amount of asset to be supplied and signed for approval. The same amount as used in permit v, s, and r

onBehalfOf

address

The address that will receive the aTokens. This will be the same as msg.sender if the user wants to receive aTokens into their own wallet, or use a different address if the beneficiary of aTokens is a different wallet

referralCode

uint16

Referral supply is currently inactive, you can pass 0. This code is used to register the integrator originating the operation, for potential rewards. 0 if the action is executed directly by the user, without any middle-men

deadline

uint256

The unix timestamp up until which the permit signature is valid

permitV

uint8

The v parameter of the ERC712 permit signature

permitR

bytes32

The r parameter of the ERC712 permit signature

permitS

bytes32

The s parameter of the ERC712 permit signature

#### withdraw

[](#write-methods-withdraw)

```
function withdraw(address asset, uint256 amount, address to) public virtual override returns (uint256)
```

Withdraws an amount of underlying asset from the reserve, burning the equivalent aTokens owned. For example, if a user has 100 aUSDC and calls withdraw(), they will receive 100 USDC, burning the 100 aUSDC.

If user has any existing debt backed by the underlying token, then the maximum amount available to withdraw is the amount that will not leave user's health factor < 1 after withdrawal.

When withdrawing to another address, msg.sender should have aToken that will be burned by Pool.

Reserves with a Loan To Value parameter of 0% must be disabled as collateral (using Pool.setUserUseReserveAsCollateral or by fully withdrawing the supplied balance) before other assets can be withdrawn.

##### Input Parameters:

[](#write-methods-withdraw-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset to withdraw, not the aToken

amount

uint256

The underlying amount to be withdrawn (the amount supplied), expressed in wei units. Use type(uint).max to withdraw the entire aToken balance

to

address

The address that will receive the underlying asset. This will be the same as msg.sender if the user wants to receive the tokens into their own wallet, or use a different address if the beneficiary is a different wallet

##### Return Values:

[](#write-methods-withdraw-return-values)

Type

Description

uint256

The final amount withdrawn

#### borrow

[](#write-methods-borrow)

```
function borrow(    address asset,    uint256 amount,    uint256 interestRateMode,    uint16 referralCode,    address onBehalfOf) public virtual override
```

Allows users to borrow a specific amount of the reserve underlying asset, provided the borrower has already supplied enough collateral, or they were given enough allowance by a credit delegator on the corresponding debt token (VariableDebtToken). For example, if a user borrows 100 USDC passing their own address as onBehalfOf, they will receive 100 USDC into their wallet and 100 variable debt tokens.

NOTE: If onBehalfOf is not the same as msg.sender, then onBehalfOf must have supplied enough collateral via supply() and have delegated credit to msg.sender via approveDelegation().

Referral program is currently inactive, you can pass 0 as referralCode. This program may be activated in the future through an Aave governance proposal.

##### Input Parameters:

[](#write-methods-borrow-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset to borrow

amount

uint256

The amount to be borrowed, expressed in wei units

interestRateMode

uint256

Should always be passed a value of 2 (variable rate mode)

referralCode

uint16

Referral supply is currently inactive, you can pass 0. This code is used to register the integrator originating the operation, for potential rewards. 0 if the action is executed directly by the user, without any middle-men

onBehalfOf

address

This should be the address of the borrower calling the function if they want to borrow against their own collateral, or the address of the credit delegator if the caller has been given credit delegation allowance

#### repay

[](#write-methods-repay)

```
function repay(    address asset,    uint256 amount,    uint256 interestRateMode,    address onBehalfOf) public virtual override returns (uint256)
```

Repays a borrowed amount on a specific reserve, burning the equivalent debt tokens owned. For example, if a user repays 100 USDC, the 100 variable debt tokens owned by the onBehalfOf address will be burned.

When repaying, the Pool contract must have allowance to spend funds on behalf of msg.sender for at least the amount for the asset you are repaying with. This can be done via the standard ERC20 approve() method on the underlying token contract.

##### Input Parameters:

[](#write-methods-repay-input-parameters)

Name

Type

Description

asset

address

The address of the borrowed underlying asset previously borrowed

amount

uint256

The amount to repay, expressed in wei units. Use type(uint256).max in order to repay the whole debt, ONLY when the repayment is not executed on behalf of a 3rd party. In case of repayments on behalf of another user, it's recommended to send an amount slightly higher than the current borrowed amount

interestRateMode

uint256

Only available option is 2 (variableRateMode)

onBehalfOf

address

The address of the user who will get their debt reduced/removed. This should be the address of the user calling the function if they want to reduce/remove their own debt, or the address of any other borrower whose debt should be removed

#### repayWithPermit

[](#write-methods-repaywithpermit)

```
function repayWithPermit(    address asset,    uint256 amount,    uint256 interestRateMode,    address onBehalfOf,    uint256 deadline,    uint8 permitV,    bytes32 permitR,    bytes32 permitS) public virtual override returns (uint256)
```

Repay with transfer approval of the borrowed asset to be repaid, done via permit function. This method removes the need for separate approval tx before repaying asset to the pool. See: [https://eips.ethereum.org/EIPS/eip-2612](https://eips.ethereum.org/EIPS/eip-2612).

Permit signature must be signed by msg.sender with spender value as Pool address.

##### Input Parameters:

[](#write-methods-repaywithpermit-input-parameters)

Name

Type

Description

asset

address

The address of the borrowed underlying asset previously borrowed. The same asset as used in permit v, r, and s

amount

uint256

The amount to repay, expressed in wei units. Use type(uint256).max in order to repay the whole debt to pay without leaving aToken dust. The same amount as used in permit v,r,s

interestRateMode

uint256

Only available option is 2 (variableRateMode)

onBehalfOf

address

The address of the user who will get their debt reduced/removed. This should be the address of the user calling the function if they want to reduce/remove their own debt, or the address of any other borrower whose debt should be removed

deadline

uint256

The unix timestamp up until which the permit signature is valid

permitV

uint8

The v parameter of the ERC712 permit signature

permitR

bytes32

The r parameter of the ERC712 permit signature

permitS

bytes32

The s parameter of the ERC712 permit signature

##### Return Values:

[](#write-methods-repaywithpermit-return-values)

Type

Description

uint256

The final amount repaid

#### repayWithATokens

[](#write-methods-repaywithatokens)

```
function repayWithATokens(address asset, uint256 amount, uint256 interestRateMode) public virtual override returns (uint256)
```

Allows a user to repay a borrowed amount on a specific reserve using the reserve aTokens, burning the equivalent debt tokens. For example, a user repays 100 USDC using 100 aUSDC, burning 100 variable debt tokens. Passing uint256.maxas the amount will clean up any residual aToken dust balance, if the user aToken balance is not enough to cover the whole debt.

##### Input Parameters:

[](#write-methods-repaywithatokens-input-parameters)

Name

Type

Description

asset

address

The address of the borrowed underlying asset previously borrowed

amount

uint256

The amount to repay. Use type(uint256).max in order to repay the whole debt for asset to pay without leaving aToken dust

interestRateMode

uint256

Only available option is 2 (variableRateMode)

##### Return Values:

[](#write-methods-repaywithatokens-return-values)

Type

Description

uint256

The final amount repaid

#### setUserUseReserveAsCollateral

[](#write-methods-setuserusereserveascollateral)

```
function setUserUseReserveAsCollateral(address asset, bool useAsCollateral) public virtual override
```

Allows suppliers to enable/disable a specific supplied asset as collateral. Sets the asset of msg.sender to be used as collateral or not.

An asset in [Isolation Mode](/docs/developers/aave-v3) can be enabled to use as collateral only if no other asset is already enabled to use as collateral.

An asset with LTV parameter of 0% cannot be enabled as collateral.

The user won’t be able to disable an asset as collateral if they have an outstanding debt position which could be left with the Health Factor < HEALTH\_FACTOR\_LIQUIDATION\_THRESHOLD on disabling the given asset as collateral.

##### Input Parameters:

[](#write-methods-setuserusereserveascollateral-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset supplied

useAsCollateral

bool

true if the user wants to use the supply as collateral, false otherwise

#### liquidationCall

[](#write-methods-liquidationcall)

```
function liquidationCall(    address collateralAsset,    address debtAsset,    address user,    uint256 debtToCover,    bool receiveAToken) public virtual override
```

Function to liquidate a non-healthy position collateral-wise, with Health Factor below 1.

When the health factor of a position is below 1, the caller (liquidator) repays the debtToCover amount of debt of the user getting liquidated. This is part or all of the outstanding borrowed amount on behalf of the borrower. The caller then receives a proportional amount of the collateralAsset (discounted amount of collateral) plus a liquidation bonus to cover market risk.

Liquidators can decide if they want to receive an equivalent amount of collateral aTokens instead of the underlying asset. When the liquidation is completed successfully, the health factor of the position is increased, bringing the health factor above 1.

Liquidators can only close a certain amount of collateral defined by a close factor. Currently the **close factor is 0.5**. In other words, liquidators can only liquidate a maximum of 50% of the amount pending to be repaid in a position. The liquidation discount applies to this amount.

*   *In most scenarios*, profitable liquidators will choose to liquidate as much as they can (50% of the user position).
    
*   debtToCover parameter can be set to uint(-1) and the protocol will proceed with the highest possible liquidation allowed by the close factor.
    
*   To check a user's health factor, use \[getUserAccountData()\].
    

Liquidators must approve() the Pool contract to use debtToCover of the underlying ERC20 of the asset used for the liquidation.

##### Input Parameters:

[](#write-methods-liquidationcall-input-parameters)

Name

Type

Description

collateralAsset

address

The address of the underlying asset used as collateral, to receive as result of the liquidation

debtAsset

address

The address of the underlying borrowed asset to be repaid with the liquidation

user

address

The address of the borrower getting liquidated

debtToCover

uint256

The debt amount of borrowed asset the liquidator will repay

receiveAToken

bool

true if the liquidator wants to receive the aTokens equivalent of the purchased collateral, false if they want to receive the underlying collateral asset directly

#### flashLoan

[](#write-methods-flashloan)

```
function flashLoan(    address receiverAddress,    address[] calldata assets,    uint256[] calldata amounts,    uint256[] calldata interestRateModes,    address onBehalfOf,    bytes calldata params,    uint16 referralCode) public virtual override
```

Allows users to access liquidity of the pool for a given list of assets within one transaction, as long as the amount taken plus a fee is returned. The receiver must approve the Pool contract for at least the *amount borrowed + fee*, otherwise the transaction will revert.

The flash loan fee is waived for approved FLASH\_BORROWER.

There are security concerns for developers of flashloan receiver contracts that must be taken into consideration. For further details, visit [Flash Loan Developers Guide](/docs/developers/flash-loans).

Referral program is currently inactive, you can pass 0 as referralCode. This program may be activated in the future through an Aave governance proposal.

##### Input Parameters:

[](#write-methods-flashloan-input-parameters)

Name

Type

Description

receiverAddress

address

The address of the contract receiving the flash-borrowed funds, implementing the IFlashLoanReceiver interface

assets

address\[\]

The addresses of the assets being flash-borrowed

amounts

uint256\[\]

The amounts of the assets being flash-borrowed. This needs to contain the same number of entries as assets

interestRateModes

uint256\[\]

The types of the debt position to open if the flash loan is not returned: 0 -> Don't open any debt, the amount + fee must be paid in this case or just revert if the funds can't be transferred from the receiver. 2 -> Open variable rate borrow position for the value of the amount flash-borrowed to the onBehalfOf address

onBehalfOf

address

The address that will receive the debt if the associated interestRateModes is 1 or 2. onBehalfOf must already have approved sufficient borrow allowance of the associated asset to msg.sender

params

bytes

Variadic packed params to pass to the receiver as extra information

referralCode

uint16

Referral supply is currently inactive, you can pass 0. This code is used to register the integrator originating the operation, for potential rewards. 0 if the action is executed directly by the user, without any middle-men

#### flashLoanSimple

[](#write-methods-flashloansimple)

```
function flashLoanSimple(    address receiverAddress,    address asset,    uint256 amount,    bytes calldata params,    uint16 referralCode) public virtual override
```

Allows users to access liquidity of the pool for a given asset within one transaction, as long as the amount taken plus a fee is returned. The receiver must approve the Pool contract for at least the *amount borrowed + fee*, otherwise the transaction will revert.

This function does not waive the fee for approved FLASH\_BORROWER, nor does it allow for opening a debt position instead of repaying.

There are security concerns for developers of flashloan receiver contracts that must be kept into consideration.

Referral program is currently inactive, you can pass 0 as referralCode. This program may be activated in the future through an Aave governance proposal.

##### Input Parameters:

[](#write-methods-flashloansimple-input-parameters)

Name

Type

Description

receiverAddress

address

The address of the contract receiving the flash-borrowed funds, implementing the IFlashLoanReceiver interface

asset

address

The address of the asset being flash-borrowed

amount

uint256

The amount of the asset being flash-borrowed

params

bytes

Variadic packed params to pass to the receiver as extra information

referralCode

uint16

Referral supply is currently inactive, you can pass 0. This code is used to register the integrator originating the operation, for potential rewards. 0 if the action is executed directly by the user, without any middle-men

#### mintToTreasury

[](#write-methods-minttotreasury)

```
function mintToTreasury(address[] calldata assets) external virtual override
```

Mints the assets accrued through the reserve factor to the treasury in the form of aTokens for the given list of assets.

##### Input Parameters:

[](#write-methods-minttotreasury-input-parameters)

Name

Type

Description

assets

address\[\]

The list of reserves for which the minting needs to be executed

#### finalizeTransfer

[](#write-methods-finalizetransfer)

```
function finalizeTransfer(    address asset,    address from,    address to,    uint256 amount,    uint256 balanceFromBefore,    uint256 balanceToBefore) external virtual override
```

Validates and finalizes an aToken transfer. It is only callable by the overlying aToken of the asset.

##### Input Parameters:

[](#write-methods-finalizetransfer-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the aToken

from

address

The user from which the aTokens are transferred

to

address

The user receiving the aTokens

amount

uint256

The amount being transferred/withdrawn

balanceFromBefore

uint256

The aToken balance of the from user before the transfer

balanceToBefore

uint256

The aToken balance of the to user before the transfer

#### setUserEMode

[](#write-methods-setuseremode)

```
function setUserEMode(uint8 categoryId) external virtual override
```

Allows a user to use the protocol in efficiency mode. The category id must be a valid id already defined by *Pool or Risk Admins*.

Will revert if user is borrowing non-compatible asset or if the change will drop the Health Factor < HEALTH\_FACTOR\_LIQUIDATION\_THRESHOLD.

##### Input Parameters:

[](#write-methods-setuseremode-input-parameters)

Name

Type

Description

categoryId

uint8

The eMode category id (0 - 255) defined by Risk or Pool Admins. categoryId set to 0 is a non eMode category

#### mintUnbacked

[](#write-methods-mintunbacked)

```
function mintUnbacked(    address asset,    uint256 amount,    address onBehalfOf,    uint16 referralCode) external virtual override onlyBridge
```

Allows contracts, with BRIDGE role permission, to mint an amount of unbacked aTokens to the onBehalfOf address. This method is part of the V3 [Portals](/docs/developers/aave-v3) feature.

Only available to the addresses with BRIDGE role. Bridge addresses can be whitelisted by Aave Governance.

Referral program is currently inactive, you can pass 0 as referralCode. This program may be activated in the future through an Aave governance proposal.

##### Input Parameters:

[](#write-methods-mintunbacked-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset to mint

amount

uint256

The amount to mint

onBehalfOf

address

The address that will receive the aTokens

referralCode

uint16

Referral supply is currently inactive, you can pass 0. This code is used to register the integrator originating the operation, for potential rewards. 0 if the action is executed directly by the user, without any middle-men

#### backUnbacked

[](#write-methods-backunbacked)

```
function backUnbacked(    address asset,    uint256 amount,    uint256 fee) external virtual override onlyBridge returns (uint256)
```

Allows contracts, with BRIDGE role permission, to back the current unbacked underlying aTokens with amount and pay fee. This method is part of the V3 [Portals](/docs/developers/aave-v3) feature.

Only available to the addresses with BRIDGE role. Bridge addresses can be whitelisted by the governance.

##### Input Parameters:

[](#write-methods-backunbacked-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset to back

amount

uint256

The amount of asset supplied to back the unbacked tokens

fee

uint256

The amount paid in fees

##### Return Value:

[](#write-methods-backunbacked-return-value)

Type

Description

uint256

The final amount backed, representing the portion of assets that were successfully supplied to back the unbacked aTokens, including any fees that were taken into account.

#### initReserve

[](#write-methods-initreserve)

```
function initReserve(    address asset,    address aTokenAddress,    address stableDebtAddress,    address variableDebtAddress,    address interestRateStrategyAddress) external virtual override onlyPoolConfigurator
```

Initializes a reserve, activating it, assigning an aToken and debt tokens and an interest rate strategy.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-initreserve-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

aTokenAddress

address

The address of the aToken that will be assigned to the reserve

stableDebtAddress

address

The address of the StableDebtToken that will be assigned to the reserve (deprecated)

variableDebtAddress

address

The address of the VariableDebtToken that will be assigned to the reserve

interestRateStrategyAddress

address

The address of the interest rate strategy contract

#### dropReserve

[](#write-methods-dropreserve)

```
function dropReserve(address asset) external virtual override onlyPoolConfigurator
```

Drop a reserve.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-dropreserve-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

#### setReserveInterestRateStrategyAddress

[](#write-methods-setreserveinterestratestrategyaddress)

```
function setReserveInterestRateStrategyAddress(address asset, address rateStrategyAddress) external virtual override onlyPoolConfigurator
```

Updates the address of the interest rate strategy contract.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-setreserveinterestratestrategyaddress-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

rateStrategyAddress

address

The address of the interest rate strategy contract

#### setConfiguration

[](#write-methods-setconfiguration)

```
function setConfiguration(address asset, DataTypes.ReserveConfigurationMap calldata configuration) external virtual override onlyPoolConfigurator
```

Sets the configuration bitmap of the reserve as a whole.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-setconfiguration-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

configuration

DataTypes.ReserveConfigurationMap

The new configuration bitmap

The [DataTypes.ReserveConfigurationMap](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L79) struct is composed of the following fields:

bit

Description

0-15

LTV

16-31

Liquidation threshold

32-47

Liquidation bonus

48-55

Decimals

56

Reserve is active

57

Reserve is frozen

58

Borrowing is enabled

59

Stable rate borrowing enabled (deprecated)

60

Asset is paused

61

Borrowing in isolation mode is enabled

62

Siloed borrowing is enabled

63

Flashloaning is enabled

64-79

Reserve factor

80-115

Borrow cap in whole tokens, borrowCap == 0 => no cap

116-151

Supply cap in whole tokens, supplyCap == 0 => no cap

152-167

Liquidation protocol fee

168-175

eMode category (deprecated)

176-211

Unbacked mint cap in whole tokens, unbackedMintCap == 0 => minting disabled

212-251

Debt ceiling for isolation mode with (ReserveConfiguration::DEBT\_CEILING\_DECIMALS) decimals

252

Virtual accounting is enabled

253-255

Unused

#### updateBridgeProtocolFee

[](#write-methods-updatebridgeprotocolfee)

```
function updateBridgeProtocolFee(uint256 protocolFee) external virtual override onlyPoolConfigurator
```

Updates the protocol fee on the bridging.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-updatebridgeprotocolfee-input-parameters)

Name

Type

Description

protocolFee

uint256

The part of the premium sent to the protocol treasury

#### updateFlashloanPremiums

[](#write-methods-updateflashloanpremiums)

```
function updateFlashloanPremiums(uint128 flashLoanPremiumTotal, uint128 flashLoanPremiumToProtocol) external virtual override onlyPoolConfigurator
```

Updates flash loan premiums. A flash loan premium consists of two parts:

*   A part is sent to aToken holders as extra, one time accumulated interest
    
*   A part is collected by the protocol treasury
    

The total premium is calculated on the total borrowed amount. The premium to protocol is calculated on the total premium, being a percentage of flashLoanPremiumTotal.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-updateflashloanpremiums-input-parameters)

Name

Type

Description

flashLoanPremiumTotal

uint128

The total premium, expressed in bps

flashLoanPremiumToProtocol

uint128

The part of the premium sent to the protocol treasury, expressed in bps

#### configureEModeCategory

[](#write-methods-configureemodecategory)

```
function configureEModeCategory(uint8 id, DataTypes.EModeCategory memory category) external virtual override onlyPoolConfigurator
```

Configures a new category for the eMode. In eMode, the protocol allows very high borrowing power to borrow assets of the same category. The category 0 is reserved for volatile heterogeneous assets and it's always disabled.

Each eMode category has a custom ltv and liquidation threshold. Each eMode category may or may not have a custom oracle to override the individual assets price oracles.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-configureemodecategory-input-parameters)

Name

Type

Description

id

uint8

The total premium, expressed in bps

category

DataTypes.EModeCategory

The configuration of the category

The [DataTypes.EModeCategory](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L114) struct is composed of the following fields:

Name

Type

Description

ltv

uint16

The custom Loan to Value for the eMode category

liquidationThreshold

uint16

The custom liquidation threshold for the eMode category

liquidationBonus

uint16

The liquidation bonus for the eMode category

collateralBitmap

uint128

Bitmap of collateral assets in the category

label

string

The custom label describing the eMode category

borrowableBitmap

uint128

Bitmap of borrowable assets in the category

#### resetIsolationModeTotalDebt

[](#write-methods-resetisolationmodetotaldebt)

```
function resetIsolationModeTotalDebt(address asset) external virtual override onlyPoolConfigurator
```

Resets the isolation mode total debt of the given asset to zero. It requires the given asset to have a zero debt ceiling.

Only callable by the [PoolConfigurator](/docs/developers/smart-contracts/pool-configurator) contract.

##### Input Parameters:

[](#write-methods-resetisolationmodetotaldebt-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset to reset the isolationModeTotalDebt

#### rescueTokens

[](#write-methods-rescuetokens)

```
function rescueTokens(address token, address to, uint256 amount) external virtual override onlyPoolAdmin
```

Rescue and transfer tokens locked in this contract.

Only available to [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#pooladmin) role. Pool admin is selected by the governance.

##### Input Parameters:

[](#write-methods-rescuetokens-input-parameters)

Name

Type

Description

token

address

The address of the token

to

address

The address of the recipient

amount

uint256

The amount of token to transfer

#### eliminateReserveDeficit

[](#write-methods-eliminatereservedeficit)

Covers the deficit of a specified reserve by burning the equivalent aToken amount for assets with virtual accounting enabled or the equivalent amount of underlying for assets with virtual accounting disabled (e.g. GHO). Only callable by address with onlyUmbrella modifier.

```
function eliminateReserveDeficit(address asset, uint256 amount) external;
```

##### Input Parameters:

[](#write-methods-eliminatereservedeficit-input-parameters)

Name

Type

Description

asset

address

Underlying token address

amount

uint256

The amount to be covered, in aToken or underlying on non-virtual accounted assets

### View Methods

[](#view-methods)

#### getUserAccountData

[](#view-methods-getuseraccountdata)

```
function getUserAccountData(address user) external view virtual override returns (    uint256 totalCollateralBase,    uint256 totalDebtBase,    uint256 availableBorrowsBase,    uint256 currentLiquidationThreshold,    uint256 ltv,    uint256 healthFactor)
```

Returns the user account data across all the reserves.

##### Input Parameters:

[](#view-methods-getuseraccountdata-input-parameters)

Name

Type

Description

user

address

The address of the user

##### Return Values:

[](#view-methods-getuseraccountdata-return-values)

Name

Type

Description

totalCollateralBase

uint256

The total collateral of the user in the base currency used by the price feed

totalDebtBase

uint256

The total debt of the user in the base currency used by the price feed

availableBorrowsBase

uint256

The borrowing power left of the user in the base currency used by the price feed

currentLiquidationThreshold

uint256

The liquidation threshold of the user

ltv

uint256

The loan to value of the user

healthFactor

uint256

The current health factor of the user

#### getConfiguration

[](#view-methods-getconfiguration)

```
function getConfiguration(address asset) external view virtual override returns (DataTypes.ReserveConfigurationMap memory)
```

Returns the configuration of the reserve.

##### Input Parameters:

[](#view-methods-getconfiguration-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getconfiguration-return-values)

Type

Description

DataTypes.ReserveConfigurationMap

The configuration of the reserve

The [DataTypes.ReserveConfigurationMap](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L79) struct is composed of the following fields:

bit

Description

0-15

LTV

16-31

Liquidation threshold

32-47

Liquidation bonus

48-55

Decimals

56

Reserve is active

57

Reserve is frozen

58

Borrowing is enabled

59

Stable rate borrowing enabled (deprecated)

60

Asset is paused

61

Borrowing in isolation mode is enabled

62

Siloed borrowing enabled

63

Flashloaning enabled

64-79

Reserve factor

80-115

Borrow cap in whole tokens, borrowCap == 0 => no cap

116-151

Supply cap in whole tokens, supplyCap == 0 => no cap

152-167

Liquidation protocol fee

168-175

eMode category (deprecated)

176-211

Unbacked mint cap in whole tokens, unbackedMintCap == 0 => minting disabled

212-251

Debt ceiling for isolation mode with (ReserveConfiguration::DEBT\_CEILING\_DECIMALS) decimals

252

Virtual accounting is enabled for the reserve

253-255

Unused

#### getUserConfiguration

[](#view-methods-getuserconfiguration)

```
function getUserConfiguration(address user) external view virtual override returns (DataTypes.UserConfigurationMap memory)
```

Returns the configuration of the user across all the reserves.

##### Input Parameters:

[](#view-methods-getuserconfiguration-input-parameters)

Name

Type

Description

user

address

The user address

##### Return Values:

[](#view-methods-getuserconfiguration-return-values)

Type

Description

DataTypes.UserConfigurationMap

The configuration of the user

The [DataTypes.UserConfigurationMap](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L105) struct is composed of the following fields:

Name

Type

Description

data

uint256

Bitmap of the users collaterals and borrows. It is divided into pairs of bits, one pair per asset. The first bit indicates if an asset is used as collateral by the user, the second whether an asset is borrowed by the user. The corresponding assets are in the same position as getReservesList(). For example, if the hex value returned is 0x40020, which represents a decimal value of 262176, then in binary it is 1000000000000100000. If we format the binary value into pairs, starting from the right, we get 1 00 00 00 00 00 00 10 00 00. If we start from the right and move left in the above binary pairs, the third pair is 10. Therefore the 1 indicates that third asset from the reserveList is used as collateral, and 0 indicates it has not been borrowed by this user

#### getReserveNormalizedIncome

[](#view-methods-getreservenormalizedincome)

```
function getReserveNormalizedIncome(address asset) external view virtual override returns (uint256)
```

Returns the ongoing normalized income for the reserve.

A value of 1e27 means there is no income. As time passes, the yield is accrued. A value of 2\*1e27 means for each unit of asset, one unit of income has been accrued.

##### Input Parameters:

[](#view-methods-getreservenormalizedincome-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreservenormalizedincome-return-values)

Type

Description

uint256

The reserve's normalized income

#### getReserveNormalizedVariableDebt

[](#view-methods-getreservenormalizedvariabledebt)

```
function getReserveNormalizedVariableDebt(address asset) external view virtual override returns (uint256)
```

Returns the normalized variable debt per unit of asset.

A value of 1e27 means there is no debt. As time passes, the debt is accrued. A value of 2\*1e27 means that for each unit of debt, one unit worth of interest has been accumulated.

##### Input Parameters:

[](#view-methods-getreservenormalizedvariabledebt-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreservenormalizedvariabledebt-return-values)

Type

Description

uint256

The reserve normalized variable debt

#### getReservesList

[](#view-methods-getreserveslist)

```
function getReservesList() external view virtual override returns (address[] memory)
```

Returns the list of the underlying assets of all the initialized reserves. It does not include dropped reserves.

##### Return Values:

[](#view-methods-getreserveslist-return-values)

Type

Description

address\[\]

The addresses of the underlying assets of the initialized reserves

#### getReserveAddressById

[](#view-methods-getreserveaddressbyid)

```
function getReserveAddressById(uint16 id) external view returns (address)
```

Returns the address of the underlying asset of a reserve by the reserve id as stored in the [DataTypes.ReserveData](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L42) struct.

##### Input Parameters:

[](#view-methods-getreserveaddressbyid-input-parameters)

Name

Type

Description

id

uint16

The id of the reserve as stored in the [DataTypes.ReserveData](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L42) struct

##### Return Values:

[](#view-methods-getreserveaddressbyid-return-values)

Type

Description

address

The address of the reserve associated with id

#### getEModeCategoryData

[](#view-methods-getemodecategorydata)

```
function getEModeCategoryData(uint8 id) external view virtual override returns (DataTypes.EModeCategory memory)
```

Returns the data of an eMode category.

Each eMode category has a custom LTV and liquidation threshold. Each eMode category may or may not have a custom oracle to override the individual assets' price oracles.

##### Input Parameters:

[](#view-methods-getemodecategorydata-input-parameters)

Name

Type

Description

id

uint8

The id of the category

##### Return Values:

[](#view-methods-getemodecategorydata-return-values)

Type

Description

DataTypes.EModeCategory

The configuration data of the category

The [DataTypes.EModeCategory](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L114) struct is composed of the following fields:

Name

Type

Description

ltv

uint16

The custom Loan to Value for the eMode category

liquidationThreshold

uint16

The custom liquidation threshold for the eMode category

liquidationBonus

uint16

The liquidation bonus for the eMode category

collateralBitmap

uint128

Bitmap of collateral assets in the category

label

string

The custom label describing the eMode category

borrowableBitmap

uint128

Bitmap of borrowable assets in the category

#### getReserveData

[](#view-methods-getreservedata)

```
function getReserveData(address asset) external view virtual override returns (DataTypes.ReserveData memory)
```

Returns the state and configuration of the reserve.

##### Input Parameters:

[](#view-methods-getreservedata-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreservedata-return-values)

Type

Description

DataTypes.ReserveData

The state and configuration data of the reserve

The [DataTypes.ReserveData](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L42) struct is composed of the following fields:

Name

Type

Description

configuration

ReserveConfigurationMap

Stores the [reserve configuration](https://github.com/aave-dao/aave-v3-origin/blob/3aad8ca184159732e4b3d8c82cd56a8707a106a2/src/core/contracts/protocol/libraries/types/DataTypes.sol#L42)

liquidityIndex

uint128

The yield generated by the reserve during time interval since lastUpdatedTimestamp. Expressed in ray

currentLiquidityRate

uint128

The current supply rate. Expressed in ray

variableBorrowIndex

uint128

The yield accrued by reserve during time interval since lastUpdatedTimestamp. Expressed in ray

currentVariableBorrowRate

uint128

The current variable borrow rate. Expressed in ray

\_\_deprecatedStableBorrowRate

uint128

DEPRECATED on v3.2.0

lastUpdateTimestamp

uint40

The timestamp of when reserve data was last updated. Used for yield calculation

id

uint16

The id of the reserve. It represents the reserve’s position in the list of active reserves

liquidationGracePeriodUntil

uint40

The timestamp until liquidations are not allowed on the reserve. If set to the past, liquidations will be allowed

aTokenAddress

address

The address of associated aToken

\_\_deprecatedStableDebtTokenAddress

address

DEPRECATED on v3.2.0

variableDebtTokenAddress

address

The address of associated variable debt token

interestRateStrategyAddress

address

The address of interest rate strategy

accruedToTreasury

uint128

The current treasury balance (scaled)

unbacked

uint128

The outstanding unbacked aTokens minted through the bridging feature

isolationModeTotalDebt

uint128

The outstanding debt borrowed against this asset in isolation mode

virtualUnderlyingBalance

uint128

The virtual balance of the underlying asset for yield calculation purposes

#### getUserEMode

[](#view-methods-getuseremode)

```
function getUserEMode(address user) external view virtual override returns (uint256)
```

Returns eMode the user is using. 0 is a non eMode category.

##### Input Parameters:

[](#view-methods-getuseremode-input-parameters)

Name

Type

Description

user

address

The address of the user

##### Return Values:

[](#view-methods-getuseremode-return-values)

Type

Description

uint256

The eMode id

#### FLASHLOAN\_PREMIUM\_TOTAL

[](#view-methods-flashloan-premium-total)

```
function FLASHLOAN_PREMIUM_TOTAL() public view virtual override returns (uint128)
```

Returns the percent of total flashloan premium paid by the borrower.

A part of this premium is added to reserve's liquidity index i.e. paid to the liquidity provider and the other part is paid to the protocol i.e. accrued to the treasury.

##### Return Values:

[](#view-methods-flashloan-premium-total-return-values)

Type

Description

uint128

The total fee on flashloans

#### BRIDGE\_PROTOCOL\_FEE

[](#view-methods-bridge-protocol-fee)

```
function BRIDGE_PROTOCOL_FEE() public view virtual override returns (uint256)
```

Returns the part of the bridge fees sent to protocol.

##### Return Values:

[](#view-methods-bridge-protocol-fee-return-values)

Type

Description

uint256

The percentage of available liquidity to borrow, expressed in bps

#### FLASHLOAN\_PREMIUM\_TO\_PROTOCOL

[](#view-methods-flashloan-premium-to-protocol)

```
function FLASHLOAN_PREMIUM_TO_PROTOCOL() public view virtual override returns (uint128)
```

Returns the percent of flashloan premium that is accrued to the treasury.

##### Return Values:

[](#view-methods-flashloan-premium-to-protocol-return-values)

Type

Description

uint128

The percentage of available liquidity to borrow, expressed in bps

#### MAX\_NUMBER\_RESERVES

[](#view-methods-max-number-reserves)

```
function MAX_NUMBER_RESERVES() public view virtual override returns (uint16)
```

Returns the maximum number of reserves supported to be listed in this Pool.

##### Return Values:

[](#view-methods-max-number-reserves-return-values)

Type

Description

uint16

The maximum number of reserves supported

#### getLiquidationGracePeriod

[](#view-methods-getliquidationgraceperiod)

Returns the liquidation grace period of the given asset

```
function getLiquidationGracePeriod(address asset) external view virtual override returns (uint40)
```

##### Input Parameters:

[](#view-methods-getliquidationgraceperiod-input-parameters)

Name

Type

Description

asset

address

Underlying token address

##### Return Values:

[](#view-methods-getliquidationgraceperiod-return-values)

Type

Description

uint256

Timestamp when the liquidation grace period will end

#### getReserveDeficit

[](#view-methods-getreservedeficit)

Returns the current deficit of a reserve.

```
function getReserveDeficit(address asset) external view returns (uint256);
```

##### Input Parameters:

[](#view-methods-getreservedeficit-input-parameters)

Name

Type

Description

asset

address

Underlying token address

##### Return Values:

[](#view-methods-getreservedeficit-return-values)

Type

Description

uint256

Current reserve deficit from undercollateralized borrow positions

#### getReserveAToken

[](#view-methods-getreserveatoken)

Returns the aToken address of a reserve.

```
function getReserveAToken(address asset) external view returns (address);
```

##### Input Parameters:

[](#view-methods-getreserveatoken-input-parameters)

Name

Type

Description

asset

address

Underlying token address

##### Return Values:

[](#view-methods-getreserveatoken-return-values)

Type

Description

address

The address of the AToken

#### getReserveVariableDebtToken

[](#view-methods-getreservevariabledebttoken)

Returns the variableDebtToken address of a reserve.

```
function getReserveVariableDebtToken(address asset) external view returns (address);
```

##### Input Parameters:

[](#view-methods-getreservevariabledebttoken-input-parameters)

Name

Type

Description

asset

address

Underlying token address

##### Return Values:

[](#view-methods-getreservevariabledebttoken-return-values)

Type

Description

address

The address of the VariableDebtToken

### Pure Methods

[](#pure-methods)

#### getRevision

[](#pure-methods-getrevision)

```
function getRevision() internal pure virtual override returns (uint256)
```

Returns the revision number of the contract. Needs to be defined in the inherited class as a constant.

Returns 0x1.

##### Return Values:

[](#pure-methods-getrevision-return-values)

Type

Description

uint256

The revision number

[

Previous

**Smart Contracts**

](/docs/developers/smart-contracts)[

Next

**L2 Pool**

](/docs/developers/smart-contracts/l2-pool)

---

<a id="doc_31"></a>

## 📁 developers/smart_contracts / Switch Adapters | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/switch_adapters.md*

Source: https://aave.com/docs/developers/smart-contracts/switch-adapters

## Switch Adapters

[](#switch-adapters)

These switch adapters integrate Aave's Flash Loans and the ParaSwap DEX aggregator smart contracts to facilitate advanced actions such as repaying borrow positions using collateral, switching collateral assets, switching borrow positions, and withdrawing and switching assets. They allow users to perform complex operations in a single transaction, leveraging the liquidity of the Aave protocol and the atomic switching capabilities of decentralized exchanges.

The table below outlines switch feature availability across V3 markets on the [Aave Labs interface](https://app.aave.com):

Market

Repay With Collateral

Collateral Switch

Debt Switch

Withdraw & Switch

Ethereum Core

Ethereum Prime

Ethereum EtherFi

Arbitrum

Avalanche

Base

BNB

Optimism

Polygon

Gnosis

Fantom

Harmony

Metis

Scroll

ZKsync

### Repay With Collateral

[](#repay-with-collateral)

The ParaSwapRepayAdapter contract enables users to repay their borrow positions on Aave using their supplied collateral directly, without the need to unwind their positions or provide additional liquidity. It leverages Aave's Flash Loans and the ParaSwap DEX aggregator to switch the user's collateral for the borrowed asset and repay the borrow position in a single atomic transaction.

By using this adapter, users can efficiently manage their positions and reduce their borrow positions using their existing collateral, saving on transaction costs and avoiding manual steps.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/extensions/paraswap-adapters/ParaSwapRepayAdapter.sol).

Reference Integration: [useCollateralRepaySwap.tsx](https://github.com/aave/interface/blob/main/src/hooks/paraswap/useCollateralRepaySwap.tsx)

#### Write Methods

[](#repay-with-collateral-write-methods)

##### executeOperation

[](#repay-with-collateral-write-methods-executeoperation)

```
function executeOperation(    address asset,    uint256 amount,    uint256 premium,    address initiator,    bytes calldata params) external override nonReentrant returns (bool)
```

Uses the received funds from the flash loan to repay a borrow position on the protocol on behalf of the user. Then, pulls the collateral from the user and switches it to the debt asset to repay the flash loan.

The user should give this contract allowance to pull the aTokens in order to withdraw the underlying asset, switch it, and repay the flash loan.

Supports only one asset on the flash loan.

The params parameter should be the ABI-encoded values of the following:

*   IERC20Detailed debtAsset — The address of the borrow position asset
    
*   uint256 debtRepayAmount — The amount of the borrow position to be repaid
    
*   uint256 buyAllBalanceOffset — Offset in the ParaSwap calldata if switching all balance
    
*   uint256 rateMode — The rate mode of the borrow position to be repaid
    
*   bytes paraswapData — Data for the ParaSwap Adapter
    
*   PermitSignature permitSignature — Struct containing the permit signature, set to zeroes if not used
    

###### Input Parameters:

Name

Type

Description

asset

address

The address of the flash-borrowed asset

amount

uint256

The amount of the flash-borrowed asset

premium

uint256

The fee of the flash-borrowed asset

initiator

address

The address of the flash loan initiator

params

bytes

The byte-encoded parameters passed when initiating the flash loan

###### Return Values:

Type

Description

bool

True if the execution of the operation succeeds, false otherwise

##### swapAndRepay

[](#repay-with-collateral-write-methods-swapandrepay)

```
function swapAndRepay(    IERC20Detailed collateralAsset,    IERC20Detailed debtAsset,    uint256 collateralAmount,    uint256 debtRepayAmount,    uint256 debtRateMode,    uint256 buyAllBalanceOffset,    bytes calldata paraswapData,    PermitSignature calldata permitSignature) external nonReentrant
```

Switches the user's collateral for the debt asset and then repays the borrow position on the protocol on behalf of the user without using flash loans. This method can be used when the temporary transfer of the collateral asset to this contract does not affect the user's position.

The user should give this contract allowance to pull the aTokens in order to withdraw the underlying asset.

###### Input Parameters:

Name

Type

Description

collateralAsset

IERC20Detailed

The address of the collateral asset to be switched

debtAsset

IERC20Detailed

The address of the debt asset

collateralAmount

uint256

The maximum amount of the collateral to be switched

debtRepayAmount

uint256

The amount of the borrow position to be repaid, or maximum amount when repaying all

debtRateMode

uint256

The rate mode of the borrow position to be repaid

buyAllBalanceOffset

uint256

Offset in the ParaSwap calldata if switching all balance, otherwise 0

paraswapData

bytes

Data for the ParaSwap Adapter

permitSignature

PermitSignature

Struct containing the permit signature, set to zeroes if not used

##### PermitSignature Struct

[](#repay-with-collateral-write-methods-permitsignature-struct)

```
struct PermitSignature {    uint256 deadline;    uint8 v;    bytes32 r;    bytes32 s;}
```

###### Members:

Name

Type

Description

deadline

uint256

The deadline timestamp for the permit signature

v

uint8

The V parameter of the ECDSA signature

r

bytes32

The R parameter of the ECDSA signature

s

bytes32

The S parameter of the ECDSA signature

* * *

### Collateral Switch

[](#collateral-switch)

The ParaSwapLiquiditySwapAdapter contract allows users to switch their supplied collateral from one asset to another in a single transaction using Aave's Flash Loans and the ParaSwap DEX aggregator.

This adapter enables users to rebalance their collateral positions without needing to withdraw and re-supply assets manually. By leveraging flash loans, the user can switch their existing collateral to a new asset and supply it back into the Aave protocol in a single transaction.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/extensions/paraswap-adapters/ParaSwapLiquiditySwapAdapter.sol).

Reference Integration: [useCollateralSwap.tsx](https://github.com/aave/interface/blob/main/src/hooks/paraswap/useCollateralSwap.tsx)

#### Write Methods

[](#collateral-switch-write-methods)

##### executeOperation

[](#collateral-switch-write-methods-executeoperation)

```
function executeOperation(    address asset,    uint256 amount,    uint256 premium,    address initiator,    bytes calldata params) external override nonReentrant returns (bool)
```

Switches the received amount from the flash loan into the specified asset. The received funds from the switch are then supplied into the protocol on behalf of the user.

The user should give this contract allowance to pull the aTokens in order to withdraw the underlying asset and repay the flash loan.

The params parameter should be the ABI-encoded values of the following:

*   IERC20Detailed assetToSwapTo — The address of the underlying asset to be switched to and supplied
    
*   uint256 minAmountToReceive — The minimum amount to be received from the switch
    
*   uint256 swapAllBalanceOffset — Offset in the Augustus calldata if switching all balance, otherwise 0
    
*   bytes swapCalldata — Calldata for ParaSwap's Augustus Swapper contract
    
*   IParaSwapAugustus augustus — Address of ParaSwap's Augustus Swapper contract
    
*   PermitSignature permitParams — Struct containing the permit signature, set to zeroes if not used
    

###### Input Parameters:

Name

Type

Description

asset

address

The address of the flash-borrowed asset

amount

uint256

The amount of the flash-borrowed asset

premium

uint256

The fee of the flash-borrowed asset

initiator

address

The address of the flash loan initiator

params

bytes

The byte-encoded parameters passed when initiating the flash loan

###### Return Values:

Type

Description

bool

True if the execution of the operation succeeds, false otherwise

##### swapAndDeposit

[](#collateral-switch-write-methods-swapanddeposit)

```
function swapAndDeposit(    IERC20Detailed assetToSwapFrom,    IERC20Detailed assetToSwapTo,    uint256 amountToSwap,    uint256 minAmountToReceive,    uint256 swapAllBalanceOffset,    bytes calldata swapCalldata,    IParaSwapAugustus augustus,    PermitSignature calldata permitParams) external nonReentrant
```

Switches an amount of an asset to another and supplies the new asset amount on behalf of the user without using a flash loan. This method can be used when the temporary transfer of the collateral asset to this contract does not affect the user's position.

The user should give this contract allowance to pull the aTokens in order to withdraw the underlying asset and perform the switch.

###### Input Parameters:

Name

Type

Description

assetToSwapFrom

IERC20Detailed

The address of the underlying asset to be switched from

assetToSwapTo

IERC20Detailed

The address of the underlying asset to be switched to and supplied

amountToSwap

uint256

Amount to be switched, or maximum amount when switching all balance

minAmountToReceive

uint256

Minimum amount to be received from the switch

swapAllBalanceOffset

uint256

Offset in Augustus calldata if switching all balance, otherwise 0

swapCalldata

bytes

Calldata for ParaSwap's Augustus Swapper contract

augustus

IParaSwapAugustus

Address of ParaSwap's Augustus Swapper contract

permitParams

PermitSignature

Struct containing the permit signature, set to zeroes if not used

* * *

### Borrow Position Switch

[](#borrow-position-switch)

The ParaSwapDebtSwapAdapter contracts allow users to switch their borrow positions from one asset to another. They leverage Aave's Flash Loans and the ParaSwap DEX aggregator to perform the switch in a single atomic transaction.

There are two versions of the adapter:

*   **ParaSwapDebtSwapAdapterV3**: The standard version that supports switching any borrow position asset.
    
    *   Source Code: [GitHub](https://github.com/bgd-labs/aave-debt-swap/blob/main/src/contracts/ParaSwapDebtSwapAdapterV3.sol)
        
    *   Reference Integration: [useDebtSwitch.tsx](https://github.com/aave/interface/blob/main/src/hooks/paraswap/useDebtSwitch.tsx)
        
    
*   **ParaSwapDebtSwapAdapterV3GHO**: A specialized version that supports GHO, where GHO can be flash minted via the ERC-3156 interface.
    
    *   Source Code: [GitHub](https://github.com/bgd-labs/aave-debt-swap/blob/main/src/contracts/ParaSwapDebtSwapAdapterV3GHO.sol)
        
    *   Reference Integration: [useDebtSwitch.tsx](https://github.com/aave/interface/blob/main/src/hooks/paraswap/useDebtSwitch.tsx)
        
    

#### ParaSwapDebtSwapAdapterV3

[](#borrow-position-switch-paraswapdebtswapadapterv3)

The ParaSwapDebtSwapAdapterV3 contract allows users to switch their borrow positions from one asset to another, enabling borrow position refinancing on the Aave protocol.

This adapter leverages Aave's Flash Loans and the ParaSwap DEX aggregator to perform the borrow position switch in a single transaction.

##### Write Methods

[](#borrow-position-switch-paraswapdebtswapadapterv3-write-methods)

###### executeOperation

```
function executeOperation(    address[] calldata assets,    uint256[] calldata amounts,    uint256[] calldata,    address initiator,    bytes calldata params) external returns (bool)
```

Performs the borrow position switch operation using the received funds from the flash loan.

Performs the switch and repay operation using the borrowed funds from the flash loan, and then re-borrows the new borrow position asset to maintain the overall borrow position.

The params parameter should be the ABI-encoded values required for the operation, such as:

*   The addresses of the borrow position assets involved
    
*   The rate modes of the borrow positions
    
*   ParaSwap switch data
    
*   Any necessary permit signatures
    

###### Input Parameters:

Name

Type

Description

assets

address\[\]

The addresses of the assets being borrowed in the flash loan

amounts

uint256\[\]

The amounts of the assets being borrowed

premiums

uint256\[\]

The fees for the flash loans

initiator

address

The address of the flash loan initiator

params

bytes

Arbitrary data containing the parameters needed for the operation

###### Return Values:

Type

Description

bool

True if the execution of the operation succeeds, false otherwise

#### ParaSwapDebtSwapAdapterV3GHO

[](#borrow-position-switch-paraswapdebtswapadapterv3gho)

The ParaSwapDebtSwapAdapterV3GHO contract is a specialized version of the borrow position switch adapter that supports GHO, allowing users to switch their borrow positions involving GHO. It utilizes the ERC-3156 flash mint interface for GHO.

Performs the switch and repay operation using the borrowed funds from the flash loan, and then re-borrows the borrow position asset to maintain the overall borrow position.

##### Write Methods

[](#borrow-position-switch-paraswapdebtswapadapterv3gho-write-methods)

###### onFlashLoan

```
function onFlashLoan(    address initiator,    address token,    uint256 amount,    uint256 fee,    bytes calldata data) external override returns (bytes32)
```

This is the ERC-3156 Flash Loan callback function that gets called when the contract receives a flash loan (in this case, flash mint) from the GHO Flash Minter.

###### Input Parameters:

Name

Type

Description

initiator

address

The initiator of the flash loan

token

address

The address of the token being borrowed

amount

uint256

The amount of tokens being borrowed

fee

uint256

The fee for the flash loan

data

bytes

Arbitrary data containing the parameters needed for the operation

###### Return Values:

Type

Description

bytes32

The keccak256 hash of the string 'ERC3156FlashBorrower.onFlashLoan'

* * *

### Withdraw & Switch

[](#withdraw-switch)

The ParaSwapWithdrawSwapAdapter contract allows users to withdraw their supplied assets from Aave and switch them to another asset in a single transaction using the ParaSwap DEX aggregator.

This adapter enables users to efficiently exit positions and switch their assets without having to perform multiple transactions, reducing gas costs and simplifying the user experience.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/extensions/paraswap-adapters/ParaSwapWithdrawSwapAdapter.sol).

Reference Integration: [WithdrawAndSwitchActions.tsx](https://github.com/aave/interface/blob/main/src/components/transactions/Withdraw/WithdrawAndSwitchActions.tsx)

#### Write Methods

[](#withdraw-switch-write-methods)

##### withdrawAndSwap

[](#withdraw-switch-write-methods-withdrawandswap)

```
function withdrawAndSwap(    IERC20Detailed assetToSwapFrom,    IERC20Detailed assetToSwapTo,    uint256 amountToSwap,    uint256 minAmountToReceive,    uint256 swapAllBalanceOffset,    bytes calldata swapCalldata,    IParaSwapAugustus augustus,    PermitSignature calldata permitParams) external nonReentrant
```

Switches an amount of an asset to another after a withdrawal and transfers the new asset to the user. The user should give this contract allowance to pull the aTokens in order to withdraw the underlying asset and perform the switch.

###### Input Parameters:

Name

Type

Description

assetToSwapFrom

IERC20Detailed

The address of the underlying asset to be switched from

assetToSwapTo

IERC20Detailed

The address of the underlying asset to be switched to

amountToSwap

uint256

Amount to be switched, or maximum amount when switching all balance

minAmountToReceive

uint256

Minimum amount to be received from the switch

swapAllBalanceOffset

uint256

Offset in Augustus calldata if switching all balance, otherwise 0

swapCalldata

bytes

Calldata for ParaSwap's Augustus Swapper contract

augustus

IParaSwapAugustus

Address of ParaSwap's Augustus Swapper contract

permitParams

PermitSignature

Struct containing the permit signature, set to zeroes if not used

##### executeOperation

[](#withdraw-switch-write-methods-executeoperation)

Note that in this contract, the executeOperation method is overridden but simply reverts with NOT\_SUPPORTED, so it's not intended to be used.

[

Previous

**Pool Configurator**

](/docs/developers/smart-contracts/pool-configurator)[

Next

**GHO**

](/docs/developers/gho)

---

<a id="doc_32"></a>

## 📁 developers/smart_contracts / Tokenization | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/tokenization.md*

Source: https://aave.com/docs/developers/smart-contracts/tokenization

## Tokenization

[](#tokenization)

## AToken

[](#atoken)

aTokens are tokens minted and burnt upon supply and withdraw of assets to an Aave market. aTokens denote the amount of crypto assets supplied to the protocol and the yield earned on those assets. The aTokens’ value is pegged to the value of the corresponding supplied asset at a 1:1 ratio and can be safely stored, transferred or traded. All yield collected by the aTokens' reserves are distributed to aToken holders directly by continuously increasing their wallet balance.

This contract is the implementation of the interest bearing token for the Aave Protocol. It inherits the [ScaledBalanceTokenBase](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/base/ScaledBalanceTokenBase.sol) and [EIP712Base](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/base/EIP712Base.sol) token contracts.

All standard EIP20 methods are implemented for aTokens, such as balanceOf, transfer, transferFrom, approve, totalSupply etc.

balanceOf will always return the most up to date balance of the user, which includes their principal balance and the yield generated by the principal balance.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/AToken.sol).

### Write Methods

[](#write-methods)

#### initialize

[](#write-methods-initialize)

```
function initialize(    IPool initializingPool,    address treasury,    address underlyingAsset,    IAaveIncentivesController incentivesController,    uint8 aTokenDecimals,    string calldata aTokenName,    string calldata aTokenSymbol,    bytes calldata params) public virtual
```

Called when aToken instance is initialized.

##### Input Parameters:

[](#write-methods-initialize-input-parameters)

Name

Type

Description

initializingPool

IPool

The address of the associated pool

treasury

address

The address of the treasury

underlyingAsset

address

The address of the underlying asset

incentivesController

IAaveIncentivesController

The address of the incentives controller for this aToken

aTokenDecimals

uint8

The decimals of the underlying asset

aTokenName

string

The name of the aToken

aTokenSymbol

string

The symbol of the aToken

params

bytes

A set of encoded parameters for additional initialization

#### mint

[](#write-methods-mint)

```
function mint(    address caller,    address onBehalfOf,    uint256 amount,    uint256 index) external virtual override onlyPool returns (bool)
```

Mints amount aTokens to user.

##### Input Parameters:

[](#write-methods-mint-input-parameters)

Name

Type

Description

caller

address

The address performing the mint

onBehalfOf

address

The address of the user that will receive the minted aTokens

amount

uint256

The amount of tokens getting minted

index

uint256

The next liquidity index of the reserve

##### Return Values:

[](#write-methods-mint-return-values)

Type

Description

bool

true if the the previous balance of the user was 0

#### burn

[](#write-methods-burn)

```
function burn(    address from,    address receiverOfUnderlying,    uint256 amount,    uint256 index) external virtual override onlyPool
```

Burns aTokens from user and sends the equivalent amount of underlying to receiverOfUnderlying.

In some instances, the mint event could be emitted from a burn transaction if the amount to burn is less than the interest that the user accrued.

##### Input Parameters:

[](#write-methods-burn-input-parameters)

Name

Type

Description

from

address

The address from which the aTokens will be burned

receiverOfUnderlying

address

The address that will receive the underlying asset

amount

uint256

The amount of tokens that will be burned

index

uint256

The next liquidity index of the reserve

#### mintToTreasury

[](#write-methods-minttotreasury)

```
function mintToTreasury(uint256 amount, uint256 index) external override onlyPool
```

Mints aTokens to the reserve treasury.

##### Input Parameters:

[](#write-methods-minttotreasury-input-parameters)

Name

Type

Description

amount

uint256

The amount of tokens getting minted

index

uint256

The address that will receive the underlying asset

#### transferOnLiquidation

[](#write-methods-transferonliquidation)

```
function transferOnLiquidation(    address from,    address to,    uint256 value) virtual override onlyPool
```

Transfers aTokens in the event of a borrow being liquidated, in case the liquidator reclaims the aToken.

##### Input Parameters:

[](#write-methods-transferonliquidation-input-parameters)

Name

Type

Description

from

address

The address getting liquidated, current owner of the aTokens

to

address

The recipient of aTokens

value

uint256

The amount of tokens getting transferred

#### transferUnderlyingTo

[](#write-methods-transferunderlyingto)

```
function transferUnderlyingTo(address target, uint256 amount) external virtual override onlyPool
```

Transfers the underlying asset to target.

Used by the [Pool](/docs/developers/pool/Pool.md) to transfer assets in borrow(), withdraw() and flashLoan().

##### Input Parameters:

[](#write-methods-transferunderlyingto-input-parameters)

Name

Type

Description

user

address

The recipient of the underlying

amount

uint256

The amount getting transferred

#### handleRepayment

[](#write-methods-handlerepayment)

```
function handleRepayment(address user, address onBehalfOf, uint256 amount) external virtual override onlyPool
```

Handles the underlying received by the aToken after the transfer has been completed.

The default implementation is empty as with standard ERC20 tokens, nothing needs to be done after the transfer is concluded. However in the future there may be aTokens that allow for example to stake the underlying to receive LM rewards. In that case, handleRepayment() would perform the staking of the underlying asset.

##### Input Parameters:

[](#write-methods-handlerepayment-input-parameters)

Name

Type

Description

user

address

The user executing the repayment

onBehalfOf

address\`

The address for which the borrow position is repaid

amount

uint256

The amount getting repaid

#### permit

[](#write-methods-permit)

```
function permit(    address owner,    address spender,    uint256 value,    uint256 deadline,    uint8 v,    bytes32 r,    bytes32 s) external override
```

Allows a user to permit another account (or contract) to use their funds using a signed message. This enables gas-less transactions and single approval/transfer transactions. Allow passing a signed message to approve spending.

Implements the permit function as for EIP-2612.

##### Input Parameters:

[](#write-methods-permit-input-parameters)

Name

Type

Description

owner

address

The owner of the funds

spender

address

The spender of the funds

value

uint256

The amount the spender is permitted to spend

deadline

uint256

The deadline timestamp, use type(uint256).max for max/no deadline

v

uint8

The V signature parameter

r

bytes32

The R signature parameter

s

bytes32

The S signature parameter

Example of signing and utilizing permit:

```
import { signTypedData_v4 } from "eth-sig-util";import { fromRpcSig } from "ethereumjs-util";// ... other importsimport aTokenAbi from "./aTokenAbi.json";// ... setup your web3 providerconst aTokenAddress = "ATOKEN_ADDRESS";const aTokenContract = new web3.eth.Contract(aTokenAbi, aTokenAddress);const privateKey = "YOUR_PRIVATE_KEY_WITHOUT_0x";const chainId = 1;const owner = "OWNER_ADDRESS";const spender = "SPENDER_ADDRESS";const value = 100; // Amount the spender is permittedconst nonce = 1; // The next valid nonce, use `_nonces()`const deadline = 1600093162;const permitParams = {  types: {    EIP712Domain: [      { name: "name", type: "string" },      { name: "version", type: "string" },      { name: "chainId", type: "uint256" },      { name: "verifyingContract", type: "address" },    ],    Permit: [      { name: "owner", type: "address" },      { name: "spender", type: "address" },      { name: "value", type: "uint256" },      { name: "nonce", type: "uint256" },      { name: "deadline", type: "uint256" },    ],  },  primaryType: "Permit",  domain: {    name: "aTOKEN_NAME",    version: "1",    chainId: chainId,    verifyingContract: aTokenAddress,  },  message: {    owner,    spender,    value,    nonce,    deadline,  },};const signature = signTypedData_v4(Buffer.from(privateKey, "hex"), {  data: permitParams,});// The signature can now be used to execute the transactionconst { v, r, s } = fromRpcSig(signature);await aTokenContract.methods  .permit({    owner,    spender,    value,    deadline,    v,    r,    s,  })  .send()  .catch((e) => {    throw Error(`Error permitting: ${e.message}`);  });
```

#### rescueTokens

[](#write-methods-rescuetokens)

```
function rescueTokens(    address token,    address to,    uint256 amount) external override onlyPoolAdmin
```

Rescue and transfer tokens locked in this contract. Only callable by [POOL\_ADMIN](/docs/developers/smart-contracts/acl-manager#roles-pool-admin).

##### Input Parameters:

[](#write-methods-rescuetokens-input-parameters)

Name

Type

Description

token

address

The address of the token

to

address

The address of the recipient

amount

uint256

The amount of token to transfer

### View Methods

[](#view-methods)

#### balanceOf

[](#view-methods-balanceof)

```
function balanceOf(address user)    public    view    virtual    override(IncentivizedERC20, IERC20)    returns (uint256)
```

Returns the amount of tokens owned by user.

Overrides the base function.

##### Input Parameters:

[](#view-methods-balanceof-input-parameters)

Name

Type

Description

user

address

The address of the user

##### Return Values:

[](#view-methods-balanceof-return-values)

Type

Description

uint256

The amount of tokens owned by user

#### totalSupply

[](#view-methods-totalsupply)

```
function totalSupply() public view virtual override(IncentivizedERC20, IERC20 returns (uint256)
```

Returns the amount of tokens in existence.

Overrides the base function.

##### Return Values:

[](#view-methods-totalsupply-return-values)

Type

Description

uint256

The amount of tokens in existence

#### RESERVE\_TREASURY\_ADDRESS

[](#view-methods-reserve-treasury-address)

```
function RESERVE_TREASURY_ADDRESS() external view override returns (address)
```

Returns the address of the Aave treasury, controlled by governance, receiving the fees on this aToken.

##### Return Values:

[](#view-methods-reserve-treasury-address-return-values)

Type

Description

address

The address of the Aave treasury

#### UNDERLYING\_ASSET\_ADDRESS

[](#view-methods-underlying-asset-address)

```
function UNDERLYING_ASSET_ADDRESS() external view override returns (address)
```

Returns the address of the underlying reserve asset of this aToken (E.g. WETH for aWETH).

##### Return Values:

[](#view-methods-underlying-asset-address-return-values)

Type

Description

address

The address of the underlying asset

#### DOMAIN\_SEPARATOR

[](#view-methods-domain-separator)

```
function DOMAIN_SEPARATOR() public view override(IAToken, EIP712Base) returns (bytes32)
```

Get the domain separator for the token at the current chain.

Return cached value if chainId matches cache, otherwise recomputes separator.

Overrides the base function to fully implement IAToken.

##### Return Values:

[](#view-methods-domain-separator-return-values)

Type

Description

bytes32

The domain separator of the token at current chain

#### nonces

[](#view-methods-nonces)

```
function nonces(address owner) public view override(IAToken, EIP712Base) returns (uint256)
```

Returns the nonce value for address specified as parameter. This is the nonce used when calling permit().

Overrides the base function to fully implement IAToken.

##### Input Parameters:

[](#view-methods-nonces-input-parameters)

Name

Type

Description

owner

address

The address of the owner

##### Return Values:

[](#view-methods-nonces-return-values)

Type

Description

uint256

The nonce of the owner

Example:

```
const token = new Contract(aTokenAddress, aToken.abi, provider);await token.nonces(user);
```

### Pure Methods

[](#pure-methods)

#### getRevision

[](#pure-methods-getrevision)

```
function getRevision() internal pure virtual override returns (uint256)
```

Returns the revision number of the contract. Needs to be defined in the inherited class as a constant.

Returns 0x1.

##### Return Values:

[](#pure-methods-getrevision-return-values)

Type

Description

uint256

The revision number

## StaticATokenFactory

[](#staticatokenfactory)

The StataTokenFactory is a factory and registry contract that manages all deployed StataToken instances for a specified Aave pool. It allows deploying new StataToken instances on demand and validates that there is only one StataToken instance per underlying asset. This contract maintains a mapping between underlying assets and their corresponding StataToken addresses.

StataTokens are ERC-4626 compliant tokens that wrap Aave's aTokens to provide a non-rebasing yield accrual mechanism.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/StataTokenFactory.sol).

### Write Methods

[](#write-methods)

#### initialize

[](#write-methods-initialize)

```
function initialize() external initializer
```

Initializes the StataTokenFactory contract. This function is part of the Initializable pattern and is required to initialize the contract after deployment. In this implementation, it does not perform any actions.

#### createStataTokens

[](#write-methods-createstatatokens)

```
function createStataTokens(address[] memory underlyings) external returns (address[] memory)
```

Creates new StataToken instances for the given underlying assets if they do not already exist. For each provided underlying asset, the function checks if a StataToken already exists. If it does, the existing StataToken address is returned. If not, it deploys a new StataToken for that underlying asset, registers it, and returns the new address.

##### Input Parameters:

[](#write-methods-createstatatokens-input-parameters)

Name

Type

Description

underlyings

address\[\]

An array of underlying asset addresses

##### Return Values:

[](#write-methods-createstatatokens-return-values)

Type

Description

address\[\]

An array of StataToken addresses corresponding to the provided underlying assets

##### Emits:

[](#write-methods-createstatatokens-emits)

*   StataTokenCreated(address indexed stataToken, address indexed underlying) event for each new StataToken created.
    

##### Reverts:

[](#write-methods-createstatatokens-reverts)

*   NotListedUnderlying(address underlying) if the underlying asset is not listed in the Aave pool.
    

### View Methods

[](#view-methods)

#### getStataTokens

[](#view-methods-getstatatokens)

```
function getStataTokens() external view returns (address[] memory)
```

Returns all StataToken instances deployed via this factory.

##### Return Values:

[](#view-methods-getstatatokens-return-values)

Type

Description

address\[\]

An array of all StataToken contract addresses

#### getStataToken

[](#view-methods-getstatatoken)

```
function getStataToken(address underlying) external view returns (address)
```

Returns the StataToken address for a given underlying asset.

##### Input Parameters:

[](#view-methods-getstatatoken-input-parameters)

Name

Type

Description

underlying

address

The address of the underlying asset

##### Return Values:

[](#view-methods-getstatatoken-return-values)

Type

Description

address

The address of the corresponding StataToken; returns address(0) if not found

#### POOL

[](#view-methods-pool)

```
function POOL() external view returns (IPool)
```

Returns the address of the Aave pool associated with this factory.

##### Return Values:

[](#view-methods-pool-return-values)

Type

Description

IPool

The address of the associated Aave pool

#### PROXY\_ADMIN

[](#view-methods-proxy-admin)

```
function PROXY_ADMIN() external view returns (address)
```

Returns the address of the proxy admin used for the StataToken proxies.

##### Return Values:

[](#view-methods-proxy-admin-return-values)

Type

Description

address

The address of the proxy admin

#### TRANSPARENT\_PROXY\_FACTORY

[](#view-methods-transparent-proxy-factory)

```
function TRANSPARENT_PROXY_FACTORY() external view returns (ITransparentProxyFactory)
```

Returns the address of the transparent proxy factory used for creating new StataToken proxies.

##### Return Values:

[](#view-methods-transparent-proxy-factory-return-values)

Type

Description

ITransparentProxyFactory

The address of the transparent proxy factory

#### STATA\_TOKEN\_IMPL

[](#view-methods-stata-token-impl)

```
function STATA_TOKEN_IMPL() external view returns (address)
```

Returns the address of the StataToken implementation used when deploying new StataToken instances.

##### Return Values:

[](#view-methods-stata-token-impl-return-values)

Type

Description

address

The address of the StataToken implementation

## VariableDebtToken

[](#variabledebttoken)

Implements a variable debt token to track the borrowing positions of users at variable rate mode.

transfer and approve functionalities are disabled as variable debt tokens are non-transferable.

The vToken value is pegged 1:1 to the value of underlying borrowed asset and represents the current total amount owed to the protocol i.e. principal debt + interest accrued.

The VariableDebtToken contract inherits the [DebtTokenBase](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/base/DebtTokenBase.sol) and [ScaledBalanceTokenBase](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/base/ScaledBalanceTokenBase.sol) token contracts.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/tokenization/VariableDebtToken.sol).

### Write Methods

[](#write-methods)

#### initialize

[](#write-methods-initialize)

```
function initialize(    IPool initializingPool,    address underlyingAsset,    IAaveIncentivesController incentivesController,    uint8 debtTokenDecimals,    string memory debtTokenName,    string memory debtTokenSymbol,    bytes calldata params) external virtual
```

Called when variableDebtToken instance is initialised.

##### Input Parameters:

[](#write-methods-initialize-input-parameters)

Name

Type

Description

initializingPool

IPool

The pool contract that is initializing this contract

underlyingAsset

address

The address of the underlying asset of this aToken (E.g. WETH for aWETH)

incentivesController

IAaveIncentivesController

The smart contract managing potential incentives distribution

debtTokenDecimals

uint8

The decimals of the variableDebtToken, same as the underlying asset's

debtTokenName

string

The name of the variable debt token

debtTokenSymbol

string

The symbol of the variable debt token

params

bytes

A set of encoded parameters for additional initialization

#### mint

[](#write-methods-mint)

```
function mint(    address user,    address onBehalfOf,    uint256 amount,    uint256 index) external virtual override onlyPool returns (bool, uint256)
```

Mints the variable debt token to the onBehalfOf address.

##### Input Parameters:

[](#write-methods-mint-input-parameters)

Name

Type

Description

user

address

The address receiving the borrowed underlying, being the delegatee in case of credit delegate, or same as onBehalfOf otherwise

onBehalfOf

address

The address receiving the variable debt tokens

amount

uint256

The amount of variable debt tokens to mint

index

uint256

The variable debt index of the reserve

##### Return Values:

[](#write-methods-mint-return-values)

Type

Description

bool

true if the previous balance of the user is 0, false otherwise

uint256

The scaled total debt of the reserve

#### burn

[](#write-methods-burn)

```
function burn(    address from,    uint256 amount,    uint256 index) external virtual override onlyPool returns (uint256)
```

Burns user variable debt.

In some instances, a burn transaction will emit a mint event if the amount to burn is less than the interest that the user accrued.

##### Input Parameters:

[](#write-methods-burn-input-parameters)

Name

Type

Description

from

address

The address from which the debt will be burned

amount

uint256

The amount of debt tokens that will be burned

index

uint256

The variable debt index of the reserve

##### Return Values:

[](#write-methods-burn-return-values)

Type

Description

uint256

The scaled total debt of the reserve

### View Methods

[](#view-methods)

#### UNDERLYING\_ASSET\_ADDRESS

[](#view-methods-underlying-asset-address)

```
function UNDERLYING_ASSET_ADDRESS() external view override returns (address)
```

Returns the address of the underlying asset of this variableDebtToken (e.g. WETH for variableDebtWETH)

##### Return Values:

[](#view-methods-underlying-asset-address-return-values)

Type

Description

address

The address of the underlying asset

#### balanceOf

[](#view-methods-balanceof)

```
function balanceOf(address account) public view virtual override returns (uint256)
```

Returns the amount of tokens owned by account - the most up to date accumulated debt (principal + interest) of the user.

Standard ERC20 function.

##### Input Parameters:

[](#view-methods-balanceof-input-parameters)

Name

Type

Description

account

address

The balance of this address

##### Return Values:

[](#view-methods-balanceof-return-values)

Type

Description

uint256

The amount of tokens owned by account

#### totalSupply

[](#view-methods-totalsupply)

```
function totalSupply() public view virtual override returns (uint256)
```

Returns the amount of tokens in existence - the most up to date total debt accrued by all protocol users for that specific variable rate of debt token.

Standard ERC20 function.

##### Return Values:

[](#view-methods-totalsupply-return-values)

Type

Description

uint256

The amount of tokens in existence

### Pure Methods

[](#pure-methods)

#### getRevision

[](#pure-methods-getrevision)

```
function getRevision() internal pure virtual override returns (uint256)
```

Returns the revision number of the contract. Needs to be defined in the inherited class as a constant.

Returns 0x1.

##### Return Values:

[](#pure-methods-getrevision-return-values)

Type

Description

uint256

The revision number

### NOT SUPPORTED OPERATIONS

[](#not-supported-operations)

Being non-transferrable, the variable debt token does not implement any of the standard ERC20 functions for transfer and allowance.

The following functions below will revert with the error code 80, OPERATION\_NOT\_SUPPORTED: transfer, allowance, approve, transferFrom, increaseAllowance, decreaseAllowance.

[

Previous

**Incentives**

](/docs/developers/smart-contracts/incentives)[

Next

**Interest Rate Strategy**

](/docs/developers/smart-contracts/interest-rate-strategy)

---

<a id="doc_33"></a>

## 📁 developers/smart_contracts / View Contracts | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/view_contracts.md*

Source: https://aave.com/docs/developers/smart-contracts/view-contracts

## View Contracts

[](#view-contracts)

The Aave Protocol has several view contracts to assist with querying onchain data.

### UiPoolDataProvider

[](#uipooldataprovider)

Contract that returns an array of all reserve or user data for a particular market (for example, liquidity, token addresses, rate strategy), used by the [Aave Interface](https://github.com/aave/interface/) to display Markets and Dashboard data. Compatible with both V2 and V3 of the Aave Protocol.

The [Aave Utilities SDK](https://github.com/aave/aave-utilities) includes an interface to make calls to this contract, and functions to format the response for frontend use-cases.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/UiPoolDataProviderV3.sol).

### View Methods

[](#view-methods)

#### getReservesList

[](#view-methods-getreserveslist)

```
function getReservesList(IPoolAddressesProvider provider) public view override returns (address[] memory)
```

Returns the list of initialised reserves in the Pool associated with the given [provider](/docs/developers/smart-contracts/pool-addresses-provider).

##### Input Parameters:

[](#view-methods-getreserveslist-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The given provider for the associated pool

##### Return Values:

[](#view-methods-getreserveslist-return-values)

Type

Description

address\[\]

The list of initialised reserves in the Pool

#### getReservesData

[](#view-methods-getreservesdata)

```
function getReservesData(IPoolAddressesProvider provider) public view override returns (AggregatedReserveData[] memory, BaseCurrencyInfo memory)
```

Returns BaseCurrencyInfo of the Pool and AggregatedReserveData\[\] for all the initialised reserves in the Pool associated with the given [provider](/docs/developers/smart-contracts/pool-addresses-provider).

##### Input Parameters:

[](#view-methods-getreservesdata-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The given provider for the associated pool

##### Return Values:

[](#view-methods-getreservesdata-return-values)

Type

Description

BaseCurrencyInfo

The base currency information

AggregatedReserveData\[\]

The aggregated reserve data

The BaseCurrencyInfo struct is composed of the following fields:

Name

Type

Description

marketReferenceCurrencyUnit

uint256

Reference aka base currency of the Aave market

marketReferenceCurrencyPriceInUsd

int256

Price of reference aka base currency in USD

networkBaseTokenPriceInUsd

int256

Price of native token of the network/chain in USD

networkBaseTokenPriceDecimals

uint8

Decimals of native token of the network/chain

The AggregatedReserveData struct is composed of the following fields:

Name

Type

Description

underlyingAsset

address

The address of the underlying asset of the reserve

name

string

The name of the underlying reserve asset

symbol

string

The symbol of the underlying reserve asset

decimals

uint256

The number of decimals of the reserve

baseLTVasCollateral

uint256

The ltv of the reserve

reserveLiquidationThreshold

uint256

The liquidation threshold of the reserve

reserveLiquidationBonus

uint256

The liquidation bonus of the resurve

reserveFactor

uint256

The reserve factor of the reserve

usageAsCollateralEnabled

bool

true if the asset is enabled to be used as collateral, false otherwise

borrowingEnabled

bool

true if borrowing is enabled, false otherwise

isActive

bool

true if reserve is active, false otherwise

isFrozen

bool

true if reserve is frozen, false otherwise

BASE DATA

liquidityIndex

uint128

The liquidity index of the reserve

variableBorrowIndex

uint128

The variable borrow index of the reserve

liquidityRate

uint128

The liquidity rate of the reserve

variableBorrowRate

uint128

The variable borrow rate of the reserve

lastUpdateTimestamp

uint40

The timestamp of the last update of the reserve

aTokenAddress

address

The AToken address of the reserve

variableDebtTokenAddress

address

The VariableDebtToken address of the reserve

interestRateStrategyAddress

address

The address of the Interest Rate strategy

availableLiquidity

uint256

The liquidity available

totalScaledVariableDebt

uint256

The total scaled variable debt

priceInMarketReferenceCurrency

uint256

Price of reference aka base currency of Aave market

priceOracle

address

The address of the price oracle used by the associated market

variableRateSlope1

uint256

The variable rate slope

variableRateSlope2

uint256

The variable rate slope

baseVariableBorrowRate

uint256

The base variable borrow rate, expressed in ray

optimalUsageRatio

uint256

The optimal usage ratio

V3 ONLY

isPaused

bool

true if the pool is paused, false otherwise

isSiloedBorrowing

bool

true if the asset is siloed for borrowing

accruedToTreasury

uint128

The amount of tokens accrued to treasury that is to be minted

unbacked

uint128

The amount of unbacked aTokens of the reserve

isolationModeTotalDebt

uint128

The outstanding debt borrowed against this asset in isolation mode

flashLoanEnabled

bool

true is asset is available to borrow in flash loan transaction

debtCeiling

uint256

The debt ceiling of the reserve

debtCeilingDecimals

uint256

The debt ceiling decimals

eModeCategoryId

uint8

The eMode id of the reserve

borrowCap

uint256

The borrow cap of the reserve

supplyCap

uint256

The supply cap of the reserve

borrowableInIsolation

bool

true is asset available to borrow against isolated collateral assets

v3.1

virtualAccActive

bool

true if virtual accounting is enabled for a reserve

virtualUnderlyingBalance

uint128

Balance of reserve if virtual accounting is used

#### getUserReservesData

[](#view-methods-getuserreservesdata)

```
function getUserReservesData(IPoolAddressesProvider provider, address user) external view override returns (UserReserveData[] memory, uint8)
```

Returns UserReserveData\[\] for all user reserves in the Pool associated with the given [provider](/docs/core-contracts/interfaces/IPoolAddressesProvider).

##### Input Parameters:

[](#view-methods-getuserreservesdata-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The given provider for the associated pool

user

address

The address of the user

#### UserReserveData

[](#view-methods-userreservedata)

Type

Description

UserReserveData\[\]

The user reserve data

The [UserReserveData](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/interfaces/IUiPoolDataProviderV3.sol) struct is composed of the following fields:

Name

Type

Description

underlyingAsset

address

The address of the underlying asset supplied/borrowed

scaledATokenBalance

uint256

The scaled balance of the aToken. scaledBalance = balance/liquidityIndex

usageAsCollateralEnabledOnUser

bool

true if the supplied asset is enabled to be used as collateral, false otherwise

scaledVariableDebt

uint256

The scaled balance of borrow position: (current balance = scaled balance \* liquidity index)

#### getEModes

[](#view-methods-getemodes)

Returns an array of all available E-mode categories in the Pool associated with the [provider](/docs/developers/smart-contracts/pool-addresses-provider).

```
function getEModes(IPoolAddressesProvider provider) external view returns (Emode[] memory)
```

##### Input Parameters:

[](#view-methods-getemodes-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The PoolAddressesProvider for the associated Pool to fetch EMode categories for

##### Return Parameters:

[](#view-methods-getemodes-return-parameters)

Name

Type

Description

categories

Emode\[\]

The list of E-Modes available in the pool

##### Emode

[](#view-methods-getemodes-emode)

The Emode struct is composed of the following fields:

Name

Type

Description

id

uint8

The unique identifier of the E-Mode

eMode

DataTypes.EModeCategory

The E-Mode configuration details

##### DataTypes.EModeCategory

[](#view-methods-getemodes-datatypesemodecategory)

The EModeCategory struct is composed of the following fields:

Name

Type

Description

ltv

uint16

Loan-to-Value ratio for the E-Mode category

liquidationThreshold

uint16

The threshold at which liquidation is triggered

liquidationBonus

uint16

The bonus applied during liquidation

collateralBitmap

uint128

Bitmap representing eligible collateral for this E-Mode

label

string

The label describing the E-Mode category

borrowableBitmap

uint128

Bitmap representing borrowable assets for this E-Mode

### WalletBalanceProvider

[](#walletbalanceprovider)

Fetches tokens balances for all underlying tokens of Aave reserves for one user address.

This contract is not used within the Aave Protocol. It is an accessory contract used to reduce the number of calls towards the blockchain from the Aave backend.

For getting ETH (native chain token) balance use MOCK\_ETH\_ADDRESS = 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/WalletBalanceProvider.sol).

### View Methods

[](#view-methods)

#### balanceOf

[](#view-methods-balanceof)

```
function balanceOf(address user, address token) public view returns (uint256)
```

Checks the token balance of a wallet in a token contract. Returns the balance of the token for user (ETH included with MOCK\_ETH\_ADDRESS).

##### Input Parameters:

[](#view-methods-balanceof-input-parameters)

Name

Type

Description

user

address

The address of the user

token

address

The address of the token

##### Return Values:

[](#view-methods-balanceof-return-values)

Type

Description

uint256

The balance of the token for user. Returns 0 for a non-contract address

#### batchBalanceOf

[](#view-methods-batchbalanceof)

```
function batchBalanceOf(address[] calldata users, address[] calldata tokens) external view returns (uint256[] memory)
```

Returns balances for a list of users and tokens (ETH included with MOCK\_ETH\_ADDRESS).

##### Input Parameters:

[](#view-methods-batchbalanceof-input-parameters)

Name

Type

Description

users

address\[\]

The list of users

tokens

address\[\]

The list of tokens

##### Return Values:

[](#view-methods-batchbalanceof-return-values)

Type

Description

uint256\[\]

A list of balances for each user

#### getUserWalletBalances

[](#view-methods-getuserwalletbalances)

```
function getUserWalletBalances(address provider, address user) external view returns (address[] memory, uint256[] memory)
```

Provides balances of user wallet for all reserves available on the pool.

##### Input Parameters:

[](#view-methods-getuserwalletbalances-input-parameters)

Name

Type

Description

provider

address

The address of the provider

user

address

The address of the user

##### Return Values:

[](#view-methods-getuserwalletbalances-return-values)

Type

Description

address\[\]

A list of user wallets

uint256\[\]

A list of balances for each user

## UiIncentiveDataProviderV3

[](#uiincentivedataproviderv3)

Contract that returns an array of all reserve incentives or user claimable rewards within a particular market, used by the [Aave Labs Interface](https://github.com/aave/interface/) to display incentives data. Compatible with both V2 and V3 of the Aave Protocol.

The [Aave Utilities SDK](https://github.com/aave/aave-utilities) includes an interface to make calls to this contract, and functions to format the response for frontend use-cases.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/UiIncentiveDataProviderV3.sol).

### View Methods

[](#view-methods)

##### getFullReservesIncentiveData

[](#view-methods-getuserwalletbalances-getfullreservesincentivedata)

```
function getFullReservesIncentiveData(IPoolAddressesProvider provider, address user)    external    view    override    returns (AggregatedReserveIncentiveData[] memory, UserReserveIncentiveData[] memory)
```

Returns both AggregatedReserveIncentiveData\[\] and UserReserveIncentiveData\[\] for the given user for the pool associated with the given [provider](/docs/core_contracts/interfaces/IPoolAddressesProvider).

##### Input Parameters:

[](#view-methods-getuserwalletbalances-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The given provider for the associated pool

user

address

The address of the user

##### Return Values:

[](#view-methods-getuserwalletbalances-return-values)

Type

Description

AggregatedReserveIncentiveData\[\]

The aggregated reserve incentive data

UserReserveIncentiveData\[\]

The user reserve incentive data

The AggregatedReserveIncentiveData struct is composed of the following fields:

Name

Type

Description

underlyingAsset

address

Address of the asset supplied/borrowed in Pool

aIncentiveData

IncentiveData

Details of rewards distributed for supplying to Aave Pool i.e. rewards for aToken holders

vIncentiveData

IncentiveData

Details of rewards distributed for variable debt borrowed from Aave Pool i.e. rewards for vToken holders

The UserReserveIncentiveData struct is composed of the following fields:

Name

Type

Description

underlyingAsset

address

Address of the asset supplied/borrowed in Pool

aTokenIncentivesUserData

UserIncentiveData

Details of user rewards received for supplying to Aave Pool i.e. rewards for aToken

vTokenIncentivesUserData

UserIncentiveData

Details of user rewards received for borrowing at variable rate from Aave Pool i.e. rewards for vToken

##### getReservesIncentivesData

[](#view-methods-getuserwalletbalances-getreservesincentivesdata)

```
function getReservesIncentivesData(IPoolAddressesProvider provider) external view override returns (AggregatedReserveIncentiveData[] memory)
```

Returns AggregatedReserveIncentiveData\[\] for the pool associated with the given [provider](/docs/developers/smart-contracts/pool-addresses-provider).

##### Input Parameters:

[](#view-methods-getuserwalletbalances-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The given provider for the associated pool

##### Return Values:

[](#view-methods-getuserwalletbalances-return-values)

Type

Description

AggregatedReserveIncentiveData\[\]

The aggregated reserve incentive data

The AggregatedReserveIncentiveData struct is composed of the following fields:

Name

Type

Description

underlyingAsset

address

Address of the asset supplied/borrowed in Pool

aIncentiveData

IncentiveData

Details of rewards distributed for supplying to Aave Pool i.e. rewards for aToken holders

vIncentiveData

IncentiveData

Details of rewards distributed for variable debt borrowed from Aave Pool i.e. rewards for vToken holders

##### getUserReservesIncentivesData

[](#view-methods-getuserwalletbalances-getuserreservesincentivesdata)

```
function getUserReservesIncentivesData(IPoolAddressesProvider provider, address user) external view override returns (UserReserveIncentiveData[] memory)
```

Returns the UserReserveIncentiveData\[\] for the given user for the pool associated with the given [provider](/docs/developers/smart-contracts/pool-addresses-provider).

##### Input Parameters:

[](#view-methods-getuserwalletbalances-input-parameters)

Name

Type

Description

provider

IPoolAddressesProvider

The given provider for the associated pool

##### Return Values:

[](#view-methods-getuserwalletbalances-return-values)

Type

Description

UserReserveIncentiveData\[\]

The user reserve incentive data

The UserReserveIncentiveData struct is composed of the following fields:

Name

Type

Description

underlyingAsset

address

Address of the asset supplied/borrowed in Pool

aTokenIncentivesUserData

UserIncentiveData

Details of user rewards received for supplying to Aave Pool i.e. rewards for aToken

vTokenIncentivesUserData

UserIncentiveData

Details of user rewards received for borrowing at variable rate from Aave Pool i.e. rewards for vToken

### AaveProtocolDataProvider

[](#aaveprotocoldataprovider)

The AaveProtocolDataProvider is a peripheral contract to collect and pre-process information from the [Pool](/docs/developers/smart-contracts/pool). This contract contains methods for querying token addresses, reserve parameters, and user account information. The methods of the PoolDataProvider are more granular than the UiPoolDataProvider, which queries data for reserve tokens or user balances simultaneously.

The source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/AaveProtocolDataProvider.sol).

### View Methods

[](#view-methods)

#### getAllReservesTokens

[](#view-methods-getallreservestokens)

```
function getAllReservesTokens() external view returns (TokenData[] memory)
```

Returns a list of the existing reserves in the pool, pairs include the symbol and tokenAddress. Handles MKR and ETH in a different way since they do not have standard symbol functions.

##### Return Values:

[](#view-methods-getallreservestokens-return-values)

Type

Description

TokenData\[\]

The list of reserves, pairs of symbols and addresses

The TokenData struct is composed of the following fields:

Name

Type

Description

symbol

string

The symbol of the underlying reserve asset

tokenAddress

address

The address of the underlying reserve asset

#### getAllATokens

[](#view-methods-getallatokens)

```
function getAllATokens() external view returns (TokenData[] memory)
```

Returns a list of the existing ATokens in the pool, pairs include the symbol and tokenAddress.

##### Return Values:

[](#view-methods-getallatokens-return-values)

Type

Description

TokenData\[\]

The list of ATokens, pairs of symbols and addresses

The TokenData struct is composed of the following fields:

Name

Type

Description

symbol

string

The symbol of aToken of the reserve

tokenAddress

address

The address of aToken of the reserve

#### getReserveConfigurationData

[](#view-methods-getreserveconfigurationdata)

```
function getReserveConfigurationData(address asset) external view returns (    uint256 decimals,    uint256 ltv,    uint256 liquidationThreshold,    uint256 liquidationBonus,    uint256 reserveFactor,    bool usageAsCollateralEnabled,    bool borrowingEnabled,    bool stableBorrowRateEnabled,    bool isActive,    bool isFrozen)
```

Returns the configuration data of the reserve as described below. Does not return borrow and supply caps, nor pause flag for compatibility.

##### Input Parameters:

[](#view-methods-getreserveconfigurationdata-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreserveconfigurationdata-return-values)

Name

Type

Description

decimals

uint256

The number of decimals of the reserve

ltv

uint256

The ltv of the reserve

liquidationThreshold

uint256

The liquidation threshold of the reserve

liquidationBonus

uint256

The liquidation bonus of the reserve

reserveFactor

uint256

The reserve factor of the reserve

usageAsCollateralEnabled

bool

true if the usage as collateral is enabled, false otherwise

borrowingEnabled

bool

true if borrowing is enabled, false otherwise

stableBorrowRateEnabled

bool

Always false (deprecated)

isActive

bool

true if reserve is active, false otherwise

isFrozen

bool

true if reserve is frozen, false otherwise

#### getReserveCaps

[](#view-methods-getreservecaps)

```
function getReserveCaps(address asset) external view returns (uint256 borrowCap, uint256 supplyCap)
```

Returns the caps parameters of the reserve.

##### Input Parameters:

[](#view-methods-getreservecaps-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

#### Return Values:

[](#view-methods-return-values)

Name

Type

Description

borrowCap

uint256

The borrow cap of the reserve

supplyCap

uint256

The supply cap of the reserve

#### getPaused

[](#view-methods-getpaused)

```
function getPaused(address asset) external view returns (bool isPaused)
```

Returns true if the pool isPaused.

##### Input Parameters:

[](#view-methods-getpaused-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getpaused-return-values)

Name

Type

Description

isPaused

bool

true if the pool is paused, false otherwise

#### getSiloedBorrowing

[](#view-methods-getsiloedborrowing)

```
function getSiloedBorrowing(address asset) external view override returns (bool)
```

Returns the siloed borrowing flag. It returns true if the asset is [siloed for borrowing](/docs/whats-new/siloed-borrowing.md).

##### Input Parameters:

[](#view-methods-getsiloedborrowing-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getsiloedborrowing-return-values)

Type

Description

bool

true if the asset is siloed for borrowing

#### getLiquidationProtocolFee

[](#view-methods-getliquidationprotocolfee)

```
function getLiquidationProtocolFee(address asset) external view override returns (uint256)
```

Returns the protocol fee on the liquidation bonus.

##### Input Parameters:

[](#view-methods-getliquidationprotocolfee-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getliquidationprotocolfee-return-values)

Type

Description

uint256

The protocol fee on liquidation

#### getUnbackedMintCap

[](#view-methods-getunbackedmintcap)

```
function getUnbackedMintCap(address asset) external view override returns (uint256)
```

Returns the unbacked mint cap of the reserve.

##### Input Parameters:

[](#view-methods-getunbackedmintcap-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getunbackedmintcap-return-values)

Type

Description

uint256

The unbacked mint cap of the reserve

#### getDebtCeiling

[](#view-methods-getdebtceiling)

```
function getDebtCeiling(address asset) external view override returns (uint256)
```

Returns the debt ceiling of the reserve.

##### Input Parameters:

[](#view-methods-getdebtceiling-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getdebtceiling-return-values)

Type

Description

uint256

The debt ceiling of the reserve

#### getReserveData

[](#view-methods-getreservedata)

```
function getReserveData(address asset) external view override returns (    uint256 unbacked,    uint256 accruedToTreasuryScaled,    uint256 totalAToken,    uint256 totalStableDebt,    uint256 totalVariableDebt,    uint256 liquidityRate,    uint256 variableBorrowRate,    uint256 stableBorrowRate,    uint256 averageStableBorrowRate,    uint256 liquidityIndex,    uint256 variableBorrowIndex,    uint40 lastUpdateTimestamp)
```

Returns the reserve data.

##### Input Parameters:

[](#view-methods-getreservedata-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreservedata-return-values)

Name

Type

Description

unbacked

uint256

The amount of unbacked aTokens of the reserve

accruedToTreasuryScaled

uint256

The scaled amount of tokens accrued to treasury that is to be minted

totalAToken

uint256

The total supply of the aToken

totalStableDebt

uint256

The total stable debt of the reserve (deprecated)

totalVariableDebt

uint256

The total variable debt of the reserve

liquidityRate

uint256

The liquidity rate of the reserve

variableBorrowRate

uint256

The variable borrow rate of the reserve

stableBorrowRate

uint256

The stable borrow rate of the reserve (deprecated)

averageStableBorrowRate

uint256

The average stable borrow rate of the reserve (deprecated)

liquidityIndex

uint256

The liquidity index of the reserve

variableBorrowIndex

uint256

The variable borrow index of the reserve

lastUpdateTimestamp

uint40

The timestamp of the last update of the reserve

#### getATokenTotalSupply

[](#view-methods-getatokentotalsupply)

```
function getATokenTotalSupply(address asset) external view override returns (uint256)
```

Returns the total supply of aTokens for a given asset.

##### Input Parameters:

[](#view-methods-getatokentotalsupply-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getatokentotalsupply-return-values)

Type

Description

uint256

The total supply of the aToken

#### getTotalDebt

[](#view-methods-gettotaldebt)

```
function getTotalDebt(address asset) external view override returns (uint256)
```

Returns the total debt for a given asset.

##### Input Parameters:

[](#view-methods-gettotaldebt-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-gettotaldebt-return-values)

Type

Description

uint256

The total borrows for an asset

#### getUserReserveData

[](#view-methods-getuserreservedata)

```
function getUserReserveData(address asset, address user) external view returns (    uint256 currentATokenBalance,    uint256 currentStableDebt,    uint256 currentVariableDebt,    uint256 principalStableDebt,    uint256 scaledVariableDebt,    uint256 stableBorrowRate,    uint256 liquidityRate,    uint40 stableRateLastUpdated,    bool usageAsCollateralEnabled)
```

Returns the following user reserve data.

##### Input Parameters:

[](#view-methods-getuserreservedata-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

user

address

The address of the user

##### Return Values:

[](#view-methods-getuserreservedata-return-values)

Name

Type

Description

currentATokenBalance

uint256

The current AToken balance of the user

currentStableDebt

uint256

The current stable debt of the user (deprecated)

currentVariableDebt

uint256

The current variable debt of the user

principalStableDebt

uint256

The principal stable debt of the user (deprecated)

scaledVariableDebt

uint256

The scaled variable debt of the user

stableBorrowRate

uint256

The stable borrow rate of the user (deprecated)

liquidityRate

uint256

The liquidity rate of the reserve

stableRateLastUpdated

uint40

The timestamp of the last update of the user stable rate (deprecated)

usageAsCollateralEnabled

bool

true if the user is using the asset as collateral, else false

#### getReserveTokensAddresses

[](#view-methods-getreservetokensaddresses)

```
function getReserveTokensAddresses(address asset) external view override returns (    address aTokenAddress,    address stableDebtTokenAddress,    address variableDebtTokenAddress)
```

Returns the addresses of the aToken, stableDebtToken and variableDebtToken of the reserve.

##### Input Parameters:

[](#view-methods-getreservetokensaddresses-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreservetokensaddresses-return-values)

Name

Type

Description

aTokenAddress

address

The AToken address of the reserve

stableDebtTokenAddress

address

The StableDebtToken address of the reserve (deprecated)

variableDebtTokenAddress

address

The VariableDebtToken address of the reserve

#### getInterestRateStrategyAddress

[](#view-methods-getinterestratestrategyaddress)

```
function getInterestRateStrategyAddress(address asset) external view override returns (address irStrategyAddress)
```

Returns the address of the Interest Rate strategy.

##### Input Parameters:

[](#view-methods-getinterestratestrategyaddress-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getinterestratestrategyaddress-return-values)

Name

Type

Description

irStrategyAddress

address

The address of the Interest Rate strategy

#### getReserveDeficit

[](#view-methods-getreservedeficit)

```
function getReserveDeficit(address asset) external view override returns (uint256)
```

##### Input Parameters:

[](#view-methods-getreservedeficit-input-parameters)

Name

Type

Description

asset

address

The address of the underlying asset of the reserve

##### Return Values:

[](#view-methods-getreservedeficit-return-values)

Type

Description

uint256

Current reserve deficit from undercollateralized borrow positions

### Pure Methods

[](#pure-methods)

##### getDebtCeilingDecimals

[](#view-methods-getreservedeficit-getdebtceilingdecimals)

```
function getDebtCeilingDecimals() external pure override returns (uint256)
```

Returns the debt ceiling decimals.

##### Return Values:

[](#view-methods-getreservedeficit-return-values)

Type

Description

uint256

The debt ceiling decimals

### LiquidationDataProvider

[](#liquidationdataprovider)

This contract is a utility for fetching and pre-processing liquidation-related parameters for a given user. It aggregates data from the underlying Pool and Price Oracle to determine a user’s position, collateral, borrow details, and liquidation limits according to the protocol parameters.

The source code is available on [GitHub](https://github.com/bgd-labs/aave-v3-origin/blob/1f4df52c1be2633b720b3638a299d74b3d5dcbb7/src/contracts/helpers/LiquidationDataProvider.sol).

### View Methods

[](#view-methods)

#### getUserPositionFullInfo

[](#view-methods-getuserpositionfullinfo)

```
getUserPositionFullInfo(address user) public view override returns (UserPositionFullInfo memory)
```

Returns aggregated position information for a user including total collateral, total debt, available borrows, current liquidation threshold, loan-to-value (LTV), and health factor. All values are denominated in the base currency.

##### Input Parameters:

[](#view-methods-getuserpositionfullinfo-input-parameters)

Name

Type

Description

user

address

The address of the user whose position is queried

##### Return Values:

[](#view-methods-getuserpositionfullinfo-return-values)

Name

Type

Description

UserPositionFullInfo

struct

The aggregated position information of the user

The UserPositionFullInfo struct is composed of the following fields:

Name

Type

Description

totalCollateralInBaseCurrency

uint256

Total collateral in base currency

totalDebtInBaseCurrency

uint256

Total debt in base currency

availableBorrowsInBaseCurrency

uint256

Available borrows in base currency

currentLiquidationThreshold

uint256

Current liquidation threshold

ltv

uint256

Loan-to-value ratio

healthFactor

uint256

Health factor of the user’s position

#### getCollateralFullInfo

[](#view-methods-getcollateralfullinfo)

```
getCollateralFullInfo(address user, address collateralAsset) external view override returns (CollateralFullInfo memory)
```

Returns detailed information regarding a user’s collateral for a given asset. The returned struct includes the asset’s unit (based on decimals), its current price (via the Price Oracle), the associated aToken address, the raw collateral balance, and its equivalent value in the base currency.

##### Input Parameters:

[](#view-methods-getcollateralfullinfo-input-parameters)

Name

Type

Description

user

address

The address of the user

collateralAsset

address

The address of the collateral asset to fetch information for

##### Return Values:

[](#view-methods-getcollateralfullinfo-return-values)

Name

Type

Description

CollateralFullInfo

struct

Detailed collateral information for the specified asset

The CollateralFullInfo struct is composed of the following fields:

Name

Type

Description

assetUnit

uint256

The unit value of the asset (10^decimals)

price

uint256

Current price of the asset from the Price Oracle

aToken

address

Address of the aToken associated with the asset

collateralBalance

uint256

The raw collateral balance of the user

collateralBalanceInBaseCurrency

uint256

Collateral balance denominated in the base currency

#### getDebtFullInfo

[](#view-methods-getdebtfullinfo)

```
getDebtFullInfo(address user, address debtAsset) external view override returns (DebtFullInfo memory)
```

Returns detailed information regarding a user’s debt for a given asset. The returned struct includes the asset’s unit, current price, the associated variable debt token address, the debt balance, and its equivalent value in the base currency.

##### Input Parameters:

[](#view-methods-getdebtfullinfo-input-parameters)

Name

Type

Description

user

address

The address of the user

debtAsset

address

The address of the debt asset to fetch information for

##### Return Values:

[](#view-methods-getdebtfullinfo-return-values)

Name

Type

Description

DebtFullInfo

struct

Detailed debt information for the specified asset

The DebtFullInfo struct is composed of the following fields:

Name

Type

Description

assetUnit

uint256

The unit value of the asset (10^decimals)

price

uint256

Current price of the asset from the Price Oracle

variableDebtToken

address

Address of the variable debt token associated with the asset

debtBalance

uint256

The raw debt balance of the user

debtBalanceInBaseCurrency

uint256

Debt balance denominated in the base currency

#### getLiquidationInfo (without custom debt amount)

[](#view-methods-getliquidationinfo-without-custom-debt-amount)

```
getLiquidationInfo(address user, address collateralAsset, address debtAsset) public view override returns (LiquidationInfo memory)
```

A convenience function that returns liquidation parameters for a user using the maximum possible debt liquidation amount. Internally, it calls the overloaded version with debtLiquidationAmount set to the maximum (type(uint256).max).

##### Input Parameters:

[](#view-methods-getliquidationinfo-without-custom-debt-amount-input-parameters)

Name

Type

Description

user

address

The address of the user

collateralAsset

address

The address of the collateral asset

debtAsset

address

The address of the debt asset

##### Return Values:

[](#view-methods-getliquidationinfo-without-custom-debt-amount-return-values)

Name

Type

Description

LiquidationInfo

struct

Detailed liquidation information for the specified user and assets

The LiquidationInfo struct is composed of the following fields:

Name

Type

Description

userInfo

struct

Aggregated position details of the user (UserPositionFullInfo above)

collateralInfo

struct

Detailed collateral information (CollateralFullInfo above)

debtInfo

struct

Detailed debt information (DebtFullInfo above)

maxCollateralToLiquidate

uint256

Maximum collateral that can be liquidated

maxDebtToLiquidate

uint256

Maximum debt that can be liquidated

liquidationProtocolFee

uint256

Protocol fee applied on the liquidation bonus

amountToPassToLiquidationCall

uint256

Adjusted debt amount for the liquidation call

#### getLiquidationInfo (with custom debt liquidation amount)

[](#view-methods-getliquidationinfo-with-custom-debt-liquidation-amount)

```
getLiquidationInfo(address user, address collateralAsset, address debtAsset, uint256 debtLiquidationAmount) public view override returns (LiquidationInfo memory)
```

Returns comprehensive liquidation parameters for a user given a specific collateral asset and debt asset, considering a custom maximum debt liquidation amount. The function aggregates the user’s position, collateral and debt details, checks if liquidation conditions are met, and computes the optimal amounts for liquidation—including any applicable protocol fees.

##### Input Parameters:

[](#view-methods-getliquidationinfo-with-custom-debt-liquidation-amount-input-parameters)

Name

Type

Description

user

address

The address of the user

collateralAsset

address

The address of the collateral asset to be liquidated

debtAsset

address

The address of the debt asset to be repaid

debtLiquidationAmount

uint256

The maximum debt amount that can be liquidated (if lower than the user’s debt balance)

##### Return Values:

[](#view-methods-getliquidationinfo-with-custom-debt-liquidation-amount-return-values)

Name

Type

Description

LiquidationInfo

struct

Detailed liquidation information for the specified user and assets

The LiquidationInfo struct is composed of the following fields:

Name

Type

Description

userInfo

struct

Aggregated position details of the user (UserPositionFullInfo above)

collateralInfo

struct

Detailed collateral information (CollateralFullInfo above)

debtInfo

struct

Detailed debt information (DebtFullInfo above)

maxCollateralToLiquidate

uint256

Maximum collateral that can be liquidated

maxDebtToLiquidate

uint256

Maximum debt that can be liquidated

liquidationProtocolFee

uint256

Protocol fee applied on the liquidation bonus

amountToPassToLiquidationCall

uint256

Adjusted debt amount for the liquidation call

[

Previous

**Wrapped Token Gateway**

](/docs/developers/smart-contracts/wrapped-token-gateway)[

Next

**Incentives**

](/docs/developers/smart-contracts/incentives)

---

<a id="doc_34"></a>

## 📁 developers/smart_contracts / Wrapped Token Gateway | Aave Protocol Documentation

*파일 경로: developers/smart_contracts/wrapped_token_gateway.md*

Source: https://aave.com/docs/developers/smart-contracts/wrapped-token-gateway

## Wrapped Token Gateway

[](#wrapped-token-gateway)

The Aave Protocol operates exclusively with ERC-20 [reserve](/docs/primitives/reserve) tokens. To accommodate network gas tokens, the WrappedTokenGateway (previously called WETHGateway) is a helper contract that enables gas tokens (ETH, POL, etc.) to be wrapped or unwrapped to perform Aave Pool methods:

*   Supply
    
*   Borrow
    
*   Repay
    
*   Withdraw
    

The smart contract source code is available on [GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/helpers/WrappedTokenGatewayV3.sol).

### Write Methods

[](#write-methods)

#### depositETH

[](#write-methods-depositeth)

```
function depositETH(    address,    address onBehalfOf,    uint16 referralCode) external payable override
```

Wraps and supplies gas tokens to the Aave Protocol. A corresponding amount of the wrapped aTokens are minted to the onBehalfOf address.

The amount of network gas tokens to be supplied is specified in the msg.value field of the transaction.

##### Input Parameters:

[](#write-methods-depositeth-input-parameters)

Name

Type

Description

onBehalfOf

address

The address of the user who will receive the aTokens representing the supplied tokens

referralCode

uint16

Inactive, can pass 0 as placeholder

#### withdrawETH

[](#write-methods-withdraweth)

```
function withdrawETH(    address,    uint256 amount,    address to) external override
```

Withdraws amount of the supplied wrapped gas token, unwraps it and transfers to the to address. If the amount is uint(-1), the entire balance is withdrawn.

The WrappedTokenGateway contract must have an approved token allowance to spend aWETH on behalf of the user, example: IERC20(aWETHAddress).approve(wrappedTokenGatewayAddress, amount)

##### Input Parameters:

[](#write-methods-withdraweth-input-parameters)

Name

Type

Description

amount

uint256

amount of aWETH to withdraw and receive native ETH

to

address

The address of the user who will receive native ETH

#### repayETH

[](#write-methods-repayeth)

```
function repayETH(    address,    uint256 amount,    uint256 rateMode,    address onBehalfOf) external payable override
```

Repays a borrow position of onBehalfOf's address for the specified amount (or for the whole amount, if amount of uint256(-1) is passed).

The amount of network gas token to be repaid must also be specified in the msg.value field of the transaction.

##### Input Parameters:

[](#write-methods-repayeth-input-parameters)

Name

Type

Description

amount

uint256

The amount to repay, or uint256(-1) if the user wants to repay everything

rateMode

uint256

Should always be passed a value of 2 (variable rate mode)

onBehalfOf

address

The address for which msg.sender is repaying

#### borrowETH

[](#write-methods-borroweth)

```
function borrowETH(    address,    uint256 amount,    uint256 interestRateMode,    uint16 referralCode) external override
```

Borrows amount of unwrapped network gas tokens to msg.sender.

The WrappedTokenGateway contract must have an approved [credit delegation](/docs/developers/credit-delegation) to borrow WETH (or corresponding wrapped gas token of the network) on behalf of the the caller, example: IVariableDebtToken(wethAddress).approveDelegation(wrappedTokenGatewayAddress, amount)

##### Input Parameters:

[](#write-methods-borroweth-input-parameters)

Name

Type

Description

amount

uint256

The amount of ETH to borrow

interestRateMode

uint256

Should always be passed a value of 2 (variable rate mode)

referralCode

uint16

Integrators are assigned a referral code and can potentially receive rewards

#### withdrawETHWithPermit

[](#write-methods-withdrawethwithpermit)

```
function withdrawETHWithPermit(    address,    uint256 amount,    address to,    uint256 deadline,    uint8 permitV,    bytes32 permitR,    bytes32 permitS) external override
```

Withdraws amount of the supplied wrapped gas token, unwraps it and transfers to the to address. If the amount is uint(-1), the entire balance is withdrawn.

##### Input Parameters:

[](#write-methods-withdrawethwithpermit-input-parameters)

Name

Type

Description

amount

uint256

The amount of aWETH to withdraw and receive native ETH

to

address

The address of the user who will receive native ETH

deadline

uint256

Timestamp of signature expiration

permitV

uint8

V parameter of ERC712 permit sig

permitR

bytes32

R parameter of ERC712 permit sig

permitS

bytes32

S parameter of ERC712 permit sig

### View Methods

[](#view-methods)

#### getWETHAddress

[](#view-methods-getwethaddress)

```
function getWETHAddress() external view returns (address)
```

Get WETH address used by WrappedTokenGatewayV3.

##### Return Values:

[](#view-methods-getwethaddress-return-values)

Type

Description

address

The WETH address used by WrappedTokenGatewayV3

[

Previous

**L2 Pool**

](/docs/developers/smart-contracts/l2-pool)[

Next

**View Contracts**

](/docs/developers/smart-contracts/view-contracts)

---

<a id="doc_35"></a>

## 📁 primitives / AAVE Token | Aave Protocol Documentation

*파일 경로: primitives/aave.md*

Source: https://aave.com/docs/primitives/aave

## AAVE

[](#aave)

The AAVE token is the native governance token of the Aave Protocol. It empowers holders to participate in decision-making through protocol governance. AAVE is an ERC-20 token deployed on the Ethereum blockchain and is widely accessible across various centralised and decentralised exchanges.

### Governance

[](#governance)

AAVE token holders have the ability to influence the future of the Aave Protocol through governance. Both AAVE and safety module staked AAVE (stkAAVE) holders can vote on proposals or delegate their voting power to others. By participating in governance votes, holders contribute to decisions on protocol deployments, parameter adjustments, features, and more.

### Liquidity Pools

[](#liquidity-pools)

AAVE tokens can be supplied to liquidity pools within the Aave Protocol, or external pools such as decentralised exchanges, allowing users to earn yield.

Holders can stake their tokens in the Aave safety module, enhancing the system's security by providing a backstop in case of insolvency and earning rewards in return. Staking AAVE can also grant reduced GHO borrowing rates, adding further incentives for participation. Additionally, AAVE tokens can be supplied to the Aave markets as collateral, allowing users to borrow other assets and increase their capital efficiency.

### Cross-Chain

[](#cross-chain)

Furthermore, AAVE has cross-chain implementation on several networks using canonical network messaging bridges. This enables users to access AAVE across different blockchain networks, with the acknowledgment that the ability to bridge tokens to and from Ethereum depends on the availability of the network bridge.

Token Deployments:

*   [Ethereum Mainnet](https://etherscan.io/address/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9)
    
*   [Arbitrum](https://arbiscan.io/address/0xba5DdD1f9d7F570dc94a51479a000E3BCE967196)
    
*   [Base](https://basescan.org/address/0x63706e401c06ac8513145b7687a14804d17f814b)
    
*   [Optimism](https://optimistic.etherscan.io/address/0x76FB31fb4af56892A25e32cFC43De717950c9278)
    
*   [Polygon](https://polygonscan.com/address/0xD6DF932A45C0f255f85145f286eA0b292B21C90B)
    

[

Previous

**Safety Module**

](/docs/primitives/safety-module)[

Next

**GHO**

](/docs/primitives/gho)

---

<a id="doc_36"></a>

## 📁 primitives / GHO Token | Aave Protocol Documentation

*파일 경로: primitives/gho.md*

Source: https://aave.com/docs/primitives/gho

## GHO

[](#gho)

GHO (pronounced "go") is a decentralised, over-collateralised stablecoin that is fully backed, transparent, and native to the Aave Protocol. Designed to maintain a value pegged to the U.S. dollar, GHO is minted by users on demand, subject to mint cap limitations set by Aave's governance. Its stability is maintained through market efficiencies and over-collateralisation mechanisms inherent in the Aave Protocol.

### Facilitators

[](#facilitators)

Facilitators are contract addresses approved by Aave Governance with the ability to mint and burn GHO tokens. Each facilitator operates under a specific bucket cap, controlling the maximum amount of GHO they can generate. Facilitators play a crucial role in maintaining GHO's stability and integrating it across various platforms and use cases.

#### Aave Ethereum V3 Market

[](#facilitators-aave-ethereum-v3-market)

The Aave V3 Ethereum Market serves as a primary facilitator for GHO. Users can mint GHO by supplying approved collateral assets into the Aave Protocol and borrowing GHO against them. This process follows standard over-collateralisation practices, ensuring the protocol's security and the stablecoin's reliability. GHO has a discount mechanism that enables holder of stkAAVE (see [safety module](/docs/primitives/safety-module)) to borrow GHO at a discounted rate from the Aave V3 Ethereum Market.

#### Flash Mint

[](#facilitators-flash-mint)

The FlashMinter facilitator allows users to access uncollateralised GHO through flash loans, provided the borrowed amount is returned within the same transaction. This feature enables arbitrage opportunities and enhances liquidity without permanently increasing the overall supply of GHO.

#### GHO Stability Module (GSM)

[](#facilitators-gho-stability-module-gsm)

The GHO Stability Module acts as a facilitator to help maintain GHO's peg to the U.S. dollar. It allows users to swap GHO for other stable assets, providing a mechanism to absorb market imbalances and keep GHO's price stable.

#### Cross-Chain

[](#facilitators-cross-chain)

Cross-chain liquidity pools enable GHO to be used across different blockchain networks. Utilising CCIP, GHO can be bridged to other chains, allowing users to access liquidity pools on platforms outside of Ethereum. This cross-chain functionality expands GHO's utility and integrates it with a broader range of DeFi applications.

Token Deployments:

*   [Ethereum Mainnet](https://etherscan.io/address/0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f)
    
*   [Arbitrum](https://arbiscan.io/address/0x7dfF72693f6A4149b17e7C6314655f6A9F7c8B33)
    
*   [Base](https://basescan.org/address/0x6Bb7a212910682DCFdbd5BCBb3e28FB4E8da10Ee)
    

### GHO Liquidity Committee

[](#gho-liquidity-committee)

The GHO Liquidity Committee (GLC) was created in October 2023 to focus solely on the liquidity of the GHO stablecoin. The committee was formed through a [governance proposal](https://governance-v2.aave.com/governance/proposal/343/) and consisted of a small team. After a successful initial 3-month period, it was [integrated](https://governance-v2.aave.com/governance/proposal/407/) into the Aave Liquidity Committee (ALC).

The ALC's main responsibilities regarding GHO include:

*   Providing analytics and modelling of the liquidity strategy
    
*   Liaising with teams that support the protocols hosting GHO liquidity
    
*   Leading and coordinating the committee's weekly activities
    
*   Providing critical feedback and helping refine the strategy
    
*   Verifying and signing transactions
    

The ALC's performance measures and liquidity targets for GHO can be found on the [GHO Analytics platform](https://aave.tokenlogic.xyz/liquidity-committee) provided by TokenLogic.

More information regarding the role of the GHO Liquidity Committee can be found in [Aave's Governance forum](https://governance.aave.com/t/temp-check-treasury-management-create-and-fund-gho-liquidity-committee/14800).

### GHO Stewards

[](#gho-stewards)

GHO Stewards is an additional entity created in April 2024 to more flexibly manage GHO market parameters, enabling GHO to be scaled per prevailing market conditions. The source code for GHO Steward contracts can be found on [GitHub](https://github.com/aave/gho-core/tree/main/src/contracts/misc).

The GHO Stewards determine if and how much to adjust the following, subject to pre-defined and Governance accepted thresholds:

*   GHO Borrow Cap
    
*   GHO Borrow Rate
    
*   GSM Exposure Cap
    
*   GSM Bucket Capacity
    
*   GSM Price Strategy
    
*   GSM Fee Strategy
    
*   GSM Price Range (Freeze, Unfreeze)
    

With many liquidity pools being created and rewards distributed across them, it is important that the DAO can swiftly increase the GHO Borrow Cap to mitigate GHO trading above $1. The GHO Stewards can swiftly increase the GHO Borrow Cap to mitigate GHO trading above the peg. The GHO Stewards can increase the GHO Borrow Cap to a threshold of 50M units to a total borrow cap of 100M.

The Borrow Rate must be adjusted gradually to enable the ecosystem to expand safely. If the trailing 30-day average price of GHO stays outside a $0.995 - $1.005 price range, the GHO Stewards are able to adjust the Borrow Rate no more than 500bps per 2-day period, up to a maximum 25% APR.

GHO Stewards consist of members from Growth (ACI), Risk (ChaosLabs), and Finance (TokenLogic + karpatkey) Service Providers and utilise a 3 of 4 multi-sig.

### Liquidity Pools

[](#liquidity-pools)

Liquidity pools are vital for providing market liquidity for GHO, enabling users to trade, borrow, and supply GHO across various platforms.

The Aave community, through the Liquidity Committee, may offer incentives to liquidity providers who supply GHO to specific pools. These incentives can include reward tokens or reduced fees, encouraging users to add liquidity and improve market depth. Incentivized liquidity pools help keep GHO readily available and maintain its peg to the U.S. dollar.

[

Previous

**AAVE**

](/docs/primitives/aave)[

Next

**Aave V3**

](/docs/developers/aave-v3)

---

<a id="doc_37"></a>

## 📁 primitives / Governance | Aave Protocol Documentation

*파일 경로: primitives/governance.md*

Source: https://aave.com/docs/primitives/governance

## Governance

[](#governance)

The Aave DAO is a decentralised collective of AAVE token holders and contributors who work together to shape the future of the protocol through a structured governance process. This community-driven model enables participants to propose, discuss, and vote on critical changes, guiding the evolution of the protocol and aligning with the collective goals of its members.

### Processes

[](#processes)

Aave's governance process is structured so that the protocol remains decentralised, secure, and adaptable. The lifecycle of a proposal is carefully designed to allow community members to present ideas, vote on them, and execute approved changes through a transparent and structured process.

#### Proposal Lifecycle

[](#processes-proposal-lifecycle)

1.  **Governance Forum** The proposal process begins with an idea introduced to the [Aave Governance Forum](https://governance.aave.com). This is where initial discussions take place and feedback is gathered. The community helps refine the proposal before moving to the next stage.
    
2.  **Temp Check (Snapshot Voting)** After discussion, the proposal proceeds to a TEMP CHECK via the [Aave Snapshot Space](https://snapshot.org/#/aave.eth). This informal vote gauges community sentiment. TEMP CHECK votes are non-binding but help determine if there is sufficient interest in moving forward. Proposals in this stage do not require detailed technical specifics.
    
3.  **ARFC (Aave Request for Final Comments)** If the TEMP CHECK passes, the proposal moves to the ARFC stage, where it undergoes more formal scrutiny. Service providers and community members contribute detailed feedback on how the proposal would impact the protocol, preparing it for the AIP stage. ARFC voting also occurs on the [Aave Snapshot Space](https://snapshot.org/#/aave.eth).
    
4.  **AIP (Aave Improvement Proposal)** The AIP stage is where the proposal becomes a formal, onchain submission. It includes two parts: metadata (stored on IPFS) and the contract payload. These are submitted through Aave's governance contracts, primarily on the Ethereum Mainnet.
    
5.  **Voting** Once submitted, the AIP enters a PENDING status before becoming ACTIVE for voting. Voting is conducted onchain through Aave governance contracts. A proposal succeeds if it meets quorum and vote differential requirements. If these thresholds aren’t met, the proposal fails.
    
6.  **Execution** A successful proposal moves to the execution phase, where it is enacted via Aave's governance infrastructure. Depending on the type of proposal, a timelock delay (either one day or 7 days) is imposed before the changes are implemented. Cross-chain proposals are executed using Aave's Delivery Infrastructure (a.DI).
    

#### Voting Overview

[](#processes-voting-overview)

IntroductionTemp CheckAave Request for Final Comments (ARFC)Aave Improvement Proposal (AIP)VotingExecutionGovernance ForumSnapshotOnchain

##### Off-chain Voting (Snapshot)

[](#processes-voting-overview-off-chain-voting-snapshot)

Off-chain votes are used to measure community sentiment during the early stages of proposal development (Temp Checks and ARFCs). These non-binding votes take place on Snapshot and last for three days, allowing token holders to participate without transaction fees.

##### Onchain Voting (Governance Interfaces)

[](#processes-voting-overview-onchain-voting-governance-interfaces)

Once a proposal reaches the AIP stage, onchain voting is required. Token holders, delegates, or delegators vote on proposals using their AAVE, stkAAVE, or aAAVE tokens. The process is secured through various governance interfaces, including [Aave Labs](https://app.aave.com), [BGD Labs](https://vote.onaave.com), and [Boardroom](https://boardroom.io/aave).

Since voting can occur on multiple networks, this can create limitations for smart contract wallets that only exist on one network. To accommodate this, governance interfaces can be used to setup **voting representatives**, which allows a separate voting address to be designated for each network.

#### Proposal Frameworks

[](#processes-proposal-frameworks)

Aave has predefined frameworks for common types of proposals, simplifying the governance process:

*   [Asset Onboarding Framework](https://governance.aave.com/t/arfc-update-the-asset-onboarding-framework/15629): Standardized lifecycle for onboarding new assets to the protocol, providing a structured process for risk assessments, and community discussions.
    
*   [New Chain Deployment Framework](https://governance.aave.com/t/arfc-new-chain-deployment-framework/15694): Guidelines for deploying Aave on new blockchains, covering security audits, liquidity considerations, and governance approval to support safe and effective multi-chain expansion.
    
*   [Emission Manager Framework](https://governance.aave.com/t/arfc-emission-manager-framework-update/16884): Simplified process for adding emission admins to reserves, improving the management of liquidity incentives.
    
*   [Caps Update Framework](https://governance.aave.com/t/arfc-aave-v3-caps-update-framework/11937): Direct-to-AIP process for adjusting caps or freezing reserves, allowing quicker governance actions to respond to market risks while maintaining protocol stability and liquidity constraints.
    
*   [Direct to AIP Framework](https://governance.aave.com/t/arfc-direct-to-aip-framework/13913): Similar to the Caps Update Framework, but broader in scope, allows certain governance actions to bypass TEMP CHECK & ARFC stages, requiring only an ARFC forum post before AIP creation.
    

These frameworks streamline governance and allow the community to focus on more complex issues while maintaining the protocol's security and adaptability.

### Community

[](#community)

#### Delegates

[](#community-delegates)

Delegates are entrusted with voting power by other community members or through self-delegation. They actively participate in governance by voting on proposals on behalf of those who have delegated their voting rights. Some delegates are compensated through the Orbit program for their contributions.

#### Delegators

[](#community-delegators)

Delegators are community members who hold AAVE, stkAAVE, or aAAVE tokens but choose to delegate their voting power to another individual or entity. This allows them to have their interests represented in governance without directly participating in every vote.

#### Contributors

[](#community-contributors)

Contributors dedicate time and resources to the Aave DAO by engaging in working groups, completing bounties, building on the protocol, or working through grants. These efforts help maintain and improve the Aave ecosystem.

#### Service Providers

[](#community-service-providers)

Service providers offer essential services to the protocol, such as risk management, financial oversight, security, and development. Examples of service providers include:

*   Chaos Labs (Risk)
    
*   Llamarisk (Risk)
    
*   Karpatkey (Finance)
    
*   Certora (Security)
    
*   Tokenlogic (Finance)
    
*   BGD Labs (Development)
    
*   ACI (Growth and Business Development)
    
*   Aave Labs (Development)
    

#### Guardians

[](#community-guardians)

The Aave Community Guardians are a group of community-elected signers authorized to execute limited emergency protections.

The Aave Guardians have responsibilities divided between two multi-signature wallets, with roles and signers listed below.

##### Protocol Emergency Guardian

[](#community-guardians-protocol-emergency-guardian)

The Protocol Emergency Guardian is the holder of the [EMERGENCY\_ADMIN](/docs/developers/smart-contracts/acl-manager#roles-emergency-admin) role for Aave protocol markets and failsafe emergency actor for cross-chain messaging in Emergency Mode.

The Protocol Emergency Guardian is a 5 of 9 multi-signature wallet consisting of the following community-elected signers:

*   Chaos Labs (risk service provider)
    
*   Llamarisk (risk service provider)
    
*   Karpatkey (finance service provider)
    
*   Certora (security service provider)
    
*   Tokenlogic (finance service provider)
    
*   BGD Labs (development service provider)
    
*   ACI (growth and business development service provider)
    
*   Ezr3al (Aave DAO delegate)
    
*   Stable Labs (Aave DAO delegate)
    

##### Governance Emergency Guardian

[](#community-guardians-governance-emergency-guardian)

The Governance Emergency Guardian is tasked to protect the Aave Protocol against potential governance takeovers by having the ability to “veto” an onchain payload if it is deemed malicious.

The Governance Emergency Guardian is a 5 of 9 multi-signature wallet consisting of the following community-elected signers:

*   Seb (Zapper)
    
*   Mounir (Paraswap)
    
*   Gavi Galloway (Standard Crypto)
    
*   Nenad (Defi Saver)
    
*   Fernando (Balancer)
    
*   Roger (Chainlink community)
    
*   Mariano Conti (DeFi OG)
    
*   Marin (Lido)
    
*   Certora (security service provider)
    

#### Stewards

[](#community-stewards)

Stewards have delegated responsibility over specific protocol parameters, allowing the DAO to quickly respond to market changes. Stewards manage areas such as the GHO stablecoin and liquidity parameters. This system streamlines governance by reducing the need for frequent votes on minor adjustments, promoting efficiency. The source code for GHO Steward contracts can be found on [GitHub](https://github.com/aave/gho-core/tree/main/src/contracts/misc).

#### GHO Bucket Steward

[](#community-gho-bucket-steward)

Parameter

Description

Facilitator Bucket Capacity

Up to 100% increase

##### GHO Aave Steward

[](#community-gho-bucket-steward-gho-aave-steward)

Parameter

Description

GHO Borrow Cap

Up to 100% increase or decrease

GHO Borrow Rate

Up to 5% change to optimalUsageRatio, baseVariableBorrowRate, variableRateSlope1, and variableRateSlope2 with maximum of 25%

GHO Supply Cap

Up to 100% increase

##### GHO CCIP Steward

[](#community-gho-bucket-steward-gho-ccip-steward)

Parameter

Description

Bridge Limit

Up to 100% increase or decrease

Rate Limit

Up to 100% increase or decrease

##### GHO Stablility Module Steward

[](#community-gho-bucket-steward-gho-stablility-module-steward)

Parameter

Description

GSM Exposure Cap

Up to 100% increase

GSM Buy/Sell Fees

Up to 0.5% increase or decrease

##### Risk Steward

[](#community-gho-bucket-steward-risk-steward)

Description

Value

Frequency of change

5 days

Maximum supply cap increase

50%

Maximum borrow cap increase

50%

[

Previous

**Oracle**

](/docs/primitives/oracle)[

Next

**Safety Module**

](/docs/primitives/safety-module)

---

<a id="doc_38"></a>

## 📁 primitives / Incentives | Aave Protocol Documentation

*파일 경로: primitives/incentives.md*

Source: https://aave.com/docs/primitives/incentives

## Incentives

[](#incentives)

User AccountsLiquidity PoolGovernance

Incentives within the Aave Protocol encourage active participation from suppliers and borrowers, enhancing liquidity and the overall efficiency of the protocol. It should be noted that there is no one source of various incentive initiatives, but they can originate from multiple sources, including the Aave DAO treasury and external entities interested in promoting liquidity for specific [reserves](/docs/primitives/reserve).

The Aave DAO, governed by AAVE token holders through proposals and voting, can allocate funds from the DAO treasury to incentivise certain activities within the protocol. Incentive programs funded by the DAO are proposed, discussed, and approved through the [Aave Governance](/docs/primitives/governance) process, ensuring community involvement and transparency.

### Liquidity Pool Incentives

[](#liquidity-pool-incentives)

Incentives can also be applied to the supply or borrow side of Aave liquidity pools, promoting activity of the incentivised [reserve](/docs/primitives/reserve). By offering rewards to suppliers and borrowers of certain assets on Aave, the visibility and adoption of tokens can be boosted. Such external incentives require governance approval.

Approved incentives are distributed continuously over time proportional to the amount of liquidity a user supplies or borrows. Users can claim these rewards via the protocol’s incentive controller, which manages the allocation and distribution of incentives. This system adds value for those actively participating in the protocol while aligning user interests with the health and stability of the Aave ecosystem.

### Safety Module

[](#safety-module)

AAVE holders can stake their tokens in the [Safety Module](/docs/primitives/safety-module), a reserve designed to secure the protocol against unexpected shortfalls. In return for staking their AAVE tokens and taking on the associated risk, participants earn rewards, typically in the form of additional AAVE tokens or other incentives approved by governance. These rewards not only compensate stakers but also enhance the protocol's security by ensuring sufficient reserves are available to cover potential deficits.

### Merit Program

[](#merit-program)

Merit is an Aave-alignment user reward system, designed as a merkle-tree-based periodic airdrop to incentivise Aave-aligned behaviours and enhance the competitiveness of the Aave protocol. More information and interface to access merit distribution can be found [here](https://apps.aavechan.com/merit).

[

Previous

**Reserve**

](/docs/primitives/reserve)[

Next

**Oracle**

](/docs/primitives/oracle)

---

<a id="doc_39"></a>

## 📁 primitives / Liquidity Pool | Aave Protocol Documentation

*파일 경로: primitives/liquidity_pool.md*

Source: https://aave.com/docs/primitives/liquidity-pool

## Liquidity Pool

[](#liquidity-pool)

SupplyBorrow%%%%%%%%%%%%%%%%

A **liquidity pool** is an Aave market instance that enables users to participate as suppliers or borrowers. Governance-approved parameters, such as reserve configurations and collateralization thresholds, define each pool. Suppliers provide liquidity into the pool that borrowers can access through overcollateralised positions. In return, suppliers earn interest, while borrowers can obtain liquidity against their collateral, all facilitated through decentralised smart contracts.

Aave liquidity pools operate on a blockchain network governed by decisions that define the chain and reserve parameters. Parameter decisions must balance liquidity demands for various actions with risk management. The use of smart contracts validate parameters, executing the actions of borrowing, repaying, and liquidation processes seamlessly without intermediaries. This decentralised approach enhances the transparency, efficiency, and security of financial interactions within the pool.

[

Previous

**Flash Loans**

](/docs/concepts/flash-loans)[

Next

**Reserve**

](/docs/primitives/reserve)

---

<a id="doc_40"></a>

## 📁 primitives / Oracle | Aave Protocol Documentation

*파일 경로: primitives/oracle.md*

Source: https://aave.com/docs/primitives/oracle

## Oracle

[](#oracle)

MarketsPriceSequencer uptimePrice Redemption Ratio

Each [reserve](/docs/primitives/reserve) within the Aave Protocol is associated with an oracle contract. These oracle contracts are responsible for reporting the market price of assets in the protocol, which is essential for determining collateralisation requirements.

The oracle for each reserve is selected through Aave Governance, establishing a decentralised model where the community decides which data sources are used. Once chosen, the oracle contract submits price feed updates based on its operational logic (time-based, deviation-based, etc.).

### Types of Oracles in Use

[](#types-of-oracles-in-use)

Currently, there are two primary types of oracle contracts utilised on production Aave markets:

1.  **Chainlink Price Feeds**: Chainlink oracles provide highly reliable, decentralised price data for various assets. These price feeds pull data from multiple sources and aggregate them, minimising the risk of manipulation or outages.
    
2.  **Correlated Assets Price Oracle (CAPO)**: CAPO is designed for assets that have a strong correlation with another asset's price. For example, wrapped tokens can use this oracle to mirror the price of their underlying assets. CAPO leverages specialised logic to adjust and submit prices that follow the movements of these correlated assets. See more details about its implementation on [GitHub](https://github.com/bgd-labs/aave-capo).
    

[

Previous

**Incentives**

](/docs/primitives/incentives)[

Next

**Governance**

](/docs/primitives/governance)

---

<a id="doc_41"></a>

## 📁 primitives / Reserve | Aave Protocol Documentation

*파일 경로: primitives/reserve.md*

Source: https://aave.com/docs/primitives/reserve

## Reserve

[](#reserve)

WETHBorrowing powerLiquidation thresholdInterest rate strategyCapsE-mode

A **reserve** is an instance of a token within an Aave [liquidity pool](/docs/primitives/liquidity-pool). Each reserve is governed by a set of parameters that manage risk and optimise liquidity. These parameters can vary across different markets, even for the same underlying token, allowing Aave to adapt to various network and pool conditions.

### Key Reserve Parameters

[](#key-reserve-parameters)

1.  **Loan-to-Value (LTV)**: The maximum amount that can be borrowed relative to the collateral’s value. For example, a 75% LTV allows borrowing 75% of the collateral’s value. An asset with an LTV of 0% cannot be enabled as collateral.
    
2.  **Liquidation Threshold**: Defines the point at which a position becomes at risk of liquidation. If the threshold is exceeded, the position could be liquidated to repay the borrower's debt.
    
3.  **Borrowing Enabled**: Determines whether liquidity of a reserve can be borrowed.
    
4.  **Caps**: Supply and Borrow caps limit the total amount of a token that can be supplied and borrowed from a reserve. These caps are crucial for maintaining liquidity and preventing overexposure during volatile market conditions​.
    
5.  **Interest Rate Model**: Interest rates in Aave adjust dynamically based on the utilisation of the liquidity pool. As more liquidity is borrowed, interest rates rise to reflect the reduced availability of assets, creating conditions that enough liquidity remains for withdrawals and liquidations. The rates are controlled by parameters that set the base rate and slopes for utilisation​.
    

### Dynamic Parameters and Governance

[](#dynamic-parameters-and-governance)

The parameters for each reserve are not fixed; they vary between markets and can change over time as Aave Governance monitors market conditions and adjusts settings accordingly. For example, the same underlying token, such as ETH, might have different LTVs or interest rates in Ethereum versus Polygon markets. These adjustments are made to optimise liquidity and risk management for each market. Governance proposals allow the community to vote on changes, such as raising borrow caps or adjusting LTVs, enabling reserves to remain aligned with current market dynamics.

[

Previous

**Liquidity Pool**

](/docs/primitives/liquidity-pool)[

Next

**Incentives**

](/docs/primitives/incentives)

---

<a id="doc_42"></a>

## 📁 primitives / Safety Module | Aave Protocol Documentation

*파일 경로: primitives/safety_module.md*

Source: https://aave.com/docs/primitives/safety-module

## Safety Module

[](#safety-module)

The [Umbrella](https://governance.aave.com/t/bgd-aave-safety-module-umbrella/18366) governance proposal outlines potential changes to the Safety Module, including automated slashing, replacing stkAAVE and stkABPT with aToken staking, and new incentives design, subject to community approval.

User AccountsSafety ModuleLiquidity PoolGovernance

Staking in the Aave Safety Module allows AAVE, GHO, and ABPT holders on the Ethereum network to contribute to the protocol's security while earning Safety Incentives. By staking, participants add an additional layer of protection, with the acknowledgement that their assets may be slashed in the event of a shortfall to cover any protocol deficits. Underlying tokens that can be supplied to safety module are listed below:

*   [AAVE](https://etherscan.io/address/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9)
    
*   [ABPT](https://etherscan.io/address/0x3de27efa2f1aa663ae5d458857e731c129069f29) ([Underlying Balancer Token Pool](https://app.balancer.fi/#/ethereum/pool/0x3de27efa2f1aa663ae5d458857e731c129069f29000200000000000000000588))
    
*   [GHO](https://etherscan.io/address/0x40d16fc0246ad3160ccc09b8d0d3a2cd28ae6c2f)
    

### Safety Incentives

[](#safety-incentives)

Safety Incentives are rewards distributed to participants who stake their assets in the Aave Safety Module. These incentives serve as compensation for the risk taken by stakers, whose assets may be slashed to cover protocol deficits in the event of a shortfall. Safety Incentives are primarily distributed in the form of AAVE tokens, and the amount allocated to stakers is determined by Aave Governance through votes on emission parameters.

The emission parameters, which dictate the rate of Safety Incentives, are voted on by the Aave DAO. These parameters are allocated from the Ecosystem Reserve (AAVE Tokens) and/or the Protocol Treasury. Governance votes allow AAVE token holders to influence how much of the reserve or treasury is allocated to these incentives and how they are distributed over time. This decentralised decision-making process aligns incentives with the overall health and security of the Aave ecosystem.

Safety Incentives accumulate over time and can be claimed at any point while tokens are staked or after un-staking from the safety module.

### Slashing Risks

[](#slashing-risks)

When staking in the Aave Safety Module, it’s important to be aware of the potential slashing risks. Slashing refers to the reduction of staked assets in the event of a shortfall event within the Aave Protocol. This mechanism is in place to protect the protocol by using a portion of staked assets to cover any deficits that may arise. While staking offers rewards through Safety Incentives, there is a risk that a portion of the staked assets could be slashed to contribute to the stability of the Aave ecosystem.

The extent of slashing varies depending on the type of token staked:

*   **stkAAVE and stkABPT**: Maximum slashing risk is up to 30% of the staked assets.
    
*   **stkGHO**: Maximum slashing risk is up to 99% of the staked assets.
    

These risks are an essential consideration for anyone looking to participate in the Aave Safety Module, as they reflect the potential loss of assets in exchange for helping to secure the protocol. The process of identifying and executing a slashing event is subject to an onchain Aave Governance proposal.

[

Previous

**Governance**

](/docs/primitives/governance)[

Next

**AAVE**

](/docs/primitives/aave)

---

<a id="doc_43"></a>

## 📁 resources / Access Controls Dashboard | Aave Protocol Documentation

*파일 경로: resources/access_controls.md*

Source: https://aave.com/docs/resources/access-controls

## Aave Protocol Access Controls

[](#aave-protocol-access-controls)

See the [Aave Permissions Book](https://github.com/bgd-labs/aave-permissions-book/tree/main/out) for more in-depth breakdown of functions and roles.

Ethereum V3 Core Market

MainnetTestnet

V3V2

Name

Address

ABI

Upgradable By

[Pool](../developers/smart-contracts/pool)

[0x8787...A4E2](https://etherscan.io/address/0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2)

[ABI](../developers/smart-contracts/pool)

Governance

[WrappedTokenGateway](../developers/smart-contracts/wrapped-token-gateway)

[0xd016...5722](https://etherscan.io/address/0xd01607c3C5eCABa394D8be377a08590149325722)

[ABI](../developers/smart-contracts/wrapped-token-gateway)

Not upgradeable

[PoolAddressesProvider](../developers/smart-contracts/pool-addresses-provider)

[0x2f39...4E9e](https://etherscan.io/address/0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e)

[ABI](../developers/smart-contracts/pool-addresses-provider)

Not upgradeable

[PoolConfigurator](../developers/smart-contracts/pool-configurator)

[0x64b7...bB27](https://etherscan.io/address/0x64b761D848206f447Fe2dd461b0c635Ec39EbB27)

[ABI](../developers/smart-contracts/pool-configurator)

Governance

[UiPoolDataProvider](../developers/smart-contracts/view-contracts)

[0x3F78...d8FC](https://etherscan.io/address/0x3F78BBD206e4D3c504Eb854232EdA7e47E9Fd8FC)

[ABI](../developers/smart-contracts/view-contracts)

Not upgradeable

[UiIncentiveDataProvider](../developers/smart-contracts/view-contracts)

[0xe3dF...F047](https://etherscan.io/address/0xe3dFf4052F0bF6134ACb73bEaE8fe2317d71F047)

[ABI](../developers/smart-contracts/view-contracts)

Not upgradeable

[UiGHODataProvider](../developers/gho)

[0x379c...1aE8](https://etherscan.io/address/0x379c1EDD1A41218bdbFf960a9d5AD2818Bf61aE8)

[ABI](../developers/gho)

Not upgradeable

[ACLManager](../developers/smart-contracts/acl-manager)

[0xc2aa...85b0](https://etherscan.io/address/0xc2aaCf6553D20d1e9d78E365AAba8032af9c85b0)

[ABI](../developers/smart-contracts/acl-manager)

Not upgradeable

[WalletBalanceProvider](../developers/smart-contracts/view-contracts)

[0xC7be...A8E2](https://etherscan.io/address/0xC7be5307ba715ce89b152f3Df0658295b3dbA8E2)

[ABI](../developers/smart-contracts/view-contracts)

Governance

[TreasuryCollector](../primitives/governance)

[0x464C...e18c](https://etherscan.io/address/0x464C71f6c2F760DdA6093dCB91C24c39e5d6e18c)

[ABI](../primitives/governance)

Governance

[AaveProtocolDataProvider](../developers/smart-contracts/view-contracts)

[0x497a...C8a6](https://etherscan.io/address/0x497a1994c46d4f6C864904A9f1fac6328Cb7C8a6)

[ABI](../developers/smart-contracts/view-contracts)

Governance

[RiskSteward](../primitives/governance)

[0x7C71...59c7](https://etherscan.io/address/0x7C7143f4bE189928A6a98D8686c5e84c893c59c7)

[ABI](../primitives/governance)

Not upgradeable

[DefaultIncentivesController](../developers/smart-contracts/incentives)

[0x8164...bFcb](https://etherscan.io/address/0x8164Cc65827dcFe994AB23944CBC90e0aa80bFcb)

[ABI](../developers/smart-contracts/incentives)

Governance

[IncentivesEmissionManager](../developers/smart-contracts/incentives)

[0x223d...d974](https://etherscan.io/address/0x223d844fc4B006D67c0cDbd39371A9F73f69d974)

[ABI](../developers/smart-contracts/incentives)

Not upgradeable

[PoolAddressesProviderRegistry](../developers/smart-contracts/pool-addresses-provider)

[0xbaA9...5170](https://etherscan.io/address/0xbaA999AC55EAce41CcAE355c77809e68Bb345170)

[ABI](../developers/smart-contracts/pool-addresses-provider)

Not upgradeable

[AaveOracle](../developers/smart-contracts/aave-oracle)

[0x5458...a0C2](https://etherscan.io/address/0x54586bE62E3c3580375aE3723C145253060Ca0C2)

[ABI](../developers/smart-contracts/aave-oracle)

Not upgradeable

[RepayWithCollateral](../developers/smart-contracts/switch-adapters)

[0x35bb...0e3E](https://etherscan.io/address/0x35bb522b102326ea3F1141661dF4626C87000e3E)

[ABI](../developers/smart-contracts/switch-adapters)

Not upgradeable

[CollateralSwitch](../developers/smart-contracts/switch-adapters)

[0xADC0...364e](https://etherscan.io/address/0xADC0A53095A0af87F3aa29FE0715B5c28016364e)

[ABI](../developers/smart-contracts/switch-adapters)

Not upgradeable

[DebtSwitch](../developers/smart-contracts/switch-adapters)

[0xd785...b442](https://etherscan.io/address/0xd7852E139a7097E119623de0751AE53a61efb442)

[ABI](../developers/smart-contracts/switch-adapters)

Not upgradeable

[WithdrawSwitchAdapter](../developers/smart-contracts/switch-adapters)

[0x78F8...20e0](https://etherscan.io/address/0x78F8Bd884C3D738B74B420540659c82f392820e0)

[ABI](../developers/smart-contracts/switch-adapters)

Not upgradeable

[ACLAdmin](../primitives/governance)

[0x5300...192A](https://etherscan.io/address/0x5300A1a15135EA4dc7aD5a167152C01EFc9b192A)

[ABI](../primitives/governance)

Not upgradeable

[CapsPlusRiskSteward](../primitives/governance)

[0x82dc...7778](https://etherscan.io/address/0x82dcCF206Ae2Ab46E2099e663F70DeE77caE7778)

[ABI](../primitives/governance)

Not upgradeable

[

Previous

**Parameters**

](/docs/resources/parameters)[

Next

**Code Licensing**

](/docs/resources/code-licensing)

---

<a id="doc_44"></a>

## 📁 resources / Addresses Dashboard | Aave Protocol Documentation

*파일 경로: resources/addresses.md*

Source: https://aave.com/docs/resources/addresses

## Aave Protocol Deployed Contracts

[](#aave-protocol-deployed-contracts)

Integrate contract addresses as Solidity or JavaScript package with the [Aave Address Book](https://github.com/bgd-labs/aave-address-book).

Ethereum V3 Core Market

ContractsReserves

MainnetTestnet

V3V2

Name

Address

ABI

[Pool](../developers/smart-contracts/pool)

[0x8787...A4E2](https://etherscan.io/address/0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2)

[ABI](../developers/smart-contracts/pool)

[WrappedTokenGateway](../developers/smart-contracts/wrapped-token-gateway)

[0xd016...5722](https://etherscan.io/address/0xd01607c3C5eCABa394D8be377a08590149325722)

[ABI](../developers/smart-contracts/wrapped-token-gateway)

[PoolAddressesProvider](../developers/smart-contracts/pool-addresses-provider)

[0x2f39...4E9e](https://etherscan.io/address/0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e)

[ABI](../developers/smart-contracts/pool-addresses-provider)

[PoolConfigurator](../developers/smart-contracts/pool-configurator)

[0x64b7...bB27](https://etherscan.io/address/0x64b761D848206f447Fe2dd461b0c635Ec39EbB27)

[ABI](../developers/smart-contracts/pool-configurator)

[UiPoolDataProvider](../developers/smart-contracts/view-contracts)

[0x3F78...d8FC](https://etherscan.io/address/0x3F78BBD206e4D3c504Eb854232EdA7e47E9Fd8FC)

[ABI](../developers/smart-contracts/view-contracts)

[UiIncentiveDataProvider](../developers/smart-contracts/view-contracts)

[0xe3dF...F047](https://etherscan.io/address/0xe3dFf4052F0bF6134ACb73bEaE8fe2317d71F047)

[ABI](../developers/smart-contracts/view-contracts)

[UiGHODataProvider](../developers/gho)

[0x379c...1aE8](https://etherscan.io/address/0x379c1EDD1A41218bdbFf960a9d5AD2818Bf61aE8)

[ABI](../developers/gho)

[ACLManager](../developers/smart-contracts/acl-manager)

[0xc2aa...85b0](https://etherscan.io/address/0xc2aaCf6553D20d1e9d78E365AAba8032af9c85b0)

[ABI](../developers/smart-contracts/acl-manager)

[WalletBalanceProvider](../developers/smart-contracts/view-contracts)

[0xC7be...A8E2](https://etherscan.io/address/0xC7be5307ba715ce89b152f3Df0658295b3dbA8E2)

[ABI](../developers/smart-contracts/view-contracts)

[TreasuryCollector](../primitives/governance)

[0x464C...e18c](https://etherscan.io/address/0x464C71f6c2F760DdA6093dCB91C24c39e5d6e18c)

[ABI](../primitives/governance)

[AaveProtocolDataProvider](../developers/smart-contracts/view-contracts)

[0x497a...C8a6](https://etherscan.io/address/0x497a1994c46d4f6C864904A9f1fac6328Cb7C8a6)

[ABI](../developers/smart-contracts/view-contracts)

[RiskSteward](../primitives/governance)

[0x7C71...59c7](https://etherscan.io/address/0x7C7143f4bE189928A6a98D8686c5e84c893c59c7)

[ABI](../primitives/governance)

[DefaultIncentivesController](../developers/smart-contracts/incentives)

[0x8164...bFcb](https://etherscan.io/address/0x8164Cc65827dcFe994AB23944CBC90e0aa80bFcb)

[ABI](../developers/smart-contracts/incentives)

[IncentivesEmissionManager](../developers/smart-contracts/incentives)

[0x223d...d974](https://etherscan.io/address/0x223d844fc4B006D67c0cDbd39371A9F73f69d974)

[ABI](../developers/smart-contracts/incentives)

[PoolAddressesProviderRegistry](../developers/smart-contracts/pool-addresses-provider)

[0xbaA9...5170](https://etherscan.io/address/0xbaA999AC55EAce41CcAE355c77809e68Bb345170)

[ABI](../developers/smart-contracts/pool-addresses-provider)

[AaveOracle](../developers/smart-contracts/aave-oracle)

[0x5458...a0C2](https://etherscan.io/address/0x54586bE62E3c3580375aE3723C145253060Ca0C2)

[ABI](../developers/smart-contracts/aave-oracle)

[RepayWithCollateral](../developers/smart-contracts/switch-adapters)

[0x35bb...0e3E](https://etherscan.io/address/0x35bb522b102326ea3F1141661dF4626C87000e3E)

[ABI](../developers/smart-contracts/switch-adapters)

[CollateralSwitch](../developers/smart-contracts/switch-adapters)

[0xADC0...364e](https://etherscan.io/address/0xADC0A53095A0af87F3aa29FE0715B5c28016364e)

[ABI](../developers/smart-contracts/switch-adapters)

[DebtSwitch](../developers/smart-contracts/switch-adapters)

[0xd785...b442](https://etherscan.io/address/0xd7852E139a7097E119623de0751AE53a61efb442)

[ABI](../developers/smart-contracts/switch-adapters)

[WithdrawSwitchAdapter](../developers/smart-contracts/switch-adapters)

[0x78F8...20e0](https://etherscan.io/address/0x78F8Bd884C3D738B74B420540659c82f392820e0)

[ABI](../developers/smart-contracts/switch-adapters)

[ACLAdmin](../primitives/governance)

[0x5300...192A](https://etherscan.io/address/0x5300A1a15135EA4dc7aD5a167152C01EFc9b192A)

[ABI](../primitives/governance)

[CapsPlusRiskSteward](../primitives/governance)

[0x82dc...7778](https://etherscan.io/address/0x82dcCF206Ae2Ab46E2099e663F70DeE77caE7778)

[ABI](../primitives/governance)

[

Previous

**FAQ**

](https://aave.com/faq)[

Next

**Parameters**

](/docs/resources/parameters)

---

<a id="doc_45"></a>

## 📁 resources / Changelog | Aave Protocol Documentation

*파일 경로: resources/changelog.md*

Source: https://aave.com/docs/resources/changelog

## Changelog

[](#changelog)

### Aave v3 Celo Market

[](#aave-v3-celo-market)

**March 17, 2025**

Aave v3 market deploys on Celo.

### Aave v3 Sonic Market

[](#aave-v3-sonic-market)

**March 3, 2025**

Aave v3 market deploys on Sonic.

### Aave v3.3

[](#aave-v33)

**February 24, 2025**

Introduces logging and burn functionality to manage undercollateralized borrow positions and refines the liquidation logic. Technical details [here](https://github.com/bgd-labs/aave-v3-origin/blob/v3.3.0/docs/3.3/Aave-v3.3-features.md).

### Aave v3 Linea Market

[](#aave-v3-linea-market)

**February 11, 2025**

Aave v3 market deploys on Linea zkEVM.

### Aave v3.2

[](#aave-v32)

**October 8, 2024**

Introduces "Liquid eModes," allowing assets to be listed in multiple eModes, alongside the removal of legacy stable rate logic. Technical details [here](https://github.com/bgd-labs/aave-v3-origin/blob/v3.3.0/docs/3.2/Aave-3.2-features.md)

### Aave v3 ZKsync Era Market

[](#aave-v3-zksync-era-market)

**September 20, 2024**

Aave v3 market deploys on ZKsync Era.

### Aave v3 EtherFi Market

[](#aave-v3-etherfi-market)

**September 9, 2024**

Aave v3 market deploys on Ethereum, optimized for EtherFi collateral assets.

### Aave v3 Ethereum Lido Market (Prime Market)

[](#aave-v3-ethereum-lido-market-prime-market)

**July 29, 2024**

Aave v3 market deploys on Ethereum optimized for blue-chip collaterals and high-leverage, correlated assets.

### Aave v3.1

[](#aave-v31)

**July 27, 2024**

Introduces security and operational improvements to protocol smart contracts. Technical details [here](https://github.com/bgd-labs/aave-v3-origin/blob/v3.3.0/docs/Aave-v3.1-features.md).

### GHO Cross-Chain

[](#gho-cross-chain)

**July 2, 2024**

Introduces a GHO facilitator that enables cross-chain bridging to Arbitrum powered by Chainlink CCIP.

### Aave v3 Scroll Market

[](#aave-v3-scroll-market)

**February 9, 2024**

Aave v3 market deploys on Scroll zkEVM Layer 2.

### GHO Stability Module

[](#gho-stability-module)

**January 29, 2024**

Introduces a GHO facilitator that supports the conversion of GHO with governance-approved assets at pre-determined ratios to maintain peg stability.

### Aave v3 BNB Chain Market

[](#aave-v3-bnb-chain-market)

**January 23, 2024**

Aave v3 market deploys on BNB Chain.

### Aave Governance v3

[](#aave-governance-v3)

**December 25, 2023**

Enhances Aave protocol governance, enabling voting on low-cost networks and improving efficiency of cross-chain proposals.

### Aave v3 Gnosis Market

[](#aave-v3-gnosis-market)

**November 6, 2023**

Aave v3 market deploys on Gnosis Chain.

### Aave v3 Base Market

[](#aave-v3-base-market)

**August 16, 2023**

Aave v3 deploys on Base, Coinbase’s Layer 2 network built on the OP Stack.

### GHO Stablecoin

[](#gho-stablecoin)

**July 16, 2023**

Launches GHO, Aave’s native decentralized stablecoin.

### Aave v3.0.2

[](#aave-v302)

**May 6, 2023**

Updates the Aave V3 codebase, addressing security and usability improvements. Technical details [here](https://github.com/bgd-labs/proposal-3.0.2-upgrade/blob/main/README.md).

### Aave v3 Metis Market

[](#aave-v3-metis-market)

**March 17, 2023**

Aave v3 deploys on the Metis Layer 2 network.

### Aave v3 Ethereum Core Market

[](#aave-v3-ethereum-core-market)

**January 27, 2023**

Aave v3 deploys on Ethereum, bringing the latest protocol innovations to mainnet. The Core market serves as the most liquid and risk-adjusted environment for a diverse range of assets.

### Aave v3

[](#aave-v3)

**March 16, 2022**

A new iteration of the Aave Protocol, introducing new features such as efficiency mode and enhanced risk measures with isolation mode, supply caps, and borrow caps.

### Aave v2 Avalanche Market

[](#aave-v2-avalanche-market)

**October 4, 2021**

Aave v2 deploys on the Avalanche C-Chain network.

### Aave v2 Polygon Market

[](#aave-v2-polygon-market)

**April 14, 2021**

Aave v2 deploys on Polygon (formerly Matic), the first protocol deployment outside of Ethereum mainnet.

### Aave Governance v2

[](#aave-governance-v2)

**December 16, 2020**

Enhances on-chain protocol governance, enabling the Aave community to propose, vote, and trustlessly execute protocol changes.

### Aave v2

[](#aave-v2)

**December 3, 2020**

Aave v2 greatly enhances protocol efficiency with reduced gas costs and new features such as collateral switch and batch flash loans.

### Aave Governance v1

[](#aave-governance-v1)

**October 29, 2020**

Introduces the first version of Aave’s governance mechanism, enabling the community to propose and vote on protocol updates.

### Aave v1

[](#aave-v1)

**January 8, 2020**

The first iteration of the Aave Protocol launches on Ethereum mainnet, introducing decentralized liquidity pools, allowing users to supply and borrow various assets via smart contracts.

[

Previous

**Code Licensing**

](/docs/resources/code-licensing)[

Next

**Web3**

](/docs/resources/web3)

---

<a id="doc_46"></a>

## 📁 resources / Code Licensing | Aave Protocol Documentation

*파일 경로: resources/code_licensing.md*

Source: https://aave.com/docs/resources/code-licensing

## Code Licensing

[](#code-licensing)

The Aave Protocol operates on decentralized blockchain networks, with smart contracts that are self-executing and publicly auditable. These smart contracts and peripheral interfaces are licensed to define and regulate the use of the underlying code. The code exists across multiple GitHub repositories, and below are examples of some key licenses that apply to different Aave components:

*   **Aave v3.3 Smart Contracts**: Business Source License 1.1 permits non-commercial use and modification, restricting competitive use for four years, with a transition to the MIT License on March 6, 2027​. ([GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/LICENSE))
    
*   **Aave v3.2 Smart Contracts**: Business Source License 1.1 permits non-commercial use and modification, restricting competitive use for four years, with a transition to the MIT License on March 6, 2027​. ([GitHub](https://github.com/aave-dao/aave-v3-origin/blob/main/LICENSE))
    
*   **Governance v3**: Business Source License 1.1 permits non-commercial use and modification, restricting competitive use for four years, with a transition to the MIT License on July 27, 2027.​ ([GitHub](https://github.com/bgd-labs/aave-governance-v3/blob/main/LICENSE))
    
*   **Safety Module**: Business Source License 1.1 permits non-commercial use and modification, with competitive restrictions, transitioning to the MIT License on January 8, 2028.​ ([GitHub](https://github.com/bgd-labs/stake-token/blob/main/LICENSE))
    
*   **GHO Stablecoin**: MIT License grants free and unrestricted rights to use, copy, modify, and distribute the software, provided the original copyright notice and license are included. The software is provided "as is," with no warranties or liabilities for any issues arising from its use. ([GitHub](https://github.com/aave/gho-core/blob/main/LICENSE))
    
*   **Aave v2 Smart Contracts**: GNU Affero General Public License ([GitHub](https://github.com/aave/protocol-v2/blob/master/LICENSE.md))
    
*   **Aave v1 Smart Contracts**: GNU Affero General Public License ([GitHub](https://github.com/aave/aave-protocol/blob/master/LICENSE.md))
    
*   **Aave Labs Interface**: All Rights Reserved. ([GitHub](https://github.com/aave/interface/blob/main/LICENSE.md))
    

[

Previous

**Access Controls**

](/docs/resources/access-controls)[

Next

**Changelog**

](/docs/resources/changelog)

---

<a id="doc_47"></a>

## 📁 resources / Glossary | Aave Protocol Documentation

*파일 경로: resources/glossary.md*

Source: https://aave.com/docs/resources/glossary

## Aave Docs Glossary

[](#aave-docs-glossary)

Term

Description

aTokens

Interest-bearing tokens received by users when they supply assets to Aave. aTokens represent the user’s share of the liquidity pool and accrue interest in real-time.

APY

Annual Percentage Yield, which is the yield/interest after a year, including compounding interest. This differs from APR, which does not account for compounding effects.

Borrow Cap

A limit set by Aave Governance on the maximum amount of an asset that can be borrowed from the protocol. This helps manage exposure and risk associated with each asset.

Collateral

An asset supplied to Aave to secure a borrowing position. The collateral must exceed the value of the borrowed amount to ensure the protocol's solvency.

Cooldown Period

A mandatory waiting period that stakers must observe before they can unstake their tokens from the Safety Module.

Credit Delegation

A feature where users can delegate their borrowing power to another user who can then take out loans using the collateral of the delegator. This is facilitated through the Aave Protocol's smart contracts.

Debt Ceiling

The maximum amount of debt that can be issued against an isolated asset. Used to limit the risk exposure to a single collateral type.

E-Mode

Efficiency Mode allows borrowers to extract higher borrowing power when using correlated assets (e.g., stablecoins).

Flash Loan

A type of uncollateralized loan offered by Aave, which must be borrowed and repaid within one transaction block.

GHO

A decentralized, overcollateralized stablecoin that is fully backed, transparent, and native to the Aave Protocol. It is governed and managed by the Aave DAO.

Governance Power

Refers to the ability to create proposals or vote in Aave’s governance system, based on AAVE, stkAAVE, or aAAVE token holdings.

Health Factor

A ratio that determines the health of a user's loan position. It compares the value of the user's collateral to their borrowed assets. A health factor below 1 triggers liquidation.

Isolation Mode

A feature in Aave V3 that limits borrowers to borrowing only certain stablecoins when using assets marked as isolated. It helps mitigate risk by restricting the total debt exposure to a single asset.

Liquidation

The process that occurs when a borrower’s health factor drops below 1, resulting in the sale of collateral to repay part of the debt and bring the position back to a safer level.

Liquidation Bonus

The bonus provided to liquidators as an incentive to purchase undercollateralized assets in a liquidation event. It is expressed in percentage points.

Liquidation Threshold

The point at which a loan becomes eligible for liquidation due to insufficient collateral relative to borrowed funds. The threshold is defined per asset and determines the collateral value required to maintain a position.

Liquidity Index

Tracks the cumulative interest earned by a reserve over time, used to calculate accurate interest payments.

Loan To Value (LTV)

The maximum percentage of a collateral asset's value that can be borrowed. For example, an LTV of 75% means that for every 1 ETH of collateral, 0.75 ETH can be borrowed.

Network Risk

Risks associated with the blockchain networks on which Aave operates, such as congestion, security vulnerabilities, or network failures.

Oracle

A service used by Aave to fetch external data, such as the prices of assets, which is critical for determining the value of collateral and debt.

Portal

A cross-chain liquidity feature in Aave V3 allowing liquidity to flow between Aave markets on different blockchains. This is made possible through governance-approved bridges.

Ray units

A unit of measurement with 27 decimals, used by Aave for internal calculations to ensure precision, particularly for rates and exchange values.

Reserve Factor

A percentage of interest accrued by borrowers that is allocated to the Aave Treasury to help safeguard the protocol.

Risk Admin

An entity or automated system responsible for adjusting risk parameters in Aave without going through a governance vote. This allows Aave to respond quickly to unforeseen risks.

Safety Module

A staking mechanism where AAVE tokens are staked to act as insurance in case of a shortfall event. Stakers earn rewards but are also exposed to slashing risk.

Siloed Borrowing

A feature in Aave V3 that restricts certain assets to being borrowed alone, mitigating the risk of price manipulation or illiquid assets affecting the protocol's solvency.

Supply Cap

A limit set on the total amount of a particular asset that can be supplied to the Aave protocol.

Utilization Rate

A metric that determines the proportion of borrowed assets to the total available assets in a reserve. A higher utilization rate indicates higher borrowing demand.

Voting Power

The amount of influence a user has in governance decisions, determined by the amount of AAVE, stkAAVE, or aAAVE they hold.

[

Previous

**Web3**

](/docs/resources/web3)

---

<a id="doc_48"></a>

## 📁 resources / Parameters Dashboard | Aave Protocol Documentation

*파일 경로: resources/parameters.md*

Source: https://aave.com/docs/resources/parameters

## Aave Protocol Parameter Dashboard

[](#aave-protocol-parameter-dashboard)

Integrate live data into JavaScript project with the [Aave Utilities](https://github.com/aave/aave-utilities) SDK and [Aave Address Book](https://github.com/bgd-labs/aave-address-book) registry.

[

Previous

**Addresses**

](/docs/resources/addresses)[

Next

**Access Controls**

](/docs/resources/access-controls)

---

<a id="doc_49"></a>

## 📁 resources / Web3 | Aave Protocol Documentation

*파일 경로: resources/web3.md*

Source: https://aave.com/docs/resources/web3

## Web3

[](#web3)

Web3 is the next evolution of the internet where people have control and ownership over their data, the relationships they form online, and their user profile. Together, these make up "social capital": Everyone has it, and it's valuable. In contrast, today when we go on the internet, we visit sites owned by large companies, who own our social capital. These "web2" companies like Amazon, Facebook and Google store user data on privately-held servers and sell it to advertisers in exchange for providing free services. This has led to a good experience for users (free, easy-to-use networks and applications), but it has also caused privacy issues, data manipulation, and limited monetisation options. Web3 addresses these issues by using blockchain technology. This technology is based on user ownership. When people own their data, they can monetise however they want, take their digital information with them (profile, content, data) when they switch networks, and it has the benefit of putting people and apps/networks on an equal footing. Web3 enables a more open and balanced internet, where people have a stake and voice in the future of the internet.

To understand the significant difference between the internet we know today (web2) and web3, take a step back.

When the internet first came about, it was hard to access because there were no easy-to-use applications. Web1 was built on open, public protocols or applications such as TCP, IP, SMTP, and HTTP that builders could develop on top of, plugging into these open protocols to create whatever applications or platforms they wanted. Nobody needed permission to use these foundational protocols or standards to build user-friendly applications like email browsers and marketplaces. These standards are the basic building blocks of the internet. They govern how computers interact with each other and the flow of information. Today, in many senses, we are locked into platforms that own our data.

## Blockchain

[](#blockchain)

A blockchain is a decentralised, distributed ledger system designed to record and verify transactions across a network of computers. This compels that no single entity or company controls the entire network, promoting a system of collective agreement and transparency. Unlike traditional databases that rely on central authorities (private servers owned by companies who set all the rules and make all the decisions), blockchains operate on a peer-to-peer network where every participant, known as nodes, has access to the entire ledger (the information is spread across multiple nodes or computers and each has an entire copy of the information). This decentralisation enhances both security and transparency, as each transaction is visible to all participants and cannot be altered without consensus (all nodes agreeing) from the network.

The core of blockchain technology lies in its unique distributed or decentralised structure. Transactions are grouped into units called "blocks." Each block contains a list of transactions that have been validated (consensus) by the network. Once a block is filled with transactions, it is added to the existing chain of blocks in a sequential manner that is time stamped. This process creates a continuous, unalterable chain of blocks, hence the name "blockchain." Each block contains a reference to the previous block, forming a chronological sequence. This structure makes it extremely difficult to alter any information in a block without changing all subsequent blocks, which would require the consensus of the majority of the network.

## Smart Contracts

[](#smart-contracts)

Smart contracts are self-executing programs that operate deterministically. When an address interacts with a smart contract, the contract executes the agreed-upon actions, such as transferring assets or updating internal accounting. This automation eliminates the need for intermediaries, making transactions more efficient and reducing the potential for human error or manipulation. By relying on code rather than third parties, smart contracts enable trustless and transparent operations, where all parties involved have confidence in the outcome.

Smart contracts are integral to many blockchain applications, as they are executed by blockchain networks like Ethereum, which functions as a global computer network. These networks process and validate the conditions set within each smart contract, updating the state of the contract with every new block added to the chain. This decentralised execution validates that smart contracts run precisely as programmed, without the risk of interference or manipulation. The combination of immutability and public auditability (transparency) in smart contracts provides a high level of trust and security, making them a foundational element in the development of decentralised applications such as identity, finance, and more.

## DeFi

[](#defi)

Decentralised Finance, or DeFi, leverages blockchains and smart contracts to create an open, transparent, and decentralised financial ecosystem. At its core, DeFi aims to improve upon traditional financial systems without the reliance on centralised institutions such as banks, brokers, and financial intermediaries. DeFi offers a novel approach to financial applications, marked by increased accessibility, transparency, and control for users.

DeFi operates on blockchain networks, with Ethereum being the first and most prominent platform. Most of these DeFi applications are now also deployed on Layer 2 blockchains, such as Arbitrum, Optimism, and ZKSync. Unlike traditional financial systems that rely on intermediaries to process and verify transactions, DeFi uses decentralised networks to perform these functions. By removing intermediaries, DeFi aims to lower costs, reduce barriers to entry, and enhance the efficiency of financial transactions.

## Stablecoins

[](#stablecoins)

Stablecoins are digital assets that aim to keep their value constant relative to a reference asset, most commonly fiat currencies like the U.S. dollar, euro, or yen. Unlike Bitcoin or Ethereum, whose values can fluctuate significantly, stablecoins are designed to be predictable and stable, making them useful for everyday transactions, remittances, and as a safe haven during market turbulence.

Stablecoins bridge the gap between traditional finance and the crypto world. They allow users to transfer value globally without major price fluctuations. Here are a few key uses:

*   Remittances: Sending money across borders can be costly and slow. Stablecoins enable faster and cheaper transactions.
    
*   DeFi (Decentralised Finance): Stablecoins are crucial in the DeFi ecosystem, where they are used for supplying, borrowing, and earning interest.
    
*   Hedging: Traders and investors use stablecoins to move out of volatile assets without converting back to fiat.
    
*   Payments: Merchants can accept stablecoins for goods and services without price volatility.
    

Stablecoins achieve stability through various mechanisms:

*   Fiat-collateralised Stablecoins: These are backed by reserves of fiat currency held in a bank account. For every stablecoin issued, an equivalent amount of fiat currency is held in reserve. Examples include Tether (USDT) and USD Coin (USDC).
    
*   Decentralised Stablecoins: These operate without a central authority and are typically issued, redeemed, and governed by smart contracts on a blockchain. Smart contracts can manage the collateral requirements and issuance based on predefined rules in a trustless and transparent process. Aave’s GHO is one example of this kind of stablecoin.
    
*   Algorithmic Stablecoins: These rely on smart contracts and algorithms to maintain their peg. Instead of being backed by reserves, these stablecoins use mechanisms like minting and burning to control the supply and stabilise the price.
    

[

Previous

**Changelog**

](/docs/resources/changelog)[

Next

**Glossary**

](/docs/resources/glossary)

---

*병합된 문서의 끝*
