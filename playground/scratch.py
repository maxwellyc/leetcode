import collections
def minWindow(S,T):
    tind = collections.defaultdict(list)
    for ind,t in enumerate(T):
        tind[t].append(ind)

    if len(T) == 1: return T if T in S else ""
    pool = collections.defaultdict(int)
    ans = [] # store start and end index (both inclusive)
    print(len(T))
    debug = []
    debu = []
    for i in range(len(S)):
        c = S[i]
        if i == 5119: print (pool)
        if c in tind:
            j_list = []
            for j in tind[c]:
                if j in pool:
                    if j + 1 == len(T):
                        print (pool[j],i, i-pool[j]+1)
                        if j+1 in pool: pool.pop(j+1)
                        if not ans or (ans[1]-ans[0] > i - pool[j]+1) :
                            ans = [pool[j],i]
                    j_list.append(j)
            if i == 5119:
                print ('jlist', j_list)
            for j in j_list[::-1]:
                if  i == 5119 and pool[j] == 4826: print (j)
                if pool[j] == 4826:
                    debug.append(S[i])
                    debu.append(i)
                pool[j+1] = pool.pop(j)

        if c == T[0]:
            pool[1] = i
        if debu and debu[-1] == 5119:
            print (debu)
    print ('i'+''.join(debug))
    print (debu)
    print (S[5119])
    print (S[5116])
    for k in range(len(debu)-1):
        if debu[k] >= debu[k+1]:
            print(debu[k],debu[k+1])

    #print (S[ans[0]:ans[1]+1] if ans else "")
    if not ans: return ""
    return S[ans[0]:ans[1]+1]

def minWindow2(S, T):
    n = len(S)
    m = len(T)

    dic = dict()
    for i, s in enumerate(T):
        dic.setdefault(s, []).append(i)

    dp = [-1 for i in range(m)]

    count = n+1
    start = -1

    for index, c in enumerate(S):
        if c in dic:
            for i in dic[c][::-1]:
                if i == 0:
                    dp[i] = index
                else:
                    dp[i] = dp[i-1]
                if i == m-1 and dp[i] >= 0 and index - dp[i]+1 < count:
                    count = index - dp[i] + 1
                    start = dp[i]
    if dp[-1] < 0:
        return ""
    print (start,start+count)
    return S[start:start+count]

