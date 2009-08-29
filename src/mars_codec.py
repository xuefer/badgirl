# -*- coding:utf-8 -*-

_mapToMars = {
	u"八": u"仈",
	u"九": u"⑨",
	u"前": u"湔",
	u"考": u"栲",
	u"宋": u"浨",
	u"內": u"禸",
	u"容": u"嫆",
	u"去": u"詓",
	u"很": u"佷",
	u"奇": u"渏",
	u"且": u"苴",
	u"情": u"凊",
	u"狂": u"誑",
	u"近": u"菦",
	u"至": u"臸",
	u"自": u"洎",
	u"己": u"巳",
	u"做": u"莋",
	u"但": u"泹",
	u"五": u"伍",
	u"又": u"叒",
	u"抄": u"莏",
	u"都": u"嘟",
	u"然": u"嘫",
	u"題": u"趧",
	u"乘": u"塖",
	u"入": u"叺",
	u"名": u"洺",
	u"句": u"呴",
	u"英": u"渶",
	u"希": u"唏",
	u"望": u"朢",
	u"像": u"潒",
	u"快": u"赽",
	u"懂": u"慬",
	u"何": u"哬",
	u"止": u"圵",
	u"直": u"矗",
	u"作": u"莋",
	u"者": u"鍺",
	u"成": u"荿",
	u"曹": u"蓸",
	u"雪": u"膤",
	u"芹": u"芹",
	u"才": u"財",
	u"面": u"媔",
	u"工": u"笁",
	u"信": u"信",
	u"例": u"唎",
	u"改": u"妀",
	u"三": u"彡",
	u"神": u"鉮",
	u"似": u"姒",
	u"就": u"僦",
	u"相": u"楿",
	u"仿": u"汸",
	u"悲": u"蕜",
	u"五": u"伍",
	u"六": u"陸",
	u"至": u"臸",
	u"梅": u"烸",
	u"完": u"唍",
	u"整": u"整",
	u"另": u"叧",
	u"久": u"玖",
	u"像": u"潒",
	u"迷": u"洣",
	u"尊": u"澊",
	u"制": u"淛",
	u"造": u"慥",
	u"重": u"偅",
	u"第": u"苐",
	u"很": u"佷",
	u"符": u"苻",
	u"持": u"歭",
	u"因": u"洇",
	u"凶": u"兇",
	u"能": u"能",
	u"偶": u"耦",
	u"然": u"嘫",
	u"迷": u"洣",
	u"茫": u"汒",
	u"右": u"祐",
	u"字": u"芓",
	u"他": u"彵",
	u"它": u"咜",
	u"新": u"噺",
	u"叶": u"旪",
	u"在": u"茬",
	u"多": u"哆",
	u"合": u"匼",
	u"或": u"戓",
	u"部": u"蔀",
	u"分": u"汾",
	u"用": u"鼡",
	u"孩": u"駭",
	u"客": u"愙",
	u"朋": u"萠",
	u"友": u"伖",
	u"激": u"噭",
	u"烈": u"烮",
	u"现": u"哯",
	u"象": u"潒",
	u"只": u"呮",
	u"而": u"洏",
	u"已": u"巳",
	u"化": u"囮",
	u"食": u"喰",
	u"物": u"粅",
	u"事": u"倳",
	u"二": u"②",
	u"球": u"浗",
	u"睛": u"聙",
	u"同": u"哃",
	u"勃": u"葧",
	u"鸟": u"茑",
	u"月": u"仴",
	u"允": u"尣",
	u"王": u"迋",
	u"皇": u"瑝",
	u"帝": u"渧",
	u"没": u"莈",
	u"有": u"洧",
	u"次": u"佽",
	u"每": u"烸",
	u"卡": u"鉲",
	u"路": u"蕗",
	u"坐": u"唑",
	u"比": u"仳",
	u"印": u"茚",
	u"度": u"喥",
	u"尼": u"胒",
	u"西": u"覀",
	u"章": u"嶂",
	u"黑": u"嫼",
	u"向": u"姠",
	u"木": u"朩",
	u"母": u"毋",
	u"上": u"仩",
	u"班": u"癍",
	u"肉": u"禸",
	u"玻": u"箥",
	u"璃": u"璃",
	u"碎": u"誶",
	u"片": u"爿",
	u"死": u"迉",
	u"千": u"芉",
	u"最": u"朂",
	u"常": u"瑺",
	u"用": u"鼡",
	u"福": u"鍢",
	u"跟": u"哏",
	u"再": u"洅",
	u"来": u"唻",
	u"冰": u"栤",
	u"封": u"葑",
	u"的": u"啲",
	u"错": u"諎",
	u"今": u"紟",
	u"年": u"姩",
	u"流": u"鋶",
	u"行": u"荇",
	u"注": u"紸",
	u"捣": u"搗",
	u"蛋": u"蜑",
	u"版": u"蝂",
	u"手": u"掱",
	u"十": u"┿",
	u"继": u"繼",
	u"忘": u"莣",
	u"失": u"夨",
	u"丹": u"丼",
	u"病": u"疒",
	u"衣": u"衤",
	u"服": u"垺",
	u"幼": u"呦",
	u"气": u"気",
	u"说": u"詤",
	u"小": u"曉",
	u"猪": u"豬",
	u"亲": u"儭",
	u"川": u"〣",
	u"火": u"吙",
	u"值": u"徝",
	u"星": u"煋",
	u"文": u"攵",
	u"之": u"の",
	u"办": u"か",
	u"元": u"え",
	u"代": u"玳",
	u"理": u"悝",
	u"背": u"褙",
	u"世": u"卋",
	u"出": u"絀",
	u"可": u"鈳",
	u"以": u"鉯",
	u"真": u"眞",
	u"时": u"塒",
	u"美": u"媄",
	u"亮": u"煷",
	u"空": u"涳",
	u"颓": u"穨",
	u"也": u"吔",
	u"是": u"昰",
	u"灰": u"咴",
	u"色": u"銫",
	u"光": u"咣",
	u"更": u"哽",
	u"音": u"喑",
	u"小": u"尛",
	u"男": u"侽",
	u"味": u"菋",
	u"道": u"噵",
	u"正": u"㊣",
	u"到": u"箌",
	u"得": u"嘚",
	u"急": u"ゑ",
	u"大": u"夶",
	u"叔": u"菽",
	u"太": u"呔",
	u"傻": u"儍",
	u"巫": u"莁",
	u"婆": u"嘙",
	u"一": u"┅",
	u"下": u"丅",
	u"安": u"咹",
	u"全": u"铨",
	u"不": u"鈈",
	u"本": u"夲",
	u"天": u"兲",
	u"要": u"偠",
	u"易": u"噫",
	u"如": u"洳",
	u"抱": u"菢",
	u"你": u"伱",
	u"中": u"ф",
	u"华": u"囮",
	u"人": u"囚",
	u"民": u"囻",
	u"共": u"囲",
	u"和": u"囷",
	u"追": u"縋",
	u"寻": u"尋",
	u"打": u"咑",
	u"出": u"絀",
	u"么": u"仫",
	u"简": u"簡",
	u"单": u"單",
	u"绝": u"絕",
	u"味": u"菋",
	u"湖": u"鍸",
	u"南": u"喃",
	u"定": u"萣",
	u"会": u"茴",
	u"我": u"莪",
	u"张": u"涨",
	u"家": u"镓",
	u"界": u"堺",
	u"的": u"嘚",
	u"省": u"渻",
	u"天": u"忝",
	u"亮": u"煷",
	u"了": u"叻",
	u"走": u"赱",
	u"真": u"嫃",
	u"明": u"朙",
	u"我": u"峩",
	u"把": u"紦",
	u"泥": u"苨",
	u"土": u"汢",
	u"脏": u"贓",
	u"永": u"詠",
	u"玉": u"玊",
	u"少": u"尐",
	u"木": u"朩",
	u"回": u"囙",
	u"女": u"囡",
	u"寸": u"団",
	u"哈": u"囧",
	u"井": u"囲",
	u"义": u"図",
	u"和": u"囷",
	u"正": u"囸",
	u"令": u"囹",
	u"台": u"囼",
	u"幸": u"圉",
	u"青": u"圊",
	u"书": u"圕",
	u"贵": u"圚",
	u"乐": u"圞",
	u"儿": u"ㄦ",
	u"子": u"孓",
	u"言": u"訁",
	u"盲": u"吂",
	u"口": u"ロ",
	u"亏": u"虧",
	u"日": u"ㄖ",
	u"中": u"Φ",
	u"甘": u"咁",
	u"左": u"咗",
	u"布": u"咘",
	u"北": u"丠",
	u"生": u"苼",
	u"白": u"苩",
	u"他": u"怹",
	u"力": u"仂",
	u"老": u"咾",
	u"再": u"洅",
	u"有": u"囿",
	u"好": u"恏",
	u"呀": u"吖",
	u"花": u"婲",
	u"月": u"冄",
	u"溅": u"濺",
	u"守": u"垨",
	u"来": u"逨",
	u"楼": u"嘍",
	u"两": u"両",
	u"毒": u"蝳",
	u"蛋": u"疍",
	u"明": u"奣",
	u"喜": u"囍",
	u"犬": u"猋",
	u"马": u"骉",
	u"牛": u"犇",
	u"羊": u"羴",
	u"虫": u"蟲",
	u"香": u"馫",
	u"泉": u"灥",
	u"田": u"畾",
	u"白": u"皛",
	u"心": u"惢",
	u"鹿": u"麤",
	u"马": u"驫",
	u"鱼": u"鱻",
	u"贝": u"贔",
	u"飞": u"飝",
	u"士": u"壵",
	u"月": u"朤",
	u"炎": u"燚",
	u"伞": u"傘",
	u"门": u"闁",
	u"风": u"闏",
	u"甜": u"憇",
	u"亚": u"亜",
	u"龙": u"龖",
	u"虎": u"虤",
	u"耳": u"聑",
	u"立": u"竝",
	u"女": u"奻",
	u"呆": u"槑",
	u"水": u"沝",
	u"山": u"屾",
	u"万": u"萬",
	u"与": u"與",
	u"丑": u"醜",
	u"专": u"專",
	u"业": u"業",
	u"丛": u"叢",
	u"东": u"東",
	u"丝": u"絲",
	u"丢": u"丟",
	u"两": u"兩",
	u"严": u"嚴",
	u"丧": u"喪",
	u"个": u"個",
	u"丬": u"爿",
	u"丰": u"豐",
	u"临": u"臨",
	u"为": u"為",
	u"丽": u"麗",
	u"举": u"舉",
	u"么": u"麼",
	u"义": u"義",
	u"乌": u"烏",
	u"乐": u"樂",
	u"乔": u"喬",
	u"习": u"習",
	u"乡": u"鄉",
	u"书": u"書",
	u"买": u"買",
	u"乱": u"亂",
	u"争": u"爭",
	u"于": u"於",
	u"亏": u"虧",
	u"云": u"雲",
	u"亘": u"亙",
	u"亚": u"亞",
	u"产": u"產",
	u"亩": u"畝",
	u"亲": u"親",
	u"亵": u"褻",
	u"亸": u"嚲",
	u"亿": u"億",
	u"仅": u"僅",
	u"从": u"從",
	u"仑": u"侖",
	u"仓": u"倉",
	u"仪": u"儀",
	u"们": u"們",
	u"价": u"價",
	u"众": u"眾",
	u"优": u"優",
	u"伙": u"夥",
	u"会": u"會",
	u"伛": u"傴",
	u"伞": u"傘",
	u"伟": u"偉",
	u"传": u"傳",
	u"伤": u"傷",
	u"伥": u"倀",
	u"伦": u"倫",
	u"伧": u"傖",
	u"伪": u"偽",
	u"伫": u"佇",
	u"体": u"體",
	u"余": u"餘",
	u"佣": u"傭",
	u"佥": u"僉",
	u"侠": u"俠",
	u"侣": u"侶",
	u"侥": u"僥",
	u"侦": u"偵",
	u"侧": u"側",
	u"侨": u"僑",
	u"侩": u"儈",
	u"侪": u"儕",
	u"侬": u"儂",
	u"俣": u"俁",
	u"俦": u"儔",
	u"俨": u"儼",
	u"俩": u"倆",
	u"俪": u"儷",
	u"俭": u"儉",
	u"债": u"債",
	u"倾": u"傾",
	u"偬": u"傯",
	u"偻": u"僂",
	u"偾": u"僨",
	u"偿": u"償",
	u"傥": u"儻",
	u"傧": u"儐",
	u"储": u"儲",
	u"傩": u"儺",
	u"儿": u"兒",
	u"兑": u"兌",
	u"兖": u"兗",
	u"党": u"黨",
	u"兰": u"蘭",
	u"关": u"關",
	u"兴": u"興",
	u"兹": u"茲",
	u"养": u"養",
	u"兽": u"獸",
	u"冁": u"囅",
	u"内": u"內",
	u"冈": u"岡",
	u"册": u"冊",
	u"写": u"寫",
	u"军": u"軍",
	u"农": u"農",
	u"冢": u"塚",
	u"冯": u"馮",
	u"冲": u"沖",
	u"决": u"決",
	u"况": u"況",
	u"冻": u"凍",
	u"净": u"淨",
	u"凄": u"淒",
	u"凉": u"涼",
	u"凌": u"淩",
	u"减": u"減",
	u"凑": u"湊",
	u"凛": u"凜",
	u"几": u"幾",
	u"凤": u"鳳",
	u"凫": u"鳧",
	u"凭": u"憑",
	u"凯": u"凱",
	u"击": u"擊",
	u"凼": u"氹",
	u"凿": u"鑿",
	u"刍": u"芻",
	u"划": u"劃",
	u"刘": u"劉",
	u"则": u"則",
	u"刚": u"剛",
	u"创": u"創",
	u"删": u"刪",
	u"别": u"別",
	u"刬": u"剗",
	u"刭": u"剄",
	u"刽": u"劊",
	u"刿": u"劌",
	u"剀": u"剴",
	u"剂": u"劑",
	u"剐": u"剮",
	u"剑": u"劍",
	u"剥": u"剝",
	u"剧": u"劇",
	u"劝": u"勸",
	u"办": u"辦",
	u"务": u"務",
	u"劢": u"勱",
	u"动": u"動",
	u"励": u"勵",
	u"劲": u"勁",
	u"劳": u"勞",
	u"势": u"勢",
	u"勋": u"勳",
	u"勐": u"猛",
	u"勚": u"勩",
	u"匀": u"勻",
	u"匦": u"匭",
	u"匮": u"匱",
	u"区": u"區",
	u"医": u"醫",
	u"华": u"華",
	u"协": u"協",
	u"单": u"單",
	u"卖": u"賣",
	u"卢": u"盧",
	u"卤": u"鹵",
	u"卧": u"臥",
	u"卫": u"衛",
	u"却": u"卻",
	u"卺": u"巹",
	u"厂": u"廠",
	u"厅": u"廳",
	u"历": u"曆",
	u"厉": u"厲",
	u"压": u"壓",
	u"厌": u"厭",
	u"厍": u"厙",
	u"厕": u"廁",
	u"厢": u"廂",
	u"厣": u"厴",
	u"厦": u"廈",
	u"厨": u"廚",
	u"厩": u"廄",
	u"厮": u"廝",
	u"县": u"縣",
	u"叁": u"三",
	u"参": u"參",
	u"叆": u"靉",
	u"叇": u"靆",
	u"双": u"雙",
	u"发": u"發",
	u"变": u"變",
	u"叙": u"敘",
	u"叠": u"疊",
	u"叶": u"葉",
	u"号": u"號",
	u"叹": u"歎",
	u"叽": u"嘰",
	u"吁": u"籲",
	u"后": u"後",
	u"吓": u"嚇",
	u"吕": u"呂",
	u"吗": u"嗎",
	u"吣": u"唚",
	u"吨": u"噸",
	u"听": u"聽",
	u"启": u"啟",
	u"吴": u"吳",
	u"呒": u"嘸",
	u"呓": u"囈",
	u"呕": u"嘔",
	u"呖": u"嚦",
	u"呗": u"唄",
	u"员": u"員",
	u"呙": u"咼",
	u"呛": u"嗆",
	u"呜": u"嗚",
	u"咏": u"詠",
	u"咔": u"哢",
	u"咙": u"嚨",
	u"咛": u"嚀",
	u"咝": u"噝",
	u"咤": u"吒",
	u"咴": u"噅",
	u"咸": u"鹹",
	u"哌": u"呱",
	u"响": u"響",
	u"哑": u"啞",
	u"哒": u"噠",
	u"哓": u"嘵",
	u"哔": u"嗶",
	u"哕": u"噦",
	u"哗": u"嘩",
	u"哙": u"噲",
	u"哜": u"嚌",
	u"哝": u"噥",
	u"哟": u"喲",
	u"唛": u"嘜",
	u"唝": u"嗊",
	u"唠": u"嘮",
	u"唡": u"啢",
	u"唢": u"嗩",
	u"唣": u"唕",
	u"唤": u"喚",
	u"唿": u"呼",
	u"啧": u"嘖",
	u"啬": u"嗇",
	u"啭": u"囀",
	u"啮": u"齧",
	u"啰": u"囉",
	u"啴": u"嘽",
	u"啸": u"嘯",
	u"喷": u"噴",
	u"喽": u"嘍",
	u"喾": u"嚳",
	u"嗫": u"囁",
	u"嗬": u"呵",
	u"嗳": u"噯",
	u"嘘": u"噓",
	u"嘤": u"嚶",
	u"嘱": u"囑",
	u"噜": u"嚕",
	u"噼": u"劈",
	u"嚣": u"囂",
	u"嚯": u"謔",
	u"团": u"團",
	u"园": u"園",
	u"囱": u"囪",
	u"围": u"圍",
	u"囵": u"圇",
	u"国": u"國",
	u"图": u"圖",
	u"圆": u"圓",
	u"圣": u"聖",
	u"圹": u"壙",
	u"场": u"場",
	u"坂": u"阪",
	u"坏": u"壞",
	u"块": u"塊",
	u"坚": u"堅",
	u"坛": u"壇",
	u"坜": u"壢",
	u"坝": u"壩",
	u"坞": u"塢",
	u"坟": u"墳",
	u"坠": u"墜",
	u"垄": u"壟",
	u"垅": u"壟",
	u"垆": u"壚",
	u"垒": u"壘",
	u"垦": u"墾",
	u"垧": u"坰",
	u"垩": u"堊",
	u"垫": u"墊",
	u"垭": u"埡",
	u"垯": u"墶",
	u"垱": u"壋",
	u"垲": u"塏",
	u"垴": u"堖",
	u"埘": u"塒",
	u"埙": u"塤",
	u"埚": u"堝",
	u"埝": u"墊",
	u"埯": u"垵",
	u"堑": u"塹",
	u"堕": u"墮",
	u"塆": u"壪",
	u"塬": u"原",
	u"墙": u"牆",
	u"壮": u"壯",
	u"声": u"聲",
	u"壳": u"殼",
	u"壶": u"壺",
	u"壸": u"壼",
	u"处": u"處",
	u"备": u"備",
	u"复": u"複",
	u"够": u"夠",
	u"头": u"頭",
	u"夸": u"誇",
	u"夹": u"夾",
	u"夺": u"奪",
	u"奁": u"奩",
	u"奂": u"奐",
	u"奋": u"奮",
	u"奖": u"獎",
	u"奥": u"奧",
	u"妆": u"妝",
	u"妇": u"婦",
	u"妈": u"媽",
	u"妩": u"嫵",
	u"妪": u"嫗",
	u"妫": u"媯",
	u"姗": u"姍",
	u"姜": u"薑",
	u"娄": u"婁",
	u"娅": u"婭",
	u"娆": u"嬈",
	u"娇": u"嬌",
	u"娈": u"孌",
	u"娱": u"娛",
	u"娲": u"媧",
	u"娴": u"嫻",
	u"婳": u"嫿",
	u"婴": u"嬰",
	u"婵": u"嬋",
	u"婶": u"嬸",
	u"媪": u"媼",
	u"嫒": u"嬡",
	u"嫔": u"嬪",
	u"嫱": u"嬙",
	u"嬷": u"嬤",
	u"孙": u"孫",
	u"学": u"學",
	u"孪": u"孿",
	u"宁": u"寧",
	u"宝": u"寶",
	u"实": u"實",
	u"宠": u"寵",
	u"审": u"審",
	u"宪": u"憲",
	u"宫": u"宮",
	u"宽": u"寬",
	u"宾": u"賓",
	u"寝": u"寢",
	u"对": u"對",
	u"寻": u"尋",
	u"导": u"導",
	u"寿": u"壽",
	u"将": u"將",
	u"尔": u"爾",
	u"尘": u"塵",
	u"尝": u"嘗",
	u"尧": u"堯",
	u"尴": u"尷",
	u"尸": u"屍",
	u"尽": u"盡",
	u"层": u"層",
	u"屃": u"屭",
	u"屉": u"屜",
	u"届": u"屆",
	u"属": u"屬",
	u"屡": u"屢",
	u"屦": u"屨",
	u"屿": u"嶼",
	u"岁": u"歲",
	u"岂": u"豈",
	u"岖": u"嶇",
	u"岗": u"崗",
	u"岘": u"峴",
	u"岙": u"嶴",
	u"岚": u"嵐",
	u"岛": u"島",
	u"岭": u"嶺",
	u"岳": u"嶽",
	u"岽": u"崠",
	u"岿": u"巋",
	u"峃": u"嶨",
	u"峄": u"嶧",
	u"峡": u"峽",
	u"峣": u"嶢",
	u"峤": u"嶠",
	u"峥": u"崢",
	u"峦": u"巒",
	u"崂": u"嶗",
	u"崃": u"崍",
	u"崄": u"嶮",
	u"崭": u"嶄",
	u"嵘": u"嶸",
	u"嵚": u"嶔",
	u"嵛": u"崳",
	u"嵝": u"嶁",
	u"嵴": u"脊",
	u"巅": u"巔",
	u"巩": u"鞏",
	u"巯": u"巰",
	u"币": u"幣",
	u"帅": u"帥",
	u"师": u"師",
	u"帏": u"幃",
	u"帐": u"帳",
	u"帘": u"簾",
	u"帜": u"幟",
	u"带": u"帶",
	u"帧": u"幀",
	u"帮": u"幫",
	u"帱": u"幬",
	u"帻": u"幘",
	u"帼": u"幗",
	u"幂": u"冪",
	u"幞": u"襆",
	u"干": u"幹",
	u"并": u"並",
	u"幺": u"么",
	u"广": u"廣",
	u"庄": u"莊",
	u"庆": u"慶",
	u"庐": u"廬",
	u"庑": u"廡",
	u"库": u"庫",
	u"应": u"應",
	u"庙": u"廟",
	u"庞": u"龐",
	u"废": u"廢",
	u"庼": u"廎",
	u"廪": u"廩",
	u"开": u"開",
	u"异": u"異",
	u"弃": u"棄",
	u"张": u"張",
	u"弥": u"彌",
	u"弪": u"弳",
	u"弯": u"彎",
	u"弹": u"彈",
	u"强": u"強",
	u"归": u"歸",
	u"当": u"當",
	u"录": u"錄",
	u"彟": u"彠",
	u"彦": u"彥",
	u"彻": u"徹",
	u"径": u"徑",
	u"徕": u"徠",
	u"御": u"禦",
	u"忆": u"憶",
	u"忏": u"懺",
	u"忧": u"憂",
	u"忾": u"愾",
	u"怀": u"懷",
	u"态": u"態",
	u"怂": u"慫",
	u"怃": u"憮",
	u"怄": u"慪",
	u"怅": u"悵",
	u"怆": u"愴",
	u"怜": u"憐",
	u"总": u"總",
	u"怼": u"懟",
	u"怿": u"懌",
	u"恋": u"戀",
	u"恳": u"懇",
	u"恶": u"惡",
	u"恸": u"慟",
	u"恹": u"懨",
	u"恺": u"愷",
	u"恻": u"惻",
	u"恼": u"惱",
	u"恽": u"惲",
	u"悦": u"悅",
	u"悫": u"愨",
	u"悬": u"懸",
	u"悭": u"慳",
	u"悯": u"憫",
	u"惊": u"驚",
	u"惧": u"懼",
	u"惨": u"慘",
	u"惩": u"懲",
	u"惫": u"憊",
	u"惬": u"愜",
	u"惭": u"慚",
	u"惮": u"憚",
	u"惯": u"慣",
	u"愍": u"湣",
	u"愠": u"慍",
	u"愤": u"憤",
	u"愦": u"憒",
	u"愿": u"願",
	u"慑": u"懾",
	u"慭": u"憖",
	u"憷": u"怵",
	u"懑": u"懣",
	u"懒": u"懶",
	u"懔": u"懍",
	u"戆": u"戇",
	u"戋": u"戔",
	u"戏": u"戲",
	u"戗": u"戧",
	u"战": u"戰",
	u"戬": u"戩",
	u"户": u"戶",
	u"扎": u"紮",
	u"扑": u"撲",
	u"扦": u"扡",
	u"执": u"執",
	u"扩": u"擴",
	u"扪": u"捫",
	u"扫": u"掃",
	u"扬": u"揚",
	u"扰": u"擾",
	u"抚": u"撫",
	u"抛": u"拋",
	u"抟": u"摶",
	u"抠": u"摳",
	u"抡": u"掄",
	u"抢": u"搶",
	u"护": u"護",
	u"报": u"報",
	u"担": u"擔",
	u"拟": u"擬",
	u"拢": u"攏",
	u"拣": u"揀",
	u"拥": u"擁",
	u"拦": u"攔",
	u"拧": u"擰",
	u"拨": u"撥",
	u"择": u"擇",
	u"挂": u"掛",
	u"挚": u"摯",
	u"挛": u"攣",
	u"挜": u"掗",
	u"挝": u"撾",
	u"挞": u"撻",
	u"挟": u"挾",
	u"挠": u"撓",
	u"挡": u"擋",
	u"挢": u"撟",
	u"挣": u"掙",
	u"挤": u"擠",
	u"挥": u"揮",
	u"挦": u"撏",
	u"捞": u"撈",
	u"损": u"損",
	u"捡": u"撿",
	u"换": u"換",
	u"捣": u"搗",
	u"据": u"據",
	u"捻": u"撚",
	u"掳": u"擄",
	u"掴": u"摑",
	u"掷": u"擲",
	u"掸": u"撣",
	u"掺": u"摻",
	u"掼": u"摜",
	u"揸": u"摣",
	u"揽": u"攬",
	u"揿": u"撳",
	u"搀": u"攙",
	u"搁": u"擱",
	u"搂": u"摟",
	u"搅": u"攪",
	u"携": u"攜",
	u"摄": u"攝",
	u"摅": u"攄",
	u"摆": u"擺",
	u"摇": u"搖",
	u"摈": u"擯",
	u"摊": u"攤",
	u"撄": u"攖",
	u"撑": u"撐",
	u"撵": u"攆",
	u"撷": u"擷",
	u"撸": u"擼",
	u"撺": u"攛",
	u"擞": u"擻",
	u"攒": u"攢",
	u"敌": u"敵",
	u"敛": u"斂",
	u"数": u"數",
	u"斋": u"齋",
	u"斓": u"斕",
	u"斗": u"鬥",
	u"斩": u"斬",
	u"断": u"斷",
	u"无": u"無",
	u"旧": u"舊",
	u"时": u"時",
	u"旷": u"曠",
	u"旸": u"暘",
	u"昙": u"曇",
	u"昼": u"晝",
	u"昽": u"曨",
	u"显": u"顯",
	u"晋": u"晉",
	u"晒": u"曬",
	u"晓": u"曉",
	u"晔": u"曄",
	u"晕": u"暈",
	u"晖": u"暉",
	u"暂": u"暫",
	u"暧": u"曖",
	u"札": u"劄",
	u"术": u"術",
	u"朴": u"樸",
	u"机": u"機",
	u"杀": u"殺",
	u"杂": u"雜",
	u"权": u"權",
	u"条": u"條",
	u"来": u"來",
	u"杨": u"楊",
	u"杩": u"榪",
	u"杰": u"傑",
	u"极": u"極",
	u"构": u"構",
	u"枞": u"樅",
	u"枢": u"樞",
	u"枣": u"棗",
	u"枥": u"櫪",
	u"枧": u"梘",
	u"枨": u"棖",
	u"枪": u"槍",
	u"枫": u"楓",
	u"枭": u"梟",
	u"柜": u"櫃",
	u"柠": u"檸",
	u"柽": u"檉",
	u"栀": u"梔",
	u"栅": u"柵",
	u"标": u"標",
	u"栈": u"棧",
	u"栉": u"櫛",
	u"栊": u"櫳",
	u"栋": u"棟",
	u"栌": u"櫨",
	u"栎": u"櫟",
	u"栏": u"欄",
	u"树": u"樹",
	u"栖": u"棲",
	u"样": u"樣",
	u"栾": u"欒",
	u"桊": u"棬",
	u"桠": u"椏",
	u"桡": u"橈",
	u"桢": u"楨",
	u"档": u"檔",
	u"桤": u"榿",
	u"桥": u"橋",
	u"桦": u"樺",
	u"桧": u"檜",
	u"桨": u"槳",
	u"桩": u"樁",
	u"梦": u"夢",
	u"梼": u"檮",
	u"梾": u"棶",
	u"检": u"檢",
	u"棂": u"欞",
	u"椁": u"槨",
	u"椟": u"櫝",
	u"椠": u"槧",
	u"椤": u"欏",
	u"椭": u"橢",
	u"楼": u"樓",
	u"榄": u"欖",
	u"榇": u"櫬",
	u"榈": u"櫚",
	u"榉": u"櫸",
	u"槚": u"檟",
	u"槛": u"檻",
	u"槟": u"檳",
	u"槠": u"櫧",
	u"横": u"橫",
	u"樯": u"檣",
	u"樱": u"櫻",
	u"橥": u"櫫",
	u"橱": u"櫥",
	u"橹": u"櫓",
	u"橼": u"櫞",
	u"檐": u"簷",
	u"檩": u"檁",
	u"欢": u"歡",
	u"欤": u"歟",
	u"欧": u"歐",
	u"歼": u"殲",
	u"殁": u"歿",
	u"殇": u"殤",
	u"残": u"殘",
	u"殒": u"殞",
	u"殓": u"殮",
	u"殚": u"殫",
	u"殡": u"殯",
	u"殴": u"毆",
	u"毁": u"毀",
	u"毂": u"轂",
	u"毕": u"畢",
	u"毙": u"斃",
	u"毡": u"氈",
	u"毵": u"毿",
	u"氇": u"氌",
	u"气": u"氣",
	u"氢": u"氫",
	u"氩": u"氬",
	u"氲": u"氳",
	u"汇": u"彙",
	u"汉": u"漢",
	u"污": u"汙",
	u"汤": u"湯",
	u"汹": u"洶",
	u"沓": u"遝",
	u"沟": u"溝",
	u"没": u"沒",
	u"沣": u"灃",
	u"沤": u"漚",
	u"沥": u"瀝",
	u"沦": u"淪",
	u"沧": u"滄",
	u"沨": u"渢",
	u"沩": u"溈",
	u"沪": u"滬",
	u"沵": u"濔",
	u"泞": u"濘",
	u"泪": u"淚",
	u"泶": u"澩",
	u"泷": u"瀧",
	u"泸": u"瀘",
	u"泺": u"濼",
	u"泻": u"瀉",
	u"泼": u"潑",
	u"泽": u"澤",
	u"泾": u"涇",
	u"洁": u"潔",
	u"洒": u"灑",
	u"洼": u"窪",
	u"浃": u"浹",
	u"浅": u"淺",
	u"浆": u"漿",
	u"浇": u"澆",
	u"浈": u"湞",
	u"浉": u"溮",
	u"浊": u"濁",
	u"测": u"測",
	u"浍": u"澮",
	u"济": u"濟",
	u"浏": u"瀏",
	u"浐": u"滻",
	u"浑": u"渾",
	u"浒": u"滸",
	u"浓": u"濃",
	u"浔": u"潯",
	u"浕": u"濜",
	u"涂": u"塗",
	u"涌": u"湧",
	u"涛": u"濤",
	u"涝": u"澇",
	u"涞": u"淶",
	u"涟": u"漣",
	u"涠": u"潿",
	u"涡": u"渦",
	u"涢": u"溳",
	u"涣": u"渙",
	u"涤": u"滌",
	u"润": u"潤",
	u"涧": u"澗",
	u"涨": u"漲",
	u"涩": u"澀",
	u"淀": u"澱",
	u"渊": u"淵",
	u"渌": u"淥",
	u"渍": u"漬",
	u"渎": u"瀆",
	u"渐": u"漸",
	u"渑": u"澠",
	u"渔": u"漁",
	u"渖": u"瀋",
	u"渗": u"滲",
	u"温": u"溫",
	u"游": u"遊",
	u"湾": u"灣",
	u"湿": u"濕",
	u"溃": u"潰",
	u"溅": u"濺",
	u"溆": u"漵",
	u"溇": u"漊",
	u"滗": u"潷",
	u"滚": u"滾",
	u"滞": u"滯",
	u"滟": u"灩",
	u"滠": u"灄",
	u"满": u"滿",
	u"滢": u"瀅",
	u"滤": u"濾",
	u"滥": u"濫",
	u"滦": u"灤",
	u"滨": u"濱",
	u"滩": u"灘",
	u"滪": u"澦",
	u"漤": u"濫",
	u"潆": u"瀠",
	u"潇": u"瀟",
	u"潋": u"瀲",
	u"潍": u"濰",
	u"潜": u"潛",
	u"潴": u"瀦",
	u"澜": u"瀾",
	u"濑": u"瀨",
	u"濒": u"瀕",
	u"灏": u"灝",
	u"灭": u"滅",
	u"灯": u"燈",
	u"灵": u"靈",
	u"灾": u"災",
	u"灿": u"燦",
	u"炀": u"煬",
	u"炉": u"爐",
	u"炖": u"燉",
	u"炜": u"煒",
	u"炝": u"熗",
	u"点": u"點",
	u"炼": u"煉",
	u"炽": u"熾",
	u"烁": u"爍",
	u"烂": u"爛",
	u"烃": u"烴",
	u"烛": u"燭",
	u"烟": u"煙",
	u"烦": u"煩",
	u"烧": u"燒",
	u"烨": u"燁",
	u"烩": u"燴",
	u"烫": u"燙",
	u"烬": u"燼",
	u"热": u"熱",
	u"焕": u"煥",
	u"焖": u"燜",
	u"焘": u"燾",
	u"煅": u"煆",
	u"煳": u"糊",
	u"煺": u"退",
	u"熘": u"溜",
	u"爱": u"愛",
	u"爷": u"爺",
	u"牍": u"牘",
	u"牦": u"犛",
	u"牵": u"牽",
	u"牺": u"犧",
	u"犊": u"犢",
	u"犟": u"強",
	u"犭": u"犬",
	u"状": u"狀",
	u"犷": u"獷",
	u"犸": u"獁",
	u"犹": u"猶",
	u"狈": u"狽",
	u"狍": u"麅",
	u"狝": u"獮",
	u"狞": u"獰",
	u"独": u"獨",
	u"狭": u"狹",
	u"狮": u"獅",
	u"狯": u"獪",
	u"狰": u"猙",
	u"狱": u"獄",
	u"狲": u"猻",
	u"猃": u"獫",
	u"猎": u"獵",
	u"猕": u"獼",
	u"猡": u"玀",
	u"猪": u"豬",
	u"猫": u"貓",
	u"猬": u"蝟",
	u"献": u"獻",
	u"獭": u"獺",
	u"玑": u"璣",
	u"玙": u"璵",
	u"玚": u"瑒",
	u"玛": u"瑪",
	u"玮": u"瑋",
	u"环": u"環",
	u"现": u"現",
	u"玱": u"瑲",
	u"玺": u"璽",
	u"珉": u"瑉",
	u"珏": u"玨",
	u"珐": u"琺",
	u"珑": u"瓏",
	u"珰": u"璫",
	u"珲": u"琿",
	u"琎": u"璡",
	u"琏": u"璉",
	u"琐": u"瑣",
	u"琼": u"瓊",
	u"瑶": u"瑤",
	u"瑷": u"璦",
	u"璇": u"璿",
	u"璎": u"瓔",
	u"瓒": u"瓚",
	u"瓮": u"甕",
	u"瓯": u"甌",
	u"电": u"電",
	u"画": u"畫",
	u"畅": u"暢",
	u"畲": u"佘",
	u"畴": u"疇",
	u"疖": u"癤",
	u"疗": u"療",
	u"疟": u"瘧",
	u"疠": u"癘",
	u"疡": u"瘍",
	u"疬": u"鬁",
	u"疮": u"瘡",
	u"疯": u"瘋",
	u"疱": u"皰",
	u"疴": u"屙",
	u"痈": u"癰",
	u"痉": u"痙",
	u"痒": u"癢",
	u"痖": u"瘂",
	u"痨": u"癆",
	u"痪": u"瘓",
	u"痫": u"癇",
	u"痴": u"癡",
	u"瘅": u"癉",
	u"瘆": u"瘮",
	u"瘗": u"瘞",
	u"瘘": u"瘺",
	u"瘪": u"癟",
	u"瘫": u"癱",
	u"瘾": u"癮",
	u"瘿": u"癭",
	u"癞": u"癩",
	u"癣": u"癬",
	u"癫": u"癲",
	u"癯": u"臒",
	u"皑": u"皚",
	u"皱": u"皺",
	u"皲": u"皸",
	u"盏": u"盞",
	u"盐": u"鹽",
	u"监": u"監",
	u"盖": u"蓋",
	u"盗": u"盜",
	u"盘": u"盤",
	u"眍": u"瞘",
	u"眦": u"眥",
	u"眬": u"矓",
	u"着": u"著",
	u"睁": u"睜",
	u"睐": u"睞",
	u"睑": u"瞼",
	u"瞒": u"瞞",
	u"瞩": u"矚",
	u"矫": u"矯",
	u"矶": u"磯",
	u"矾": u"礬",
	u"矿": u"礦",
	u"砀": u"碭",
	u"码": u"碼",
	u"砖": u"磚",
	u"砗": u"硨",
	u"砚": u"硯",
	u"砜": u"碸",
	u"砺": u"礪",
	u"砻": u"礱",
	u"砾": u"礫",
	u"础": u"礎",
	u"硁": u"硜",
	u"硅": u"矽",
	u"硕": u"碩",
	u"硖": u"硤",
	u"硗": u"磽",
	u"硙": u"磑",
	u"硚": u"礄",
	u"确": u"確",
	u"硷": u"鹼",
	u"碍": u"礙",
	u"碛": u"磧",
	u"碜": u"磣",
	u"碱": u"堿",
	u"碹": u"镟",
	u"磙": u"滾",
	u"礼": u"禮",
	u"祎": u"禕",
	u"祢": u"禰",
	u"祯": u"禎",
	u"祷": u"禱",
	u"祸": u"禍",
	u"禀": u"稟",
	u"禄": u"祿",
	u"禅": u"禪",
	u"离": u"離",
	u"秃": u"禿",
	u"秆": u"稈",
	u"种": u"種",
	u"积": u"積",
	u"称": u"稱",
	u"秽": u"穢",
	u"秾": u"穠",
	u"稆": u"穭",
	u"税": u"稅",
	u"稣": u"穌",
	u"稳": u"穩",
	u"穑": u"穡",
	u"穷": u"窮",
	u"窃": u"竊",
	u"窍": u"竅",
	u"窑": u"窯",
	u"窜": u"竄",
	u"窝": u"窩",
	u"窥": u"窺",
	u"窦": u"竇",
	u"窭": u"窶",
	u"竖": u"豎",
	u"竞": u"競",
	u"笃": u"篤",
	u"笋": u"筍",
	u"笔": u"筆",
	u"笕": u"筧",
	u"笺": u"箋",
	u"笼": u"籠",
	u"笾": u"籩",
	u"筑": u"築",
	u"筚": u"篳",
	u"筛": u"篩",
	u"筜": u"簹",
	u"筝": u"箏",
	u"筹": u"籌",
	u"签": u"簽",
	u"简": u"簡",
	u"箓": u"籙",
	u"箦": u"簀",
	u"箧": u"篋",
	u"箨": u"籜",
	u"箩": u"籮",
	u"箪": u"簞",
	u"箫": u"簫",
	u"篑": u"簣",
	u"篓": u"簍",
	u"篮": u"籃",
	u"篱": u"籬",
	u"簖": u"籪",
	u"籁": u"籟",
	u"籴": u"糴",
	u"类": u"類",
	u"籼": u"秈",
	u"粜": u"糶",
	u"粝": u"糲",
	u"粤": u"粵",
	u"粪": u"糞",
	u"粮": u"糧",
	u"糁": u"糝",
	u"糇": u"餱",
	u"紧": u"緊",
	u"絷": u"縶",
	u"纟": u"糸",
	u"纠": u"糾",
	u"纡": u"紆",
	u"红": u"紅",
	u"纣": u"紂",
	u"纤": u"纖",
	u"纥": u"紇",
	u"约": u"約",
	u"级": u"級",
	u"纨": u"紈",
	u"纩": u"纊",
	u"纪": u"紀",
	u"纫": u"紉",
	u"纬": u"緯",
	u"纭": u"紜",
	u"纮": u"紘",
	u"纯": u"純",
	u"纰": u"紕",
	u"纱": u"紗",
	u"纲": u"綱",
	u"纳": u"納",
	u"纴": u"紝",
	u"纵": u"縱",
	u"纶": u"綸",
	u"纷": u"紛",
	u"纸": u"紙",
	u"纹": u"紋",
	u"纺": u"紡",
	u"纻": u"紵",
	u"纼": u"紖",
	u"纽": u"紐",
	u"纾": u"紓",
	u"线": u"線",
	u"绀": u"紺",
	u"绁": u"絏",
	u"绂": u"紱",
	u"练": u"練",
	u"组": u"組",
	u"绅": u"紳",
	u"细": u"細",
	u"织": u"織",
	u"终": u"終",
	u"绉": u"縐",
	u"绊": u"絆",
	u"绋": u"紼",
	u"绌": u"絀",
	u"绍": u"紹",
	u"绎": u"繹",
	u"经": u"經",
	u"绐": u"紿",
	u"绑": u"綁",
	u"绒": u"絨",
	u"结": u"結",
	u"绔": u"絝",
	u"绕": u"繞",
	u"绖": u"絰",
	u"绗": u"絎",
	u"绘": u"繪",
	u"给": u"給",
	u"绚": u"絢",
	u"绛": u"絳",
	u"络": u"絡",
	u"绝": u"絕",
	u"绞": u"絞",
	u"统": u"統",
	u"绠": u"綆",
	u"绡": u"綃",
	u"绢": u"絹",
	u"绣": u"繡",
	u"绤": u"綌",
	u"绥": u"綏",
	u"绦": u"絛",
	u"继": u"繼",
	u"绨": u"綈",
	u"绩": u"績",
	u"绪": u"緒",
	u"绫": u"綾",
	u"绬": u"緓",
	u"续": u"續",
	u"绮": u"綺",
	u"绯": u"緋",
	u"绰": u"綽",
	u"绱": u"緔",
	u"绲": u"緄",
	u"绳": u"繩",
	u"维": u"維",
	u"绵": u"綿",
	u"绶": u"綬",
	u"绷": u"繃",
	u"绸": u"綢",
	u"绹": u"綯",
	u"绺": u"綹",
	u"绻": u"綣",
	u"综": u"綜",
	u"绽": u"綻",
	u"绾": u"綰",
	u"绿": u"綠",
	u"缀": u"綴",
	u"缁": u"緇",
	u"缂": u"緙",
	u"缃": u"緗",
	u"缄": u"緘",
	u"缅": u"緬",
	u"缆": u"纜",
	u"缇": u"緹",
	u"缈": u"緲",
	u"缉": u"緝",
	u"缊": u"縕",
	u"缋": u"繢",
	u"缌": u"緦",
	u"缍": u"綞",
	u"缎": u"緞",
	u"缏": u"緶",
	u"缐": u"線",
	u"缑": u"緱",
	u"缒": u"縋",
	u"缓": u"緩",
	u"缔": u"締",
	u"缕": u"縷",
	u"编": u"編",
	u"缗": u"緡",
	u"缘": u"緣",
	u"缙": u"縉",
	u"缚": u"縛",
	u"缛": u"縟",
	u"缜": u"縝",
	u"缝": u"縫",
	u"缞": u"縗",
	u"缟": u"縞",
	u"缠": u"纏",
	u"缡": u"縭",
	u"缢": u"縊",
	u"缣": u"縑",
	u"缤": u"繽",
	u"缥": u"縹",
	u"缦": u"縵",
	u"缧": u"縲",
	u"缨": u"纓",
	u"缩": u"縮",
	u"缪": u"繆",
	u"缫": u"繅",
	u"缬": u"纈",
	u"缭": u"繚",
	u"缮": u"繕",
	u"缯": u"繒",
	u"缰": u"韁",
	u"缱": u"繾",
	u"缲": u"繰",
	u"缳": u"繯",
	u"缴": u"繳",
	u"缵": u"纘",
	u"罂": u"罌",
	u"网": u"網",
	u"罗": u"羅",
	u"罚": u"罰",
	u"罢": u"罷",
	u"罴": u"羆",
	u"羁": u"羈",
	u"羟": u"羥",
	u"羡": u"羨",
	u"翘": u"翹",
	u"翙": u"翽",
	u"翚": u"翬",
	u"耢": u"耮",
	u"耧": u"耬",
	u"耸": u"聳",
	u"耻": u"恥",
	u"聂": u"聶",
	u"聋": u"聾",
	u"职": u"職",
	u"聍": u"聹",
	u"联": u"聯",
	u"聩": u"聵",
	u"聪": u"聰",
	u"肃": u"肅",
	u"肠": u"腸",
	u"肤": u"膚",
	u"肷": u"膁",
	u"肾": u"腎",
	u"肿": u"腫",
	u"胀": u"脹",
	u"胁": u"脅",
	u"胆": u"膽",
	u"胜": u"勝",
	u"胧": u"朧",
	u"胨": u"腖",
	u"胪": u"臚",
	u"胫": u"脛",
	u"胶": u"膠",
	u"脉": u"脈",
	u"脍": u"膾",
	u"脏": u"髒",
	u"脐": u"臍",
	u"脑": u"腦",
	u"脓": u"膿",
	u"脔": u"臠",
	u"脚": u"腳",
	u"脱": u"脫",
	u"脶": u"腡",
	u"脸": u"臉",
	u"腊": u"臘",
	u"腌": u"醃",
	u"腘": u"膕",
	u"腭": u"齶",
	u"腻": u"膩",
	u"腼": u"靦",
	u"腽": u"膃",
	u"腾": u"騰",
	u"膑": u"臏",
	u"臜": u"臢",
	u"舆": u"輿",
	u"舣": u"艤",
	u"舰": u"艦",
	u"舱": u"艙",
	u"舻": u"艫",
	u"艰": u"艱",
	u"艳": u"豔",
	u"艹": u"艸",
	u"艺": u"藝",
	u"节": u"節",
	u"芈": u"羋",
	u"芗": u"薌",
	u"芜": u"蕪",
	u"芦": u"蘆",
	u"苁": u"蓯",
	u"苇": u"葦",
	u"苈": u"藶",
	u"苋": u"莧",
	u"苌": u"萇",
	u"苍": u"蒼",
	u"苎": u"苧",
	u"苏": u"蘇",
	u"苘": u"檾",
	u"苹": u"蘋",
	u"茎": u"莖",
	u"茏": u"蘢",
	u"茑": u"蔦",
	u"茔": u"塋",
	u"茕": u"煢",
	u"茧": u"繭",
	u"荆": u"荊",
	u"荐": u"薦",
	u"荙": u"薘",
	u"荚": u"莢",
	u"荛": u"蕘",
	u"荜": u"蓽",
	u"荞": u"蕎",
	u"荟": u"薈",
	u"荠": u"薺",
	u"荡": u"蕩",
	u"荣": u"榮",
	u"荤": u"葷",
	u"荥": u"滎",
	u"荦": u"犖",
	u"荧": u"熒",
	u"荨": u"蕁",
	u"荩": u"藎",
	u"荪": u"蓀",
	u"荫": u"蔭",
	u"荬": u"蕒",
	u"荭": u"葒",
	u"荮": u"葤",
	u"药": u"藥",
	u"莅": u"蒞",
	u"莜": u"蓧",
	u"莱": u"萊",
	u"莲": u"蓮",
	u"莳": u"蒔",
	u"莴": u"萵",
	u"莶": u"薟",
	u"获": u"獲",
	u"莸": u"蕕",
	u"莹": u"瑩",
	u"莺": u"鶯",
	u"莼": u"蓴",
	u"萚": u"蘀",
	u"萝": u"蘿",
	u"萤": u"螢",
	u"营": u"營",
	u"萦": u"縈",
	u"萧": u"蕭",
	u"萨": u"薩",
	u"葱": u"蔥",
	u"蒇": u"蕆",
	u"蒉": u"蕢",
	u"蒋": u"蔣",
	u"蒌": u"蔞",
	u"蓝": u"藍",
	u"蓟": u"薊",
	u"蓠": u"蘺",
	u"蓣": u"蕷",
	u"蓥": u"鎣",
	u"蓦": u"驀",
	u"蔷": u"薔",
	u"蔹": u"蘞",
	u"蔺": u"藺",
	u"蔼": u"藹",
	u"蕲": u"蘄",
	u"蕴": u"蘊",
	u"薮": u"藪",
	u"藁": u"槁",
	u"藓": u"蘚",
	u"虏": u"虜",
	u"虑": u"慮",
	u"虚": u"虛",
	u"虫": u"蟲",
	u"虬": u"虯",
	u"虮": u"蟣",
	u"虽": u"雖",
	u"虾": u"蝦",
	u"虿": u"蠆",
	u"蚀": u"蝕",
	u"蚁": u"蟻",
	u"蚂": u"螞",
	u"蚕": u"蠶",
	u"蚝": u"蠔",
	u"蚬": u"蜆",
	u"蛊": u"蠱",
	u"蛎": u"蠣",
	u"蛏": u"蟶",
	u"蛮": u"蠻",
	u"蛰": u"蟄",
	u"蛱": u"蛺",
	u"蛲": u"蟯",
	u"蛳": u"螄",
	u"蛴": u"蠐",
	u"蜕": u"蛻",
	u"蜗": u"蝸",
	u"蜡": u"蠟",
	u"蝇": u"蠅",
	u"蝈": u"蟈",
	u"蝉": u"蟬",
	u"蝎": u"蠍",
	u"蝼": u"螻",
	u"蝾": u"蠑",
	u"螀": u"螿",
	u"螨": u"蟎",
	u"蟏": u"蠨",
	u"衅": u"釁",
	u"衔": u"銜",
	u"补": u"補",
	u"衬": u"襯",
	u"衮": u"袞",
	u"袄": u"襖",
	u"袅": u"嫋",
	u"袆": u"褘",
	u"袜": u"襪",
	u"袭": u"襲",
	u"袯": u"襏",
	u"装": u"裝",
	u"裆": u"襠",
	u"裈": u"褌",
	u"裢": u"褳",
	u"裣": u"襝",
	u"裤": u"褲",
	u"裥": u"襇",
	u"褛": u"褸",
	u"褴": u"襤",
	u"襁": u"繈",
	u"襕": u"襴",
	u"见": u"見",
	u"观": u"觀",
	u"觃": u"覎",
	u"规": u"規",
	u"觅": u"覓",
	u"视": u"視",
	u"觇": u"覘",
	u"览": u"覽",
	u"觉": u"覺",
	u"觊": u"覬",
	u"觋": u"覡",
	u"觌": u"覿",
	u"觍": u"覥",
	u"觎": u"覦",
	u"觏": u"覯",
	u"觐": u"覲",
	u"觑": u"覷",
	u"觞": u"觴",
	u"触": u"觸",
	u"觯": u"觶",
	u"詟": u"讋",
	u"誉": u"譽",
	u"誊": u"謄",
	u"讠": u"訁",
	u"计": u"計",
	u"订": u"訂",
	u"讣": u"訃",
	u"认": u"認",
	u"讥": u"譏",
	u"讦": u"訐",
	u"讧": u"訌",
	u"讨": u"討",
	u"让": u"讓",
	u"讪": u"訕",
	u"讫": u"訖",
	u"训": u"訓",
	u"议": u"議",
	u"讯": u"訊",
	u"记": u"記",
	u"讱": u"訒",
	u"讲": u"講",
	u"讳": u"諱",
	u"讴": u"謳",
	u"讵": u"詎",
	u"讶": u"訝",
	u"讷": u"訥",
	u"许": u"許",
	u"讹": u"訛",
	u"论": u"論",
	u"讻": u"訩",
	u"讼": u"訟",
	u"讽": u"諷",
	u"设": u"設",
	u"访": u"訪",
	u"诀": u"訣",
	u"证": u"證",
	u"诂": u"詁",
	u"诃": u"訶",
	u"评": u"評",
	u"诅": u"詛",
	u"识": u"識",
	u"诇": u"詗",
	u"诈": u"詐",
	u"诉": u"訴",
	u"诊": u"診",
	u"诋": u"詆",
	u"诌": u"謅",
	u"词": u"詞",
	u"诎": u"詘",
	u"诏": u"詔",
	u"诐": u"詖",
	u"译": u"譯",
	u"诒": u"詒",
	u"诓": u"誆",
	u"诔": u"誄",
	u"试": u"試",
	u"诖": u"詿",
	u"诗": u"詩",
	u"诘": u"詰",
	u"诙": u"詼",
	u"诚": u"誠",
	u"诛": u"誅",
	u"诜": u"詵",
	u"话": u"話",
	u"诞": u"誕",
	u"诟": u"詬",
	u"诠": u"詮",
	u"诡": u"詭",
	u"询": u"詢",
	u"诣": u"詣",
	u"诤": u"諍",
	u"该": u"該",
	u"详": u"詳",
	u"诧": u"詫",
	u"诨": u"諢",
	u"诩": u"詡",
	u"诪": u"譸",
	u"诫": u"誡",
	u"诬": u"誣",
	u"语": u"語",
	u"诮": u"誚",
	u"误": u"誤",
	u"诰": u"誥",
	u"诱": u"誘",
	u"诲": u"誨",
	u"诳": u"誑",
	u"说": u"說",
	u"诵": u"誦",
	u"诶": u"誒",
	u"请": u"請",
	u"诸": u"諸",
	u"诹": u"諏",
	u"诺": u"諾",
	u"读": u"讀",
	u"诼": u"諑",
	u"诽": u"誹",
	u"课": u"課",
	u"诿": u"諉",
	u"谀": u"諛",
	u"谁": u"誰",
	u"谂": u"諗",
	u"调": u"調",
	u"谄": u"諂",
	u"谅": u"諒",
	u"谆": u"諄",
	u"谇": u"誶",
	u"谈": u"談",
	u"谊": u"誼",
	u"谋": u"謀",
	u"谌": u"諶",
	u"谍": u"諜",
	u"谎": u"謊",
	u"谏": u"諫",
	u"谐": u"諧",
	u"谑": u"謔",
	u"谒": u"謁",
	u"谓": u"謂",
	u"谔": u"諤",
	u"谕": u"諭",
	u"谖": u"諼",
	u"谗": u"讒",
	u"谘": u"諮",
	u"谙": u"諳",
	u"谚": u"諺",
	u"谛": u"諦",
	u"谜": u"謎",
	u"谝": u"諞",
	u"谞": u"諝",
	u"谟": u"謨",
	u"谠": u"讜",
	u"谡": u"謖",
	u"谢": u"謝",
	u"谣": u"謠",
	u"谤": u"謗",
	u"谥": u"諡",
	u"谦": u"謙",
	u"谧": u"謐",
	u"谨": u"謹",
	u"谩": u"謾",
	u"谪": u"謫",
	u"谫": u"譾",
	u"谬": u"謬",
	u"谭": u"譚",
	u"谮": u"譖",
	u"谯": u"譙",
	u"谰": u"讕",
	u"谱": u"譜",
	u"谲": u"譎",
	u"谳": u"讞",
	u"谴": u"譴",
	u"谵": u"譫",
	u"谶": u"讖",
	u"谷": u"穀",
	u"豮": u"豶",
	u"贝": u"貝",
	u"贞": u"貞",
	u"负": u"負",
	u"贠": u"貟",
	u"贡": u"貢",
	u"财": u"財",
	u"责": u"責",
	u"贤": u"賢",
	u"败": u"敗",
	u"账": u"賬",
	u"货": u"貨",
	u"质": u"質",
	u"贩": u"販",
	u"贪": u"貪",
	u"贫": u"貧",
	u"贬": u"貶",
	u"购": u"購",
	u"贮": u"貯",
	u"贯": u"貫",
	u"贰": u"貳",
	u"贱": u"賤",
	u"贲": u"賁",
	u"贳": u"貰",
	u"贴": u"貼",
	u"贵": u"貴",
	u"贶": u"貺",
	u"贷": u"貸",
	u"贸": u"貿",
	u"费": u"費",
	u"贺": u"賀",
	u"贻": u"貽",
	u"贼": u"賊",
	u"贽": u"贄",
	u"贾": u"賈",
	u"贿": u"賄",
	u"赀": u"貲",
	u"赁": u"賃",
	u"赂": u"賂",
	u"赃": u"贓",
	u"资": u"資",
	u"赅": u"賅",
	u"赆": u"贐",
	u"赇": u"賕",
	u"赈": u"賑",
	u"赉": u"賚",
	u"赊": u"賒",
	u"赋": u"賦",
	u"赌": u"賭",
	u"赍": u"齎",
	u"赎": u"贖",
	u"赏": u"賞",
	u"赐": u"賜",
	u"赑": u"贔",
	u"赒": u"賙",
	u"赓": u"賡",
	u"赔": u"賠",
	u"赕": u"賧",
	u"赖": u"賴",
	u"赗": u"賵",
	u"赘": u"贅",
	u"赙": u"賻",
	u"赚": u"賺",
	u"赛": u"賽",
	u"赜": u"賾",
	u"赝": u"贗",
	u"赞": u"贊",
	u"赟": u"贇",
	u"赠": u"贈",
	u"赡": u"贍",
	u"赢": u"贏",
	u"赣": u"贛",
	u"赪": u"赬",
	u"赵": u"趙",
	u"赶": u"趕",
	u"趋": u"趨",
	u"趱": u"趲",
	u"趸": u"躉",
	u"跃": u"躍",
	u"跄": u"蹌",
	u"跖": u"蹠",
	u"跞": u"躒",
	u"践": u"踐",
	u"跶": u"躂",
	u"跷": u"蹺",
	u"跸": u"蹕",
	u"跹": u"躚",
	u"跻": u"躋",
	u"踊": u"踴",
	u"踌": u"躊",
	u"踪": u"蹤",
	u"踬": u"躓",
	u"踯": u"躑",
	u"蹑": u"躡",
	u"蹒": u"蹣",
	u"蹰": u"躕",
	u"蹿": u"躥",
	u"躏": u"躪",
	u"躜": u"躦",
	u"躯": u"軀",
	u"车": u"車",
	u"轧": u"軋",
	u"轨": u"軌",
	u"轩": u"軒",
	u"轪": u"軑",
	u"轫": u"軔",
	u"转": u"轉",
	u"轭": u"軛",
	u"轮": u"輪",
	u"软": u"軟",
	u"轰": u"轟",
	u"轱": u"軲",
	u"轲": u"軻",
	u"轳": u"轤",
	u"轴": u"軸",
	u"轵": u"軹",
	u"轶": u"軼",
	u"轷": u"軤",
	u"轸": u"軫",
	u"轹": u"轢",
	u"轺": u"軺",
	u"轻": u"輕",
	u"轼": u"軾",
	u"载": u"載",
	u"轾": u"輊",
	u"轿": u"轎",
	u"辀": u"輈",
	u"辁": u"輇",
	u"辂": u"輅",
	u"较": u"較",
	u"辄": u"輒",
	u"辅": u"輔",
	u"辆": u"輛",
	u"辇": u"輦",
	u"辈": u"輩",
	u"辉": u"輝",
	u"辊": u"輥",
	u"辋": u"輞",
	u"辌": u"輬",
	u"辍": u"輟",
	u"辎": u"輜",
	u"辏": u"輳",
	u"辐": u"輻",
	u"辑": u"輯",
	u"辒": u"轀",
	u"输": u"輸",
	u"辔": u"轡",
	u"辕": u"轅",
	u"辖": u"轄",
	u"辗": u"輾",
	u"辘": u"轆",
	u"辙": u"轍",
	u"辚": u"轔",
	u"辞": u"辭",
	u"辩": u"辯",
	u"辫": u"辮",
	u"边": u"邊",
	u"辽": u"遼",
	u"达": u"達",
	u"迁": u"遷",
	u"过": u"過",
	u"迈": u"邁",
	u"运": u"運",
	u"还": u"還",
	u"这": u"這",
	u"进": u"進",
	u"远": u"遠",
	u"违": u"違",
	u"连": u"連",
	u"迟": u"遲",
	u"迩": u"邇",
	u"迳": u"逕",
	u"迹": u"跡",
	u"适": u"適",
	u"选": u"選",
	u"逊": u"遜",
	u"递": u"遞",
	u"逦": u"邐",
	u"逻": u"邏",
	u"遗": u"遺",
	u"遥": u"遙",
	u"邓": u"鄧",
	u"邝": u"鄺",
	u"邬": u"鄔",
	u"邮": u"郵",
	u"邹": u"鄒",
	u"邺": u"鄴",
	u"邻": u"鄰",
	u"郁": u"鬱",
	u"郄": u"郤",
	u"郏": u"郟",
	u"郐": u"鄶",
	u"郑": u"鄭",
	u"郓": u"鄆",
	u"郦": u"酈",
	u"郧": u"鄖",
	u"郸": u"鄲",
	u"酝": u"醞",
	u"酦": u"醱",
	u"酱": u"醬",
	u"酽": u"釅",
	u"酾": u"釃",
	u"酿": u"釀",
	u"释": u"釋",
	u"里": u"裏",
	u"鉅": u"钜",
	u"鉴": u"鑒",
	u"銮": u"鑾",
	u"錾": u"鏨",
	u"钆": u"釓",
	u"钇": u"釔",
	u"针": u"針",
	u"钉": u"釘",
	u"钊": u"釗",
	u"钋": u"釙",
	u"钌": u"釕",
	u"钍": u"釷",
	u"钎": u"釺",
	u"钏": u"釧",
	u"钐": u"釤",
	u"钑": u"鈒",
	u"钒": u"釩",
	u"钓": u"釣",
	u"钔": u"鍆",
	u"钕": u"釹",
	u"钖": u"鍚",
	u"钗": u"釵",
	u"钘": u"鈃",
	u"钙": u"鈣",
	u"钚": u"鈈",
	u"钛": u"鈦",
	u"钝": u"鈍",
	u"钞": u"鈔",
	u"钟": u"鍾",
	u"钠": u"鈉",
	u"钡": u"鋇",
	u"钢": u"鋼",
	u"钣": u"鈑",
	u"钤": u"鈐",
	u"钥": u"鑰",
	u"钦": u"欽",
	u"钧": u"鈞",
	u"钨": u"鎢",
	u"钩": u"鉤",
	u"钪": u"鈧",
	u"钫": u"鈁",
	u"钬": u"鈥",
	u"钭": u"鈄",
	u"钮": u"鈕",
	u"钯": u"鈀",
	u"钰": u"鈺",
	u"钱": u"錢",
	u"钲": u"鉦",
	u"钳": u"鉗",
	u"钴": u"鈷",
	u"钵": u"缽",
	u"钶": u"鈳",
	u"钷": u"鉕",
	u"钸": u"鈽",
	u"钹": u"鈸",
	u"钺": u"鉞",
	u"钻": u"鑽",
	u"钼": u"鉬",
	u"钽": u"鉭",
	u"钾": u"鉀",
	u"钿": u"鈿",
	u"铀": u"鈾",
	u"铁": u"鐵",
	u"铂": u"鉑",
	u"铃": u"鈴",
	u"铄": u"鑠",
	u"铅": u"鉛",
	u"铆": u"鉚",
	u"铈": u"鈰",
	u"铉": u"鉉",
	u"铊": u"鉈",
	u"铋": u"鉍",
	u"铌": u"鈮",
	u"铍": u"鈹",
	u"铎": u"鐸",
	u"铏": u"鉶",
	u"铐": u"銬",
	u"铑": u"銠",
	u"铒": u"鉺",
	u"铓": u"鋩",
	u"铔": u"錏",
	u"铕": u"銪",
	u"铖": u"鋮",
	u"铗": u"鋏",
	u"铘": u"鋣",
	u"铙": u"鐃",
	u"铚": u"銍",
	u"铛": u"鐺",
	u"铜": u"銅",
	u"铝": u"鋁",
	u"铞": u"銱",
	u"铟": u"銦",
	u"铠": u"鎧",
	u"铡": u"鍘",
	u"铢": u"銖",
	u"铣": u"銑",
	u"铤": u"鋌",
	u"铥": u"銩",
	u"铦": u"銛",
	u"铧": u"鏵",
	u"铨": u"銓",
	u"铩": u"鎩",
	u"铪": u"鉿",
	u"铫": u"銚",
	u"铬": u"鉻",
	u"铭": u"銘",
	u"铮": u"錚",
	u"铯": u"銫",
	u"铰": u"鉸",
	u"铱": u"銥",
	u"铲": u"鏟",
	u"铳": u"銃",
	u"铴": u"鐋",
	u"铵": u"銨",
	u"银": u"銀",
	u"铷": u"銣",
	u"铸": u"鑄",
	u"铹": u"鐒",
	u"铺": u"鋪",
	u"铻": u"鋙",
	u"铼": u"錸",
	u"铽": u"鋱",
	u"链": u"鏈",
	u"铿": u"鏗",
	u"销": u"銷",
	u"锁": u"鎖",
	u"锂": u"鋰",
	u"锃": u"鋥",
	u"锄": u"鋤",
	u"锅": u"鍋",
	u"锆": u"鋯",
	u"锇": u"鋨",
	u"锈": u"鏽",
	u"锉": u"銼",
	u"锊": u"鋝",
	u"锋": u"鋒",
	u"锌": u"鋅",
	u"锍": u"鋶",
	u"锎": u"鐦",
	u"锏": u"鐧",
	u"锐": u"銳",
	u"锑": u"銻",
	u"锒": u"鋃",
	u"锓": u"鋟",
	u"锔": u"鋦",
	u"锕": u"錒",
	u"锖": u"錆",
	u"锗": u"鍺",
	u"锘": u"鍩",
	u"错": u"錯",
	u"锚": u"錨",
	u"锛": u"錛",
	u"锜": u"錡",
	u"锝": u"鍀",
	u"锞": u"錁",
	u"锟": u"錕",
	u"锠": u"錩",
	u"锡": u"錫",
	u"锢": u"錮",
	u"锣": u"鑼",
	u"锤": u"錘",
	u"锥": u"錐",
	u"锦": u"錦",
	u"锧": u"鑕",
	u"锨": u"鍁",
	u"锩": u"錈",
	u"锪": u"鍃",
	u"锫": u"錇",
	u"锬": u"錟",
	u"锭": u"錠",
	u"键": u"鍵",
	u"锯": u"鋸",
	u"锰": u"錳",
	u"锱": u"錙",
	u"锲": u"鍥",
	u"锳": u"鍈",
	u"锴": u"鍇",
	u"锵": u"鏘",
	u"锶": u"鍶",
	u"锷": u"鍔",
	u"锸": u"鍤",
	u"锹": u"鍬",
	u"锺": u"鍾",
	u"锻": u"鍛",
	u"锼": u"鎪",
	u"锽": u"鍠",
	u"锾": u"鍰",
	u"锿": u"鎄",
	u"镀": u"鍍",
	u"镁": u"鎂",
	u"镂": u"鏤",
	u"镃": u"鎡",
	u"镄": u"鐨",
	u"镅": u"鎇",
	u"镆": u"鏌",
	u"镇": u"鎮",
	u"镈": u"鎛",
	u"镉": u"鎘",
	u"镊": u"鑷",
	u"镋": u"钂",
	u"镌": u"鐫",
	u"镍": u"鎳",
	u"镎": u"鎿",
	u"镏": u"鎦",
	u"镐": u"鎬",
	u"镑": u"鎊",
	u"镒": u"鎰",
	u"镓": u"鎵",
	u"镔": u"鑌",
	u"镕": u"鎔",
	u"镖": u"鏢",
	u"镗": u"鏜",
	u"镘": u"鏝",
	u"镙": u"鏍",
	u"镚": u"鏰",
	u"镛": u"鏞",
	u"镜": u"鏡",
	u"镝": u"鏑",
	u"镞": u"鏃",
	u"镟": u"鏇",
	u"镠": u"鏐",
	u"镡": u"鐔",
	u"镢": u"钁",
	u"镣": u"鐐",
	u"镤": u"鏷",
	u"镥": u"鑥",
	u"镦": u"鐓",
	u"镧": u"鑭",
	u"镨": u"鐠",
	u"镩": u"鑹",
	u"镪": u"鏹",
	u"镫": u"鐙",
	u"镬": u"鑊",
	u"镭": u"鐳",
	u"镮": u"鐶",
	u"镯": u"鐲",
	u"镰": u"鐮",
	u"镱": u"鐿",
	u"镲": u"鑔",
	u"镳": u"鑣",
	u"镴": u"鑞",
	u"镵": u"鑱",
	u"镶": u"鑲",
	u"长": u"長",
	u"门": u"門",
	u"闩": u"閂",
	u"闪": u"閃",
	u"闫": u"閆",
	u"闬": u"閈",
	u"闭": u"閉",
	u"问": u"問",
	u"闯": u"闖",
	u"闰": u"閏",
	u"闱": u"闈",
	u"闲": u"閑",
	u"闳": u"閎",
	u"间": u"間",
	u"闵": u"閔",
	u"闶": u"閌",
	u"闷": u"悶",
	u"闸": u"閘",
	u"闹": u"鬧",
	u"闺": u"閨",
	u"闻": u"聞",
	u"闼": u"闥",
	u"闽": u"閩",
	u"闾": u"閭",
	u"闿": u"闓",
	u"阀": u"閥",
	u"阁": u"閣",
	u"阂": u"閡",
	u"阃": u"閫",
	u"阄": u"鬮",
	u"阅": u"閱",
	u"阆": u"閬",
	u"阇": u"闍",
	u"阈": u"閾",
	u"阉": u"閹",
	u"阊": u"閶",
	u"阋": u"鬩",
	u"阌": u"閿",
	u"阍": u"閽",
	u"阎": u"閻",
	u"阏": u"閼",
	u"阐": u"闡",
	u"阑": u"闌",
	u"阒": u"闃",
	u"阓": u"闠",
	u"阔": u"闊",
	u"阕": u"闋",
	u"阖": u"闔",
	u"阗": u"闐",
	u"阘": u"闒",
	u"阙": u"闕",
	u"阚": u"闞",
	u"阛": u"闤",
	u"队": u"隊",
	u"阳": u"陽",
	u"阴": u"陰",
	u"阵": u"陣",
	u"阶": u"階",
	u"际": u"際",
	u"陆": u"陸",
	u"陇": u"隴",
	u"陈": u"陳",
	u"陉": u"陘",
	u"陕": u"陝",
	u"陧": u"隉",
	u"陨": u"隕",
	u"险": u"險",
	u"随": u"隨",
	u"隐": u"隱",
	u"隶": u"隸",
	u"隽": u"雋",
	u"难": u"難",
	u"雏": u"雛",
	u"雠": u"讎",
	u"雳": u"靂",
	u"雾": u"霧",
	u"霁": u"霽",
	u"霉": u"黴",
	u"霭": u"靄",
	u"靓": u"靚",
	u"静": u"靜",
	u"靥": u"靨",
	u"鞑": u"韃",
	u"鞒": u"鞽",
	u"鞯": u"韉",
	u"鞴": u"韝",
	u"韦": u"韋",
	u"韧": u"韌",
	u"韨": u"韍",
	u"韩": u"韓",
	u"韪": u"韙",
	u"韫": u"韞",
	u"韬": u"韜",
	u"韵": u"韻",
	u"页": u"頁",
	u"顶": u"頂",
	u"顷": u"頃",
	u"顸": u"頇",
	u"项": u"項",
	u"顺": u"順",
	u"须": u"須",
	u"顼": u"頊",
	u"顽": u"頑",
	u"顾": u"顧",
	u"顿": u"頓",
	u"颀": u"頎",
	u"颁": u"頒",
	u"颂": u"頌",
	u"颃": u"頏",
	u"预": u"預",
	u"颅": u"顱",
	u"领": u"領",
	u"颇": u"頗",
	u"颈": u"頸",
	u"颉": u"頡",
	u"颊": u"頰",
	u"颋": u"頲",
	u"颌": u"頜",
	u"颍": u"潁",
	u"颎": u"熲",
	u"颏": u"頦",
	u"颐": u"頤",
	u"频": u"頻",
	u"颒": u"頮",
	u"颓": u"頹",
	u"颔": u"頷",
	u"颕": u"頴",
	u"颖": u"穎",
	u"颗": u"顆",
	u"题": u"題",
	u"颙": u"顒",
	u"颚": u"顎",
	u"颛": u"顓",
	u"颜": u"顏",
	u"额": u"額",
	u"颞": u"顳",
	u"颟": u"顢",
	u"颠": u"顛",
	u"颡": u"顙",
	u"颢": u"顥",
	u"颣": u"纇",
	u"颤": u"顫",
	u"颥": u"顬",
	u"颦": u"顰",
	u"颧": u"顴",
	u"风": u"風",
	u"飏": u"颺",
	u"飐": u"颭",
	u"飑": u"颮",
	u"飒": u"颯",
	u"飓": u"颶",
	u"飔": u"颸",
	u"飕": u"颼",
	u"飖": u"颻",
	u"飗": u"飀",
	u"飘": u"飄",
	u"飙": u"飆",
	u"飚": u"飆",
	u"飞": u"飛",
	u"飨": u"饗",
	u"餍": u"饜",
	u"饤": u"飣",
	u"饥": u"饑",
	u"饦": u"飥",
	u"饧": u"餳",
	u"饨": u"飩",
	u"饩": u"餼",
	u"饪": u"飪",
	u"饫": u"飫",
	u"饬": u"飭",
	u"饭": u"飯",
	u"饮": u"飲",
	u"饯": u"餞",
	u"饰": u"飾",
	u"饱": u"飽",
	u"饲": u"飼",
	u"饳": u"飿",
	u"饴": u"飴",
	u"饵": u"餌",
	u"饶": u"饒",
	u"饷": u"餉",
	u"饸": u"餄",
	u"饹": u"餎",
	u"饺": u"餃",
	u"饻": u"餏",
	u"饼": u"餅",
	u"饽": u"餑",
	u"饾": u"餖",
	u"饿": u"餓",
	u"馀": u"餘",
	u"馁": u"餒",
	u"馂": u"餕",
	u"馃": u"餜",
	u"馄": u"餛",
	u"馅": u"餡",
	u"馆": u"館",
	u"馇": u"餷",
	u"馈": u"饋",
	u"馉": u"餶",
	u"馊": u"餿",
	u"馋": u"饞",
	u"馌": u"饁",
	u"馍": u"饃",
	u"馎": u"餺",
	u"馏": u"餾",
	u"馐": u"饈",
	u"馑": u"饉",
	u"馒": u"饅",
	u"馓": u"饊",
	u"馔": u"饌",
	u"馕": u"饢",
	u"马": u"馬",
	u"驭": u"馭",
	u"驮": u"馱",
	u"驯": u"馴",
	u"驰": u"馳",
	u"驱": u"驅",
	u"驲": u"馹",
	u"驳": u"駁",
	u"驴": u"驢",
	u"驵": u"駔",
	u"驶": u"駛",
	u"驷": u"駟",
	u"驸": u"駙",
	u"驹": u"駒",
	u"驺": u"騶",
	u"驻": u"駐",
	u"驼": u"駝",
	u"驽": u"駑",
	u"驾": u"駕",
	u"驿": u"驛",
	u"骀": u"駘",
	u"骁": u"驍",
	u"骂": u"罵",
	u"骃": u"駰",
	u"骄": u"驕",
	u"骅": u"驊",
	u"骆": u"駱",
	u"骇": u"駭",
	u"骈": u"駢",
	u"骉": u"驫",
	u"骊": u"驪",
	u"骋": u"騁",
	u"验": u"驗",
	u"骍": u"騂",
	u"骎": u"駸",
	u"骏": u"駿",
	u"骐": u"騏",
	u"骑": u"騎",
	u"骒": u"騍",
	u"骓": u"騅",
	u"骔": u"騌",
	u"骕": u"驌",
	u"骖": u"驂",
	u"骗": u"騙",
	u"骘": u"騭",
	u"骙": u"騤",
	u"骚": u"騷",
	u"骛": u"騖",
	u"骜": u"驁",
	u"骝": u"騮",
	u"骞": u"騫",
	u"骟": u"騸",
	u"骠": u"驃",
	u"骡": u"騾",
	u"骢": u"驄",
	u"骣": u"驏",
	u"骤": u"驟",
	u"骥": u"驥",
	u"骦": u"驦",
	u"骧": u"驤",
	u"髅": u"髏",
	u"髋": u"髖",
	u"髌": u"髕",
	u"鬓": u"鬢",
	u"魇": u"魘",
	u"魉": u"魎",
	u"鱼": u"魚",
	u"鱽": u"魛",
	u"鱾": u"魢",
	u"鱿": u"魷",
	u"鲀": u"魨",
	u"鲁": u"魯",
	u"鲂": u"魴",
	u"鲄": u"魺",
	u"鲅": u"鮁",
	u"鲆": u"鮃",
	u"鲇": u"鯰",
	u"鲈": u"鱸",
	u"鲉": u"鮋",
	u"鲊": u"鮓",
	u"鲋": u"鮒",
	u"鲌": u"鮊",
	u"鲍": u"鮑",
	u"鲎": u"鱟",
	u"鲏": u"鮍",
	u"鲐": u"鮐",
	u"鲑": u"鮭",
	u"鲒": u"鮚",
	u"鲓": u"鮳",
	u"鲔": u"鮪",
	u"鲕": u"鮞",
	u"鲖": u"鮦",
	u"鲗": u"鰂",
	u"鲘": u"鮜",
	u"鲙": u"鱠",
	u"鲚": u"鱭",
	u"鲛": u"鮫",
	u"鲜": u"鮮",
	u"鲝": u"鮺",
	u"鲞": u"鯗",
	u"鲟": u"鱘",
	u"鲠": u"鯁",
	u"鲡": u"鱺",
	u"鲢": u"鰱",
	u"鲣": u"鰹",
	u"鲤": u"鯉",
	u"鲥": u"鰣",
	u"鲦": u"鰷",
	u"鲧": u"鯀",
	u"鲨": u"鯊",
	u"鲩": u"鯇",
	u"鲪": u"鮶",
	u"鲫": u"鯽",
	u"鲬": u"鯒",
	u"鲭": u"鯖",
	u"鲮": u"鯪",
	u"鲯": u"鯕",
	u"鲰": u"鯫",
	u"鲱": u"鯡",
	u"鲲": u"鯤",
	u"鲳": u"鯧",
	u"鲴": u"鯝",
	u"鲵": u"鯢",
	u"鲶": u"鯰",
	u"鲷": u"鯛",
	u"鲸": u"鯨",
	u"鲹": u"鯵",
	u"鲺": u"鯴",
	u"鲻": u"鯔",
	u"鲼": u"鱝",
	u"鲽": u"鰈",
	u"鲾": u"鰏",
	u"鲿": u"鱨",
	u"鳀": u"鯷",
	u"鳁": u"鰮",
	u"鳂": u"鰃",
	u"鳃": u"鰓",
	u"鳄": u"鱷",
	u"鳅": u"鰍",
	u"鳆": u"鰒",
	u"鳇": u"鰉",
	u"鳈": u"鰁",
	u"鳉": u"鱂",
	u"鳊": u"鯿",
	u"鳋": u"鰠",
	u"鳌": u"鼇",
	u"鳍": u"鰭",
	u"鳎": u"鰨",
	u"鳏": u"鰥",
	u"鳐": u"鰩",
	u"鳑": u"鰟",
	u"鳒": u"鰜",
	u"鳓": u"鰳",
	u"鳔": u"鰾",
	u"鳕": u"鱈",
	u"鳖": u"鱉",
	u"鳗": u"鰻",
	u"鳘": u"鰵",
	u"鳙": u"鱅",
	u"鳛": u"鰼",
	u"鳜": u"鱖",
	u"鳝": u"鱔",
	u"鳞": u"鱗",
	u"鳟": u"鱒",
	u"鳠": u"鱯",
	u"鳡": u"鱤",
	u"鳢": u"鱧",
	u"鳣": u"鱣",
	u"鸟": u"鳥",
	u"鸠": u"鳩",
	u"鸡": u"雞",
	u"鸢": u"鳶",
	u"鸣": u"鳴",
	u"鸤": u"鳲",
	u"鸥": u"鷗",
	u"鸦": u"鴉",
	u"鸧": u"鶬",
	u"鸨": u"鴇",
	u"鸩": u"鴆",
	u"鸪": u"鴣",
	u"鸫": u"鶇",
	u"鸬": u"鸕",
	u"鸭": u"鴨",
	u"鸮": u"鴞",
	u"鸯": u"鴦",
	u"鸰": u"鴒",
	u"鸱": u"鴟",
	u"鸲": u"鴝",
	u"鸳": u"鴛",
	u"鸴": u"鴬",
	u"鸵": u"鴕",
	u"鸶": u"鷥",
	u"鸷": u"鷙",
	u"鸸": u"鴯",
	u"鸹": u"鴰",
	u"鸺": u"鵂",
	u"鸻": u"鴴",
	u"鸼": u"鵃",
	u"鸽": u"鴿",
	u"鸾": u"鸞",
	u"鸿": u"鴻",
	u"鹀": u"鵐",
	u"鹁": u"鵓",
	u"鹂": u"鸝",
	u"鹃": u"鵑",
	u"鹄": u"鵠",
	u"鹅": u"鵝",
	u"鹆": u"鵒",
	u"鹇": u"鷳",
	u"鹈": u"鵜",
	u"鹉": u"鵡",
	u"鹊": u"鵲",
	u"鹋": u"鶓",
	u"鹌": u"鵪",
	u"鹍": u"鶤",
	u"鹎": u"鵯",
	u"鹏": u"鵬",
	u"鹐": u"鵮",
	u"鹑": u"鶉",
	u"鹒": u"鶊",
	u"鹓": u"鵷",
	u"鹔": u"鷫",
	u"鹕": u"鶘",
	u"鹖": u"鶡",
	u"鹗": u"鶚",
	u"鹘": u"鶻",
	u"鹙": u"鶖",
	u"鹚": u"鶿",
	u"鹛": u"鶥",
	u"鹜": u"鶩",
	u"鹝": u"鷊",
	u"鹞": u"鷂",
	u"鹟": u"鶲",
	u"鹠": u"鶹",
	u"鹡": u"鶺",
	u"鹢": u"鷁",
	u"鹣": u"鶼",
	u"鹤": u"鶴",
	u"鹥": u"鷖",
	u"鹦": u"鸚",
	u"鹧": u"鷓",
	u"鹨": u"鷚",
	u"鹩": u"鷯",
	u"鹪": u"鷦",
	u"鹫": u"鷲",
	u"鹬": u"鷸",
	u"鹭": u"鷺",
	u"鹯": u"鸇",
	u"鹰": u"鷹",
	u"鹱": u"鸌",
	u"鹲": u"鸏",
	u"鹳": u"鸛",
	u"鹴": u"鸘",
	u"鹾": u"鹺",
	u"麦": u"麥",
	u"麸": u"麩",
	u"黄": u"黃",
	u"黉": u"黌",
	u"黡": u"黶",
	u"黩": u"黷",
	u"黪": u"黲",
	u"黾": u"黽",
	u"鼋": u"黿",
	u"鼌": u"鼂",
	u"鼍": u"鼉",
	u"鼗": u"鞀",
	u"鼹": u"鼴",
	u"齄": u"齇",
	u"齐": u"齊",
	u"齑": u"齏",
	u"齿": u"齒",
	u"龀": u"齔",
	u"龁": u"齕",
	u"龂": u"齗",
	u"龃": u"齟",
	u"龄": u"齡",
	u"龅": u"齙",
	u"龆": u"齠",
	u"龇": u"齜",
	u"龈": u"齦",
	u"龉": u"齬",
	u"龊": u"齪",
	u"龋": u"齲",
	u"龌": u"齷",
	u"龙": u"龍",
	u"龚": u"龔",
	u"龛": u"龕",
	u"龟": u"龜"
}

_mapFromMars = None

import codecs
from StringIO import StringIO

__all__ = ['encode', 'decode']

def url_encode(input):
	s = StringIO()
	for i in input:
		s.write(i in _mapToMars and _mapToMars[i] or i)
	return (s.getvalue(), len(input))

def url_decode(input):
	global _mapFromMars
	if not _mapFromMars:
		_mapFromMars = dict([(v, k) for (k, v) in _mapToMars.iteritems()])
	s = StringIO()
	for i in input:
		s.write(i in _mapFromMars and _mapFromMars[i] or i)
	return (s.getvalue(), len(input))

class Codec(codecs.Codec):
	def encode(self, input, errors='strict'):
		return url_encode(input, errors)

	def decode(self, input, errors='strict'):
		return url_decode(input, errors)

class StreamWriter(Codec, codecs.StreamWriter):
	pass

class StreamReader(Codec, codecs.StreamReader):
	pass

def search_function(encoding):
	if encoding == "mars":
		return (url_encode, url_decode, StreamReader, StreamWriter)

	return None

codecs.register(search_function)
