#TITLE
Loi de Position and spelling in French: the use of diacritics as a way to indicate divergent pronunciation?


#PROJECT DESCRIPTION
In French, the letter <e> can be realized as [e] or [ɛ], among others. French also has variants of this letter that uses diactritics. The <é> variant denotes the pronunciation [e] and the <è> variant denotes the pronunciation [ɛ]. This project looks at whether these two variants with diacritics are used to indicate a pronunciation that goes against the common mid-vowel assignment phenomenon of Loi de Position in French.
The Loi de Position states that [e] should appear in open syllables and [ɛ] should appear in closed syllables. As a consequence, if <é> (denoting the pronunciation [e]) appears more often in an open syllable, this would suggest that this specific variant is used to indicate a pronunciation that goes against the Loi de Position. The same can be said if <è> (denoting the pronunciation [ɛ]) appears more often in a closed syllable.
In order to test this, we will look at the syllabic environment for each instance of <é> and <è> in a French orthographic corpus. As the corpus is orthographic, we will have to make rough estimates of syllabation based on spelling. To indicate a use of these letter that contradicts the Loi de Position, this is what we expect to find:
<é> in closed syllables:
	- <é> followed by 2+ consonants in a non-final environment
	- <é> followed by 1+ consonant in a final environment
<è> in open syllables:
	- <è> followed by 0 or 1 consonants in a non-final environment
	- <è> followed by 0 consonants in a final environment

#HOW TO RUN THE CODE
I am starting with the French Sequoia corpus from https://github.com/surfacesyntacticud/SUD_French-Sequoia
My first code is aigugetdata.py and gravegetdata.py that extracts all lines that contain respectively <é> and <è>. It outputs two text files "aigudata.txt" and "gravedata.txt" containing all the lines with <é> and all the lines with <è>.
My second code is "aigumakelist.py" and "gravemakelist.py" (split in two to deal with <é> and <è>). It lists words containing <é> and <è> in "aigudata.txt" and "gravedata.txt". It also counts the number of consonants after the <é> or <è>, as well as whether the syllable is final (F) or non-final (N). It outputs a table of all the words containing <é> or <è> in the first column, the number of consonants in the second, and final/non-final in the third. The output is saved in the files "aigulist.txt" or "gravelist.txt". 
Finally, my third code is "aigufrequency.py" and "gravefrequency.py" (split in two again). It deletes repeated lines, as we don't want the frequency of one word in the language to influence our results, and then counts how many of each unique combination there is (number of consonants and final/non final), for both <é> and <è>. This outputs "aigufrequency.txt" and "gravefrequency.txt" which includes the number of instances of each combination for both <é> and <è>.
We have a final output that is two text files that tell us how frequent <é> and <è> are in each possible context. Then, we can analyze it linguistically as follows.

#METHODS, RESULTS, CONCLUSIONS
We must first categorize our orthographic contexts for what we can assume the syllabic structure to be:
- 0 consonants following the vowel is always an open syllable.
- 1 consonant following the vowel in a final syllable is always a closed syllable
- 1 consonant following the vowel in an non-final syllable is always an open syllable (French has a strong preference for onsets rather than codas).
- 2+ consonants following the vowel are considered to be always a closed syllable here for simplicity.

Again, the Loi de Position predicts [e] in open syllables and [ɛ] in closed syllables, so finding an <é> in a closed syllable and a <è> in an open syllable would indicate a pronunciation that goes against the loi de position.

The results are as follows:

For <è>
1 consonant(s) in N context: 170 instances
1 consonant(s) in F context: 14 instances
2 consonant(s) in N context: 17 instances

For <é>
0 consonant(s) in F context: 404 instances
0 consonant(s) in N context: 386 instances
1 consonant(s) in N context: 1045 instances
1 consonant(s) in F context: 162 instances
2 consonant(s) in N context: 110 instances
3 consonant(s) in N context: 1 instances


Starting with <è>, we find that 84.5% of <è> are in a 1 consonant non-final context, which is a context where the Loi de Position predicts [e]. This tends to support our hypothesis that the diacritic is present to indicate a pronunciation that does not follow the Loi de Position. The remaining 15.5% do not support this hypothesis.

As for <é>, we find that 49.5% of <é> are also in a 1 consonant non-final context, which does not support out hypothesis. In addition, 18.3% and 19.1% of <é> are in contexts that also do not support our hypothesis, which overall suggest our hypothesis is not supported as around 87% of cases do not.

These results are limited by the choice of focusing on spelling. Spelling in French is particularly distant from pronunciation, and as such our results may not be a very accurate representation of what we were trying to find. In addition, the context as defined here lacks nuance. Many additional factors tend to affect syllable structure in French, such as the type of consonant, the type of word, its etymology, etc.

Nonetheless, this shows that computational tools can constitute a way to answer this question, especially if applied to large corpora. Ideally, repeating the process with a corpus that has an IPA transcription would be the best way to move forward with this topic.
