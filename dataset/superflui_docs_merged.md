# Berachain 문서

*이 문서는 모든 Berachain 문서를 하나의 종합적인 참조로 결합합니다.*

## 목차

1. [concepts/Glossary of Terms](#doc_1)
2. [concepts/What is Superfluid?](#doc_2)
3. [concepts/advanced-topics/Super Apps](#doc_3)
4. [concepts/advanced-topics/Superfluid Host](#doc_4)
5. [concepts/overview/Distributions](#doc_5)
6. [concepts/overview/Money Streaming](#doc_6)
7. [concepts/overview/Super Tokens](#doc_7)
8. [concepts/use-cases/Social & Community](#doc_8)
9. [concepts/use-cases/Token-Cost-Averaging](#doc_9)
10. [faq/Frequently Asked Questions](#doc_10)
11. [governance/Governance Overview](#doc_11)
12. [protocol/Contract Addresses](#doc_12)
13. [protocol/Quickstart](#doc_13)
14. [protocol/advanced-topics/automations/Auto-Wrap](#doc_14)
15. [protocol/advanced-topics/automations/Stream Accounting API](#doc_15)
16. [protocol/advanced-topics/automations/Stream Scheduler](#doc_16)
17. [protocol/advanced-topics/automations/Vesting Scheduler](#doc_17)
18. [protocol/advanced-topics/solvency/Liquidations & TOGA](#doc_18)
19. [protocol/advanced-topics/solvency/Running a Sentinel](#doc_19)
20. [protocol/advanced-topics/solvency/Solvency Dashboard](#doc_20)
21. [protocol/advanced-topics/super-apps/Callbacks](#doc_21)
22. [protocol/advanced-topics/super-apps/Quickstart](#doc_22)
23. [protocol/advanced-topics/super-apps/Registering Super Apps](#doc_23)
24. [protocol/advanced-topics/super-apps/Super Apps in Depth](#doc_24)
25. [protocol/contribute/Bounty Program](#doc_25)
26. [protocol/contribute/Security & Bug Bounties](#doc_26)
27. [protocol/contribute/Token Explorer Submission](#doc_27)
28. [protocol/distributions/Distribution Pools Explained](#doc_28)
29. [protocol/distributions/guides/Create, Update and Connect your Pools](#doc_29)
30. [protocol/distributions/guides/How to Design your Distribution Pools?](#doc_30)
31. [protocol/distributions/guides/Testing](#doc_31)
32. [protocol/examples/Advertisement Auction DApp](#doc_32)
33. [protocol/examples/Staking Platform](#doc_33)
34. [protocol/money-streaming/Money Streaming in Superfluid](#doc_34)
35. [protocol/money-streaming/examples/FlowSplitter Smart Contract](#doc_35)
36. [protocol/money-streaming/guides/Control Flows](#doc_36)
37. [protocol/money-streaming/guides/Manage Access Control and User Data](#doc_37)
38. [protocol/money-streaming/guides/Testing](#doc_38)
39. [protocol/super-tokens/Overview of Super Tokens](#doc_39)
40. [protocol/super-tokens/guides/Using the SuperTokenV1Library](#doc_40)
41. [protocol/super-tokens/guides/deploy-super-token/Deploy a Pure Super Token](#doc_41)
42. [protocol/super-tokens/guides/deploy-super-token/Deploy a Wrapper Super Token](#doc_42)
43. [protocol/super-tokens/guides/deploy-super-token/Deploying a Custom Super Token](#doc_43)
44. [sdk/Quickstart](#doc_44)
45. [sdk/advanced-topics/Batch transactions with Macros](#doc_45)
46. [sdk/distributions/Connecting and Claiming from the Pools](#doc_46)
47. [sdk/distributions/Create and Manage Distribution Pools](#doc_47)
48. [sdk/distributions/Subgraph](#doc_48)
49. [sdk/examples/Rewards Distribution Using Macros](#doc_49)
50. [sdk/money-streaming/Create, Update, and Delete Flows](#doc_50)
51. [sdk/money-streaming/Manage Access Control and User Data](#doc_51)
52. [sdk/money-streaming/Subgraph](#doc_52)
53. [sdk/super-tokens/How to make your balance dance?](#doc_53)
54. [sdk/super-tokens/Tracking Super Token Balances](#doc_54)
55. [sdk/super-tokens/Wrap and Unwrap Super Tokens](#doc_55)
56. [technical-reference/CFAv1Forwarder](#doc_56)
57. [technical-reference/GDAv1Forwarder](#doc_57)
58. [technical-reference/ISETH](#doc_58)
59. [technical-reference/ISuperToken](#doc_59)
60. [technical-reference/ISuperfluidPool](#doc_60)
61. [technical-reference/Protocol Architecture](#doc_61)
62. [technical-reference/Subgraph Endpoints](#doc_62)
63. [technical-reference/SuperTokenV1Library](#doc_63)
64. [use-cases/Superfluid Vesting](#doc_64)

---

<a id="doc_1"></a>

## 📁 concepts / Glossary of Terms

*파일 경로: concepts/glossary.mdx*

import Link from '@docusaurus/Link';


This glossary provides a comprehensive overview of terms and concepts within the Superfluid ecosystem.

### General Conceptual Terms

**Superfluid Ecosystem**: The collective of users and Super Apps utilizing real-time finance through Superfluid.

**Real-Time Finance**: The movement of money on a second-by-second basis enabled by Superfluid's smart contract framework.

### Super Tokens

**Super Token**: Tokens used in all Superfluid operations. Types include ERC20 Wrapper Tokens, Pure Super Tokens, and Native Asset Super Tokens. Detailed information is available in our [Super Tokens section](../developers/super-tokens/super-tokens/).

**Wrap**: The process of converting ERC20 tokens into wrapped super tokens. This involves transferring ERC20 assets into the wrapper contract and receiving an equivalent amount of super tokens.

**Unwrap**: Converting wrapped super tokens back into their underlying ERC20 assets. This involves burning super tokens and transferring the underlying asset to the user.

**Real Time Balance**: A dynamic calculation of an account's balance, considering both Superfluid agreement logic and static token balances.

### Agreements

**Superfluid Agreement**: Additional functionalities for Super Tokens provided by the Superfluid protocol. Examples include the Constant Flow Agreement and the Instant Distribution Agreement, with potential for more in the future.

**Constant Flow Agreement (CFA)**: An agreement allowing perpetual, second-by-second movement of Super Tokens between addresses.

**Instant Distribution Agreement (IDA)**: An agreement for mass dispersion of Super Tokens to multiple addresses based on distribution shares or "units" at a fixed gas cost.

**Flow**: A continuous money stream from one address to another. A sender can maintain only one flow to the same receiver per token.

**Flow Rate**: The amount of tokens sent in a stream, denominated in wei per second.

**Net Flow Rate**: The net amount of tokens sent or received per second by an account for a specific token.

**ACL (Access Control List)**: A feature enabling varying levels of control to operators for creating, updating, or deleting streams on behalf of an account.

**Index**: A pool created using the Instant Distribution Agreement.

**Publisher**: The creator of an Index.

**Units**: Shares denoting an address’s share of an IDA index, interchangeable with "distribution shares".

**Distribution**: The action of sending tokens to addresses owning shares in an index, proportionate to the number of shares held.

### Protocol

**Callback**: A function that automatically executes when specific actions are taken. Super Apps use callbacks to respond to Superfluid-related actions.

**User Data**: Data that can be included with Superfluid function calls and utilized within Super App callbacks.

**Batch Calls**: A Super Token feature allowing multiple actions to be executed in a single transaction.

**The Superfluid Host**: The core of the protocol, processing function calls and facilitating protocol governance and Super App callbacks.

**Resolver**: A contract assisting in locating all protocol constituent contract addresses.

### Sentinels & Solvency

**Buffer**: Tokens locked temporarily when a stream starts.

**Liquidation**: The process initiated by a sentinel when an account's balance reaches zero while streaming funds.

**Sentinel**: A node monitoring the Superfluid network and closing critical or insolvent streams. Anyone can run a sentinel node.

**PIC (Patrician in Charge)**: The recipient of rewards for closing streams during the priority period when an account becomes critical.

**TOGA (Transparent Ongoing Auction)**: An auction allowing individuals to become the PIC by staking a higher amount than the current PIC.

**Stake**: Funds locked in the TOGA contract by the PIC.

**Top Up**: Adding to a Super Token balance to prevent liquidation due to a zero balance.

---

<a id="doc_2"></a>

## 📁 concepts / What is Superfluid?

*파일 경로: concepts/superfluid.mdx*

---
sidebar_position: 1
---


### Introduction

Superfluid is a revolutionary asset [streaming](./overview/money-streaming.mdx) and [distribution](./overview/distributions.mdx) protocol bringing subscriptions, salaries, vesting,
and rewards to DAOs and crypto-native businesses worldwide. This is made possible by the protocol’s smart contract
framework which introduces the [Super Token](./overview/super-tokens.mdx) - an extension to the [ERC-20](https://eips.ethereum.org/EIPS/eip-20) standard 
enabling the transfer of value in completely novel ways.

### Super Tokens

The Superfluid protocol is designed to be a "token-centric" protocol, in that all of its functionalities revolve around the concept of [Super Tokens](./overview/super-tokens.mdx).
The framework & Super Token standard can be used to add dynamic balances to tokens on chain,
describing cash flows and executing them automatically over time in a non-interactive way.
Any token can be transferred in Superfluid streams or distributions, which are programmable, composable, and modular.
No capital is locked up, and all inflows and outflows are netted in real-time at every block without consuming any gas.
The code is fully open source, while the protocol is non-custodial and permissionless.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    <img src="/assets/Superfluid-main-GIF.gif" alt="Superfluid with people" width="600" />
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*A visualization of the Superfluid Protocol*</p>
</div>

**The Superfluid Protocol has currently two main pillars that define its interactions with Super Tokens. These pillars (formerly called Agreements) are the following:**
- [***Money Streaming***](./overview/money-streaming.mdx) - A set of features that enable the creation of money streams between two parties.
- [***Distributions***](./overview/distributions.mdx) - A set of features that enables the creation of a pool of funds that can be distributed to multiple recipients.

We go in further details about these two pillars in the next sections.

### Money Streaming

#### Definition

Money Streaming is a continuous transfer of tokens from a sender to a receiver at a defined per-second rate, resulting in a "stream". This stream is perpetual and persists until it's canceled by either the sender or the receiver, or until the sender's Super Token balance is depleted.

#### Explanation

Money Streaming is a novel approach to token transfers, offering a dynamic way of sending funds. Instead of one-time transactions, tokens flow from the sender to the receiver continuously, creating a stream. This method provides real-time financial transactions, enabling a more fluid movement of assets over time, reflecting real-world economic activities more closely.

#### Example

<div style={{ display: 'flex', justifyContent: 'center' }}>
    <img src="/assets/Superfluid-GIF.gif" alt="Superfluid with people" width="600" />
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*A visualization of money streaming from the [Superfluid dashboard](https://app.superfluid.finance/)*</p>
</div>

Consider Alice wants to pay Bob a salary of 1200 USDCx per year using Money Streaming. She sets up a stream with a flow rate of 0.038 USDCx per second. Bob's balance starts increasing every second, and Alice's decreases, ensuring a steady transfer of salary.

### Distributions

#### Definition

Distributions in Superfluid refer to a scalable one-to-many fund transfer method. It involves creating pools with a pool admin managing units for members, who can receive funds instantly or through continuous streaming.

#### Explanation

Distributions are a significant advancement in decentralized finance, enabling efficient and scalable fund transfers among multiple recipients. This method is especially useful for scenarios where funds need to be distributed among many parties, like dividends or rewards, ensuring equitable and automated distribution based on predefined units.

#### Example

Imagine a DeFi project creating a reward pool for liquidity providers. The project sets up a distribution pool with a total of 1000 units. If a liquidity provider has 100 units, they receive 10% of the total funds distributed through the pool, either instantly or as a continuous stream, depending on the distribution method.

---

<a id="doc_3"></a>

## 📁 concepts/advanced-topics / Super Apps

*파일 경로: concepts/advanced-topics/super-apps.mdx*

---
sidebar_position: 4
---
import Admonition from '@theme/Admonition';


Super Apps represents a class of smart contracts that interact seamlessly with the Superfluid Protocol, enabling dynamic responses to Money streaming or Distributions (Also called Super Agreements).

### Definition

Super Apps are smart contracts registered with the Superfluid Protocol, designed to **react to Super Agreements**. These reactions are facilitated through callbacks, allowing Super Apps to engage dynamically with the creation, modification, and termination of Super Agreements.

### **Reacting to Super Agreements**

The reactivity of Super Apps stems from **callbacks**. These are segments of code within the Super App that are triggered when a Super Agreement involving the Super App is created, updated, or deleted. Such callbacks can execute various actions, from minting NFTs to initiating new Streams (Constant Flow Agreements).

#### **Example - Stream Consolidator Super App**

Consider a Super App designed to consolidate all incoming flows into a single outgoing flow to a specific account (Account Z):

1. **Incoming Flow from Account A**: Account A initiates a Money Stream to the Super App (100 USDCx/mo). The Super App, in turn, starts an outbound Stream of the same rate to Account Z.
2. **Multiple Flow Adjustments**: If Account B starts a new Money Stream to the Super App (25 USDCx/mo) and Account A adjusts its flow (to 50 USDCx/mo), the Super App responds by updating its outbound Streams accordingly.
3. **Ongoing Reactions**: The Super App continues to adapt to new Money Streams or adjustments from various accounts, maintaining a reactive outbound flow.

<Admonition type="info">
<strong>NOTE</strong>: For a smart contract to qualify as a Super App, it must have defined callbacks to interact with Super Agreements.
</Admonition>

### Registering With The Protocol

Registration of a Super App with the Superfluid Protocol is crucial. This registration process involves coding the smart contract to be identifiable as a Super App within the protocol.

#### Purpose of Registration

- **Protocol Recognition**: When a stream is initiated towards a contract, the Superfluid Protocol checks if the recipient is a registered Super App.
- **Callback Activation**: If identified as a Super App, the protocol activates the Super App's callbacks, enabling its reactive capabilities.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![Super App Registration](/assets/image_(82).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Super App Registration*</p>
</div>

### Why Are Super Apps Needed?

Super Apps introduce a layer of programmability to Super Agreements, enhancing the potential for innovative decentralized applications (dApps).

#### Potential Use Cases

- **Lending Applications**: Automate loan repayments through Streams, eliminating the need for manual transactions.
- **Subscription Services**: Enable on-chain subscriptions paid via Streams, incorporating features like automatic affiliate payouts.

Super Apps open up a realm of possibilities, combining custom logic with the functionalities of Super Agreements to craft unique and scalable dApps.

For further inspiration, explore the following examples of Super Apps:

[Explore Super App Examples](https://github.com/superfluid-finance/super-examples)

---

<a id="doc_4"></a>

## 📁 concepts/advanced-topics / Superfluid Host

*파일 경로: concepts/advanced-topics/superfluid-host.mdx*

---
sidebar_position: 5
---

import Admonition from '@theme/Admonition';


The Superfluid Host Contract is a central element of the Superfluid Protocol, acting as a hub connecting Super Tokens, Super Agreements, and Super Apps.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![Superfluid Host Contract](/assets/image_(68)_(1).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Superfluid Host Contract*</p>
</div>

Let's explore how the Host Contract interacts with different components of the Superfluid Protocol.

### Super Agreements 🔗 Host Contract

Super Agreements, each with their unique contracts, interface with the Host Contract. Interaction with a Super Agreement is typically done by calling [`callAgreement()`](https://docs.superfluid.finance/superfluid/developers/solidity-examples/interacting-with-superfluid-smart-contracts) on the Host Contract, specifying the agreement and parameters.

#### Key Points

- **Upgradeability and Expansion**: Super Agreements can be updated or new ones can be added and registered with the Host Contract.

<Admonition type="info">
<strong>NOTE</strong>: Direct interactions with Super Token contracts are not required for invoking Super Agreements. Instead, these agreements are accessed via the Host Contract, which then manages the Super Token balances involved.
</Admonition>

### Super Tokens 🔗 Host Contract

Super Tokens form the foundational layer of the Superfluid Protocol, where all Super Agreement data for an account is compiled.

#### Functionality

- **Aggregated Balance Calculation**: The impact of each Super Agreement on an account's balance is cumulatively calculated to determine the Super Token balance.
- **Data Sourcing**: Super Token contracts obtain necessary data through the Host Contract by iterating over the registered Super Agreements.

### Super Apps 🔗 Host Contract

Registration of Super Apps with the Superfluid Host is essential to enable their callback functionalities.

#### Interaction Mechanics

- **Registration Requirement**: Super Apps must be registered with the Host to function correctly.
- **Callback Activation**: When a Super Agreement is engaged with a Super App, the Host Contract triggers the Super App's callbacks.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![Super Apps and Host Contract](/assets/image_(58).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Super Apps and Host Contract*</p>
</div>

In summary, the Superfluid Host Contract is integral to the Superfluid Protocol, facilitating seamless interactions and integrations among Super Tokens, Super Agreements, and Super Apps.

---

<a id="doc_5"></a>

## 📁 concepts/overview / Distributions

*파일 경로: concepts/overview/distributions.mdx*

---
sidebar_position: 3
---

import PoolInstantVis from "@site/src/components/Visualizations/PoolInstantVis";
import PoolStreamVis from "@site/src/components/Visualizations/PoolStreamVis";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import ThemedImage from '@theme/ThemedImage';



The introduction of Distributions marks a significant advancement in DeFi applications, offering a scalable method for one-to-many fund transfers.
Distributions allow for the transfer of value to multiple recipients with minimal on-chain data modification, making them infinitely scalable, highly efficient and gas-friendly.

:::note
There are other on-chain solutions that may seem to solve this problem without using a new token implementation (e.g [Disperse App](https://disperse.app/)).
While these solutions can be great for a low amount of recipients, they are not infinitely scalable and can become very expensive as the number of recipients increases. Furthermore, they do not allow for distributing money streaming
:::

### Overview

Distributions function by allowing for the creation of **pools** with a designated **pool admin** who manages **units** for **pool members**. Members of these pools can receive funds either instantly or through continuous streaming, making this method highly efficient and scalable. There are two types of Distributions:

- **Instant Distributions**: They allow one transaction distribution to any number of receivers with a fixed gas cost.
- **Streaming Distributions**: They allow for continuous distribution of funds to receivers through [Money Streaming](./money-streaming.mdx) to a Pool.

---
<Tabs defaultValue="instant" values={[
  { label: 'Instant Distribution', value: 'instant' },
  { label: 'Streaming Distribution', value: 'streaming' },
]}>
<TabItem value="instant">

**Instant Distributions** allow one transaction to distribute to any number of receivers with a fixed gas cost.

<div style={{ display: "flex", justifyContent: "center" }}>
  *Click on the Blue Circle to initiate an Instant Distribution*
  <br />
</div>
<PoolInstantVis />
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>
    *By creating a Distribution Pool, you can distribute any token instantly*
  </p>
</div>

  </TabItem>
  <TabItem value="streaming">

**Instant Distributions** allow for continuous distribution of funds to receivers through [Money Streaming](./money-streaming.mdx) to a Pool.

<div style={{ display: "flex", justifyContent: "center" }}>
  *Watch how the continuous stream gets distributed automatically through the pool*
  <br />
</div>
<PoolStreamVis />
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>
    *By creating a Distribution Pool, you can distribute any stream with no gas cost*
  </p>
</div>

  </TabItem>
  
</Tabs>

---

#### Definitions

- **Pool**: A channel for proportional token distribution.
- **Distribution**: The action of allocating specified token amounts to receivers.
- **Units**: Represent the proportion of the distribution each subscriber receives.
- **Pool Admin**: The administrator of the distribution process.
- **Subscribers/Pool Member**: Receivers allocated units and eligible to receive tokens through the Index.

#### Key Features

- **Pools as Contracts**: Unlike previous approaches, pools in streaming distributions are contracts and can be ERC20 tokens. This allows pool members to transfer units among themselves, which wasn't possible earlier.
- **Roles and Permissions**: A pool admin can grant and revoke units, while any account can act as a **distributor** to execute fund distributions.
- **Distribution Methods**: There are two primary ways to distribute funds:
  - **Instant Distribution**: Calculated as `distributionAmount * (poolMemberUnits / poolTotalUnits)`.
  - **Streaming Distribution**: Determined by `poolFlowRate * (poolMemberUnits / poolTotalUnits)`.
- **Gas Efficiency**: The cost of executing distributions remains constant, regardless of the number of pool members.

#### High-Level Workflow

1. **Pool Creation**: Any account can create a pool and appoint a pool admin. This pool acts as a channel for distributing funds.
2. **Unit Management**: The pool admin assigns units to members, representing their share in future distributions.
3. **Member Connection**: Pool members can connect to or disconnect from the pool, affecting how they access distributed funds.
4. **Distribution Execution**: Distributors can initiate either instant or streaming distributions, which are then divided among pool members based on their unit share.

### Distribution Examples

#### Streaming Distribution Illustration

This diagram shows a distributor streaming funds to various pool members, each holding different unit amounts. Note: A single transaction can cater to multiple members.

<div style={{ display: "flex", justifyContent: "center" }}>
![Streaming Distribution](/assets/streaming-distribution-light.png)
</div>


#### Adjusting Unit Counts

Here, a distributor modifies unit counts for members. This change instantly alters the distribution rate for all members in one transaction. Batch updates can be done using Superfluid's batch call.

<div style={{ display: "flex", justifyContent: "center" }}>
![Unit Count Adjustment](/assets/unit-count-adjustment.png)
</div>

#### Modifying the Flow Rate

This example demonstrates how a change in the distributor's streaming rate affects the total flow rate of the pool, thus instantly impacting each member's rate.

<div style={{ display: "flex", justifyContent: "center" }}>
![Flow Rate Change](/assets/modify-flow-rate.png)
</div>

### Advanced Pool Features

As pools are also ERC20 tokens, they enable:

- **Transfer of Units**: Pool members can freely transfer their units.
- **Delegated Transfers**: Using the `approve` and `transferFrom` functions, units can be transferred on behalf of a member.

These features add composability and flexibility, expanding the potential use cases for pools in web3.

---

<a id="doc_6"></a>

## 📁 concepts/overview / Money Streaming

*파일 경로: concepts/overview/money-streaming.mdx*

---
sidebar_position: 2
---
import Admonition from '@theme/Admonition';


### Definition

Money Streaming is a process where tokens are continuously transferred from a sender to a receiver at a defined per-second rate. The result of this process is a "stream". A stream is perpetual and will continue until canceled by the sender/the receiver or the sender's Super Token balance is depleted.

### **Terminology**

- **Flow Rate**: The rate at which the sender's balance decreases and the receiver's increases per second.
- **Netflow Rate**: The rate of change of an account's Super Token balance per second.
- **Sender**: The account initiating the stream, specifying a receiver and flow rate.
- **Receiver**: The account on the receiving end of a stream.
- [**CRUD Timestamp**](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete): The timestamp when a stream is created, updated, or deleted.
- **Real-Time Balance**: The change in the account's Super Token balance since the last CRUD action.
- **Static Balance**: The Super Token balance at the last CRUD timestamp.
- **Current Balance**: The sum of Static Balance and Streaming Real-Time Balance.

<Admonition type="info">
<strong>NOTE</strong>: Flow rates are per second but can be represented in different time units for convenience. For example, "100 USDCx/mo." is approximately "0.0039 USDCx/sec."
</Admonition>

### Computation

The netflow for an account is calculated by netting its inbound and outbound streaming flow rates.

<div style={{ display: "flex", justifyContent: "center" }}>
  ![Netflow Calculation](/assets/image_(63).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*Example of Net Flow calculation*</p>
</div>

When a stream is modified, the following are updated in the Superfluid contracts:

1. New Netflow rate
2. New CRUD timestamp
3. New Static Balance: set to the Current Balance at the CRUD timestamp
4. Real-Time Balance reset to zero

The Real-Time Balance then adjusts by-the-second at the netflow rate.

<div style={{ display: "flex", justifyContent: "center" }}>
  ![Streaming Real-Time Balance](/assets/image_(50)_(1).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*Streaming Real-Time Balance*</p>
</div>

<Admonition type="info">
<strong>NOTE</strong>: Creating a stream is a one-time action. The balance is dynamically calculated and does not require continuous transactions.
</Admonition>

### **Formula**

- **Static Balance**: Initial balance at the latest CRUD timestamp
- **Real-Time Balance**: Netflow Rate * Seconds since the latest CRUD timestamp
- **Current Balance**: Static Balance + Real-Time Balance

### Example - Monitoring Account A's Current Balance

Let's examine how Account A's balance changes with stream interactions.

##### **1. Starting an Outbound Stream**

<div style={{ display: "flex", justifyContent: "center" }}>
  ![Outbound Stream](/assets/image_(50)_(1)_(1).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*Outbound Stream*</p>
</div>

- Initial Balance: 1000 USDCx
- Flow Rate to Account B: 0.01 USDCx/sec
- Time Elapsed: 1000 seconds
- **Current Balance**: 990 USDCx

##### **2. Increasing the Flow Rate**



<div style={{ display: "flex", justifyContent: "center" }}>
  ![Flow Rate Increase](/assets/image_(60).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*Flow Rate Increase*</p>
</div>

- Static Balance: 990 USDCx
- New Flow Rate: 0.02 USDCx/sec
- **Current Balance**: 990 USDCx

##### **3. Time Elapse Post Flow Rate Change**

<div style={{ display: "flex", justifyContent: "center" }}>
  ![Time Elapse](/assets/image_(59)_(1).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*Time Elapse*</p>
</div>

- Time Elapsed: 2000 seconds
- **Current Balance**: 950 USDCx

##### **4. Receiving an Inbound Stream**

<div style={{ display: "flex", justifyContent: "center" }}>
    ![Inbound Stream](/assets/image_(57).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
    <p>*Inbound Stream*</p>
</div>

- Inbound Flow Rate from Account C: 0.04 USDCx/sec
- **Current Balance**: 950 USDCx

##### **5. Post Inbound Stream Time Elapse**

<div style={{ display: "flex", justifyContent: "center" }}>
    ![Post Inbound Stream](/assets/image_(39).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
    <p>*Post Inbound Stream*</p>
</div>

- Time Elapsed: 1000 seconds
- **Current Balance**: 970 USDCx

##### **6. Deleting the Outbound Stream**

<div style={{ display: "flex", justifyContent: "center" }}>
    ![Deleting Outbound Stream](/assets/image_(38).png)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
    <p>*Deleting Inbound Stream</p>
</div>

- Static Balance: 970 USDCx
- **Current Balance**: 970 USDCx

### Other Considerations

##### Discrete Actions and Active Streams

Transferring, wrapping, or unwrapping Super Tokens, being lump-sum actions, only affect the Static Balance and not the Real-Time Balance.

##### Interaction with Distributions 

Actions within Distributions have their own Real-Time Balance and are added separately to the overall account balance.

### Solvency and Sentinels

Accounts with negative net flow rates reaching zero balance are considered **critical**. Superfluid handles this with buffer deposits and Sentinels.

#### Buffer

Buffer deposits are taken when opening a stream, serving as a reserve in case of a critical balance. If a stream is closed before hitting critical, the buffer is refunded. In cases where the account becomes critical, the buffer is used to continue outbound streams until Sentinels intervene.

#### Sentinels

Sentinels are external actors who monitor Constant Flow Agreements (Money Streaming), close streams of critical accounts, and earn buffer deposits.

_For more details, see the [Liquidations](/docs/protocol/advanced-topics/solvency/liquidations-and-toga.mdx) and [Sentinels](/docs/protocol/advanced-topics/solvency/running-a-sentinnel.mdx) pages._

---

<a id="doc_7"></a>

## 📁 concepts/overview / Super Tokens

*파일 경로: concepts/overview/super-tokens.mdx*

---
sidebar_position: 1
---

import SuperTokenVis from "@site/src/components/Visualizations/SuperTokenVis";
import SuperTokenPureVis from "@site/src/components/Visualizations/SuperTokenPureVis";


Super Tokens extend the [ERC20 token standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) with additional functionalities like [Money Streaming](./money-streaming.mdx) or [Distributions](./distributions.mdx), formerly known as Super Agreements. There are two types of Super Tokens: wrapper and custom.

:::info
Super Tokens can perform all the functions of a traditional [ERC20 token](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/), plus additional value transfer methods enabled by Superfluid, such as money streaming.
:::

### Wrapper Super Tokens

Wrapper Super Tokens are existing tokens wrapped to gain Superfluid functionalities. Wrapping converts the underlying token into its Super Token version, while unwrapping reverses the process.

<div style={{ display: "flex", justifyContent: "center" }}>
  <SuperTokenVis />
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*By wrapping the original token you obtain a SUPER TOKEN*</p>
</div>

For more informations, about the wrapping process, please refer to our [Developers Section](/docs/category/deploy-a-super-token).

### Pure Super Tokens

Pure Super Tokens are natively Superfluid-enabled without an underlying token. They offer inherent ERC20 functionalities plus Superfluid's Super Agreement capabilities.

<div style={{ display: "flex", justifyContent: "center" }}>
  <SuperTokenPureVis />
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>*A Pure Super Token has inherent superpowers such as [Money Streaming](./money-streaming.mdx) and [Distributions](./distributions.mdx)*</p>
</div>

### Real-Time Balance

Super Tokens track an account's balance dynamically, factoring in both regular transfers and impacts from Money Streaming and Distributions.

- **Static Balance**: The standard ERC20 balance affected by lump-sum transfers.
- **Real-Time Balances**: The ongoing impact of each Super Agreement on an account's balance, which can be positive or negative.

The actual current balance is a sum of these components.

> **Current Balance Formula**: Current Balance = Real-Time Balances + Static Balance

#### Example Calculation

- Account A's Static Balance: 1,000 USDCx
- Account A's Stream Out: -100 USDCx
- Account A's Instant Distribution Receipts: +200 USDCx

> **Current Balance**: 1000 - 100 + 200 = **1100 USDCx**

:::info About Super Tokens `balanceOf()`
If you are familiar with the ERC20 standard, you are certainly familiar with `balanceOf()`. A Super Token `balanceOf()` function reflects this dynamic balance, unlike a regular ERC20's static approach.
:::

---

<a id="doc_8"></a>

## 📁 concepts/use-cases / Social & Community

*파일 경로: concepts/use-cases/social-and-community.mdx*

---
sidebar_position: 4
---


Superfluid Protocol introduces innovative methods for community engagement and social token incentives, fostering long-term loyalty and participation.

### Gradual Social Token Incentives

Rather than distributing social tokens in a single airdrop, Superfluid enables a gradual, by-the-second streaming of tokens to community members or creator audiences.

#### Concept

- **Long-Term Engagement**: This model rewards ongoing loyalty and engagement, as opposed to immediate lump-sum airdrops.
- **Example**: Consider the scenario where the longer an individual holds a community NFT, the more social tokens they accrue, discouraging immediate selling post-airdrop.

Explore this concept with the [Reverb project](https://ethglobal.com/showcase/reverb-x2kgs), a platform that streams social tokens based on music listening habits.

### Perpetual Conditional Rewards (PCR)

The PCR model within the Superfluid Protocol offers a scalable way to incentivize community actions based on specific Key Performance Indicators (KPIs).

#### Mechanism

- **Reward Distribution**: Rewards are streamed to participants based on progress towards a KPI metric.
- **Funding and Execution**: Funded through money streams and distributed using the Superfluid Instant Distribution Agreement, with KPI verification via UMA's KPI Options.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![Perpetual Conditional Rewards](/assets/image_(31).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Perpetual Conditional Rewards*</p>
</div>

#### Use Cases

- **Community Incentives**: Communities can incentivize members for activities like increasing Twitter followers or GitHub repo stars.
- **Scalable Incentives**: This system provides a method to reward members proportionally for contributing to communal goals.

For a deeper dive into the PCR concept, refer to this [Twitter thread by UMAprotocol](https://twitter.com/UMAprotocol/status/1517165913706930176?s=20&t=aWpKxDP7mqoQFGK9vcCygg).

Superfluid's approach to social tokens and community incentives represents a shift towards more dynamic and engagement-focused reward systems in the digital space.

---

<a id="doc_9"></a>

## 📁 concepts/use-cases / Token-Cost-Averaging

*파일 경로: concepts/use-cases/defi.mdx*

---
sidebar_position: 1
---


Token-Cost-Averaging* (TCA) is one possible application designed to leverage the power of Superfluid streams.
This application could allow the user to swap tokens in continuous real-time streams: stream in your Sell token and receive back the Buy token periodically.

### What is Token-Cost-Averaging (TCA)?
Token-Cost-Averaging (TCA) is an investment strategy where an investor divides up the total amount to be invested across periodic purchases of a target asset
(just like Dollar-Cost-Averaging but it's asset agnostic).
This strategy gives users the best results over time by swapping tokens in continuous real-time streams: stream in your Sell token and receive back the Buy token periodically.

### How does it work?
This application could be a new trading app powered by Superfluid.
It could be designed to provide a more efficient and accessible way to perform Token-Cost-Averaging (TCA) by leveraging the power of Superfluid's streaming technology.
Under the hood, the app would perform swaps time-continuously using a Time-Weighted Average Price (TWAP) oracle for liquidity source aggregation and a fair price over time.

### The Superfluid Advantage
Compared to existing TCA or DCA (Dollar-Cost-Averaging) dApps built on other protocols, Superfluid offers several advantages:

- **Efficiency and Accessibility:** Building on Money Streams makes TCA more efficient and accessible. By using Superfluid's streaming technology,
it allows for continuous and automated investment flows, reducing the need for manual intervention and making investment more seamless and user-friendly.
- **Reduced Volatility Impact:** The core idea of TCA is to mitigate the risks associated with volatile market conditions.
Superfluid enhances this approach by allowing for more frequent and smaller investments, thereby further reducing the potential impact of sudden market changes.
- **Innovation in DeFi:** By leveraging Superfluid's groundbreaking streaming technology, this TCA app stands at the forefront of innovation in decentralized finance, offering a unique approach to cryptocurrency investments.

---

<a id="doc_10"></a>

## 📁 faq / Frequently Asked Questions

*파일 경로: faq/faq.mdx*

### How can I deploy a Super Token?
- You can deploy a Wrapped Super Token using the [Super Token Factory contract](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-wrapped-super-token). A no-code interface is found on the same page of the docs.
- You can deploy a Pure Super Token using this [interface on the docs](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-pure-super-token).

### How do I know if I should use simple Money Streaming or Distribution Pools?
- Use Money Streaming if you want to stream money from one account to another.
- Use Distribution Pools if you want to distribute money from one account to multiple accounts.
- Use Distribution Pools if you want to distribute money from multiple accounts to multiple accounts.

### What is a Super App and when should I use it?
A Super App is a smart contract that interacts with the Superfluid Protocol and creates automated hooks reacting to Stream actions (Streams started, Streams updated, Streams deleted).
If your application needs to start or end an action on-chain following a stream state update, you can create a Super App to automate this process.
Learn more about Super Apps in the [Superfluid Protocol documentation](/docs/protocol/advanced-topics/super-apps).

### How can I deploy a Super App?
You can deploy a Super App using the [Super App Base Flow contract](/docs/protocol/advanced-topics/super-apps/deploy-a-super-app).

### How can I interact with the Superfluid Protocol on-chain?
The Superfluid Protocol is a token-centric protocol, meaning that all interactions are done through the `SuperTokenV1Library`.
To learn more about how to interact with the Superfluid Protocol on-chain, refer its [Technical Reference](/docs/technical-reference/SuperTokenV1Library.mdx).

### How can I interact with the Superfluid Protocol on the frontend?
The recommended way to interact with the Superfluid Protocol on the frontend is to use the Superfluid Contract Fowarders:
- For Money Streaming: Use the `CFAv1Forwarder` contract. To learn more about how to use it, refer to [CFAv1Forwarder](/docs/technical-reference/CFAv1Forwarder.mdx).
- For Distribution Pools: Use the `GDAv1Forwarder` contract. To learn more about how to use it, refer to [GDAv1Forwarder](/docs/technical-reference/GDAv1Forwarder.mdx).

### Where do I find the Superfluid Protocol addresses?
You can find the Superfluid Protocol addresses on the [Superfluid Explorer](https://Explorer.superfluid.finance/), under the tab "Protocol".

### Where do I find the Superfluid Subgraph playground and endpoints?
- You can find the Superfluid Subgraph playground on the [Superfluid Explorer](https://Explorer.superfluid.finance/), under the tab "Subgraph".
- You can find the Superfluid Subgraph endpoints on the [Superfluid Docs](/docs/technical-reference/subgraph).

### How can I get help with the Superfluid Protocol?
Reach out to us on the [Superfluid Discord](https://discord.gg/pPzPEDMVua).

---

<a id="doc_11"></a>

## 📁 governance / Governance Overview

*파일 경로: governance/governance.mdx*

---
sidebar_position: 1
---

import Card from '@site/src/components/Card';
import styles from '@site/src/components/Card/styles.module.css';
import { 
  UsersThree, 
  Gavel, 
  Coins, 
  ChartLineUp
} from '@phosphor-icons/react';


The Superfluid protocol is governed by its community through a decentralized autonomous organization (DAO). This section outlines the key components of Superfluid's governance system.

<div className={styles.governanceGrid}>
  <Card
    title="Organization"
    description="Learn about the Superfluid DAO structure, Foundation, Security Council, and governance bodies."
    link="https://forum.superfluid.org/t/superfluid-dao-governance-and-tokenomics/69#p-124-organization-2"
    icon={() => <UsersThree size={32} weight="bold" />}
  />
  <Card
    title="Voting Process"
    description="Understand how proposals are submitted, voted on, and implemented through the Superfluid governance system."
    link="https://forum.superfluid.org/t/superfluid-dao-governance-and-tokenomics/69#p-124-voting-3"
    icon={() => <Gavel size={32} weight="bold" />}
  />
  <Card
    title="SUP Token"
    description="Explore the Superfluid Token (SUP), its functionality, distribution, and role in protocol governance."
    link="https://forum.superfluid.org/t/superfluid-dao-governance-and-tokenomics/69#p-124-sup-token-4"
    icon={() => <Coins size={32} weight="bold" />}
  />
  <Card
    title="Streaming Programmatic Rewards"
    description="Discover how the DAO allocates tokens to users and developers to incentivize ecosystem growth."
    link="https://forum.superfluid.org/t/superfluid-dao-governance-and-tokenomics/69#p-124-streaming-programmatic-rewards-8"
    icon={() => <ChartLineUp size={32} weight="bold" />}
  />
</div>

:::info
For detailed information about specific aspects of governance, click on any of the cards above.
:::

---

<a id="doc_12"></a>

## 📁 protocol / Contract Addresses

*파일 경로: protocol/contract-addresses.mdx*

---
sidebar_position: 8
---

import ContractsTable from '@site/src/components/ContractsTable';


This section provides an overview of the Superfluid Protocol's main smart contracts and their respective addresses
on the supported chains. For a detailed list of all contract addresses, refer to the [Superfluid Explorer](https://Explorer.superfluid.finance/).

### Table of Contract Addresses

The Superfluid Protocol is composed of several smart contracts that interact with each other to facilitate real-time finance on the blockchain.
Below is a table of the main contracts and their respective addresses on the all chains.

<ContractsTable/>

For more information on the Superfluid Protocol's contract addresses, please refer to the [Superfluid Explorer](https://Explorer.superfluid.finance/).

### Protocol Architecture

To learn more about the Superfluid Protocol's architecture, refer to the [Architecture Section](/docs/technical-reference/architecture).

---

<a id="doc_13"></a>

## 📁 protocol / Quickstart

*파일 경로: protocol/quickstart.mdx*

---
sidebar_position: 1
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import FlowSenderVis from '@site/src/components/Visualizations/FlowSenderVis';
import MotomoComponent from '@site/src/components/MotomoComponent';



<MotomoComponent/>

Superfluid is a token-centric protocol revolving around a new token standard called Super Token. Super Tokens have special capabilities.
One of them allows to create second-by-second token transfers (called [Money Streaming](/docs/protocol/money-streaming/overview.mdx)).
In this guide, we'll walk through the process of setting up and deploying a basic vesting contract which deploys a Mock Super Token and creates a stream to a recipient.

This contract allows you to:
- Deploy a Mock Super Token
- Create, update or delete money streams

:::note Why this Quickstart?
This is just an example to get you started with Superfluid. You can use this as a base to build more complex applications.

You DO NOT need to follow this quickstart guide in order to create, update and delete streams. You can do this directly from the [Dashboard](https://app.superfluid.finance/) or by interacting with the [CFAv1Forwarder contract](https://docs.superfluid.finance/docs/technical-reference/CFAv1Forwarder).
:::

### Prerequisites

- The [Superfluid Simple Vesting Contract Repository](https://github.com/superfluid-finance/superfluid-boilerplate)
- A development environment *(Remix or Foundry)*
- A testnet wallet (in case you want to deploy the contract to a testnet) *(e.g., MetaMask)*


### Contract Overview: SuperfluidBoilerplate

In this guide we will describe the contract [`SuperfluidVesting.sol`](https://github.com/superfluid-finance/superfluid-quickstart/blob/master/src/SuperfluidVesting.sol):
- This contract is designed to interact with the Superfluid protocol, specifically to deploy a [Super Token](/docs/protocol/super-tokens/overview) and use [Money Streaming](/docs/protocol/money-streaming/overview.mdx).
- The contract enables the deployment of a Mock Super Token in the constructor.
- This contract enables the creation, modification, and deletion of continuous money streams to the a recipient.

<div style={{ display: 'flex', justifyContent: 'center' }}>
<FlowSenderVis/>
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Visualization showing the vesting contract streaming tokens to users*</p>
</div>


#### Contract and Key Functions

<div>
<details>
<summary>Click here to show `SuperfluidBoilerplate` contract</summary>
<p>

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {SuperTokenV1Library, ISuperToken, ISuperfluid} from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";
import {ISuperTokenFactory} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperTokenFactory.sol";
import {PureSuperTokenProxy, IPureSuperToken} from "./PureSuperToken.sol";

/// @title SuperfluidVesting
/// @notice A contract for managing token vesting using Superfluid streams
/// @dev Uses SuperTokenV1Library for handling Superfluid token operations
contract SuperfluidVesting {
    using SuperTokenV1Library for ISuperToken;

    /// @notice The Super Token that will be used for vesting
    ISuperToken public acceptedSuperToken;
    /// @notice The Superfluid protocol host contract
    ISuperfluid public host;
    /// @notice The address of the contract owner
    address public owner;

    /// @notice Restricts function access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /// @notice Initializes the vesting contract
    /// @param _host The address of the Superfluid host contract
    /// @dev Assigns the host and owner addresses
    /// Creates a new PureSuperToken and initializes it with mock data
    /// Mints the total supply of the token to the contract
    constructor(ISuperfluid _host) {
        host = _host;
        owner = msg.sender;
        acceptedSuperToken = IPureSuperToken(address(new PureSuperTokenProxy()));
        PureSuperTokenProxy(payable(address(acceptedSuperToken))).initialize(
            ISuperTokenFactory(host.getSuperTokenFactory()),
            "Mock Super Token",
            "mST",
            address(this),
            1000000000000000000000000
        );
    }

    /// @notice Creates or updates a vesting stream for a recipient
    /// @param recipient The address that will receive the stream
    /// @param flowRate The rate at which tokens will be streamed (tokens per second)
    /// @dev Flow rate must be positive and contract must have sufficient balance
    function setVesting(address recipient, int96 flowRate) public onlyOwner {
        require(flowRate > 0, "Flow rate must be greater than 0");
        require(acceptedSuperToken.balanceOf(address(this)) > 0, "Insufficient balance");
        acceptedSuperToken.flow(recipient, flowRate);
    }
}
```

</p>
</details>
</div>


The contract has two main methods:

- **constructor**: Creates a new contract and with it it deploys a Mock Super Token with 1,000,000 units initial supply minted to the contract.
- **setVesting**: Creates, updates or deletes a stream to the user with the specified flow rate, gated by the modifier `onlyOwner`.


### Environment Setup and Deployment

<Tabs>
  <TabItem value="remix" label="Remix IDE" default>

#### Using Remix IDE

1. **Create Files**: 
   - Create `SuperfluidVesting.sol` and paste the main contract from the [repository's `/src` folder](https://github.com/superfluid-finance/superfluid-quickstart/tree/master/src)
   - Create `PureSuperToken.sol` and paste the interface from the [repository's `/src` folder](https://github.com/superfluid-finance/superfluid-quickstart/tree/master/src)
2. **Compile**: Select compiler version 0.8.20 or higher
3. **Deploy**: 
   - Select "Injected Provider - MetaMask"
   - Choose your network (make sure Superfluid supports it - check [here](https://explorer.superfluid.finance/base-mainnet/protocol))
   - Enter the Superfluid host address in the constructor (get it from the [docs](/docs/protocol/contract-addresses) or from the [explorer](https://explorer.superfluid.finance/base-mainnet/protocol))
   - Click "Deploy"

  </TabItem>
  <TabItem value="foundry" label="Foundry">

#### Using Foundry

After cloning the [Superfluid Boilerplate Repository](https://github.com/superfluid-finance/superfluid-quickstart), you can test and deploy the contract with the following commands:

1. **Install Dependencies**:
```bash
forge install
```

2. **Test**:
```bash
forge test
```

3. **Deploy**:
```bash
forge create src/SuperfluidVesting.sol:SuperfluidVesting \
  --constructor-args SUPERFLUID_HOST_ADDRESS \
  --rpc-url YOUR_RPC_URL \
  --private-key YOUR_PRIVATE_KEY
```

  </TabItem>
</Tabs>

:::tip Where can I get the Superfluid host address?
Make sure to use the correct Superfluid host address for your network.
You can get the Superfluid host address from the [docs](/docs/protocol/contract-addresses) or from the [explorer](https://explorer.superfluid.finance/base-mainnet/protocol).
:::

### Using the Contract

After deployment, interact with your contract in 3 different ways:

1. **Create Vesting**:
   - Call `setFlowRate(flowRate)`
   - The `flowRate` is tokens per second (with 18 decimals)
   - Example:
     - For 1 token per month, use `flowRate ≈ 380414535736`
2. **Update Vesting**:
   - Call `setFlowRate(flowRate)`
   - The `flowRate` is tokens per second (with 18 decimals)
   - Example:
     - For 1 token per week, use `flowRate ≈ 1653439153439`
3. **Delete Vesting**:
   - Call `setFlowRate(0)`

:::tip How do I find the full list of methods for the SuperTokenV1Library?
You can find the full list of methods for the SuperTokenV1Library in the [SuperTokenV1Library Technical Reference](/docs/technical-reference/SuperTokenV1Library).
:::

### Testing Your Contract

As you can see in the repository, we have a test file that tests the contract. Here's a breakdown of the test file:

```solidity
// SPDX-License-Identifier: MIT OR Apache-2.0
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import {SuperfluidVesting} from "../src/SuperfluidVesting.sol";
import {SuperfluidFrameworkDeployer} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeployer.t.sol";
import {SuperTokenV1Library, ISuperToken, ISuperfluid} from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";
import { ERC1820RegistryCompiled } from "@superfluid-finance/ethereum-contracts/contracts/libs/ERC1820RegistryCompiled.sol";


contract SuperfluidVestingTest is Test {
    SuperfluidVesting private vestingContract;
    SuperfluidFrameworkDeployer.Framework private sf;
    ISuperToken private acceptedSuperToken;
    using SuperTokenV1Library for ISuperToken;

    function setUp() public {
        vm.etch(ERC1820RegistryCompiled.at, ERC1820RegistryCompiled.bin);
        SuperfluidFrameworkDeployer sfDeployer = new SuperfluidFrameworkDeployer();
        sfDeployer.deployTestFramework();
        sf = sfDeployer.getFramework();
    
        vestingContract = new SuperfluidVesting(sf.host);
        acceptedSuperToken = vestingContract.acceptedSuperToken();
    }

    function testVesting() public {
        vestingContract.setVesting(address(this), 100000000);
        uint256 flowRate = uint256(uint96(acceptedSuperToken.getFlowRate(address(vestingContract), address(this))));
        assertEq(flowRate, uint256(100000000));
    }

}
```

The test file does two main things:

1. **Setup (`setUp` function)**:
   - Deploys a local version of the Superfluid protocol for testing
   - Creates our `SuperfluidBoilerplate` contract
   - Deploys the Mock Super Token

2. **Vesting Test (`testVesting` function)**:
   - Creates a vesting stream with a flow rate of 100000000 wad/second
   - Verifies that the flow rate was set correctly

You can run these tests using the `forge test` command as shown in the setup instructions above.

### Next Steps

Now that you understand the basics, you can:

1. **Explore Super Tokens**:
   - [Super Tokens Overview](/docs/protocol/super-tokens/overview)
   - [Advanced Token Creation](docs/protocol/super-tokens/guides/deploy-super-token/deploy-custom-super-token)

2. **Build Smart Contracts**:
   - [Money Streaming Overview](/docs/protocol/money-streaming/overview)
   - [Distribution Pools Overview](docs/protocol/distributions/overview)
   - [How to use the SuperTokenV1Library](/docs/protocol/super-tokens/guides/using-library)

3. **Build your client application**:
   - [SDK Quickstart](/docs/sdk/quickstart)

---

<a id="doc_14"></a>

## 📁 protocol/advanced-topics/automations / Auto-Wrap

*파일 경로: protocol/advanced-topics/automations/auto-wrap.mdx*

---
sidebar_position: 1
---

import Link from '@docusaurus/Link';


### What's Auto-Wrap?

Auto-Wrap is an automated token wrapping system that automatically wraps ERC20 tokens to Super Tokens just in time to keep your streams running. When your Super Token balance reaches a certain lower threshold, Auto-Wrap steps in and wraps enough tokens into the needed Super Token on your behalf to ensure you never run out of balance, as that would make all streams stop.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://www.notion.so/superfluidhq/Setting-Up-Superfluid-Auto-Wrap-9a565d53bbee4bdc953cc2a656c43761"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for full a guide on how to set up an Auto-Wrap Automation
   </a>
</div>

### Why Auto-Wrap?

Most organizations don’t hold their assets as Super Tokens. DAOs are more likely to hold USDC than USDCx in their treasury to limit exposure to third party protocols. So when a DAO is paying contributors in streams of USDCx they need to ensure they periodically wrap additional USDC in USDCx to keep their streams running. This can be a tedious manual process because it requires you to:

1. Periodically check the Super Token balance to make sure it isn’t reaching zero.
2. If it is approaching zero, manually wrap additional USDC to USDCx to avoid running out of USDCx balance.

With Auto-Wrap, this manual process is fully automated. The system keeps monitoring a wallet balance of a specific token (i.e. USDC) and when it’s too low (normally less than 2 days worth of outgoing streaming) it automatically wraps a variable amount (normally 7 days worth of outgoing streaming) to keep streams running over time. All payroll admin needs to do is ensure they’re holding enough USDC in their wallet - the wrapping part is taken care of by Auto-Wrap.

### Example

1. Auto-Wrap identifies that the DAO’s DAIx balance is running low. In this example, it’s less than a two days away from running out of DAIx.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Auto-Wrap identifying low balance](/assets/image_(5)_(3)_(1).png)
</div>

2. Auto-Wrap automatically steps in and replenishes the DAIx balance back to seven days worth of outgoing stream so payment continues without interruption. No manual triggering required!

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Auto-Wrap replenishing balance](/assets/image_(8).png)
</div>

### Setting Up Auto-Wrap

To set up Auto-Wrap for your organization, follow the detailed guide available here:

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://www.notion.so/superfluidhq/Setting-Up-Superfluid-Auto-Wrap-9a565d53bbee4bdc953cc2a656c43761"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for full a guide on how to set up an Auto-Wrap Automation
   </a>
</div>

---

<a id="doc_15"></a>

## 📁 protocol/advanced-topics/automations / Stream Accounting API

*파일 경로: protocol/advanced-topics/automations/stream-accounting-api.mdx*

---
sidebar_position: 4
---
import Link from '@docusaurus/Link';


### Overview

- Streams move value every second, but accounting tools usually record value transfer on a non-real-time basis (typically monthly).
- The Stream Accounting API represents streams in a format consumable by traditional accounting tools.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://superfluidhq.notion.site/Using-the-Stream-Accounting-API-3d161745acfe4750acf43c546f84c724"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for full a guide on how to set up a Stream Accounting API Automation
   </a>
</div>

### Functionality

- The Stream Accounting API is RESTful and exposes an endpoint for fetching stream data across all Superfluid tokens and networks.
- It allows chopping up the amounts an address has been streaming into accounting periods of your choice (monthly, daily, even hourly).

#### Token Pricing

- Price information for each period is available if the token has Coingecko tracking.
- You can select price granularity to get average prices over a timeframe or instantaneous prices for each period.

#### Accommodating Flow Rate Updates

- The API accommodates changes in stream flow rates, segmenting data into separate periods for each flow rate.

#### Outgoing & Incoming

- Accounts for both outgoing and incoming streams, denoting incoming streams with positive values and outbound streams with negative values.

#### All Networks and All Tokens

- Supports all Superfluid-supported networks and tokens through the [Superfluid Subgraphs](https://docs.superfluid.finance/superfluid/developers/subgraph).

### Example

- Alice pays Bob in a stream of 0.1 ETHx per month.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Alice pays Bob](/assets/image_(17).png)
</div>

- Fetch accounting info for Alice's stream from June 1st to September 15th.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Accounting Info for June 1st to September 15th](/assets/image_(5)_(2)_(1).png)
</div>

- Stream Accounting API provides data for the requested months.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Stream Accounting API Data](/assets/image_(1)_(2).png)
</div>

- If Alice updates her stream to 0.2 ETHx/month on September 15th.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Stream Update to 0.2 ETHx](/assets/image_(4)_(5).png)
</div>

- Request accounting info from June 1st to December 1st.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Accounting Info from June 1st to December 1st](/assets/image_(3)_(3).png)
</div>

- API provides data for the updated period.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![API Data for Updated Period](/assets/image_(2)_(5).png)
</div>

### Setting up the Stream Accounting API

The Stream Accounting API is a robust tool for integrating real-time streaming data into your traditional accounting systems. Whether you're tracking incoming or outgoing streams, dealing with various tokens, or managing complex stream adjustments, the API provides the flexibility and precision required for accurate financial reporting.

You will find below a link to a full guide on how to set up a Stream Accounting API Automation.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://superfluidhq.notion.site/Using-the-Stream-Accounting-API-3d161745acfe4750acf43c546f84c724"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for full a guide on how to set up a Stream Accounting API Automation
   </a>
</div>

---

<a id="doc_16"></a>

## 📁 protocol/advanced-topics/automations / Stream Scheduler

*파일 경로: protocol/advanced-topics/automations/stream-scheduler.mdx*

---
sidebar_position: 2
---

import Link from '@docusaurus/Link';


### What’s the Stream Scheduler?

The Stream Scheduler is a Superfluid feature that enables you to:

1. Schedule the closing of an existing stream.
2. Schedule the start of a new stream.
3. Schedule both the start and end of a new stream.

This functionality is accessible directly from the Superfluid Dashboard after [approval for access](https://use.superfluid.finance/schedulestreams) and can also be implemented using underlying contracts and off-chain automations.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://superfluidhq.notion.site/Setting-Up-Stream-Scheduling-551888de690e402caee50e8d87cb6930"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for full a guide on how to set up a Stream Scheduler Automation
   </a>
</div>

### Why Schedule Streams?

Scheduling streams offers automation for streams with fixed start and/or end dates. This is particularly useful for applications like payroll, subscriptions, and token vesting. By default, Superfluid streams are perpetual, running until manually canceled or until the balance is depleted. The Stream Scheduler allows for automated stream management, eliminating the need for manual intervention.

### Example:

Consider the following scenario, visualized in these [Miro diagrams](https://miro.com/app/board/uXjVP--AM4I=/?share_link_id=524959909457):

1. **Stream Scheduling**:
   On January 1st, you grant operator permissions to the Stream Scheduler contract and schedule a stream with the following details:
   
   - **Flow Rate**: 100 DAIx/mo.
   - **To**: Alice’s account
   - **Start**: March 1st, 2023, at 12:00 am
   - **End**: March 20th, 2023, at 12:00 am
   
   
   <br/>
   <div style={{ display: 'flex', justifyContent: 'center' }}>
     ![Stream Scheduling Example](/assets/image_(1)_(4).png)
   </div>

2. **Stream Initiation**:
   On March 1st, the scheduled stream from you to Alice commences.

   <div style={{ display: 'flex', justifyContent: 'center' }}>
     ![Stream Initiation](/assets/image_(3)_(2).png)
   </div>

3. **Stream Cancellation**:
   On March 20th, the stream from you to Alice is automatically canceled.

   <div style={{ display: 'flex', justifyContent: 'center' }}>
     ![Stream Cancellation](/assets/image_(7).png)
   </div>


### Setting Up Stream Scheduling

The Stream Scheduler is a versatile tool that enhances the functionality of Superfluid streams by automating their creation and termination based on predefined schedules.
This feature simplifies the management of streaming payments, especially in use cases like subscription services, vesting schedules, and regular disbursements.

To get started with stream scheduling and unlock the full potential of automated streaming in Superfluid, follow the detailed guide provided in the link below.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://superfluidhq.notion.site/Setting-Up-Stream-Scheduling-551888de690e402caee50e8d87cb6930"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for full a guide on how to set up a Stream Scheduler Automation
   </a>
</div>

---

<a id="doc_17"></a>

## 📁 protocol/advanced-topics/automations / Vesting Scheduler

*파일 경로: protocol/advanced-topics/automations/vesting-scheduler.mdx*

---
sidebar_position: 3
---

import Link from '@docusaurus/Link';


### What’s the Vesting Scheduler?

The Vesting Scheduler is a sophisticated smart contract designed for setting up token vesting schedules. It's non-custodial and operates by moving tokens directly from your wallet or Safe to a specified recipient. The contract includes options for adding cliffs, after which it initiates a linear vesting process through a Superfluid stream, ensuring the recipient receives tokens directly in their wallet without any need for claiming.

While the integration of the Vesting Scheduler into the Superfluid Dashboard is forthcoming, it's already possible to interact directly with the contract alongside off-chain automations. Detailed instructions for setting up automated vesting can be found in the documentation.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://www.notion.so/superfluidhq/Setting-Up-Automated-Vesting-f3e11a257a2d4b0b89210def54a59278"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for a full guide on Setting Up Automated Vesting
   </a>
</div>

### Why Automate Vesting with Superfluid?

Automating vesting with Superfluid streamlines the process of setting up a linear vesting schedule, providing flexibility and security. With this system, you can:

- Implement linear vesting schedules with customizable cliffs.
- Specify both the cliff date/time and amount.
- Determine your total vesting amount and its time frame.
- Retain all tokens in your wallet or Safe until they're transferred to the recipient.

### Example:

1. **Initial Setup**: On January 1st, you aim to vest 400 AMZNx to Alice from February 1st to June 1st. The vesting schedule includes a cliff of 100 AMZNx on March 1st.

   <div style={{ display: 'flex', justifyContent: 'center' }}>
   ![Initial Vesting Setup](/assets/image_(4)_(3).png)
   </div>

2. **Cliff Execution**: On March 1st, the cliff amount of 100 AMZNx is transferred to Alice, and the linear vesting stream begins. No action is needed on February 1st due to the cliff.

   <div style={{ display: 'flex', justifyContent: 'center' }}>
   ![Cliff Execution](/assets/image_(2)_(1).png)
   </div>

3. **Completion of Vesting**: By June 1st, the vesting process is complete, and the stream to Alice is cancelled.

   <div style={{ display: 'flex', justifyContent: 'center' }}>
   ![Completion of Vesting](/assets/image_(12)_(2).png)
   </div>

### Setting Up Vesting Scheduling

The scheduler's integration with Superfluid streams adds an extra layer of convenience, eliminating the need for manual intervention once the schedule is set. This not only saves time but also ensures accuracy and reliability in the vesting process.

If you're interested in setting up automated vesting, you can find detailed instructions in the link below.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://www.notion.so/superfluidhq/Setting-Up-Automated-Vesting-f3e11a257a2d4b0b89210def54a59278"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      Click here for a full guide on Setting Up Automated Vesting
   </a>
</div>

---

<a id="doc_18"></a>

## 📁 protocol/advanced-topics/solvency / Liquidations & TOGA

*파일 경로: protocol/advanced-topics/solvency/liquidations-and-toga.mdx*

---
sidebar_position: 1
---

import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";


### Liquidation and Solvency

When opening a stream, the protocol will take a small `buffer` or `deposit`. By leaving their streams open for too long, stream creators stand to lose this `buffer`. This mechanism creates the main incentive for users to close their Superfluid streams before running out of tokens. It is a user's own responsibility to close their stream.

`superApps` can also draw an `owedDeposit`, allowing them to open a stream of the same size, without needing an initial balance.

Here's the general flow of solvency states for Super Tokens in a Constant Flow Agreement (Money Streaming):

##### 1. Solvent

Everyone is in good standing. The sender's balance is greater than 0. The stream flows to the receiver as expected, and there are enough tokens to back the stream.

##### 2. Critical

The sender's balance is now zero, and the permissions on the stream now allow anyone to close it. Until the stream is actually closed, funds are paid to the receiver's wallet using the sender's initial `buffer`.

The critical period is subdivided into 2 sub-periods:\
a) _**Patrician Period**_: starts when the stream becomes critical (duration defined as governance parameter)\
b) _**Plebs Period**_: spans the remaining timeframe until the stream becomes insolvent

When the stream is closed, any remaining `buffer` is taken and assigned/distributed either to the _**PIC**_ or a _**Pleb**_.\
If the stream is closed during the Plebs Period, we call the account closing the stream a Pleb.

##### 3. Insolvent

If the stream isn't closed, and the sender's deposit is completely consumed, then the insolvent period begins. The stream will continue to the receiver, however since these tokens don't actually exist in the sender's wallet, we must keep track of this `deficit` so that the Super Token itself can remain solvent within the Superfluid Protocol.\
We also call this open ended timeframe the _**Pirate Period**_.

When the stream is eventually closed, the `deficit` is taken from the PICs stake as a slashing fee. This slashing fee is then burned, to offset the tokens created by the insolvent stream. Additionally, a reward equal in amount to the `buffer` amount before its consumption is issued to the account closing the stream, whom we call a _**Pirate.**_. This reward is also detracted from the PICs stake.

<div style={{ display: "flex", justifyContent: "center" }}>
  ![Buffer and
  balance](https://lh6.googleusercontent.com/X7ShIBo-weuUDIVwxj4Klj0VNy0PNP7ajC9zNC9WxiCOMkPDfhjpK4YpNJQ8i1Oor2OjDYzxr1493JxtCU4ycHwU7lZ9rRkiwm4mRQEA9xTDybxd4WXht3JW95U6qEqEvSHA60zi)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>
    *Visualization showing the tota user balance as well as the outgoing stream
    part of the buffer*
  </p>
</div>

#### Patricians, Plebs and Pirates (3Ps)

Each token has an account called a _**PIC (Patrician in Charge)**_.

Every time a stream is closed while Critical during the Patrician Period, the remaining amount of the `buffer` balance of the closed stream is taken and added to the PICs stake as a reward.

Every time a stream is closed while Critical during the Plebs Period, the remaining buffer is rewarded to the Pleb.

Every time a stream is closed while Insolvent, the PIC is slashed, and the Pirate is rewarded with the full buffer amount.

The monopoly on rewards during the Patrician Period gives PICs an incentive to make sure streams are closed during that timeframe.\
They can set up one or multiple redundant instances of the [superfluid-sentinel](https://github.com/superfluid-finance/superfluid-sentinel) (and/or other mechanisms for closing streams) to ensure this. Note that the PIC account is not needed (not in a _hot wallet_) for this operations as the rewards incurred during the patrician period will be added to the PIC stake regardless of transaction sender.

Plebs act as a fallback in case PICs fail to do their job despite of the incentives.\
The earlier in the Pleb Period a Pleb closes the stream, the more buffer there's left as a reward.

Unlike the PIC, individual Plebs and Pirates don't have a monopoly. Whoever manages to get a stream closing transaction included first during the Plebs / Pirate Period, gets the reward.

Patrician, Pleb and Pirate are roles which map to accounts in specific circumstances.\
The same account could have any of those roles in the context of various stream closing transactions, defined by the timing of that transaction and the state of the TOGA contract (list of PICs) at the time of transaction execution. The reference sentinel implementation provides configuration options influencing that behaviour and timing of transactions.

Note that thanks to this flexible roles model, PICs have an incentive to close streams even after missing the Patrician Period:

1. they can still get rewards, essentially acting as a Pleb or Pirate in the context of that transaction
2. due to the slashing of the `deficit` from their stake, their incentive to close insolvent streams grows linearly over time

![Toga payoff table](</assets/image_(72).png>)

#### TOGA - Transparent OnGoing Auction

Since the role of a PIC comes with a monopoly on rewards incurred during the Patrician Period, a fair mechanism for assigning this role is needed. Such a mechanism is provided by the TOGA.

To become a PIC for a token, aspiring Patricians must post a `stake` to the TOGA contract, in the token they are trying to become a PIC for. If the new `stake` is higher than the existing `stake`, the new Patrician becomes the PIC, and the previous Patrician gets their current `stake` back.

PICs can't remove their `stake` at will through a single transaction, but rather, they have to specify an `exitRate`, which defines the flowrate of a Stream to their account. The `exitRate` is also not completely arbitrary, it is limited such that the `stake` will remain above zero for at least a week.

All liquidation rewards are added to the `stake`, thus - depending on the exitRate set by the PIC and the number of size of streams becoming critical - the stake of a PIC could shrink, grow or stay the same over time. (The maximum allowed `exitRate` is calculated based on the worst case of no rewards being added during that timeframe.)

In order to become the PIC, you can either use the Dapp at https://toga.superfluid.finance/ or use `ERC777.send()` to post the desired stake to the TOGA contract - optionally with an `exitRate` set in the `data` parameter if you don't like the default `exitRate`. The TOGA contract implements an ERC777 callback for the auction mechanism.

:::warning CAUTION
Do NOT use `ERC20.transfer()` for TOGA bids, because those may not trigger the needed callback in the future.
:::

#### Current Parameters

<Tabs
    defaultValue="polygon"
    values={[
        { label: 'Polygon', value: 'polygon' },
        { label: 'Ethereum Mainnet', value: 'ethereum-mainnet' },
        { label: 'Gnosis Chain', value: 'gnosis-chain' },
        { label: 'Optimism', value: 'optimism' },
        { label: 'Arbitrum', value: 'arbitrum' },
        { label: 'Goerli', value: 'goerli' },
    ]}
>
    <TabItem value="polygon">
        **Deposit**

        4 hour `deposit`

        4 hour maximum `owedDeposit`

        30 minutes `patrician period`

        **TOGA**

        1 week minimum `exitPeriod`

        4 week default `exitPeriod`
    </TabItem>
    <TabItem value="ethereum-mainnet">
        **Minimum Deposit**

        Ethereum L1 is a different environment from other networks where Superfluid has been deployed.
        This is due to the fact that performing any operation on L1 is much more expensive
        in terms of gas cost than it is on other networks.

        To cover additional costs incurred by sentinels, tokens on L1 have been deployed with minimum deposit values.
        This means that the buffer on each of these tokens will not always be calculated
        as 4 hours worth of the stream as it is on lower cost networks.

        - ETHx: 0.042 ETHx
        - USDCx & DAIx: 69 tokens

        **Deposit**

        4 hour `deposit` (note that this value only applies if the deposit is > the min deposit)

        4 hour maximum `owedDeposit`

        30 minutes `patrician period`

        **TOGA**

        1 week minimum `exitPeriod`

        4 week default `exitPeriod`
    </TabItem>
    <TabItem value="gnosis-chain">
        **Deposit**

        4 hour `deposit`

        4 hour maximum `owedDeposit`

        30 minutes `patrician period`

        **TOGA**

        1 week minimum `exitPeriod`

        4 week default `exitPeriod`
    </TabItem>
    <TabItem value="optimism">
        **Deposit**

        4 hour `deposit`

        4 hour maximum `owedDeposit`

        30 minutes `patrician period`

        **TOGA**

        1 week minimum `exitPeriod`

        4 week default `exitPeriod`
    </TabItem>
    <TabItem value="arbitrum">
        **Deposit**

        4 hour `deposit`

        4 hour maximum `owedDeposit`

        30 minutes `patrician period`

        **TOGA**

        1 week minimum `exitPeriod`

        4 week default `exitPeriod`
    </TabItem>
    <TabItem value="goerli">
        **Deposit**

        1 hour `deposit`

        1 hour maximum `owedDeposit`

        12 minutes `patrician period`

        **TOGA**

        1 week minimum `exitPeriod`

        4 week default `exitPeriod`
    </TabItem>

</Tabs>

---

:::info
Note that this parameter definitions in terms of time units refer to simplified idealized scenarios and are basically lower bounds.
:::

\
The deposit related timeframes directly apply for streams where the sender account has no incoming streams and where the net flowrate is thus equal to the outgoing flowrate. If however the sender account has incoming streams, this timeframes are stretched proportionally. If for example the aggregate incoming flowrate is half of the aggregate outgoing flowrate, the time for the buffer to be consumed (critial period) doubles, as do the patrician period and the plebs period. If the aggregate incoming flowrate equals the aggregate outgoing flowrate (net flowrate = zero), those periods become potentially infinite (as long as the net flowrate doesn't change), because in that case the buffer wouldn't be consumed further, but not restored either, leaving outgoing streams critical in perpetuity.

\
For the TOGA `exitPeriod`, something similar applies - it's the lower bound for how long it would take a PIC to stream out the stake with a given `exitRate`, assuming nothing is added to the stake during that time. In practice, accrued liquidation rewards may be added to the stake during that time, leading to a proportional extension of the exitPeriod. In theory such added rewards could even completely offset the exitRate, leading to a net growing stake. In that case the PIC could periodically increase the exitRate (a larger stake allows for a larger exitRate) and would eventually be able to set an exitRate which leads to a shrinking stake.

---

<a id="doc_19"></a>

## 📁 protocol/advanced-topics/solvency / Running a Sentinel

*파일 경로: protocol/advanced-topics/solvency/running-a-sentinnel.mdx*

---
sidebar_position: 2
---


In our section on [Liquidations & TOGA](./liquidations-and-toga.mdx), we described how the Superfluid protocol handles solvency & liquidations. Sentinels play a vital role in this process. This page provides links to various resources that will aid you on your journey to help secure the protocol 🛡⚔️

#### Who Should Run a Sentinel?

1. Crypto enthusiasts who want to help secure a new, innovative primitive for web3 😁
2. Teams that have a service running on Superfluid. Perhaps you’ve launched your own dapp or your own Super Token, and you want to be 100% certain that your users are in good standing.
3. Professional operators who want to run profitable enterprises. If you have DevOps skills and/or you’re able to acquire capital to become the PIC for several tokens, participating in this process could be a good opportunity!

### Getting Started

#### Running a Sentinel - Step By Step Guide

<div style={{ textAlign: 'center', margin: '20px' }}>
<iframe width="700" height="400" src="https://www.youtube.com/embed/COo9IoVU9A0?si=OZFO1MOSNHNNr8sG&amp;start=1147" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

#### Sentinel Repository

If you want to start running a Sentinel today, you can clone [this repo](https://github.com/superfluid-finance/superfluid-sentinel) and customize your own `.env` file before starting the software. At minimum, you're going to need a reliable RPC URL, and a private key with native tokens to pay for gas when performing liquidations. Detailed instructions for running your Sentinel can be found in the repository's README and in the above video.

<div style={{ textAlign: 'center', margin: '20px' }}>
<a href="https://github.com/superfluid-finance/superfluid-sentinel" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/GitHub-View%20Repo-black?style=for-the-badge&logo=github" alt="GitHub" />
</a>
</div>

#### Becoming the PIC

You can become the PIC by connecting your wallet at the [TOGA dashboard.](https://toga.superfluid.finance/) There, you'll also see information on the current PIC stake amount, stream data by token, and a real time list of all liquidations. TOGA contract addresses are also available in our [Explorer](https://Explorer.superfluid.finance/) for each network.


<div style={{ textAlign: 'center', margin: '20px' }}>
  <a href="https://toga.superfluid.finance" target="_blank" rel="noopener noreferrer">
    <button class="button-50" role="button">The TOGA Dashboard</button>
  </a>
</div>

#### Additional Resources

Running sentinels does require some active management.&#x20;

We recommend you to join our discord server, and specifically the sentinels channel to keep in touch with any news and updates!

<div style={{ textAlign: 'center', margin: '20px' }}>
[![Join our Discord](https://img.shields.io/badge/Join%20our%20Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](http://discord.superfluid.finance)
</div>

### Glossary of Terms:

**Buffer**: The amount of tokens that an account must temporarily lock up when a stream is started.

**Liquidation**: Occurs when a stream is closed by a sentinel once an account's token balance hits zero while still streaming funds

**Sentinel**: A node that watches the Superfluid network & closes streams when they become critical or insolvent. Anyone can become a Sentinel by running a node

**PIC**: The Patrician in Charge who receives rewards each time a stream is closed in the priority period when an account goes critical

**TOGA**: the Transparent Ongoing Auction which allows anyone to become the Patrician in Charge (PIC) if they put up a higher staked amount than the previous PIC

**Stake**: The amount of funds locked in the TOGA contract by the Patrician in Charge (PIC)

---

<a id="doc_20"></a>

## 📁 protocol/advanced-topics/solvency / Solvency Dashboard

*파일 경로: protocol/advanced-topics/solvency/solvency-dashboard.mdx*

---
sidebar_position: 3
---
import Link from '@docusaurus/Link';


Click on the link below to find the solvency dashboard for the Superfluid protocol.

<div style={{ textAlign: 'center', margin: '20px' }}>
   <a 
      href="https://superfluid.metabaseapp.com/public/dashboard/a074474a-3c03-4368-84f9-a87761f5d902"
      className="button-link"
      style={{
         backgroundColor: 'green',
         color: 'white',
         fontSize: '16px',
         padding: '10px 20px',
         textDecoration: 'none',
         borderRadius: '4px',
         display: 'inline-block'
      }}
   >
      The Solvency Dashboard
   </a>
</div>

:::note
"Slot" refers to the solvency period during which the liquidation was executed.
> 
> Slot 1: Patrician Period
>
> Slot 2: Pleb Period
>
> Slot 3: Pirate Period
> 
See this [**explainer**](./liquidations-and-toga.mdx#patricians-plebs-and-pirates-3ps) for further details.
:::

---

<a id="doc_21"></a>

## 📁 protocol/advanced-topics/super-apps / Callbacks

*파일 경로: protocol/advanced-topics/super-apps/callbacks.mdx*

---
sidebar_position: 3
---



Super App callbacks play a pivotal role in how Super Apps interact with the Superfluid Protocol. These callbacks are invoked in response to specific events related to Super Agreements.

### Callback Invocation Conditions

Depending on the Super Agreement involved, the callbacks are triggered under different scenarios. The following table outlines these conditions:

<table><thead><tr><th width="150">Agreement</th><th width="273.3632148377125">Callback</th><th>Condition</th></tr></thead><tbody><tr><td>CFAv1</td><td>beforeAgreementCreated, afterAgreementCreated</td><td>A stream to a Super App is created.</td></tr><tr><td>CFAv1</td><td>beforeAgreementUpdated, afterAgreementUpdated</td><td>A stream to a Super App is updated.</td></tr><tr><td>CFAv1</td><td>beforeAgreementTerminated, afterAgreementTerminated</td><td>A stream to a Super App is deleted.</td></tr><tr><td>IDAv1</td><td>beforeAgreementCreated, afterAgreementCreated</td><td>A subscription (with zero units) to an index published by a Super App is approved.</td></tr><tr><td>IDAv1</td><td>beforeAgreementUpdated, afterAgreementUpdated</td><td>A subscription (with units) to an index published by a Super App is approved.</td></tr><tr><td>IDAv1</td><td>beforeAgreementTerminated, afterAgreementTerminated</td><td>A subscription to an index published by a Super App is revoked.</td></tr><tr><td>IDAv1</td><td>beforeAgreementUpdated, afterAgreementUpdated</td><td>A subscription to an index published by a Super App is claimed</td></tr><tr><td>IDAv1</td><td>beforeAgreementCreated, afterAgreementCreated</td><td>Units of an index are issued to a Super App if the units were previously zero.</td></tr><tr><td>IDAv1</td><td>beforeAgreementUpdated, afterAgreementUpdated</td><td>Units of an index are issued to a Super App if the units were previously non-zero.</td></tr><tr><td>IDAv1</td><td>beforeAgreementTerminated, afterAgreementTerminated</td><td>Units of an index issued to a Super App are deleted.</td></tr></tbody></table>

### Callback Origin

The Superfluid protocol itself triggers these callbacks on-chain in response to various actions performed within the Constant Flow Agreement contract. The protocol checks if a Super App is involved in a transaction and, if so, executes the relevant callbacks.

#### Anatomy of Super App Callbacks

Below are examples of Super App callbacks and their structure:

```solidity
function beforeAgreementCreated(
    ISuperToken /*superToken*/,
    address /*agreementClass*/,
    bytes32 /*agreementId*/,
    bytes calldata /*agreementData*/,
    bytes calldata /*ctx*/
) external view virtual override returns (bytes memory /*cbdata*/) {
    revert("Unsupported callback - Before Agreement Created");
}
```

```solidity
function afterAgreementCreated(
    ISuperToken /*superToken*/,
    address /*agreementClass*/,
    bytes32 /*agreementId*/,
    bytes calldata /*agreementData*/,
    bytes calldata /*cbdata*/,
    bytes calldata /*ctx*/
) external virtual override returns (bytes memory /*newCtx*/) {
    revert("Unsupported callback - After Agreement Created");
}
```

##### Callback Execution

* `beforeAgreement` callbacks are executed before the corresponding agreement contract action. They are `view` functions and can return data to be used in `afterAgreement` callbacks.
* `afterAgreement` callbacks are executed after the agreement contract action. They can implement logic based on the outcome of the agreement action and the data returned from `beforeAgreement` callbacks.

##### Callback Parameters

* **`ISuperToken`**: The Super Token used in the transaction.
* **`address`**: Address of the Constant Flow Agreement contract.
* **`agreementId`**: A unique identifier for the agreement.
* **`agreementData`**: Encoded data of the agreement details.
* **`cbdata`**: Data returned from `beforeAgreement` callbacks (applicable to `afterAgreement` callbacks).
* **`ctx`**: Context of the transaction, essential for understanding the background of the callback invocation.

#### Utilizing Callbacks

Understanding and effectively using these callbacks is crucial for Super App developers. Each callback serves a specific purpose and offers the flexibility to execute custom logic in response to changes in Super Agreements.

### CallAgreement vs CallAgreementWithContext

If you're making a call to a Superfluid agreement inside of a Super App callback, you should remember that you need to "receive a context, and return a context" by using the `callAgreementWithContext` function. If you're not making this call inside of a Super App callback, you should use `callAgreement`.


:::note
Note that this is a highly technical section for those looking to understand lower level features of the protocol. If you're looking to create, update, and delete streams or work with the instant distribution agreement in your super app callbacks, you can refer to the [SuperTokenV1Library](https://github.com/superfluid-finance/super-examples/blob/main/projects/tradeable-cashflow/contracts/RedirectAll.sol#L223) to perform these operations in a single line of code.
:::

#### In Depth

When calling the host contract to trigger actions related to the constant flow agreement (CFA) or instant distribution agreement (IDA), you may use either `callAgreement` or `callAgreementWithContext`. Both of these functions allow you to pass in an encoded call to the agreement you'd like to interact with, as well as an optional `userData` value. The `callAgreementWithContext` function will perform the same actions as the `callAgreement` function, but it also enables you to pass in a new context value (abbreviated `ctx` ) to your function call.

Keep in mind that `callAgreementWithContext` is designed for use within Super Apps - if this function is run outside of a Super App, then `callAgreementWithContext` will fail due to this statement:

``` solidity
require(
    context.appAddress == msg.sender,  
    "SF: callAgreementWithContext from wrong address"
);
```

`callAgreementWithContext` is primarily meant for use within Super App callbacks. Each Super App callback will be passed a context value (`ctx`) from the host contract (as the Superfluid host contract is the _caller_ of each callback). This `ctx` value is what needs to be passed to any call you want to make to the Superfluid host contract _inside_ of your callback (this goes for all operations which create, update, and delete flows in these callbacks). As a reminder, the logic within the 'host' contract can be found in `Superfluid.sol`.

The process looks like this:

<div>
<details>
<summary>Click here to show the code</summary>
<p>

```solidity
//a function which we'll use to create a flow within a callback
function _createFlowInCallback(
        bytes calldata ctx,
        ISuperfluid _host, 
        IConstantFlowAgreementV1 _cfa,    
        ISuperfluidToken _acceptedToken,
        address _receiver, 
        int96 _flowRate	
    )
	private
	returns (bytes memory newCtx)
    {
        newCtx = ctx;

        (newCtx,) = _host.callAgreementwithContext(
	    _cfa,
            abi.encodeWithSelector(
            _cfa.deleteFlow.selector,
            _acceptedToken,
            address(this),
	    _receiver,
            new bytes(0) // placeholder
          ),
          "0x", //placeholder userdata value
          newCtx //passing in the context from the super app callback
       );	
}

function afterAgreementCreated(
    ISuperToken _superToken,
    address _agreementClass,
    bytes32, // _agreementId,
    bytes calldata /*_agreementData*/,
    bytes calldata ,// _cbdata,
    bytes calldata _ctx
)
    external override
    onlyExpected(_superToken, _agreementClass)
    onlyHost
    returns (bytes memory newCtx)
{
//passing in the ctx which is sent to the callback here
   return _createFlowInCallback(_ctx, _host, _cfa, _acceptedToken, _receiver, _flowrate); 
}
```
</p>
</details>
</div>


You can also do this in a much easier way by using our new CFA Library, which abstracts away the need to use `host.callAgreement` or `host.callAgreementWithContext` directly.

<div>
<details>
<summary>Click here to show the code</summary>
<p>
```solidity
using CFALibraryV1 for CFALibraryV1.InitData;

    //initialize cfaV1 variable
    CFALibraryV1.InitData public cfaV1; 

    constructor(
        ISuperfluid host
    ) {

    //initialize InitData struct, and set equal to cfaV1
    cfaV1 = CFALibraryV1.InitData(
       host,
       IConstantFlowAgreementV1(
	  address(host.getAgreementClass(
           keccak256("org.superfluid-finance.agreements.ConstantFlowAgreement.v1")
	   ))
        )
     );
   }

function afterAgreementCreated(
    ISuperToken _superToken,
    address _agreementClass,
    bytes32, // _agreementId,
    bytes calldata /*_agreementData*/,
    bytes calldata ,// _cbdata,
    bytes calldata _ctx
)
    external override
    onlyExpected(_superToken, _agreementClass)
    onlyHost
    returns (bytes memory newCtx)
{
//passing in the ctx which is sent to the callback here
//createFlowWithCtx makes use of callAgreementWithContext
   return cfaV1.createFlowWithCtx(_ctx, receiver, token, flowRate);
}
```
</p>
</details>
</div>

You may have another scenario in which you want to make additional calls to the host contract after you first run `callAgreementWithContext`. If you do this, you can save the value returned by the first `callAgreementWithContext` function to a new variable, then pass this value to your next call to `callAgreementWithContext` . The takeaway here is that you need to pass the most recent iteration of `ctx` when creating, updating, or deleting flows inside Super App callbacks. You can see this done here with the CFA Library:

<div>
<details>
<summary>Click here to show the code</summary>
<p>
```solidity
using CFALibraryV1 for CFALibraryV1.InitData;

    //initialize cfaV1 variable
    CFALibraryV1.InitData public cfaV1; 

    constructor(
        ISuperfluid host
    ) {

    //initialize InitData struct, and set equal to cfaV1
    cfaV1 = CFALibraryV1.InitData(
       host,
       IConstantFlowAgreementV1(
	  address(host.getAgreementClass(
           keccak256("org.superfluid-finance.agreements.ConstantFlowAgreement.v1")
	    ))
        )
     );
   }

function afterAgreementCreated(
    ISuperToken _superToken,
    address _agreementClass,
    bytes32, // _agreementId,
    bytes calldata /*_agreementData*/,
    bytes calldata ,// _cbdata,
    bytes calldata _ctx
)
    external override
    onlyExpected(_superToken, _agreementClass)
    onlyHost
    returns (bytes memory newCtx)
{
   newCtx = cfaV1.createFlowWithCtx(_ctx, receiver, token, flowRate); //passing in the ctx which is sent to the callback here
   newCtx = cfaV1.createFlowWithCtx(newCtx, receiver, token, flowRate); //passing in the ctx which is returned from the first call here
			 
}
```
</p>
</details>
</div>

One final item to note is to not manually change the value of `ctx` when it's used within a Super App. `Ctx` is formatted in a very specific way within a struct that is compiled to bytecode by the protocol, and it's not meant to be manipulated directly. If you wish to pass in userData to your function call, this can be done by simply adding the `userData` value in as a parameter:

<div>
<details>
<summary>Click here to show the code</summary>
<p>
```solidity
//using the CFA Library:
function afterAgreementCreated(
    ISuperToken _superToken,
    address _agreementClass,
    bytes32, // _agreementId,
    bytes calldata /*_agreementData*/,
    bytes calldata ,// _cbdata,
    bytes calldata _ctx
)
    external override
    onlyExpected(_superToken, _agreementClass)
    onlyHost
    returns (bytes memory newCtx)
{
   //passing in the ctx which is sent to the callback here
   //createFlowWithCtx makes use of callAgreementWithContext
   return cfaV1.createFlowWithCtx(_ctx, receiver, token, flowRate, userData);
}

//using a low level call
function afterAgreementCreated(
    ISuperToken _superToken,
    address _agreementClass,
    bytes32, // _agreementId,
    bytes calldata /*_agreementData*/,
    bytes calldata ,// _cbdata,
    bytes calldata _ctx
)
    external override
    onlyExpected(_superToken, _agreementClass)
    onlyHost
    returns (bytes memory newCtx)
  {
	newCtx = _ctx;
	 (newCtx,) = _host.callAgreementwithContext(
	      _cfa,
	      abi.encodeWithSelector(
	      _cfa.deleteFlow.selector,
	      _acceptedToken,
	      address(this),
	      _receiver,
        new bytes(0) // placeholder
      ),
      userData, //userData goes here
      newCtx //passing in the context from the super app callback
   );	
 }

```
</p>
</details>
</div>

If you read through the Superfluid codebase, you'll see that nearly every state changing operation will return a context value. This `ctx` value helps to provide additional internal accounting for the protocol to enhance security, and it allows you to decode it and make use of values like userData inside Super Apps. When making calls within your Super Apps, keep in mind that you need to pass in updated context values if you want to make use of the callbacks properly. Remember: if you need to run callAgreement within a Super App callback, you'll need to use `callAgreementWithContext` and pass in `ctx`.

---

<a id="doc_22"></a>

## 📁 protocol/advanced-topics/super-apps / Quickstart

*파일 경로: protocol/advanced-topics/super-apps/deploy-a-super-app.mdx*

---
sidebar_position: 1
---
import Admonition from '@theme/Admonition';
import CodeBlock from '@theme/CodeBlock';


### Inroduction

Super Apps are smart contracts registered with the Superfluid Protocol, allowing them to **react to actions of the Superfluid protocol** (like flow creations, flow updates and flow deletions).

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![The Tradeable Cashflow NFT](/assets/image_(29)_(1).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Super App Illustration*</p>
</div>

This guide provides a simple example of how to deploy a Super App using the [CFASuperAppBase](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/apps/CFASuperAppBase.sol).

:::tip About this Guide
This guide provides a basic example of deploying a Super App using the CFASuperAppBase contract. For more advanced Super App development, refer to the [Super Apps in Depth](/docs/protocol/advanced-topics/super-apps/understand-super-apps).
:::

:::warning Dont overcomplicate it !
For most use cases, the CFASuperAppBase is sufficient. It simplifies the callback process and reduces redundancy.
:::

### CFASuperAppBase - Simplifying Super App Development

#### What is [CFASuperAppBase](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/apps/CFASuperAppBase.sol)?

[CFASuperAppBase](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/apps/CFASuperAppBase.sol) is an inheritable base contract designed to streamline the development of Super Apps.
It abstracts the complexities involved in writing callbacks and reduces redundancy.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![SuperAppBaseFlow Illustration](/assets/image_(30)_(2).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*CFASuperAppBase Illustration*</p>
</div>

:::info Example
onFlowCreated is a more intuitive function than afterAgreementCreated.
:::

#### Key Features of CFASuperAppBase

- **Intuitive Callback Functions**: CFASuperAppBase consolidates callback development into three functions (`onFlowCreated`, `onFlowUpdated`, `onFlowDeleted`) with user-friendly parameters.
- **Ease of Use**: Simplifies the callback process compared to the original SuperAppBase, making it more accessible for developers.

##### Importing and Using CFASuperAppBase

```solidity
// Example Code
import { CFASuperAppBase } from "@superfluid-finance/ethereum-contracts/contracts/apps/CFASuperAppBase.sol";

contract SomeSuperAppContract is CFASuperAppBase {
    // Your contract implementation
}
```

##### Constructor Arguments

```solidity
constructor(
    ISuperfluid host_,
    bool activateOnCreated,
    bool activateOnUpdated,
    bool activateOnDeleted
)
    // Constructor implementation
```

* **`host_`**: Superfluid Host address for your target network.
* **Activation Flags**: Indicate which callbacks (`onFlowCreated`, `onFlowUpdated`, `onFlowDeleted`) your Super App will use.

#### Token Acceptance

Override the `isAcceptedSuperToken` function to specify which Super Tokens can trigger the Super App's callbacks.

```solidity
function isAcceptedSuperToken(ISuperToken /*superToken*/) public view virtual returns (bool) {
    return true; // Default implementation
}
```

#### Callback Functions

##### onFlowCreated

Override for logic when a new flow to the Super App is created.

```solidity
function onFlowCreated(
    ISuperToken superToken,
    address sender,
    bytes calldata ctx
) internal virtual returns (bytes memory /*newCtx*/) {
    // Your logic here
}
```

##### onFlowUpdated

Override for logic when an existing flow to the Super App is updated.

```solidity
function onFlowUpdated(
    ISuperToken superToken,
    address sender,
    int96 previousFlowRate,
    uint256 lastUpdated,
    bytes calldata ctx
) internal virtual returns (bytes memory /*newCtx*/) {
    // Your logic here
}
```

##### onFlowDeleted

Override for logic when an existing flow to the Super App is deleted. Note: This callback must not revert to avoid jailing the Super App.

```solidity
function onFlowDeleted(
    ISuperToken superToken,
    address sender,
    address receiver,
    int96 previousFlowRate,
    uint256 lastUpdated,
    bytes calldata ctx
) internal virtual returns (bytes memory /*newCtx*/) {
    // Your logic here
}
```

### Registering a Super App

Deploying a Super App involves integration with the Superfluid Protocol and compliance with its governance for activation.
For your Super App to be recognized by the protocol, you must register it with the Superfluid Host contract.
If you deploy your Super App on a testnet, you can call the function `selfRegister` to register it.

This is how the function looks on the CFASuperAppBase:

```solidity
function selfRegister(
        bool activateOnCreated,
        bool activateOnUpdated,
        bool activateOnDeleted
    ) public {
        HOST.registerApp(getConfigWord(activateOnCreated, activateOnUpdated, activateOnDeleted));
    }
```

If you are deploying on a mainnet or a network with permissioned registration, you will need to follow the registration process outlined in [Registering a Super App](/docs/protocol/advanced-topics/super-apps/register).

---

<a id="doc_23"></a>

## 📁 protocol/advanced-topics/super-apps / Registering Super Apps

*파일 경로: protocol/advanced-topics/super-apps/register.mdx*

---
sidebar_position: 4
---

### Overview

To activate a Super App, you need to register it in the [Superfluid Host](/docs/concepts/advanced-topics/superfluid-host) contract. This registration is crucial for enabling the Super App's business logic to be invoked via agreement hooks.

### Registration Process

#### Basic Registration

You can 

1. Use the `registerApp` method of the host contract.
2. Two ways to register:
   - Self-registration: `registerApp(configWord)`
   - Registration by another account: `registerApp(app, configWord)`



#### Permissioned vs. Non-Permissioned Networks

Some networks require additional steps for Super App registration. Here's how to check:

1. Query `host.APP_WHITE_LISTING_ENABLED()` on your target network.
2. You can do this via the Superfluid Explorer:
   - Go to the "protocol" section (e.g., [Polygon Mainnet Explorer](https://Explorer.superfluid.finance/matic/protocol))
   - Click the Explorer link for "Host"
   - Navigate to Contract -> Read as Proxy
   - Expand "WHITE_LISTING_ENABLED"

![Superfluid Explorer Screenshot](https://github.com/superfluid-finance/protocol-monorepo/assets/5479136/442b460c-d1e9-419e-8483-12235ca19f0a)

- If `false`: Standard registration process applies
- If `true`: Follow the permissioned registration process below

### Permissioned App Registration

If your target network requires permissioned registration:

1. Get a "deployer" account whitelisted (can be an EOA or a contract)
2. Choose your deployment strategy:

   a) For a single Super App:
   - Register in the constructor or initialize method
   - Use `host.registerApp(configWord)`
   - Whitelist the EOA making this transaction

   b) For multiple Super App instances (e.g., factory pattern):
   - Whitelist a contract as the deployer
   - Use `host.registerApp(app, configWord)` from this contract

#### Important Notes

- Using `registerApp(configWord)`: `tx.origin` must be whitelisted
- Using `registerApp(app, configWord)`: `msg.sender` must be whitelisted

### Need Help?

If you need assistance or have questions about the process:
1. Join our [Discord](http://discord.superfluid.finance/)
2. Contact the Superfluid dev team in the #development channel

### Code Examples

Here are some basic examples to illustrate the registration process:

```solidity
// Self-registration in constructor
constructor(ISuperfluid host, uint256 configWord) {
    host.registerApp(configWord);
}

// Registration by another account
function registerSuperApp(ISuperfluid host, ISuperApp app, uint256 configWord) external {
    host.registerApp(app, configWord);
}
```

Remember to adjust these examples based on your specific Super App implementation and network requirements.

---

<a id="doc_24"></a>

## 📁 protocol/advanced-topics/super-apps / Super Apps in Depth

*파일 경로: protocol/advanced-topics/super-apps/understand-super-apps.mdx*

---
sidebar_position: 2
---

import Admonition from '@theme/Admonition';
import CodeBlock from '@theme/CodeBlock';


#### **What is a Super App?**

Super Apps are smart contracts registered with the Superfluid Protocol, allowing them to **react to Super Agreements** (like money streams). They are similar to ERC777 hooks but for Super Agreements.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![The Tradeable Cashflow NFT](/assets/image_(29)_(1).png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*The Tradeable Cashflow NFT*</p>
</div>

Super Apps can execute custom logic in response to streaming-related actions. A great example is the [tradeable cashflow NFT contract](https://github.com/superfluid-finance/super-examples/tree/c784d239557d6fb5e56a2c8951ac4353256d611d/projects/tradeable-cashflow), which automatically opens a new stream from the NFT contract to the owner of the NFT upon receiving a stream.

Callbacks in Super Apps are triggered by these actions:

1. A flow is opened with the Super App as the `receiver`.
2. A flow involving the Super App as the `receiver` is updated.
3. A flow is closed by the Super App's counterparty.

These callbacks can execute any arbitrary logic, enabling a wide range of possibilities for Super Apps.

#### Super App Configuration

Super Apps need to be registered with the Superfluid Protocol to use callbacks. Here's how to register a Super App:

<CodeBlock className="language-javascript">
{`
// Example registration code for a Super App
uint256 configWord =
    SuperAppDefinitions.APP_LEVEL_FINAL |
    SuperAppDefinitions.BEFORE_AGREEMENT_CREATED_NOOP |
    SuperAppDefinitions.BEFORE_AGREEMENT_UPDATED_NOOP |
    SuperAppDefinitions.BEFORE_AGREEMENT_TERMINATED_NOOP;

string memory registrationKey = ""; // Can be empty for testnet deployments

_host.registerAppWithKey(configWord, registrationKey);
`}
</CodeBlock>

The `APP_LEVEL_FINAL` flag ensures that the callbacks run in the first app in a chain of Super Apps. The `_NOOP` designations specify which callbacks are not used, avoiding unnecessary reverts.

For mainnet deployments, pre-approval is required for registering Super Apps. Check out the [Super App White-listing Guide](https://github.com/superfluid-finance/protocol-monorepo/wiki/Super-App-White-listing-Guide) for more information.

#### Super App Stream Buffers

When creating a Superfluid stream, an up-front buffer is taken to ensure the protocol's security. These deposits vary based on whether the stream is sent to a Super App and whether it's on testnet or mainnet.

For example, on testnets, the deposit is 1 hour x `flowRate` for non-Super Apps and up to 2 hours x `flowRate` for Super Apps. On mainnet, these values are 4 hours and 8 hours x `flowRate`, respectively.

#### Super App Callbacks

Super App callbacks are triggered in response to certain actions in Superfluid agreements:

- When a stream is created, updated, or closed involving a Super App.
- Before and after these actions occur, different callbacks are executed.

Callback Anatomy:

<CodeBlock className="language-javascript">
{`
function beforeAgreementCreated(
    ISuperToken /*superToken*/,
    address /*agreementClass*/,
    bytes32 /*agreementId*/,
    bytes calldata /*agreementData*/,
    bytes calldata /*ctx*/
)
    external
    view
    virtual
    override
    returns (bytes memory /*cbdata*/)
{
    revert("Unsupported callback - Before Agreement Created");
}
`}
</CodeBlock>

<CodeBlock className="language-javascript">
{`
function afterAgreementCreated(
    ISuperToken /*superToken*/,
    address /*agreementClass*/,
    bytes32 /*agreementId*/,
    bytes calldata /*agreementData*/,
    bytes calldata /*cbdata*/,
    bytes calldata /*ctx*/
)
    external
    virtual
    override
    returns (bytes memory /*newCtx*/)
{
    revert("Unsupported callback - After Agreement Created");
}
`}
</CodeBlock>

#### Super App Rules (Jail System)

Super Apps must comply with specific rules to avoid being jailed. These rules ensure the security and proper functioning of the protocol.

1. Super Apps cannot revert in the termination callback.
2. Super Apps must not become insolvent.
3. Operations within the termination callback must adhere to a gas limit.
4. The `ctx` data must be correctly handled in the termination callback.

##### Checking for Jailing

To check if a Super App is jailed, call `isAppJailed` on the Superfluid Host contract with the Super App's address. This can be done on Etherscan or through the Superfluid subgraph.

<Admonition type="note">
  For more details on the Jail system and Super App rules, visit the [Superfluid documentation](https://docs.superfluid.finance/superfluid).
</Admonition>

#### Conclusion

Super Apps offer a versatile framework for building complex, reactive financial applications on the Superfluid Protocol. By understanding their mechanics, rules, and potential, developers can create innovative solutions for real-time finance.

---

<a id="doc_25"></a>

## 📁 protocol/contribute / Bounty Program

*파일 경로: protocol/contribute/bounty-program.mdx*

---
sidebar_position: 1
---



The Superfluid Bounty Program allows developers to tackle a variety of technical issues laid out by the Superfluid Team and earn payouts for completion. Ready to get bounty hunting? Let's get started!

### Bounties

Pick a bounty issue you would like to complete in our [repo](https://github.com/orgs/superfluid-finance/projects/17/). They range in skill utilization (Solidity, Node.js, DevOps, etc.) and size.

### Getting Started

Comment on the GitHub issue with the below template:

```
Hi @youssea, I'm interested in taking on this bounty: Expected Completion Date: [ date you intend on completing the bounty by ** ]

```

In the #💰bounties channel in our [Discord](https://discord.gg/pPzPEDMVua), notify us of your intent to create the bounty with the below message template:

```
Hi @Sunny | Superfluid#7782, I'm interested in taking on this bounty: Issue: [ link to GitHub issue ] Expected Completion Date: [ date you intend on completing the bounty by ** ]

```

** This is a soft deadline. It is simply so we can check up on progress and offer support.

### During Work

A Superfluid team member will open a Discord thread for communication as you work on your issue. Let us know how things are going and if you've got any questions! We're super responsive :)

### Upon Completion

- Submit a pull request and tag the bounty issue you've completed in it ([Example Pull Request](https://github.com/superfluid-finance/protocol-monorepo/pull/717)).
- Once it's merged, fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSePPMtMcDndvgJvpkDMtY1BChkrXaqABO0SKA-4c-i2rbhZKA/viewform) and submit [this invoice](https://app.request.finance/create/3834fe3c2faaa829) to us.
    - In the Bounty KYC Form, for "Hackathon Name" put down the "Bounty".
    - In the Bounty KYC Form, for "Your Hack Name" put down the title of your bounty.
    - In the Request Invoice, please invoice for USDC on Polygon (not DAI or any other token).
- Wait for your bounty to pay out on the next Wednesday! Congrats on your valued contribution to Superfluid 🏁

### Referrals

If you find someone to complete a bounty, you can earn 20% of the bounty value as a referral payout!

- When the person you referred completes the bounty, let us know in the **#💰bounties** channel that you referred that person.
- We will verify with the bounty completer that you did in fact refer that person.
- If that looks good, we'll give you the green light to follow steps 2 and 3 of "Upon Completion" below to earn your payout.

:::tip Note
To make it easier for us to verify your referral, please have the person you referred add this to the form field *Your Hack Name*: "Referred by [your Discord or GitHub handle]".
:::

### Important Note

Bounty hunters must adhere to the following statement 👇

*"I am not a resident, citizen, national or agent of, or an entity organized, incorporated or doing business in, Belarus, Burundi, Crimea and Sevastopol, Cuba, Democratic Republic of Congo, Iran, Iraq, Libya, North Korea, Somalia, Sudan, Syria, Venezuela, Zimbabwe or any other country to which the United States, the United Kingdom, the Cayman Islands, the European Union or any of its member states or the United Nations or any of its member states (collectively, the “Major Jurisdictions”) embargoes goods or imposes similar sanctions (such embargoed or sanctioned territories, collectively, the “Restricted Territories”). I am not, and do not directly or indirectly own or control, and have not received any assets from, any blockchain address that is, listed on any sanctions list or equivalent maintained by any of the Major Jurisdictions (such sanctions-listed persons, collectively, “Sanctions Lists Persons”). I do not intend to transact in or with any Restricted Territories or Sanctions List Persons. I did not take part and do not intend to take part to any illegal activity, including but not limited to money laundering, internet hacking and terrorism financing."*

---

<a id="doc_26"></a>

## 📁 protocol/contribute / Security & Bug Bounties

*파일 경로: protocol/contribute/bug-bounties.mdx*

---
sidebar_position: 2
---

import React from 'react';
import Link from '@docusaurus/Link';


### Immunefi Bug Bounty Program

We have an [Immunefi](https://immunefi.com/bounty/superfluid/) bug bounty program with a maximum bounty of $100,000.

This program is focused on the protocol's smart contracts and is focused on preventing:

- Superfluid framework bugs
- Bugs in CFA/IDA in general
  - Anything that would avoid streams from being closed
  - Anything that would result in the sum of all account balances drifting significantly from the total supply
- Theft of tokens in third party wrapper contracts
- Other unexpected behavior in any super token contracts

**Learn more here:**

For more details, please visit the [Immunefi Bug Bounty Program page](https://immunefi.com/bounty/superfluid/).

### Audit Resources

Superfluid has been audited on multiple occasions, you can find these past audit reports here:

For the audit reports, check out the [Superfluid GitHub repository](https://github.com/superfluid-finance/protocol-monorepo/tree/dev/packages/ethereum-contracts/audits).

### General Security Tips For Superfluid Developers

- We recommend what every good security expert would recommend: full test coverage, separation of concerns, and using automated tools like GitHub Actions or [Trail of Bits](https://blog.trailofbits.com/2018/03/23/use-our-suite-of-ethereum-security-tools/)' tools for fuzzing & static analysis
  - Guides like [this one from Consensys](https://consensys.github.io/smart-contract-best-practices/) can be helpful in understanding what to think about before deploying smart contracts to mainnet.
  - If you're looking for inspiration on setting up your own GitHub Actions pipelines, you can find a breakdown of Superfluid's own GitHub Actions setup [here](https://github.com/superfluid-finance/protocol-monorepo/wiki/Superfluid-GitHub-Actions-Deep-Dive).
- Beyond this, we recommend that you continue to think about security & potential for loss of funds in the front end and off-chain components of your project (if you have them).
  - For example, we highly recommend you adopt some of the same UX practices that we do in the [Superfluid dashboard](https://app.superfluid.finance/) if you have a front end that allows people to create Superfluid streams.
  - I.e., we let the user know that letting their balance hit zero before they close their stream will [lead to a liquidation](/docs/protocol/advanced-topics/solvency/liquidations-and-toga).

#### Security Tips for Building Super Apps

- Be careful that your application does not get jailed unexpectedly.
- We have detailed information [here](https://docs.superfluid.finance/superfluid/developers/super-apps/super-app#super-app-rules-jail-system) regarding the jail system and how to avoid a jailed Super App, but one of the most common reasons for a jailed super app is an unexpected revert in either the `beforeAgreementTerminated` or `afterAgreementTerminated` callbacks.

#### Custom Super Tokens

- In general, we advise sticking to the existing Super Token interfaces seen [here](https://github.com/superfluid-finance/protocol-monorepo/tree/dev/packages/ethereum-contracts/contracts/interfaces/tokens) unless you have a good reason not to.
- If you want to deviate from this, we strongly encourage you to reach out to the Superfluid developer team in the #dev-support channel in our [Discord](https://discord.superfluid.finance).

---

<a id="doc_27"></a>

## 📁 protocol/contribute / Token Explorer Submission

*파일 경로: protocol/contribute/submit-token-dashboard.mdx*

---
sidebar_position: 3
---

import TokenListingForm from '@site/src/components/TokenListingForm';


You want your token to show up on the [Superfluid Explorer](https://Explorer.superfluid.finance/)? Look no further.
In order to list a new token on the [Superfluid Explorer](https://Explorer.superfluid.finance/) and have it visible in our Dashboard, please follow the steps below.

:::warning Disclaimer
If your token looks like a potential scam or we can't find reliable information about your project/company, we reserve the right to avoid listing it on our visual Dashboard.
:::

### Steps to List Your Token

#### 1. Fill out the form

You will find the form below. If you prefer, you can also access it [here](https://airtable.com/appxGogNpt64ImOFH/shrzOcdK9eveDmRWV).

<TokenListingForm/>

#### 2. Issue Created

When you submit the Airtable form, it auto-generates a GitHub issue in our Token Assets repository. You can find the issues [here](https://github.com/superfluid-finance/assets/issues).

The Superfluid team will use the informations from the issue to add the token to the Explorer and to our protocol resolver. Hang tight!

#### 3. Confirmation

The issue will be closed upon completion or rejection. Wait for a confirmation by the Superfluid team to the Discord handle you provided in the form before sharing publicly that your token is now live on Superfluid.

If you don't hear back from us within a week or need more information on the listing process, please feel free to reach out via email at [support@superfluid.finance](mailto:support@superfluid.finance) or reach out to us in the Support Channel of our [Discord](https://discord.gg/pPzPEDMVua).

---

<a id="doc_28"></a>

## 📁 protocol/distributions / Distribution Pools Explained

*파일 경로: protocol/distributions/overview.mdx*

---
sidebar_position: 1
---

import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';
import UnitsVisualization from "@site/src/components/Visualizations/UnitsVis";
import PoolStreamVisualization from '@site/src/components/Visualizations/PoolStreamVis';
import PoolInstantVis from "@site/src/components/Visualizations/PoolInstantVis";
import PoolStreamVis from "@site/src/components/Visualizations/PoolStreamVis";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


### Introduction

Distributions is a Superfluid primitive that allows scalable are one-to-many or many-to-many transfer of value, in the form of discreet transfers or [Money Streaming](/docs/protocol/money-streaming/overview.mdx).
Superfluid's implementation of this concept allows for the creation of **Pools** with a designated **pool admin** who manages **units** for **pool members**.
Members of these pools can receive funds either instantly or through continuous streaming, making this method highly efficient and scalable.
We make the difference between two types of Distributions:

- **Instant Distribution**: They allow one discreet transfer of Super Tokens to any number of receivers with a fixed gas cost.
- **Streaming Distribution**: They allow for continuous distribution of funds to receivers through [Money Streaming](/docs/protocol/money-streaming/overview.mdx) to a Pool.

:::note About Pools
The same pool can be used to distribute any Super Token, be it for Instant or Streaming Distributions.
:::

---
<Tabs defaultValue="instant" values={[
  { label: 'Instant Distribution', value: 'instant' },
  { label: 'Streaming Distribution', value: 'streaming' },
]}>
<TabItem value="instant">

**Instant Distributions allow one transaction to distribute to any number of receivers with a fixed gas cost.**

<div style={{ display: "flex", justifyContent: "center" }}>
  *Click on the Blue Circle to initiate an Instant Distribution*
  <br />
</div>
<PoolInstantVis />
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>
    *By creating a Distribution Pool, you can distribute any token instantly*
  </p>
</div>

  </TabItem>
  <TabItem value="streaming">

**Instant Distributions allow for continuous distribution of funds to receivers through [Money Streaming](../money-streaming/overview.mdx) to a Pool.**

<div style={{ display: "flex", justifyContent: "center" }}>
  *Watch how the continuous stream gets distributed automatically through the pool*
  <br />
</div>
<PoolStreamVis />
<div style={{ display: "flex", justifyContent: "center" }}>
  <p>
    *By creating a Distribution Pool, you can distribute any stream with no gas cost*
  </p>
</div>

  </TabItem>
  
</Tabs>

---
#### How It Works

1. **Create a Pool**: Deploying a pool contract creates a pool with a unique address.
2. **Assigning Proportions**: The pool admin sets proportions by allocating units to pool members.
3. **Distributing Tokens**: Pool members receive tokens based on their unit holdings.

<Admonition type="info">
Distributions are persistent, allowing multiple triggers with varying amounts. Units can be adjusted as needed.
</Admonition>

### Key Concepts

- **Pool**: Channels for proportional token distribution.
- **Pool Admin**: Decides of the most important parameters of the distribution, including units.
- **Pool Members**: Receivers allocated units for distribution.

<div style={{ display: 'flex', justifyContent: 'center' }}>
<UnitsVisualization/>
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Visualization of unit distribution in a pool*</p>
</div>

### Balancing Formula

Calculates the current balance of an account subscribed to one or more distribution Indices.

<div style={{ display: 'flex', justifyContent: 'center' }}>
![Balance calculation formula](/assets/image_(56).png)
</div>

<Admonition type="info">
Publishers can manage multiple Indices, and subscribers can be part of multiple Indices.
</Admonition>

### Pool Administration and Member Participation

Pool admins manage units and distributions, while members receive distributions based on their units.

<div style={{ display: 'flex', justifyContent: 'center' }}>
<PoolStreamVisualization/>
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Visualization of money streaming from an external source to a Pool and its members*</p>
</div>

#### Distribution Types

- **Instant Distribution**: One-time proportional token allocation.
- **Streaming Distribution**: Continuous flow of tokens over time.

#### Major Design Choices

- **Pool Administration**: Admins have control over unit management and token distribution.
- **Member Participation**: Members receive distributions proportionate to their units.
- **ERC20 Compatibility**: The Pool interacts seamlessly with ERC20 standards.

### Learn More about Distribution Pools
- [What is a Distribution Pool?](/docs/protocol/distributions/guides/pools.mdx#what-is-a-pool)
- [Important Pools related Functions](/docs/protocol/distributions/guides/pools#important-functions)
- [Example: Advertisement Auction DApp](/docs/protocol/distributions/examples/example1)

---

<a id="doc_29"></a>

## 📁 protocol/distributions/guides / Create, Update and Connect your Pools

*파일 경로: protocol/distributions/guides/on-chain.mdx*

---
sidebar_position: 2
---

import Admonition from '@theme/Admonition';


Building on top of the Superfluid's Distribution Pools protocol involves interacting with Super Tokens. Remember, Superfluid is a token-centric protocol, and all of the primitives are centered around [Super Tokens](/docs/protocol/super-tokens/overview).
Distribution Pools allow for scalable and efficient one-to-many token distributions at a fixed gas cost.

When interacting with Super Tokens on-chain, you can use the Superfluid's [SuperTokenV1Library](/docs/technical-reference/SuperTokenV1Library) to access the core functions.

:::warning About the General Distributions Agreement
At times, we use "Distribution Pools" or the "General Distributions Agreement" (GDA) interchangeably.
The GDA is the name of the implementation in our codebase. If you are interested in the technical details, you can find the full Superfluid Architecture [here](/docs/technical-reference/Architecture).
:::

### Importance of Distribution Pools

Distribution Pools are at the core of Superfluid's functionality, enabling a multitude of applications such as subscription services, salary payments, and rewards distribution. They are designed to be flexible, allowing for both instant and streaming distributions.

- **Instant Distributions**: Allow for a one-time distribution of a specified amount of tokens to all members of a pool instantly.
- **Streaming Distributions**: Enable a continuous flow of tokens to pool members over time.

:::note About Pools
The same pool can be used to distribute any Super Token, be it for Instant or Streaming Distributions.
:::


### Key Functions of SuperTokenV1Library.sol

[`SuperTokenV1Library.sol`](/docs/technical-reference/SuperTokenV1Library) provides several functions to interact with pools and distributions:


#### createPool

```solidity
function createPool(ISuperToken token, address admin, struct PoolConfig poolConfig) internal returns (contract ISuperfluidPool pool)

// simplified variant using the following default settings:
// admin = msg.sender, poolConfig = { transferabilityForUnitsOwner: false, distributionFromAnyAddress: true }
function createPool(contract ISuperToken token) internal returns (contract ISuperfluidPool pool);
```

Creates a new Superfluid Distribution Pool.

#### distribute

```solidity
function distribute(ISuperToken token, ISuperfluidPool pool, uint256 amount) internal returns (bool)
```

Distributes the specified amount of tokens among pool members.

#### distributeFlow

```solidity
function distributeFlow(ISuperToken token, ISuperfluidPool pool, int96 requestedFlowRate) internal returns (bool)
```

Initiates a distribution flow from a sender to a pool with the specified total flow rate.

:::warning Important
Keep in mind that the total amount of units in the pool needs to be significantly lower than the total flow rate or the total tokens distributed of the pool.
To understand more why this is the case, please refer to the [Member Units](/docs/protocol/distributions/guides/pools.mdx#about-member-units) section.
:::

#### connectPool

```solidity
function connectPool(ISuperToken token, contract ISuperfluidPool pool) internal returns (bool)
```

Connects a pool member to pool.

:::tip About Pool Connections
Learn more about claiming units and connecting to pools in the [How to design your pools section](/docs/protocol/distributions/guides/pools#about-pool-connections-and-claiming).
:::

#### getFlowDistributionFlowRate

```solidity
function getFlowDistributionFlowRate(ISuperToken token, address from, ISuperfluidPool to) internal view returns (int96)
```

Gets the flow rate of a distribution from a sender to a pool.

#### isMemberConnected

```solidity
function isMemberConnected(ISuperToken token, address pool, address member) internal view returns (bool)
```

Checks whether a member is connected to a pool and eligible to receive distributions.

### ISuperfluidPool

#### updateMemberUnits

```solidity
function updateMemberUnits(address memberAddress, uint128 newUnits) internal returns (bool)
```

Updates the units of a pool member.

### Contract Example

Here's a simple contract example using some of the functions from `SuperTokenV1Library.sol` to interact with distributions:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@superfluid-finance/ethereum-contracts/contracts/superfluid/SuperTokenV1Library.sol";

contract MyDistributionsContract {
    using SuperTokenV1Library for ISuperToken;

    ISuperToken private _superToken;

    constructor(ISuperToken superToken) {
        _superToken = superToken;
    }

    function estimateDistribution(ISuperfluidPool pool, uint256 amount) public {
        _superToken.estimateDistributionActualAmount(address(this), pool, amount);
        // Additional logic for distribution
    }

    function startStreamingDistribution(ISuperfluidPool pool, int96 flowRate) public {
        _superToken.distributeFlow(pool, flowRate);
        // Additional logic for streaming distribution
    }
}
```

This contract demonstrates how to use the `SuperTokenV1Library` in order to interact with Distribution Pools.

:::tip
When using the `SuperTokenV1Library.sol`, you don't need to include the `SuperToken` as a parameter in your method call.
Simply call `SuperToken.[Method]` and the library will handle the rest.
:::

### Further Reading
For more detailed information on the implementation and usage of `SuperTokenV1Library.sol`, refer to the [SuperTokenV1Library Technical reference](/docs/technical-reference/SuperTokenV1Library).

---

<a id="doc_30"></a>

## 📁 protocol/distributions/guides / How to Design your Distribution Pools?

*파일 경로: protocol/distributions/guides/pools.mdx*

---
sidebar_position: 1
---
import Admonition from '@theme/Admonition';
import PoolsVisualization from '@site/src/components/Visualizations/PoolStreamVis';


In this page we will explain Distribution Pools and show you the most relevant ways to interact with them through the Super Token interface.
To do this, we will go through some key concepts, and show you how to leverage Superfluid's [`SuperTokenV1Library.sol`](/docs/technical-reference/SuperTokenV1Library) for your Distribution Pools smart contracts.

:::note About `SuperTokenV1Library.sol`
The [`SuperTokenV1Library.sol`](/docs/technical-reference/SuperTokenV1Library) is a comprehensive library which makes it more convenient to use invoke Superfluid specific functionality on Super Tokens.
:::

:::warning About the General Distributions Agreement - GDA
At times, we use "Distribution Pools" or the "General Distributions Agreement (GDA)" interchangeably due to "GDA" being the name of the implementation in our [codebase](https://github.com/superfluid-finance/protocol-monorepo). 
:::

### What is a Pool?

A pool is a smart contract that facilitates the distribution of tokens to multiple members, managed by a pool admin. Members hold units within the pool that determine their proportion of the distribution.

<div style={{ display: 'flex', justifyContent: 'center' }}>
<PoolsVisualization/>
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*A visualization of units in a pool*</p>
</div>

:::note

The Superfluid pool implements basic ERC20 functionality, allowing it to interact seamlessly with [ERC20](https://docs.openzeppelin.com/contracts/4.x/erc20) standards.
This allows you to interact with the pool units as if they were ERC20 tokens, including transferring them to other addresses, if it is allowed by the pool configuration.
Check the [next section](#important-functions) for more information on pool configurations.

:::

### About Member Units

#### How is a member's share of the pool determined?

A pool member's units determine their share of the pool's distributions.
In the background, the calculation of each member's share is calculated following these two steps:

1. **Calculating the flow rate per unit:** We calculate the flow rate or amount of tokens to be distributed *per unit* like so:

<div style={{ display: 'flex', justifyContent: 'center' }}>
    <img src="/assets/flowrate-formula.png" alt="Superfluid with people" width="400" />
</div>
<br/>
2. **Calculating the flow rate for each member:** We multiply the flow rate per unit by the number of units each member has to get the flow rate for each member, as follows:
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <img src="/assets/flowrate-member-units.png" alt="Superfluid with people" width="500" />
</div>
<br/>

One of the limitations of Solidity is its incapacity to handle floating point numbers. 
This makes it so that the flow rate per unit is calculated as an integer. If the result of the division is not an integer, the result is rounded down.

#### Examples

The examples below show how the flow rate per unit is calculated in different scenarios where Distributions reach their limitations

1. **Example 1:** Let's take a pool that has 100 wei/second as total flow rate and 3 members, each member has 1 unit.
    - The flow rate per unit is 100 / 3 = 33.33
    - However, since Solidity can't handle floating point numbers, the flow rate per unit is 33
    - The pool distributes 33 tokens to each unit
    - 1 token is left undistributed
2. **Example 2:** Let's take a pool that has 100 wei/second as total flow rate and 200 members, each member has 1 units.
    - The flow rate per unit is 100 / 200 = 0.5
    - However, since Solidity can't handle floating point numbers, the flow rate per unit is 0
    - The pool distributes 0 tokens to each unit
    - 200 tokens are left undistributed

These examples are extreme and almost never happen in practice. However, it is important to be aware of these limitations when designing your pools.

:::tip How to design your pools?
The best way to design your pools is to make sure that the total flow rate or the tokens distributed are always orders of magnitude higher than the number of total units in the pool.
This way, you can be sure that the flow rate per unit will always be significantly higher than 0 and that all members will receive a share of the distribution.
:::

### About Pool Connections and Claiming

#### What is the difference between connecting to a pool and claiming tokens?
After creating a pool and assigning units to pool members,
they need to connect to the pool or claim their Super Tokens in order for it to show on their balance.
Simply assigning units (shares) to a member does not automatically reflect in their balance.
The accumulated tokens NEED to be claimed by the member (or a different address), or the member needs to connect to the pool
to start receiving their share of the Super Token Distributions.

#### How can members collect their Distributions from the pool?

There are two ways for members to get their streamed or transferred Super Tokens from a pool:
- **Connecting to the Pool (Recommended)**: Members should connect to the pool to start receiving their share of the Super Token Distributions in real time to their balance.
This includes both Instant Distributions and Streaming Distributions. In order to connect to the pool, the member should call the `connectPool` function from the [`SuperTokenV1Library`](/docs/technical-reference/SuperTokenV1Library) or [`GDAv1Forwarder`](/docs/technical-reference/GDAv1Forwarder#fn-connectpool).
The address calling the function should be the address of the member. Other addresses will not be able to connect a member to the pool.

- **Claiming the Tokens**: Members can claim their share of the Super Token Distributions accumulated from the pool at any time,
even if they are not connected to the pool. As a matter of fact, anyone can claim the tokens on behalf of the member. To do so, the function
`claimAll` from the [`SuperTokenV1Library`](/docs/technical-reference/SuperTokenV1Library) or [`GDAv1Forwarder`](/docs/technical-reference/GDAv1Forwarder#fn-claimall) should be called with the address of the member as the argument.

:::note Connecting to the pool includes claiming
When a member connects to the pool, they automatically claim the accumulated tokens and start receiving the distributions in real time.
:::

:::tip Reminder
We use the `SuperTokenV1Library` to interact with the Superfluid protocol [on-chain](/docs/protocol/distributions/guides/distributions-and-super-tokens/on-chain) (from your smart contracts),
while we use the forwarders (eg. `GDAv1Forwarder`) to interact with the Superfluid protocol [off-chain](/docs/protocol/distributions/guides/distributions-and-super-tokens/off-chain) (from your web3 frontend applications).
:::

:::tip Recommendation
It is recommended to prompt users to connect to the pool as soon as possible to start receiving the distributions in real time.
Depending on your use case, periodic claiming may also offer the best UX, however pool connections usually offer
the best UX for real-time distributions.
:::

#### How can members disconnect from the pool?
Members can always disconnect from the pool to stop receiving distributions in real time by calling the function `disconnectPool` from the [`SuperTokenV1Library`](/docs/technical-reference/SuperTokenV1Library) or [`GDAv1Forwarder`](/docs/technical-reference/GDAv1Forwarder#fn-disconnectpool).

#### Example
- **Jake** creates a pool and assigns 100 units to **Alice**, 200 units to **Bob**, and 200 units to **Charlie**.
- **Alice** connects to the pool before any Distribution is made. Thus, she's able to receive her share of the Distributions in real time when they start.
- **Jake** starts a stream of 100 tokens/second to the pool.
- **Alice** receives 20 tokens/second directly into her balance, **Bob** and **Charlie** each accumulate 40 tokens/second in the pool.
- After 100 seconds, **Alice** can already see 2000 tokens on her balance. **Bob** and **Charlie** are each eligible to get 4000 tokens, but they cannot see them on their balance just yet.
- **Bob** chooses to claim every 100 seconds, while **Charlie** chooses to connect to the pool.
- **Bob** receives periodically 4000 tokens every 100 seconds.
- By connecting to the pool, **Charlie** automatically claims the accumulated tokens, but also starts receiving tokens in real time.


### Important Functions

Here are some of the most important functions for interacting with Superfluid pools:

:::note Reminder
Some of this functions are available via [`SuperTokenV1Library.sol`](/docs/technical-reference/SuperTokenV1Library) (contracts using that lib) only.
:::

#### createPool

```solidity
function createPool(ISuperToken token, address admin, PoolConfig memory poolConfig)
```

Creates a new pool with the specified admin, configuration and poolConfig.

The `PoolConfig` struct is defined as follows:

```solidity
struct PoolConfig {
    bool transferabilityForUnitsOwner;
    bool distributionFromAnyAddress;
}
```
- `transferabilityForUnitsOwner`: If true, the pool members can transfer their owned units, else, only the pool admin can manipulate the units for pool members
- `distributionFromAnyAddress`: If true, anyone can execute distributions via the pool, else, only the pool admin can execute distributions via the pool

:::warning Strong recommendation
We don't recommend setting `transferabilityForUnitsOwner` to `true` unless you have a specific use case that absolutely requires it. This can sometimes lead to unexpected behavior and security risks.
:::

SuperTokenV1Library also provides overloaded variants setting default values for `admin` (default: `msg.sender`) and/or `poolConfig` (default: `{ transferabilityForUnitsOwner: false, distributionFromAnyAddress: true }`).

#### updateMemberUnits

This function is part of `ISuperfluidPool`, can thus be invoked on pool contracts.

```solidity
function updateMemberUnits(address memberAddress, uint128 newUnits)
```

Updates the number of units a member has within a pool, effectively changing their share of future distributions.

:::warning Important
Keep in mind that the total amount of units in the pool needs to be significantly lower than the total flow rate or the total tokens distributed of the pool.
To understand more why this is the case, please refer to the [Member Units](#about-member-units) section.
:::

#### claimAll

```solidity
function claimAll(ISuperToken token, ISuperfluidPool pool, address memberAddress)
```

Allows a member to claim their share of the tokens from all previous distributions.

#### connectPool

```solidity
function connectPool(ISuperToken token, ISuperfluidPool pool)
```

Connects a pool member to a pool.

:::tip About pool connections
The pool member needs to connect to a pool before the distribution balance is reflected in their net balance.
If the distribution starts before the user is connected to the pool, the user will still receive the tokens
when they connect to the pool eventually.
:::

#### disconnectPool

```solidity
function disconnectPool(ISuperToken token, ISuperfluidPool pool)
```

Disconnects a pool member from a pool.

#### distribute

```solidity
function distribute(ISuperToken token, ISuperfluidPool pool, uint256 requestedAmount)
```

Distributes a specified amount of tokens to the pool, to be shared among members according to their units.

#### distributeFlow

```solidity
function distributeFlow(ISuperToken token, ISuperfluidPool pool, int96 requestedFlowRate)
```

Flow-distributes with the specified flowrate to the pool, with the flow going to members according to their units.

### Example Usage

Here's how you might use these functions within a smart contract to set up and manage a pool:

```solidity
// Assume ISuperToken and SuperfluidPool interfaces are imported and available.

contract MyPool {
    Using SuperTokenV1Library for ISuperToken;
    
    ISuperToken private superToken;
    ISuperfluidPool private pool;
    
    constructor(ISuperToken _superToken) {
        superToken = _superToken;
        // create a pool with default settings:
        // msg.sender is admin, non-transferrable units, anybody can distribute to it
        pool = superToken.createPool();
    }

    // Use updateMemberUnits to assign units to a member.
    // (This will typically be a permissioned operation, it's akin to minting tokens)
    function updateMemberUnits(address member, uint128 units) public {
        pool.updateMemberUnits(member, units);
    }

    // Instant distribution of tokens to pool members proportional to their current units
    function distribute(uint256 amount) public {
        superToken.distribute(pool, amount);
    }

    // Flow distribution of tokens to pool members proportional to their current units
    function distributeFlow(int96 flowRate) public {
        superToken.distributeFlow(pool, flowRate);
    }
}
```

In this example, `MyPool` creates a pool, adds a member, and makes an Instant Distribution (discreet transfer - through `distribute`) and a Streaming Distribution (continuous flow - through `distributeFlow`) using the functions from `SuperTokenV1Library.sol`.

:::info Learn more about the `SuperTokenV1Library`
For more detailed information on the implementation and usage of `SuperTokenV1Library.sol`, refer to the [Technical Reference](/docs/technical-reference/SuperTokenV1Library).
:::

---

<a id="doc_31"></a>

## 📁 protocol/distributions/guides / Testing

*파일 경로: protocol/distributions/guides/testing.mdx*

---
sidebar_position: 4
---

import TabItem from '@theme/TabItem'; import Tabs from '@theme/Tabs';


In this guide, we'll walk through the process of testing the `DistributionContract` using the Foundry framework. This guide follows the structure used for the `Superfluid` contract, adapting to the specifics of the `DistributionContract`.

### Prerequisites

Before diving into testing your Superfluid contracts with Foundry, make sure you have set up your development environment properly. Here's a brief explanation of each step required:

1. **Creating and Navigating to Your Project Directory**:

   ```bash
   mkdir superfluid-example && cd superfluid-example
   ```

   This command creates a new directory named `foundry-example` and then changes your current working directory to it.

2. **Initializing a Foundry Project**:

   ```bash
   forge init
   ```

   This initializes a new Foundry project in your directory, setting up the necessary structure and configuration for Ethereum smart contract development.

3. **Installing Superfluid Protocol Dependencies**:

   ```bash
   forge install superfluid-protocol-monorepo=https://github.com/superfluid-finance/protocol-monorepo --no-commit
   ```

   Installs the `dev` branch of the Superfluid protocol from its GitHub repository.

4. **Installing OpenZeppelin Contracts**:

   ```bash
   forge install https://github.com/OpenZeppelin/openzeppelin-contracts@v4.9.6 --no-commit
   ```

   Installs the necessary (4.9.X) of the OpenZeppelin contracts, which are widely used for secure smart contract development.

These steps ensure you have the necessary tools and dependencies installed to start developing and testing your Superfluid-based contracts with Foundry.

### Contract and Key Functions

<div>
<details>
<summary>Click here to show `DistributionContract`</summary> 
<p>

```solidity
//SPDX-License-Identifier: Unlicensed
pragma solidity ^0.8.14;

import { ISuperfluid, ISuperToken } from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";

import { SuperTokenV1Library } from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";

import {IGeneralDistributionAgreementV1, ISuperfluidPool, PoolConfig} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/agreements/gdav1/IGeneralDistributionAgreementV1.sol";

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IFakeDAI is IERC20 {

    function mint(address account, uint256 amount) external;

}

contract DistributionContract {

    using SuperTokenV1Library for ISuperToken;
    
    mapping (address => bool) public accountList;

    ISuperToken public daix;

    ISuperfluidPool pool;

    // fDAIx address on Polygon Mumbai = 0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f
    constructor(ISuperToken _daix) {

        daix = _daix;

    }

    /// @dev Mints 10,000 fDAI to this contract and wraps it all into fDAIx
    function gainDaiX() external {

        // Get address of fDAI by getting underlying token address from DAIx token
        IFakeDAI fdai = IFakeDAI( daix.getUnderlyingToken() );
        
        // Mint 10,000 fDAI
        fdai.mint(address(this), 10000e18);

        // Approve fDAIx contract to spend fDAI
        fdai.approve(address(daix), 20000e18);

        // Wrap the fDAI into fDAIx
        daix.upgrade(10000e18);

    }

    /// @dev creates a Pool with this contract being the admin
    function createPool(ISuperToken token, PoolConfig memory poolConfig) external {

        // Create Pool
        pool=daix.createPool(token, address(this), poolConfig);

    }

    /// @dev updates Units for a specific member
    function updateMemberUnits(address memberAddress, uint128 newUnits) external {

        // Update member units
        pool.updateMemberUnits(memberAddress, newUnits);

    }

    /// @dev creates a stream from this contract to the pool
    function createStreamToPool(int96 flowRate) external {

        // Create stream
        daix.createFlow(receiver, flowRate);

    }

}
```

</p> </details> </div>

* **gainDaiX**: Mints and wraps fDAI into fDAIx.
* **createPool**: Initiates a new Superfluid pool with this contract as the admin.
* **updateMemberUnits**: Updates units for a specific pool member.
* **createStreamToPool**: Creates a money stream from this contract to the pool.

### Writing Tests

#### Setting Up Your Test Environment

Your test environment will depend on where you would like to test your Superfluid application.
You can fork a public testnet where an instance of the Superfluid Protocol already exists (e.g Polygon Mumbai). In this case, you do not need to deploy a new instance of the Superfluid protocol.
However, if you are testing on a local testnet you would need to deploy a new instance of the Superfluid protocol.

<Tabs
    defaultValue="testnet"
    values={[
        { label: 'Forking Testnet', value: 'testnet' },
        { label: 'Local Net', value: 'localnet' },
    ]}
>

<TabItem value="testnet">

- Create a new Solidity file for your tests
- Import `forge-std/Test.sol` and inherit from `Test`.
- Import the Superfluid protocol contracts.
- Write your `setUp` function to run before each test case.

```solidity
pragma solidity ^0.8.14;
import "forge-std/Test.sol";
import {ISuperfluid, ISuperToken} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";
import {TestGovernance, Superfluid, ConstantFlowAgreementV1, CFAv1Library, SuperTokenFactory} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeploymentSteps.sol";
import {SuperfluidFrameworkDeployer} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeployer.sol";
import {SuperTokenV1Library} from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";

contract DistributionContractTest is Test {
    // Test contract instance
    DistributionContract distributionContract;
    // Mumbai fork parameters
    uint256 mumbaiFork;
    // Set up your environment variables and include MUMBAI_RPC_URL
    string MUMBAI_RPC_URL = vm.envString("MUMBAI_RPC_URL");

    // Setup function to initialize test environment
    function setUp() public {

        //Forking and selecting the Mumbai testnet
        mumbaiFork = vm.createSelectFork(MUMBAI_RPC_URL);

        //Pointing to the fake Daix contract on Mumbai
        //For token and protocol addresses on all networks, check out the Superfluid Explorer: https://Explorer.superfluid.finance/
        daix = ISuperToken(0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f);

        //Deploy the contract
        vm.prank(address(0x123)); // Simulate a different caller
        distributionContract= new DistributionContract(daix);
        vm.unprank(); // Restore the caller

        //Add other functions and test contracts...
    }
}
```

</TabItem>
<TabItem value="localnet">
- Create a new Solidity file for your test.
- Import `forge-std/Test.sol` and inherit from `Test`.
- Import the Superfluid protocol contracts.
- Deploy a new instance of the Superfluid Protocol in the `setUp`function.
- Create and Deploy a new instance of your test contract.

```solidity
pragma solidity ^0.8.14;
import "forge-std/Test.sol";
import {ISuperfluid} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";
import {SuperfluidFrameworkDeployer,
    TestGovernance,
    Superfluid,
    ConstantFlowAgreementV1,
    CFAv1Library,
    SuperTokenFactory
} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeployer.sol";


contract DistributionContractTest is Test {
    // Test contract instance
    DistributionContract distributionContract;
    //Set up your Superfluid framework
    struct Framework {
        TestGovernance governance;
        Superfluid host;
        ConstantFlowAgreementV1 cfa;
        CFAv1Library.InitData cfaLib;
        InstantDistributionAgreementV1 ida;
        IDAv1Library.InitData idaLib;
        SuperTokenFactory superTokenFactory;
    }

    SuperfluidFrameworkDeployer.Framework sf;
    

    // Setup function to initialize test environment
    function setUp() public {
        address public owner;
	    //DEPLOYING THE FRAMEWORK
        SuperfluidFrameworkDeployer sfDeployer = new SuperfluidFrameworkDeployer();
        sfDeployer.deployFramework();
        sf = sfDeployer.getFramework();
				
	    // DEPLOYING DAI and DAI wrapper super token

	    ISuperToken daix = sfDeployer.deployWrapperToken(
	    "Fake DAI", "DAI", 18, 10000000000000
	    );

        // Deploy your contract here
        distributionContract= new DistributionContract(daix);

    }
}
```
</TabItem>
</Tabs>

:::tip About the `setUp` Function
The `setUp` function is an **optional** function standardized by Foundry (but it is necessary here, especially in the case of local testnet). It is a special function that is executed before each test case. It is used to initialize the test environment and contract instances.
To learn more about the `setUp` function, check out the [Foundry documentation](https://book.getfoundry.sh/forge/writing-tests).
:::

#### Testing Contract Functions

##### GainDaiX Function

The `gainDaiX` function mints and wraps fDAI into fDAIx. Here's how to test it:

```solidity
function testGainDaiX() public {
    // Setup: Deploy the DistributionContract with a mock fDAIx token
    ISuperToken daix = new MockSuperToken();
    DistributionContract distributionContract = new DistributionContract(daix);

    // Action: Call the gainDaiX function
    distributionContract.gainDaiX();

    // Assertions: Check if the contract has the expected amount of fDAIx
    uint256 balance = daix.balanceOf(address(distributionContract));
    assertEq(balance, 10000e18, "The balance of fDAIx should be 10,000 after gainDaiX");
}
```

##### CreatePool Function

To test `createPool`, you'll verify if a pool is created with the correct parameters:

```solidity
function testCreatePool() public {
    // Setup: Deploy the DistributionContract and mock tokens
    ISuperToken daix = new MockSuperToken();
    DistributionContract distributionContract = new DistributionContract(daix);

    // Define pool configuration
    PoolConfig memory poolConfig;
    // Set poolConfig parameters...

    // Action: Call the createPool function
    distributionContract.createPool(daix, poolConfig);

    // Assertions: Verify if the pool is created correctly
    ISuperfluidPool pool = distributionContract.pool();
    // Additional assertions about pool...
}
```

##### UpdateMemberUnits Function

Testing `updateMemberUnits` involves checking if member units in a pool are updated correctly:

```solidity
function testUpdateMemberUnits() public {
    // Setup: Deploy the DistributionContract, create a pool, and add members
    ISuperToken daix = new MockSuperToken();
    DistributionContract distributionContract = new DistributionContract(daix);
    // Create pool...
    address memberAddress = address(new Member());

    // Action: Update member units
    uint128 newUnits = 100;
    distributionContract.updateMemberUnits(memberAddress, newUnits);

    // Assertions: Check if the member's units are updated
    uint128 updatedUnits = daix.getMemberUnits(memberAddress);
    assertEq(updatedUnits, newUnits, "Member units should be updated to the new value");
}
```

##### CreateStreamToPool Function

For `createStreamToPool`, you'll need to ensure that a stream is correctly established:

```solidity
function testCreateStreamToPool() public {
    // Setup: Deploy the DistributionContract and create a pool
    ISuperToken daix = new MockSuperToken();
    DistributionContract distributionContract = new DistributionContract(daix);
    // Create pool...

    // Action: Create a stream to the pool
    int96 flowRate = 1000;
    distributionContract.createStreamToPool(flowRate);

    // Assertions: Verify the stream is created with the correct flow rate
    // Implement checks for stream creation...
}
```

#### Using Cheat Codes

Foundry's cheat codes can simulate various scenarios. Here's an example of using a cheat code to test access control:

```solidity
function testUnauthorizedAccess() public {
    // Setup: Deploy the DistributionContract
    DistributionContract distributionContract = new DistributionContract(...);

    // Use cheat codes to simulate an unauthorized user
    vm.prank(address(0x123));
    vm.expectRevert("Unauthorized access");

    // Attempt to call a function that requires specific permissions
    distributionContract.someFunctionRequiringAuthorization();
}

### Running Tests

Execute your tests using the following command:

```bash
forge test
```

### Best Practices

* Write clear, descriptive test cases.
* Maintain code readability.
* Use Foundry cheat codes for simulating real-world scenarios.
* Aim for high test coverage.

### Conclusion

Testing ensures the reliability and security of blockchain contracts. This guide provides a foundational approach for using Foundry to test the `DistributionContract`.

### Further Resources

* [Foundry Book](https://foundry.readthedocs.io)

---

<a id="doc_32"></a>

## 📁 protocol/examples / Advertisement Auction DApp

*파일 경로: protocol/examples/example1.mdx*

---
sidebar_position: 1
---

import GdaSuperVis from '@site/src/components/Visualizations/GdaSuperExampleVis';
import Admonition from '@theme/Admonition';
import CodeBlock from '@theme/CodeBlock';


This guide explores the development of a decentralized application (DApp) for an advertisement auction system, leveraging the capabilities of Superfluid's [Distribution Pools](docs/protocol/distributions/guides/pools.mdx) (also called the *General Distributions Agreement - GDA*).

### Overview

In the ever-evolving landscape of digital advertising, there's a need for more dynamic and efficient systems. Traditional models often involve complex, non-transparent payment structures and lack real-time interaction capabilities. Our DApp aims to address these challenges by using Distributions from Superfluid Protocol for seamless transactions and fair distribution of advertising revenues.

This example addresses the following Superfluid Protocol features:

- [Money Streaming](/docs/protocol/money-streaming/overview)
- [Distribution Pools](/docs/protocol/distributions/guides/pools)
- [Super Apps](/docs/protocol/advanced-topics/super-apps/deploy-a-super-app)

:::tip Check out the full codebase
For the complete implementation of the DApp, including the smart contract and foundry test, refer to the [GitHub repository](https://github.com/superfluid-finance/ad-auction-example).
:::

#### The Problem

The main challenges in current digital advertising models include:

1. **Lack of Transparency**: Difficulty in tracking funds and understanding distribution mechanisms.
2. **Inefficient Payment Systems**: Cumbersome processes for handling and distributing advertising revenue.
3. **Static Advertisement Bidding**: Traditional models don't allow real-time bidding, leading to less engagement and fairness.


#### Our Solution

Our DApp introduces a novel approach to advertisement auctioning:

- **Continuous Funds Stream**: Utilizing Superfluid's money streaming concept, funds flow continuously into a distribution pool.
- **Dynamic Advertisement Auctioning**: Advertisers bid for ad space in real-time through streaming payments, creating an engaging and fair auction system.
- **Proportional Distribution**: Funds are distributed between the DApp owner and previous advertisers based on their advertising duration, ensuring fair compensation.

<div style={{ display: 'flex', justifyContent: 'center' }}>
<GdaSuperVis/>
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Visualization of our advertisement auction app mechanism*</p>
</div>

:::note
In the visualization above we see how the previous streamer joins the pool to become a new member and get money streamed to him
:::

#### Smart Contract Structure

The `AdSpotContract` is at the heart of our DApp, built on Ethereum and integrated with Superfluid Protocol. It encompasses:

- **Pool Creation and Management**: Facilities for users to create and administer distribution pools.
- **Auction Mechanism**: Mechanisms for real-time bidding and advertisement space allocation.
- **Fund Distribution Logic**: Automated and transparent distribution of funds between DApp owners and advertisers.
- **Superfluid Integration**: Leveraging Superfluid's GDA for efficient streaming of funds.

In the following sections, we'll delve deeper into each aspect of the DApp, providing insights into the smart contract functionalities, implementation guide, and UI/UX considerations.

<Admonition type="note">
This guide is intended for blockchain developers and assumes familiarity with Ethereum smart contract development and minimal familiarity with the concept of [Distribution Pools](/docs/protocol/distributions/guides/pools.mdx).
</Admonition>

### Smart Contract Implementation

The [`AdSpotContract`](https://github.com/superfluid-finance/ad-auction-example/blob/master/src/AdSpotContract.sol) plays a crucial role in our DApp, integrating Superfluid's streaming capabilities for an innovative advertisement auction system. Let's dive into the key components and functionalities of this smart contract.

#### Contract Overview

This guide demonstrates how to use the Superfluid Protocol's [Distribution Pools](/docs/protocol/distributions/guides/pools.mdx) (also known as the GDA in our codebase) to develop a decentralized application (DApp) for advertisement auctioning. We'll walk through the key components of the `AdSpotContract`.

### Contract Initialization

The `AdSpotContract` is initialized with necessary Superfluid interfaces and parameters. Here's a look at the constructor:

```solidity
constructor(ISuperToken _acceptedToken)
    CFASuperAppBase(ISuperfluid(_acceptedToken.getHost()))
{
    // Contract initialization code
}
```

This constructor sets up the Superfluid context and initializes the fund distribution pool.

### Real-Time Auctioning Logic

The contract employs callback functions to manage auction logic. Here's an example of a callback function handling new flow creation:

```solidity
function onFlowCreated(
    ISuperToken /*superToken*/,
    address sender,
    bytes calldata ctx
) internal override returns (bytes memory newCtx) {
    // Logic for handling new flow creation
}
```

These functions are crucial for updating the highest bidder and managing the distribution of shares.

### NFT Showcase Feature

The contract also includes a feature for the highest bidder to showcase an NFT:

```solidity
function setNftToShowcase(address _nftAddress, uint256 _tokenId) external {
    // NFT showcase logic
}
```

This feature adds interactivity to the advertisement space, allowing for dynamic content display.

### Getters for Contract State

Various getter functions provide important information about the contract's state:

```solidity
function getHighestBidder() public view returns (address) {
    // Logic to retrieve the highest bidder
}
```

These functions are essential for users to interact with and understand the contract's current state.

<Admonition type="info">

For a complete code base and tests of the `AdSpotContract`, refer to the [full contract code](https://github.com/superfluid-finance/ad-auction-example/).

</Admonition>

### Conclusion

This guide provided a high-level overview of the `AdSpotContract` used in a DApp for advertisement auctioning with Superfluid. The contract demonstrates a real-time auction mechanism, a dynamic NFT showcase feature, and efficient fund distribution using Superfluid's streaming capabilities.

---

<a id="doc_33"></a>

## 📁 protocol/examples / Staking Platform

*파일 경로: protocol/examples/example2.mdx*

---
sidebar_position: 2
---

import StakingContract from '@site/src/components/StakingContract';


This guide explores the development of a staking platform, leveraging the capabilities of Superfluid's [Distribution Pools](/docs/protocol/distributions/guides/pools.mdx) (also called the *General Distributions Agreement - GDA*).


<StakingContract/>


### Repository

The contract and associated tests can be found in the [SuperfluidStaking Repository](https://github.com/superfluid-finance/sf-example-staking).

### Contract Architecture

The SuperfluidStaking system consists of two main contracts:

1. **SuperfluidStaking**: The core contract that manages staking, unstaking, and reward distribution.
2. **ClaimContract**: An auxiliary contract created for each staker to manage their individual rewards.

#### SuperfluidStaking Contract

This contract is responsible for:

- Accepting stakes from users
- Managing the total staked amount
- Creating and upgrading Super Tokens for rewards
- Creating and managing a Superfluid pool for reward distribution
- Handling the unstaking process
- Facilitating reward claims

Key components:

- `underlyingStakedToken`: The ERC20 token that users stake
- `underlyingRewardsToken`: The ERC20 token used for rewards
- `superToken`: The Super Token wrapper for the rewards token
- `pool`: The Superfluid pool used for distributing rewards
- `scalingFactor`: A factor used to scale down staked amounts for precision

#### ClaimContract

This contract is created for each staker and is responsible for:

- Claiming rewards from the Superfluid pool
- Holding claimed rewards until withdrawn by the staker

### Setup and Installation

To set up the development environment and run the tests, follow these steps:

1. **Install Foundry**

   Foundry is a blazing fast, portable and modular toolkit for Ethereum application development. To install Foundry, run the following command:

   ```bash
   curl -L https://foundry.paradigm.xyz | bash
   ```

   Then, run `foundryup` in a new terminal session to install the latest version.

2. **Clone the repository**

   ```bash
   git clone https://github.com/superfluid-finance/sf-example-staking
   cd superfluid-staking
   ```

3. **Install dependencies**

   Use Forge to install the necessary dependencies:

   ```bash
   forge install
   ```

   This will install OpenZeppelin contracts and Superfluid contracts as specified in the `foundry.toml` file.

4. **Compile the contracts**

   ```bash
   forge build
   ```

5. **Run the tests**

   ```bash
   forge test
   ```

   This will run all the test cases defined in the `test` directory.

### Contract Interaction Flow

1. **Deployment**: The contract is deployed with parameters for the staked token, rewards token, Superfluid token factory, and scaling factor.

2. **Supplying Funds**: The contract owner calls `supplyFunds` to add rewards to the pool.

3. **Staking**: Users call `stake` to deposit tokens. This creates a ClaimContract if they don't have one and updates their units in the Superfluid pool.

4. **Unstaking**: Users call `unstake` to withdraw their staked tokens. This updates their units in the Superfluid pool.

5. **Claiming Rewards**: Users call `claimRewards` to receive their accumulated rewards. This interacts with their ClaimContract to fetch and distribute rewards.

### Key Considerations

- The use of a scaling factor is crucial for maintaining precision in reward calculations, especially when dealing with tokens of different decimals.
- The ClaimContract pattern allows for efficient reward claiming without requiring frequent updates to the main contract.
- The contract leverages Superfluid's streaming capabilities for continuous and gas-efficient reward distribution.

### Testing

The test suite (located in `test/SuperfluidStaking.t.sol`) covers various scenarios including:

- Staking and unstaking
- Reward distribution and claiming
- Multiple users interacting with the contract
- Edge cases and potential vulnerabilities

To run a specific test:

```bash
forge test --match-test testFunctionName
```

Replace `testFunctionName` with the name of the test function you want to run.

### Conclusion

The SuperfluidStaking contract provides a robust and efficient system for stake-based reward distribution using Superfluid.
By following this guide, you should be able to understand the contract's architecture, set up your development environment, and run the tests.

---

<a id="doc_34"></a>

## 📁 protocol/money-streaming / Money Streaming in Superfluid

*파일 경로: protocol/money-streaming/overview.mdx*

---
sidebar_position: 1
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';


Money Streaming, previously known as Constant Flow Agreement (CFA), revolutionizes the movement of tokens with a by-the-second transfer mechanism. This page provides an in-depth overview of Money Streaming and the unique aspects of Flow NFTs in the Superfluid ecosystem.

### What is Money Streaming?

Money Streaming allows for continuous, per-second token transfers between accounts, offering a dynamic and flexible approach to token distribution.

#### Key Characteristics

- **Perpetual Transfers**: Streams continue until canceled by the sender or the sender's balance depletes.
- **Flexible Management**: Streams can be created, updated, or deleted at any time by the sender.

For a more conceptual breakdown, refer to the [detailed Money Streaming overview](/docs/protocol/money-streaming/overview.mdx).

### Flows and Flow Rates

Money Streaming in Superfluid introduces the concepts of flows and flow rates, key elements for managing the continuous movement of tokens. This section defines these concepts and explains how to calculate flow rates accurately.

Flows in Superfluid represent the continuous, per-second movement of tokens between accounts. They are defined by their flow rate and can be dynamically managed by the sender.

:::tip

You may have a hard time seeing the difference between "Flows" and "Streams". This is a feature, not a bug. The key difference is the following: Flows can be equal to 0, while Streams need to be strictly positive.

:::

Flows have the following Characteristics:

- **Perpetual**: Flows continue until the sender decides to cancel or the balance depletes.
- **Flexible**: Flows can be created, updated, or stopped at any time.

#### Calculating Flow Rates


Flow rates dictate the speed at which tokens are transferred per second. Superfluid requires these rates to be specified in wei per second.

It's crucial to translate your desired flow rate into wei per second accurately. Incorrect calculations can lead to discrepancies between expected and actual flow rates as displayed on the Superfluid Dashboard and Explorer.

<Admonition type="info" title="Flow Rate Conversion">

Flow rates can be reframed from larger time denominations like months or years into wei per second. Understand the conversion process to accurately determine the wei/second rate for your flows.

</Admonition>

#### Calculation Examples

##### From Month to Wei/Second

- **Monthly Rate**: 10 DAIx/month.
- **Calculation**: 10 DAIx / ((365/12) * 24 * 60 * 60) = 3805175038052 wei/second.

##### From Year to Wei/Second

- **Yearly Rate**: 100 DAIx/year.
- **Calculation**: 100 DAIx / (365 * 24 * 60 * 60) = 3170979198376 wei/second.

<Admonition type="warning" title="Calculation Precision">

Using an approximate number of days in a month (like 30 days) for calculations can lead to slightly inaccurate wei/second rates, affecting how the rate appears on Superfluid interfaces.

</Admonition>

This section provides a clear understanding of flows and flow rates within the Superfluid Money Streaming, enabling users to accurately manage and interpret their token streams.

---

<a id="doc_35"></a>

## 📁 protocol/money-streaming/examples / FlowSplitter Smart Contract

*파일 경로: protocol/money-streaming/examples/example1.mdx*

---
sidebar_position: 1
---


This guide provides an overview and usage instructions for the `FlowSplitter` smart contract, which leverages the Superfluid protocol to route incoming streams of Super Tokens to two different recipients based on predefined proportions.

### Introduction

The `FlowSplitter` contract is designed to automatically split incoming Super Token streams to a main and a side receiver. This splitting is determined by the `sideReceiverPortion` parameter, which defines the percentage of the incoming flow to be routed to the side receiver, with the remainder going to the main receiver.

### Contract Overview

<img src="/assets/diagram.png" alt="FlowSplitter Diagram"/>


The above diagram illustrates how the `FlowSplitter` works. For example, if the `sideReceiverPortion` is set to 30%, then 30% of all incoming Super Token streams will be routed to the side receiver, and the remaining 70% will go to the main receiver.

<div>
<details>
<summary>Click here to show `FlowSender` contract</summary>
<p>

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.18;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

import {SuperTokenV1Library} from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";
import {SuperAppBaseFlow} from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperAppBaseFlow.sol";
import {
    ISuperfluid,
    ISuperToken
} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";

/// @title FlowSplitter
/// @author Superfluid | Modified by @0xdavinchee
/// @dev A negative sideReceiverPortion portion is not allowed
/// A portion > 1000 is fine though because the protocol will
/// revert when trying to create a flow with a negative flow rate
/// A flowRate which is less than 1000 will be rounded down to 0 and will revert
/// Also an inflow which does not contain a whole number will be rounded down,
/// this will also lead to a revert.
contract FlowSplitter is SuperAppBaseFlow {
    using SuperTokenV1Library for ISuperToken;

    /// @dev Account that ought to be routed the majority of the inflows
    address public immutable MAIN_RECEIVER;

    /// @dev Account that ought to be routed the minority of the inflows
    address public immutable SIDE_RECEIVER;

    /// @dev Account that deployed the contract
    address public immutable CREATOR;

    /// @dev Super Token that the FlowSplitter will accept streams of
    ISuperToken public immutable ACCEPTED_SUPER_TOKEN;

    /// @dev number out of 1000 representing portion of inflows to be redirected to SIDE_RECEIVER
    ///      Ex: 300 would represent 30%
    int96 public sideReceiverPortion;

    error INVALID_PORTION();
    error SAME_RECEIVERS_NOT_ALLOWED();
    error NO_SELF_FLOW();
    error NOT_CREATOR();

    /// @dev emitted when the split of the outflow to MAIN_RECEIVER and SIDE_RECEIVER is updated
    event SplitUpdated(int96 mainReceiverPortion, int96 newSideReceiverPortion);

    constructor(
        ISuperfluid host_,
        ISuperToken acceptedSuperToken_,
        address creator_,
        address mainReceiver_,
        address sideReceiver_,
        int96 sideReceiverPortion_
    ) SuperAppBaseFlow(host_, true, true, true) {
        if (sideReceiverPortion_ <= 0 || sideReceiverPortion_ == 1000) revert INVALID_PORTION();
        if (mainReceiver_ == sideReceiver_) revert SAME_RECEIVERS_NOT_ALLOWED();
        if (mainReceiver_ == address(this) || sideReceiver_ == address(this)) revert NO_SELF_FLOW();

        ACCEPTED_SUPER_TOKEN = acceptedSuperToken_;
        CREATOR = creator_;
        MAIN_RECEIVER = mainReceiver_;
        SIDE_RECEIVER = sideReceiver_;
        sideReceiverPortion = sideReceiverPortion_;
    }

    /// @dev checks that only the acceptedToken is used when sending streams into this contract
    /// @param superToken_ the token being streamed into the contract
    function isAcceptedSuperToken(ISuperToken superToken_) public view override returns (bool) {
        return superToken_ == ACCEPTED_SUPER_TOKEN;
    }

    /// @notice Returns the outflow rates to main and side receiver given flowRate_ and an arbitrary
    /// sideReceiverPortion_
    /// @dev If either returns 0, it will revert when trying to create a flow
    ///     because the protocol does not allow creating flows with a flow rate of 0
    ///     Also, if the sum of the two outflows is not equal to the inflow, it means the app will
    ///     receive a residual flow.
    /// @param flowRate_ the inflow rate
    /// @param sideReceiverPortion_ the portion of the inflow to be redirected to SIDE_RECEIVER
    /// @return mainFlowRate the outflow rate to MAIN_RECEIVER
    /// @return sideFlowRate the outflow rate to SIDE_RECEIVER
    /// @return residualFlowRate the residual flow rate
    function getMainAndSideReceiverFlowRates(int96 flowRate_, int96 sideReceiverPortion_)
        external
        pure
        returns (int96 mainFlowRate, int96 sideFlowRate, int96 residualFlowRate)
    {
        mainFlowRate = (flowRate_ * (1000 - sideReceiverPortion_)) / 1000;
        sideFlowRate = (flowRate_ * sideReceiverPortion_) / 1000;
        residualFlowRate = flowRate_ - (mainFlowRate + sideFlowRate);
    }

    /// @notice Updates the split of the outflow to MAIN_RECEIVER and SIDE_RECEIVER
    /// @dev Only the creator should be able to call update split.
    /// @param newSideReceiverPortion_ the new portion of inflows to be redirected to SIDE_RECEIVER
    function updateSplit(int96 newSideReceiverPortion_) external {
        if (newSideReceiverPortion_ <= 0 || newSideReceiverPortion_ >= 1000) revert INVALID_PORTION();
        if (msg.sender != CREATOR) revert NOT_CREATOR();

        sideReceiverPortion = newSideReceiverPortion_;

        // get current outflow rate
        int96 totalOutflowRate = ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), MAIN_RECEIVER)
            + ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), SIDE_RECEIVER);

        int96 mainReceiverPortion = 1000 - newSideReceiverPortion_;

        // update outflows
        // @note there is a peculiar bug here where you can't change the outflow in any way
        ACCEPTED_SUPER_TOKEN.updateFlow(MAIN_RECEIVER, (totalOutflowRate * mainReceiverPortion) / 1000);
        ACCEPTED_SUPER_TOKEN.updateFlow(SIDE_RECEIVER, (totalOutflowRate * newSideReceiverPortion_) / 1000);

        emit SplitUpdated(mainReceiverPortion, newSideReceiverPortion_);
    }

    // ---------------------------------------------------------------------------------------------
    // CALLBACK LOGIC

    function onFlowCreated(ISuperToken superToken_, address sender_, bytes calldata ctx_)
        internal
        override
        returns (bytes memory newCtx)
    {
        newCtx = ctx_;

        // get inflow rate from sender_
        int96 inflowRate = superToken_.getFlowRate(sender_, address(this));

        // if there's no outflow already, create outflows
        if (superToken_.getFlowRate(address(this), MAIN_RECEIVER) == 0) {
            newCtx =
                superToken_.createFlowWithCtx(MAIN_RECEIVER, (inflowRate * (1000 - sideReceiverPortion)) / 1000, newCtx);

            newCtx = superToken_.createFlowWithCtx(SIDE_RECEIVER, (inflowRate * sideReceiverPortion) / 1000, newCtx);
        }
        // otherwise, there's already outflows which should be increased
        else {
            newCtx = superToken_.updateFlowWithCtx(
                MAIN_RECEIVER,
                ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), MAIN_RECEIVER)
                    + (inflowRate * (1000 - sideReceiverPortion)) / 1000,
                newCtx
            );

            newCtx = superToken_.updateFlowWithCtx(
                SIDE_RECEIVER,
                ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), SIDE_RECEIVER)
                    + (inflowRate * sideReceiverPortion) / 1000,
                newCtx
            );
        }
    }

    function onFlowUpdated(
        ISuperToken superToken_,
        address sender_,
        int96 previousFlowRate_,
        uint256, /*lastUpdated*/
        bytes calldata ctx_
    ) internal override returns (bytes memory newCtx) {
        newCtx = ctx_;

        // get inflow rate change from sender_
        int96 inflowChange = superToken_.getFlowRate(sender_, address(this)) - previousFlowRate_;

        // update outflows
        newCtx = superToken_.updateFlowWithCtx(
            MAIN_RECEIVER,
            ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), MAIN_RECEIVER)
                + (inflowChange * (1000 - sideReceiverPortion)) / 1000,
            newCtx
        );

        newCtx = superToken_.updateFlowWithCtx(
            SIDE_RECEIVER,
            ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), SIDE_RECEIVER) + (inflowChange * sideReceiverPortion) / 1000,
            newCtx
        );
    }

    function onFlowDeleted(
        ISuperToken superToken_,
        address, /*sender_*/
        address receiver_,
        int96 previousFlowRate_,
        uint256, /*lastUpdated*/
        bytes calldata ctx_
    ) internal override returns (bytes memory newCtx) {
        newCtx = ctx_;

        // remaining inflow is equal to total outflow less the inflow that just got deleted
        int96 remainingInflow = (
            ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), MAIN_RECEIVER)
                + ACCEPTED_SUPER_TOKEN.getFlowRate(address(this), SIDE_RECEIVER)
        ) - previousFlowRate_;

        // handle "rogue recipients" with sticky stream - see readme
        if (receiver_ == MAIN_RECEIVER || receiver_ == SIDE_RECEIVER) {
            newCtx = superToken_.createFlowWithCtx(receiver_, previousFlowRate_, newCtx);
        }

        // if there is no more inflow, outflows should be deleted
        if (remainingInflow <= 0) {
            newCtx = superToken_.deleteFlowWithCtx(address(this), MAIN_RECEIVER, newCtx);

            newCtx = superToken_.deleteFlowWithCtx(address(this), SIDE_RECEIVER, newCtx);
        }
        // otherwise, there's still inflow left and outflows must be updated
        else {
            newCtx = superToken_.updateFlowWithCtx(
                MAIN_RECEIVER, (remainingInflow * (1000 - sideReceiverPortion)) / 1000, newCtx
            );

            newCtx =
                superToken_.updateFlowWithCtx(SIDE_RECEIVER, (remainingInflow * sideReceiverPortion) / 1000, newCtx);
        }
    }
}
```

</p>
</details>
</div>

### Key Components

- **`MAIN_RECEIVER`:** The primary account that receives the majority of the inflows.
- **`SIDE_RECEIVER`:** The secondary account that receives a smaller, specified portion of the inflows.
- **`ACCEPTED_SUPER_TOKEN`:** The specific Super Token that the `FlowSplitter` will accept for streaming.
- **`sideReceiverPortion`:** A numerical value representing the portion (out of 1000) of inflows redirected to the `SIDE_RECEIVER`.

### Usage

#### Deploying the Contract

To deploy the `FlowSplitter`, you must specify the following parameters:

- `host_`: The Superfluid host contract.
- `acceptedSuperToken_`: The Super Token to be accepted by the contract.
- `creator_`: The address of the account deploying the contract.
- `mainReceiver_`: The address of the main receiver.
- `sideReceiver_`: The address of the side receiver.
- `sideReceiverPortion_`: The initial portion of the inflow to be directed to the side receiver.

#### Updating the Flow Split

The creator of the contract can update the flow split by calling the `updateSplit` function with a new `sideReceiverPortion_`. This adjusts the outflow rates to both receivers accordingly.

```solidity
function updateSplit(int96 newSideReceiverPortion_) external;
```

#### Calculating Flow Rates

To calculate the exact outflow rates for the main and side receivers based on any inflow rate and `sideReceiverPortion`, use the `getMainAndSideReceiverFlowRates` function:

```solidity
function getMainAndSideReceiverFlowRates(
    int96 flowRate_,
    int96 sideReceiverPortion_
) external pure returns (
    int96 mainFlowRate,
    int96 sideFlowRate,
    int96 residualFlowRate
);
```

#### Handling Streams

The contract includes several internal callback functions that handle the creation, updating, and deletion of streams:

* `onFlowCreated`: Called when a new inflow to the `FlowSplitter` is created.
* `onFlowUpdated`: Called when an existing inflow to the `FlowSplitter` is updated.
* `onFlowDeleted`: Called when an inflow to the `FlowSplitter` is deleted.

### Conclusion

The `FlowSplitter` smart contract offers a robust solution for automatically splitting incoming Super Token streams. By setting the `sideReceiverPortion`, users can determine the flow rates to different parties, enabling a fair and transparent distribution of funds.

---

<a id="doc_36"></a>

## 📁 protocol/money-streaming/guides / Control Flows

*파일 경로: protocol/money-streaming/guides/create-update-delete-flow.mdx*

---
sidebar_position: 1
---


This guide covers various methods for managing flows directly on the Superfluid protocol. It includes creating, updating, and deleting flows, **on chain, from another smart contracts**.
This guide does NOT cover:
- How to create a flow by an operator on behalf of another account. For that, please refer to the [ACL and User Data guide](/docs/protocol/money-streaming/guides/acl-user-data).
- How to manage flows with user data. For that, please refer to the [ACL and User Data guide](/docs/protocol/money-streaming/guides/acl-user-data).
- How to create flows by interacting with the Money Streaming Forwarder contract from client applications. For that please refer to the [SDK section](/docs/sdk/money-streaming/create-update-delete-flow).

### Prerequisites

Before proceeding, ensure you have:

- Familiarity with Solidity.
- Basic understanding of Superfluid and its functionalities.
- Access to a development environment for deploying or interacting with Smart Contracts.
- Importing the SuperTokenV1Library in your smart contract. For more details, refer to the [Using the SuperTokenV1Library](/docs/protocol/super-tokens/guides/using-library).

### What is a flow?
In Superfluid terminology, a flow is a continuous stream of tokens from one account to another.
It is a fundamental concept in the Superfluid protocol, enabling real-time, continuous payments between accounts.

:::tip What is the difference between a "Stream" and a "Flow"?
This is a small technicality which is not necessarily important to understand.
However, in Superfluid, a "Flow" is a more general term than a "Stream".
A Stream is a non-zero flow, while a zero flow is not considered a Stream.
:::

### Set the flowrate

#### Function `flow`

This function sets the specified flowrate between sender and receiver.

```solidity
/**
    * @dev Sets the given CFA flowrate between the caller and a given receiver.
    * If there's no pre-existing flow and `flowRate` non-zero, a new flow is created.
    * If there's an existing flow and `flowRate` non-zero, the flowRate of that flow is updated.
    * If there's an existing flow and `flowRate` zero, the flow is deleted.
    * If the existing and given flowRate are equal, no action is taken.
    * On creation of a flow, a "buffer" amount is automatically detracted from the sender account's available balance.
    * If the sender account is solvent when the flow is deleted, this buffer is redeemed to it.
    * @param token Super token address
    * @param receiver The receiver of the flow
    * @param flowRate The wanted flowrate in wad/second. Only positive values are valid here.
    * @return bool
    */
function flow(ISuperToken token, address receiver, int96 flowRate)
    internal returns (bool)
```

:::note when not using the lib
The CFAv1Forwarder contract has a function called `setFlowrate` which does the same.
:::

### CRUD methods

If you want to be more explicit when changing the state of flows, you can use the following CRUD methods:

#### Function: `createFlow`

To create a flow, you need to call `createFlow` by specifying the token, sender, receiver, and flow rate.

```solidity
/**
 * @dev Create flow
 * @param token The token used in flow
 * @param receiver The receiver of the flow
 * @param flowRate The desired flowRate
 */
function createFlow(ISuperToken token, address receiver, int96 flowRate)
    internal returns (bool)
```

#### Function: `updateFlow`

For an existing flow, you can update the flow rate through the `updateFlow` function.

```solidity
/**
 * @dev Update flow
 * @param token The token used in flow
 * @param receiver The receiver of the flow
 * @param flowRate The desired flowRate
 */
function updateFlow(ISuperToken token, address receiver, int96 flowRate)
    internal returns (bool)
```

#### Function: `deleteFlow`

To delete an existing, you need to call `deleteFlow` and  specify the token, sender, and receiver.

```solidity
/**
 * @dev Delete flow without userData
 * @param token The token used in flow
 * @param sender The sender of the flow
 * @param receiver The receiver of the flow
 */
function deleteFlow(ISuperToken token, address sender, address receiver)
    internal returns (bool)
```

:::warning Can I update or delete a non-existent flow?
No, you cannot update or delete a non-existent flow. If a flow does not exist, the function will revert.
:::

:::tip Full list of functions
For a full list of functions related to creating, updating, and deleting flows, refer to the [SuperTokenV1Library technical reference](/docs/technical-reference/SuperTokenV1Library).
:::

### Example: Control Flows

For this example, we'll use the `FlowSender` contract described in the [Quickstart](/docs/protocol/quickstart.mdx) as our example to demonstrate how to write a contract with creates, updates, deletes and reads flow data.

<div>
<details>
<summary>Click here to show `FlowSender` contract</summary>
<p>

```solidity
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import { ISuperfluid, ISuperToken } from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";
import { SuperTokenV1Library } from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";

interface IFakeDAI is IERC20 {
    function mint(address account, uint256 amount) external;
}

contract FlowSender {
    using SuperTokenV1Library for ISuperToken;

    mapping (address => bool) public accountList;
    ISuperToken public daix;

    // fDAIx address on Polygon Mumbai = 0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f
    constructor(ISuperToken _daix) {
        daix = _daix;
    }

    /// @dev Mints 10,000 fDAI to this contract and wraps it all into fDAIx
    function gainDaiX() external {

        // Get address of fDAI by getting underlying token address from DAIx token
        IFakeDAI fdai = IFakeDAI( daix.getUnderlyingToken() );

        // Mint 10,000 fDAI
        fdai.mint(address(this), 10000e18);

        // Approve fDAIx contract to spend fDAI
        fdai.approve(address(daix), 20000e18);

        // Wrap the fDAI into fDAIx
        daix.upgrade(10000e18);
    }

    /// @dev controls a stream with the given flowrate between this contract and the desired receiver
    function setStream(address receiver, int96 flowRate) external {
        daix.flow(receiver, flowRate);
    }

    /// @dev get flow rate between this contract and the given receiver
    function getFlowRate(address receiver) external view returns (int96 flowRate) {
        return daix.getFlowRate(address(this), receiver);
    }
}
```

</p>
</details>
</div>

This contract has a few functions:

- **gainDaiX**: Mints and wraps fDAI into fDAIx (Superfluid's wrapped token).
- **setStream**: Controls a stream between the contract and a receiver
- **getFlowRate**: Reads the current flow rate of a stream.

:::tip About the `SuperTokenV1Library`
As you can see, the `FlowSender` contract uses the [`SuperTokenV1Library`](/docs/technical-reference/SuperTokenV1Library) to interact with the Superfluid protocol.
Instead of passing the token address to the functions, the contract uses `using SuperTokenV1Library for ISuperToken;` to access the functions directly.
You can learn more about how to use the `SuperTokenV1Library` in the [Using the SuperTokenV1Library](/docs/protocol/super-tokens/guides/using-library) guide.
:::

---

<a id="doc_37"></a>

## 📁 protocol/money-streaming/guides / Manage Access Control and User Data

*파일 경로: protocol/money-streaming/guides/acl-user-data.mdx*

---
sidebar_position: 2
---


This page provides an overview of how to manage access control and user data in the Superfluid protocol.
We will show how to use the [SuperTokenV1Library](/docs/technical-reference/SuperTokenV1Library) to interact with the protocol and demonstrate how to grant permissions, create flows,
and attach user data to transactions within your smart contracts.

### Introduction to SuperTokenV1Library

The [SuperTokenV1Library](/docs/technical-reference/SuperTokenV1Library) is the primary interface for developers to interact with the Superfluid protocol when building smart contracts on-chain.
It provides a comprehensive set of tools for working with [Money Streaming](/docs/protocol/money-streaming/overview) (*Constant Flow Agreement - CFA*) and [Distribution Pools](/docs/protocol/distributions/overview) (*General Distributions Agreement - GDA*).

To use the SuperTokenV1Library in your smart contract:

1. Import the library:
   ```solidity
   import "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";
   ```

2. Include the `using` statement:
   ```solidity
   using SuperTokenV1Library for ISuperToken;
   ```

:::tip Learn more about the SuperTokenV1Library
For more details on the SuperTokenV1Library, refer to the page [Using the SuperTokenV1Library](/docs/protocol/super-tokens/guides/using-library). For a full list of its functions, refer to its [technical reference](/docs/technical-reference/SuperTokenV1Library).
:::

### Access Control in Superfluid

Access control is a crucial aspect of smart contract security, allowing certain addresses to perform specific actions.
In the context of Superfluid and money streaming, Access Control Lists (ACLs) enables one address (the Flow Operator) to manage streams on behalf of another address.

#### How Access Control Works in Superfluid

Superfluid implements a flexible permission system for flow management:

1. **Granting Permissions**: An account can grant permissions to a flow operator, specifying what actions they can perform (create, update, delete flows) and setting a flow rate allowance.

2. **Flow Rate Allowance**: This is the maximum net flow rate that the operator can create on behalf of the account.

3. **Operator Actions**: Once granted permissions, the operator can perform the allowed actions within the specified flow rate allowance.

:::tip Access Control for [Distribution Pools](/docs/protocol/distributions/overview)
In this document, we address Access Control for Money Streaming (CFA). Currently, there are no access control functions for [Distribution Pools](/docs/protocol/distributions/overview). However, you can build your own access control system using the SuperTokenV1Library functions.
:::

#### Key Functions for Access Control

1. `setFlowPermissions`: Set specific permissions for a flow operator.

```solidity
function setFlowPermissions(
    ISuperToken token,
    address flowOperator,
    bool allowCreate,
    bool allowUpdate,
    bool allowDelete,
    int96 flowRateAllowance
) internal returns (bool)
```

2. `flowFrom`: Control a flow as an operator on behalf of another account.

```solidity
function flowFrom(
    ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate
) internal returns (bool)
```

3. `revokeFlowPermissions`: Revoke all permissions from a flow operator.

```solidity
function revokeFlowPermissions(
    ISuperToken token,
    address flowOperator
) internal returns (bool)
```

:::tip Full list of functions
For a full list of functions related to access control, refer to the [SuperTokenV1Library technical reference](/docs/technical-reference/SuperTokenV1Library).
:::

### User Data in Superfluid

User data in Superfluid allows developers to attach additional information to transactions. This can be used for various purposes, such as including metadata, triggering specific logic in receiver contracts, or implementing off-chain systems.

#### How to Use User Data

Many functions in the SuperTokenV1Library accept a `userData` parameter. This is typically a `bytes` type, allowing you to encode any data you want to include.

Example of using user data when controlling a flow:

```solidity
function flowFrom(
    ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes memory userData
) internal returns (bool)
```

You can encode various types of data into the `userData` parameter. For example:

```solidity
bytes memory userData = abi.encode(uint256(1234), "Hello, Superfluid!");
createFlowWithUserData(token, receiver, flowRate, userData);
```

### Example: Granting Permissions and Creating a Flow

Here's a simple example demonstrating how one contract can grant permissions to another, allowing it to create a flow on its behalf:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { ISuperfluid, ISuperToken } from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";
import { SuperTokenV1Library } from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";

contract PermissionGranter {
    using SuperTokenV1Library for ISuperToken;

    function grantPermissions(
        ISuperToken token,
        address operator,
        int96 flowRateAllowance
    ) external {
        token.setFlowPermissions(
            operator,
            true, // allowCreate
            false, // allowUpdate
            false, // allowDelete
            flowRateAllowance
        );
    }
}

contract FlowCreator {
    using SuperTokenV1Library for ISuperToken;

    function createFlowAsOperator(
        ISuperToken token,
        address sender,
        address receiver,
        int96 flowRate
    ) external {
        token.flowFrom(sender, receiver, flowRate);
    }
}
```

In this example, `PermissionGranter` can grant permissions to `FlowCreator`. Once permissions are granted, `FlowCreator` can create flows on behalf of the address that called `grantPermissions`.

To use these contracts:

1. Deploy both contracts.
2. Call `grantPermissions` on `PermissionGranter`, passing the token address, the address of the `FlowCreator` contract, and the desired flow rate allowance.
3. Now, anyone can call `createFlowAsOperator` on `FlowCreator`, which will create a flow from the address that granted permissions to the specified receiver.

This setup allows for flexible delegation of flow creation, which can be useful in various DeFi applications, automated systems, or multi-sig wallet scenarios.

---

<a id="doc_38"></a>

## 📁 protocol/money-streaming/guides / Testing

*파일 경로: protocol/money-streaming/guides/testing.mdx*

---
sidebar_position: 4
---

import TabItem from "@theme/TabItem";
import Tabs from "@theme/Tabs";


In this guide, we'll walk through the process of testing a Superfluid contract using the Foundry framework. We'll use the `FlowSender` contract described in the [Quickstart](/docs/protocol/quickstart.mdx) as our example to demonstrate how to write effective tests.

### Prerequisites

Before diving into testing your Superfluid contracts with Foundry, make sure you have set up your development environment properly. Here's a brief explanation of each step required:

1. **Creating and Navigating to Your Project Directory**:

   ```bash
   mkdir superfluid-example && cd superfluid-example
   ```

   This command creates a new directory named `foundry-example` and then changes your current working directory to it.

2. **Initializing a Foundry Project**:

   ```bash
   forge init
   ```

   This initializes a new Foundry project in your directory, setting up the necessary structure and configuration for Ethereum smart contract development.

3. **Installing Superfluid Protocol Dependencies**:

   ```bash
   forge install superfluid-protocol-monorepo=https://github.com/superfluid-finance/protocol-monorepo --no-commit
   ```

   Installs the `dev` branch of the Superfluid protocol from its GitHub repository.

4. **Installing OpenZeppelin Contracts**:

   ```bash
   forge install https://github.com/OpenZeppelin/openzeppelin-contracts@v4.9.6 --no-commit
   ```

   Installs the necessary (4.9.X) of the OpenZeppelin contracts, which are widely used for secure smart contract development.

These steps ensure you have the necessary tools and dependencies installed to start developing and testing your Superfluid-based contracts with Foundry.

### Contract and Key Functions

<div>
<details>
<summary>Click here to show `FlowSender` contract</summary>
<p>

```solidity
//SPDX-License-Identifier: Unlicensed
pragma solidity ^0.8.14;

import { ISuperfluid, ISuperToken } from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";

import { SuperTokenV1Library } from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// For deployment on Mumbai Testnet

interface IFakeDAI is IERC20 {

    function mint(address account, uint256 amount) external;

}

contract FlowSender {

    using SuperTokenV1Library for ISuperToken;

    mapping (address => bool) public accountList;

    ISuperToken public daix;

    // fDAIx address on Polygon Mumbai = 0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f
    constructor(ISuperToken _daix) {

        daix = _daix;

    }

    /// @dev Mints 10,000 fDAI to this contract and wraps it all into fDAIx
    function gainDaiX() external {

        // Get address of fDAI by getting underlying token address from DAIx token
        IFakeDAI fdai = IFakeDAI( daix.getUnderlyingToken() );

        // Mint 10,000 fDAI
        fdai.mint(address(this), 10000e18);

        // Approve fDAIx contract to spend fDAI
        fdai.approve(address(daix), 20000e18);

        // Wrap the fDAI into fDAIx
        daix.upgrade(10000e18);

    }

    /// @dev creates a stream from this contract to desired receiver at desired rate
    function createStream(int96 flowRate, address receiver) external {

        // Create stream
        daix.createFlow(receiver, flowRate);

    }

    /// @dev updates a stream from this contract to desired receiver to desired rate
    function updateStream(int96 flowRate, address receiver) external {

        // Update stream
        daix.updateFlow(receiver, flowRate);

    }

    /// @dev deletes a stream from this contract to desired receiver
    function deleteStream(address receiver) external {

        // Delete stream
        daix.deleteFlow(address(this), receiver);

    }

    /// @dev get flow rate between this contract to certain receiver
    function readFlowRate(address receiver) external view returns (int96 flowRate) {

        // Get flow rate
        return daix.getFlowRate(address(this), receiver);

    }

}
```

</p>
</details>
</div>

- **gainDaiX**: Mints and wraps fDAI into fDAIx (Superfluid's wrapped token).
- **createStream**: Initiates a new money stream to a specified receiver.
- **updateStream**: Updates an existing money stream's flow rate.
- **deleteStream**: Terminates an existing money stream.
- **readFlowRate**: Reads the current flow rate of a stream.

### Writing Tests

#### Setting Up Your Test Environment

Your test environment will depend on where you would like to test your Superfluid application.
You can fork a public testnet where an instance of the Superfluid Protocol already exists (e.g Polygon Mumbai). In this case, you do not need to deploy a new instance of the Superfluid protocol.
However, if you are testing on a local testnet you would need to deploy a new instance of the Superfluid protocol.

<Tabs
    defaultValue="testnet"
    values={[
        { label: 'Forked Testnet', value: 'testnet' },
        { label: 'Local Net', value: 'localnet' },
    ]}
>

<TabItem value="testnet">

- Create a new Solidity file for your tests
- Import `forge-std/Test.sol` and inherit from `Test`.
- Import the Superfluid protocol contracts.
- Write your `setUp` function to run before each test case.

```solidity
pragma solidity ^0.8.14;
import "forge-std/Test.sol";
import {ISuperfluid, ISuperToken} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";
import {TestGovernance, Superfluid, ConstantFlowAgreementV1, CFAv1Library, SuperTokenFactory} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeploymentSteps.sol";
import {SuperfluidFrameworkDeployer} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeployer.sol";
import {SuperTokenV1Library} from "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";

contract FlowSenderTest is Test {
    // Test contract instance
    FlowSender flowSender;
    // Mumbai fork parameters
    uint256 mumbaiFork;
    // Set up your environment variables and include MUMBAI_RPC_URL
    string MUMBAI_RPC_URL = vm.envString("MUMBAI_RPC_URL");

    // Setup function to initialize test environment
    function setUp() public {

        //Forking and selecting the Mumbai testnet
        mumbaiFork = vm.createSelectFork(MUMBAI_RPC_URL);

        //Pointing to the fake Daix contract on Mumbai
        //For token and protocol addresses on all networks, check out the Superfluid Explorer: https://Explorer.superfluid.finance/
        daix = ISuperToken(0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f);

        //Deploy the contract
        vm.prank(address(0x123)); // Simulate a different caller
        flowSender=new FlowSender(daix);
        vm.unprank(); // Restore the caller

        //Add other functions and test contracts...
    }
}
```

</TabItem>
<TabItem value="localnet">
- Create a new Solidity file for your test.
- Import `forge-std/Test.sol` and inherit from `Test`.
- Import the Superfluid protocol contracts.
- Deploy a new instance of the Superfluid Protocol in the `setUp` function.
- Create and Deploy a new instance of your test contract.

```solidity
pragma solidity ^0.8.14;
import "forge-std/Test.sol";
import {ISuperfluid} from "@superfluid-finance/ethereum-contracts/contracts/interfaces/superfluid/ISuperfluid.sol";
import {SuperfluidFrameworkDeployer,
    TestGovernance,
    Superfluid,
    ConstantFlowAgreementV1,
    CFAv1Library,
    SuperTokenFactory
} from "@superfluid-finance/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeployer.sol";


contract FlowSenderTest is Test {
    // Test contract instance
    FlowSender flowSender;
    //Set up your Superfluid framework
    struct Framework {
        TestGovernance governance;
        Superfluid host;
        ConstantFlowAgreementV1 cfa;
        CFAv1Library.InitData cfaLib;
        InstantDistributionAgreementV1 ida;
        IDAv1Library.InitData idaLib;
        SuperTokenFactory superTokenFactory;
    }

    SuperfluidFrameworkDeployer.Framework sf;

    // Setup function to initialize test environment
    function setUp() public {
        address public owner;
	    //DEPLOYING THE FRAMEWORK
        SuperfluidFrameworkDeployer sfDeployer = new SuperfluidFrameworkDeployer();
        sfDeployer.deployTestFramework();
        sf = sfDeployer.getFramework();

	    // DEPLOYING DAI and DAI wrapper super token

	    ISuperToken daix = sfDeployer.deployWrapperToken(
	    "Fake DAI", "DAI", 18, 10000000000000
	    );

        // Initialize your contract here
        flowSender = new FlowSender(
            daix
        );

    }
}
```

</TabItem>
</Tabs>

:::tip About the `setUp` Function
The `setUp` function is an **optional** function standardized by Foundry (but it is necessary here, especially in the case of local testnet). It is a special function that is executed before each test case. It is used to initialize the test environment and contract instances.
To learn more about the `setUp` function, check out the [Foundry documentation](https://book.getfoundry.sh/forge/writing-tests).
:::

#### Testing Contract Functions

##### GainDaiX Function

Let's write a test for the `gainDaiX` function in the `FlowSender` contract:

```solidity
function testGainDaiX() public {
    // Setup: Deploy the FlowSender contract
    IFakeDAI fdai = new FakeDAI();
    ISuperToken daix = new SuperToken(address(fdai));
    FlowSender flowSender = new FlowSender(daix);

    // Action: Call the gainDaiX function
    flowSender.gainDaiX();

    // Assertions: Check if the contract has the expected amount of DAIx
    uint256 balance = daix.balanceOf(address(flowSender));
    assertEq(balance, 10000e18, "The balance of DAIx should be 10,000 after gainDaiX");
}
```

##### CreateStream Function

Now, let's test the `createStream` function:

```solidity
function testCreateStream() public {
    // Setup: Deploy the FlowSender contract and create a receiver address
    IFakeDAI fdai = new FakeDAI();
    ISuperToken daix = new SuperToken(address(fdai));
    FlowSender flowSender = new FlowSender(daix);
    address receiver = address(new Receiver());

    // Setup: Define a flow rate
    int96 flowRate = 1000; // Example flow rate

    // Action: Call the createStream function
    flowSender.createStream(flowRate, receiver);

    // Assertions: Verify if the stream is created with correct parameters
    (,int96 outFlowRate,,) = daix.getFlow(address(flowSender), receiver);
    assertEq(outFlowRate, flowRate, "The flow rate should match the specified rate");
}

```

#### Using Cheat Codes

Foundry's cheat codes can simulate various blockchain states and interactions. For example, to test the `deleteStream` function, you might want to simulate different account permissions:

```solidity
function testDeleteStream() public {
    // Setup: Deploy the FlowSender contract and create a receiver address
    IFakeDAI fdai = new FakeDAI();
    ISuperToken daix = new SuperToken(address(fdai));
    FlowSender flowSender = new FlowSender(daix);
    address receiver = address(new Receiver());

    // Setup: Create a stream first
    flowSender.createStream(1000, receiver);

    // Use cheat codes to simulate different account permissions
    // Attempt to delete a stream with an unauthorized user
    vm.prank(address(0x123)); // Simulate a different caller
    vm.expectRevert("Unauthorized"); // Expect a revert due to unauthorized access
    flowSender.deleteStream(receiver);

    // Action: Attempt to delete a stream with the correct permission
    flowSender.deleteStream(receiver);

    // Assertions: Verify the stream is deleted
    (,int96 outFlowRate,,) = daix.getFlow(address(flowSender), receiver);
    assertEq(outFlowRate, 0, "The flow rate should be zero after deletion");
}

```

### Running Tests

To execute your tests, use:

```bash
forge test
```

### Best Practices

- Write clear and descriptive test cases.
- Ensure code readability for easier maintenance.
- Use Foundry cheat codes to simulate real-world scenarios.
- Strive for high test coverage to capture a wide range of use cases.

### Conclusion

Testing is crucial in blockchain development for ensuring contract reliability and security, especially for complex protocols like Superfluid. This guide provides a foundation for using Foundry to write and run effective tests.

### Further Resources

- [Foundry Book](https://foundry.readthedocs.io)

---

<a id="doc_39"></a>

## 📁 protocol/super-tokens / Overview of Super Tokens

*파일 경로: protocol/super-tokens/overview.mdx*

---
sidebar_position: 1
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SuperTokenVis from '@site/src/components/Visualizations/SuperTokenVis';




Super Tokens extend the ERC20 token standard by integrating additional functionalities like streams and distributions. Super Tokens exist in two primary forms: Wrapper and Pure.



### Real-Time Balance

Super Tokens revolutionize balance calculations by combining traditional static balances with dynamic, real-time adjustments based on streams and distributions, leading to a more fluid representation of an account's value.

Characteristics of Super Tokens:

* **Static Balance**: Reflects the conventional ERC20 balance, representing the basic, unchanging part of an account's value.
* **Real-Time Balances**: Incorporates fluctuations from streams and distributions, adjusting the balance with each block to reflect ongoing financial activities. When you call the method `balanceOf()` on a Super Token, you get a real-time balance.
* **Complex Calculation**: Unlike conventional tokens, `balanceOf()` method in Super Tokens doesn't just retrieve a stored value; it performs complex calculations based on numerous parameters to give the real time balance.
* **Ongoing Relationships**: These calculations consider the account's continuous relationships with others, making the balance more representative of the current financial state.
* **Time-Sensitive**: In cases involving streams, the balance is further influenced by time, specifically through the timestamp of the latest block, making it sensitive to the passage of time.
* **Dynamic Adjustment**: As a result, the balance is a "real-time balance," capable of changing with every new block, independent of direct transactions affecting the account.

### Types of Super Tokens

<Tabs
  defaultValue="wrapper"
  values={[
    {label: 'Wrapper Super Tokens', value: 'wrapper'},
    {label: 'Pure Super Tokens', value: 'pure'},
    {label: 'Native Super Tokens', value: 'native'},
  ]}>
  <TabItem value="wrapper">

#### 1. Wrapper Super Tokens

Wrapper Super Tokens are wrapped from existing ERC20 tokens to allow interaction with the Superfluid Protocol.
They are the most common currently and can be permissionlessly created for any ERC20 token.

##### Wrapping & Unwrapping

- **Wrapping**: Deposit ERC20 tokens into the Wrapper Super Token contract to mint an equivalent amount of Super Tokens.
- **Unwrapping**: Burn Super Tokens to get back the underlying ERC20 tokens.


##### When to use Custom Wrappers?

- **Unconventional ERC-20**: Custom Wrapper Super Tokens are typically used when underlying ERC20 tokens have complex functionalities that standard wrappers can't handle.
- **Additional Features**: They can also be used to add additional features to the Super Token which don't exist in the Super Token contract.

For detailed deployment steps and further information, visit the [Deploy a Super Token Page](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-wrapped-super-token.mdx).

  </TabItem>
  <TabItem value="pure">

#### 2. Pure Super Tokens

Pure Super Tokens are independent of any underlying asset, inheriting all Superfluid functionalities directly.

##### Customization

Pure Super Tokens can be customized with additional features like pre-minting, access control, and wallet whitelisting. They can be categorized as Governed or Independent, with Governed Pure Super Tokens recommended for alignment with Superfluid Protocol Governance.

For a step-by-step guide on deploying Pure Super Tokens, refer to the [Pure Super Token Deployment](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-pure-super-token.mdx) section.

  </TabItem>
  <TabItem value="native">

#### 3. Native Super Tokens

Native Super Tokens are similar to wrappers but are designed for native assets like ETH, MATIC, or AVAX. Depositing these assets into the Native Super Token contract yields a wrapped version of the asset.

Canonical deployments of Native Super Tokens are available for each chain that Superfluid operates on. For detailed deployment steps and further information, visit the [Deploy a Super Token Page](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-wrapped-super-token.mdx).

  </TabItem>
</Tabs>

---

<a id="doc_40"></a>

## 📁 protocol/super-tokens/guides / Using the SuperTokenV1Library

*파일 경로: protocol/super-tokens/guides/using-library.mdx*

---
sidebar_position: 1
---


The [SuperTokenV1Library](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol) is the primary interface for developers to interact with the Superfluid protocol
when building smart contracts on-chain.

This comprehensive library provides all the necessary tools to work with the two main primitives of the Superfluid protocol:
[Money Streaming](/docs/protocol/money-streaming/overview) (also called *Constant Flow Agreement* or *CFA*)
and [Distribution Pools](/docs/protocol/distributions/overview) (also called *General Distributions Agreement* or *GDA*).

### Getting Started

To use the SuperTokenV1Library in your smart contract, follow these steps:

1. Import the library in your contract:

```solidity
import "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";
```

2. Include the `using` statement in your contract:

```solidity
using SuperTokenV1Library for ISuperToken;
```

:::note about Native Super Tokens
For Native Super Tokens, use `using SuperTokenV1Library for ISETH;` instead.
:::

:::tip Technical Reference
For more details on the full list of functions and usage, refer to the [SuperTokenV1Library Technical Reference](/docs/technical-reference/SuperTokenV1Library).
:::

### Key Concepts

The SuperTokenV1Library revolves around two main primitives:

1. **Constant Flow Agreement (CFA)**: This represents Money Streaming functionality.
2. **General Distributions Agreement (GDA)**: This handles Distribution Pools.

The library provides functions for various operations within these primitives:

- Writing to the protocol (e.g., creating flows, updating flows, creating pools)
- Reading from the protocol (e.g., getting flow rates)
- Access control (allowing other wallets to control flow rates)
- Attaching user data to blockchain function calls

### Key Functions

Let's explore some example functions in the SuperTokenV1Library:

#### Money Streaming (CFA) Functions

The library provides a wide range of functions for managing money streams, including creating, updating, and deleting flows. For example:

##### Creating a Flow

```solidity
function createFlow(
    ISuperToken token,
    address receiver,
    int96 flowRate,
    bytes memory userData
) internal returns (bool)
```

This function creates a new money stream. You can omit the `userData` parameter if not needed.

##### Getting Flow Information

```solidity
function getFlowInfo(
    ISuperToken token,
    address sender,
    address receiver
) internal returns (
    uint256 lastUpdated,
    int96 flowRate,
    uint256 deposit,
    uint256 owedDeposit
)
```

This function retrieves detailed information about a specific flow.

#### Distribution Pools (GDA) Functions

By the same token, the library provides functions for managing distribution pools, including creating pools and claiming distributions:

##### Creating a Pool

```solidity
function createPool(
    contract ISuperToken token,
    address admin,
    struct PoolConfig poolConfig
) 
    internal 
    returns (contract ISuperfluidPool pool)
```

The `PoolConfig` struct is defined as follows:

```solidity
struct PoolConfig {
    bool transferabilityForUnitsOwner;
    bool distributionFromAnyAddress;
}
```
- `transferabilityForUnitsOwner`: If true, the pool members can transfer their owned units, else, only the pool admin can manipulate the units for pool members
- `distributionFromAnyAddress`: If true, anyone can execute distributions via the pool, else, only the pool admin can execute distributions via the pool

##### Claiming tokens

```solidity
function claimAll(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    address memberAddress
) 
    internal 
    returns (bool)
```
This function allows a member to claim all tokens to all the members of the pool.


#### Access Control Functions

The library also provides functions for managing access control and permissions between different wallet addresses and smart contracts:

##### Setting Flow Permissions

```solidity
function setFlowPermissions(
    ISuperToken token,
    address flowOperator,
    bool allowCreate,
    bool allowUpdate,
    bool allowDelete,
    int96 flowRateAllowance
) internal returns (bool)
```

This function allows you to grant specific permissions to another address (flowOperator) to manage flows on your behalf.

### Advanced Usage

#### Context-Aware Functions

For more advanced use cases including with [Super Apps](/docs/protocol/advanced-topics/super-apps/understand-super-apps), the library provides context-aware versions of many functions. These are useful when you need to chain multiple operations or when working within the context of a Superfluid callback:

```solidity
function createFlowFromWithCtx(
    ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes memory ctx
) internal returns (bytes memory newCtx)
```

#### User Data

Many functions in the SuperTokenV1Library allow you to attach user data to your transactions. This can be useful for adding metadata or triggering specific logic in receiver contracts.

### Best Practices

1. Always check return values of functions to ensure operations were successful.
2. Be mindful of gas costs, especially when working with multiple flows or large distribution pools.
3. Use the appropriate permissions and access control functions to ensure the security of your contract.

### Conclusion

The SuperTokenV1Library is a powerful tool for interacting with the Superfluid protocol on-chain, in order to build smart contracts. By leveraging its functions for money streaming and distribution pools, you can create sophisticated blockchain applications with real-time finance capabilities. Always refer to the latest documentation and test thoroughly to ensure your implementation is correct and secure.

---

<a id="doc_41"></a>

## 📁 protocol/super-tokens/guides/deploy-super-token / Deploy a Pure Super Token

*파일 경로: protocol/super-tokens/guides/deploy-super-token/deploy-pure-super-token.mdx*

---
sidebar_position: 2
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';
import PureSuperTokenDeployer from '@site/src/components/PureSuperTokenDeployer';
import PureSuperTokenInitializer from '@site/src/components/PureSuperTokenInitializer';


This guide offers detailed instructions for deploying [Pure Super Tokens](/docs/protocol/super-tokens/overview#types-of-super-tokens).
The good news is that you can deploy your own Pure Super Token and initialize it without leaving this page.

<Admonition type="info">

Learn more about Pure Super Tokens in the [Types of Super Tokens](/docs/protocol/super-tokens/overview.mdx#types-of-super-tokens) section.

</Admonition>

### Prerequisites

Before you start, ensure you have:

- Basic understanding of blockchain and smart contracts.
- Access to a compatible cryptocurrency wallet (like [MetaMask](https://metamask.io/)).
- ETH or relevant cryptocurrency for transaction fees.

---
### Deploy a Pure Super Token from the interface (Easy)

You can use the interface below to deploy a Pure Super Token:
<PureSuperTokenDeployer/>

<br/>
Once the contract is deployed, you can use the address to initialize the Pure Super Token.
<PureSuperTokenInitializer/>

<br/>
<Admonition type="warning" title="Check Parameters">

Double-check the parameters to avoid deployment errors.

</Admonition>

:::tip Add your token to the Superfluid Dashboard

After deploying your Pure Super Token, you can add it to the [Superfluid Dashboard](https://app.superfluid.finance/) for easy access and monitoring.

Follow [these steps](/docs/protocol/contribute/submit-token-dashboard) to submit your request. You will need to provide the Super Token address and some other information.
:::

---

### Deploying a Custom Pure Super Token (Advanced)

Deploying a Pure Super Token allows for custom non-Superfluid logic integration.

#### Detailed Steps

1. **Repository Setup**: Clone the [custom-supertokens repository](https://github.com/superfluid-finance/custom-supertokens#setup) and follow the setup instructions.
2. **Logic Selection**: Choose from existing logic examples or develop your own based on [PureSuperToken.sol](https://github.com/superfluid-finance/custom-supertokens/blob/main/contracts/PureSuperToken.sol).
3. **Deployment**: Create a .env file, configure it for your network, and follow the repository's deployment steps.

<Admonition type="note" title="Custom Logic Caution">

If developing custom logic, ensure to rename the contract in the .sol file to avoid conflicts during the build.

</Admonition>

---

<a id="doc_42"></a>

## 📁 protocol/super-tokens/guides/deploy-super-token / Deploy a Wrapper Super Token

*파일 경로: protocol/super-tokens/guides/deploy-super-token/deploy-wrapped-super-token.mdx*

---
sidebar_position: 1
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';
import ERC20Wrapper from '@site/src/components/Erc20Wrapper';


This guide offers detailed instructions for deploying [Wrapped Super Tokens](/docs/protocol/super-tokens/overview#1-wrapper-super-tokens) using the [Super Token Factory contract](#super-tokens-factory-contract).

<Admonition type="info">

Learn more about Wrapper Super Tokens in the [Types of Super Tokens](/docs/protocol/super-tokens/overview.mdx#types-of-super-tokens) section.

</Admonition>

### Prerequisites

Before you start, ensure you have:

- Basic understanding of blockchain and smart contracts.
- Access to a compatible cryptocurrency wallet (like [MetaMask](https://metamask.io/)).
- ETH or relevant cryptocurrency for transaction fees.

---
### Super Tokens Factory Contract

The [Super Token Factory contract](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/superfluid/SuperTokenFactory.sol) is used to create Super Tokens:
- It is permissionless and can be used by anyone to create Super Tokens.
- It is deployed on all the networks where you can find the Superfluid Protocol.

We will describe the steps for deploying each type of Super Token in the following chapters.

:::tip Contract addresses
For addresses of the Super Token Factory contract on different networks, refer to [The Superfluid Explorer](https://Explorer.superfluid.finance/), the Protocol section.
:::

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![SuperFluidConsole](/assets/ScreenshotConsoleFactory.png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*SuperFluid Explorer: Protocol Section*</p>
</div>

---

### Deploying a Wrapper Super Token

:::tip Are you looking for a Super Token?
Are you looking for a specific token? It may already exist.

Check the [Explorer](https://Explorer.superfluid.finance/) to see if someone else has already created and listed a wrapper for the token you are looking for.
:::

You can deploy your own Wrapper Super Token using the Super Token Factory contract through the interface below. Please ensure you have the required parameters ready before proceeding:
- **Underlying Token**: The address of the ERC20 token to wrap.
- **Name**: The name of the Super Token. We always recommend using the same name as the underlying token prefexed with 'Super' (eg. 'Super DAI').
- **Symbol**: The symbol of the Super Token. We recommend using the same symbol as the underlying token suffixed with 'x' (eg. 'DAIx').

:::tip What is Upgradability?
If you look at the `CreateERC20Wrapper` method at the [Super Token Factory contract](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/superfluid/SuperTokenFactory.sol), you'll see a parameter called `Upgradability`.

This allows Superfluid Protocol Governance to upgrade the Super Token contract in the future and stay compatible with the latest features.
    - '0': Not Upgradable: The contract cannot be upgraded.
    - '1': Semi-Upgradability: The contract can be upgraded by Superfluid Protocol Governance but only under certain [conditions](https://github.com/superfluid-finance/protocol-monorepo/wiki/About-Super-Token-Classification).
    - '2': Fully Upgradable: The contract can be upgraded by Superfluid Protocol Governance without any restrictions.

For the purpose of simplicity, we always recommend using '1'. This is why this parameter is not included in the interface below and is set to 1 by default.
:::

You can choose to deploy your Wrapper Super Token using the interface on your favourite scanner (eg. [Etherscan](https://etherscan.io/)).
You can also use the interface below to deploy your Wrapper Super Token:
<ERC20Wrapper/>

<br/>

:::warning Manual name and symbol
Manual name and symbol input is not recommended unless the deployer above gives you an error and is unable to detect the underlying token name and symbol. The recommended format is always 'Super' + 'Underlying Token Name' and 'Underlying Token Symbol' + 'x'.
:::

:::warning Check Parameters
Double-check the parameters to avoid deployment errors.
:::

#### Verifying and Adding Token to Superfluid Dashboard

After you token has been deployed, you can follow these steps in order to add your token to the Superfluid Dashboard:
- Locate the new Super Token's address in the "SuperTokenCreated" event log. This will allow you to retrieve the Super Token address.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    ![Super Token Address](/assets/SuperTokenEvent.png)
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Super Token Address on Etherscan*</p>
</div>

- Follow [these steps](/docs/protocol/contribute/submit-token-dashboard) to submit your request. You will need to provide the Super Token address and some other information.

---

### Deploying a Self-Governed Super Token

Self-Governed Super Tokens give you the ability to control and update Super Token logic.

#### Deployment Process

1. **Using SuperTokenFactory**: Interact with the `createERC20Wrapper` function with the `admin` parameter on the SuperTokenFactory contract.
2. **Updating Logic**: Use `updateCode` to apply custom logic or update to the latest Superfluid token contract.

<Admonition type="tip">

For more information, see the [Self-Governed Super Token Wiki](https://github.com/superfluid-finance/protocol-monorepo/wiki/Self-Governed-Super-Token) or seek assistance on [Superfluid Discord](https://discord.superfluid.finance/).

</Admonition>

<Admonition type="warning" title="Be careful!">

Unless you know what you are doing, deploying a self-governed Super Token is not recommended.

</Admonition>

---

<a id="doc_43"></a>

## 📁 protocol/super-tokens/guides/deploy-super-token / Deploying a Custom Super Token

*파일 경로: protocol/super-tokens/guides/deploy-super-token/deploy-custom-super-token.mdx*

---
sidebar_position: 3
---



This guide will walk you through the process of deploying a Custom Super Token for the Superfluid protocol.
Custom Super Tokens allow you to create tokens with additional functionality while maintaining compatibility with the Superfluid protocol.

This documentation contains different guides if you are looking to easily deploy a simple [Wrapped Super Token](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-wrapped-super-token) or a simple [Pure Super Token](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-pure-super-token) from your interface with no code.
We strongly recommend to check those guides first before this one.

For the purposes of this guide, we'll explore two examples:
- [a Pure Super Token](#example-1-pure-super-token)
- [a Bridged Super Token](#example-2-bridged-super-token)

### Prerequisites

Before we begin, make sure you have the following:

- [Foundry](https://book.getfoundry.sh/) installed on your system
- Basic knowledge of Solidity and smart contract development

### Getting Started

First, let's clone the Custom Super Tokens repository:

```bash
git clone https://github.com/superfluid-finance/custom-supertokens
cd custom-supertokens
```

This repository is structured as a Foundry project and contains multiple examples of custom Super Tokens.

Once you've cloned the repository, install the dependencies:

```bash
forge install
```

This command will install the required packages, including `@superfluid-finance`, `@openzeppelin-contracts (v4.9.3)`, and `forge-std`.

### Example 1: Pure Super Token

Let's start with the Pure Super Token example. This is a simple custom Super Token implementation.

#### Understanding the Contract

The `PureSuperToken.sol` file contains the contract for our Pure Super Token:

```solidity
contract PureSuperTokenProxy is CustomSuperTokenBase, UUPSProxy {
    function initialize(
        ISuperTokenFactory factory,
        string memory name,
        string memory symbol,
        address receiver,
        uint256 initialSupply
    ) external {
        ISuperTokenFactory(factory).initializeCustomSuperToken(address(this));
        ISuperToken(address(this)).initialize(
            IERC20(address(0)),
            18,
            name,
            symbol
        );
        ISuperToken(address(this)).selfMint(receiver, initialSupply, "");
    }
}
```

This contract creates a new `UUPSProxy` which is initialized as a Pure Super Token. The `initialize` function sets up the token using the `SuperTokenFactory` and mints the initial supply to the specified receiver.

#### Testing

To test the Pure Super Token, run:

```bash
forge test --match testDeploy testSuperTokenBalance
```

This will execute the tests in `PureSuperToken.t.sol`, which include deploying the token and checking the receiver's balance.

#### Deployment

To deploy the Pure Super Token, use the following Foundry command:

```bash
forge create --rpc-url <RPC_URL> --private-key <YOUR_PRIVATE_KEY> --etherscan-api-key <YOUR_API_KEY> --verify --via-ir src/PureSuperToken.sol:PureSuperTokenProxy
```

Replace `<RPC_URL>`, `<YOUR_PRIVATE_KEY>`, and `<YOUR_API_KEY>` with your actual values.

#### Initialization

After deployment, you need to initialize the token by calling the `initialize` function with the appropriate parameters:

```solidity
pureSuperToken.initialize(
    superTokenFactory,
    "MyToken",
    "MTK",
    initialReceiver,
    initialSupply
);
```

### Example 2: Bridged Super Token

The Bridged Super Token is a more complex example that includes additional functionality for cross-chain operations.

#### Understanding the Contract

The `BridgedSuperToken.sol` file contains the contract for our Bridged Super Token. This implementation includes features like minting and burning limits for bridges.

#### Testing

To test the Bridged Super Token, run:

```bash
forge test
```

This will execute the tests in `BridgedSuperTokenTest.t.sol`, which cover various aspects of the token's functionality, including limit setting, minting, and burning.

#### Deployment and Initialization

The deployment and initialization process for the Bridged Super Token is similar to the Pure Super Token. Use the `forge create` command for deployment, and then call the `initialize` function to set up the token.

### Creating Your Own Custom Super Token

When creating your own custom Super Token, you can use the following functions from the [ISuperToken Interface](/docs/technical-reference/ISuperToken)

#### `selfMint`

```solidity
function selfMint(
    address account,
    uint256 amount,
    bytes memory userData
) external;
```

This function mints new tokens for the specified account. If `userData` is not empty, it invokes the `tokensReceived` hook according to ERC777 semantics.

#### `selfBurn`

```solidity
function selfBurn(
    address account,
    uint256 amount,
    bytes memory userData
) external;
```

This function burns existing tokens for the specified account. If `userData` is not empty, it invokes the `tokensToSend` hook according to ERC777 semantics.

#### `selfTransferFrom`

```solidity
function selfTransferFrom(
    address sender,
    address spender,
    address recipient,
    uint256 amount
) external;
```

This function transfers tokens from the `sender` to the `recipient`. If `spender` isn't the same as `sender`, it checks if `spender` has allowance to spend tokens of `sender`.

#### `selfApproveFor`

```solidity
function selfApproveFor(
    address account,
    address spender,
    uint256 amount
) external;
```

This function gives `spender` the `amount` allowance to spend the tokens of `account`.

These functions allow you to customize the behavior of your Super Token while maintaining compatibility with the Superfluid protocol.

### Conclusion

By following this guide, you should now be able to deploy and initialize custom Super Tokens for the Superfluid protocol. Remember to thoroughly test your custom implementations and consider the security implications of any additional functionality you add to your tokens.

For more information on Custom Super Tokens, check out the [Custom Super Token Wiki](https://github.com/superfluid-finance/protocol-monorepo/wiki/About-Custom-Super-Token) and the [Deploy a Custom Super Token Guide](https://docs.superfluid.finance/docs/protocol/super-tokens/guides/deploy-super-token/deploy-custom-super-token).

---

<a id="doc_44"></a>

## 📁 sdk / Quickstart

*파일 경로: sdk/quickstart.mdx*

---
sidebar_position: 1
---


This guide will help you get started with the Superfluid protocol by creating a simple React app that interacts with the protocol.
You'll learn how to connect your wallet, create streams, and create pools using the Superfluid protocol.

### How to Interact with the Superfluid Protocol

When interacting with the Superfluid protocol from a client application, you'll use one of two contracts depending on the functionality you need:

1. For Money Streaming: Use the [`CFAv1Forwarder`](/docs/technical-reference/CFAv1Forwarder) contract
2. For Distribution Pools: Use the [`GDAv1Forwarder`](/docs/technical-reference/GDAv1Forwarder) contract

We use these forwarder contracts instead of building an SDK because:
- It simplifies the integration process
- It reduces the need for frequent updates to the SDK
- It allows for more flexibility and direct interaction with the protocol

### Contract Addresses and ABIs

Here are the addresses for each contract across all Superfluid-supported chains:

- `CFAv1Forwarder`: `0xcfA132E353cB4E398080B9700609bb008eceB125`
- `GDAv1Forwarder`: `0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08`

You can find the full ABIs for these contracts in the following technical references:
- [CFAv1Forwarder ABI](/docs/technical-reference/CFAv1Forwarder)
- [GDAv1Forwarder ABI](/docs/technical-reference/GDAv1Forwarder)

### Creating a React App (Next.js)

To create a new Next.js app, follow these steps:

1. Open your terminal and run:
   ```
   npx create-next-app@latest my-superfluid-app
   ```
2. Navigate to your new app directory:
   ```
   cd my-superfluid-app
   ```
3. Install necessary dependencies:
   ```
   npm install ethers@5.7.2
   ```

### Superfluid Interaction Component

In this section, we will provide a React component that allows you to interact with the Superfluid protocol.
This component will allow you to:
- Connect your wallet (eg. Metamask)
- Create a stream through the `CFAv1Forwarder` contract (for [Money Streaming](docs/concepts/overview/money-streaming))
- Create a pool through the `GDAv1Forwarder` contract (for [Distribution Pools](docs/concepts/overview/distributions))

Here's a React component that allows you to create a stream and create a pool. You can copy and paste this into a new file in your Next.js app's `pages` directory (e.g., `pages/superfluid-demo.js`):

:::note
For a full list of available functions and events, refer to the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder) and [GDAv1Forwarder technical reference](/docs/technical-reference/GDAv1Forwarder).
:::

```jsx live
// Don't forget imports
//import React, { useState } from 'react';
//import { ethers } from 'ethers';

function SuperfluidDemo() {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState('');
  const [tokenAddress, setTokenAddress] = useState('');
  const [receiverAddress, setReceiverAddress] = useState('');
  const [flowRate, setFlowRate] = useState('');
  const [adminAddress, setAdminAddress] = useState('');
  const [message, setMessage] = useState('');

  const CFAv1ForwarderAddress = '0xcfA132E353cB4E398080B9700609bb008eceB125';
  const GDAv1ForwarderAddress = '0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08';
  // Simplified ABIs with only the functions we need
  const CFAv1ForwarderABI = [
  "function createFlow(address token, address sender, address receiver, int96 flowRate, bytes memory userData) external returns (bool)"
  ];

  const GDAv1ForwarderABI = [
  "function createPool(address token, address admin, (uint32 transferabilityForUnitsOwner, bool distributionFromAnyAddress) memory poolConfig) external returns (bool, address)"
  ];

  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        setProvider(provider);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        setMessage(`Connected to ${address}`);
      } catch (error) {
        console.error('Failed to connect wallet:', error);
        setMessage('Failed to connect wallet. Please try again.');
      }
    } else {
      setMessage('Please install Metamask to use this feature.');
    }
  };

  const createStream = async () => {
    if (!provider) {
      setMessage('Please connect your wallet first.');
      return;
    }

    const signer = provider.getSigner();
    const contract = new ethers.Contract(CFAv1ForwarderAddress, CFAv1ForwarderABI, signer);

    try {
      const tx = await contract.createFlow(
        tokenAddress,
        account,
        receiverAddress,
        flowRate,
        "0x"
      );
      await tx.wait();
      setMessage('The stream has been created successfully.');
    } catch (error) {
      console.error('Error creating stream:', error);
      setMessage('Failed to create stream. Please try again.');
    }
  };

  const createPool = async () => {
    if (!provider) {
      setMessage('Please connect your wallet first.');
      return;
    }

    const signer = provider.getSigner();
    const contract = new ethers.Contract(GDAv1ForwarderAddress, GDAv1ForwarderABI, signer);

    try {
      const poolConfig = {
        transferabilityForUnitsOwner: 0,
        distributionFromAnyAddress: false
      };
      const tx = await contract.createPool(tokenAddress, adminAddress, poolConfig);
      const receipt = await tx.wait();
      const [success, poolAddress] = receipt.events.find(e => e.event === 'PoolCreated').args;
      setMessage(`Pool created successfully at ${poolAddress}`);
    } catch (error) {
      console.error('Error creating pool:', error);
      setMessage('Failed to create pool. Please try again.');
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: 'auto', padding: '20px' }}>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', textAlign: 'center' }}>Superfluid Demo</h1>
      
      {!account ? (
        <button onClick={connectWallet} style={{ backgroundColor: 'blue', color: 'white', padding: '10px', borderRadius: '5px', border: 'none', cursor: 'pointer', width: '100%' }}>Connect Wallet</button>
      ) : (
        <p>Connected: {account}</p>
      )}
      
      <input
        placeholder="Token Address"
        value={tokenAddress}
        onChange={(e) => setTokenAddress(e.target.value)}
        style={{ width: '100%', padding: '10px', margin: '10px 0' }}
      />
      
      <h2 style={{ fontSize: '20px', fontWeight: 'bold' }}>Create Stream</h2>
      <input
        placeholder="Receiver Address"
        value={receiverAddress}
        onChange={(e) => setReceiverAddress(e.target.value)}
        style={{ width: '100%', padding: '10px', margin: '10px 0' }}
      />
      <input
        placeholder="Flow Rate"
        value={flowRate}
        onChange={(e) => setFlowRate(e.target.value)}
        style={{ width: '100%', padding: '10px', margin: '10px 0' }}
      />
      <button onClick={createStream} style={{ backgroundColor: 'green', color: 'white', padding: '10px', borderRadius: '5px', border: 'none', cursor: 'pointer', width: '100%' }}>Create Stream</button>
      
      <h2 style={{ fontSize: '20px', fontWeight: 'bold', marginTop: '20px' }}>Create Pool</h2>
      <input
        placeholder="Admin Address"
        value={adminAddress}
        onChange={(e) => setAdminAddress(e.target.value)}
        style={{ width: '100%', padding: '10px', margin: '10px 0' }}
      />
      <button onClick={createPool} style={{ backgroundColor: 'blue', color: 'white', padding: '10px', borderRadius: '5px', border: 'none', cursor: 'pointer', width: '100%' }}>Create Pool</button>

      {message && <p style={{ marginTop: '20px', textAlign: 'center' }}>{message}</p>}
    </div>
  );
}
```

To use this component:

1. Copy the above code into a new file in your Next.js app's `pages` directory (e.g., `pages/superfluid-demo.js`).
2. Uncomment the necessary imports at the top of the file.
3. Run your Next.js app with `npm run dev`.
4. Navigate to `http://localhost:3000/superfluid-demo` in your browser.
5. Connect your wallet, then you can create streams and pools using the Superfluid protocol.

This component provides a basic interface for creating streams and pools. In a production environment, you would want to add more error checking, input validation, and additional features.

:::tip About the Component
A few tips in order to make sure you can use the component correctly:
- The component above uses simple ethers.js functions to interact with the Superfluid protocol. You can choose to use a different library or SDK if you prefer (eg. [Viem](https://viem.sh/), [Web3.js](https://docs.web3js.org/)).
- The component does not manage wallet connections or chain switching in a production-ready way. You should add more robust error handling and user feedback.
- The component uses the Superfluid forwarders ABIs in a simplified form. You can find the full ABIs in the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder) and [GDAv1Forwarder technical reference](/docs/technical-reference/GDAv1Forwarder).
:::

---

<a id="doc_45"></a>

## 📁 sdk/advanced-topics / Batch transactions with Macros

*파일 경로: sdk/advanced-topics/batch-calls.mdx*

---
sidebar_position: 1
---


import CodeBlock from "@theme/CodeBlock";
import MacroForwarder from "!!raw-loader!@site/src/contracts/MacroForwarder.sol";
import MacroForwarderABI from "!!raw-loader!@site/src/abis/macroForwarder.json";
import MultiFlowDeleteMacro from "!!raw-loader!@site/src/contracts/MultiFlowDeleteMacro.sol";


Superfluid's infrastructure introduces innovative approaches to batching transactions and account abstraction,
leveraging the [modular architrecture](/docs/technical-reference/Architecture) of Superfluid,
and specifically the mastermind contract of the protocol called the [Superfluid Host](/docs/concepts/advanced-topics/superfluid-host).
This document provides a guide of how to use the MacroForwarder contract to batch transactions.

### Background

The Superfluid Host contract makes it possible to batch transactions from day one through a method called `batchCall`.
Eventually, the Superfluid Host adopted [ERC-2771](https://eips.ethereum.org/EIPS/eip-2771). As opposed to the [EIP-4337](https://ethereum.org/en/roadmap/account-abstraction)
which uses a Contract Account (CA) for abstraction, ERC-2771
extends the capabilities of the Host by allowing a trusted forwarder to pass the original `msg.sender` to the host contract through the method `forwardBatchCall`.


### Macro Forwarder Contract Overview

Introducing a simple and secure way for builders to define their own macros without needing to be directly trusted by the Superfluid host contract.
This approach simplifies on-chain logic for batch calls, reduces gas consumption and potentially ameliorates the front-end code, addressing atomicity issues.
Today, Superfluid has a contract called [`MacroForwarder.sol`](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/utils/MacroForwarder.sol)
 which is a trusted forwarder for user-defined macro interfaces.

<div>
<details>
<summary>Click here to show the `MacroForwarder` contract</summary>
<p>

<CodeBlock language="solidity">{MacroForwarder}</CodeBlock>

</p>
</details>
</div>

#### Macro Forwarder Contract Address

The `MacroForwarder` contract has the same address on all networks:

```bash
0xFD0268E33111565dE546af2675351A4b1587F89F
```

#### Macro Forwarder Contract ABI

In order to interact with the `MacroForwarder` contract from your client application, you can use the following ABI:

<div>
<details>
<summary>Click here to show the `MacroForwarder` ABI</summary>
<p>

<CodeBlock language="json">{MacroForwarderABI}</CodeBlock>

</p>
</details>
</div>


### How to use the Macro Forwarder

In order to understand how to use the `MacroForwarder` contract,
we will use an example contract called `MultiFlowDeleteMacro.sol` which allows us to batch call delete flow transactions from one account to multiple accounts for a specific Super Token:

<div>
<details>
<summary>Click here to show the `MultiFlowDeleteMacro` contract</summary>
<p>
<CodeBlock language="solidity">{MultiFlowDeleteMacro}</CodeBlock>
</p>
</details>
</div>

The steps in order to use the `MacroForwarder` contract are as follows:
1. Create a contract which inherit the User Defined Macro Interface
2. Implement your Macro Interface
3. Use the Macro Forwarder to batch call the transactions

:::tip Get ready for tests and deployment
Creating your own macro involves testing and deploying a smart contract. If you are not familiar with testing and deployment frameworks on the Ethereum Virtual Machine,
you should consider learning about [Hardhat](https://hardhat.org/) or [Foundry](https://book.getfoundry.sh/).
:::


#### 1. Create your contract and inherit the User Defined Macro Interface

As you may have noticed, the `MultiFlowDeleteMacro` contract inherits the `IUserDefinedMacro` interface like so:

```solidity
contract MultiFlowDeleteMacro is IUserDefinedMacro {
    ...
}
```
This is an interface that defines the `buildBatchOperations` method. It is the only required method to be implemented in the contract that inherits it.

Therefore, the first step is to create a new contract which inherits the `IUserDefinedMacro` interface.

#### 2. Implement your Macro Interface

The `buildBatchOperations` method is the only required method to be implemented in the contract that inherits the `IUserDefinedMacro` interface.
This method returns an array of `ISuperfluid.Operation[]` struct which will be consumed by the `MacroForwarder` contract. This struct is defined as follows:

```solidity
struct Operation {
    operationType operationType;
    address target;
    bytes data;
}
```

In the example contract `MultiFlowDeleteMacro`, you can see that the `buildBatchOperations` method is implemented as follows:

```solidity
function buildBatchOperations(ISuperfluid host, bytes memory params, address msgSender) public virtual view
        returns (ISuperfluid.Operation[] memory operations)
    {
        IConstantFlowAgreementV1 cfa = IConstantFlowAgreementV1(address(host.getAgreementClass(
            keccak256("org.superfluid-finance.agreements.ConstantFlowAgreement.v1")
        )));

        // parse params
        (ISuperToken token, address[] memory receivers) =
            abi.decode(params, (ISuperToken, address[]));

        // construct batch operations
        operations = new ISuperfluid.Operation[](receivers.length);
        for (uint i = 0; i < receivers.length; ++i) {
            bytes memory callData = abi.encodeCall(cfa.deleteFlow,
                                                   (token,
                                                    msgSender,
                                                    receivers[i],
                                                    new bytes(0) // placeholder
                                                   ));
            operations[i] = ISuperfluid.Operation({
                operationType : BatchOperation.OPERATION_TYPE_SUPERFLUID_CALL_AGREEMENT, // type
                target: address(cfa),
                data: abi.encode(callData, new bytes(0))
            });
        }
    }

```


:::warning About the method `getParams`
The `MultiFlowDeleteMacro` example contract contains a method called `getParams`. This method is not required to be implemented in the contract that inherits the `IUserDefinedMacro` interface.
However, it is highly recommended to implement this method in order to parse the parameters of the macro on the front-end.

This method is simply implemented by encoding the parameters that will be used to call the method `runMacro`from `MacroForwarder` contract. It is usually one line of code as such:

```solidity
function getParams(ISuperToken token, address[] memory receivers) public pure returns (bytes memory) {
    return abi.encode(token, receivers);
}
```
:::

Once, you set up and tested your Macro contract, you can deploy it to your target EVM network and use the `MacroForwarder` contract to batch call the transactions.

#### 3. Use the Macro Forwarder to batch call the transactions

The `MacroForwarder` contract is used to batch call the transactions. It is a simple contract that has a method called `runMacro` which takes the following parameters:

- `IUserDefinedMacro m`: The address of the contract that inherits the `IUserDefinedMacro` interface
- `bytes calldata params`: The parameters of the macro

The `runMacro` method is called by the user and it will batch call the transactions defined in the `buildBatchOperations` method of the `IUserDefinedMacro` contract.

To showcase how this works, we use the [`MacroFowarder` contract](https://sepolia-optimism.etherscan.io/address/0xFD0268E33111565dE546af2675351A4b1587F89F) deployed on OP Sepolia.
We deployed an example of our [`MultiFlowDeleteMacro` contract](https://sepolia-optimism.etherscan.io/address/0x997b37Fb47c489CF067421aEeAf7Be0543fA5362) on the same network.
We will use the `MacroForwarder` contract to batch call the transactions.

We showcase below a simple React component which implements all of this:

<div>
<details>
<summary>Click here to show the `MacroForwarderComponent`</summary>
<p>

```jsx
const MacroForwarderComponent = ({
  macroForwarderAddress,
  userDefinedMacroAddress,
}) => {
  const [walletAddress, setWalletAddress] = useState("");
  const [superToken, setSuperToken] = useState("");
  const [receivers, setReceivers] = useState("");
  const [message, setMessage] = useState("");

  // ABI for MacroForwarder contract including `runMacro`
  const macroForwarderABI = [
    //ABI for MacroForwarder contract
  ];

  // ABI for your UserDefinedMacro including `getParams`
  const iUserDefinedMacroABI = [
    //ABI for your UserDefinedMacro including `getParams`
  ];

  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setWalletAddress(address);
        console.log("Connected to MetaMask");
      } catch (error) {
        console.error("Error connecting to MetaMask", error);
        setMessage("Error connecting to MetaMask");
      }
    } else {
      console.log("Ethereum wallet is not connected or not installed.");
      setMessage("Ethereum wallet is not connected or not installed.");
    }
  };

  const executeMacro = async () => {
    try {
      if (!walletAddress) throw new Error("Wallet not connected.");
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      const userDefinedMacroContract = new ethers.Contract(
        userDefinedMacroAddress,
        iUserDefinedMacroABI,
        signer
      );
      const receiversArray = receivers
        .split(",")
        .map((address) => address.trim());
      const params = await userDefinedMacroContract.getParams(
        superToken,
        receiversArray
      );

      const macroForwarderContract = new ethers.Contract(
        macroForwarderAddress,
        macroForwarderABI,
        signer
      );
      const tx = await macroForwarderContract.runMacro(
        userDefinedMacroAddress,
        params
      );
      await tx.wait();
      setMessage("Macro executed successfully.");
    } catch (error) {
      console.error("Error executing macro", error);
      setMessage(`Error: ${error.message}`);
    }
  };

  return (
    <div
      style={{
        textAlign: "center",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h2>Macro Forwarder Interface</h2>
      <h3>Connect Wallet to your chosen testnet (e.g. OP Sepolia)</h3>
      {walletAddress ? (
        <p>
          Connected Wallet: <strong>{walletAddress}</strong>
        </p>
      ) : (
        <button
          onClick={connectWallet}
          style={{
            backgroundColor: "#168c1e",
            color: "white",
            padding: "10px 15px",
            borderRadius: "5px",
            border: "none",
            cursor: "pointer",
          }}
        >
          Connect Wallet
        </button>
      )}
      <div style={{ margin: "10px" }}>
        {walletAddress && (
          <>
            <div>
              <input
                type="text"
                placeholder="SuperToken Address"
                value={superToken}
                onChange={(e) => setSuperToken(e.target.value)}
                style={{ margin: "5px", padding: "5px" }}
              />
              <input
                type="text"
                placeholder="Receiver Addresses (comma separated)"
                value={receivers}
                onChange={(e) => setReceivers(e.target.value)}
                style={{ margin: "5px", padding: "5px" }}
              />
            </div>
            <button onClick={executeMacro} style={{ margin: "10px" }}>
              Execute Macro
            </button>
            <p style={{ marginTop: "20px" }}>{message}</p>
          </>
        )}
      </div>
    </div>
  );
};

```

</p>
</details>
</div>

The `MacroForwarderComponent` is a simple React component that allows you to connect your wallet and execute the macro using EthersJS.
If you deployed your own `MultiFlowDeleteMacro` contract, you can use the `MacroForwarderComponent` to batch call the transactions by inputing
the `MacroForwarder` and `MultiFlowDeleteMacro` contract addresses in the playground below.

```jsx live
function MacroComponentExample() {

const macroForwarderAddress="0xFD0268E33111565dE546af2675351A4b1587F89F";
const userMacroAddress="0x997b37Fb47c489CF067421aEeAf7Be0543fA5362";
return (
    <div>
      <MacroForwarderComponent
      macroForwarderAddress={macroForwarderAddress}
      userDefinedMacroAddress={userMacroAddress}
      />
    </div>
  );
}
```

### Next Steps - EIP-712 Support

We will provide a guide which laverages [EIP-712](https://eips.ethereum.org/EIPS/eip-712) for typed structured data hashing and signing, enhancing the security and usability of macro transactions.
This will allow for the following features:

- On-chain verifiable signatures.
- Multilingual support for transaction signing.
- Supports meta transactions, allowing for gas-less transactions.
- And more...

---

<a id="doc_46"></a>

## 📁 sdk/distributions / Connecting and Claiming from the Pools

*파일 경로: sdk/distributions/connect-claim-pool.mdx*

---
sidebar_position: 2
---


This guide focuses on connecting and claiming from Superfluid [Distribution Pools](/docs/concepts/overview/distributions) using the `GDAv1Forwarder` contract.
You'll learn how to interact with Superfluid pools from client applications. We will specifically show how you can connect members to pools, and claim tokens from them.

### Interacting with the Superfluid Protocol

To interact with Superfluid's distribution pools from client applications, you'll use the `GDAv1Forwarder` contract. Here's how to set it up:

#### Contract ABI and Address

The `GDAv1Forwarder` contract address is the same on all Superfluid chains:

```
0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08
```

You can find the full ABI of the `GDAv1Forwarder` contract in the [GDAv1Forwarder technical reference](/docs/technical-reference/GDAv1Forwarder).

#### Setting up with ethers.js

Here's how to initiate interaction with the `GDAv1Forwarder` contract using ethers.js:

```javascript
import { ethers } from 'ethers';

// Assuming you have a provider set up (e.g., using MetaMask)
const provider = new ethers.providers.Web3Provider(window.ethereum);

// The address of the GDAv1Forwarder contract
const forwarderAddress = '0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08';

// The ABI of the GDAv1Forwarder contract (import this from the technical reference)
const forwarderABI = [...]; // Insert the ABI here

// Create a contract instance
const forwarderContract = new ethers.Contract(forwarderAddress, forwarderABI, provider.getSigner());
```

### Understanding Connecting and Claiming

When interacting with Superfluid pools, it's important to understand the difference between connecting to a pool and claiming from it:

1. **Connecting to a Pool**: 
   - When a member connects to a pool, they start receiving streams and transfers in real-time.
   - The member's balance will automatically reflect incoming tokens without any further action.
   - This is ideal for continuous, real-time token distribution.

2. **Claiming from a Pool**:
   - Claiming is the process of explicitly withdrawing accumulated tokens from the pool.
   - Members can claim periodically to move tokens from the pool to their personal balance.
   - This is useful for members who prefer to manually manage their token receipts or for specific accounting purposes.

In essence, connecting provides a passive, continuous flow of tokens, while claiming is an active process to withdraw accumulated tokens.

### Interacting with the GDAv1Forwarder Contract

Let's look at how to use the `GDAv1Forwarder` contract to connect, disconnect, and claim from pools.

#### Connecting to a Pool

To connect a member to a pool, use the `connectPool` function:

```solidity
function connectPool(
    ISuperfluidPool pool,
    bytes memory userData
) external returns (bool)
```

##### Parameters
- `pool`: The Superfluid Pool to connect.
- `userData`: User-specific data.

##### Usage Example

```javascript
const connectPool = async (poolAddress, userData = "0x") => {
  try {
    const tx = await forwarderContract.connectPool(poolAddress, userData);
    const receipt = await tx.wait();
    console.log("Successfully connected to pool");
    return receipt.status === 1; // 1 indicates success
  } catch (error) {
    console.error("Error connecting to pool:", error);
    return false;
  }
};
```

:::tip Connecting triggers a claim
When a member connects to a pool, the contract automatically claims all the previously available tokens for the member.
:::

#### Disconnecting from a Pool

To disconnect a member from a pool, use the `disconnectPool` function:

```solidity
function disconnectPool(
    ISuperfluidPool pool,
    bytes memory userData
) external returns (bool)
```

##### Parameters
- `pool`: The Superfluid Pool to disconnect.
- `userData`: User-specific data.

##### Usage Example

```javascript
const disconnectPool = async (poolAddress, userData = "0x") => {
  try {
    const tx = await forwarderContract.disconnectPool(poolAddress, userData);
    const receipt = await tx.wait();
    console.log("Successfully disconnected from pool");
    return receipt.status === 1; // 1 indicates success
  } catch (error) {
    console.error("Error disconnecting from pool:", error);
    return false;
  }
};
```

#### Claiming All Tokens from a Pool

To claim all available tokens for a member from a pool, use the `claimAll` function:

```solidity
function claimAll(
    ISuperfluidPool pool,
    address memberAddress,
    bytes memory userData
) external
```

##### Parameters
- `pool`: The Superfluid Pool to claim from.
- `memberAddress`: The address of the member to claim for.
- `userData`: User-specific data.

##### Usage Example

```javascript
const claimAll = async (poolAddress, memberAddress, userData = "0x") => {
  try {
    const tx = await forwarderContract.claimAll(poolAddress, memberAddress, userData);
    await tx.wait();
    console.log("Successfully claimed all tokens from pool");
    return true;
  } catch (error) {
    console.error("Error claiming tokens from pool:", error);
    return false;
  }
};
```

### Live UI Example for Pool Interaction

Here's an example of a UI component for connecting, disconnecting, and claiming from Superfluid pools:

```jsx live

function PoolInteractionManager() {
  const [poolAddress, setPoolAddress] = useState('');
  const [memberAddress, setMemberAddress] = useState('');
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');
  const toast = useToast();

  const forwarderAddress = '0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08';
  const forwarderABI = GDAv1ForwarderABI; // You will need to import the ABI in your code. You can do that from: https://docs.superfluid.finance/docs/technical-reference/CFAv1Forwarder

  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        setWalletConnected(true);
        toast({
          title: 'Wallet connected',
          description: `Connected to ${address}`,
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
      } catch (error) {
        console.error('Failed to connect wallet:', error);
        toast({
          title: 'Connection failed',
          description: 'Failed to connect wallet. Please try again.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    } else {
      toast({
        title: 'Metamask not detected',
        description: 'Please install Metamask to use this feature.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const performAction = async (action) => {
    if (!walletConnected) {
      toast({
        title: 'Wallet not connected',
        description: 'Please connect your wallet first.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(forwarderAddress, forwarderABI, signer);

    try {
      let tx;
      switch (action) {
        case 'connect':
          tx = await contract.connectPool(poolAddress, "0x");
          break;
        case 'disconnect':
          tx = await contract.disconnectPool(poolAddress, "0x");
          break;
        case 'claim':
          tx = await contract.claimAll(poolAddress, memberAddress || account, "0x");
          break;
      }
      await tx.wait();
      toast({
        title: 'Action successful',
        description: `Successfully ${action}ed ${action === 'claim' ? 'from' : 'to'} pool`,
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error(`Error ${action}ing:`, error);
      toast({
        title: 'Action failed',
        description: `Failed to ${action} ${action === 'claim' ? 'from' : 'to'} pool. Please try again.`,
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Box maxWidth="500px" margin="auto" padding="20px">
      <VStack spacing={4} align="stretch">
        <Text fontSize="2xl" fontWeight="bold" textAlign="center">Pool Interaction Manager</Text>
        
        {!walletConnected ? (
          <Button colorScheme="blue" onClick={connectWallet}>Connect Wallet</Button>
        ) : (
          <Text>Connected: {account}</Text>
        )}
        
        <Input
          placeholder="Pool Address"
          value={poolAddress}
          onChange={(e) => setPoolAddress(e.target.value)}
        />
        <Input
          placeholder="Member Address (for claiming, optional)"
          value={memberAddress}
          onChange={(e) => setMemberAddress(e.target.value)}
        />
        
        <HStack spacing={4}>
          <Button colorScheme="green" onClick={() => performAction('connect')} flex={1}>Connect to Pool</Button>
          <Button colorScheme="red" onClick={() => performAction('disconnect')} flex={1}>Disconnect from Pool</Button>
        </HStack>
        <Button colorScheme="blue" onClick={() => performAction('claim')}>Claim All Tokens</Button>
      </VStack>
    </Box>
  );
}
```

This UI provides the following features:

1. **Wallet Connection**: Users can connect their Ethereum wallet to interact with the Superfluid protocol.
2. **Connect to Pool**: Users can connect to a specified pool.
3. **Disconnect from Pool**: Users can disconnect from a specified pool.
4. **Claim All Tokens**: Users can claim all available tokens from a specified pool.
5. **Feedback**: Toast notifications inform users about the success or failure of their actions.

To use this component:

1. Click "Connect Wallet" to connect your Ethereum wallet.
2. Enter the pool address in the "Pool Address" field.
3. (Optional) Enter a member address in the "Member Address" field for claiming. If left empty, it will use the connected wallet's address.
4. Click the appropriate button to connect to a pool, disconnect from a pool, or claim all tokens.

Remember to replace the `forwarderABI` placeholder with the actual ABI of the `GDAv1Forwarder` contract.

This example provides a starting point for building a user interface to interact with Superfluid pools. In a production environment, you would want to add more robust error checking, input validation, and additional features like displaying pool information or showing the user's current pool connections.

:::tip the example does not work on your developer environment?
The example above is a live example and requires the ABI to be imported. In the case of this example, the ABI has already been imported through the live coder.

In order to make it work on your developer environment, head to the [GDAv1Forwarder technical reference](/docs/technical-reference/GDAv1Forwarder) and copy the ABI.
Then, replace the `forwarderABI` variable in the example with the ABI you copied.
:::

---

<a id="doc_47"></a>

## 📁 sdk/distributions / Create and Manage Distribution Pools

*파일 경로: sdk/distributions/create-manage-pools.mdx*

---
sidebar_position: 1
---


This guide explains how to create and manage [Distribution Pools](/docs/protocol/distributions/overview) in Superfluid using the `GDAv1Forwarder` contract.
Distribution pools are a key feature of Superfluid that enable scalable one-to-many and many-to-many transfers and streaming of tokens.

:::tip What are Distribution Pools?
Distribution pools are a mechanism for distributing tokens among multiple recipients.
They are managed by a pool admin who controls the pool's configuration and member units.
Pool members receive distributions based on their units in the pool.
To learn more about distribution pools, refer to the [Distributions Overview](/docs/protocol/distributions/overview).
:::

### Interacting with Distribution Pools from Client Applications

To interact with Superfluid's distribution pools from client applications, you'll use the [`GDAv1Forwarder`](/docs/technical-reference/GDAv1Forwarder) contract. Here's how to set it up:

#### Contract ABI and Address

The `GDAv1Forwarder` contract address is the same on all Superfluid chains:

```
0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08
```

You can find the full ABI of the `GDAv1Forwarder` contract in the [GDAv1Forwarder technical reference](/docs/technical-reference/GDAv1Forwarder).

#### Setting up with ethers.js

Here's how to initiate interaction with the `GDAv1Forwarder` contract using ethers.js:

```javascript
import { ethers } from 'ethers';

// Assuming you have a provider set up (e.g., using MetaMask)
const provider = new ethers.providers.Web3Provider(window.ethereum);

// The address of the GDAv1Forwarder contract
const forwarderAddress = '0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08';

// The ABI of the GDAv1Forwarder contract (import this from the technical reference)
const forwarderABI = [...]; // Insert the ABI here

// Create a contract instance
const forwarderContract = new ethers.Contract(forwarderAddress, forwarderABI, provider.getSigner());
```

### Understanding Distribution Pools

Distributions is a Superfluid primitive that allows scalable one-to-many or many-to-many transfer of value, in the form of discrete transfers or Money Streaming. Superfluid's implementation of this concept allows for the creation of **Pools** with a designated **pool admin** who manages **units** for **pool members**.

Key concepts:
- **Pool**: A mechanism for distributing tokens among multiple recipients.
- **Pool Admin**: The address that has control over the pool's configuration and member units.
- **Units**: A measure of a member's share in the pool's distributions.
- **Pool Members**: Addresses that receive distributions from the pool based on their units.

### Interacting with the GDAv1Forwarder Contract

Let's look at how to use the `GDAv1Forwarder` contract to create and manage distribution pools.

#### Creating a Pool

To create a new Superfluid Pool, use the `createPool` function:

```solidity
function createPool(
    ISuperfluidToken token,
    address admin,
    PoolConfig memory config
) external returns (bool success, ISuperfluidPool pool)
```

##### Parameters
- `token`: The Super Token address.
- `admin`: The pool admin address.
- `config`: The pool configuration (see below).

The `PoolConfig` struct is defined as follows:

```solidity
struct PoolConfig {
    bool transferabilityForUnitsOwner;
    bool distributionFromAnyAddress;
}
```
- `transferabilityForUnitsOwner`: If true, the pool members can transfer their owned units, else, only the pool admin can manipulate the units for pool members
- `distributionFromAnyAddress`: If true, anyone can execute distributions via the pool, else, only the pool admin can execute distributions via the pool

:::warning Strong recommendation
We don't recommend setting `transferabilityForUnitsOwner` to `true` unless you have a specific use case that absolutely requires it. This can sometimes lead to unexpected behavior and security risks.
:::

##### Usage Example

```javascript
const createPool = async (tokenAddress, adminAddress, config) => {
  try {
    const tx = await forwarderContract.createPool(tokenAddress, adminAddress, config);
    const receipt = await tx.wait();
    const [success, poolAddress] = receipt.events.find(e => e.event === 'PoolCreated').args;
    console.log("Pool created successfully:", poolAddress);
    return poolAddress;
  } catch (error) {
    console.error("Error creating pool:", error);
  }
};
```

#### Updating Member Units

To update the units of a pool member, use the `updateMemberUnits` function:

```solidity
function updateMemberUnits(
    ISuperfluidPool pool,
    address memberAddress,
    uint128 newUnits,
    bytes memory userData
) external
```

##### Parameters
- `pool`: The Superfluid Pool to update.
- `memberAddress`: The address of the member to update.
- `newUnits`: The new units of the member.
- `userData`: User-specific data.

##### Usage Example

```javascript
const updateMemberUnits = async (poolAddress, memberAddress, newUnits, userData) => {
  try {
    const tx = await forwarderContract.updateMemberUnits(poolAddress, memberAddress, newUnits, userData);
    await tx.wait();
    console.log("Member units updated successfully!");
  } catch (error) {
    console.error("Error updating member units:", error);
  }
};
```

### Live UI Example for Distribution Pool Management

Here's an example of a UI component for creating and managing distribution pools:

```jsx live
function DistributionPoolManager() {
  const [tokenAddress, setTokenAddress] = useState('');
  const [adminAddress, setAdminAddress] = useState('');
  const [poolAddress, setPoolAddress] = useState('');
  const [memberAddress, setMemberAddress] = useState('');
  const [newUnits, setNewUnits] = useState('');
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');
  const toast = useToast();

  const forwarderAddress = '0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08';
  const forwarderABI = GDAv1ForwarderABI; // You will need to import the ABI in your code. You can do that from: https://docs.superfluid.finance/docs/technical-reference/CFAv1Forwarder

  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        setWalletConnected(true);
        toast({
          title: 'Wallet connected',
          description: `Connected to ${address}`,
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
      } catch (error) {
        console.error('Failed to connect wallet:', error);
        toast({
          title: 'Connection failed',
          description: 'Failed to connect wallet. Please try again.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    } else {
      toast({
        title: 'Metamask not detected',
        description: 'Please install Metamask to use this feature.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const createPool = async () => {
    if (!walletConnected) {
      toast({
        title: 'Wallet not connected',
        description: 'Please connect your wallet first.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(forwarderAddress, forwarderABI, signer);

    try {
      // For simplicity, we're using a basic pool configuration here
      const config = {
        transferabilityForUnitsOwner: 0, // Non-transferable
        distributionFromAnyAddress: false
      };
      
      const tx = await contract.createPool(tokenAddress, adminAddress, config);
      const receipt = await tx.wait();
      const [success, poolAddress] = receipt.events.find(e => e.event === 'PoolCreated').args;
      
      setPoolAddress(poolAddress);
      toast({
        title: 'Pool created',
        description: `Pool created successfully at ${poolAddress}`,
        status: 'success',
        duration: 5000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Error creating pool:', error);
      toast({
        title: 'Error',
        description: 'Failed to create pool. Please try again.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const updateMemberUnits = async () => {
    if (!walletConnected) {
      toast({
        title: 'Wallet not connected',
        description: 'Please connect your wallet first.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(forwarderAddress, forwarderABI, signer);

    try {
      const tx = await contract.updateMemberUnits(poolAddress, memberAddress, newUnits, "0x");
      await tx.wait();
      toast({
        title: 'Units updated',
        description: 'Member units updated successfully',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Error updating member units:', error);
      toast({
        title: 'Error',
        description: 'Failed to update member units. Please try again.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Box maxWidth="500px" margin="auto" padding="20px">
      <VStack spacing={4} align="stretch">
        <Text fontSize="2xl" fontWeight="bold" textAlign="center">Distribution Pool Manager</Text>
        
        {!walletConnected ? (
          <Button colorScheme="blue" onClick={connectWallet}>Connect Wallet</Button>
        ) : (
          <Text>Connected: {account}</Text>
        )}
        
        <Text fontSize="xl" fontWeight="bold">Create Pool</Text>
        <Input
          placeholder="Token Address"
          value={tokenAddress}
          onChange={(e) => setTokenAddress(e.target.value)}
        />
        <Input
          placeholder="Admin Address"
          value={adminAddress}
          onChange={(e) => setAdminAddress(e.target.value)}
        />
        <Button colorScheme="green" onClick={createPool}>Create Pool</Button>
        
        <Text fontSize="xl" fontWeight="bold" mt={4}>Update Member Units</Text>
        <Input
          placeholder="Pool Address"
          value={poolAddress}
          onChange={(e) => setPoolAddress(e.target.value)}
        />
        <Input
          placeholder="Member Address"
          value={memberAddress}
          onChange={(e) => setMemberAddress(e.target.value)}
        />
        <Input
          placeholder="New Units"
          value={newUnits}
          onChange={(e) => setNewUnits(e.target.value)}
        />
        <Button colorScheme="blue" onClick={updateMemberUnits}>Update Member Units</Button>
      </VStack>
    </Box>
  );
}
```

This UI provides the following features:

1. **Wallet Connection**: Users can connect their Ethereum wallet to interact with the Superfluid protocol.
2. **Create Pool**: Users can create a new distribution pool by providing the token address and admin address.
3. **Update Member Units**: Users can update the units of a pool member by providing the pool address, member address, and new units.
4. **Feedback**: Toast notifications inform users about the success or failure of their actions.

To use this component:

1. Click "Connect Wallet" to connect your Ethereum wallet.
2. To create a pool, enter the token address and admin address, then click "Create Pool".
3. To update member units, enter the pool address, member address, and new units, then click "Update Member Units".

This example provides a starting point for building a user interface to manage distribution pools in Superfluid. In a production environment, you would want to add more robust error checking, input validation, and additional features like displaying pool information or listing pool members.

:::tip the example does not work on your developer environment?
The example above is a live example and requires the ABI to be imported. In the case of this example, the ABI has already been imported through the live coder.

In order to make it work on your developer environment, head to the [GDAv1Forwarder technical reference](/docs/technical-reference/GDAv1Forwarder) and copy the ABI.
Then, replace the `forwarderABI` variable in the example with the ABI you copied.
:::

---

<a id="doc_48"></a>

## 📁 sdk/distributions / Subgraph

*파일 경로: sdk/distributions/subgraph.mdx*

---
sidebar_position: 4
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';


The Graph is the indexing layer of our industry, providing a queryable platform for the vast data produced by blockchain networks. The Graph can be used for querying data in the Superfluid ecosystem and other on-chain data. Experiment with queries using the [GraphQL Playground](https://thegraph.com/hosted-service/).

<Admonition type="tip" title="New to GraphQL?">

Before diving into subgraph queries, familiarize yourself with GraphQL basics:
[Learn GraphQL](https://graphql.org/learn/)

</Admonition>

### Querying Different Networks

#### Superfluid Explorer

The Superfluid Explorer is an interactive interface for exploring the Superfluid Protocol and interacting with its Subgraph. It provides an intuitive way to query on-chain data, get contract addresses, and manage your Superfluid finances. The console supports various blockchain networks, allowing you to seamlessly switch between them and access specific data sets. Whether you're analyzing streams, checking balances, or staying up to date with the new deployments. The Superfluid Explorer makes these tasks accessible and straightforward.

Explore Superfluid data across various networks using the Superfluid Explorer. Select a network to start querying:

<Tabs
  defaultValue="popular"
  values={[
    {label: 'Popular', value: 'popular'},
    {label: 'Other', value: 'other'},
  ]}>
  
  <TabItem value="popular">
    <div style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap' }}>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=ethereum"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Ethereum
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=matic"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Polygon
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=avalanche"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Avalanche
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=optimism"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Optimism
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=arbitrum"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Arbitrum
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=binance-smart-chain"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Binance Smart Chain
      </a>
    </div>
  </TabItem>
  <TabItem value="other">
    <p>For other networks, use the Superfluid Explorer:</p>
    <a 
      href="https://console.superfluid.finance/"
      className="button-link"
      style={{
        backgroundColor: 'green',
        color: 'white',
        padding: '10px 20px',
        textDecoration: 'none',
        borderRadius: '4px',
        display: 'inline-block'
      }}
    >
      Superfluid Explorer
    </a>
  </TabItem>
</Tabs>

#### Subgraph Networks

You can have the full list of available subgraph endpoints in the [Subgraph Endpoints](/docs/technical-reference/subgraph) page.

### Resources

- **Subgraph Queries**: [Guide on Querying the Graph](https://thegraph.com/docs/en/developer/query-the-graph/)
- **Deploy a Subgraph**: [Creating a Subgraph](https://thegraph.com/docs/en/developer/create-subgraph-hosted/)
- **GraphQL Schema**: [Superfluid Schema](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/subgraph/schema.graphql)
- **Our Subgraph Endpoints**: [Subgraph Endpoints](/docs/technical-reference/subgraph)


### Helpful Tips

- All addresses in the subgraph (`id`, `underlyingAddress`, etc.) are lowercase.
- Convert addresses to lowercase before querying.

#### Notable Breaking Changes

<Admonition type="caution" title="Migrating From Legacy Subgraph to V1">

Significant changes were made in October 2021:

- `totalSubscriptions` is now `totalSubscriptionsWithUnits`.
- `Subscriber` entity changed to `Subscription`.
- `createdAt` and `updatedAt` fields are now `createdAtTimestamp` and `updatedAtTimestamp`.

</Admonition>

### Schema Overview

The Superfluid Subgraph includes various entities for querying. Think of entities as analogous to database tables. Here's a brief overview:

#### Event Entities

Event entities correspond to contract events, often with added data. Each event entity is immutable and created once.

- **Event ID Format**: `eventName-transactionHash-logIndex`.
- **Naming Convention**: For V1, event names end with 'Event'.

#### Higher Order Level Entities (HOL)

HOL entities represent entities over their lifetime and may be updated.

- **`Account`**: Represents any address interacting with Superfluid.
- **`Token`**: Represents valid SuperTokens.
- **`Pool`**, **`PoolMember`**, **`Stream`**, **`StreamPeriod`**: Related to Superfluid streams and [pools](/docs/protocol/distributions/guides/pools.mdx).

#### Aggregate Entities

Aggregate entities store cumulative data at both account-token and global token levels:

- **`TokenStatistic`**: Aggregates data for a single Token type.
- **`AccountTokenSnapshot`**: Aggregates data on an account's interaction with a token.

### Query Examples

#### Super Token Data Query

```javascript
{
  tokens(first: 100) {
    id
    symbol
    name
    underlyingAddress
  }
}
```
#### Get the pools that a user is a member of

To list all pools that an account is currently a member (insert the ethereum address in the query below):

```javascript
query MyQuery {
  pools(
    first: 10
    where: {poolMembers_: {account: "YOUR_ADDRESS_HERE", account_: {}}}
  ) {
    totalUnits
    totalMembers
    flowRate
    createdAtBlockNumber
  }
}
```

#### Get all the pools for a specific token

To list all pools for a token (insert the token address in the query below):

```javascript
query MyQuery {
  pools(where: {token: "YOUR_TOKEN_ADDRESS_HERE"}) {
    createdAtBlockNumber
    createdAtTimestamp
    flowRate
    id
    totalMembers
    totalUnits
    admin {
      isSuperApp
    }
  }
}
```
#### Get all the pools for a specific pool admin

To list all pools for a pool admin (insert the pool admin address in the query below):

```javascript
query MyQuery {
  pools(first: 10, where: {admin: "YOUR_POOL_ADMIN_ADDRESS_HERE"}) {
    totalUnits
    totalMembers
    flowRate
    createdAtBlockNumber
    token {
      id
      isSuperToken
      symbol
    }
  }
}
```

### Explore more queries

Explore more queries using the [Superfluid Subgraph Playground](https://console.superfluid.finance/subgraph).

---

<a id="doc_49"></a>

## 📁 sdk/examples / Rewards Distribution Using Macros

*파일 경로: sdk/examples/example1.mdx*

---
sidebar_position: 1
---


This guide will walk you through creating a web application that enables
streaming reward distributions using Superfluid's [Distribution Pools](/docs/protocol/distributions/overview) and Macro for [Batching Calls](/docs/sdk/advanced-topics/batch-calls).

:::tip
If you want to see the full example, you can check it out in the [GitHub Repository](https://github.com/superfluid-finance/rewards-macro-example).
:::

### Overview

The application we'll build allows users to:
- Connect their wallet and validate network
- Select a Superfluid pool
- Add multiple recipients with their respective units
- Set a flow rate for rewards
- Execute all operations in a single transaction

### Prerequisites

Before starting, ensure you have:
- Basic knowledge of React and TypeScript
- Node.js installed
- A Web3 wallet (like MetaMask)
- Some ETH on Optimism Sepolia network

### Setting Up the Project

1. Create a new Next.js project:
```bash
npx create-next-app@latest rewards-distribution --typescript --tailwind
cd rewards-distribution
```

2. Install dependencies:
```bash
npm install ethers@6 @superfluid-finance/sdk-core
```

3. Install UI components:
```bash
npx shadcn-ui@latest init
```

### Understanding the Core Concepts

#### Superfluid Distribution Pools

[Distribution Pools](/docs/protocol/distributions/overview) allow for proportional distribution of streaming tokens. Think of it as a smart contract that:
- Manages a pool of tokens
- Distributes streams based on units assigned to recipients
- Handles all the complex token streaming logic

:::tip
To deploy a Distribution Pool, you can use the [GDAv1Forwarder](/docs/technical-reference/GDAv1Forwarder).
:::

#### Superfluid Macros

[Macros](/docs/sdk/advanced-topics/batch-calls) allow us to batch multiple operations into a single transaction. In our case, we're using:
- `MacroForwarder`: Contract that executes our macro
- [`RewardsMacro`](https://github.com/superfluid-finance/rewards-macro-example/blob/main/contracts/RewardsMacro.sol): Our custom macro for setting up distributions

In our example, we deployed a [`RewardsMacro`](https://github.com/superfluid-finance/rewards-macro-example/blob/main/contracts/RewardsMacro.sol) contract on [OP Sepolia](https://optimism-sepolia.blockscout.com/address/0xA315e7EB0a278fac7B3a74DB895f5bf801EAb632?tab=contract) for the purposes of our example.

### Key Components

#### 1. Network Management

First, we need to ensure users are on the correct network:

```typescript
const OP_SEPOLIA_CHAIN_ID = "0xaa37dc" // 11155420 in hex

const switchToOpSepolia = async () => {
  try {
    await window.ethereum.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId: OP_SEPOLIA_CHAIN_ID }],
    });
    return true;
  } catch (switchError) {
    // Handle network switch error
  }
}
```

#### 2. Pool Validation

We validate the pool address and check user's balance:

```typescript
const POOL_ABI = ["function superToken() external view returns (ISuperfluidToken)"]
const SUPER_TOKEN_ABI = ["function balanceOf(address account) external view returns (uint256)"]

const checkPoolAndBalance = async () => {
  const poolContract = new ethers.Contract(poolAddress, POOL_ABI, provider);
  const tokenAddress = await poolContract.superToken();
  const tokenContract = new ethers.Contract(tokenAddress, SUPER_TOKEN_ABI, provider);
  const balance = await tokenContract.balanceOf(userAddress);
  // Handle results
}
```

#### 3. Reward Distribution Setup

The core functionality uses the RewardsMacro contract:

```typescript
const executeRewardsMacro = async () => {
  // Parse recipients and units
  const receivers = [...] // Array of addresses
  const units = [...] // Array of BigInts
  
  // Convert flow rate from tokens/day to wei/second
  const weiBigInt = ethers.parseEther(flowRatePerDay)
  const flowRateWeiPerSecond = weiBigInt / BigInt(86400)
  
  // Get macro parameters
  const params = await rewardsMacro.getParams(
    poolAddress,
    receivers,
    units,
    flowRateWeiPerSecond
  )
  
  // Execute through MacroForwarder
  await macroForwarder.runMacro(REWARDS_MACRO, params)
}
```

### User Interface

<div style={{ display: 'flex', justifyContent: 'center' }}>
    <img src="/img/example-ui.png" alt="Example UI" width="600" />
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Screenshot of the UI*</p>
</div>

The UI is built with Tailwind CSS and shadcn/ui components. Key features include:
- Network status indicator
- Pool validation feedback
- Balance display
- Recipients input area
- Flow rate input with conversion

```typescript
<Card className="max-w-2xl mx-auto bg-gray-800">
  <CardHeader>
    <CardTitle>Reward Stream Distribution</CardTitle>
  </CardHeader>
  <CardContent>
    {/* Network Check */}
    {/* Pool Input */}
    {/* Recipients Input */}
    {/* Flow Rate Input */}
    {/* Execute Button */}
  </CardContent>
</Card>
```

### Testing the Application

1. Deploy the contract and set up your pool
   - Deploy the `RewardsMacro` contract on your desired network (you can use the contract deployed on [OP Sepolia](https://optimism-sepolia.blockscout.com/address/0xA315e7EB0a278fac7B3a74DB895f5bf801EAb632?tab=contract))
   - Create your pool using the [GDAv1Forwarder](/docs/technical-reference/GDAv1Forwarder)
   - Ensure you use the correct Super Token for your pool (in our example, we used the [Super fake DAI](https://optimism-sepolia.blockscout.com/address/0x7f5c765057ef45c28ae624f7b77854c32c201422?tab=contract) Super Token)

2. Test the flow:
   - Connect wallet
   - Enter pool address
   - Add recipients
   - Set flow rate
   - Execute distribution

### Common Issues and Solutions

#### Invalid Pool Address
```typescript
try {
  await poolContract.superToken()
} catch (e) {
  // Handle invalid pool
}
```

#### Insufficient Balance
```typescript
if (Number(userBalance) === 0) {
  // Disable execution
  // Show warning
}
```

#### Network Issues
```typescript
if (chainId !== OP_SEPOLIA_CHAIN_ID) {
  await switchToOpSepolia()
}
```

### Next Steps

Consider extending the application with:
- Multiple network support
- Distribution history
- Analytics dashboard

---

<a id="doc_50"></a>

## 📁 sdk/money-streaming / Create, Update, and Delete Flows

*파일 경로: sdk/money-streaming/create-update-delete-flow.mdx*

---
sidebar_position: 1
---


This guide covers various methods for managing flows in Superfluid from your client application side.
This guide will not cover how to interact with the protocol from another smart contract. 
For that, please refer to the [Create, Update, and Delete Flows guide](/docs/protocol/money-streaming/guides/create-update-delete-flow) in the Contracts section.

### Prerequisites

Before proceeding, ensure you have:

* Familiarity with JavaScript (and an EVM framework such as ethers.js, viem or wagmi).
* Basic understanding of Superfluid and its functionalities.
* Access to a development environment for developing client applications.

### What is a flow?
In Superfluid terminology, a flow is a continuous stream of tokens from one account to another.
It is a fundamental concept in the Superfluid protocol, enabling real-time, continuous payments between accounts.

:::tip What is the difference between a "Stream" and a "Flow"?
This is a small technicality which is not necessarily important to understand.
However, in Superfluid, a "Flow" is a more general term than a "Stream".
A Stream is a non-zero flow, while a zero flow is not considered a Stream.
:::

### How to interact with the Superfluid protocol from a client application?
There are mainly two ways to interact with the Superfluid protocol from a client application:
- The [`CFAv1Forwarder`](/docs/technical-reference/CFAv1Forwarder) contract: This contract is used to create, update, and delete flows.
- The [`GDAv1Forwarder`](/docs/technical-reference/GDAv1Forwarder) contract: This contract is used to create and manage Distribution Pools.

For the purposes of this guide, we will focus on the [`CFAv1Forwarder`](/docs/technical-reference/CFAv1Forwarder) contract which allows you to create, update, and delete flows.

:::tip Where does the name CFAv1Forwarder come from?
The name `CFAv1Forwarder` is derived from the term "Constant Flow Agreement" (CFA) which is the underlying agreement that governs Money Streaming in Superfluid.
:::

### Interacting with the CFAv1Forwarder Contract

To interact with Money Streaming, you'll need to use the `CFAv1Forwarder` contract. Here's how to get started:

#### Contract ABI and Address

You can find the full ABI of the `CFAv1Forwarder` contract in the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder).

The `CFAv1Forwarder` contract address is the same on all networks:

```
0xcfA132E353cB4E398080B9700609bb008eceB125
```

#### Initiating Contract Interaction with ethers.js

Here's an example of how to initiate interaction with the `CFAv1Forwarder` contract using ethers.js:

```javascript
import { ethers } from 'ethers';

// Assuming you have a provider set up (e.g., using MetaMask)
const provider = new ethers.providers.Web3Provider(window.ethereum);

// The address of the CFAv1Forwarder contract
const forwarderAddress = '0xcfA132E353cB4E398080B9700609bb008eceB125';

// The ABI of the CFAv1Forwarder contract (import this from the technical reference)
const forwarderABI = [...]; // Insert the ABI here

// Create a contract instance
const forwarderContract = new ethers.Contract(forwarderAddress, forwarderABI, provider.getSigner());
```

Now that we have our contract instance set up, let's look at how to create, update, and delete flows.

### Creating a Flow

To create a new flow, you can use the `createFlow` function of the `CFAv1Forwarder` contract.

#### Function Signature

```solidity
function createFlow(
    ISuperToken token,
    address sender,
    address receiver,
    int96 flowrate,
    bytes userData
) external returns (bool)
```

#### Parameters

- `token`: The address of the Super Token you want to stream.
- `sender`: The address that will be sending the tokens.
- `receiver`: The address that will be receiving the tokens.
- `flowrate`: The rate at which tokens will be streamed, in tokens per second (using 18 decimal places).
- `userData`: (Optional) Additional data to include with the transaction. Use "0x" if not needed.

#### Example Usage

```javascript
const createFlow = async (tokenAddress, receiver, flowRate) => {
  try {
    const tx = await forwarderContract.createFlow(
      tokenAddress,
      await provider.getSigner().getAddress(), // sender (current user)
      receiver,
      flowRate,
      "0x" // no user data
    );
    await tx.wait();
    console.log("Flow created successfully!");
  } catch (error) {
    console.error("Error creating flow:", error);
  }
};
```
:::tip using setFlowrate instead
You can also use the `setFlowrate` function to update the flow rate of an existing flow.
For a full list of functions available in the `CFAv1Forwarder` contract, refer to the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder).
:::

### Updating a Flow

To update an existing flow, use the `updateFlow` function.

#### Function Signature

```solidity
function updateFlow(
    ISuperToken token,
    address sender,
    address receiver,
    int96 flowrate,
    bytes userData
) external returns (bool)
```

#### Parameters

The parameters are the same as for `createFlow`. The `flowrate` parameter specifies the new flow rate.

#### Example Usage

```javascript
const updateFlow = async (tokenAddress, receiver, newFlowRate) => {
  try {
    const tx = await forwarderContract.updateFlow(
      tokenAddress,
      await provider.getSigner().getAddress(), // sender (current user)
      receiver,
      newFlowRate,
      "0x" // no user data
    );
    await tx.wait();
    console.log("Flow updated successfully!");
  } catch (error) {
    console.error("Error updating flow:", error);
  }
};
```
:::tip using setFlowrate instead
You can also use the `setFlowrate` function to update the flow rate of an existing flow.
For a full list of functions available in the `CFAv1Forwarder` contract, refer to the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder).
:::

### Deleting a Flow

To stop and delete an existing flow, use the `deleteFlow` function.

#### Function Signature

```solidity
function deleteFlow(
    ISuperToken token,
    address sender,
    address receiver,
    bytes userData
) external returns (bool)
```

#### Parameters

- `token`: The address of the Super Token of the flow you want to delete.
- `sender`: The address that is sending the tokens in the flow.
- `receiver`: The address that is receiving the tokens in the flow.
- `userData`: (Optional) Additional data to include with the transaction. Use "0x" if not needed.

#### Example Usage

```javascript
const deleteFlow = async (tokenAddress, receiver) => {
  try {
    const tx = await forwarderContract.deleteFlow(
      tokenAddress,
      await provider.getSigner().getAddress(), // sender (current user)
      receiver,
      "0x" // no user data
    );
    await tx.wait();
    console.log("Flow deleted successfully!");
  } catch (error) {
    console.error("Error deleting flow:", error);
  }
};
```

:::tip using setFlowrate instead
You can also use the `setFlowrate` function to update the flow rate of an existing flow.
For a full list of functions available in the `CFAv1Forwarder` contract, refer to the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder).
:::


### Building a Simple UI

Here's an example of how you might build a simple UI to interact with these functions:

```jsx live
function FlowManager() {
  const [tokenAddress, setTokenAddress] = useState('');
  const [receiver, setReceiver] = useState('');
  const [flowRate, setFlowRate] = useState('');
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');
  const toast = useToast();

  const forwarderAddress = '0xcfA132E353cB4E398080B9700609bb008eceB125';
  const forwarderABI = CFAv1ForwarderABI; // You will need to import the ABI in your code. You can do that from: https://docs.superfluid.finance/docs/technical-reference/CFAv1Forwarder

  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        setWalletConnected(true);
        toast({
          title: 'Wallet connected',
          description: `Connected to ${address}`,
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
      } catch (error) {
        console.error('Failed to connect wallet:', error);
        toast({
          title: 'Connection failed',
          description: 'Failed to connect wallet. Please try again.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    } else {
      toast({
        title: 'Metamask not detected',
        description: 'Please install Metamask to use this feature.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const handleFlow = async (action) => {
    if (!walletConnected) {
      toast({
        title: 'Wallet not connected',
        description: 'Please connect your wallet first.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(forwarderAddress, forwarderABI, signer);

    try {
      let tx;
      switch (action) {
        case 'create':
          tx = await contract.createFlow(tokenAddress, account, receiver, flowRate, "0x");
          break;
        case 'update':
          tx = await contract.updateFlow(tokenAddress, account, receiver, flowRate, "0x");
          break;
        case 'delete':
          tx = await contract.deleteFlow(tokenAddress, account, receiver, "0x");
          break;
      }
      await tx.wait();
      toast({
        title: 'Transaction successful',
        description: `Flow ${action}d successfully!`,
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error(`Error ${action}ing flow:`, error);
      toast({
        title: 'Transaction failed',
        description: `Failed to ${action} flow. Please try again.`,
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Box maxWidth="500px" margin="auto" padding="20px">
      <VStack spacing={4} align="stretch">
        <Text fontSize="2xl" fontWeight="bold" textAlign="center">Flow Manager</Text>
        
        {!walletConnected ? (
          <Button colorScheme="blue" onClick={connectWallet}>Connect Wallet</Button>
        ) : (
          <Text>Connected: {account}</Text>
        )}
        
        <Input
          placeholder="Token Address"
          value={tokenAddress}
          onChange={(e) => setTokenAddress(e.target.value)}
        />
        <Input
          placeholder="Receiver Address"
          value={receiver}
          onChange={(e) => setReceiver(e.target.value)}
        />
        <Input
          placeholder="Flow Rate"
          value={flowRate}
          onChange={(e) => setFlowRate(e.target.value)}
        />
        
        <HStack spacing={4}>
          <Button colorScheme="green" onClick={() => handleFlow('create')} flex={1}>Create Flow</Button>
          <Button colorScheme="yellow" onClick={() => handleFlow('update')} flex={1}>Update Flow</Button>
          <Button colorScheme="red" onClick={() => handleFlow('delete')} flex={1}>Delete Flow</Button>
        </HStack>
      </VStack>
    </Box>
  );
}
```

This UI provides input fields for the token address, receiver address, and flow rate, along with buttons to create, update, and delete flows. You would need to implement the `createFlow`, `updateFlow`, and `deleteFlow` functions as shown in the previous examples.

:::tip the example does not work on your developer environment?
The example above is a live example and requires the ABI to be imported. In the case of this example, the ABI has already been imported through the live coder.

In order to make it work on your developer environment, head to the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder) and copy the ABI.
Then, replace the `forwarderABI` variable in the example with the ABI you copied.
:::

---

<a id="doc_51"></a>

## 📁 sdk/money-streaming / Manage Access Control and User Data

*파일 경로: sdk/money-streaming/acl-user-data.mdx*

---
sidebar_position: 2
---


This guide explains how to manage access control and user data in the Superfluid protocol from your client applications:
- Access control allows you to delegate flow management to another account
- User data lets you attach additional information to transactions.

### Interacting with the Superfluid Protocol

To interact with the Superfluid protocol from client applications, you'll use the [`CFAv1Forwarder`](/docs/technical-reference/CFAv1Forwarder) contract.
In the case of a JavaScript/TypeScript based application, here's how to set it up:

#### Contract ABI and Address

The `CFAv1Forwarder` contract address is the same on all networks:

```
0xcfA132E353cB4E398080B9700609bb008eceB125
```

You can find the full ABI of the `CFAv1Forwarder` contract in the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder).

#### Setting up with ethers.js

Here's how to initiate interaction with the `CFAv1Forwarder` contract using ethers.js:

```javascript
import { ethers } from 'ethers';

// Assuming you have a provider set up (e.g., using MetaMask)
const provider = new ethers.providers.Web3Provider(window.ethereum);

// The address of the CFAv1Forwarder contract
const forwarderAddress = '0xcfA132E353cB4E398080B9700609bb008eceB125';

// The ABI of the CFAv1Forwarder contract (import this from the technical reference)
const forwarderABI = [...]; // Insert the ABI here

// Create a contract instance
const forwarderContract = new ethers.Contract(forwarderAddress, forwarderABI, provider.getSigner());
```

### Access Control in Superfluid

Access control in Superfluid allows one account (the flow operator) to manage flows on behalf of another account. This is particularly useful for automated systems, multi-sig wallets, or any scenario where you want to delegate flow management.

Key concepts:
- **Flow Operator**: An account that has been granted permissions to manage flows on behalf of another account.
- **Permissions**: The specific actions a flow operator is allowed to perform (create, update, delete flows).
- **Flow Rate Allowance**: The maximum net flow rate a flow operator can create on behalf of the account.

### User Data in Superfluid

User data in Superfluid allows you to attach additional information to transactions. This can be used for various purposes:
- Including metadata with transactions
- Triggering specific logic in receiver contracts
- Implementing off-chain systems that react to on-chain events

User data is typically passed as a `bytes` parameter in Superfluid functions, allowing you to encode any type of data you need.

### Key Functions for Access Control (with User Data)

#### grantPermissions

Grants permissions to a flow operator to manage flows on behalf of the caller.

```solidity
function grantPermissions(
    ISuperToken token,
    address flowOperator
) external returns (bool)
```

##### Parameters
- `token`: The Super Token address
- `flowOperator`: The account to which permissions are granted

##### Usage Example

```javascript
const grantPermissions = async (tokenAddress, flowOperatorAddress) => {
  try {
    const tx = await forwarderContract.grantPermissions(tokenAddress, flowOperatorAddress);
    await tx.wait();
    console.log("Permissions granted successfully!");
  } catch (error) {
    console.error("Error granting permissions:", error);
  }
};
```

#### revokePermissions

Revokes all permissions previously granted to a flow operator.

```solidity
function revokePermissions(
    ISuperToken token,
    address flowOperator
) external returns (bool)
```

##### Parameters
- `token`: The Super Token address
- `flowOperator`: The account from which permissions are revoked

##### Usage Example

```javascript
const revokePermissions = async (tokenAddress, flowOperatorAddress) => {
  try {
    const tx = await forwarderContract.revokePermissions(tokenAddress, flowOperatorAddress);
    await tx.wait();
    console.log("Permissions revoked successfully!");
  } catch (error) {
    console.error("Error revoking permissions:", error);
  }
};
```

#### setFlowrateFrom

Allows a flow operator to set the flow rate from one account to another.

```solidity
function setFlowrateFrom(
    ISuperToken token,
    address sender,
    address receiver,
    int96 flowrate
) external returns (bool)
```

##### Parameters
- `token`: The Super Token address
- `sender`: The sender of the flow
- `receiver`: The receiver of the flow
- `flowrate`: The desired flow rate in tokens per second (using 18 decimal places)

##### Usage Example

```javascript
const setFlowrateFrom = async (tokenAddress, senderAddress, receiverAddress, flowRate) => {
  try {
    const tx = await forwarderContract.setFlowrateFrom(tokenAddress, senderAddress, receiverAddress, flowRate);
    await tx.wait();
    console.log("Flow rate set successfully!");
  } catch (error) {
    console.error("Error setting flow rate:", error);
  }
};
```

### Live UI Example for Access Control List Management

Here's an example of a UI component for managing access control lists:

```jsx live
function AccessControlManager() {
  const [tokenAddress, setTokenAddress] = useState('');
  const [flowOperator, setFlowOperator] = useState('');
  const [sender, setSender] = useState('');
  const [receiver, setReceiver] = useState('');
  const [flowRate, setFlowRate] = useState('');
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');
  const toast = useToast();
  
  const forwarderAddress = '0xcfA132E353cB4E398080B9700609bb008eceB125';
  const forwarderABI = CFAv1ForwarderABI; // You will need to import the ABI in your code. You can do that from: https://docs.superfluid.finance/docs/technical-reference/CFAv1Forwarder


  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        setWalletConnected(true);
        toast({
          title: 'Wallet connected',
          description: `Connected to ${address}`,
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
      } catch (error) {
        console.error('Failed to connect wallet:', error);
        toast({
          title: 'Connection failed',
          description: 'Failed to connect wallet. Please try again.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    } else {
      toast({
        title: 'Metamask not detected',
        description: 'Please install Metamask to use this feature.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const handleAction = async (action) => {
    if (!walletConnected) {
      toast({
        title: 'Wallet not connected',
        description: 'Please connect your wallet first.',
        status: 'warning',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(forwarderAddress, forwarderABI, signer);

    try {
      let tx;
      switch (action) {
        case 'grant':
          tx = await contract.grantPermissions(tokenAddress, flowOperator);
          break;
        case 'revoke':
          tx = await contract.revokePermissions(tokenAddress, flowOperator);
          break;
        case 'setFlowrate':
          tx = await contract.setFlowrateFrom(tokenAddress, sender, receiver, flowRate);
          break;
      }
      await tx.wait();
      toast({
        title: 'Transaction successful',
        description: `${action} action completed successfully!`,
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error(`Error performing ${action} action:`, error);
      toast({
        title: 'Transaction failed',
        description: `Failed to ${action}. Please try again.`,
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Box maxWidth="500px" margin="auto" padding="20px">
      <VStack spacing={4} align="stretch">
        <Text fontSize="2xl" fontWeight="bold" textAlign="center">Access Control Manager</Text>
        
        {!walletConnected ? (
          <Button colorScheme="blue" onClick={connectWallet}>Connect Wallet</Button>
        ) : (
          <Text>Connected: {account}</Text>
        )}
        
        <Input
          placeholder="Token Address"
          value={tokenAddress}
          onChange={(e) => setTokenAddress(e.target.value)}
        />
        <Input
          placeholder="Flow Operator Address"
          value={flowOperator}
          onChange={(e) => setFlowOperator(e.target.value)}
        />
        <Input
          placeholder="Sender Address (for setFlowrateFrom)"
          value={sender}
          onChange={(e) => setSender(e.target.value)}
        />
        <Input
          placeholder="Receiver Address (for setFlowrateFrom)"
          value={receiver}
          onChange={(e) => setReceiver(e.target.value)}
        />
        <Input
          placeholder="Flow Rate (for setFlowrateFrom)"
          value={flowRate}
          onChange={(e) => setFlowRate(e.target.value)}
        />
        
        <HStack spacing={4}>
          <Button colorScheme="green" onClick={() => handleAction('grant')} flex={1}>Grant Permissions</Button>
          <Button colorScheme="red" onClick={() => handleAction('revoke')} flex={1}>Revoke Permissions</Button>
        </HStack>
        <Button colorScheme="blue" onClick={() => handleAction('setFlowrate')}>Set Flowrate From</Button>
      </VStack>
    </Box>
  );
}
```

This UI provides the following features:

1. **Wallet Connection**: Users can connect their Ethereum wallet to interact with the Superfluid protocol.
2. **Input Fields**: Users can enter the token address, flow operator address, sender address, receiver address, and flow rate.
3. **Action Buttons**: Separate buttons for granting permissions, revoking permissions, and setting flow rate.
4. **Feedback**: Toast notifications to inform users about the success or failure of their actions.

To use this component:

1. Click "Connect Wallet" to connect your Ethereum wallet.
2. Enter the required information in the input fields.
3. Click the appropriate button to perform the desired action (grant permissions, revoke permissions, or set flow rate).

This example provides a starting point for building a user interface to manage access control in Superfluid. In a production environment, you would want to add more robust error checking, input validation, and possibly additional features like displaying current permissions or flow rates.

:::tip the example does not work on your developer environment?
The example above is a live example and requires the ABI to be imported. In the case of this example, the ABI has already been imported through the live coder.

In order to make it work on your developer environment, head to the [CFAv1Forwarder technical reference](/docs/technical-reference/CFAv1Forwarder) and copy the ABI.
Then, replace the `forwarderABI` variable in the example with the ABI you copied.
:::

---

<a id="doc_52"></a>

## 📁 sdk/money-streaming / Subgraph

*파일 경로: sdk/money-streaming/subgraph.mdx*

---
sidebar_position: 3
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';


The Graph is the indexing layer of the blockchain industry, providing a queryable platform for the vast data produced by blockchain networks.
The Graph can be used for querying data in the Superfluid ecosystem and other on-chain data. Experiment with queries using the [GraphQL Playground](https://thegraph.com/hosted-service/).

<Admonition type="tip" title="New to GraphQL?">

Before diving into subgraph queries, familiarize yourself with GraphQL basics:
[Learn GraphQL](https://graphql.org/learn/)

</Admonition>

### Querying Different Networks

#### Superfluid Explorer

The Superfluid Explorer is an interactive interface for exploring the Superfluid Protocol and interacting with its Subgraph. It provides an intuitive way to query on-chain data, get contract addresses, and manage your Superfluid finances. The console supports various blockchain networks, allowing you to seamlessly switch between them and access specific data sets. Whether you're analyzing streams, checking balances, or staying up to date with the new deployments. The Superfluid Explorer makes these tasks accessible and straightforward.

Explore Superfluid data across various networks using the Superfluid Explorer. Select a network to start querying:

<Tabs
  defaultValue="popular"
  values={[
    {label: 'Popular', value: 'popular'},
    {label: 'Other', value: 'other'},
  ]}>
  
  <TabItem value="popular">
    <div style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap' }}>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=ethereum"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Ethereum
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=matic"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Polygon
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=avalanche"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Avalanche
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=optimism"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Optimism
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=arbitrum"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Arbitrum
      </a>
      <a 
        href="https://console.superfluid.finance/subgraph?_network=binance-smart-chain"
        className="button-link"
        style={{
          backgroundColor: 'green',
          color: 'white',
          padding: '10px 20px',
          textDecoration: 'none',
          borderRadius: '4px',
          display: 'inline-block',
          margin: '5px'
        }}
      >
        Binance Smart Chain
      </a>
    </div>
  </TabItem>
  <TabItem value="other">
    <p>For other networks, use the Superfluid Explorer:</p>
    <a 
      href="https://console.superfluid.finance/"
      className="button-link"
      style={{
        backgroundColor: 'green',
        color: 'white',
        padding: '10px 20px',
        textDecoration: 'none',
        borderRadius: '4px',
        display: 'inline-block'
      }}
    >
      Superfluid Explorer
    </a>
  </TabItem>
</Tabs>

#### Subgraph Networks

You can have the full list of available subgraph endpoints in the [Subgraph Endpoints](/docs/technical-reference/subgraph) page.

### Resources

- **Subgraph Queries**: [Guide on Querying the Graph](https://thegraph.com/docs/en/developer/query-the-graph/)
- **Deploy a Subgraph**: [Creating a Subgraph](https://thegraph.com/docs/en/developer/create-subgraph-hosted/)
- **GraphQL Schema**: [Superfluid Schema](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/subgraph/schema.graphql)
- **Our Subgraph Endpoints**: [Subgraph Endpoints](/docs/technical-reference/subgraph)

### Helpful Tips

- All addresses in the subgraph (`id`, `underlyingAddress`, etc.) are lowercase.
- Convert addresses to lowercase before querying.

#### Notable Breaking Changes

<Admonition type="caution" title="Migrating From Legacy Subgraph to V1">

Significant changes were made in October 2021:

- `totalSubscriptions` is now `totalSubscriptionsWithUnits`.
- `Subscriber` entity changed to `Subscription`.
- `createdAt` and `updatedAt` fields are now `createdAtTimestamp` and `updatedAtTimestamp`.

</Admonition>

### Schema Overview

The Superfluid Subgraph includes various entities for querying. Think of entities as analogous to database tables. Here's a brief overview:

#### Event Entities

Event entities correspond to contract events, often with added data. Each event entity is immutable and created once.

- **Event ID Format**: `eventName-transactionHash-logIndex`.
- **Naming Convention**: For V1, event names end with 'Event'.

#### Higher Order Level Entities (HOL)

HOL entities represent entities over their lifetime and may be updated.

- **`Account`**: Represents any address interacting with Superfluid.
- **`Token`**: Represents valid SuperTokens.
- **`Pool`**, **`PoolMember`**, **`Stream`**, **`StreamPeriod`**: Related to Superfluid streams and [pools](/docs/protocol/distributions/guides/pools).

#### Aggregate Entities

Aggregate entities store cumulative data at both account-token and global token levels:

- **`TokenStatistic`**: Aggregates data for a single Token type.
- **`AccountTokenSnapshot`**: Aggregates data on an account's interaction with a token.

### Query Examples

Here are examples to help you get started with Superfluid subgraphs:

#### Super Token Data Query

```javascript
{
  tokens(first: 100) {
    id
    symbol
    name
    underlyingAddress
  }
}
```

#### Get All Streams for a Given Account

To list all streams that an account is currently receiving (swap 'receiver' for 'sender' to see streams being sent):

```javascript
query MyQuery {
  streams(where: {receiver: "YOUR_ADDRESS_HERE"}) {
    currentFlowRate
    token {
      symbol
    }
    sender {
      id
    }
    receiver {
      id
    }
  }
}
```

#### Getting Stream Data Between 2 Parties

Query active streams between two parties, such as Alice ("0x658...") and Bob ("0xd66..."):

```javascript
{
  streams(where:{
    sender: "0x658e1b019f2f30c8089a9ae3ae5820f335bd9ce4"
    receiver: "0xd66e40b0c30595bec72153b502ac1e0c4785991b"
  }) {
    token {
      id
      symbol
    }
    createdAtTimestamp
    updatedAtTimestamp
    currentFlowRate
    streamedUntilUpdatedAt
  }
}
```

<Admonition type="note">

To calculate the current total amount streamed, use: _**streamedUntilUpdatedAt + ((current time in seconds) - updatedAtTimestamp) * currentFlowRate**_.

</Admonition>

#### Get The Most Recently Updated Flows

Query the 10 most recently updated flows using the `FlowUpdatedEvent` type:

```javascript
{
  flowUpdatedEvents(first: 10, orderBy: timestamp, orderDirection: desc) {
    oldFlowRate
    flowRate
    userData
    stream {
      token {
        symbol
      }
      sender {
        id
      }
      receiver {
        id
      }
    }
  }
}
```

<Admonition type="info">

Understand the difference between a Flow and a Stream. A new stream is created each time a stream is terminated and restarted.

</Admonition>

#### Get Aggregate Flow Data For a Given Token

Query aggregate data for a specific token, such as Super DAI on Polygon:

```javascript
{
  tokenStatistics(where: {
    id: "0x1305f6b6df9dc47159d12eb7ac2804d4a33173c2" // DAIx address on Matic
  }) {
    totalNumberOfActiveStreams
    totalNumberOfActiveIndexes
    totalAmountStreamedUntilUpdatedAt
    totalOutflowRate
    totalAmountDistributedUntilUpdatedAt
  }
}
```

#### Get Data On a Specific Account

Query data on a specific account using both the `Account` and `AccountTokenSnapshot` entities:

```javascript
{
  accounts(where: {
    id: "0x..." // Enter an address below
  }) {
    isSuperApp
    inflows {
      currentFlowRate
      token {
        symbol
      }
      sender {
        id
      }
    }
    outflows {
      currentFlowRate
      token {
        symbol
      }
      receiver {
        id
      }
    }
    accountTokenSnapshots {
      token {
        id
      }
      totalNumberOfActiveStreams
      totalNetFlowRate
    }
  }
}
```

<Admonition type="tip">

Use `AccountTokenSnapshot` to get activity data for a specific token associated with an account.

</Admonition> 

### Explore more queries

Explore more queries using the [Superfluid Subgraph Playground](https://console.superfluid.finance/subgraph).

---

<a id="doc_53"></a>

## 📁 sdk/super-tokens / How to make your balance dance?

*파일 경로: sdk/super-tokens/balance-dance.mdx*

---
sidebar_position: 3
---

import FlowingBalance from "@site/src/components/FlowingBalance";


Have you ever been to the [Superfluid Dashboard](https://app.superfluid.finance/) and seen the balance of a user dancing like in the GIF below?
This is because the balance of Super Tokens is constantly being updated, with each block.

<div style={{ display: "flex", justifyContent: "center" }}>
![Dancing Balance](/assets/flowing-balance.gif)
</div>
<div style={{ display: "flex", justifyContent: "center" }}>
*GIF of a "Flowing Balance" from the [Superfluid Dashboard](https://app.superfluid.finance/)*
</div>
We call this the `FlowingBalance` component and it's a great way to show the balance of a user in a dynamic and visually appealing way.
In this guide, we will show you how to make your balance dance. Let's get started!
### Overview

The `FlowingBalance` component is designed to dynamically display a Super Token's balance that updates over time based on a specified flow rate, a starting balance and a starting date.
This guide breaks down the component into its core functionalities, including utility functions, custom hooks, and the component itself.

`FlowingBalance` leverages React's hooks to animate balance changes over time, simulating a continuous flow of currency.
It's particularly useful in applications that need to show real-time updates to a user's balance of Super Tokens, providing a visually appealing and responsive user interface.

<div>
<details>
<summary>Click here to show `FlowingBalance` Component code</summary>
<p>
```jsx
import React, { useEffect, useState, useMemo, memo } from 'react';
import { formatEther } from 'viem';

// Constants
export const ANIMATION_MINIMUM_STEP_TIME = 40;

// Utility functions
export const absoluteValue = (n: bigint) => {
  return n >= BigInt(0) ? n : -n;
};

export function toFixedUsingString(numStr: string, decimalPlaces: number): string {
  const [wholePart, decimalPart] = numStr.split('.');

  if (!decimalPart || decimalPart.length <= decimalPlaces) {
    return numStr.padEnd(wholePart.length + 1 + decimalPlaces, '0');
  }

  const decimalPartBigInt = BigInt(`${decimalPart.slice(0, decimalPlaces)}${decimalPart[decimalPlaces] >= '5' ? '1' : '0'}`);

  return `${wholePart}.${decimalPartBigInt.toString().padStart(decimalPlaces, '0')}`;
}

// Hooks
export const useSignificantFlowingDecimal = (
  flowRate: bigint,
  animationStepTimeInMs: number,
): number | undefined => useMemo(() => {
  if (flowRate === BigInt(0)) {
    return undefined;
  }

  const ticksPerSecond = 1000 / animationStepTimeInMs;
  const flowRatePerTick = flowRate / BigInt(ticksPerSecond);

  const [beforeEtherDecimal, afterEtherDecimal] = formatEther(flowRatePerTick).split('.');

  const isFlowingInWholeNumbers = absoluteValue(BigInt(beforeEtherDecimal)) > BigInt(0);

  if (isFlowingInWholeNumbers) {
    return 0; // Flowing in whole numbers per tick.
  }
  const numberAfterDecimalWithoutLeadingZeroes = BigInt(afterEtherDecimal);

  const lengthToFirstSignificantDecimal = afterEtherDecimal
    .toString()
    .replace(numberAfterDecimalWithoutLeadingZeroes.toString(), '').length; // We're basically counting the zeroes.

  return Math.min(lengthToFirstSignificantDecimal + 2, 18); // Don't go over 18.
}, [flowRate, animationStepTimeInMs]);

const useFlowingBalance = (
  startingBalance: bigint,
  startingBalanceDate: Date,
  flowRate: bigint
) => {
  const [flowingBalance, setFlowingBalance] = useState(startingBalance);

  const startingBalanceTime = startingBalanceDate.getTime();
  useEffect(() => {
    if (flowRate === BigInt(0)) return;

    let lastAnimationTimestamp = 0;

    const animationStep = (currentAnimationTimestamp: number) => {
      const animationFrameId = window.requestAnimationFrame(animationStep);
      if (
        currentAnimationTimestamp - lastAnimationTimestamp >
        ANIMATION_MINIMUM_STEP_TIME
      ) {
        const elapsedTimeInMilliseconds = BigInt(
          Date.now() - startingBalanceTime
        );
        const flowingBalance_ =
          startingBalance + (flowRate * elapsedTimeInMilliseconds) / BigInt(1000);

        setFlowingBalance(flowingBalance_);

        lastAnimationTimestamp = currentAnimationTimestamp;
      }

      return () => window.cancelAnimationFrame(animationFrameId);
    };

    let animationFrameId = window.requestAnimationFrame(animationStep);

    return () => window.cancelAnimationFrame(animationFrameId);
  }, [startingBalance, startingBalanceTime, flowRate]);

  return flowingBalance;
};

// FlowingBalance Component
const FlowingBalance: React.FC<{
  startingBalance: bigint;
  startingBalanceDate: Date;
  flowRate: bigint;
}> = memo(({ startingBalance, startingBalanceDate, flowRate }) => {
  const flowingBalance = useFlowingBalance(
    startingBalance,
    startingBalanceDate,
    flowRate
  );

  const decimalPlaces = useSignificantFlowingDecimal(
    flowRate,
    ANIMATION_MINIMUM_STEP_TIME
  );

  return (
    <div className="flowing-balance">
    {decimalPlaces !== undefined
      ? toFixedUsingString(formatEther(flowingBalance), decimalPlaces)
      : formatEther(flowingBalance)}
  </div>
  );
});

export default FlowingBalance;

```
</p>
</details>
</div>

The component explicited in the code above is composed of the following parts:
- **Constants**: This section defines the minimum time interval between animation updates.
- **Utility Functions**: These functions are used to calculate the absolute value of a number and format a number to a specified number of decimal places.
- **Hooks**: These custom hooks are used to calculate the number of significant decimal places to display and update the flowing balance over time.
- **FlowingBalance Component**: This functional component uses the hooks and utility functions to render the flowing balance, taking `startingBalance`, `startingBalanceDate`, and `flowRate` as props.

### Constants

```jsx
export const ANIMATION_MINIMUM_STEP_TIME = 40;
```

This constant defines the minimum time interval (in milliseconds) between animation updates. It's used to throttle the animation and ensure that updates occur no more frequently than every 40 milliseconds.

### Utility Functions

#### `absoluteValue`

```jsx
export const absoluteValue = (n: bigint) => {
  return n >= BigInt(0) ? n : -n;
};
```

Converts a `bigint` to its absolute value. This function is crucial for calculations that require the non-negative form of a number.

#### `toFixedUsingString`

```jsx
export function toFixedUsingString(numStr: string, decimalPlaces: number): string {
  // Implementation details
}
```

Formats a number (expressed as a string) to a specified number of decimal places. This function is essential for displaying the balance in a user-friendly format, ensuring that the balance is rounded and displayed with a consistent number of decimal places.

### Hooks

#### `useSignificantFlowingDecimal`

```jsx
export const useSignificantFlowingDecimal = (flowRate: bigint, animationStepTimeInMs: number): number | undefined => {
  // Hook logic
};
```

Determines the number of significant decimal places to display based on the flow rate and animation step time. This custom hook helps adjust the precision of the balance display dynamically, based on how quickly the balance is changing.

#### `useFlowingBalance`

```jsx
const useFlowingBalance = (startingBalance: bigint, startingBalanceDate: Date, flowRate: bigint) => {
  // Hook logic
};
```

Calculates and updates the flowing balance over time. This hook is the core of the component, using the `requestAnimationFrame` API to smoothly update the balance display at a rate that's throttled by `ANIMATION_MINIMUM_STEP_TIME`.

### FlowingBalance Component

```jsx
const FlowingBalance: React.FC<{startingBalance: bigint; startingBalanceDate: Date; flowRate: bigint;}> = memo(({ startingBalance, startingBalanceDate, flowRate }) => {
  // Component logic
});
```

This functional component uses the above hooks and utility functions to render the flowing balance. It takes `startingBalance`, `startingBalanceDate`, and `flowRate` as props, calculating the current balance based on these inputs and displaying it in a formatted manner.

#### Usage Example

Below is an example of how to use the `FlowingBalance` component within your application.

```jsx
<FlowingBalance startingBalance={BigInt("1000000000000000000")} startingBalanceDate={new Date('2024-01-01T00:00:00.000Z')} flowRate={BigInt("1000000000000000")} />
```

This component exemplifies how to combine React's capabilities with the performance of the Web APIs to create dynamic and responsive UIs. By breaking down the component into its constituent parts, developers can gain insights into its functionality and customize it according to their needs.

:::tip My component is being jumpy, what can I do?
Sometimes, especially if you center your component using `justifyContent: "center"`, the component may have a jumpy behaviour like below:
<div style={{ display: "flex", fontSize: "1.2rem", fontWeight: "bold", justifyContent: "center" }}>
    ❌ <FlowingBalance startingBalance={BigInt("1000000000000000000")} startingBalanceDate={new Date('2024-01-01T00:00:00.000Z')} flowRate={BigInt("1000000000000000")} />
</div>
If you run into this issue, you can try to set a fixed width to the component like such:
```jsx
<div style={{ display: "flex", fontSize: "1.2rem", fontWeight: "bold", justifyContent: "center" }}>
  <div style={{ width: "135px", margin: "auto" }}>
    <FlowingBalance startingBalance={BigInt("1000000000000000000")} startingBalanceDate={new Date('2024-01-01T00:00:00.000Z')} flowRate={BigInt("1000000000000000")} />
  </div>
</div>
```
This should fix the jumpy behaviour and make the component flow smoothly like the example below:
<div style={{ display: "flex", fontSize: "1.2rem", fontWeight: "bold", justifyContent: "center" }}>
  <div style={{ width: "160px", margin: "auto" }}>
   ✅ <FlowingBalance startingBalance={BigInt("1000000000000000000")} startingBalanceDate={new Date('2024-01-01T00:00:00.000Z')} flowRate={BigInt("1000000000000000")} />
  </div>
</div>
:::

### Best practices

- **Throttle the animation**: Ensure that the animation updates occur at a reasonable interval, such as every 40 milliseconds. This helps prevent excessive CPU usage and ensures a smooth user experience.
- **Use fixed width**: If the component is jumpy, consider setting a fixed width to the component to ensure a smooth flow of the balance.
- **Time conversion**: When showing the flow rate and converting the blockchain value to a human-readable value (eg. wei/s to ETH/month),
    ensure that the time conversion is accurate and consistent with the rest of Superfluid's time-based calculations:
    - 1 year = 365 days
    - 1 month = 1 year/12
    - 1 day = 24 hours
    - 1 hour = 60 minutes
    - 1 minute = 60 seconds
    - 1 second = 1000 milliseconds
- **Current timestamp**: Following Superfluid's implementation, it is recommended to use `Date.now()` to get the current timestamp in milliseconds instead of using `(await ethers.provider.getBlock('latest')).timestamp` for example.

---

<a id="doc_54"></a>

## 📁 sdk/super-tokens / Tracking Super Token Balances

*파일 경로: sdk/super-tokens/super-token-balances.mdx*

---
sidebar_position: 2
---
import Admonition from '@theme/Admonition';
import Link from '@docusaurus/Link';


Super Token balances can dynamically change every second, presenting unique challenges and considerations for tracking them within the Ethereum ecosystem.

### Compatibility with ERC20

Super Tokens, while being ERC20 compatible, have some nuances in terms of forward compatibility with Ethereum infrastructure and tools.

#### Key Points

- **Backward Compatibility**: Super Tokens work with existing Ethereum tools like Metamask and Gnosis Safe. You can view balances in Metamask, transfer funds using Gnosis Safe, and even swap Super Tokens on platforms like Uniswap.
- **Forward Compatibility**: While tools like Metamask and Gnosis Safe can display balances accurately, they do not support all functionalities of Super Tokens. For example, you cannot swap your streamed money on Automated Market Makers (eg. Uniswap).

### Balance Tracking Considerations

Tracking the balance of Super Tokens requires a more nuanced approach than traditional ERC20 tokens.

#### Challenges

- **Event-Based Tracking Limitation**: Some applications, like Etherscan, use `transfer` events to track user balances. However, due to scalability concerns, Super Tokens don't emit `transfer` events with every balance change, leading to potential discrepancies in displayed balances.
- **Multi-source updates**: Super Tokens can be updated from multiple sources, from [Money Streaming](/docs/protocol/money-streaming/overview.mdx), but also [Distributions](/docs/protocol/distributions/overview.mdx).

#### Solution 1 (recommended): Using `balanceOf`

As we mentioned earlier, Super Tokens are ERC20 compatible, so you can use the `balanceOf` function from the token smart contract to get the real time aggregated balance of a user.
The Superfluid Protocol modifies the `balanceOf` function to account for the various fund movement methods unique to Super Tokens including Money Streaming and Distributions.
You can simply call this function to get the real time aggregated balance of a user like so:

```jsx
const fetchBlockchainBalance = async () => {
    setLoading(true);
    setError("");
    try {
      const provider = new ethers.providers.JsonRpcProvider(
        "YOUR PROVIDER URL"
      );
      const contractAddress = "0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f"; //fake DAIx contract address on Mumbai
      const contractABI = [
        "function transferFrom(address from, address to, uint value)",
        "function balanceOf(address owner) view returns (uint balance)",
      ];
      const contract = new ethers.Contract(
        contractAddress,
        contractABI,
        provider
      );
      const userAddress = liveAddress;
      const balance = await contract.balanceOf(userAddress);
      return(ethers.utils.formatEther(balance.toString()));
    } catch (error) {
      console.error("Error fetching blockchain balance:", error);
    }
  };
```

:::tip About Accuracy
We recommend this solution because it guarantees the most accurate result. However, it is important to note that this method is not always possible depending on your application architecture design.
:::

#### Solution 2: Using queries from the Subgraph

To accurately track Super Token balances, you can use the queries below to get inflows and outflow object from Superfluid's [Subgraph](https://explorer.superfluid.finance/subgraph).

##### Getting all the inflows for user
```graphql
query allReceivedStreams($receiver: String) {
  cfaStreams: streams(where: {receiver: $receiver}) {
    currentFlowRate
    streamedUntilUpdatedAt
    updatedAtTimestamp
  }
  gdaStreams: poolMembers(where: {account: $receiver}) {
    pool {
      totalUnits
      flowRate
      totalAmountDistributedUntilUpdatedAt
      updatedAtTimestamp
    }
    units
    totalAmountReceivedUntilUpdatedAt
    poolTotalAmountDistributedUntilUpdatedAt
    updatedAtTimestamp
  }
}
```
##### Getting all the outflows for user
```graphql
query allSentStreams($sender: String) {
  cfaStreams: streams(where: {sender: $sender}) {
    currentFlowRate
    streamedUntilUpdatedAt
    updatedAtTimestamp
  }
  gdaStreams: poolDistributors(where: {account: $sender}) {
    flowRate
    updatedAtTimestamp
    totalAmountDistributedUntilUpdatedAt
  }
}
```
Doing this allows you to do the following:
- Get **the data related to each stream a user is receiving** : This allows us to calculate the positive balance associated with each stream they receive.
- Get **the data related to each pool where the user is connected** : This allows us to calculate the positive balance associated with each membership in a pool.
- Get **the data related to each stream a user is sending** : This allows us to calculate the negative balance associated with each stream they send.
- Get **the data related to each pool where the user is distributing** : This allows us to calculate the negative balance associated with each distribution they make.

:::tip How to calculate each balance?
The rule of thumb for calculating each one of these balances is the following:

<div style={{ display: 'flex', justifyContent: 'center' }}>
    **The Balance = FlowRate * (CurrentTime - LastUpdatedAtTime) + StreamedUntilUpdatedAt**.
</div>
:::


Once we have the balance from each stream and each pool/distribution, we can sum them up to get the net aggregated balance of a user.
An implementation of this can be seen in the `NetBalance` component below.

<div>
<details>
<summary>Click here to show `NetBalance` component</summary>
<p>
```jsx
const NetBalance = ({ liveAddress }) => {
  const [realTimeBalance, setRealTimeBalance] = useState(null);
  const [blockchainBalance, setBlockchainBalance] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function fetchSubgraphBalance() {
    setLoading(true); // Assuming setLoading is a function that updates loading state
    setError(""); // Assuming setError is a function that clears any previous errors
    const endpoint = "https://polygon-mumbai.subgraph.x.superfluid.dev";
    const provider = new ethers.providers.JsonRpcProvider(
      "https://polygon-testnet.public.blastapi.io"
    );
    const currentTimestamp = (await provider.getBlock("latest")).timestamp;

    const inflowQuery = {
      query: `query allReceivedStreams($receiver: String) {
        cfaStreams: streams(where: {receiver: $receiver}) {
          currentFlowRate
          streamedUntilUpdatedAt
          updatedAtTimestamp
        }
        gdaStreams: poolMembers(where: {account: $receiver}) {
          pool {
            totalUnits
            flowRate
            totalAmountDistributedUntilUpdatedAt
            updatedAtTimestamp
          }
          units
          totalAmountReceivedUntilUpdatedAt
          poolTotalAmountDistributedUntilUpdatedAt
          updatedAtTimestamp
        }
      }`,
      variables: { receiver: liveAddress },
    };

    const outflowQuery = {
      query: `query allSentStreams($sender: String) {
        cfaStreams: streams(where: {sender: $sender}) {
          currentFlowRate
          streamedUntilUpdatedAt
          updatedAtTimestamp
        }
        gdaStreams: poolDistributors(where: {account: $sender}) {
          flowRate
          updatedAtTimestamp
          totalAmountDistributedUntilUpdatedAt
        }
      }`,
      variables: { sender: liveAddress },
    };

    try {
      const inflowResponse = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(inflowQuery),
      });

      const outflowResponse = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(outflowQuery),
      });

      const inflowData = await inflowResponse.json();
      const outflowData = await outflowResponse.json();

      let netBalance = 0;

      // Calculate inflow balance
      inflowData.data.cfaStreams.forEach((stream) => {
        netBalance +=
          parseInt(stream.currentFlowRate) *
            (currentTimestamp - parseInt(stream.updatedAtTimestamp)) +
          parseInt(stream.streamedUntilUpdatedAt);
      });

      inflowData.data.gdaStreams.forEach((pool) => {
        const balance =
          (parseInt(pool.units) / parseInt(pool.pool.totalUnits)) *
            parseInt(pool.pool.flowRate) *
            (currentTimestamp - parseInt(pool.updatedAtTimestamp)) +
          parseInt(pool.totalAmountReceivedUntilUpdatedAt);
        netBalance += balance;
      });

      // Calculate outflow balance (as negative)
      outflowData.data.cfaStreams.forEach((stream) => {
        netBalance -=
          parseInt(stream.currentFlowRate) *
            (currentTimestamp - parseInt(stream.updatedAtTimestamp)) +
          parseInt(stream.streamedUntilUpdatedAt);
      });

      outflowData.data.gdaStreams.forEach((pool) => {
        const balance =
          parseInt(pool.flowRate) *
            (currentTimestamp - parseInt(pool.updatedAtTimestamp)) -
          parseInt(pool.totalAmountDistributedUntilUpdatedAt);
        netBalance -= balance;
      });

      setRealTimeBalance(ethers.utils.formatEther(netBalance.toString())); // Assuming setRealTimeBalance is a function that updates the balance state
    } catch (error) {
      console.error("Error calculating net balance:", error);
      setError("Failed to calculate net balance."); // Assuming setError is a function that sets error state
    } finally {
      setLoading(false); // Assuming setLoading is a function that updates loading state
    }
  }

  const fetchBlockchainBalance = async () => {
    setLoading(true);
    setError("");
    try {
      const provider = new ethers.providers.JsonRpcProvider(
        "https://polygon-testnet.public.blastapi.io"
      );
      const contractAddress = "0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f"; //fake DAIx contract address on Mumbai
      const contractABI = [
        "function transferFrom(address from, address to, uint value)",
        "function balanceOf(address owner) view returns (uint balance)",
      ];
      const contract = new ethers.Contract(
        contractAddress,
        contractABI,
        provider
      );

      const userAddress = liveAddress;
      const balance = await contract.balanceOf(userAddress);
      setBlockchainBalance(ethers.utils.formatEther(balance.toString()));
    } catch (error) {
      console.error("Error fetching blockchain balance:", error);
      setError("Failed to fetch blockchain balance.");
    } finally {
      setLoading(false);
    }
  };

  const handleFetch = async () => {
    await fetchSubgraphBalance();
    await fetchBlockchainBalance();
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: "Arial",
      }}
    >
      <h1>Real-Time Balance</h1>
      <div
        style={{
          border: "1px solid #ccc",
          padding: "20px",
          borderRadius: "5px",
          marginBottom: "20px",
        }}
      >
        <p>
          Enter your <strong>liveAddress</strong> in the code editor, then click
          "Fetch Balance" to compare your real-time balance from the subgraph
          with the blockchain balance.
        </p>
      </div>
      <button
        onClick={handleFetch}
        disabled={loading}
        style={{
          padding: "10px",
          fontSize: "16px",
          margin: "10px 0",
          cursor: loading ? "not-allowed" : "pointer",
          backgroundColor: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "5px",
          outline: "none",
        }}
      >
        {loading ? "Loading..." : "Fetch Balance"}
      </button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {realTimeBalance !== null && (
        <p>Real-Time Balance from Subgraph: {realTimeBalance} fake DAIx</p>
      )}
      {blockchainBalance !== null && (
        <p>Balance from Blockchain: {blockchainBalance} fake DAIx</p>
      )}
    </div>
  );
};
```
</p>
</details>
</div>

Furthermore, you can use the live code block below to see the `NetBalance` component in action:
- Enter your `liveAddress` in the code editor.
- Click "Fetch Balance" to compare your real-time balance from the subgraph with the blockchain balance.

```jsx live
function UserBalance() {
const yourAddress="0x5e48a37d34d93778807ef19d74e06128252bab45";

return (
    <div>
      <RealTimeBalance liveAddress={yourAddress} />
    </div>
  );
}
```

:::tip About this example
Please keep in mind that in the example above we make the assumption that the user is only using Money Streaming and Distributions in the form of the GDA,
but not Distributions in the form of the IDA. If you are using IDA, you will need to add a new query to get the data related to each transfer a user is distributing.
:::

---

<a id="doc_55"></a>

## 📁 sdk/super-tokens / Wrap and Unwrap Super Tokens

*파일 경로: sdk/super-tokens/wrap-unwrap.mdx*

---
sidebar_position: 1
---


This guide explains how to wrap and unwrap [Wrapped Super Tokens](/docs/protocol/super-tokens/overview#types-of-super-tokens) from your client application.

For all Wrapped Super Tokens, this is an important step in the user journey. It allows users to convert their ERC20 tokens to Super Tokens and vice versa.

:::tip how to deploy a wrapped super token?
If you need to deploy a Wrapped Super Token, you can follow our guide on [Deploying a Wrapped Super Token](/docs/protocol/super-tokens/guides/deploy-super-token/deploy-wrapped-super-token).
:::


### Why do we need to wrap and unwrap Super Tokens?

Super Tokens are an enhanced version of ERC20 tokens, typically built on top of existing ERC20 tokens. This means that to use a Super Token, you often need to "wrap" an ERC20 token into its Super Token equivalent, and vice versa when you want to convert back to the original ERC20.

To find out the address of the underlying ERC20 token for a Super Token, you can use the `getUnderlyingToken` view function provided by the [Super Token interface contract](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/interfaces/superfluid/ISuperToken.sol).

:::tip Super Token Interface
You can find the complete Super Token interface in our [ISuperToken Technical Reference](/docs/technical-reference/ISuperToken).
:::

:::warning Not all Wrapped Super Tokens have an underlying ERC20 token
In the case of [Native Super Tokens](/docs/protocol/super-tokens/overview#3-native-super-tokens) (like the ETHx), they do not have a underlying ERC20 token, but rather the native coin of the chain.
Native Super Tokens inherit the ISETH interface, which you can also find in the [Technical Reference Section](/docs/technical-reference/ISETH).
:::

### Super Token ABI

You can find the ABI for the Super Token Interface at the [ISuperToken Technical Reference](/docs/technical-reference/ISuperToken). This ABI includes all the functions available for interacting with Super Tokens.

You can find the ABI for the Native Super Token Interface at the [ISETH Technical Reference](/docs/technical-reference/ISETH). This ABI includes all the functions available for interacting with Native Super Tokens.

### Wrapping and Unwrapping Functions

Super Tokens provide several functions for wrapping (upgrading) and unwrapping (downgrading) tokens:

#### Wrapping (Upgrading) Functions

For wrapping ERC20 tokens into Super Tokens, you can use the following functions from the [Super Token interface](/docs/technical-reference/ISuperToken):
1. `upgrade(uint256 amount)`: Upgrades ERC20 tokens to Super Tokens.
2. `upgradeTo(address to, uint256 amount, bytes userData)`: Upgrades ERC20 tokens to Super Tokens and transfers them to a specified address.

For wrapping Native Super Tokens (like ETHx), you can use the following function from the [ISETH interface](/docs/technical-reference/ISETH):
1. `upgradeByETH() payable`: Upgrades native tokens to Super Tokens.
2. `upgradeByETHTo(address to) payable`: Upgrades native tokens to Super Tokens and transfers them to a specified address.

#### Unwrapping (Downgrading) Functions

For unwrapping Super Tokens back to ERC20 tokens, you can use the following functions from the [Super Token interface](/docs/technical-reference/ISuperToken):
1. `downgrade(uint256 amount)`: Downgrades Super Tokens back to ERC20 tokens.
2. `downgradeTo(address to, uint256 amount)`: Downgrades Super Tokens to ERC20 tokens and transfers them to a specified address.

For unwrapping Native Super Tokens (like ETHx), you can use the following function from the [ISETH interface](/docs/technical-reference/ISETH):
1. `downgradeToETH(uint256 amount)`: Downgrades Super Tokens back to native tokens.

:::warning Approval for Wrapping
Before wrapping ERC20 tokens into Super Tokens, you need to approve the Super Token contract to spend your ERC20 tokens. This is not needed for unwrapping.
:::

### Live Code Example: Wrapping ERC20 to Super Token

Here's a simple example of how to wrap an ERC20 token into a Super Token using ethers.js:

```jsx live
function WrapERC20ToSuperToken() {
  const [amount, setAmount] = useState('');
  const [status, setStatus] = useState('');

  const wrapTokens = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // ERC20 token contract - you need to replace this with the actual token address
        const erc20Address = '0x123...'; // Replace with actual ERC20 token address
        const erc20Abi = ['function approve(address spender, uint256 amount) public returns (bool)'];
        const erc20Contract = new ethers.Contract(erc20Address, erc20Abi, signer);

        // Super Token contract - you need to replace this with the actual Super Token address
        const superTokenAddress = '0x456...'; // Replace with actual Super Token address
        const superTokenAbi = ['function upgrade(uint256 amount) external'];
        const superTokenContract = new ethers.Contract(superTokenAddress, superTokenAbi, signer);

        // Approve the Super Token contract to spend ERC20 tokens
        const approveTx = await erc20Contract.approve(superTokenAddress, amount);
        await approveTx.wait();
        setStatus('Approval successful. Wrapping tokens...');

        // Upgrade (wrap) ERC20 to Super Token
        const upgradeTx = await superTokenContract.upgrade(amount);
        await upgradeTx.wait();
        setStatus('Tokens successfully wrapped!');
      } catch (error) {
        console.error('Error:', error);
        setStatus('Error: ' + error.message);
      }
    } else {
      setStatus('Please install MetaMask!');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Amount to wrap"
      />
      <button onClick={wrapTokens}>Wrap Tokens</button>
      <p>{status}</p>
    </div>
  );
}
```

:::warning Replace Placeholder Addresses
Replace the placeholder addresses in the code above with actual contract addresses of your ERC20 token and Super Token.
:::

This example demonstrates how to:
1. Connect to the user's wallet
2. Approve the Super Token contract to spend ERC20 tokens
3. Upgrade (wrap) ERC20 tokens to Super Tokens

For more detailed information about the ISuperToken interface and its functions, please refer to our [ISuperToken Technical Reference](/docs/technical-reference/ISuperToken).

---

<a id="doc_56"></a>

## 📁 technical-reference / CFAv1Forwarder

*파일 경로: technical-reference/CFAv1Forwarder.mdx*

---
sidebar_position: 3
---

import BonadocsWidget from "@bonadocs/widget"


The **CFAv1Forwarder** contract is a Superfluid forwarder that implements the Constant Flow Agreement (CFA) related functions.
It is a contract specifically made immutable in order to facilitate the interaction with [Money Streaming](/docs/protocol/money-streaming/overview.mdx) through the Constant Flow Agreement (CFA).

This contract is optimized for interaction that would happen from your client application.
For more information on the best practices regarding this interaction, please refer to the [Create, Update and Delete Flows](/docs/sdk/money-streaming/create-update-delete-flow) or [Manage Access Control and User Data](/docs/sdk/money-streaming/acl-user-data).

### Contract Address

The `CFAv1Forwarder` contract address is the same on all networks:

```
0xcfA132E353cB4E398080B9700609bb008eceB125
```

### ABI

In order to interact with the `CFAv1Forwarder` contract, you can use the following ABI:

<div>
<details>
<summary>Click here to show `CFAv1Forwarder` ABI</summary>
<p>
```json
[
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluid",
        "name": "host",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  { "inputs": [], "name": "CFA_FWD_INVALID_FLOW_RATE", "type": "error" },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "createFlow",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "deleteFlow",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "getAccountFlowInfo",
    "outputs": [
      { "internalType": "uint256", "name": "lastUpdated", "type": "uint256" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "getAccountFlowrate",
    "outputs": [
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "name": "getBufferAmountByFlowrate",
    "outputs": [
      { "internalType": "uint256", "name": "bufferAmount", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" }
    ],
    "name": "getFlowInfo",
    "outputs": [
      { "internalType": "uint256", "name": "lastUpdated", "type": "uint256" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "getFlowOperatorPermissions",
    "outputs": [
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowrateAllowance", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" }
    ],
    "name": "getFlowrate",
    "outputs": [
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "grantPermissions",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "revokePermissions",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "name": "setFlowrate",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "name": "setFlowrateFrom",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "updateFlow",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowrateAllowance", "type": "int96" }
    ],
    "name": "updateFlowOperatorPermissions",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

```
</p>
</details>
</div>

### CFA_FWD_INVALID_FLOW_RATE

```solidity
error CFA_FWD_INVALID_FLOW_RATE()
````

### \_cfa

```solidity
contract IConstantFlowAgreementV1 _cfa
```

### Fn constructor

```solidity
function constructor(
    contract ISuperfluid host
)
    public
```

##### Parameters

| Name   | Type                 | Description |
| :----- | :------------------- | :---------- |
| `host` | contract ISuperfluid |             |

### Fn setFlowrate

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x57e6aa36" />

##### Parameters

| Name       | Type                 | Description                                                             |
| :--------- | :------------------- | :---------------------------------------------------------------------- |
| `token`    | contract ISuperToken | Super token address                                                     |
| `receiver` | address              | The receiver of the flow                                                |
| `flowrate` | int96                | The wanted flowrate in wad/second. Only positive values are valid here. |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Sets the given flowrate between msg.sender and a given receiver.
If there's no pre-existing flow and `flowrate` non-zero, a new flow is created.
If there's an existing flow and `flowrate` non-zero, the flowrate of that flow is updated.
If there's an existing flow and `flowrate` zero, the flow is deleted.
If the existing and given flowrate are equal, no action is taken.
On creation of a flow, a "buffer" amount is automatically detracted from the sender account's available balance.
If the sender account is solvent when the flow is deleted, this buffer is redeemed to it.

### Fn setFlowrateFrom

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0xc5ad5c1a" />

##### Parameters

| Name       | Type                 | Description                                                             |
| :--------- | :------------------- | :---------------------------------------------------------------------- |
| `token`    | contract ISuperToken | Super token address                                                     |
| `sender`   | address              | The sender of the flow                                                  |
| `receiver` | address              | The receiver of the flow                                                |
| `flowrate` | int96                | The wanted flowrate in wad/second. Only positive values are valid here. |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Like `setFlowrate`, but can be invoked by an account with flowOperator permissions
on behalf of the sender account.

### Fn getFlowrate

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x1d8b6526" />

_Currently, only 0 or 1 flows can exist between 2 accounts. This may change in the future._

##### Parameters

| Name       | Type                 | Description              |
| :--------- | :------------------- | :----------------------- |
| `token`    | contract ISuperToken | Super token address      |
| `sender`   | address              | The sender of the flow   |
| `receiver` | address              | The receiver of the flow |

##### Return Values

| Name       | Type  | Description                                                                        |
| :--------- | :---- | :--------------------------------------------------------------------------------- |
| `flowrate` | int96 | The flowrate from the sender to the receiver account. Returns 0 if no flow exists. |

Get the flowrate of the flow between 2 accounts if exists.

### Fn getFlowInfo

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x2860fd93" />

##### Parameters

| Name       | Type                 | Description              |
| :--------- | :------------------- | :----------------------- |
| `token`    | contract ISuperToken | Super token address      |
| `sender`   | address              | The sender of the flow   |
| `receiver` | address              | The receiver of the flow |

##### Return Values

| Name          | Type    | Description                                                              |
| :------------ | :------ | :----------------------------------------------------------------------- |
| `lastUpdated` | uint256 | Timestamp of last update (flowrate change) or zero if no flow exists     |
| `flowrate`    | int96   | Current flowrate of the flow or zero if no flow exists                   |
| `deposit`     | uint256 | Deposit amount locked as security buffer during the lifetime of the flow |
| `owedDeposit` | uint256 | Extra deposit amount borrowed to a SuperApp receiver by the flow sender  |

Get all available information about a flow (if exists).
If only the flowrate is needed, consider using `getFlowrate` instead.

### Fn getBufferAmountByFlowrate

```solidity
function getBufferAmountByFlowrate(
    contract ISuperToken token,
    int96 flowrate
)
    external
    returns (uint256 bufferAmount)
```
<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x09f0b495" />

##### Parameters

| Name       | Type                 | Description                                            |
| :--------- | :------------------- | :----------------------------------------------------- |
| `token`    | contract ISuperToken | Super token address                                    |
| `flowrate` | int96                | The flowrate for which the buffer amount is calculated |

##### Return Values

| Name           | Type    | Description                                             |
| :------------- | :------ | :------------------------------------------------------ |
| `bufferAmount` | uint256 | The buffer amount required for the given configuration. |

Get the buffer amount required for the given token and flowrate.
This amount can vary based on the combination of token, flowrate and chain being queried.
The result for a given set of parameters can change over time,
because it depends on governance configurable protocol parameters.
Changes of the required buffer amount affect only flows created or updated after the change.

### Fn getAccountFlowrate

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x22c904d9" />

##### Parameters

| Name      | Type                 | Description         |
| :-------- | :------------------- | :------------------ |
| `token`   | contract ISuperToken | Super token address |
| `account` | address              | Account to query    |

##### Return Values

| Name       | Type  | Description                                                                               |
| :--------- | :---- | :---------------------------------------------------------------------------------------- |
| `flowrate` | int96 | The net flowrate (aggregate incoming minus aggregate outgoing flowrate), can be negative. |

Get the net flowrate of an account.

### Fn getAccountFlowInfo

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x0f1ac495" />

##### Parameters

| Name      | Type                 | Description         |
| :-------- | :------------------- | :------------------ |
| `token`   | contract ISuperToken | Super token address |
| `account` | address              | Account to query    |

##### Return Values

| Name          | Type    | Description                                                                                |
| :------------ | :------ | :----------------------------------------------------------------------------------------- |
| `lastUpdated` | uint256 | Timestamp of last update of a flow to or from the account (flowrate change)                |
| `flowrate`    | int96   | Current net aggregate flowrate                                                             |
| `deposit`     | uint256 | Aggregate deposit amount currently locked as security buffer for outgoing flows            |
| `owedDeposit` | uint256 | Aggregate extra deposit amount currently borrowed to SuperApps receiving from this account |

Get aggregated flow information (if any exist) of an account.
If only the net flowrate is needed, consider using `getAccountFlowrate` instead.

### Fn createFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0xe15536b6" />

##### Parameters

| Name       | Type                 | Description                                                          |
| :--------- | :------------------- | :------------------------------------------------------------------- |
| `token`    | contract ISuperToken | Super token address                                                  |
| `sender`   | address              | Sender address of the flow                                           |
| `receiver` | address              | Receiver address of the flow                                         |
| `flowrate` | int96                | The flowrate in wad/second to be set initially                       |
| `userData` | bytes                | (optional) User data to be set. Should be set to zero if not needed. |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Low-level wrapper of createFlow/createFlowByOperator.
If the address of msg.sender is not the same as the address of the `sender` argument,
createFlowByOperator is used internally. In this case msg.sender needs to have permission to create flows
on behalf of the given sender account with sufficient flowRateAllowance.
Currently, only 1 flow can exist between 2 accounts, thus `createFlow` will fail if one already exists.

### Fn updateFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x0c033991" />

##### Parameters

| Name       | Type                 | Description                                                          |
| :--------- | :------------------- | :------------------------------------------------------------------- |
| `token`    | contract ISuperToken | Super token address                                                  |
| `sender`   | address              | Sender address of the flow                                           |
| `receiver` | address              | Receiver address of the flow                                         |
| `flowrate` | int96                | The flowrate in wad/second the flow should be updated to             |
| `userData` | bytes                | (optional) User data to be set. Should be set to zero if not needed. |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Low-level wrapper if updateFlow/updateFlowByOperator.
If the address of msg.sender doesn't match the address of the `sender` argument,
updateFlowByOperator is invoked. In this case msg.sender needs to have permission to update flows
on behalf of the given sender account with sufficient flowRateAllowance.

### Fn deleteFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0xb4b333c6" />

##### Parameters

| Name       | Type                 | Description                                                          |
| :--------- | :------------------- | :------------------------------------------------------------------- |
| `token`    | contract ISuperToken | Super token address                                                  |
| `sender`   | address              | Sender address of the flow                                           |
| `receiver` | address              | Receiver address of the flow                                         |
| `userData` | bytes                | (optional) User data to be set. Should be set to zero if not needed. |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Low-level wrapper of deleteFlow/deleteFlowByOperator.
If msg.sender isn't the same as sender address, msg.sender needs to have permission
to delete flows on behalf of the given sender account.

### Fn grantPermissions

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x7243fb93" />

##### Parameters

| Name           | Type                 | Description                              |
| :------------- | :------------------- | :--------------------------------------- |
| `token`        | contract ISuperToken | Super token address                      |
| `flowOperator` | address              | Account to which permissions are granted |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Grants a flowOperator permission to create/update/delete flows on behalf of msg.sender.
In order to restrict what a flowOperator can or can't do, the flowOperator account
should be a contract implementing the desired restrictions.

### Fn revokePermissions

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x0bd0728d" />

##### Parameters

| Name           | Type                 | Description                                |
| :------------- | :------------------- | :----------------------------------------- |
| `token`        | contract ISuperToken | Super token address                        |
| `flowOperator` | address              | Account from which permissions are revoked |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Revokes all permissions previously granted to a flowOperator by msg.sender.
Revocation doesn't undo or reset flows previously created/updated by the flowOperator.
In order to be sure about the state of flows at the time of revocation, you need to check that state
either in the same transaction or after this transaction.

### Fn updateFlowOperatorPermissions

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x30885591" />

##### Parameters

| Name                | Type                 | Description                                                                              |
| :------------------ | :------------------- | :--------------------------------------------------------------------------------------- |
| `token`             | contract ISuperToken | Super token address                                                                      |
| `flowOperator`      | address              | Account for which permissions are set on behalf of msg.sender                            |
| `permissions`       | uint8                | Bitmask for create/update/delete permission flags. See library `FlowOperatorDefinitions` |
| `flowrateAllowance` | int96                | Max. flowrate in wad/second the operator can set for individual flows.                   |

##### Return Values

| Name  | Type | Description |
| :---- | :--- | :---------- |
| `[0]` | bool | bool        |

Low-level wrapper of `IConstantFlowAgreementV1.updateFlowOperatorPermissions`
flowrateAllowance does NOT restrict the net flowrate a flowOperator is able to set.
In order to restrict that, flowOperator needs to be a contract implementing the wanted limitations.

### Fn getFlowOperatorPermissions

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x4d3f60f9" />

##### Parameters

| Name           | Type                 | Description                                          |
| :------------- | :------------------- | :--------------------------------------------------- |
| `token`        | contract ISuperToken | Super token address                                  |
| `sender`       | address              | The account which (possibly) granted permissions      |
| `flowOperator` | address              | Account to which (possibly) permissions were granted |

##### Return Values

| Name                | Type  | Description                                                                           |
| :------------------ | :---- | :------------------------------------------------------------------------------------ |
| `permissions`       | uint8 | A bitmask of the permissions currently granted (or not) by `sender` to `flowOperator` |
| `flowrateAllowance` | int96 | Max. flowrate in wad/second the flowOperator can set for individual flows.            |

Get the currently set permissions granted to the given flowOperator by the given sender account.

### Fn \_setFlowrateFrom

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0xc5ad5c1a" />

##### Parameters

| Name       | Type                 | Description |
| :--------- | :------------------- | :---------- |
| `token`    | contract ISuperToken |             |
| `sender`   | address              |             |
| `receiver` | address              |             |
| `flowrate` | int96                |             |

### Fn \_createFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0xe15536b6" />

##### Parameters

| Name       | Type                 | Description |
| :--------- | :------------------- | :---------- |
| `token`    | contract ISuperToken |             |
| `sender`   | address              |             |
| `receiver` | address              |             |
| `flowrate` | int96                |             |
| `userData` | bytes                |             |

### Fn \_updateFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x0c033991" />

##### Parameters

| Name       | Type                 | Description |
| :--------- | :------------------- | :---------- |
| `token`    | contract ISuperToken |             |
| `sender`   | address              |             |
| `receiver` | address              |             |
| `flowrate` | int96                |             |
| `userData` | bytes                |             |

### Fn \_deleteFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0xb4b333c6" />

##### Parameters

| Name       | Type                 | Description |
| :--------- | :------------------- | :---------- |
| `token`    | contract ISuperToken |             |
| `sender`   | address              |             |
| `receiver` | address              |             |
| `userData` | bytes                |             |

### Fn \_updateFlowOperatorPermissions

<BonadocsWidget widgetConfigUri="ipfs://bafkreie4jxs6zvo6xwdjdkfhxuks6efmpag2ywyz5kr24ztqyqvd2duqjy" contract="CFAv1Forwarder" functionKey="0x30885591" />

##### Parameters

| Name                | Type                 | Description |
| :------------------ | :------------------- | :---------- |
| `token`             | contract ISuperToken |             |
| `flowOperator`      | address              |             |
| `permissions`       | uint8                |             |
| `flowrateAllowance` | int96                |             |

---

<a id="doc_57"></a>

## 📁 technical-reference / GDAv1Forwarder

*파일 경로: technical-reference/GDAv1Forwarder.mdx*

---
sidebar_position: 4
---

import CodeBlock from "@theme/CodeBlock";
import gdaForwarder from "!!raw-loader!@site/src/abis/gdaForwarder.json";
import BonadocsWidget from "@bonadocs/widget";


The **GDAv1Forwarder** contract is a Superfluid forwarder that implements the General Distribution Agreement (GDA) related functions.
It is a contract specifically made immutable in order to facilitate the interaction with [Distributions](/docs/protocol/distributions/overview.mdx) through the General Distribution Agreement (GDA).

This contract is optimized for interaction that would happen from outside the blockchain (off-chain).
For more information on the best practices regarding this interaction, please refer to the [SDK Section](/docs/sdk/quickstart) section of this documentation.

### Contract Address

The `GDAv1Forwarder` contract address is the same on all Superfluid chains:

```
0x6DA13Bde224A05a288748d857b9e7DDEffd1dE08
```


### ABI

In order to interact with the `GDAv1Forwarder` contract, you can use the following ABI:

<div>
<details>
<summary>Click here to show `GDAv1Forwarder` ABI</summary>
<p>

<CodeBlock language="json">{gdaForwarder}</CodeBlock>

</p>
</details>
</div>

### \_gda

```solidity
contract IGeneralDistributionAgreementV1 _gda
```

### Fn constructor

```solidity
function constructor(
    contract ISuperfluid host
)
    public
```

##### Parameters

| Name   | Type                 | Description |
| :----- | :------------------- | :---------- |
| `host` | contract ISuperfluid |             |

### Fn createPool

<BonadocsWidget widgetConfigUri="ipfs://bafkreihna7h5d6tweo36atgsqbhvqdjdwq2374i3bdel7ko4cyurfe3zx4" contract="GDAv1Forwarder" functionKey="0x0779d365" />

_Creates a new Superfluid Pool._

##### Parameters

| Name     | Type                      | Description                                                                    |
| :------- | :------------------------ | :----------------------------------------------------------------------------- |
| `token`  | contract ISuperfluidToken | The Super Token address.                                                       |
| `admin`  | address                   | The pool admin address.                                                        |
| `config` | struct PoolConfig         | The pool configuration (see PoolConfig in IGeneralDistributionAgreementV1.sol) |

##### Return Values

| Name      | Type                     | Description                                                           |
| :-------- | :----------------------- | :-------------------------------------------------------------------- |
| `success` | bool                     | A boolean value indicating whether the pool was created successfully. |
| `pool`    | contract ISuperfluidPool | The address of the deployed Superfluid Pool                           |

### Fn updateMemberUnits

<BonadocsWidget widgetConfigUri="ipfs://bafkreihna7h5d6tweo36atgsqbhvqdjdwq2374i3bdel7ko4cyurfe3zx4" contract="GDAv1Forwarder" functionKey="0x398c74e1" />

_Updates the units of a pool member._

##### Parameters

| Name            | Type                     | Description                          |
| :-------------- | :----------------------- | :----------------------------------- |
| `pool`          | contract ISuperfluidPool | The Superfluid Pool to update.       |
| `memberAddress` | address                  | The address of the member to update. |
| `newUnits`      | uint128                  | The new units of the member.         |
| `userData`      | bytes                    | User-specific data.                  |

### Fn claimAll

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0xd2c0d542" />

_Claims all tokens from the pool._

##### Parameters

| Name            | Type                     | Description                             |
| :-------------- | :----------------------- | :-------------------------------------- |
| `pool`          | contract ISuperfluidPool | The Superfluid Pool to claim from.      |
| `memberAddress` | address                  | The address of the member to claim for. |
| `userData`      | bytes                    | User-specific data.                     |

### Fn connectPool

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0xf0b7b915" />

_Connects a pool member to `pool`._

##### Parameters

| Name       | Type                     | Description                     |
| :--------- | :----------------------- | :------------------------------ |
| `pool`     | contract ISuperfluidPool | The Superfluid Pool to connect. |
| `userData` | bytes                    | User-specific data.             |

##### Return Values

| Name  | Type | Description                                                       |
| :---- | :--- | :---------------------------------------------------------------- |
| `[0]` | bool | A boolean value indicating whether the connection was successful. |

### Fn disconnectPool

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x30925b79" />

_Disconnects a pool member from `pool`._

##### Parameters

| Name       | Type                     | Description                        |
| :--------- | :----------------------- | :--------------------------------- |
| `pool`     | contract ISuperfluidPool | The Superfluid Pool to disconnect. |
| `userData` | bytes                    | User-specific data.                |

##### Return Values

| Name  | Type | Description                                                          |
| :---- | :--- | :------------------------------------------------------------------- |
| `[0]` | bool | A boolean value indicating whether the disconnection was successful. |

### Fn distribute

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x6d1007a6" />

_Tries to distribute `requestedAmount` amount of `token` from `from` to `pool`._

##### Parameters

| Name              | Type                      | Description                                  |
| :---------------- | :------------------------ | :------------------------------------------- |
| `token`           | contract ISuperfluidToken | The Super Token address.                     |
| `from`            | address                   | The address from which to distribute tokens. |
| `pool`            | contract ISuperfluidPool  | The Superfluid Pool address.                 |
| `requestedAmount` | uint256                   | The amount of tokens to distribute.          |
| `userData`        | bytes                     | User-specific data.                          |

##### Return Values

| Name  | Type | Description                                                         |
| :---- | :--- | :------------------------------------------------------------------ |
| `[0]` | bool | A boolean value indicating whether the distribution was successful. |

### Fn distributeFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x5a6c6dbc" />

_Tries to distribute flow at `requestedFlowRate` of `token` from `from` to `pool`._

##### Parameters

| Name                | Type                      | Description                                  |
| :------------------ | :------------------------ | :------------------------------------------- |
| `token`             | contract ISuperfluidToken | The Super Token address.                     |
| `from`              | address                   | The address from which to distribute tokens. |
| `pool`              | contract ISuperfluidPool  | The Superfluid Pool address.                 |
| `requestedFlowRate` | int96                     | The flow rate of tokens to distribute.       |
| `userData`          | bytes                     | User-specific data.                          |

##### Return Values

| Name  | Type | Description                                                         |
| :---- | :--- | :------------------------------------------------------------------ |
| `[0]` | bool | A boolean value indicating whether the distribution was successful. |

### Fn isPool

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x7b2cc0da" />

_Checks if the specified account is a pool._

##### Parameters

| Name      | Type                      | Description                   |
| :-------- | :------------------------ | :---------------------------- |
| `token`   | contract ISuperfluidToken | The Super Token address.      |
| `account` | address                   | The account address to check. |

##### Return Values

| Name  | Type | Description                                               |
| :---- | :--- | :-------------------------------------------------------- |
| `[0]` | bool | A boolean value indicating whether the account is a pool. |

### Fn getNetFlow

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0xe8e7e2d1" />

_Gets the GDA net flow rate for the specified account._

##### Parameters

| Name      | Type                      | Description              |
| :-------- | :------------------------ | :----------------------- |
| `token`   | contract ISuperfluidToken | The Super Token address. |
| `account` | address                   | The account address.     |

##### Return Values

| Name  | Type  | Description                            |
| :---- | :---- | :------------------------------------- |
| `[0]` | int96 | The gda net flow rate for the account. |

### Fn getFlowDistributionFlowRate

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x44999ff7" />

_Gets the flow rate of tokens between the specified accounts._

##### Parameters

| Name    | Type                      | Description                              |
| :------ | :------------------------ | :--------------------------------------- |
| `token` | contract ISuperfluidToken | The Super Token address.                 |
| `from`  | address                   | The sender address.                      |
| `to`    | contract ISuperfluidPool  | The receiver address (the pool address). |

##### Return Values

| Name  | Type  | Description                     |
| :---- | :---- | :------------------------------ |
| `[0]` | int96 | The flow distribution flow rate |

### Fn getPoolAdjustmentFlowRate

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x4e9ced57" />

_Gets the pool adjustment flow rate for the specified pool._

##### Parameters

| Name   | Type    | Description       |
| :----- | :------ | :---------------- |
| `pool` | address | The pool address. |

##### Return Values

| Name  | Type  | Description                    |
| :---- | :---- | :----------------------------- |
| `[0]` | int96 | The pool adjustment flow rate. |

### Fn estimateFlowDistributionActualFlowRate

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0x4d5c91ec" />

_Estimates the actual flow rate for flow distribution to the specified pool._

##### Parameters

| Name                | Type                      | Description              |
| :------------------ | :------------------------ | :----------------------- |
| `token`             | contract ISuperfluidToken | The Super Token address. |
| `from`              | address                   | The sender address.      |
| `to`                | contract ISuperfluidPool  | The pool address.        |
| `requestedFlowRate` | int96                     | The requested flow rate. |

##### Return Values

| Name                        | Type  | Description |
| :-------------------------- | :---- | :---------- |
| `actualFlowRate`            | int96 |             |
| `totalDistributionFlowRate` | int96 |             |

### Fn estimateDistributionActualAmount

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0xeccfc6a5" />

_Estimates the actual amount for distribution to the specified pool._

##### Parameters

| Name              | Type                      | Description              |
| :---------------- | :------------------------ | :----------------------- |
| `token`           | contract ISuperfluidToken | The Super Token address. |
| `from`            | address                   | The sender address.      |
| `to`              | contract ISuperfluidPool  | The pool address.        |
| `requestedAmount` | uint256                   | The requested amount.    |

##### Return Values

| Name           | Type    | Description                         |
| :------------- | :------ | :---------------------------------- |
| `actualAmount` | uint256 | The actual amount for distribution. |

### Fn isMemberConnected

<BonadocsWidget widgetConfigUri="ipfs://bafkreibd2smont3drvknabftn52vk3qdyxyosvnjmytb4giopyv3wha5x4" contract="GDAv1Forwarder" functionKey="0xc782eb9c" />

_Checks if the specified member is connected to the pool._

##### Parameters

| Name     | Type                     | Description                  |
| :------- | :----------------------- | :--------------------------- |
| `pool`   | contract ISuperfluidPool | The Superfluid Pool address. |
| `member` | address                  | The member address.          |

##### Return Values

| Name  | Type | Description                                                             |
| :---- | :--- | :---------------------------------------------------------------------- |
| `[0]` | bool | A boolean value indicating whether the member is connected to the pool. |

### Fn getPoolAdjustmentFlowInfo

<BonadocsWidget widgetConfigUri="ipfs://bafkreihna7h5d6tweo36atgsqbhvqdjdwq2374i3bdel7ko4cyurfe3zx4" contract="GDAv1Forwarder" functionKey="0x37bd42e0" />

_Gets the pool adjustment flow information for the specified pool._

##### Parameters

| Name   | Type                     | Description       |
| :----- | :----------------------- | :---------------- |
| `pool` | contract ISuperfluidPool | The pool address. |

##### Return Values

| Name  | Type    | Description                                             |
| :---- | :------ | :------------------------------------------------------ |
| `[0]` | address | The pool admin, pool ID, and pool adjustment flow rate. |
| `[1]` | bytes32 |                                                         |
| `[2]` | int96   |                                                         |

---

<a id="doc_58"></a>

## 📁 technical-reference / ISETH

*파일 경로: technical-reference/ISETH.mdx*

---
sidebar_position: 6
---
import CodeBlock from "@theme/CodeBlock";
import ISETH from "!!raw-loader!@site/src/abis/ISETH.json";


ISETH is the interface for native Super Tokens.

### ABI

In order to interact with any contract satistying the `ISETH` interface, you can use the following ABI:

<div>
<details>
<summary>Click here to show `ISETH` ABI</summary>
<p>

<CodeBlock language="json">{ISETH}</CodeBlock>

</p>
</details>
</div>

### Fn upgradeByETH

```solidity
function upgradeByETH(
) 
    external
```

### Fn upgradeByETHTo

```solidity
function upgradeByETHTo(
    address to
) 
    external
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `to` | address |  |

### Fn downgradeToETH

```solidity
function downgradeToETH(
    uint256 wad
) 
    external
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `wad` | uint256 |  |

## ISETH

**Super ETH (SETH) full interface**

---

<a id="doc_59"></a>

## 📁 technical-reference / ISuperToken

*파일 경로: technical-reference/ISuperToken.mdx*

---
sidebar_position: 5
---


import CodeBlock from "@theme/CodeBlock";
import ISuperToken from "!!raw-loader!@site/src/abis/ISuperToken.json";


This is the technical reference related to the interface for Super Tokens.

### Implementation addresses
Super Token deployments work in a proxy pattern with the original implementation being comon between all super tokens for each chain.
The implementation address for the SuperToken is different for each network and can be found in the SuperTokenFactory at the method `getSuperTokenLogic`.

To get the addresses of all the SuperTokenFactory contracts, you can use the [Superfluid Explorer](https://explorer.superfluid.finance/), section Protocol.

### ABI

In order to interact with any contract satistying the `ISuperToken` interface, you can use the following ABI:

<div>
<details>
<summary>Click here to show `ISuperToken` ABI</summary>
<p>

<CodeBlock language="json">{ISuperToken}</CodeBlock>

</p>
</details>
</div>

### Functions

#### Fn initialize

```solidity
function initialize(
    contract IERC20 underlyingToken,
    uint8 underlyingDecimals,
    string n,
    string s
) 
    external
```
_Initialize the contract_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `underlyingToken` | contract IERC20 |  |
| `underlyingDecimals` | uint8 |  |
| `n` | string |  |
| `s` | string |  |

#### Fn initializeWithAdmin

```solidity
function initializeWithAdmin(
    contract IERC20 underlyingToken,
    uint8 underlyingDecimals,
    string n,
    string s,
    address admin
) 
    external
```
_Initialize the contract with an admin_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `underlyingToken` | contract IERC20 |  |
| `underlyingDecimals` | uint8 |  |
| `n` | string |  |
| `s` | string |  |
| `admin` | address |  |

#### Fn changeAdmin

```solidity
function changeAdmin(
    address newAdmin
) 
    external
```
_Only the current admin can call this function
if admin is address(0), it is implicitly the host address_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newAdmin` | address | New admin address |

Changes the admin for the SuperToken

#### Fn getAdmin

```solidity
function getAdmin(
) 
    external 
    returns (address admin)
```
_Returns the admin address for the SuperToken_

#### Fn CONSTANT_OUTFLOW_NFT

```solidity
function CONSTANT_OUTFLOW_NFT(
) 
    external 
    returns (contract IConstantOutflowNFT)
```

#### Fn CONSTANT_INFLOW_NFT

```solidity
function CONSTANT_INFLOW_NFT(
) 
    external 
    returns (contract IConstantInflowNFT)
```

#### Fn POOL_ADMIN_NFT

```solidity
function POOL_ADMIN_NFT(
) 
    external 
    returns (contract IPoolAdminNFT)
```

#### Fn POOL_MEMBER_NFT

```solidity
function POOL_MEMBER_NFT(
) 
    external 
    returns (contract IPoolMemberNFT)
```

#### Fn name

```solidity
function name(
) 
    external 
    returns (string)
```
_Returns the name of the token._

#### Fn symbol

```solidity
function symbol(
) 
    external 
    returns (string)
```
_Returns the symbol of the token, usually a shorter version of the
name._

#### Fn decimals

```solidity
function decimals(
) 
    external 
    returns (uint8)
```
_Returns the number of decimals used to get its user representation.
For example, if `decimals` equals `2`, a balance of `505` tokens should
be displayed to a user as `5,05` (`505 / 10 ** 2`).

Tokens usually opt for a value of 18, imitating the relationship between
Ether and Wei. This is the value ERC20 uses, unless _setupDecimals is
called._

##### Note 

SuperToken always uses 18 decimals.

This information is only used for _display_ purposes: it in
no way affects any of the arithmetic of the contract, including
[IERC20-balanceOf](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) and [IERC20-transfer](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20).

#### Fn totalSupply

```solidity
function totalSupply(
) 
    external 
    returns (uint256)
```
_See [IERC20-totalSupply](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

#### Fn balanceOf

```solidity
function balanceOf(
    address account
) 
    external 
    returns (uint256 balance)
```
_Returns the amount of tokens owned by an account (`owner`)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |

#### Fn transfer

```solidity
function transfer(
    address recipient,
    uint256 amount
) 
    external 
    returns (bool)
```
_Moves `amount` tokens from the caller's account to `recipient`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `recipient` | address |  |
| `amount` | uint256 |  |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | Returns Success a boolean value indicating whether the operation succeeded. |

##### Emits 

a ERC20 Transfer event.

#### Fn allowance

```solidity
function allowance(
    address owner,
    address spender
) 
    external 
    returns (uint256)
```
_Returns the remaining number of tokens that `spender` will be
        allowed to spend on behalf of `owner` through [transferFrom](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20). This is
        zero by default._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `owner` | address |  |
| `spender` | address |  |

This value changes when [approve](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) or [transferFrom](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) are called.

#### Fn approve

```solidity
function approve(
    address spender,
    uint256 amount
) 
    external 
    returns (bool)
```
_Sets `amount` as the allowance of `spender` over the caller's tokens._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `spender` | address |  |
| `amount` | uint256 |  |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | Returns Success a boolean value indicating whether the operation succeeded. |

##### Note 

Beware that changing an allowance with this method brings the risk
that someone may use both the old and the new allowance by unfortunate
transaction ordering. One possible solution to mitigate this race
condition is to first reduce the spender&#x27;s allowance to 0 and set the
desired value afterwards:
https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729

##### Emits 

an [Approval](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

#### Fn transferFrom

```solidity
function transferFrom(
    address sender,
    address recipient,
    uint256 amount
) 
    external 
    returns (bool)
```
_Moves `amount` tokens from `sender` to `recipient` using the
        allowance mechanism. `amount` is then deducted from the caller's
        allowance._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `sender` | address |  |
| `recipient` | address |  |
| `amount` | uint256 |  |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | Returns Success a boolean value indicating whether the operation succeeded. |

##### Emits 

a [Transfer](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

#### Fn increaseAllowance

```solidity
function increaseAllowance(
    address spender,
    uint256 addedValue
) 
    external 
    returns (bool)
```
_Atomically increases the allowance granted to `spender` by the caller.

This is an alternative to `approve` that can be used as a mitigation for
problems described in [IERC20-approve](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `spender` | address |  |
| `addedValue` | uint256 |  |

##### Emits 

an [Approval](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event indicating the updated allowance.

@custom:requirements
- &#x60;spender&#x60; cannot be the zero address.

#### Fn decreaseAllowance

```solidity
function decreaseAllowance(
    address spender,
    uint256 subtractedValue
) 
    external 
    returns (bool)
```
_Atomically decreases the allowance granted to `spender` by the caller.

This is an alternative to approve that can be used as a mitigation for
problems described in [IERC20-approve](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `spender` | address |  |
| `subtractedValue` | uint256 |  |

##### Emits 

an [Approval](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event indicating the updated allowance.

@custom:requirements
- &#x60;spender&#x60; cannot be the zero address.
- &#x60;spender&#x60; must have allowance for the caller of at least
&#x60;subtractedValue&#x60;.

#### Fn granularity

```solidity
function granularity(
) 
    external 
    returns (uint256)
```
_Returns the smallest part of the token that is not divisible. This
        means all token operations (creation, movement and destruction) must have
        amounts that are a multiple of this number._

##### Note 

For super token contracts, this value is always 1

#### Fn send

```solidity
function send(
    address recipient,
    uint256 amount,
    bytes userData
) 
    external
```
_Moves `amount` tokens from the caller's account to `recipient`.

If send or receive hooks are registered for the caller and `recipient`,
     the corresponding functions will be called with `userData` and empty
     `operatorData`. See [IERC777Sender](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) and [IERC777Recipient](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `recipient` | address |  |
| `amount` | uint256 |  |
| `userData` | bytes |  |

##### Emits 

a [Sent](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

@custom:requirements
- the caller must have at least &#x60;amount&#x60; tokens.
- &#x60;recipient&#x60; cannot be the zero address.
- if &#x60;recipient&#x60; is a contract, it must implement the [IERC777Recipient](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)
interface.

#### Fn burn

```solidity
function burn(
    uint256 amount,
    bytes userData
) 
    external
```
_Destroys `amount` tokens from the caller's account, reducing the
total supply and transfers the underlying token to the caller's account.

If a send hook is registered for the caller, the corresponding function
will be called with `userData` and empty `operatorData`. See [IERC777Sender](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `amount` | uint256 |  |
| `userData` | bytes |  |

##### Emits 

a [Burned](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

@custom:requirements
- the caller must have at least &#x60;amount&#x60; tokens.

#### Fn isOperatorFor

```solidity
function isOperatorFor(
    address operator,
    address tokenHolder
) 
    external 
    returns (bool)
```
_Returns true if an account is an operator of `tokenHolder`.
Operators can send and burn tokens on behalf of their owners. All
accounts are their own operator.

See [operatorSend](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) and [operatorBurn](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `operator` | address |  |
| `tokenHolder` | address |  |

#### Fn authorizeOperator

```solidity
function authorizeOperator(
    address operator
) 
    external
```
_Make an account an operator of the caller.

See [isOperatorFor](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `operator` | address |  |

##### Emits 

an [AuthorizedOperator](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

@custom:requirements
- &#x60;operator&#x60; cannot be calling address.

#### Fn revokeOperator

```solidity
function revokeOperator(
    address operator
) 
    external
```
_Revoke an account's operator status for the caller.

See [isOperatorFor](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) and [defaultOperators](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `operator` | address |  |

##### Emits 

a [RevokedOperator](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

@custom:requirements
- &#x60;operator&#x60; cannot be calling address.

#### Fn defaultOperators

```solidity
function defaultOperators(
) 
    external 
    returns (address[])
```
_Returns the list of default operators. These accounts are operators
for all token holders, even if [authorizeOperator](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) was never called on
them.

This list is immutable, but individual holders may revoke these via
[revokeOperator](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20), in which case [isOperatorFor](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) will return false._

#### Fn operatorSend

```solidity
function operatorSend(
    address sender,
    address recipient,
    uint256 amount,
    bytes userData,
    bytes operatorData
) 
    external
```
_Moves `amount` tokens from `sender` to `recipient`. The caller must
be an operator of `sender`.

If send or receive hooks are registered for `sender` and `recipient`,
the corresponding functions will be called with `userData` and
`operatorData`. See [IERC777Sender](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) and [IERC777Recipient](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `sender` | address |  |
| `recipient` | address |  |
| `amount` | uint256 |  |
| `userData` | bytes |  |
| `operatorData` | bytes |  |

##### Emits 

a [Sent](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

@custom:requirements
- &#x60;sender&#x60; cannot be the zero address.
- &#x60;sender&#x60; must have at least &#x60;amount&#x60; tokens.
- the caller must be an operator for &#x60;sender&#x60;.
- &#x60;recipient&#x60; cannot be the zero address.
- if &#x60;recipient&#x60; is a contract, it must implement the [IERC777Recipient](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)
interface.

#### Fn operatorBurn

```solidity
function operatorBurn(
    address account,
    uint256 amount,
    bytes userData,
    bytes operatorData
) 
    external
```
_Destroys `amount` tokens from `account`, reducing the total supply.
The caller must be an operator of `account`.

If a send hook is registered for `account`, the corresponding function
will be called with `userData` and `operatorData`. See [IERC777Sender](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20)._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |
| `amount` | uint256 |  |
| `userData` | bytes |  |
| `operatorData` | bytes |  |

##### Emits 

a [Burned](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#IERC20) event.

@custom:requirements
- &#x60;account&#x60; cannot be the zero address.
- &#x60;account&#x60; must have at least &#x60;amount&#x60; tokens.
- the caller must be an operator for &#x60;account&#x60;.

#### Fn selfMint

```solidity
function selfMint(
    address account,
    uint256 amount,
    bytes userData
) 
    external
```
_Mint new tokens for the account
If `userData` is not empty, the `tokensReceived` hook is invoked according to ERC777 semantics.

@custom:modifiers
 - onlySelf_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |
| `amount` | uint256 |  |
| `userData` | bytes |  |

#### Fn selfBurn

```solidity
function selfBurn(
    address account,
    uint256 amount,
    bytes userData
) 
    external
```
_Burn existing tokens for the account
If `userData` is not empty, the `tokensToSend` hook is invoked according to ERC777 semantics.

@custom:modifiers
 - onlySelf_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |
| `amount` | uint256 |  |
| `userData` | bytes |  |

#### Fn selfTransferFrom

```solidity
function selfTransferFrom(
    address sender,
    address spender,
    address recipient,
    uint256 amount
) 
    external
```
_Transfer `amount` tokens from the `sender` to `recipient`.
If `spender` isn't the same as `sender`, checks if `spender` has allowance to
spend tokens of `sender`.

@custom:modifiers
 - onlySelf_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `sender` | address |  |
| `spender` | address |  |
| `recipient` | address |  |
| `amount` | uint256 |  |

#### Fn selfApproveFor

```solidity
function selfApproveFor(
    address account,
    address spender,
    uint256 amount
) 
    external
```
_Give `spender`, `amount` allowance to spend the tokens of
`account`.

@custom:modifiers
 - onlySelf_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |
| `spender` | address |  |
| `amount` | uint256 |  |

#### Fn transferAll

```solidity
function transferAll(
    address recipient
) 
    external
```
_Transfer all available balance from `msg.sender` to `recipient`_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `recipient` | address |  |

#### Fn getUnderlyingToken

```solidity
function getUnderlyingToken(
) 
    external 
    returns (address tokenAddr)
```
_Return the underlying token contract_

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `tokenAddr` | address | Underlying token address |

#### Fn getUnderlyingDecimals

```solidity
function getUnderlyingDecimals(
) 
    external 
    returns (uint8 underlyingDecimals)
```
_Return the underlying token decimals_

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `underlyingDecimals` | uint8 | Underlying token decimals |

#### Fn toUnderlyingAmount

```solidity
function toUnderlyingAmount(
    uint256 amount
) 
    external 
    returns (uint256 underlyingAmount, uint256 adjustedAmount)
```
_Return the underlying token conversion rate_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `amount` | uint256 | Number of tokens to be upgraded (in 18 decimals) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `underlyingAmount` | uint256 | The underlying token amount after scaling |
| `adjustedAmount` | uint256 | The super token amount after scaling |

#### Fn upgrade

```solidity
function upgrade(
    uint256 amount
) 
    external
```
_Upgrade ERC20 to SuperToken._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `amount` | uint256 | Number of tokens to be upgraded (in 18 decimals) |

##### Note 

It will use &#x60;transferFrom&#x60; to get tokens. Before calling this
function you should &#x60;approve&#x60; this contract

#### Fn upgradeTo

```solidity
function upgradeTo(
    address to,
    uint256 amount,
    bytes userData
) 
    external
```
_Upgrade ERC20 to SuperToken and transfer immediately_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `to` | address | The account to receive upgraded tokens |
| `amount` | uint256 | Number of tokens to be upgraded (in 18 decimals) |
| `userData` | bytes | User data for the TokensRecipient callback |

##### Note 

It will use &#x60;transferFrom&#x60; to get tokens. Before calling this
function you should &#x60;approve&#x60; this contract

@custom:warning
- there is potential of reentrancy IF the &quot;to&quot; account is a registered ERC777 recipient.
@custom:requirements
- if &#x60;userData&#x60; is NOT empty AND &#x60;to&#x60; is a contract, it MUST be a registered ERC777 recipient
  otherwise it reverts.


#### Fn downgrade

```solidity
function downgrade(
    uint256 amount
) 
    external
```
_Downgrade SuperToken to ERC20.
It will call transfer to send tokens_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `amount` | uint256 | Number of tokens to be downgraded |

#### Fn downgradeTo

```solidity
function downgradeTo(
    address to,
    uint256 amount
) 
    external
```
_Downgrade SuperToken to ERC20 and transfer immediately_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `to` | address | The account to receive downgraded tokens |
| `amount` | uint256 | Number of tokens to be downgraded (in 18 decimals) |


#### Fn operationApprove

```solidity
function operationApprove(
    address account,
    address spender,
    uint256 amount
) 
    external
```
_Perform ERC20 approve by host contract._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address | The account owner to be approved. |
| `spender` | address | The spender of account owner's funds. |
| `amount` | uint256 | Number of tokens to be approved.

@custom:modifiers
 - onlyHost |

#### Fn operationIncreaseAllowance

```solidity
function operationIncreaseAllowance(
    address account,
    address spender,
    uint256 addedValue
) 
    external
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |
| `spender` | address |  |
| `addedValue` | uint256 |  |

#### Fn operationDecreaseAllowance

```solidity
function operationDecreaseAllowance(
    address account,
    address spender,
    uint256 subtractedValue
) 
    external
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address |  |
| `spender` | address |  |
| `subtractedValue` | uint256 |  |

#### Fn operationTransferFrom

```solidity
function operationTransferFrom(
    address account,
    address spender,
    address recipient,
    uint256 amount
) 
    external
```
_Perform ERC20 transferFrom by host contract._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address | The account to spend sender's funds. |
| `spender` | address | The account where the funds is sent from. |
| `recipient` | address | The recipient of the funds. |
| `amount` | uint256 | Number of tokens to be transferred.

@custom:modifiers
 - onlyHost |

#### Fn operationSend

```solidity
function operationSend(
    address spender,
    address recipient,
    uint256 amount,
    bytes userData
) 
    external
```
_Perform ERC777 send by host contract._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `spender` | address | The account where the funds is sent from. |
| `recipient` | address | The recipient of the funds. |
| `amount` | uint256 | Number of tokens to be transferred. |
| `userData` | bytes | Arbitrary user inputted data

@custom:modifiers
 - onlyHost |

#### Fn operationUpgrade

```solidity
function operationUpgrade(
    address account,
    uint256 amount
) 
    external
```
_Upgrade ERC20 to SuperToken by host contract._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address | The account to be changed. |
| `amount` | uint256 | Number of tokens to be upgraded (in 18 decimals)

@custom:modifiers
 - onlyHost |

#### Fn operationDowngrade

```solidity
function operationDowngrade(
    address account,
    uint256 amount
) 
    external
```
_Downgrade ERC20 to SuperToken by host contract._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address | The account to be changed. |
| `amount` | uint256 | Number of tokens to be downgraded (in 18 decimals)

@custom:modifiers
 - onlyHost |

### Events

#### Event AdminChanged

```solidity
event AdminChanged(
    address oldAdmin,
    address newAdmin
)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `oldAdmin` | address |  |
| `newAdmin` | address |  |

#### Event TokenUpgraded

```solidity
event TokenUpgraded(
    address account,
    uint256 amount
)
```

Token upgrade event

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address | Account where tokens are upgraded to |
| `amount` | uint256 | Amount of tokens upgraded (in 18 decimals) |

#### Event TokenDowngraded

```solidity
event TokenDowngraded(
    address account,
    uint256 amount
)
```

Token downgrade event

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `account` | address | Account whose tokens are downgraded |
| `amount` | uint256 | Amount of tokens downgraded |

#### Event ConstantOutflowNFTCreated

```solidity
event ConstantOutflowNFTCreated(
    contract IConstantOutflowNFT constantOutflowNFT
)
```

Constant Outflow NFT proxy created event

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `constantOutflowNFT` | contract IConstantOutflowNFT | constant outflow nft address |
#### Event ConstantInflowNFTCreated

```solidity
event ConstantInflowNFTCreated(
    contract IConstantInflowNFT constantInflowNFT
)
```

Constant Inflow NFT proxy created event

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `constantInflowNFT` | contract IConstantInflowNFT | constant inflow nft address |
#### Event PoolAdminNFTCreated

```solidity
event PoolAdminNFTCreated(
    contract IPoolAdminNFT poolAdminNFT
)
```

Pool Admin NFT proxy created event

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `poolAdminNFT` | contract IPoolAdminNFT | pool admin nft address |
#### Event PoolMemberNFTCreated

```solidity
event PoolMemberNFTCreated(
    contract IPoolMemberNFT poolMemberNFT
)
```

Pool Member NFT proxy created event

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `poolMemberNFT` | contract IPoolMemberNFT | pool member nft address |

### Error Codes

#### SUPER_TOKEN_CALLER_IS_NOT_OPERATOR_FOR_HOLDER

```solidity
error SUPER_TOKEN_CALLER_IS_NOT_OPERATOR_FOR_HOLDER()
```

#### SUPER_TOKEN_NOT_ERC777_TOKENS_RECIPIENT

```solidity
error SUPER_TOKEN_NOT_ERC777_TOKENS_RECIPIENT()
```

#### SUPER_TOKEN_INFLATIONARY_DEFLATIONARY_NOT_SUPPORTED

```solidity
error SUPER_TOKEN_INFLATIONARY_DEFLATIONARY_NOT_SUPPORTED()
```

#### SUPER_TOKEN_NO_UNDERLYING_TOKEN

```solidity
error SUPER_TOKEN_NO_UNDERLYING_TOKEN()
```

#### SUPER_TOKEN_ONLY_SELF

```solidity
error SUPER_TOKEN_ONLY_SELF()
```

#### SUPER_TOKEN_ONLY_ADMIN

```solidity
error SUPER_TOKEN_ONLY_ADMIN()
```

#### SUPER_TOKEN_ONLY_GOV_OWNER

```solidity
error SUPER_TOKEN_ONLY_GOV_OWNER()
```

#### SUPER_TOKEN_APPROVE_FROM_ZERO_ADDRESS

```solidity
error SUPER_TOKEN_APPROVE_FROM_ZERO_ADDRESS()
```

#### SUPER_TOKEN_APPROVE_TO_ZERO_ADDRESS

```solidity
error SUPER_TOKEN_APPROVE_TO_ZERO_ADDRESS()
```

#### SUPER_TOKEN_BURN_FROM_ZERO_ADDRESS

```solidity
error SUPER_TOKEN_BURN_FROM_ZERO_ADDRESS()
```

#### SUPER_TOKEN_MINT_TO_ZERO_ADDRESS

```solidity
error SUPER_TOKEN_MINT_TO_ZERO_ADDRESS()
```

#### SUPER_TOKEN_TRANSFER_FROM_ZERO_ADDRESS

```solidity
error SUPER_TOKEN_TRANSFER_FROM_ZERO_ADDRESS()
```

#### SUPER_TOKEN_TRANSFER_TO_ZERO_ADDRESS

```solidity
error SUPER_TOKEN_TRANSFER_TO_ZERO_ADDRESS()
```

#### SUPER_TOKEN_NFT_PROXY_ADDRESS_CHANGED

```solidity
error SUPER_TOKEN_NFT_PROXY_ADDRESS_CHANGED()
```

---

<a id="doc_60"></a>

## 📁 technical-reference / ISuperfluidPool

*파일 경로: technical-reference/ISuperfluidPool.mdx*

---
sidebar_position: 7
---

import CodeBlock from "@theme/CodeBlock";
import ISuperfluidPool from "!!raw-loader!@site/src/abis/ISuperfluidPool.json";


This is the technical reference related to the interface for any super token pool regardless of the distribution schemes.

### ABI

In order to interact with the `ISuperfluidPool` contract, you can use the following ABI:

<div>
<details>
<summary>Click here to show `ISuperfluidPool` ABI</summary>
<p>

<CodeBlock language="json">{ISuperfluidPool}</CodeBlock>

</p>
</details>
</div>

### SUPERFLUID_POOL_INVALID_TIME

```solidity
error SUPERFLUID_POOL_INVALID_TIME()
```

### SUPERFLUID_POOL_NO_POOL_MEMBERS

```solidity
error SUPERFLUID_POOL_NO_POOL_MEMBERS()
```

### SUPERFLUID_POOL_NO_ZERO_ADDRESS

```solidity
error SUPERFLUID_POOL_NO_ZERO_ADDRESS()
```

### SUPERFLUID_POOL_NOT_POOL_ADMIN_OR_GDA

```solidity
error SUPERFLUID_POOL_NOT_POOL_ADMIN_OR_GDA()
```

### SUPERFLUID_POOL_NOT_GDA

```solidity
error SUPERFLUID_POOL_NOT_GDA()
```

### SUPERFLUID_POOL_TRANSFER_UNITS_NOT_ALLOWED

```solidity
error SUPERFLUID_POOL_TRANSFER_UNITS_NOT_ALLOWED()
```

### SUPERFLUID_POOL_SELF_TRANSFER_NOT_ALLOWED

```solidity
error SUPERFLUID_POOL_SELF_TRANSFER_NOT_ALLOWED()
```

### Event MemberUnitsUpdated

```solidity
event MemberUnitsUpdated(
    contract ISuperfluidToken token,
    address member,
    uint128 oldUnits,
    uint128 newUnits
)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperfluidToken |  |
| `member` | address |  |
| `oldUnits` | uint128 |  |
| `newUnits` | uint128 |  |
### Event DistributionClaimed

```solidity
event DistributionClaimed(
    contract ISuperfluidToken token,
    address member,
    int256 claimedAmount,
    int256 totalClaimed
)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperfluidToken |  |
| `member` | address |  |
| `claimedAmount` | int256 |  |
| `totalClaimed` | int256 |  |

### Fn transferabilityForUnitsOwner

```solidity
function transferabilityForUnitsOwner(
) 
    external 
    returns (bool)
```

A boolean indicating whether pool members can transfer their units

### Fn distributionFromAnyAddress

```solidity
function distributionFromAnyAddress(
) 
    external 
    returns (bool)
```

A boolean indicating whether addresses other than the pool admin can distribute via the pool

### Fn admin

```solidity
function admin(
) 
    external 
    returns (address)
```
_The admin is the creator of the pool and has permissions to update member units
and is the recipient of the adjustment flow rate_

The pool admin

### Fn superToken

```solidity
function superToken(
) 
    external 
    returns (contract ISuperfluidToken)
```

The SuperToken for the pool

### Fn getTotalUnits

```solidity
function getTotalUnits(
) 
    external 
    returns (uint128)
```

The total units of the pool

### Fn getTotalConnectedUnits

```solidity
function getTotalConnectedUnits(
) 
    external 
    returns (uint128)
```

The total number of units of connected members

### Fn getTotalDisconnectedUnits

```solidity
function getTotalDisconnectedUnits(
) 
    external 
    returns (uint128)
```

The total number of units of disconnected members

### Fn getUnits

```solidity
function getUnits(
    address memberAddr
) 
    external 
    returns (uint128)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |

The total number of units for `memberAddr`

### Fn getTotalFlowRate

```solidity
function getTotalFlowRate(
) 
    external 
    returns (int96)
```

The total flow rate of the pool

### Fn getTotalConnectedFlowRate

```solidity
function getTotalConnectedFlowRate(
) 
    external 
    returns (int96)
```

The flow rate of the connected members

### Fn getTotalDisconnectedFlowRate

```solidity
function getTotalDisconnectedFlowRate(
) 
    external 
    returns (int96)
```

The flow rate of the disconnected members

### Fn getDisconnectedBalance

```solidity
function getDisconnectedBalance(
    uint32 time
) 
    external 
    returns (int256 balance)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `time` | uint32 | The time to query |

The balance of all the disconnected members at `time`

### Fn getTotalAmountReceivedByMember

```solidity
function getTotalAmountReceivedByMember(
    address memberAddr
) 
    external 
    returns (uint256 totalAmountReceived)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `totalAmountReceived` | uint256 | The total amount received by the member |

The total amount received by `memberAddr` in the pool

### Fn getMemberFlowRate

```solidity
function getMemberFlowRate(
    address memberAddr
) 
    external 
    returns (int96)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |

The flow rate a member is receiving from the pool

### Fn getClaimable

```solidity
function getClaimable(
    address memberAddr,
    uint32 time
) 
    external 
    returns (int256)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |
| `time` | uint32 | The time to query |

The claimable balance for `memberAddr` at `time` in the pool

### Fn getClaimableNow

```solidity
function getClaimableNow(
    address memberAddr
) 
    external 
    returns (int256 claimableBalance, uint256 timestamp)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |

The claimable balance for `memberAddr` at `block.timestamp` in the pool

### Fn updateMemberUnits

```solidity
function updateMemberUnits(
    address memberAddr,
    uint128 newUnits
) 
    external 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |
| `newUnits` | uint128 | The new units for the member |

Sets `memberAddr` ownedUnits to `newUnits`

### Fn claimAll

```solidity
function claimAll(
    address memberAddr
) 
    external 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `memberAddr` | address | The address of the member |

Claims the claimable balance for `memberAddr` at `block.timestamp`

### Fn claimAll

```solidity
function claimAll(
) 
    external 
    returns (bool)
```

Claims the claimable balance for `msg.sender` at `block.timestamp`

### Fn increaseAllowance

```solidity
function increaseAllowance(
    address spender,
    uint256 addedValue
) 
    external 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `spender` | address | The address of the spender |
| `addedValue` | uint256 | The amount to increase the allowance by |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | true if successful |

Increases the allowance of `spender` by `addedValue`

### Fn decreaseAllowance

```solidity
function decreaseAllowance(
    address spender,
    uint256 subtractedValue
) 
    external 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `spender` | address | The address of the spender |
| `subtractedValue` | uint256 | The amount to decrease the allowance by |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | true if successful |

Decreases the allowance of `spender` by `subtractedValue`

---

<a id="doc_61"></a>

## 📁 technical-reference / Protocol Architecture

*파일 경로: technical-reference/Architecture.mdx*

---
sidebar_position: 1
---
import ContractsTable from '@site/src/components/ContractsTable';


The Superfluid Protocol is designed with a modular and upgradable architecture, consisting of several smart contract components that interact with each other to facilitate real-time finance on the blockchain.

### Overview
The architecture diagram below provides a high-level overview of the Superfluid Protocol's components and their relationships.
It is the protocol deployed when a new `SuperfluidFrameworkDeployer` instance is created and the method `deployFramework()`.
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <img src="/assets/architecture.png" alt="Architecture" width="900" />
</div>
<div style={{ display: 'flex', justifyContent: 'center' }}>
    <p>*Architecture of the Superfluid Protocol*</p>
</div>

### Legend

- **Immutable Instance**: These are contract instances that are not intended to be upgraded or changed.
- **Upgradable Instance**: These are contract instances that are intended to be upgraded or changed, eventually by the Superfluid Protocol's Governance.
- **Link**: Represents the relationship or interaction between components.


### Components

#### SuperToken (UUPS Proxy - EIP-1967)

This is the fundamental smart contract within the Superfluid Protocol, which is an upgradable advanced token contract which inherits from the ERC20 standard, and enhances it
with additional features such as Money Streaming and Distributions.

:::note Unmanaged SuperTokens
Super Token contracts can be created by anyone, and can either be managed by the Superfluid Protocol ([The Host](#superfluid-host-contract-uups-proxy)), or completely unmanaged with no influence from the Host.
They can be used to represent any asset or right, and can be used in any context.
:::

#### Superfluid Agreements

##### ConstantFlowAgreementV1 (UUPS Proxy)

A versioned agreement that governs the continuous flow of tokens between parties, ie [Money Streaming](/docs/protocol/money-streaming/overview.mdx).

##### InstantDistributionAgreementV1 (UUPS Proxy)

A smart contract that manages the mechanisms for the instant distribution of tokens, a feature that allows for scalable one-to-many token distributions.

:::warning Deprecated
This agreement is in the process of being deprecated in favor of the more flexible [GeneralDistributionAgreementV1](#generaldistributionagreementv1-uups-proxy).
:::

##### GeneralDistributionAgreementV1 (UUPS Proxy)

A smart contract that manages the mechanisms for everything related to one-to-many transfers and streams, ie [Distributions](/docs/protocol/distributions/overview.mdx).

#### Infrastructure

##### Superfluid Host Contract (UUPS Proxy)

The central contract that hosts the Superfluid Protocol, managing the various tokens and agreements.

##### SuperTokenFactory (UUPS Proxy)

A factory contract for creating SuperTokens, likely with specific initial conditions or properties.

##### SuperfluidPool (UUPS Proxy)

This a contract representing the [Pools](/docs/protocol/distributions/guides/pools.mdx) created to manage Distributions.

#### Superfluid Governance

##### SuperfluidGovernanceII (UUPS Proxy)

The main governance contract that will allow Superfluid community members to participate in the governance of the protocol.

#### Existential NFTs

##### ConstantFlowNFT (UUPS Proxy)

Smart contract for non-fungible tokens (NFTs) that have a constant flow rate associated with them. These are NFTs minted to represent Money Streaming flows.

##### PoolAdminNFT (UUPS Proxy)

NFT contract representing admin rights over a [SuperfluidPool](#superfluidpool-uups-proxy).

##### PoolMemberNFT (UUPS Proxy)

This is an NFT contract where tokens represent membership within a pool, granting units to members in that pool.

### Learn more

The technical details and contract interactions are further documented in the codebase. Refer to the following for an in-depth understanding:

- [Superfluid Framework Deployment Steps](https://github.com/superfluid-finance/protocol-monorepo/blob/dev/packages/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeploymentSteps.sol).
- [Superfluid Protocol Monorepo Wiki](https://github.com/superfluid-finance/protocol-monorepo/wiki).

---

<a id="doc_62"></a>

## 📁 technical-reference / Subgraph Endpoints

*파일 경로: technical-reference/subgraph.mdx*

---
sidebar_position: 8
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


This document provides an overview of the available networks and their respective subgraph URLs. The format for the subgraph URL is the following:
`https://subgraph-endpoints.superfluid.dev/<canonical-name>/protocol-v1`

:::tip Automations subgraphs
Automation subgraphs have the following formats:
- Vesting Scheduler: `https://subgraph-endpoints.superfluid.dev/<canonical-name>/vesting-scheduler`
- Flow Scheduler: `https://subgraph-endpoints.superfluid.dev/<canonical-name>/flow-scheduler`
- Auto-wrap: `https://subgraph-endpoints.superfluid.dev/<canonical-name>/auto-wrap`
:::

### Available Networks

Below is a table of the available networks along with their details:

| Network Name | Canonical Name | Testnet | Chain ID | Subgraph URL |
| --- | --- | --- | --- | --- |
| Avalanche Fuji | avalanche-fuji | Yes | 43113 | [https://subgraph-endpoints.superfluid.dev/avalanche-fuji/protocol-v1](https://subgraph-endpoints.superfluid.dev/avalanche-fuji/protocol-v1) |
| Sepolia | eth-sepolia | Yes | 11155111 | [https://subgraph-endpoints.superfluid.dev/eth-sepolia/protocol-v1](https://subgraph-endpoints.superfluid.dev/eth-sepolia/protocol-v1) |
| Optimism Sepolia | optimism-sepolia | Yes | 11155420 | https://subgraph-endpoints.superfluid.dev/optimism-sepolia/protocol-v1 |
| Scroll Sepolia | scroll-sepolia | Yes | 534351 | https://subgraph-endpoints.superfluid.dev/scroll-sepolia/protocol-v1 |
| Gnosis Chain | xdai-mainnet | No | 100 | https://subgraph-endpoints.superfluid.dev/xdai-mainnet/protocol-v1 |
| Polygon | polygon-mainnet | No | 137 | https://subgraph-endpoints.superfluid.dev/polygon-mainnet/protocol-v1 |
| Optimism | optimism-mainnet | No | 10 | https://subgraph-endpoints.superfluid.dev/optimism-mainnet/protocol-v1 |
| Arbitrum One | arbitrum-one | No | 42161 | https://subgraph-endpoints.superfluid.dev/arbitrum-one/protocol-v1 |
| Avalanche C | avalanche-c | No | 43114 | https://subgraph-endpoints.superfluid.dev/avalanche-c/protocol-v1 |
| BNB Smart Chain | bsc-mainnet | No | 56 | https://subgraph-endpoints.superfluid.dev/bsc-mainnet/protocol-v1 |
| Ethereum | eth-mainnet | No | 1 | https://subgraph-endpoints.superfluid.dev/eth-mainnet/protocol-v1 |
| Celo | celo-mainnet | No | 42220 | https://subgraph-endpoints.superfluid.dev/celo-mainnet/protocol-v1 |
| Base | base-mainnet | No | 8453 | https://subgraph-endpoints.superfluid.dev/base-mainnet/protocol-v1 |
| Scroll | scroll-mainnet | No | 534352 | https://subgraph-endpoints.superfluid.dev/scroll-mainnet/protocol-v1 |
| Degen Chain | degenchain | No | 666666666 | https://subgraph-endpoints.superfluid.dev/degenchain/protocol-v1 |

---

<a id="doc_63"></a>

## 📁 technical-reference / SuperTokenV1Library

*파일 경로: technical-reference/SuperTokenV1Library.mdx*

---
sidebar_position: 1
---

**Library for Token Centric Interface**

The `SuperTokenV1Library` is a solidity library that allows you to interact with the Superfluid Protocol.
It is a comprehensive library for Superfluid protocol. It includes all the functions that are
required to interact with the Superfluid protocol. It includes functions for interacting with Money Streaming and Distributions.
In order to have access to the library, you need to:

- Import the library in your contract as such:

    `import "@superfluid-finance/ethereum-contracts/contracts/apps/SuperTokenV1Library.sol";`

- Make sure that you include the `using` statement in your contract:

    `using SuperTokenV1Library for ISuperToken;`


:::note Note 1
In the case of interacting with Native Super Tokens you should use `using SuperTokenV1Library for ISETH;` instead.
:::

:::note Note 2
It is important to "warm up" the cache and cache the `host`, `cfa`, `gda` before calling,
this is only applicable to Foundry tests where the vm.expectRevert() will not work as expected.
You must use vm.startPrank(account) instead of vm.prank when executing functions if the cache
isn't "warmed up" yet. vm.prank impersonates the account only for the first call, which will be
used for caching.
:::

### Fn flowX

```solidity
function flowX(
    contract ISuperToken token,
    address receiverOrPool,
    int96 flowRate
) 
    internal 
    returns (bool)
```
_creates a flow to an account or to pool members.
If the receiver is an account, it uses the CFA, if it's a pool it uses the GDA._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `receiverOrPool` | address | The receiver (account) or pool |
| `flowRate` | int96 | the flowRate to be set. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the operation was successful.
Note that all the specifics of the underlying agreement used still apply.
E.g. if the GDA is used, the effective flowRate may differ from the selected one. |

### Fn transferX

```solidity
function transferX(
    contract ISuperToken token,
    address receiverOrPool,
    uint256 amount
) 
    internal 
    returns (bool)
```
_transfers `amount` to an account or distributes it to pool members._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `receiverOrPool` | address | The receiver (account) or pool |
| `amount` | uint256 | the amount to be transferred/distributed |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the operation was successful.
Note in case of distribution, the effective amount may be smaller than requested. |

### Fn getFlowRate

```solidity
function getFlowRate(
    contract ISuperToken token,
    address sender,
    address receiverOrPool
) 
    internal 
    returns (int96 flowRate)
```
_get flow rate between two accounts for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | The sender of the flow |
| `receiverOrPool` | address | The receiver or pool receiving or distributing the flow |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `flowRate` | int96 | The flow rate
Note: edge case: if a CFA stream is going to a pool, it will return 0. |

### Fn getFlowInfo

```solidity
function getFlowInfo(
    contract ISuperToken token,
    address sender,
    address receiverOrPool
) 
    internal 
    returns (uint256 lastUpdated, int96 flowRate, uint256 deposit, uint256 owedDeposit)
```
_get flow info between an account and another account or pool for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | The sender of the flow |
| `receiverOrPool` | address | The receiver or pool receiving or distributing the flow |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `lastUpdated` | uint256 | Timestamp of flow creation or last flowrate change |
| `flowRate` | int96 | The flow rate |
| `deposit` | uint256 | The amount of deposit the flow |
| `owedDeposit` | uint256 | The amount of owed deposit of the flow
Note: edge case: a CFA stream going to a pool will not be "seen". |

### Fn getNetFlowRate

```solidity
function getNetFlowRate(
    contract ISuperToken token,
    address account
) 
    internal 
    returns (int96 flowRate)
```
_get net flow rate for given account for given token (CFA + GDA)_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `account` | address | Account to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `flowRate` | int96 | The net flow rate of the account |

### Fn getNetFlowInfo

```solidity
function getNetFlowInfo(
    contract ISuperToken token,
    address account
) 
    internal 
    returns (uint256 lastUpdated, int96 flowRate, uint256 deposit, uint256 owedDeposit)
```
_get the aggregated flow info of the account (CFA + GDA)_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `account` | address | Account to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `lastUpdated` | uint256 | Timestamp of the last change of the net flow |
| `flowRate` | int96 | The net flow rate of token for account |
| `deposit` | uint256 | The sum of all deposits for account's flows |
| `owedDeposit` | uint256 | The sum of all owed deposits for account's flows |

### Fn getBufferAmountByFlowRate

```solidity
function getBufferAmountByFlowRate(
    contract ISuperToken token,
    int96 flowRate
) 
    internal 
    returns (uint256 bufferAmount)
```
_calculate buffer needed for a CFA flow with the given flowrate (for GDA, see 2nd notice below)_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowRate` | int96 | The flowrate to calculate the needed buffer for |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `bufferAmount` | uint256 | The buffer amount based on flowRate, liquidationPeriod and minimum deposit |

the returned amount is exact only for the scenario where no flow exists before.
In order to get the buffer delta for a delta flowrate, you need to get the buffer amount
for the new total flowrate and subtract the previous buffer.
That's because there's not always linear proportionality between flowrate and buffer.
for GDA flows, the required buffer is typically slightly lower.
That's due to an implementation detail (round-up "clipping" to 64 bit in the CFA).
The return value of this method is thus to be considered not a precise value, but a
lower bound for GDA flows.

### Fn flow

```solidity
function flow(
    contract ISuperToken token,
    address receiver,
    int96 flowRate
) 
    internal 
    returns (bool)
```
_Sets the given CFA flowrate between the caller and a given receiver.
If there's no pre-existing flow and `flowRate` non-zero, a new flow is created.
If there's an existing flow and `flowRate` non-zero, the flowRate of that flow is updated.
If there's an existing flow and `flowRate` zero, the flow is deleted.
If the existing and given flowRate are equal, no action is taken.
On creation of a flow, a "buffer" amount is automatically detracted from the sender account's available balance.
If the sender account is solvent when the flow is deleted, this buffer is redeemed to it._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The wanted flowrate in wad/second. Only positive values are valid here. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | bool |

### Fn flow (with User Data)

```solidity
function flow(
    contract ISuperToken token,
    address receiver,
    int96 flowRate,
    bytes userData
) 
    internal 
    returns (bool)
```
_Set CFA flowrate with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The wanted flowrate in wad/second. Only positive values are valid here. |
| `userData` | bytes | The userdata passed along with call |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | bool |

### Fn createFlow

```solidity
function createFlow(
    contract ISuperToken token,
    address receiver,
    int96 flowRate
) 
    internal 
    returns (bool)
```
_Create flow without userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |

### Fn createFlow (with User Data)

```solidity
function createFlow(
    contract ISuperToken token,
    address receiver,
    int96 flowRate,
    bytes userData
) 
    internal 
    returns (bool)
```
_Create flow with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `userData` | bytes | The userdata passed along with call |

### Fn updateFlow

```solidity
function updateFlow(
    contract ISuperToken token,
    address receiver,
    int96 flowRate
) 
    internal 
    returns (bool)
```
_Update flow without userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |

### Fn updateFlow (with User Data)

```solidity
function updateFlow(
    contract ISuperToken token,
    address receiver,
    int96 flowRate,
    bytes userData
) 
    internal 
    returns (bool)
```
_Update flow with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `userData` | bytes | The userdata passed along with call |

### Fn deleteFlow

```solidity
function deleteFlow(
    contract ISuperToken token,
    address sender,
    address receiver
) 
    internal 
    returns (bool)
```
_Delete flow without userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |

### Fn deleteFlow (with User Data)

```solidity
function deleteFlow(
    contract ISuperToken token,
    address sender,
    address receiver,
    bytes userData
) 
    internal 
    returns (bool)
```
_Delete flow with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `userData` | bytes | The userdata passed along with call |

### Fn flowFrom

```solidity
function flowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate
) 
    internal 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The wanted flowRate in wad/second. Only positive values are valid here. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | bool |

Like `flow`, but can be invoked by an account with flowOperator permissions
on behalf of the sender account.

### Fn flowFrom (with User Data)

```solidity
function flowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes userData
) 
    internal 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The wanted flowRate in wad/second. Only positive values are valid here. |
| `userData` | bytes | The userdata passed along with call |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | bool |

Like `flowFrom`, but takes userData

### Fn setFlowPermissions

```solidity
function setFlowPermissions(
    contract ISuperToken token,
    address flowOperator,
    bool allowCreate,
    bool allowUpdate,
    bool allowDelete,
    int96 flowRateAllowance
) 
    internal 
    returns (bool)
```
_Update permissions for flow operator_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address given flow permissions |
| `allowCreate` | bool | creation permissions |
| `allowUpdate` | bool |  |
| `allowDelete` | bool |  |
| `flowRateAllowance` | int96 | The allowance provided to flowOperator |

### Fn setMaxFlowPermissions

```solidity
function setMaxFlowPermissions(
    contract ISuperToken token,
    address flowOperator
) 
    internal 
    returns (bool)
```
_Update permissions for flow operator - give operator max permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address given flow permissions |

### Fn revokeFlowPermissions

```solidity
function revokeFlowPermissions(
    contract ISuperToken token,
    address flowOperator
) 
    internal 
    returns (bool)
```
_Update permissions for flow operator - revoke all permission_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address given flow permissions |

### Fn increaseFlowRateAllowance

```solidity
function increaseFlowRateAllowance(
    contract ISuperToken token,
    address flowOperator,
    int96 addedFlowRateAllowance
) 
    internal 
    returns (bool)
```
_Increases the flow rate allowance for flow operator_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is increased |
| `addedFlowRateAllowance` | int96 | amount to increase allowance by |

allowing userData to be a parameter here triggered stack too deep error

### Fn increaseFlowRateAllowance (with User Data)

```solidity
function increaseFlowRateAllowance(
    contract ISuperToken token,
    address flowOperator,
    int96 addedFlowRateAllowance,
    bytes userData
) 
    internal 
    returns (bool)
```
_Increases the flow rate allowance for flow operator_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is increased |
| `addedFlowRateAllowance` | int96 | amount to increase allowance by |
| `userData` | bytes | The userdata passed along with call |

allowing userData to be a parameter here triggered stack too deep error

### Fn decreaseFlowRateAllowance

```solidity
function decreaseFlowRateAllowance(
    contract ISuperToken token,
    address flowOperator,
    int96 subtractedFlowRateAllowance
) 
    internal 
    returns (bool)
```
_Decreases the flow rate allowance for flow operator_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is decreased |
| `subtractedFlowRateAllowance` | int96 | amount to decrease allowance by |

allowing userData to be a parameter here triggered stack too deep error

### Fn decreaseFlowRateAllowance (with User Data)

```solidity
function decreaseFlowRateAllowance(
    contract ISuperToken token,
    address flowOperator,
    int96 subtractedFlowRateAllowance,
    bytes userData
) 
    internal 
    returns (bool)
```
_Decreases the flow rate allowance for flow operator_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is decreased |
| `subtractedFlowRateAllowance` | int96 | amount to decrease allowance by |
| `userData` | bytes | The userdata passed along with call |

allowing userData to be a parameter here triggered stack too deep error

### Fn increaseFlowRateAllowanceWithPermissions

```solidity
function increaseFlowRateAllowanceWithPermissions(
    contract ISuperToken token,
    address flowOperator,
    uint8 permissionsToAdd,
    int96 addedFlowRateAllowance
) 
    internal 
    returns (bool)
```
_Increases the flow rate allowance for flow operator and adds the permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is increased |
| `permissionsToAdd` | uint8 | The permissions to add for the flow operator |
| `addedFlowRateAllowance` | int96 | amount to increase allowance by |

allowing userData to be a parameter here triggered stack too deep error

### Fn increaseFlowRateAllowanceWithPermissions (with User Data)

```solidity
function increaseFlowRateAllowanceWithPermissions(
    contract ISuperToken token,
    address flowOperator,
    uint8 permissionsToAdd,
    int96 addedFlowRateAllowance,
    bytes userData
) 
    internal 
    returns (bool)
```
_Increases the flow rate allowance for flow operator and adds the permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is increased |
| `permissionsToAdd` | uint8 | The permissions to add for the flow operator |
| `addedFlowRateAllowance` | int96 | amount to increase allowance by |
| `userData` | bytes | The userdata passed along with call |

allowing userData to be a parameter here triggered stack too deep error

### Fn decreaseFlowRateAllowanceWithPermissions

```solidity
function decreaseFlowRateAllowanceWithPermissions(
    contract ISuperToken token,
    address flowOperator,
    uint8 permissionsToRemove,
    int96 subtractedFlowRateAllowance
) 
    internal 
    returns (bool)
```
_Decreases the flow rate allowance for flow operator and removes the permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is subtracted |
| `permissionsToRemove` | uint8 | The permissions to remove for the flow operator |
| `subtractedFlowRateAllowance` | int96 | amount to subtract allowance by |

allowing userData to be a parameter here triggered stack too deep error

### Fn decreaseFlowRateAllowanceWithPermissions (with User Data)

```solidity
function decreaseFlowRateAllowanceWithPermissions(
    contract ISuperToken token,
    address flowOperator,
    uint8 permissionsToRemove,
    int96 subtractedFlowRateAllowance,
    bytes userData
) 
    internal 
    returns (bool)
```
_Decreases the flow rate allowance for flow operator and removes the permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address whose flow rate allowance is subtracted |
| `permissionsToRemove` | uint8 | The permissions to remove for the flow operator |
| `subtractedFlowRateAllowance` | int96 | amount to subtract allowance by |
| `userData` | bytes | The userdata passed along with call |

allowing userData to be a parameter here triggered stack too deep error

### Fn createFlowFrom

```solidity
function createFlowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate
) 
    internal 
    returns (bool)
```
_Creates flow as an operator without userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |

### Fn createFlowFrom (with User Data)

```solidity
function createFlowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes userData
) 
    internal 
    returns (bool)
```
_Creates flow as an operator with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `userData` | bytes | The user provided data |

### Fn updateFlowFrom

```solidity
function updateFlowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate
) 
    internal 
    returns (bool)
```
_Updates flow as an operator without userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |

### Fn updateFlowFrom (with User Data)

```solidity
function updateFlowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes userData
) 
    internal 
    returns (bool)
```
_Updates flow as an operator with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `userData` | bytes | The user provided data |

### Fn deleteFlowFrom

```solidity
function deleteFlowFrom(
    contract ISuperToken token,
    address sender,
    address receiver
) 
    internal 
    returns (bool)
```
_Deletes flow as an operator without userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |

### Fn deleteFlowFrom (with User Data)

```solidity
function deleteFlowFrom(
    contract ISuperToken token,
    address sender,
    address receiver,
    bytes userData
) 
    internal 
    returns (bool)
```
_Deletes flow as an operator with userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `userData` | bytes | The user provided data |

### Fn createFlowWithCtx

```solidity
function createFlowWithCtx(
    contract ISuperToken token,
    address receiver,
    int96 flowRate,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Create flow with context and userData_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn createFlowFromWithCtx

```solidity
function createFlowFromWithCtx(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Create flow by operator with context_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn updateFlowWithCtx

```solidity
function updateFlowWithCtx(
    contract ISuperToken token,
    address receiver,
    int96 flowRate,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Update flow with context_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn updateFlowFromWithCtx

```solidity
function updateFlowFromWithCtx(
    contract ISuperToken token,
    address sender,
    address receiver,
    int96 flowRate,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Update flow by operator with context_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The receiver of the flow |
| `receiver` | address | The receiver of the flow |
| `flowRate` | int96 | The desired flowRate |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn deleteFlowWithCtx

```solidity
function deleteFlowWithCtx(
    contract ISuperToken token,
    address sender,
    address receiver,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Delete flow with context_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn deleteFlowFromWithCtx

```solidity
function deleteFlowFromWithCtx(
    contract ISuperToken token,
    address sender,
    address receiver,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Delete flow by operator with context_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token to flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn setFlowPermissionsWithCtx

```solidity
function setFlowPermissionsWithCtx(
    contract ISuperToken token,
    address flowOperator,
    bool allowCreate,
    bool allowUpdate,
    bool allowDelete,
    int96 flowRateAllowance,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Update permissions for flow operator in callback_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address given flow permissions |
| `allowCreate` | bool | creation permissions |
| `allowUpdate` | bool |  |
| `allowDelete` | bool |  |
| `flowRateAllowance` | int96 | The allowance provided to flowOperator |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

allowing userData to be a parameter here triggered stack too deep error

### Fn setMaxFlowPermissionsWithCtx

```solidity
function setMaxFlowPermissionsWithCtx(
    contract ISuperToken token,
    address flowOperator,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Update permissions for flow operator - give operator max permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address given flow permissions |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn revokeFlowPermissionsWithCtx

```solidity
function revokeFlowPermissionsWithCtx(
    contract ISuperToken token,
    address flowOperator,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Update permissions for flow operator - revoke all permission_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `flowOperator` | address | The address given flow permissions |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn getCFAFlowRate

```solidity
function getCFAFlowRate(
    contract ISuperToken token,
    address sender,
    address receiver
) 
    internal 
    returns (int96 flowRate)
```
_get CFA flow rate between two accounts for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `flowRate` | int96 | The flow rate |

### Fn getCFAFlowInfo

```solidity
function getCFAFlowInfo(
    contract ISuperToken token,
    address sender,
    address receiver
) 
    internal 
    returns (uint256 lastUpdated, int96 flowRate, uint256 deposit, uint256 owedDeposit)
```
_get CFA flow info between two accounts for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | The sender of the flow |
| `receiver` | address | The receiver of the flow |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `lastUpdated` | uint256 | Timestamp of flow creation or last flowrate change |
| `flowRate` | int96 | The flow rate |
| `deposit` | uint256 | The amount of deposit the flow |
| `owedDeposit` | uint256 | The amount of owed deposit of the flow |

### Fn getCFANetFlowRate

```solidity
function getCFANetFlowRate(
    contract ISuperToken token,
    address account
) 
    internal 
    returns (int96 flowRate)
```
_get CFA net flow rate for given account for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `account` | address | Account to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `flowRate` | int96 | The net flow rate of the account |

### Fn getCFANetFlowInfo

```solidity
function getCFANetFlowInfo(
    contract ISuperToken token,
    address account
) 
    internal 
    returns (uint256 lastUpdated, int96 flowRate, uint256 deposit, uint256 owedDeposit)
```
_get the aggregated CFA flow info of the account_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `account` | address | Account to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `lastUpdated` | uint256 | Timestamp of the last change of the net flow |
| `flowRate` | int96 | The net flow rate of token for account |
| `deposit` | uint256 | The sum of all deposits for account's flows |
| `owedDeposit` | uint256 | The sum of all owed deposits for account's flows |

### Fn getFlowPermissions

```solidity
function getFlowPermissions(
    contract ISuperToken token,
    address sender,
    address flowOperator
) 
    internal 
    returns (bool allowCreate, bool allowUpdate, bool allowDelete, int96 flowRateAllowance)
```
_get existing CFA flow permissions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `sender` | address | sender of a flow |
| `flowOperator` | address | the address we are checking permissions of for sender & token |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `allowCreate` | bool | is true if the flowOperator can create flows |
| `allowUpdate` | bool | is true if the flowOperator can update flows |
| `allowDelete` | bool | is true if the flowOperator can delete flows |
| `flowRateAllowance` | int96 | The flow rate allowance the flowOperator is granted (only goes down) |

### Fn createPool

```solidity
function createPool(
    contract ISuperToken token,
    address admin,
    struct PoolConfig poolConfig
) 
    internal 
    returns (contract ISuperfluidPool pool)
```
_Creates a new Superfluid Pool._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `admin` | address | The pool admin address. |
| `poolConfig` | struct PoolConfig | The pool configuration (see PoolConfig in IGeneralDistributionAgreementV1.sol) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `pool` | contract ISuperfluidPool | The address of the deployed Superfluid Pool |

### Fn createPool

```solidity
function createPool(
    contract ISuperToken token,
    address admin
) 
    internal 
    returns (contract ISuperfluidPool pool)
```
_Creates a new Superfluid Pool with default PoolConfig: units not transferrable, allow multi-distributors_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `admin` | address | The pool admin address. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `pool` | contract ISuperfluidPool | The address of the deployed Superfluid Pool |

### Fn createPool

```solidity
function createPool(
    contract ISuperToken token
) 
    internal 
    returns (contract ISuperfluidPool pool)
```
_Creates a new Superfluid Pool with default PoolConfig and the caller set as admin_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken |  |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `pool` | contract ISuperfluidPool | The address of the deployed Superfluid Pool |

### Fn claimAll

```solidity
function claimAll(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    address memberAddress
) 
    internal 
    returns (bool)
```
_Claims all tokens from the pool._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to claim from. |
| `memberAddress` | address | The address of the member to claim for. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the claim was successful. |

### Fn claimAll (with User Data)

```solidity
function claimAll(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    address memberAddress,
    bytes userData
) 
    internal 
    returns (bool)
```
_Claims all tokens from the pool._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to claim from. |
| `memberAddress` | address | The address of the member to claim for. |
| `userData` | bytes | User-specific data. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the claim was successful. |

### Fn connectPool

```solidity
function connectPool(
    contract ISuperToken token,
    contract ISuperfluidPool pool
) 
    internal 
    returns (bool)
```
_Connects a pool member to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to connect. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the connection was successful. |

### Fn connectPool (with User Data)

```solidity
function connectPool(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    bytes userData
) 
    internal 
    returns (bool)
```
_Connects a pool member to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to connect. |
| `userData` | bytes | User-specific data. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the connection was successful. |

### Fn disconnectPool

```solidity
function disconnectPool(
    contract ISuperToken token,
    contract ISuperfluidPool pool
) 
    internal 
    returns (bool)
```
_Disconnects a pool member from `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to disconnect. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the disconnection was successful. |

### Fn disconnectPool (with User Data)

```solidity
function disconnectPool(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    bytes userData
) 
    internal 
    returns (bool)
```
_Disconnects a pool member from `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to disconnect. |
| `userData` | bytes | User-specific data. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the disconnection was successful. |

### Fn distribute

```solidity
function distribute(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    uint256 requestedAmount
) 
    internal 
    returns (bool)
```
_Tries to distribute `requestedAmount` amount of `token` from `from` to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool address. |
| `requestedAmount` | uint256 | The amount of tokens to distribute. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the distribution was successful. |

### Fn distribute (with User Data)

```solidity
function distribute(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool pool,
    uint256 requestedAmount,
    bytes userData
) 
    internal 
    returns (bool)
```
_Tries to distribute `requestedAmount` amount of `token` from `from` to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `from` | address | The address from which to distribute tokens. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool address. |
| `requestedAmount` | uint256 | The amount of tokens to distribute. |
| `userData` | bytes | User-specific data. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the distribution was successful. |

### Fn distributeFlow

```solidity
function distributeFlow(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    int96 requestedFlowRate
) 
    internal 
    returns (bool)
```
_Tries to distribute flow at `requestedFlowRate` of `token` from `from` to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool address. |
| `requestedFlowRate` | int96 | The flow rate of tokens to distribute. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the distribution was successful. |

### Fn distributeFlow (with User Data)

```solidity
function distributeFlow(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool pool,
    int96 requestedFlowRate,
    bytes userData
) 
    internal 
    returns (bool)
```
_Tries to distribute flow at `requestedFlowRate` of `token` from `from` to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `from` | address | The address from which to distribute tokens. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool address. |
| `requestedFlowRate` | int96 | The flow rate of tokens to distribute. |
| `userData` | bytes | User-specific data. |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `[0]` | bool | A boolean value indicating whether the distribution was successful. |

### Fn claimAllWithCtx

```solidity
function claimAllWithCtx(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    address memberAddress,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Claims all tokens from the pool._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to claim from. |
| `memberAddress` | address | The address of the member to claim for. |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn connectPoolWithCtx

```solidity
function connectPoolWithCtx(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Connects a pool member to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to connect. |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn disconnectPoolWithCtx

```solidity
function disconnectPoolWithCtx(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Disconnects a pool member from `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool to disconnect. |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn distributeWithCtx

```solidity
function distributeWithCtx(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool pool,
    uint256 requestedAmount,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Tries to distribute `requestedAmount` amount of `token` from `from` to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `from` | address | The address from which to distribute tokens. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool address. |
| `requestedAmount` | uint256 | The amount of tokens to distribute. |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn distributeFlowWithCtx

```solidity
function distributeFlowWithCtx(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool pool,
    int96 requestedFlowRate,
    bytes ctx
) 
    internal 
    returns (bytes newCtx)
```
_Tries to distribute flow at `requestedFlowRate` of `token` from `from` to `pool`._

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The Super Token address. |
| `from` | address | The address from which to distribute tokens. |
| `pool` | contract ISuperfluidPool | The Superfluid Pool address. |
| `requestedFlowRate` | int96 | The flow rate of tokens to distribute. |
| `ctx` | bytes | Context bytes (see ISuperfluid.sol for Context struct) |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `newCtx` | bytes | The updated context after the execution of the agreement function |

### Fn getGDAFlowRate

```solidity
function getGDAFlowRate(
    contract ISuperToken token,
    address distributor,
    contract ISuperfluidPool pool
) 
    internal 
    returns (int96 flowRate)
```
_get flowrate between a distributor and pool for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `distributor` | address | The ditributor of the flow |
| `pool` | contract ISuperfluidPool | The GDA pool |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `flowRate` | int96 | The flow rate |

### Fn getFlowDistributionFlowRate

```solidity
function getFlowDistributionFlowRate(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool to
) 
    internal 
    returns (int96)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken |  |
| `from` | address |  |
| `to` | contract ISuperfluidPool |  |

alias of getGDAFlowRate

### Fn getGDAFlowInfo

```solidity
function getGDAFlowInfo(
    contract ISuperToken token,
    address distributor,
    contract ISuperfluidPool pool
) 
    internal 
    returns (uint256 lastUpdated, int96 flowRate, uint256 deposit)
```
_get flow info of a distributor to a pool for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | The token used in flow |
| `distributor` | address | The ditributor of the flow |
| `pool` | contract ISuperfluidPool | The GDA pool |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `lastUpdated` | uint256 | Timestamp of flow creation or last flowrate change |
| `flowRate` | int96 | The flow rate |
| `deposit` | uint256 | The amount of deposit the flow |

### Fn getGDANetFlowRate

```solidity
function getGDANetFlowRate(
    contract ISuperToken token,
    address account
) 
    internal 
    returns (int96 flowRate)
```
_get GDA net flow rate for given account for given token_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `account` | address | Account to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `flowRate` | int96 | The net flow rate of the account |

### Fn getGDANetFlowInfo

```solidity
function getGDANetFlowInfo(
    contract ISuperToken token,
    address account
) 
    internal 
    returns (uint256 lastUpdated, int96 flowRate, uint256 deposit, uint256 owedDeposit)
```
_get the aggregated GDA flow info of the account_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `account` | address | Account to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `lastUpdated` | uint256 | Timestamp of the last change of the net flow |
| `flowRate` | int96 | The net flow rate of token for account |
| `deposit` | uint256 | The sum of all deposits for account's flows |
| `owedDeposit` | uint256 | The sum of all owed deposits for account's flows |

### Fn getPoolAdjustmentFlowRate

```solidity
function getPoolAdjustmentFlowRate(
    contract ISuperToken token,
    contract ISuperfluidPool pool
) 
    internal 
    returns (int96 poolAdjustmentFlowRate)
```
_get the adjustment flow rate for a pool_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `pool` | contract ISuperfluidPool | The pool to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `poolAdjustmentFlowRate` | int96 | The adjustment flow rate of the pool |

### Fn getTotalAmountReceivedByMember

```solidity
function getTotalAmountReceivedByMember(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    address memberAddr
) 
    internal 
    returns (uint256 totalAmountReceived)
```
_Get the total amount of tokens received by a member via instant and flowing distributions_

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken | Super token address |
| `pool` | contract ISuperfluidPool | The pool to query |
| `memberAddr` | address | The member to query |

##### Return Values

| Name | Type | Description |
| :--- | :--- | :---------- |
| `totalAmountReceived` | uint256 | The total amount received by the member |

### Fn getTotalAmountReceivedFromPool

```solidity
function getTotalAmountReceivedFromPool(
    contract ISuperToken token,
    contract ISuperfluidPool pool,
    address memberAddr
) 
    internal 
    returns (uint256 totalAmountReceived)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken |  |
| `pool` | contract ISuperfluidPool |  |
| `memberAddr` | address |  |

alias for `getTotalAmountReceivedByMember`

### Fn estimateFlowDistributionActualFlowRate

```solidity
function estimateFlowDistributionActualFlowRate(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool to,
    int96 requestedFlowRate
) 
    internal 
    returns (int96 actualFlowRate, int96 totalDistributionFlowRate)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken |  |
| `from` | address |  |
| `to` | contract ISuperfluidPool |  |
| `requestedFlowRate` | int96 |  |

### Fn estimateDistributionActualAmount

```solidity
function estimateDistributionActualAmount(
    contract ISuperToken token,
    address from,
    contract ISuperfluidPool to,
    uint256 requestedAmount
) 
    internal 
    returns (uint256 actualAmount)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken |  |
| `from` | address |  |
| `to` | contract ISuperfluidPool |  |
| `requestedAmount` | uint256 |  |

### Fn isMemberConnected

```solidity
function isMemberConnected(
    contract ISuperToken token,
    address pool,
    address member
) 
    internal 
    returns (bool)
```

##### Parameters

| Name | Type | Description |
| :--- | :--- | :---------- |
| `token` | contract ISuperToken |  |
| `pool` | address |  |
| `member` | address |  |

---

<a id="doc_64"></a>

## 📁 use-cases / Superfluid Vesting

*파일 경로: use-cases/vesting.mdx*

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Superfluid vesting is simple, non-custodial, liquid and composable. Anyone can create Superfluid vesting schedules easily by using the no-code
Superfluid Dashboard or the Vesting Scheduler SDK built on a robust smart contract framework


### Vesting with the Superfluid Dashboard (No-code)

#### Step 1: Accessing the Dashboard

Navigate to the [Superfluid Dashboard](https://app.superfluid.finance/vesting). Ensure you are connected to the appropriate network (e.g., Polygon Mumbai for testing or Ethereum mainnet for live transactions).

<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
  <img src="/assets/dashboard-vesting.png" alt="Vesting Dashboard" style={{ maxWidth: '80%' }} />
</div>
<br/>

:::note
Vesting via the dashboard requires a simple whitelisting. Register your interest to be whitelisted [here](https://airtable.com/appmq3TJDdQUrTQpx/shr6iaRWUXVZwVWSd).

:::

#### Step 2: Creating the Vesting Schedule
Fill in the information below in order to create a vesting schedule:

<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
  <img src="/assets/vesting-schedule.gif" alt="Create Vesting Schedule" style={{ maxWidth: '80%' }} />
</div>
<br/>
1. **Receiver**: Enter the public address, ENS, or Lens of the recipient.
2. **Super Token**: Select the Super Token you wish to vest. If you don't have super tokens, you can wrap your tokens using the [Super Token Wrapper](https://app.superfluid.finance/wrap).
3. **Vesting Start Date**: Set the date and time when the vesting will start.
4. **Total Vested Amount**: Input the total amount of tokens to be vested.
5. **Total Vesting Period**: Specify the duration over which the tokens will vest.
6. **Optional Cliff**: Toggle the 'Add Cliff' option and specify the cliff amount and period if needed.

:::note
The "cliff amount" is the amount of tokens that will be vested at the start of the vesting period. For example, if you set a cliff of 100 tokens, the recipient will receive 100 tokens at the start of the vesting period, and the remaining tokens will be vested over the vesting period.
:::

#### Step 3: Preview and Create

After entering the vesting parameters, preview the vesting schedule to ensure everything is correct. Then, create the vesting schedule with a single transaction.

<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
  <img src="/assets/vesting-preview.png" alt="Vesting Preview" style={{ maxWidth: '80%' }} />
</div>
<br/>

#### Step 4: Sharing the Vesting Schedule

A link to the vesting schedule status page can be shared with the recipient, providing them with an up-to-date view of their vesting progress.
<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
  <img src="/assets/vesting-ongoing.png" alt="Vesting Custom Page" style={{ maxWidth: '80%' }} />
</div>
<br/>

### Vesting using the Superfluid Vesting Scheduler (for Devs)

The Vesting Scheduler is a sophisticated smart contract designed for setting up token vesting schedules.
It's non-custodial and operates by moving tokens directly from your wallet or Safe to a specified recipient.
The contract includes options for adding cliffs, after which it initiates a linear vesting process through a Superfluid stream,
ensuring the recipient receives tokens directly in their wallet without any need for claiming.

For a more detailed explanation of the Vesting Scheduler, check out the Vesting Scheduler Automation [Full Guide](/docs/protocol/advanced-topics/automations/vesting-scheduler).

If you have questions about how to build with this smart contract framework, don't hesitate to reach out to our team or community on [Discord](https://discord.gg/pPzPEDMVua)!


---

### Benefits of Superfluid Vesting

Superfluid vesting offers:

* **Simple UI**: A user-friendly interface allowing easy setup in just a few clicks.
* **Full Liquidity**: Maintained liquidity for senders and immediate token flow for receivers.
* **Composability**: The ability to transfer vested tokens seamlessly to DeFi products.
* **Reduced Volatility**: Tokens are streamed every second, mitigating market volatility.
* **Enhanced Security**: Safe streaming without locking tokens in a contract.
* **No Custody**: Tokens are streamed directly to the recipient's wallet.

For a hands-on demonstration, try setting up a vesting schedule on the Superfluid Dashboard or explore building with the smart contract framework today.

---

*병합된 문서의 끝*
