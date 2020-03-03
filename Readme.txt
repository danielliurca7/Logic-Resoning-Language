    Parsarea am facut-o in ANTLR4(ca sa nu fac CPL degeaba). Am modificat umpic gramatica pentru ca cea din enunt era ambigua.
        - comentariile sunt doar cu cu #
        - definirea unei reguli se face cu ':-' ca in prolog, in loc de ':'

    La reprezentare e basically copy paste din laborator doar ca am mai pus cf unde trebuie.

    Pentru evaluarea functiilor iau valoarea fiecaruia dintre argumente si aplic functia cu numele corespunzator.

    La algoritmul de backward chaining am trei cazuri importante:
        - daca teorema contine doar constante ca termeni, atunci caut in baza de cunostinte un fapt care unifica(care este defapt egal) cu teorema
        - cautam in baza de cunostinte fapte care unifica cu teorema si retinem substitutiile obtinute in urma unificarii intr-o lista de substitutii
        - cautam in baza de cunostinte reguli ale caror concluzii unifica cu teorema si retinem substitutiile obtinute in urma unificarii intr-o lista de substitutii
            - daca gasim o regula valida, incercam sa demonstram premizele
            - pentru fiecare premisa substituim substitutiile obtinute anterior si facem un join intre rezultatele anterioare si substitutiile noi
            - din toate rezultatele obtinute dupa satisfacerea tuturor premizelor alegem doar pe cele care apar in concluzie
            - ca optimizare m-am gandit ca daca extingem o regula complet(avem in substitutie toate variabilele concluziei) sa o scoatem din baza de cunostinta si sa punem in loc fapte
            - la final combin probabilitatile pentru substitutii identice