S = "jbsgekcxgwzachbcahyrdvycugbfnlvhbmdploguqigvlmjkznliugdqmtiqurlguofvgntaazeoamgqjikhwiuuvdosqkxmxpbuticodcxybweydapqikefbcqdlkiuebdfxckojqzcjsytceouwtkzjyjqwwfvroqnnaqetrpjjfqpssjnkmuxuhxchjrpzlnfnyfbepdjzpyphzjdovoyynsjrovtqvpzkgsytgzlgkrctgrfarehhhmyowcccoonhouavksclacghhhwwpcikqqbzflscsyypyzzzndfmxuajwrokdbcjddudwxzqtqvomtpejewfkjnujabojkeblgxjkpjcoabgkyigqewlvgsdmqtgylmknojaajkupndjgypgowdkhyptezzrgcscaydwqyvjzhozoqmkhhxvgfhwxzvrhwlpadejyjfssfagfnbgwztmgglcwpkovssutzozkfxfxgeyqdgechviomqiygccxfydywpjxzskrrmyrdxxtthsirsdoxzbcwferhhuszgrzfoqiatlnzkahhnqdghmnatmiuhthmfwzaalpfnntyuqgflkhlqxuhnazekmdysmttomrofuczrqtrmnlvvsjhrxczslnbjjeycctluxewbldtyeddfutapqcvivmocskjzhaqsvodrnehxlnzqdjrflaphxgeffldghutmxdesrrjfjvuixjjylzmtowipyaoqylbmnqzsxhjhtpmmrommmfqzbfrdrzidjacvupujpkzblnleggmkhhjgfhonyyuvbfyhhyqafogbvgulvfphmedaroesvjwfofstjfnomihiqmfrwycwybwwwoozcwbdyyfbufnzvscuvvonxlezxktunteuzbrukpyjfzljlwrbaqocpwkukgynizjrtvqigpfbrihfvygtotcuhnpwubznvzjxheiwwbmnoivokxvfbzjvjzqzsaxgfreyrfbsqtfwtjzyfurtvhmnqaeurfwvzbpxhbzxzyjojwxqbsrsvultfnyspgjmtvprkdfajgcnsrnfiygzqzrospzpocrrlfvquowbosdufcznhqjntczesgsugmcjshevfbrghkgqpfkwkrkohwxeqluigswkgzokvmmovxwiitjntdtpkzvwztajtaiuommghpvrxoetqthaikjqviqxajbgnhqvswcyadbxbdpvmhyiibxeotjtbsycsuiutxoyixkbbyxcqvpxwujfzvclbpnibukzkylgudtumekozxvsytlvpyvsbjzuyrkdypzallwiiavatvzdeulnaegtviknuqjnsqfczfwtxaojnxgpjtucefkvfzzouxvrchtlxxcxkfkfqjqnrmenpizdjiqxenjomycnrpikwmmwvoboctukncxaxolngzlyjmojppgbsplqnmzhwbjmuiculgsxreauxungfuafpqyefymmotzhwlhqmgzbvxgrrxkfndycmzdjdknzrduoiqavgemfvmvpkpxhbzdskljxemmlykckkncuymrubbikkwkzmwzzmkoegrzdiluwwdlywkxuulsjxboiuzutzfgdkauvfsafspcxvhholecbxglqvmefaujtyxgoajfcblwoxdugjuguzideviaduoxmyevjqfsxhaombkimmfhvhlfxygmnbkuvttjyuecqkmiptiokrscnysvhsypkoamertftkfzcludcchxdqaaxlmjnpyuwcolpjcizassuzmptagxwzqgvbhytfxwgkcrsvpdcmugyntuuwotuevkydawypsqboyoquhgaqtzotedvasxjnhhmrerwcbktaczoavtdlcoctxpgeijaromhfxhgwegumgpnyohxubutftutfltxglpnvpredranlbfnwigpxauiqfbmwnytqodbujplmxfmntncmkmupycjvfrvcuncovjpcferdpbeerdvnhxlvttaowotckwzlglbltlxdyhdsjceyeuxmpubnfyaskjupcwrqqusjaqmkfhlwyesonsiwskofwzdjldxmpjocxmsknswomqrdoaaqyszdwmgolaawckvdbjjfiledjkgvwanapwwppivdwhhuzcdegbhdpumuhzkazzrixzjddwmlvgogswalqecdaostjctvmacmzclrtoadqzdidcqadpevgpcjljsmwnlqbwvmsqwzkjvkbucqfayaijgelrbsemjettxucnlgmwpwdxgcjiduwsborrvzlxqayvnttwuwzekvmxnnznhdqwleawdogllababjckbruztqkvrbxrmlflezehxuezodvqzsimmhcndvedbkiesnezphgjyrufwmfsjslhoguhjgfvdnxanxrunyvvqzeihadqwgqyaajwidxfigkubjuhzjyvgvupfpylfhieralqjnwbcqdsthmyhuxjgqpniahwezavdolvosblmevbvtlijlaykvtiafpvssklmuolnnrrogsptefcgalmcpmubcqjkgkbfoxhchqkqmeahqpaepbbpnpyvzsmyygpaxljsguwiuaiwsscsefbvsvynzkeztlcgncskshqebnwccmxhmotrfttipvxzgnyzamrtjejmluqhuawtcchaumaxqoadttzwtutyyozkpvkrlusdeiioyivdkvbrfypdpuwqnwuaedcnegparkmenoqrevosnwmktcssvkrzkiulvagaqxkcuusohgwcbqmybjwufgghuostgronsrnuhdxlfctrqnpcgnmswjmfkbwtcefdcmdjfaarawupgjduectaefpicuxhfvutohxlahyxfohgfrwxeafzjisueltaywroyvndswlqdoomyhkiymxodkkkisbeuhxmusytytbliwvigmcapqrwxubiogvfthbapljhjhhgthiluetsmdcykgtfbqkgfetfggntxrttnedyptjlyrtehncwjndeluucnvhfshupyyonhetbfslblynsetlwhgdycxzfoczxubkzbfouocvnlmzbbtpjkkxzewicpqojiyafcctbtgzbptpnlpmluwhzvonpeozlakomkxizxpaygrrlwmmcqjlsxswpzqagrolsraalsgwfwqbssmcmokspjdylrsewllxskkajauxmozhsbuoyihynrvkkwnawkgeclcdzplxmqalzvvzjymvglkdpxaftpgkhvthsnmrmzwidiwrnohwekmomisokbmtqyfgvdvikdxavqrhxwaukoaufpyjkrqgdmgdbhaqwdakykzwqenenzglnrndihvauqzqgxkzaqcldlwhsexuczhwmswrgabwcmqbhkbzchfghvlpmfhxatunbneaxabgvlbzghqfiivyzzydbppjhtykjovgacgtooskatdzofozdwfrvvzwnwxxrnlxhctmjjynmlfdqdpdaskzkypndamthectfmiajvolpgimsnjqqxjuveadoagrqaujqxbhbhkxkbeilhphlvqucnqqnkfhjchjewwgoxuxziluupktzdberdhfzhzunotnxounrwcwgiotiknscejhmsqfazhmoiajgbhpdlpcvqnrmpjshtmamlpezyxouzfheonuiwfjytjpkukjwtbivnicimhykhvvgjuxmocjdqrhtsumwtwpdxtwczpozyzaspdtzgaphxokvbipzjwyxlxkgrzcgykiklvlvhxaccqkjitjoboiihucvqjjbubkeenaoorrcscciyndajtwugvktifzjprtajtogetrnxvqzelutigumcxmiubkyejprwmywalzyvifbgekxdmbjzohjttkcgpgogreypnrsmzdkoaaelqoycfkagcsqrbfbayegzwqqicrdhraktneyjqqqgdikyfrzdicwoiqwlbfgleqawcnfgbgbzkwsjvtgvwyqmngivjsfafwztwdgyydsbnzozhusgexpxnhxnocciyjznsuzgujebwfibviztcxvkwzaxlukvhoiobeobpixywkzgccjxorzjrrelblxudlnmffmhcljjfpcyehhzjltlozifcpyerovgaxhtzadrndchxlaowtntjvxmxgxkfwwylnjtbispqottrhflgezdesfsascmkpnubzgpvwytecuymjzkhftjsschaseosuttthnbqtjvewrumxlsqphdzekpsjkwsctwenuwlbvttlyjcckqibaefylnqmxjxcumswmgxgpxpvsmvlpbkphsalvhucfwuwgfvnvypqdztusportfhbjxmgohizsmtwpvtnkdjmjvifdehqnbnjwkcuvgmetlzonumnhudkndltvglpetcqkhuxxpfiywdndqdwebryopuwyuskwqccvhergzbpxfosmpldfvtgzbqvyfaixvkmitfiieqvmstxrvsnawmreworucntyhpnclopxzhvrwxqamgfqekwphdmqzmrgpuzcpxrqzlvssqtpokxflhgbgyyvrnqxgyyxnaxonaxuqkdzrykngpwcrhyeaimmjosfdpbjxclvofbieagpbkivosijbfshkjwlfbxqrkrxbtiisjumjyrgygrwovgqmjnswzydenofzuhhwszdajeiquosdualsttmvulgxkxjwhiqyiycslgubaijdymllperwgezqrdwfddwpjnanatlrzazmxhzdujqzupbefavuienylsxlzxhsyfzjuizzhbrwrubxlsptuuvcdpsyvrcyjomqsahyjnqilzbfjiuxbfywkwcrqegqcbquusmnmqgpdlopdwzrvwgphaldawxmtvqfmuopmduxbhlhsxcwvcyonpnfvgtixvgpibwgvomylownrpugzmdrofaoqurwrabmjswfhvwgacuqplelpmaympfjtdldtpkyoakaeuufnpniwjwcjmaalfgbaqrqkdnzbmneuutknsfgboicpjitbpbcvkrtohpficdedkegsfsmsjtoivfeyejrhkwkqarhbdmpbdudeuevaqjiifrqoctbslveczgmeejxoylxuvgikrqapztshjyebzjaijbglbbkemsenlefsqoywlcnrtcemhfnuqxsntbvsprbsgffagetnyiwucxfycoxatektpwmluygpkkokemdlohnfhajxvctrpinjuwcyaeqbkblrqqbflaiqhegxyhggfjxrljizawtyervvwhhejzyqnbcfmywvmrwlvqofggbuwrnwcaijriosdalflllazcfwplqksefwmukpgsfdnfzkanzqshdoxgnagrelwnhhooywxhrmvwrpxjfyygndwzfcjipmfyotwoftibgmcajfifpkqtyjsofmrdkorqsheqadydumootmuookxokypvebipuvldjzglbripnsflcpidcztwahhorsnwbsznojufukkjpxwzuvyyxcxlibcxjdwxbieupjonckbabireuieenqkaqbipefvayktnesafirjwfdizytqxrvxlfnfngdcasymyteamhqpukerpgxrikxjajwnluyzwdzhxciyaqgcxlodjulnwzsnlwyygmcvjlptqxswtezmxwssasjksgtifuvwsjsgvkbmkjqybbmqmnbtowtopobimaqqlcyqgvvidzzsegoituxznknjmkcmyqnmpjuhhjptvzvvkrvcxgmkkiearftyehscvlqvgzvhazymoihoykefsxpfbdfdaijeixulztrhfcfcnvbrxjbcqesfbmjhwekvfbdzkmllhaqbriipaqrflircskwbzideewmudctatullbjayrifdivustyczkqmxrorvhstciclscukvfyvoqularvfbyfvgzzvwhskvsbstsezfcfvbozmrirefnckgpllfynkukywieqpkhmdkczhkzsuenkedxempawuldsvovarkgvbwjyynyohswbkelnwvzxszqfgyofqemvfmurfumtgqcumegndsrmycthtjkjouwvgbxiobwpfippmvszxdxwctdwoghpmksnmwrfhzafowyhcfqkagabhkpiskvesibfagguuublwbdamxznvkcmduqafesgxblevdtcdpooijjcmylseqtsaksnfwjvyqwmxriinbinndzzbnvihdvofeaadwvhcqtkwnlzhdjkpqbixpbnqhtfdngtazwnxuhfeesafphvzlyqdhpcvswokftxxwysbroanqgpkztmjmgsidjkxswxrdgjypwycsutygdpyyurwsullyfmcmerlolrjgnphfoizossvuxoiensfickdtynkdhrwpkuepifxslthbpqjeejoilrtlzcqedzngnjebvnjdmncxadysrhmjtnngcirmoqzjhubfstuogccrrefoyihyguznhmpbyjjabonxbolijzzahsjcxvvrmygbuykfotaztbnuvpzcmfgwvdqigeqekiixomchndcbegcvvgtzhfodwddnelfmhqaqjkdidemcnlzxwkbsajtisgayfnnckxojexrljpebaffyfdqekkbkdqcxamhiukbjsykphkwjxkbqdsxkkskqqojglqlxyrfhxozumwzplexuzrptxcuvrxmofspejtcsojgsupnofovrwrbxgjzfkxtshggqiwribzssvbciytaneomptohytmjzffvcfgidhvbgyokmoediwajzoamxjkgbpointuxyrrrkybgzvgaqbvnpcauwfwayrzvheiggyklzinhwbksdvgvpwnhskngzzaavwudwtnslpztrjcyvcaetixwxgowgrayijcyzafgrlpxphcuscxevahiiwbcbbpljaevtvaaeqqxdohqxjczjosgeeplgiwnjtpjnuuetvurwfyygrvuybnjrhsgvzwxmulwyheibxwgrzpmnwdohxfwgrehkozvovurlkmxedfzhrplabtgeojykjesuujxbzbefezlzjkguncqybcefmmuqmiqznbbojmehvelqqoofkirmagmsrxyqaxbeeqgghsaslfqpwmtrqcmgsygcqxcfrcuusxuqogvraxyxlkukkqezhzsxwnkfnycpmqumftpvtpheiwiuskxynkyrxfawayvuqrkecjoiyuerkxbjivrkkqeokjfsftnckqernpegjsifpbkqlwfhpztthovhyxkpfhbmydesmnnyxxikpwtxthpsmoefyjonnjhojirxtrjnaoobtomzxzujcwrykrpzgdslrxbauluzcbbbmtmhkspmuehdnhdeptiwwtypquiznozhtnglbyrbbelzbvihkpumcryzmrbjagsntozlombiahvdgtmehffomccrevlvqulivxaoqdacjpvwodmnuopfeldscrzoxpgmwodzfonfpujmoubqfvvljyufgtfjufezzlaeofpxudynxprbtkyhdncizgnkrdtbhlgzvikqmqmodroaubmkihyehmfcbnadnxkgnbtfkgzkgciveyhdvhplxoluumkrfirszbfhnpectropyzpmwexgfaouokkvffpaxhqfhvkzdedknqrnstfihdptmacugdraiqjqctqybkbtaaktdsapbcgpoaladreeoyulbxlheybmsbtcxqwpqrdbuiqiutcyhkvuhpumadiylegrkzyqzvpqbxinfeafvzvahxbqgtyiqfbebpjifdqyxcifzhpqlobtjiwexhquexhdimqdusglxgifyjwwkmuddoecwmbgpwgdnijegynifwekzrtpqvfoejerpwchbjtjpcgtokyhoyssdunywshbxywwjizqklbfsiytdsvptymtnqopbprlmgiveimfeadujtprvwatjkskghhhtkebphdauycurfvtwulmuouwkcglimgiwyrxswnwobedlfstkxadpwmjdvfreyybgpbbpgzgjblfanaybzngckipkrzqhajprpyqxrqqrcbtnlyjtopjvpqpmeckvnbexulatotvpzyvfzqbcbzzfynduurgaczkjwacnkavmitsqzjjkgrscmeucqfioykuqpuucpgpqhhibhsquzufwmgadyyzalakuykrwyhmfwxumzgalhlwadrgrynxyiwblhlugqodtokrwsulgohqdhstxyajcvxvngvtluxyakiujttaobucrncloyuskqlxflyxkivcyygozccucweswxyippobtabcqpylkvwmuowhajznlautebntpidzkymupzrdmujhxwdszbpuiprekyasthdfoigkpbbiwzjobmwccqfcdotiqvsjftfomyewwzuahsiuuiccgwlhzbbcexwtgiyvrvlxaxoigeahepsrsfflxwmyzufozitlbarvsjdyatpkcuvgkwggkgkuvcpagndyqzxlvuztligtfniemgknrfmqzhjillmdrfemgmekwpuxtguegzqkaqqariehhjkinigwsmfetygapoudshepaekswcwafvymqngborlfzcihmdkiduqqfxsheuzfteifrtqjcqiwcsbietldjwfkdtmujosihsgqeppmeumextxtpbtiiyivmhurejfeioosourgswejlowwtfpackctcgiqyjtyjhbnawbyvedjzvesrbgktqnwmudinidgtbobquisdooeiwtlacehfspisrntmsfkerdnpwkxnaemvpcykpjclqystkdtguemlgpfmqaooqoivsdvzeeafxtwfxktlbdlmtyvcihvogtcqulirnvwwgwxrjfjlqtmocngtvorkfcsfxwvgzzfumlwqnuskxfacbnetpxncawxhjrfxbdxjnkuxesmqjowawzjoujlmdfaokhlaysayyerylxyytoltyuzorrplljkzmowsgnrnbmbkwcapbilnqqopameaynnqnvmylgxozotigudxkuedsekhjwbauwrkutctnwdmtyuxenvbsvrmaxlamrtpyotxycmnizxhugicywvaqpoxyigrvczdkbncbaplbzyxwhiymjgeryyrxgrauyqsexoeilyoyvhtmylwpmzbfnukaalxpeakwiooniwzfaspzlaftokualigdeykznqyzyyopfxxwlhqayeououwzraidlzeichnacxsnyguuuvrtbzujosjetkaxuvwliagkznfjufcmycpkdfwezgbkfjscjttxeuvgvxwcwrmpbkagwajcsumdyvjfvqbennkkqqmjntuvldbqergiohsbyrxpyhopxvnrtcuushpiybajdujozclcivukqllnpsicxntxetiwpxamcmpxxzfhealjaiptyrmivqqcbnbqfkfbzmsosvyrkhntbjgramvxjsjbhrkbylohpyhwuipserbgdtdypatmjdablxblzrmbeypjwoggguywhbzaputvqblduvdowjrwwlfbnkbnizwfnlihpvmnvgsuuinytcnoqitlnmfawrkflgadjldxdbofgbmindetjbhvtipwbxoxtbxikmelsfjhcugsjlfnknsmvbkajloiadbjblccsvibkersuhvoxyxaguartaicuejgthxvdkwqyzwvzbjpohswinowrzrtomjvbflqbzjqojjxmaguayzlumapruurivupsijxwqlaffwyahufoayxwactvtxwznxotnalpgfinypxayqdzczcvqeuodcvsfgjmdlffjnkzdoqsjbwepsvvjtxqlxdfghuuqlrdddvvldgojkxrdysowifiaufllqwcpfufybaxisffyqcsmqkgpeueknuexcdgbijcldkzluherxvcpeiurjlpgknylkkxfewnkfbdscvytxqdeclpqtdqtwglhaulpiqhfzymvayfdysbfwgpsh"

T = "itekuaabngdyukattklqhiakrmegzafuhrmyaqaesfzrjnevsocbkqgxqracsimqvgcatfwxcbhttxjftvffncnjapacxxthtust"
minWindow(S,T)
#print(len(minWindow2(S0,T)))

# ans =""
# i = j = 0
#
# print (S0)
# while i < len(T):
#     while j < len(S0):
#         if T[i] != S0[j] :
#             j += 1
#         else:
#             ans += T[i]
#             break
#     i+=1
# print(ans==T)
