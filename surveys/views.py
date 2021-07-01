from django.shortcuts import render

# Create your functions here
def getListOfCountries():
    countryList = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps",
                   "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
                   "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
                   "Bhutan", "Bolivia", "Bosnia & Herzegovina", "Botswana", "Brazil", "Brunei",
                   "Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde",
                   "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
                   "Congo", "Dem. Republic of Congo", "Costa Rica", "Croatia", "Cuba",
                   "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
                   "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
                   "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
                   "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
                   "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
                   "Iraq", "Republic of Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan",
                   "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Dem. Ppl. Rep. of Korea",
                   "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
                   "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
                   "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
                   "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
                   "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar, (Burma)",
                   "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
                   "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea",
                   "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
                   "Russian Federation", "Rwanda", "St. Kitts & Nevis", "St. Lucia", "St. Vincent & the Grenadines",
                   "Samoa", "San Marino", "Sao Tome & Principe", "Saudi Arabia", "Senegal", "Serbia",
                   "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
                   "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
                   "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
                   "Thailand", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan",
                   "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America",
                   "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen",
                   "Zambia", "Zimbabwe"]
    return countryList

def getListOfReligions():
    religionList = ["Atheism / Agnosticism", "Baha'i", "Buddhism", "Confucianism", "Druze",
                    "European Paganism", "Gnosticism", "Hinduism", "Islam", "Jainism", "Judaism",
                    "Rastafarianism", "Shinto", "Sikhism", "Traditional African", "Zoroastrianism",
                    "Other"]
    return religionList

def getCatholicRites():
    catholicRites = ["Latin Catholic", "Coptic Catholic", "Eritrean Catholic", "Ethiopian Catholic",
                     "Armenian Catholic", "Albanian Greek Catholic", "Belarusian Greek Catholic",
                     "Bulgarian Greek Catholic", "Croatian / Serbian Greek Catholic",
                     "Greek Byzantine Catholic", "Hungarian Greek Catholic", "Italo-Albanian Greek Catholic",
                     "Macedonian Greek Catholic", "Melkite Greek Catholic", "Romanian Greek Catholic",
                     "Russian Greek Catholic", "Ruthenian Greek Catholic", "Slovak Greek Catholic", "Ukranian Greek Catholic",
                     "Chaldean Catholic", "Syro-Malabar Catholic", "Maronite Catholic", "Syriac Catholic", "Syro-Malankara Catholic"]
    return catholicRites

def getStatesList(countryName):
    statesDict = {"India": ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam",
                               "Bihar", "Chandigarh", "Chhattisgarh", "Dadra - Nagar Haveli / Daman - Diu",
                               "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir",
                               "Jharkhand", "Karnataka", "Kerela", "Ladakh", "Lakshadweep", "Madhya Pradesh",
                               "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry",
                               "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                               "Uttarakhand", "West Bengal"],
                      "Pakistan": ["Islamabad Capital Territory",
                                   "Balochistan",
                                   "Khyber Pakhtunkhwa",
                                   "Punjab",
                                   "Sindh"],
                       "Australia": ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria",
                                                  "Western Australia", "Australian Capital Territory", "Jervis Bay Territory",
                                                  "Northern Territory"]}
    return statesDict[countryName]

