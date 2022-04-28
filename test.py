from fuzzy_extractor import FuzzyExtractor
extractor = FuzzyExtractor(16, 8)
key, helper = extractor.generate('AABBCCDDEEFFGGHH')
r_key = extractor.reproduce('AABBCCDDEEFFGGHH', helper)  # r_key should equal key
r_key = extractor.reproduce('AABBCCDDEEFFGGHI', helper)  # r_key will probably still equal key!
r_key = extractor.reproduce('AAAAAAAAAAAAAAAA', helper)  # r_key is no longer likely to equal key