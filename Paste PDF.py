# coding=utf8
import sublime_plugin, sublime, re

# to transfer cleaned data to sublime text
def clean_paste(data):

    #Standard stuff like apostrophes 
    data = data.replace(u'\"', '&rdquo;')
    data = data.replace(u'”', '&rdquo;')
    data = data.replace(u'“', '&ldquo;')
    data = data.replace(u'\'', '&rsquo;')
    data = data.replace(u'’', "&rsquo;")
    data = data.replace(u'‘', "&lsquo;")
    data = data.replace(u'†', "&#8224;")
    data = data.replace(u'& ', "&amp; ")
    data = data.replace(u'–', '-')
    data = data.replace(u'–', '-')
    data = data.replace(u'+', u'&plus;')
    data = data.replace(u'°', u'&deg;')

    # Accents and weird characters 
    data = data.replace(u' a ',  u'')
    data = data.replace(u' a',  u'')
    data = data.replace(u'd',  u'd')
    data = data.replace(u'n',  u'n')
    data = data.replace(u'',  u'P')
    data = data.replace(u'',  u'e')
    data = data.replace(u'',  u'o')
    data = data.replace(u'',  u's')
    data = data.replace(u'',  u'g')
    data = data.replace(u'',  u'g')
    data = data.replace(u'',  u'a')
    data = data.replace(u'',  u'O')
    data = data.replace(u'',  u'a')
    data = data.replace(u'',  u'n')
    data = data.replace(u'',  u'c')
    data = data.replace(u'',  u'C')
    data = data.replace(u'',  u'k')
    data = data.replace(u'',  u'g')
    data = data.replace(u'',  u'g')
    data = data.replace(u'',  u'y')
    data = data.replace(u'',  u'y')
    data = data.replace(u' yag',  u'')  
    data = data.replace(u'', '')
    data = data.replace(u'', '')
    data = data.replace(u'', '')
    data = data.replace(u'', '')
    data = data.replace(u'', '')  

    data = data.replace(u'ä',  u'a')
    data = data.replace(u'à',  u'a')
    data = data.replace(u'â',  u'a')
    data = data.replace(u'aˆ', u'a')
    data = data.replace(u'̂a',  u'a')
    data = data.replace(u'à',  u'a')
    data = data.replace(u'â',  u'a')
    data = data.replace(u'âˆ', u'a')
    data = data.replace(u'à',  u'a')
    data = data.replace(u'̂â',  u'a')
    data = data.replace(u'̂ä',  u'a')
    data = data.replace(u'À',  u'A')
    data = data.replace(u'Â',  u'A')
    data = data.replace(u'À',  u'A')
    data = data.replace(u'Â',  u'A')

    data = data.replace(u'é',  u'e')
    data = data.replace(u'è',  u'e')
    data = data.replace(u'ê',  u'e')
    data = data.replace(u'ˆe', u'e')
    data = data.replace(u'́e',  u'e')
    data = data.replace(u'é',  u'e')
    data = data.replace(u'è',  u'e')
    data = data.replace(u'è',  u'e')
    data = data.replace(u'ê',  u'e')
    data = data.replace(u'ê',  u'e')
    data = data.replace(u'ë',  u'e')
    data = data.replace(u'é',  u'e')
    data = data.replace(u'É',  u'E')
    data = data.replace(u'È',  u'E')
    data = data.replace(u'Ê',  u'E')
    data = data.replace(u'É',  u'E')
    data = data.replace(u'È',  u'E')
    data = data.replace(u'Ê',  u'E')

    data = data.replace(u'î', u'i')
    data = data.replace(u'Î', u'I')
    data = data.replace(u'ï', u'i')
    data = data.replace(u'Ï', u'I')
    data = data.replace(u'î', u'i')
    data = data.replace(u'Î', u'I')
    data = data.replace(u'ï', u'i')
    data = data.replace(u'Ï', u'I')

    data = data.replace(u'ô',  u'o')
    data = data.replace(u'̂o',  u'o')
    data = data.replace(u'Ô',  u'O')
    data = data.replace(u'oˆ', u'o')
    data = data.replace(u'Ö',  u'O')
    data = data.replace(u'ô',  u'o')
    data = data.replace(u'̂ô',  u'o')
    data = data.replace(u'Ô',  u'O')
    data = data.replace(u'ô',  u'o')

    data = data.replace(u'ù', u'u')
    data = data.replace(u'Ù', u'U')
    data = data.replace(u'û', u'u')
    data = data.replace(u'Û', u'U')
    data = data.replace(u'ù', u'u')
    data = data.replace(u'Ù', u'U')
    data = data.replace(u'û', u'u')
    data = data.replace(u'Û', u'U')

    data = data.replace(u'œ', u'oe ')
    data = data.replace(u'Ç', u'C')
    data = data.replace(u'ç', u'ç')
    data = data.replace(u'Ç', u'C')
    data = data.replace(u'ç', u'c')

    # Spanish accents (Ome Gak)
    data = data.replace(u'á', u'a')
    data = data.replace(u'Á', u'A')
    data = data.replace(u'é', u'e')
    data = data.replace(u'É', u'E')
    data = data.replace(u'í', u'i')
    data = data.replace(u'Í', u'I')
    data = data.replace(u'ó', u'o')
    data = data.replace(u'Ó', u'O')
    data = data.replace(u'ú', u'u')
    data = data.replace(u'Ú', u'U')
    data = data.replace(u'ü', u'u')
    data = data.replace(u'Ü', u'U')
    data = data.replace(u'ñ', u'n')
    data = data.replace(u'Ñ', u'N')
    data = data.replace(u'á', u'a')
    data = data.replace(u'Á', u'A')
    data = data.replace(u'é', u'e')
    data = data.replace(u'É', u'E')
    data = data.replace(u'í', u'i')
    data = data.replace(u'Í', u'I')
    data = data.replace(u'ó', u'o')
    data = data.replace(u'Ó', u'O')
    data = data.replace(u'ú', u'u')
    data = data.replace(u'Ú', u'U')
    data = data.replace(u'ü', u'u')
    data = data.replace(u'Ü', u'U')
    data = data.replace(u'ñ', u'n')
    data = data.replace(u'Ñ', u'N')

    # Clean data
    data = re.sub(r't t', r'tt', data) 
    data = re.sub(r'(\d\d\d) (\dOn Sale)', r'\1', data) 
    data = re.sub(r'OrOanic|OrOni', r'Organic', data)    
    data = re.sub(r'Gluten-Free', r'Gluten-Free! ', data)
    data = re.sub(r'GF\nFREE\nGLUTEN', r'Gluten-Free! ', data)
    data = re.sub(r'(\d\d\d\d) (\d\d)', r'\1', data)
    data = re.sub(r'FOR', r'for', data)
    data = re.sub(r'DanDOrganic', r'Dan-D-Organic', data)
    data = re.sub(r'Per\nlb', r'Per lb', data)
    data = re.sub(r'(\$\d\d.\d\d)lb', r'\1\lb', data)
    data = re.sub(r'(\$\d.\d\d)lb', r'\1\lb', data)
    data = re.sub(r'(Per\n(\d+\w+))', r'Per \2', data)
    data = re.sub(r'\$(\d|\d.\d\d)\$', r'$\1', data)
    data = re.sub(r'\*SAME ITEM OF EQUAL OR\nLESSER VALUE.', r'Buy One Get one Free (Same item of equal or lesser value) ', data)
    data = re.sub(r'(LOW SODIUM| LOW SODIUM|LOW\nSODIUM| LOW\nSODIUM)', r'', data)
    data = re.sub(r'Instore', r'In-store', data)
    data = re.sub(r'(?<!, )(Same price as regular produce|Random Weight|All Size Packages|Previously Frozen|Frozen|While quantities|Selected|Tips Removed|Assorted|Made in|Grown in|Product of|Family Pack Savings Size|Canadian Grain Fed|Head Off|Bone in|\W\w+ Bone removed|\d Per Pack)', r', \1', data) 
    data = re.sub(r'(\d+|\d+\-\d+)\sLoads', r', \1 Loads', data)
    data = re.sub(r'(?<!Per)\n(?<!\,\s)(\d+\-\d+|\d+\–\d+|\d+\.\d+|\d+\.\d+\–\d+|\d+\–\d+\.\d+|\d+\.\d+\–\d+\.\d+|\d+\.\d+\-\d+|\d+\-\d+\.\d+|\d+\.\d+\-\d+\.\d+|\d+) Pack', r', \1 pack', data)
    data = re.sub(r'(?<!Per)\n(?<!\,\s)(\d+\-\d+|\d+\–\d+|\d+\.\d+|\d+\.\d+\–\d+|\d+\–\d+\.\d+|\d+\.\d+\–\d+\.\d+|\d+\.\d+\-\d+|\d+\-\d+\.\d+|\d+\.\d+\-\d+\.\d+|\d+)([a-zA-Z]+)', r', \1\2', data)

    # #deletes "you save"...
    data = re.sub(r'(You Save|Save up to) (\$|)( |)\d+( \d+|)(¢|)(ea.|\/\w+|)(\.|)', r'', data)

    #delete On Sale.
    data = re.sub(r'^(On Sale|O n Sale|O n S ale)\n(\$\d+)Each\n([\s\S]*)', r'\3 \2 Each', data)
    data = re.sub(r'(\d+)(\d\d)(?!\S+)\n(On Sale|O n Sale|O n S ale)\n(Each|E ach|Ea ch|Eac h)', r'$\1.\2 Each', data)
    data = re.sub(r'(\d+)(\d\d)(\s\d)(?!\S)\n(On Sale|O n Sale|O n S ale)\n(Each|E ach|Ea ch|Eac h)', r'$\1.\2 Each', data)
    data = re.sub(r'(\d+)(\d\d)(?!\S+)\n(On Sale|O n Sale|O n S ale)', r'$\1.\2', data)
    data = re.sub(r'(\d+) (\d\d)(?!\S+)\n(On Sale|O n Sale|O n S ale)', r'$\1.\2', data)
    data = re.sub(r'(On Sale|O n Sale|O n S ale)\s(\d+)(\d\d)', r'$\2.\3', data)    
    data = re.sub(r'(On Sale|O n Sale|O n S ale)\n(\d\d¢|\d\d ¢)', r'\2', data) 
    data = re.sub(r'(\d\d) ¢', r'\1¢', data)
    data = re.sub(r'On Sale|O n Sale|O n S ale', r'', data) 

    # $XX.XX Each
    data = re.sub(r'(\d+)(\d\d)\n', r'$\1.\2', data)
    data = re.sub(r'Per (\d+)( |)(\d+)( |)(\w)\n', r'Per \1\3\5 ', data)
    data = re.sub(r'(\d+)(\d\d)(?!\S+) (Per \d+\w+|Per \n\d+\w+|Per\n\d+\w+|Per lb)', r'$\1.\2 \3', data)
    data = re.sub(r'(\d+)(\d\d)(?!\S+)\n(Per \d+\w+|Per \n\d+\w+|Per\n\d+\w+|Per lb)', r'$\1.\2 \3', data)    
    data = re.sub(r'(\d+)(\d\d)(\s|\n|\n\n)(Each|E ach|Ea ch|Eac h)', r'$\1.\2 Each', data)
    data = re.sub(r'(\d\d%)[\n\s](OFF|off|of f)\n(At Till|at till|At Ti ll)', r'\1 Off at Till', data)
    data = re.sub(r'(\d\d%)(OFF|off|of f)\n(At Till|at till|At Ti ll)', r'\1 Off at Till', data)
    data = re.sub(r'(\d\d)¢(Each|Per)', r'\1¢ \2', data)
    data = re.sub(r'(\d\d) ¢(Each|Per)', r'\1¢ \2', data)
    data = re.sub(r'(\d+)\s(\d+)(\d\d)\n(for)', r'\1 for $\2.\3', data)
    data = re.sub(r'(\d+)\s(\d\d)¢\n(for)', r'\1 for \2¢', data)
    data = re.sub(r'(\d+)for', r'\1 for ', data)
    data = re.sub(r'(\d+)\$(\d+) For', r'\1 for $\2', data)
    data = re.sub(r'Regular\nRetail:', r'Regular Retail:', data)
    data = re.sub(r'(\$\d+).(\d\d)\n(Per \d+\w+|Per \n\d+\w+|Per\n\d+\w+|Per lb)', r'\1.\2 \3', data)

    #Price data $23/lb, per mg, etc. Puts KG after in price.
    data = re.sub(r'(\$\d+\.\d+\/kg|\$\d+\/kg)(\n| |)(\$\d+\.\d\d|\$\d+|\$\d|\d\d¢|\d+)(\n([\s\S]*)| |)(\n|)( |)(Per)(\n|)( |)(lb|l b)', r'\3\2 \8 lb, \1', data)
    data = re.sub(r'(\$\d+\.\d+\/lb|\$\d+\/lb)(\n| |)(\$\d+\.\d\d|\$\d+|\$\d|\d\d¢|\d+)(\n([\s\S]*)| |)(\n|)( |)(Per \d+\w+|Per \n\d+\w+|Per\n\d+\w+)', r'\3\2 \8, \1', data)
    data = re.sub(r'(\$\d+\.\d\d|\$\d+|\$\d|\d\d¢|\d+)(\n([\s\S]*)| |)(\n|)( |)(Per \d+\w+|Per \n\d+\w+|Per\n\d+\w+)([\s\S]*)(\n|)( |)(\$\d+\.\d+\/lb|\$\d+\/lb)', r'\7 \1 \6, \10', data)

    #Bogo!
    data = re.sub(r'([\s\S]*)(Regular Retail:)([\s\S]*)(\*SAME I TEM OF EQUAL OR\nLESSER VALUE.|\*SAME ITEM OF EQUAL OR\nLES SER VALUE.|\*SAME ITEM OF EQUA L OR\nLESSER VALUE.|\* SAME ITEM OF EQUAL OR\nLESSER VALUE.|\*SAME ITEM OF EQUAL OR\nL ESSER VALUE.|\*Same item of equal or lesser value|Buy One Get one Free \(Same item of equal or lesser value\))', r'\1 \4 \2 \3', data)
    data = re.sub(r'(\*SAME I TEM OF EQUAL OR\nLESSER VALUE.|\*SAME ITEM OF EQUAL OR\nLES SER VALUE.|\*SAME ITEM OF EQUA L OR\nLESSER VALUE.|\* SAME ITEM OF EQUAL OR\nLESSER VALUE.|\*SAME ITEM OF EQUAL OR\nL ESSER VALUE.|\*Same item of equal or lesser value|Buy One Get one Free \(Same item of equal or lesser value\))([\s\S]*)(Regular Retail:)([\s\S]*)', r'\2 Buy One Get one Free (Same item of equal or lesser value) \3 \4  ', data)
    
    #cleans up trailing duplicate numbers
    data = re.sub(r'(\d+% Off at Till)( |)(\d+)', r'\1', data)

    #moves price from the beginning of the line to the end
    data = re.sub(r'(^\$\d+.\d+\nPer lb\n)([\s\S]*)(\$\d+.\d+/kg)((EARN|GET)[\s\S]*)', r'\2\1, \3\4', data)
    data = re.sub(r'(^\$\d+.\d+\nPer lb\n)([\s\S]*)(\$\d+.\d+/kg)', r'\2\1, \3', data)
    data = re.sub(r'(^\$\d+.\d+\nPer \d+g\n)([\s\S]*)((EARN|GET|\d+ Bonus)[\s\S]*)', r'\2\1\3', data)
    data = re.sub(r'(^\$\d+.\d+\nPer \d+g\n)([\s\S]*)', r'\2\1', data)
    data = re.sub(r'(^\$\d+.\d+ Each\n)([\s\S]*)((EARN|GET|\d\d+ Bonus)[\s\S]*)', r'\2\1\3', data)
    data = re.sub(r'(^\$\d+.\d+ Each\n)([\s\S]*)((EARN|GET|\d+ Bonus)[\s\S]*)', r'\2\1\3', data)
    data = re.sub(r'(^\$\d+.\d+ Each\n)([\s\S]*)', r'\2\1', data)
    data = re.sub(r'(^ \d\d% Off at Till)([\s\S]*)((EARN|GET|\d+ Bonus)[\s\S]*)', r'\2\1\3', data)
    data = re.sub(r'(^ \d\d% Off at Till)([\s\S]*)', r'\2\1', data)
    data = re.sub(r'(\$\d+.\d\d)( Per lb| Per \d+g)\n([\S\s]+)(\$\d+.\d\d)(\/kg|\/lb)([\S\s]+|)', r'\3\1\2, \4\5\6', data)
    data = re.sub(r'(\$\d+.\d\d)( Per lb| Per \d+g)\n([\S\s]+)(\d+.\d\d)(\/kg|\/lb)([\S\s]+|)', r'\3\1\2, $\4\5\6', data)

    #moves price for case and single items together 
    data = re.sub(r'(\nSingle,)(\n\$\d+.\d\d|\n\$\d+| \d+¢|\n\d+¢| \d+ for \$\d+.\d\d| \d+ for \$\d+)(\n\$\d+.\d\d\nCase\nof \d+|\n\$\d+\nCase\nof \d+)', r'\3, Single, \2', data)
    data = re.sub(r'(Case of \d+,\n\$\d+\.\d\d)(\n\$\d+\.\d\d Each)', r'\2, \1', data)
    data = re.sub(r'(Case of \d+,\n\$\d+\.\d\d)(\n, \d for \$\d+\.\d\d)', r'\2, \1', data)
    data = re.sub(r'(Case of \d+,\n\$\d+\.\d\d)(\n, \d for \$\d+)', r'\2, \1', data)
    
    #Splits the price from the food name
    data = re.sub(r'(\d+ for \d\.\d\d, Case of \d+,\n\$\d+\.\d\d|\d+ for \d, Case of \d+,\n\$\d+\.\d\d|\d+ for \$\d\.\d\d, Case of \d+,\n\$\d+\.\d\d|\d+ for \$\d, Case of \d+,\n\$\d+\.\d\d|\$\d+\.\d\d Each, Case of \d+,\n\$\d+\.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \d+ for \d+¢|\$\d+\.\d\d\nCase\nof \d+, Single,  \d+¢|\$\d+\.\d\d\nCase\nof \d+, Single,  \d+ for \$\d+.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \$\d+.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \d\d¢|\d+ for \$\d+\.\d\d|\d+ for \$\d+|\d+ \$\d+.\d\d for|\$\d+\.\d\d Per \d+\w+|\$\d+ Per \d+\w+|\$\d Per \d+\w+|\d+for\$\d+|\d+\% Off|\$\d+ On Sale|\d+\nOn Sale|\d+\.\d\d\nOn Sale|\$\d+\n|\$\d+\.\d\d\n|\$\d+\.\d\d Each|\$\d+ Each|\d+¢|(\$\d+\.\d\d|\$\d+) Per lb, (\$\d+\.\d\d\/kg|\$\d+\/kg)|Buy One Get one Free \(Same item of equal or lesser value\) Regular Retail[\s\S]*)', r'";\r\t$Price = "\1', data)

    #reward miles
    data = re.sub(r'(\d+)\nreward miles\n(EARN|GET)', r', Earn \1 reward miles ', data) 
    data = re.sub(r'(\d+)reward miles\n(EARN|GET)', r', Earn \1 reward miles ', data) 
    data = re.sub(r'(\d+) Bonus\nMiles', r', Earn \1 bonus miles ', data) 
    data = re.sub(r'EACH', r'Each', data)
    data = re.sub(r'WHEN YOU\nBUY (\d+)', r'When you buy \1', data)
    data = re.sub(r'PER PACKAGE', r'Per Package', data)    
    data = re.sub(r'PER ', r'Per ', data)
    data = re.sub(r'(reward miles)\s(\d+)', r'\2 \1 ', data)
    data = re.sub(r'EARN|GET', r', Earn', data)

    # replace hr's with new lines
    data = data.replace('________________________________________', '\n')
   
    # clean new lines, remove trailing commas and spaces and add in food name
    data = data.replace('\n', ' ')
    data = data.replace('\n\s\n', '')
    data = re.sub(r'^', r'$FoodName = "', data)
    data = re.sub(r'$| $|,$|, $', r'";', data) 
    
    #  watch for multiple spaces
    data = re.sub(r'     ', r' ', data)
    data = re.sub(r'    ', r' ', data)
    data = re.sub(r'   ', r' ', data)
    data = re.sub(r'  ', r' ', data)

    # clean previously hyphenated words, spaces before commas, double commas
    data = re.sub(r'- ', r'', data)
    data = re.sub(r',,', r',', data)
    data = re.sub(r', ,', r',', data)
    data = re.sub(r' ,', r',', data)
    data = re.sub(r'\.,', r'.', data)
    data = re.sub(r' , "|, "|,"|" ', r'"', data)

   
    # Create reward text for the 4 boxes
    data = re.sub(r'(\d+)reward miles\n(GET|EARN)\nWhen you spend (\$\d\d) on any of these featured items', r'Earn \1 reward miles when you spend \3 on any of these featured items', data) 
    data = re.sub(r'(\$FoodName \=\")(, Earn \d\d reward miles When you spend \$\d\d on(| any of) these featured items(|.))(\"\;)', r'\2', data) 
    data = re.sub(r'(\$FoodName \=\")(, Earn \d\d reward miles When you buy any (\d\d|\d) of these featured items(|.))(\"\;)', r'\2', data) 
    data = re.sub(r'(\$FoodName =")(, Earn \d+ reward miles When you buy any \d of these featured items.)(";)', r'\2', data) 

    # Leftover stuff from the 2016 flyer design that's not caught previously
    data = re.sub(r'"ga | ga"', r'"', data)
    data = re.sub(r'SAVINGS FAMILY PACK BUY, Earn FREE1', r'', data)
    data = re.sub(r' BUY, Earn FREE1', r'', data)
    data = re.sub(r' PER KILOGRAM', r' Per Kilogram', data)
    data = re.sub(r' WHEN YOU BUY (\d+) PACKAGES', r' When you buy \1 packages', data)
    data = re.sub(r' WHEN YOU BUY', r' when you buy', data)
    data = re.sub(r' PER PACKAGE', r' Per Package', data)

    # In case you paste in a second time, this will allow you to do that.
    data = re.sub(r'\$Price = &rdquo;|\$Price =&rdquo;|&rdquo;;|\$FoodName = &rdquo;|\$FoodName =&rdquo;', r'', data)
    data = re.sub(r'(\t\s"|\t"|\s\s\s\s\s"|\s\s\s\s"|\s\s\s"|\s\s"|\s")', r'"', data)
    
    # X $X.XX for
    data = re.sub(r'(\$Price =")(\d+) (\$\d+\.\d\d|\$\d+) for([\S\s]+|)(";)', r'\1\2 for \3\4\5', data) 
    
    # Moves product names if they fall after the price
    data = re.sub(r'(\$FoodName =")([\S\s]+)(\d+ for \$\d+, Case of \d+, \$\d+\.\d+|\d+ for \d\.\d\d, Case of \d+,\n\$\d+\.\d\d|\d+ for \d, Case of \d+,\n\$\d+\.\d\d|\d+ for \$\d\.\d\d, Case of \d+,\n\$\d+\.\d\d|\d+ for \$\d, Case of \d+,\n\$\d+\.\d\d|\$\d+\.\d\d Each, Case of \d+,\n\$\d+\.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \d+ for \d+¢|\$\d+\.\d\d\nCase\nof \d+, Single,  \d+¢|\$\d+\.\d\d\nCase\nof \d+, Single,  \d+ for \$\d+.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \$\d+.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \d\d¢|\d+ for \$\d+\.\d\d|\d+ for \$\d+|\$\d+\.\d\d Per \d+\w+|\$\d+ Per \d+\w+|\$\d Per \d+\w+|\d+for\$\d+|\d+\% Off at Till|\$\d+ On Sale|\d+\nOn Sale|\d+\.\d\d\nOn Sale|\$\d+\n|\$\d+\.\d\d\n|\$\d+\.\d\d Each|\$\d+ Each|\$\d+\.\d+ Per \d+g|\d+¢ Per \d+g|\d+¢ Each|(\$\d+\.\d\d|\$\d+) Per lb, (\$\d+\.\d\d\/kg|\$\d+\/kg)|Buy One Get one Free \(Same item of equal or lesser value\) Regular Retail[\s\S]*) ([\S\s]+)(";)', r'\1\6, \2\3\7', data)
    data = re.sub(r' !', r'', data)
    data = re.sub(r'(\$FoodName =")([\S\s]+)(Gluten-Free)(";)', r'\1\3 \2\4', data)    

    # Remove anything that isn't caught
    data = re.sub(r'[^a-zA-z\n\t\r\d\s\ \&\;\,\.\¢\!\@\#\$\%\*\\\/\?\<\>\~\`\:\"\'\_\-\+\=\(\)\{\}\[\]]+', r'!!!!!!!!!!!!!!!', data)


# All done
    return data

# Paste PDF Function
class PastePdf(sublime_plugin.TextCommand):
    def run(self, edit):
        old_clipboard = sublime.get_clipboard()
        sublime.set_clipboard(clean_paste(old_clipboard))
        self.view.run_command('paste')