def getLanguages():
    languages = ["Abkhazian (ab)", "Achinese (ace)", "Acoli (ach)", "Adangme (ada)", "Adyghe (ady)", "Afar (aa)", "Afrihili (afh)", "Afrikaans (af)", "Aghem (agq)", "Ainu (ain)", "Akan (ak)", "Akkadian (akk)", "Akoose (bss)", "Alabama (akz)", "Albanian (sq)", "Aleut (ale)", "Algerian Arabic (arq)", "Amarik (am)", "American English (en_US)", "American Sign Language (ase)", "Ancient Egyptian (egy)", "Ancient Greek (grc)", "Angika (anp)", "Ao Naga (njo)", "Arabik (ar)", "Aragonese (an)", "Aramaic (arc)", "Araona (aro)", "Arapaho (arp)", "Arawak (arw)", "Armenian (hy)", "Aromanian (rup)", "Arpitan (frp)", "Assamese (as)", "Asturian (ast)", "Asu (asa)", "Atsam (cch)", "Australian English (en_AU)", "Austrian German (de_AT)", "Avaric (av)", "Avestan (ae)", "Awadhi (awa)", "Aymara (ay)", "Azerbaijani (az)", "Badaga (bfq)", "Bafia (ksf)", "Bafut (bfd)", "Bakhtiari (bqi)", "Balinese (ban)", "Baluchi (bal)", "Bambara (bm)", "Bamun (bax)", "Banjar (bjn)", "Basaa (bas)", "Bashkir (ba)", "Basque (eu)", "Batak Toba (bbc)", "Bavarian (bar)", "Beja (bej)", "Belarus kasa (be)", "Bemba (bem)", "Bena (bez)", "Bengali kasa (bn)", "Betawi (bew)", "Bɛɛmis kasa (my)", "Bhojpuri (bho)", "Bikol (bik)", "Bini (bin)", "Bishnupriya (bpy)", "Bislama (bi)", "Blin (byn)", "Blissymbols (zbl)", "Bodo (brx)", "Borɔfo (en)", "Bosnian (bs)", "Bɔlgeria kasa (bg)", "Brahui (brh)", "Braj (bra)", "Brazilian Portuguese (pt_BR)", "Breton (br)", "British English (en_GB)", "Buginese (bug)", "Bulu (bum)", "Buriat (bua)", "Caddo (cad)", "Cajun French (frc)", "Canadian English (en_CA)", "Canadian French (fr_CA)", "Cantonese (yue)", "Capiznon (cps)", "Carib (car)", "Catalan (ca)", "Cayuga (cay)", "Cebuano (ceb)", "Central Atlas Tamazight (tzm)", "Central Dusun (dtp)", "Central Kurdish (ckb)", "Central Yupik (esu)", "Chadian Arabic (shu)", "Chagatai (chg)", "Chamorro (ch)", "Chechen (ce)", "Cherokee (chr)", "Cheyenne (chy)", "Chibcha (chb)", "Chiga (cgg)", "Chimborazo Highland Quichua (qug)", "Chinook Jargon (chn)", "Chipewyan (chp)", "Choctaw (cho)", "Church Slavic (cu)", "Chuukese (chk)", "Chuvash (cv)", "Classical Newari (nwc)", "Classical Syriac (syc)", "Colognian (ksh)", "Comorian (swb)", "Congo Swahili (swc)", "Coptic (cop)", "Cornish (kw)", "Corsican (co)", "Cree (cr)", "Creek (mus)", "Crimean Turkish (crh)", "Croatian (hr)", "Dakota (dak)", "Danish (da)", "Dargwa (dar)", "Dazaga (dzg)", "Delaware (del)", "Dɛɛkye (nl)", "Dinka (din)", "Divehi (dv)", "Dogri (doi)", "Dogrib (dgr)", "Duala (dua)", "Dyula (dyu)", "Dzongkha (dz)", "Eastern Frisian (frs)", "Efik (efi)", "Egyptian Arabic (arz)", "Ekajuk (eka)", "Elamite (elx)", "Embu (ebu)", "Emilian (egl)", "Erzya (myv)", "Esperanto (eo)", "Estonian (et)", "European Portuguese (pt_PT)", "European Spanish (es_ES)", "Ewe (ee)", "Ewondo (ewo)", "Extremaduran (ext)", "Fang (fan)", "Fanti (fat)", "Faroese (fo)", "Fiji Hindi (hif)", "Fijian (fj)", "Filipino (fil)", "Finnish (fi)", "Flemish (nl_BE)", "Fon (fon)", "Frafra (gur)", "Frɛnkye (fr)", "Friulian (fur)", "Fulah (ff)", "Ga (gaa)", "Gagauz (gag)", "Galician (gl)", "Gan Chinese (gan)", "Ganda (lg)", "Gayo (gay)", "Gbaya (gba)", "Geez (gez)", "Georgian (ka)", "Gheg Albanian (aln)", "Ghomala (bbj)", "Gilaki (glk)", "Gilbertese (gil)", "Goan Konkani (gom)", "Gondi (gon)", "Gorontalo (gor)", "Gothic (got)", "Grebo (grb)", "Greek kasa (el)", "Guarani (gn)", "Gujarati (gu)", "Gusii (guz)", "Gwichʼin (gwi)", "Gyaaman (de)", "Gyabanis kasa (jv)", "Gyapan kasa (ja)", "Haida (hai)", "Haitian (ht)", "Hakka Chinese (hak)", "Hangri kasa (hu)", "Hausa (ha)", "Hawaiian (haw)", "Hebrew (he)", "Herero (hz)", "Hiligaynon (hil)", "Hindi (hi)", "Hiri Motu (ho)", "Hittite (hit)", "Hmong (hmn)", "Hupa (hup)", "Iban (iba)", "Ibibio (ibb)", "Icelandic (is)", "Ido (io)", "Igbo (ig)", "Iloko (ilo)", "Inari Sami (smn)", "Indonihyia kasa (id)", "Ingrian (izh)", "Ingush (inh)", "Interlingua (ia)", "Interlingue (ie)", "Inuktitut (iu)", "Inupiaq (ik)", "Irish (ga)", "Italy kasa (it)", "Jamaican Creole English (jam)", "Jju (kaj)", "Jola-Fonyi (dyo)", "Judeo-Arabic (jrb)", "Judeo-Persian (jpr)", "Jutish (jut)", "Kabardian (kbd)", "Kabuverdianu (kea)", "Kabyle (kab)", "Kachin (kac)", "Kaingang (kgp)", "Kako (kkj)", "Kalaallisut (kl)", "Kalenjin (kln)", "Kalmyk (xal)", "Kamba (kam)", "Kambodia kasa (km)", "Kanembu (kbl)", "Kannada (kn)", "Kanuri (kr)", "Kara-Kalpak (kaa)", "Karachay-Balkar (krc)", "Karelian (krl)", "Kashmiri (ks)", "Kashubian (csb)", "Kawi (kaw)", "Kazakh (kk)", "Kenyang (ken)", "Khasi (kha)", "Khotanese (kho)", "Khowar (khw)", "Kikuyu (ki)", "Kimbundu (kmb)", "Kinaray-a (krj)", "Kirmanjki (kiu)", "Klingon (tlh)", "Kom (bkm)", "Komi (kv)", "Komi-Permyak (koi)", "Kongo (kg)", "Konkani (kok)", "Korea kasa (ko)", "Koro (kfo)", "Kosraean (kos)", "Kotava (avk)", "Koyra Chiini (khq)", "Koyraboro Senni (ses)", "Kpelle (kpe)", "Krio (kri)", "Kuanyama (kj)", "Kumyk (kum)", "Kurdish (ku)", "Kurukh (kru)", "Kutenai (kut)", "Kwasio (nmg)", "Kyaena kasa (zh)", "Kyɛk kasa (cs)", "Kyrgyz (ky)", "Kʼicheʼ (quc)", "Ladino (lad)", "Lahnda (lah)", "Lakota (lkt)", "Lamba (lam)", "Langi (lag)", "Lao (lo)", "Latgalian (ltg)", "Latin (la)", "Latin American Spanish (es_419)", "Latvian (lv)", "Laz (lzz)", "Lezghian (lez)", "Ligurian (lij)", "Limburgish (li)", "Lingala (ln)", "Lingua Franca Nova (lfn)", "Literary Chinese (lzh)", "Lithuanian (lt)", "Livonian (liv)", "Lojban (jbo)", "Lombard (lmo)", "Low German (nds)", "Lower Silesian (sli)", "Lower Sorbian (dsb)", "Lozi (loz)", "Luba-Katanga (lu)", "Luba-Lulua (lua)", "Luiseno (lui)", "Lule Sami (smj)", "Lunda (lun)", "Luo (luo)", "Luxembourgish (lb)", "Luyia (luy)", "Maba (mde)", "Macedonian (mk)", "Machame (jmc)", "Madurese (mad)", "Mafa (maf)", "Magahi (mag)", "Main-Franconian (vmf)", "Maithili (mai)", "Makasar (mak)", "Makhuwa-Meetto (mgh)", "Makonde (kde)", "Malagasy (mg)", "Malay kasa (ms)", "Malayalam (ml)", "Maltese (mt)", "Manchu (mnc)", "Mandar (mdr)", "Mandingo (man)", "Manipuri (mni)", "Manx (gv)", "Maori (mi)", "Mapuche (arn)", "Marathi (mr)", "Mari (chm)", "Marshallese (mh)", "Marwari (mwr)", "Masai (mas)", "Mazanderani (mzn)", "Medumba (byv)", "Mende (men)", "Mentawai (mwv)", "Meru (mer)", "Metaʼ (mgo)", "Mexican Spanish (es_MX)", "Micmac (mic)", "Middle Dutch (dum)", "Middle English (enm)", "Middle French (frm)", "Middle High German (gmh)", "Middle Irish (mga)", "Min Nan Chinese (nan)", "Minangkabau (min)", "Mingrelian (xmf)", "Mirandese (mwl)", "Mizo (lus)", "Modern Standard Arabic (ar_001)", "Mohawk (moh)", "Moksha (mdf)", "Moldavian (ro_MD)", "Mongo (lol)", "Mongolian (mn)", "Morisyen (mfe)", "Moroccan Arabic (ary)", "Mossi (mos)", "Multiple Languages (mul)", "Mundang (mua)", "Muslim Tat (ttt)", "Myene (mye)", "Nama (naq)", "Nauru (na)", "Navajo (nv)", "Ndonga (ng)", "Neapolitan (nap)", "Newari (new)", "Nɛpal kasa (ne)", "Ngambay (sba)", "Ngiemboon (nnh)", "Ngomba (jgo)", "Nheengatu (yrl)", "Nias (nia)", "Niuean (niu)", "No linguistic content (zxx)", "Nogai (nog)", "North Ndebele (nd)", "Northern Frisian (frr)", "Northern Sami (se)", "Northern Sotho (nso)", "Norwegian (no)", "Norwegian Bokmål (nb)", "Norwegian Nynorsk (nn)", "Novial (nov)", "Nuer (nus)", "Nyamwezi (nym)", "Nyanja (ny)", "Nyankole (nyn)", "Nyasa Tonga (tog)", "Nyoro (nyo)", "Nzima (nzi)", "NʼKo (nqo)", "Occitan (oc)", "Ojibwa (oj)", "Old English (ang)", "Old French (fro)", "Old High German (goh)", "Old Irish (sga)", "Old Norse (non)", "Old Persian (peo)", "Old Provençal (pro)", "Oriya (or)", "Oromo (om)", "Osage (osa)", "Ossetic (os)", "Ottoman Turkish (ota)", "Pahlavi (pal)", "Palatine German (pfl)", "Palauan (pau)", "Pali (pi)", "Pampanga (pam)", "Pangasinan (pag)", "Papiamento (pap)", "Pashto (ps)", "Pennsylvania German (pdc)", "Pɛɛhyia kasa (fa)", "Phoenician (phn)", "Picard (pcd)", "Piedmontese (pms)", "Plautdietsch (pdt)", "Pohnpeian (pon)", "Pontic (pnt)", "Pɔland kasa (pl)", "Pɔɔtugal kasa (pt)", "Prussian (prg)", "Pungyabi kasa (pa)", "Quechua (qu)", "Rahyia kasa (ru)", "Rajasthani (raj)", "Rapanui (rap)", "Rarotongan (rar)", "Rewanda kasa (rw)", "Riffian (rif)", "Romagnol (rgn)", "Romansh (rm)", "Romany (rom)", "Rombo (rof)", "Romenia kasa (ro)", "Root (root)", "Rotuman (rtm)", "Roviana (rug)", "Rundi (rn)", "Rusyn (rue)", "Rwa (rwk)", "Saho (ssy)", "Sakha (sah)", "Samaritan Aramaic (sam)", "Samburu (saq)", "Samoan (sm)", "Samogitian (sgs)", "Sandawe (sad)", "Sango (sg)", "Sangu (sbp)", "Sanskrit (sa)", "Santali (sat)", "Sardinian (sc)", "Sasak (sas)", "Sassarese Sardinian (sdc)", "Saterland Frisian (stq)", "Saurashtra (saz)", "Scots (sco)", "Scottish Gaelic (gd)", "Selayar (sly)", "Selkup (sel)", "Sena (seh)", "Seneca (see)", "Serbian (sr)", "Serbo-Croatian (sh)", "Serer (srr)", "Seri (sei)", "Shambala (ksb)", "Shan (shn)", "Shona (sn)", "Sichuan Yi (ii)", "Sicilian (scn)", "Sidamo (sid)", "Siksika (bla)", "Silesian (szl)", "Simplified Chinese (zh_Hans)", "Sindhi (sd)", "Sinhala (si)", "Skolt Sami (sms)", "Slave (den)", "Slovak (sk)", "Slovenian (sl)", "Soga (xog)", "Sogdien (sog)", "Somalia kasa (so)", "Soninke (snk)", "South Azerbaijani (azb)", "South Ndebele (nr)", "Southern Altai (alt)", "Southern Sami (sma)", "Southern Sotho (st)", "Spain kasa (es)", "Sranan Tongo (srn)", "Standard Moroccan Tamazight (zgh)", "Sukuma (suk)", "Sumerian (sux)", "Sundanese (su)", "Susu (sus)", "Swahili (sw)", "Swati (ss)", "Sweden kasa (sv)", "Swiss French (fr_CH)", "Swiss German (gsw)", "Swiss High German (de_CH)", "Syriac (syr)", "Tachelhit (shi)", "Taeland kasa (th)", "Tagalog (tl)", "Tahitian (ty)", "Taita (dav)", "Tajik (tg)", "Talysh (tly)", "Tamashek (tmh)", "Tamil kasa (ta)", "Taroko (trv)", "Tasawaq (twq)", "Tatar (tt)", "Telugu (te)", "Tereno (ter)", "Teso (teo)", "Tetum (tet)", "Tɛɛki kasa (tr)", "Tibetan (bo)", "Tigre (tig)", "Tigrinya (ti)", "Timne (tem)", "Tiv (tiv)", "Tlingit (tli)", "Tok Pisin (tpi)", "Tokelau (tkl)", "Tongan (to)", "Tornedalen Finnish (fit)", "Traditional Chinese (zh_Hant)", "Tsakhur (tkr)", "Tsakonian (tsd)", "Tsimshian (tsi)", "Tsonga (ts)", "Tswana (tn)", "Tulu (tcy)", "Tumbuka (tum)", "Tunisian Arabic (aeb)", "Turkmen (tk)", "Turoyo (tru)", "Tuvalu (tvl)", "Tuvinian (tyv)", "Twi (tw)", "Tyap (kcg)", "Udmurt (udm)", "Ugaritic (uga)", "Ukren kasa (uk)", "Umbundu (umb)", "Unknown Language (und)", "Upper Sorbian (hsb)", "Urdu kasa (ur)", "Uyghur (ug)", "Uzbek (uz)", "Vai (vai)", "Venda (ve)", "Venetian (vec)", "Veps (vep)", "Viɛtnam kasa (vi)", "Volapük (vo)", "Võro (vro)", "Votic (vot)", "Vunjo (vun)", "Walloon (wa)", "Walser (wae)", "Waray (war)", "Warlpiri (wbp)", "Washo (was)", "Wayuu (guc)", "Welsh (cy)", "West Flemish (vls)", "Western Frisian (fy)", "Western Mari (mrj)", "Wolaytta (wal)", "Wolof (wo)", "Wu Chinese (wuu)", "Xhosa (xh)", "Xiang Chinese (hsn)", "Yangben (yav)", "Yao (yao)", "Yapese (yap)", "Yemba (ybb)", "Yiddish (yi)", "Yoruba (yo)", "Zapotec (zap)", "Zarma (dje)", "Zaza (zza)", "Zeelandic (zea)", "Zenaga (zen)", "Zhuang (za)", "Zoroastrian Dari (gbz)", "Zulu (zu)", "Zuni (zun)"]
    return languages

