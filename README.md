# Follow The Herd

**Twitter community mapping by topic**

An attempt to use group theory to identify communities on twitter based on
retweet and favorite habits of pre qualified statuses on twitter.

- [Follow The Herd](#follow-the-herd)
  - [Data Collection](#data-collection)
    - [Base data set](#base-data-set)
    - [Additional data](#additional-data)
  - [Data model](#data-model)


## Data Collection ##

### Base data set ###
1. Qualify one status
2. Collet all status IDs posted by or retweeted by the original poster
3. Collect all(?) retweeting accounts of our one post
4. Collect all the statuses ID each account
5. Calculate association between each account and each other account based on
   the ratio between the total post of the account and the intersection of the
   posts tweeted by the target account.
6. Identify core community member account by high aggregated associativity of
   other account to them. (Rate average reverse associativity should be a good
   indicator)
7. Identify core statuses by high number of retweets within the community above
   a threshold.
8. Repeat the process for all core statuses until no more status with retweet
   rates above the threshold are available.

### Additional data ###
1. Figure out how to scrape favorites
2. Do the same with favorites

## Data model
We will use a graph database wherein each post is a node 
