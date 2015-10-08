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


------------------------------------------
PART B
------------------------------------------
PART B2:
	TRIGRAM CONJ ADV ADP -2.9755173148
	TRIGRAM DET NOUN NUM -8.9700526163
	TRIGRAM NOUN PRT PRON -11.0854724592


PART B4:
	Night NOUN -13.8819025994
	Place VERB -15.4538814891
	prime ADJ -10.6948327183
	STOP STOP 0.0
	_RARE_ VERB -3.17732085089

PART B5:
	own trigram accuracy = Percent correct tags: 80.9865733774

PART B6:
	nltk accuracy = Percent correct tags: 90.0811069635


------------------------------------------
RUNTIMES
------------------------------------------
Part A time: 24.853025 sec
Part B time: 25.904883 sec


-----------------------------------------
OTHER NOTES
-----------------------------------------
This project is under git version control.
Two other branches house different versions of the algorithm. Their accuracy was never as high as the original implementation.

This project is also under a virtualenv. It houses all dependencies for the project.
To activate, type:  source bin/activate
(But on clic, you shouldn't need to because the machines have all these libraries installed)