# Create your views here.
def catholic(request):
    context = {"countryList": getListOfCountries(),
               "religionList": getListOfReligions(),
               "catholicRites": getCatholicRites(),
               "languages": getLanguages()}
    return render(request, "catholic.html", context)

def surveys(request):
    context = {"countryList": getListOfCountries(),
               "religionList": getListOfReligions(),
               "catholicRites": getCatholicRites(),
               "languages": getLanguages()}
    return render(request, "catholic.html", context)

def countryFrom(request, countryName):
    if request.method == "GET":
        countryStates = {"India": ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam",
                                   "Bihar", "Chandigarh", "Chhattisgarh", "Dadra - Nagar Haveli / Daman - Diu",
                                   "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir",
                                   "Jharkhand", "Karnataka", "Kerela", "Ladakh", "Lakshadweep", "Madhya Pradesh",
                                   "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry",
                                   "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                                   "Uttarakhand", "West Bengal"],
                          "Pakistan": ["Islamabad Capital Territory",
                                       "Balochistan",
                                       "Khyber Pakhtunkhwa",
                                       "Punjab",
                                       "Sindh"],
                           "Australia": ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria",
                                                      "Western Australia", "Australian Capital Territory", "Jervis Bay Territory",
                                                      "Northern Territory"]}
        if countryName in countryStates.keys():
            context = {"statesList": countryStates[countryName]}
            return render(request, "template-parts/countryFrom.html", context)
        else:
            context = {"statesList": ["No states available"]}
            return render(request, "template-parts/countryFrom.html", context)

def countryIn(request, countryName):
    if request.method == "GET":
        countryStates = {"India": ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam",
                                   "Bihar", "Chandigarh", "Chhattisgarh", "Dadra - Nagar Haveli / Daman - Diu",
                                   "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir",
                                   "Jharkhand", "Karnataka", "Kerela", "Ladakh", "Lakshadweep", "Madhya Pradesh",
                                   "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry",
                                   "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
                                   "Uttarakhand", "West Bengal"],
                          "Pakistan": ["Islamabad Capital Territory",
                                       "Balochistan",
                                       "Khyber Pakhtunkhwa",
                                       "Punjab",
                                       "Sindh"],
                           "Australia": ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria",
                                                      "Western Australia", "Australian Capital Territory", "Jervis Bay Territory",
                                                      "Northern Territory"]}
        if countryName in countryStates.keys():
            context = {"statesList": countryStates[countryName]}
            return render(request, "template-parts/countryIn.html", context)
        else:
            context = {"statesList": ["No states available"]}
            return render(request, "template-parts/countryIn.html", context)
