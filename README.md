# Quran-Tracker
Log and calculate quran memorizing progress.

# Usage
Log your memorized ayah in quran.csv. Separate memorized ayah with `,` for multiple section. example:
<pre>
no  ; surah         ; ayah ; memorized
2   ; Al-Baqarah    ; 286  ; 1-5, 255-257, 275-281, 284-286
</pre>

Run q.py. qt will read quran.csv and give show your memorizing progress. 

<pre>
% python q.py

memorized : 905 of 6236 (14.51%)
remainder : 5331 (85.49%)
</pre>

# Tips
Use lafdzi to find your memorized ayah quickly. type the ayah in quran latin transliteration. lafzi will give you the surah name and exact ayah position. 
http://lafzi.apps.cs.ipb.ac.id/web/

# Todo
* Memorized histogram
* Statistic in html format
