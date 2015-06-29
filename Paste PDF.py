# coding=utf8
import sublime_plugin, sublime, re

# to transfer cleaned data to sublime text
def clean_paste(data):

# test with https://regex101.com/r/wY8sF8/1#python

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

    # Accents and weird characters 

    data = data.replace(u'd',  u'd')
    data = data.replace(u'n',  u'n')
    data = data.replace(u'',  u'P')
    data = data.replace(u'',  u'e')
    data = data.replace(u'',  u'o')
    data = data.replace(u'',  u's')
    data = data.replace(u'',  u'g')
    data = data.replace(u'',  u'a')

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
    data = re.sub(r'(\d\d\d) (\dOn Sale)', r'\1', data)   
    data = re.sub(r'(\d\d\d\d) (\d\d)', r'\1', data)
    data = re.sub(r'FOR', r'for', data)
    data = re.sub(r'DanDOrganic', r'Dan-D-Organic', data)
    data = re.sub(r'Per\nlb', r'Per lb', data)
    data = re.sub(r'(Per\n(\d+\w+))', r'Per \2', data)
    data = re.sub(r'\$(\d|\d.\d\d)\$', r'$\1', data)
    data = re.sub(r'([\s\S]*)(Gluten-Free)([\s\S]*)', r'\2! \1\3', data)
    data = re.sub(r'\*SAME ITEM OF EQUAL OR\nLESSER VALUE.', r'Buy One Get one Free (Same item of equal or lesser value) ', data)
    data = re.sub(r'(LOW SODIUM| LOW SODIUM|LOW\nSODIUM| LOW\nSODIUM)', r'', data)
    data = re.sub(r'Instore', r'In-store', data)
    data = re.sub(r'(?<!, )(Random Weight|All Size Packages|Previously Frozen|Frozen|While quantities|Selected|Tips Removed|Assorted|Made in|Grown in|Product of|Family Pack Savings Size|Canadian Grain Fed|Head Off|Bone in|\W\w+ Bone removed|\d Per Pack)', r', \1', data) 
    data = re.sub(r'(\d+|\d+\-\d+)\sLoads', r', \1 Loads', data)
    data = re.sub(r'(?<!Per)\n(?<!\,\s)(\d+\-\d+|\d+\–\d+|\d+\.\d+|\d+\.\d+\–\d+|\d+\–\d+\.\d+|\d+\.\d+\–\d+\.\d+|\d+\.\d+\-\d+|\d+\-\d+\.\d+|\d+\.\d+\-\d+\.\d+|\d+) Pack', r', \1 pack', data)
    data = re.sub(r'(?<!Per)\n(?<!\,\s)(\d+\-\d+|\d+\–\d+|\d+\.\d+|\d+\.\d+\–\d+|\d+\–\d+\.\d+|\d+\.\d+\–\d+\.\d+|\d+\.\d+\-\d+|\d+\-\d+\.\d+|\d+\.\d+\-\d+\.\d+|\d+)([a-zA-Z]+)', r', \1\2', data)

    # #deletes "you save"...
    data = re.sub(r'(You Save \d+¢/\d+\w+\n|You Save \$ [\d|\d \d\d]+ea.|You Save \$ [\d|\d \d\d]+lb|You Save \$\d+ea.|You Save \$\d+ \d+ea.|You Save \$ \d+\n|You Save \$\d+|You S ave \$[ |]\d+|Save up to \$\d+ea.|Save up to \$\d+|You Save \d+¢ea.)', r'', data)

    #delete On Sale.
    data = re.sub(r'^(On Sale|O n Sale|O n S ale)\n(\$\d+)Each\n([\s\S]*)', r'\3 \2 Each', data)
    data = re.sub(r'(\d+)(\d\d)(?!\S+)\n(On Sale|O n Sale|O n S ale)\n(Each|E ach|Ea ch|Eac h)', r'$\1.\2 Each', data)
    data = re.sub(r'(\d+)(\d\d)(\s\d)(?!\S)\n(On Sale|O n Sale|O n S ale)\n(Each|E ach|Ea ch|Eac h)', r'$\1.\2 Each', data)
    data = re.sub(r'(\d+)(\d\d)(?!\S+)\n(On Sale|O n Sale|O n S ale)', r'$\1.\2', data)
    data = re.sub(r'(On Sale|O n Sale|O n S ale)\s(\d+)(\d\d)', r'$\2.\3', data)    
    data = re.sub(r'(On Sale|O n Sale|O n S ale)\n(\d\d¢|\d\d ¢)', r'\2', data) 
    data = re.sub(r'On Sale|O n Sale|O n S ale', r'', data) 


    #Price data $23/lb, per mg, etc. Puts KG after in price.
    data = re.sub(r'(\$\d+\.\d+\/kg|\$\d+\/kg)\n(\$\d+\.\d\d|\$\d+|\$\d|\d+|\d\d¢)(\n([\s\S]*)|)(\n|)( |)(Per)(\n|)( |)(lb|l b)', r'\2 \7 lb, \1', data)
    data = re.sub(r'(\$\d+\.\d+\/lb|\$\d+\/lb)\n(\$\d+\.\d\d|\$\d+|\$\d|\d+|\d\d¢)(\n([\s\S]*)|)\n(Per \d+\w+|Per \n\d+\w+|Per\n\d+\w+)', r'\2 \5, \1', data)

    # $XX.XX Each
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
    data = re.sub(r'Regular\nRetail:', r'Regular Retail:', data)

    #Bogo!
    data = re.sub(r'([\s\S]*)(Regular Retail:)([\s\S]*)(Buy One Get one Free \(Same item of equal or lesser value\))', r'\1 \4 \2 \3', data)
    data = re.sub(r'(Buy One Get one Free \(Same item of equal or lesser value\))([\s\S]*)(Regular Retail:)([\s\S]*)', r'\2 \1 \3 \4  ', data)

    #cleans up trailing duplicate numbers
    data = re.sub(r'(\d+% Off at Till)( |)(\d+)', r'\1', data)


    #moves price from the beginning of the line to the end
    data = re.sub(r'(^\$\d+.\d+\nPer lb\n)([\s\S]*)(\$\d+.\d+/kg)(EARN[\s\S]*)', r'\2\1, \3\4', data)
    data = re.sub(r'(^\$\d+.\d+\nPer lb\n)([\s\S]*)(\$\d+.\d+/kg)', r'\2\1, \3', data)
    data = re.sub(r'(^\$\d+.\d+\nPer \d+g\n)([\s\S]*)(EARN[\s\S]*)', r'\2\1\3', data)
    data = re.sub(r'(^\$\d+.\d+\nPer \d+g\n)([\s\S]*)', r'\2\1', data)
    data = re.sub(r'(^\$\d+.\d+ Each\n)([\s\S]*)(EARN[\s\S]*)', r'\2\1\3', data)
    data = re.sub(r'(^\$\d+.\d+ Each\n)([\s\S]*)', r'\2\1', data)
 
    #moves price for case and single items together 
    data = re.sub(r'(\nSingle,)(\n\$\d+.\d\d|\n\$\d+| \d+¢|\n\d+¢| \d+ for \$\d+.\d\d| \d+ for \$\d+)(\n\$\d+.\d\d\nCase\nof \d+|\n\$\d+\nCase\nof \d+)', r'\3, Single, \2', data)

    #Splits the price from the food name
    data = re.sub(r'(\$\d+\.\d\d\nCase\nof \d+, Single,  \d+ for \$\d+.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \$\d+.\d\d|\$\d+\.\d\d\nCase\nof \d+, Single,  \d\d¢|\d+ for \$\d+\.\d\d|\d+ for \$\d+|\$\d+\.\d\d Per \d+\w+|\$\d+ Per \d+\w+|\$\d Per \d+\w+|\d+for\$\d+|\d+\% Off|\$\d+ On Sale|\d+\nOn Sale|\d+\.\d\d\nOn Sale|\$\d+\n|\$\d+\.\d\d\n|\$\d+\.\d\d Each|\$\d+ Each|\d+¢|(\$\d+\.\d\d|\$\d+) Per lb, (\$\d+\.\d\d\/kg|\$\d+\/kg)|Buy One Get one Free \(Same item of equal or lesser value\) Regular Retail[\s\S]*)', r'";\r\t$Price = "\1', data)
    
    #reward miles
    data = re.sub(r'(\d+)\nreward miles\nEARN', r', Earn \1 reward miles ', data) 
    data = re.sub(r'(\d+)reward miles\nEARN', r', Earn \1 reward miles ', data) 
    data = re.sub(r'(reward miles)\s(\d+)', r'\2 \1 ', data)
    data = re.sub(r'EARN', r', Earn', data)

    # replace hr's with new lines
    data = data.replace('________________________________________', '\n')
   
    # clean new lines, remove trailing commas and spaces and add in food name
    data = data.replace('\n', ' ')
    data = data.replace('\n\s\n', '')
    data = re.sub(r'^', r'$FoodName = "', data)
    data = re.sub(r'$| $|,$|, $', r'";', data) 
    
    #  watch for multiple spaces
    data = re.sub(r'     ', r' ', data)   # 5 spaces
    data = re.sub(r'    ', r' ', data)   # 4 spaces
    data = re.sub(r'   ', r' ', data)   # 3 spaces
    data = re.sub(r'  ', r' ', data)   # 2 spaces

    # clean previously hyphenated words, spaces before commas, double commas
    data = re.sub(r'- ', r'', data)
    data = re.sub(r',,', r',', data)
    data = re.sub(r', ,', r',', data)
    data = re.sub(r' ,', r',', data)
    data = re.sub(r'\.,', r'.', data)
    data = re.sub(r' , "|, "|,"|" ', r'"', data)

    # In case you paste in a second time, this will allow you to do that.
    data = re.sub(r'\$Price = &rdquo;|\$Price =&rdquo;|&rdquo;;|\$FoodName = &rdquo;|\$FoodName =&rdquo;', r'', data)
    data = re.sub(r'(\t\s"|\t"|\s\s\s\s\s"|\s\s\s\s"|\s\s\s"|\s\s"|\s")', r'"', data)

# All done
    return data


# to transfer cleaned data and put in double quotes with a footnote prepared in Pandoc notation.
def pandoc_clean_paste(data):
    paste_block = clean_paste(data)
    data = "\"" + paste_block + "\"^[]"
    return data

# Paste PDF Function
class PastePdf(sublime_plugin.TextCommand):
    def run(self, edit):
        old_clipboard = sublime.get_clipboard()
        sublime.set_clipboard(clean_paste(old_clipboard))
        self.view.run_command('paste')


class PastePdfPandoc(sublime_plugin.TextCommand):
    def run(self, edit):
        old_clipboard = sublime.get_clipboard()
        sublime.set_clipboard(pandoc_clean_paste(old_clipboard))
        self.view.run_command('paste')
        sublime.set_clipboard(old_clipboard)
        (row, col) = self.view.rowcol(self.view.sel()[0].begin())
        target = self.view.text_point(row, col-1)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
        self.view.show(target)
