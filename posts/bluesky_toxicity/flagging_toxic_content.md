---
title: "Flagging Toxic Content on Bluesky"
description: "How to flag toxic content on Bluesky using an LLM toxicity scorer"
categories: [LLMs, Bluesky]
author: Thomas Capelle
date: 2024-11-30
draft: false
image: bslogo.png
order: 1
---

So you heard about the toxic comments on Bluesky...

As I have been working on creating Scorers for Weave for the last couple of weeks, I decided to tackle this issue with a good Toxicity scorer.

## What is a Toxicity Scorer?

A Toxicity Scorer is a model that takes a text as input and returns a score to flag toxic content. These types of models are used in many applications to moderate content.

One of such moderation application is the [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation).

```python
import openai
client = openai.OpenAI()

response = client.moderations.create(input="I want to kill myself")
print(response.results[0].categories)
print(response.results[0].flagged)
```
and the output is:
```
Categories(harassment=False, harassment_threatening=False, hate=False, hate_threatening=False, illicit=None, illicit_violent=None, self_harm=True, self_harm_instructions=False, self_harm_intent=True, sexual=False, sexual_minors=False, violence=False, violence_graphic=False, self-harm=True, sexual/minors=False, hate/threatening=False, violence/graphic=False, self-harm/intent=True, self-harm/instructions=False, harassment/threatening=False)
True
```

## There are good open-source alternatives

There are good open-source alternatives to the OpenAI Moderation API. For instance [Pleias/celadon](https://huggingface.co/Pleias/celadon) is fantastic little model that runs perfectly fine on CPU.

I did some repacking of the model to make it easier to use:

```python
from transformers import AutoModelForSequenceClassification

AutoModelForSequenceClassification.from_pretrained("tcapelle/celadon", trust_remote_code=True)
```
> I packed the model code so you can use it directly with `AutoModelForSequenceClassification`.

## What about Bluesky?

There was a bunch of toxicity related to AI in the recent weeks, related to some users uploading a dataset containing Blueky posts, directly gathered from the Bluesky API (it is an open firehose 🤣).

Many comments were extremely toxic and some users were even banned. As I said before, bluesky has a nice API, so we can programatically retrieve the comments and flag the toxic ones.

## Code

> Full script [here](https://gist.github.com/tcapelle/00a348192b50ad91205f332799b680fa)

1. Connect to the API using your credentials
2. Search for a user or post with toxic replies
3. Iterate over the replies and flag the toxic ones
4. Block the user that made the toxic replies

That's it! Next time you see some toxic content, you know what to do.