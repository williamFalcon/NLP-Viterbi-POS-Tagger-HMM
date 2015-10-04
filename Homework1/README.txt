=====================================
NAME: WILLIAM FALCON
UNI: WAF2107
=====================================

PART A1:
	UNIGRAM 	natural 			-13.766408817
	BIGRAM 		natural that 		-4.05889368905
	TRIGRAM 	natural that he 	-1.58496250072

PART A2:
	A2.uni.txt 	perplexity: 	1052.4865859
	A2.bi.txt 	perplexity: 	53.8984761198
	A3.tri.txt 	perplexity: 	5.7106793082

PART A3:
	The perplexity is 12.5516094886

PART A4:
	Yes. The model with just unigrams is not conditioned on any contexts. As a result the perplexity is extremely hight.
	The bigrams add significant value by conditioning on one word. The trigrams have very low perplexity, but I would imagine is sparce since there
	are significantly less trigrams than there are bigrams and it may miss some input phrases.
	The interpolated model seems to combine the best of both worlds and its score reflects this. I expected that it wouldn't be nearly as low as the solo trigrams,
	but not as high as the bigrams. This number seems a bit more solid in accounting for sparcity and taking into consideration all prior ngrams (uni, bi, tri).

PART A5:
	Sample1 perplexity: 1.54761961801
	Sample2 perplexity: 7.31320091815

	I would argue the one with the lowest score means it is from the brown corpus. However, I would have expected a score much higher for Sample2 (seeing how it is from another
	language). However, I imagine the many -1000 sentences would have this effect.

