# Quran-Tracker
Log and calculate your quran memorizing progress.

# Usage
Log your memorized ayah in quran.csv. Use `{start-end}, {start-end} format` to log multiple section. For instance, you have memorized al-baqarah ayah 1 to 5, 255 to 257, 275 to 281. Write those section like this:  
<pre>
no  ; surah         ; ayah ; memorized
2   ; Al-Baqarah    ; 286  ; 1-5, 255-257, 275-281
</pre>

Run `q.py`. Quran tracker will read quran.csv and show your memorizing progress. 

<pre>
% python q.py

memorized : 905 of 6236 (14.51%)
remainder : 5331 (85.49%)
</pre>

# Tips
Use lafdzi to find your memorized ayah quickly. type the ayah in quran latin transliteration. lafzi will give you the surah name and exact ayah position. 
http://lafzi.apps.cs.ipb.ac.id/web/

# How to memorize (ID audio format) 
https://www.youtube.com/watch?v=Yh73VTASvNw

# Todo
* Memorized histogram
* Statistic in html format
