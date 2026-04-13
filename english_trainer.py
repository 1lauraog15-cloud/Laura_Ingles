import streamlit as st
import random
import anthropic

st.set_page_config(page_title="Laura_Inglés", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.flashcard {
    background: linear-gradient(135deg, #1e3a5f 0%, #2d6a9f 100%);
    border-radius: 16px; padding: 2rem 2.5rem; margin: 1rem 0;
    color: white; box-shadow: 0 8px 24px rgba(0,0,0,0.2);
}
.word-title { font-size: 2.2rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.3rem; }
.translation { font-size: 1.1rem; color: #a8d8f0; font-style: italic; margin-bottom: 1rem; }
.tag { display: inline-block; background: rgba(255,255,255,0.15); border-radius: 20px;
       padding: 2px 10px; font-size: 0.82rem; margin: 2px; }
.section-header { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.5rem; }
.example-box { background: #f0f7ff; border-left: 4px solid #2d6a9f;
               padding: 0.8rem 1rem; border-radius: 0 8px 8px 0; margin: 0.5rem 0; color: #1a1a2e; }
.score-box { background: #e8f5e9; border-radius: 10px; padding: 0.5rem 1rem;
             display: inline-block; font-weight: 600; color: #2e7d32; }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  DATA
# ════════════════════════════════════════════════════════════════════════════

VOCABULARY = [
    {"word":"acquiesce","translation":"ceder / aceptar de mala gana","definition":"Accept something reluctantly but without protest","synonyms":["comply","consent","yield","concede"],"antonyms":["resist","object","refuse","protest"],"example":"She acquiesced to her manager's demands despite her reservations.","collocation":"acquiesce to/in a decision"},
    {"word":"acrimony","translation":"acritud / amargura","definition":"Bitterness or ill feeling, especially in speech","synonyms":["bitterness","hostility","rancour","animosity"],"antonyms":["goodwill","warmth","cordiality","amity"],"example":"The divorce was conducted with surprising acrimony.","collocation":"with acrimony; bitter acrimony"},
    {"word":"ambivalent","translation":"ambivalente / con sentimientos encontrados","definition":"Having mixed feelings or contradictory ideas about something","synonyms":["uncertain","undecided","equivocal","torn"],"antonyms":["certain","decisive","unequivocal","resolute"],"example":"He felt ambivalent about moving abroad — excited yet deeply anxious.","collocation":"ambivalent about/towards something"},
    {"word":"ameliorate","translation":"mejorar / paliar","definition":"Make something bad or unsatisfactory better","synonyms":["improve","alleviate","mitigate","enhance"],"antonyms":["worsen","aggravate","exacerbate","deteriorate"],"example":"Aid agencies worked to ameliorate the effects of the drought.","collocation":"ameliorate conditions, a situation"},
    {"word":"anachronistic","translation":"anacrónico","definition":"Belonging to a period other than that being portrayed; out of date","synonyms":["outdated","archaic","obsolete","antiquated"],"antonyms":["modern","contemporary","current","up-to-date"],"example":"Some people regard the monarchy as anachronistic.","collocation":"anachronistic view, system, institution"},
    {"word":"arduous","translation":"arduo / extenuante","definition":"Involving or requiring strenuous effort; difficult and tiring","synonyms":["gruelling","laborious","strenuous","taxing"],"antonyms":["easy","effortless","straightforward","simple"],"example":"The arduous trek through the mountains took three days.","collocation":"arduous task, journey, process"},
    {"word":"astute","translation":"astuto / perspicaz","definition":"Having an ability to accurately assess situations; shrewd","synonyms":["shrewd","sharp","perceptive","sagacious"],"antonyms":["naive","obtuse","foolish","gullible"],"example":"She made an astute observation about the company's financial model.","collocation":"astute businessman, observer, move"},
    {"word":"attrition","translation":"desgaste / atrición","definition":"The process of gradually reducing strength by sustained attack","synonyms":["erosion","wearing down","depletion","weakening"],"antonyms":["strengthening","growth","reinforcement","build-up"],"example":"The war of attrition exhausted both sides.","collocation":"war of attrition; staff attrition"},
    {"word":"benevolent","translation":"benévolo / bondadoso","definition":"Well meaning and kindly; generous","synonyms":["kind","charitable","philanthropic","magnanimous"],"antonyms":["malevolent","cruel","unkind","selfish"],"example":"The funds came from a benevolent anonymous donor.","collocation":"benevolent dictator, organisation, gesture"},
    {"word":"byzantine","translation":"bizantino / intrincado","definition":"Excessively complicated and difficult to understand","synonyms":["intricate","convoluted","labyrinthine","complex"],"antonyms":["simple","straightforward","transparent","clear"],"example":"The byzantine regulations made it nearly impossible to register a business.","collocation":"byzantine system, rules, bureaucracy"},
    {"word":"cajole","translation":"engatusar / persuadir con halagos","definition":"Persuade someone to do something by sustained coaxing or flattery","synonyms":["coax","wheedle","persuade","inveigle"],"antonyms":["coerce","force","discourage","dissuade"],"example":"She cajoled her reluctant colleague into joining the project.","collocation":"cajole someone into doing something"},
    {"word":"candour","translation":"franqueza / sinceridad","definition":"The quality of being open and honest in expression; frankness","synonyms":["frankness","openness","honesty","directness"],"antonyms":["dishonesty","evasiveness","insincerity","deception"],"example":"His candour during the interview was both refreshing and disarming.","collocation":"speak with candour; commendable candour"},
    {"word":"complacent","translation":"complaciente consigo mismo / conformista","definition":"Showing smug or uncritical satisfaction with oneself or one's achievements","synonyms":["self-satisfied","smug","content","untroubled"],"antonyms":["anxious","humble","dissatisfied","vigilant"],"example":"The team became dangerously complacent after their early success.","collocation":"complacent attitude; become complacent"},
    {"word":"conciliatory","translation":"conciliador","definition":"Intended to make someone less angry; willing to make concessions","synonyms":["appeasing","placatory","mollifying","diplomatic"],"antonyms":["antagonistic","provocative","aggressive","confrontational"],"example":"The manager adopted a conciliatory tone to ease the dispute.","collocation":"conciliatory gesture, tone, approach"},
    {"word":"contentious","translation":"controvertido / polémico","definition":"Causing or likely to cause an argument; controversial","synonyms":["controversial","disputed","debatable","divisive"],"antonyms":["uncontroversial","agreed","harmonious","settled"],"example":"The proposed reform proved highly contentious among legislators.","collocation":"contentious issue, point, debate"},
    {"word":"corroborate","translation":"corroborar / confirmar","definition":"Confirm or give support to a statement, theory, or finding","synonyms":["confirm","verify","substantiate","validate"],"antonyms":["contradict","refute","disprove","undermine"],"example":"Several witnesses corroborated the account given by the defendant.","collocation":"corroborate a claim, evidence, testimony"},
    {"word":"curtail","translation":"recortar / limitar","definition":"Reduce in extent or quantity; impose a restriction on","synonyms":["reduce","restrict","cut back","limit"],"antonyms":["extend","expand","increase","prolong"],"example":"Budget constraints forced them to curtail their research programme.","collocation":"curtail spending, freedom, activities"},
    {"word":"deference","translation":"deferencia / respeto","definition":"Humble submission and respect shown to someone","synonyms":["respect","regard","reverence","submission"],"antonyms":["disrespect","defiance","arrogance","insolence"],"example":"In deference to her expertise, the committee accepted her recommendation.","collocation":"show deference to; in deference to"},
    {"word":"denigrate","translation":"denigrar / menospreciar","definition":"Criticise unfairly; disparage","synonyms":["disparage","belittle","deprecate","malign"],"antonyms":["praise","commend","honour","extol"],"example":"It is unprofessional to denigrate your rivals in public.","collocation":"denigrate someone's reputation, work, efforts"},
    {"word":"disparate","translation":"dispar / heterogéneo","definition":"Essentially different in kind; not allowing comparison","synonyms":["different","dissimilar","divergent","heterogeneous"],"antonyms":["similar","alike","comparable","homogeneous"],"example":"The study brought together disparate fields of research.","collocation":"disparate groups, elements, views"},
    {"word":"disparity","translation":"disparidad / desigualdad","definition":"A great difference between things","synonyms":["inequality","gap","imbalance","discrepancy"],"antonyms":["parity","equality","similarity","balance"],"example":"The growing disparity between rich and poor is a major political issue.","collocation":"growing disparity; disparity between/in"},
    {"word":"eloquent","translation":"elocuente","definition":"Fluent or persuasive in speaking or writing","synonyms":["articulate","persuasive","expressive","fluent"],"antonyms":["inarticulate","tongue-tied","stilted","hesitant"],"example":"Her eloquent speech moved the entire audience to tears.","collocation":"eloquent speaker, argument, silence"},
    {"word":"endemic","translation":"endémico","definition":"Regularly found among particular people or in a certain area","synonyms":["widespread","prevalent","rife","pervasive"],"antonyms":["rare","uncommon","isolated","sporadic"],"example":"Corruption is endemic in the country's political system.","collocation":"endemic to a region; endemic disease"},
    {"word":"ephemeral","translation":"efímero / pasajero","definition":"Lasting for a very short time","synonyms":["fleeting","transient","momentary","short-lived"],"antonyms":["permanent","enduring","lasting","eternal"],"example":"Social media fame is often ephemeral.","collocation":"ephemeral trend, pleasure, nature"},
    {"word":"exacerbate","translation":"exacerbar / empeorar","definition":"Make a problem, bad situation, or negative feeling worse","synonyms":["aggravate","worsen","intensify","compound"],"antonyms":["alleviate","improve","mitigate","ease"],"example":"Poor communication only served to exacerbate the conflict.","collocation":"exacerbate tensions, a problem, symptoms"},
    {"word":"fastidious","translation":"meticuloso / quisquilloso","definition":"Very attentive to accuracy and detail; hard to please","synonyms":["meticulous","scrupulous","exacting","particular"],"antonyms":["careless","slovenly","sloppy","indifferent"],"example":"She was fastidious about maintaining accurate records.","collocation":"fastidious about details, cleanliness"},
    {"word":"fledgling","translation":"novel / en ciernes","definition":"New and inexperienced; just starting to develop","synonyms":["emerging","nascent","budding","incipient"],"antonyms":["established","experienced","mature","veteran"],"example":"The fledgling start-up struggled to compete with established rivals.","collocation":"fledgling company, democracy, career"},
    {"word":"futile","translation":"fútil / inútil","definition":"Producing no useful result; pointless","synonyms":["pointless","fruitless","vain","ineffective"],"antonyms":["effective","productive","fruitful","worthwhile"],"example":"Any attempt to reason with him seemed utterly futile.","collocation":"futile attempt, effort, gesture"},
    {"word":"idiosyncrasy","translation":"idiosincrasia / peculiaridad","definition":"A mode of behaviour or way of thought peculiar to an individual","synonyms":["quirk","peculiarity","eccentricity","characteristic"],"antonyms":["normality","convention","conformity","uniformity"],"example":"Every great artist has at least one idiosyncrasy that makes their work instantly recognisable.","collocation":"personal idiosyncrasy; cultural idiosyncrasy"},
    {"word":"impasse","translation":"punto muerto / callejón sin salida","definition":"A situation in which no progress is possible","synonyms":["deadlock","stalemate","standstill","dead end"],"antonyms":["breakthrough","progress","resolution","agreement"],"example":"Negotiations reached an impasse after three days of talks.","collocation":"reach an impasse; break an impasse"},
    {"word":"impetuous","translation":"impetuoso / impulsivo","definition":"Acting or done quickly without thought or care","synonyms":["impulsive","rash","hasty","reckless"],"antonyms":["cautious","measured","deliberate","considered"],"example":"His impetuous decision to resign shocked the board.","collocation":"impetuous decision, action, behaviour"},
    {"word":"inadvertent","translation":"involuntario / accidental","definition":"Not resulting from or achieved through deliberate planning","synonyms":["unintentional","accidental","unintended","unwitting"],"antonyms":["deliberate","intentional","conscious","planned"],"example":"The mistake was inadvertent, not the result of negligence.","collocation":"inadvertent error, consequence, disclosure"},
    {"word":"innate","translation":"innato / natural","definition":"Inborn; natural; not acquired","synonyms":["inherent","natural","inborn","instinctive"],"antonyms":["learned","acquired","cultivated","developed"],"example":"She had an innate talent for languages that set her apart from her peers.","collocation":"innate ability, talent, sense"},
    {"word":"insidious","translation":"insidioso / traicionero","definition":"Proceeding in a gradual subtle way but with harmful effects","synonyms":["subtle","treacherous","stealthy","pernicious"],"antonyms":["obvious","overt","harmless","benign"],"example":"The insidious effects of stress are often overlooked.","collocation":"insidious disease, influence, spread"},
    {"word":"lucid","translation":"lúcido / claro","definition":"Expressed clearly; easy to understand; mentally clear","synonyms":["clear","coherent","articulate","intelligible"],"antonyms":["confused","muddled","incoherent","obscure"],"example":"Even in old age, her mind remained remarkably lucid.","collocation":"lucid explanation, account, interval"},
    {"word":"meticulous","translation":"meticuloso / minucioso","definition":"Showing great attention to detail; very careful and precise","synonyms":["thorough","precise","scrupulous","painstaking"],"antonyms":["careless","sloppy","haphazard","negligent"],"example":"The report was the result of months of meticulous research.","collocation":"meticulous attention, planning, record-keeping"},
    {"word":"mitigate","translation":"mitigar / atenuar","definition":"Make less severe, serious, or painful","synonyms":["alleviate","lessen","reduce","ease"],"antonyms":["aggravate","intensify","exacerbate","worsen"],"example":"Measures were taken to mitigate the impact of the floods.","collocation":"mitigate risk, damage, the effects of"},
    {"word":"nuanced","translation":"matizado / con matices","definition":"Characterised by subtle shades of meaning or expression","synonyms":["subtle","complex","refined","sophisticated"],"antonyms":["simplistic","crude","blunt","one-dimensional"],"example":"The film offers a nuanced portrayal of life in wartime.","collocation":"nuanced analysis, view, approach"},
    {"word":"obsequious","translation":"obsequioso / servil","definition":"Obedient or attentive to an excessive or servile degree","synonyms":["servile","subservient","fawning","sycophantic"],"antonyms":["assertive","independent","blunt","direct"],"example":"His obsequious manner irritated his colleagues.","collocation":"obsequious behaviour, attitude, manner"},
    {"word":"obsolete","translation":"obsoleto / en desuso","definition":"No longer produced or used; out of date","synonyms":["outdated","outmoded","archaic","superseded"],"antonyms":["current","modern","up-to-date","cutting-edge"],"example":"Many traditional skills have become obsolete in the digital age.","collocation":"render obsolete; become obsolete"},
    {"word":"paramount","translation":"primordial / de suma importancia","definition":"More important than anything else; supreme","synonyms":["supreme","foremost","primary","overriding"],"antonyms":["secondary","minor","trivial","subordinate"],"example":"Safety must be of paramount importance on construction sites.","collocation":"of paramount importance; paramount concern"},
    {"word":"pervasive","translation":"omnipresente / generalizado","definition":"Spreading widely throughout an area or group of people","synonyms":["widespread","prevalent","rife","ubiquitous"],"antonyms":["localised","limited","confined","rare"],"example":"There was a pervasive sense of unease throughout the organisation.","collocation":"pervasive influence, atmosphere, problem"},
    {"word":"pragmatic","translation":"pragmático","definition":"Dealing with things sensibly and realistically, not theoretically","synonyms":["practical","realistic","sensible","rational"],"antonyms":["idealistic","impractical","unrealistic","dogmatic"],"example":"We need a pragmatic approach rather than an idealistic one.","collocation":"pragmatic approach, solution, decision"},
    {"word":"proliferate","translation":"proliferar / multiplicarse","definition":"Increase rapidly in numbers; multiply","synonyms":["multiply","spread","mushroom","expand"],"antonyms":["decrease","dwindle","decline","diminish"],"example":"Fast food chains have proliferated across the country.","collocation":"rapidly proliferate; proliferate in/across"},
    {"word":"reticent","translation":"reservado / reticente","definition":"Not revealing one's thoughts or feelings readily; reserved","synonyms":["reserved","taciturn","quiet","withdrawn"],"antonyms":["forthright","talkative","open","outspoken"],"example":"She was reticent about discussing her personal life.","collocation":"reticent about; remain reticent"},
    {"word":"resilience","translation":"resiliencia / capacidad de recuperación","definition":"The capacity to recover quickly from difficulties; toughness","synonyms":["toughness","durability","flexibility","adaptability"],"antonyms":["fragility","vulnerability","weakness","brittleness"],"example":"The community showed remarkable resilience in the aftermath of the crisis.","collocation":"show resilience; build resilience; emotional resilience"},
    {"word":"rhetoric","translation":"retórica","definition":"Language designed to have a persuasive or impressive effect","synonyms":["oratory","eloquence","discourse","bombast"],"antonyms":["plain speech","directness","candour","sincerity"],"example":"His speech was full of rhetoric but lacked concrete proposals.","collocation":"political rhetoric; hollow rhetoric; mere rhetoric"},
    {"word":"scrutinise","translation":"escrutar / examinar minuciosamente","definition":"Examine or inspect closely and thoroughly","synonyms":["examine","inspect","analyse","investigate"],"antonyms":["ignore","overlook","glance at","skim"],"example":"The committee scrutinised every line of the proposed budget.","collocation":"scrutinise data, a contract, accounts"},
    {"word":"spurious","translation":"espurio / falso","definition":"Not being what it purports to be; false or fake","synonyms":["false","bogus","counterfeit","unfounded"],"antonyms":["genuine","authentic","valid","legitimate"],"example":"The report was later revealed to be based on spurious data.","collocation":"spurious claim, argument, evidence"},
    {"word":"tenacious","translation":"tenaz / perseverante","definition":"Tending to keep a firm hold; very persistent","synonyms":["persistent","determined","resolute","dogged"],"antonyms":["weak","irresolute","yielding","halfhearted"],"example":"She was tenacious in her pursuit of justice.","collocation":"tenacious defender, pursuit; tenaciously held belief"},
    {"word":"transient","translation":"transitorio / pasajero","definition":"Lasting only for a short time; not permanent","synonyms":["temporary","fleeting","brief","passing"],"antonyms":["permanent","lasting","enduring","stable"],"example":"The transient nature of city life can be isolating.","collocation":"transient population, effect, feeling"},
    {"word":"ubiquitous","translation":"ubicuo / omnipresente","definition":"Present, appearing, or found everywhere","synonyms":["omnipresent","pervasive","universal","everywhere"],"antonyms":["rare","scarce","uncommon","localised"],"example":"Smartphones have become ubiquitous in modern society.","collocation":"ubiquitous technology, presence, symbol"},
    {"word":"unprecedented","translation":"sin precedentes","definition":"Never done or known before","synonyms":["unparalleled","unequalled","unique","extraordinary"],"antonyms":["common","ordinary","familiar","precedented"],"example":"The pandemic caused unprecedented disruption to global supply chains.","collocation":"unprecedented scale, levels, decision"},
    {"word":"vacillate","translation":"vacilar / fluctuar","definition":"Waver between different opinions or actions; be indecisive","synonyms":["waver","hesitate","fluctuate","oscillate"],"antonyms":["decide","commit","resolve","determine"],"example":"The government vacillated over its response to the crisis.","collocation":"vacillate between; vacillate over a decision"},
    {"word":"viable","translation":"viable / factible","definition":"Capable of working successfully; feasible","synonyms":["feasible","workable","practical","achievable"],"antonyms":["unworkable","impractical","impossible","unfeasible"],"example":"The committee concluded that the plan was not financially viable.","collocation":"viable option, alternative, solution"},
    {"word":"volatile","translation":"volátil / inestable","definition":"Liable to change rapidly and unpredictably","synonyms":["unstable","unpredictable","erratic","changeable"],"antonyms":["stable","steady","predictable","consistent"],"example":"The stock market remains volatile amid geopolitical uncertainty.","collocation":"volatile situation, market, relationship"},
    {"word":"wane","translation":"menguar / decrecer","definition":"Decrease in vigour, power, or extent; decline","synonyms":["decline","diminish","decrease","fade"],"antonyms":["grow","increase","flourish","wax"],"example":"Public enthusiasm for the project began to wane.","collocation":"wane in popularity; on the wane"},
    {"word":"zenith","translation":"cénit / apogeo","definition":"The time at which something is most powerful or successful","synonyms":["peak","pinnacle","apex","summit"],"antonyms":["nadir","low point","decline","trough"],"example":"The empire reached its zenith in the eighteenth century.","collocation":"at its zenith; zenith of power/fame"},
    # ── From My Vocabulary Notes ──────────────────────────────────────────
    {"word":"acknowledge","translation":"reconocer / admitir","definition":"Accept or admit the truth or existence of something","synonyms":["admit","recognise","concede","accept"],"antonyms":["deny","ignore","reject","dismiss"],"example":"She acknowledged that the report contained several significant errors.","collocation":"acknowledge a mistake, fact, receipt"},
    {"word":"acquire","translation":"adquirir / obtener","definition":"Come to have or obtain something, especially over time","synonyms":["obtain","gain","secure","attain"],"antonyms":["lose","give up","relinquish","forfeit"],"example":"The company has acquired three new subsidiaries in the past year.","collocation":"acquire skills, knowledge, assets"},
    {"word":"astonished","translation":"asombrado / atónito","definition":"Greatly surprised or amazed","synonyms":["amazed","astounded","stunned","flabbergasted"],"antonyms":["unsurprised","unfazed","indifferent","expected"],"example":"She was astonished to discover that her article had gone viral overnight.","collocation":"astonished by/at; utterly astonished"},
    {"word":"awareness","translation":"conciencia / conocimiento","definition":"Knowledge or perception of a situation or fact","synonyms":["consciousness","understanding","recognition","mindfulness"],"antonyms":["ignorance","unawareness","obliviousness","neglect"],"example":"Public awareness of mental health issues has grown considerably.","collocation":"raise awareness; lack of awareness; awareness campaign"},
    {"word":"barely","translation":"apenas / a duras penas","definition":"Only just; almost not","synonyms":["scarcely","hardly","just","only just"],"antonyms":["easily","comfortably","clearly","well"],"example":"She had barely sat down when her phone rang.","collocation":"barely audible, visible, noticeable"},
    {"word":"cranky","translation":"malhumorado / irritable","definition":"Irritable and easily upset; bad-tempered","synonyms":["irritable","grumpy","tetchy","cantankerous"],"antonyms":["cheerful","good-humoured","easygoing","placid"],"example":"He was cranky all morning after missing his train.","collocation":"feel cranky; cranky mood"},
    {"word":"delighted","translation":"encantado / contentísimo","definition":"Feeling or showing great pleasure; very happy","synonyms":["thrilled","overjoyed","elated","pleased"],"antonyms":["disappointed","dismayed","displeased","unhappy"],"example":"She was absolutely delighted when she received the acceptance letter.","collocation":"delighted with/by/at; absolutely delighted"},
    {"word":"distressed","translation":"angustiado / afligido","definition":"Suffering from anxiety, sorrow, or pain","synonyms":["upset","troubled","distraught","anguished"],"antonyms":["calm","composed","relieved","content"],"example":"The witness appeared visibly distressed during the hearing.","collocation":"visibly distressed; distressed at/by"},
    {"word":"drought","translation":"sequía","definition":"A prolonged period of abnormally low rainfall","synonyms":["dry spell","water shortage","aridity","dearth"],"antonyms":["flood","deluge","abundance","plenty"],"example":"The prolonged drought devastated crops across the region.","collocation":"severe drought; drought conditions; suffer a drought"},
    {"word":"flattered","translation":"halagado / adulado","definition":"Pleased by the praise, attention, or flattery shown","synonyms":["honoured","pleased","gratified","complimented"],"antonyms":["insulted","offended","humiliated","displeased"],"example":"She was flattered to be asked to speak at the conference.","collocation":"feel flattered; deeply flattered"},
    {"word":"foolish","translation":"tonto / necio / imprudente","definition":"Lacking good sense or judgement; unwise","synonyms":["unwise","imprudent","senseless","reckless"],"antonyms":["wise","sensible","prudent","shrewd"],"example":"It would be foolish to ignore the warning signs.","collocation":"foolish mistake, decision, pride"},
    {"word":"frightened","translation":"asustado / atemorizado","definition":"Afraid or anxious; filled with fear","synonyms":["afraid","scared","terrified","apprehensive"],"antonyms":["brave","unafraid","fearless","bold"],"example":"The child was frightened by the sudden loud noise.","collocation":"frightened of/by; deeply frightened"},
    {"word":"glum","translation":"sombrío / cabizbajo","definition":"Looking or feeling dejected; morose","synonyms":["dejected","morose","despondent","downcast"],"antonyms":["cheerful","upbeat","bright","happy"],"example":"He sat in the corner looking glum after hearing the news.","collocation":"look glum; feel glum; glum expression"},
    {"word":"hesitant","translation":"vacilante / indeciso","definition":"Tentative, unsure, or slow to act","synonyms":["uncertain","undecided","reluctant","tentative"],"antonyms":["decisive","confident","assertive","certain"],"example":"She was hesitant to voice her concerns in front of the board.","collocation":"hesitant about/to; remain hesitant"},
    {"word":"infer","translation":"inferir / deducir","definition":"Deduce or conclude from evidence and reasoning","synonyms":["deduce","conclude","gather","surmise"],"antonyms":["state","assert","declare","express"],"example":"From the data, we can infer that demand is likely to increase.","collocation":"infer from; reasonably infer"},
    {"word":"influx","translation":"afluencia / entrada masiva","definition":"An arrival or entry of large numbers of people or things","synonyms":["inflow","surge","flood","stream"],"antonyms":["outflow","departure","exodus","decline"],"example":"The city struggled to cope with a sudden influx of tourists.","collocation":"influx of migrants, capital, visitors"},
    {"word":"lasting","translation":"duradero / permanente","definition":"Enduring or able to endure over a long period of time","synonyms":["enduring","permanent","durable","long-lasting"],"antonyms":["temporary","fleeting","brief","transient"],"example":"The speech left a lasting impression on everyone who heard it.","collocation":"lasting impact, impression, damage, peace"},
    {"word":"mogul","translation":"magnate / poderoso","definition":"A very powerful or influential person in a particular industry","synonyms":["magnate","tycoon","baron","powerbroker"],"antonyms":["nobody","subordinate","follower","unknown"],"example":"She became a media mogul after buying three major publishing houses.","collocation":"media mogul; film mogul; business mogul"},
    {"word":"neglectful","translation":"negligente / descuidado","definition":"Failing to give proper care or attention","synonyms":["negligent","careless","inattentive","remiss"],"antonyms":["attentive","careful","diligent","conscientious"],"example":"The report criticised the neglectful management of public funds.","collocation":"neglectful of duties, responsibilities"},
    {"word":"nonchalant","translation":"despreocupado / indiferente","definition":"Feeling or appearing calm and relaxed, not worried","synonyms":["indifferent","casual","unconcerned","blasé"],"antonyms":["anxious","concerned","worried","tense"],"example":"Despite the chaos around her, she remained remarkably nonchalant.","collocation":"nonchalant attitude, manner, shrug"},
    {"word":"oblivious","translation":"ajeno a / inconsciente de","definition":"Not aware of or concerned about what is happening around","synonyms":["unaware","unconscious","ignorant","heedless"],"antonyms":["aware","conscious","attentive","alert"],"example":"He was completely oblivious to the tension in the room.","collocation":"oblivious to/of; blissfully oblivious"},
    {"word":"outrageous","translation":"indignante / escandaloso","definition":"Shockingly bad or excessive; wildly unacceptable","synonyms":["scandalous","shocking","disgraceful","preposterous"],"antonyms":["acceptable","reasonable","mild","appropriate"],"example":"The level of inequality in the country is quite simply outrageous.","collocation":"outrageous behaviour, claim, price, suggestion"},
    {"word":"overwhelming","translation":"abrumador / aplastante","definition":"Very great in amount; difficult to fight or resist","synonyms":["overpowering","staggering","crushing","massive"],"antonyms":["manageable","slight","modest","weak"],"example":"There was an overwhelming sense of relief when the crisis ended.","collocation":"overwhelming majority, evidence, support, pressure"},
    {"word":"promising","translation":"prometedor / con buenas perspectivas","definition":"Showing signs of future success; full of potential","synonyms":["hopeful","auspicious","encouraging","talented"],"antonyms":["unpromising","bleak","discouraging","disappointing"],"example":"The young scientist had a highly promising academic record.","collocation":"promising start, career, outlook; show promise"},
    {"word":"reckless","translation":"temerario / imprudente","definition":"Acting without thinking of the consequences; heedless of danger","synonyms":["rash","impetuous","irresponsible","careless"],"antonyms":["cautious","careful","prudent","responsible"],"example":"The driver was charged with reckless endangerment.","collocation":"reckless behaviour, disregard, abandon"},
    {"word":"relieved","translation":"aliviado","definition":"No longer feeling distressed about a situation; comforted","synonyms":["reassured","comforted","grateful","thankful"],"antonyms":["worried","anxious","stressed","concerned"],"example":"She was relieved to hear that the operation had been a success.","collocation":"feel relieved; greatly relieved; relieved to hear"},
    {"word":"ripple","translation":"ondulación / efecto en cadena","definition":"A small wave or series of waves; a spreading effect","synonyms":["wave","undulation","tremor","reverberation"],"antonyms":["stillness","calm","flatness","stasis"],"example":"A single decision can send ripples through an entire organisation.","collocation":"ripple effect; cause ripples; ripples of change"},
    {"word":"rusty","translation":"oxidado / falto de práctica","definition":"Covered with rust; or, not as good as usual due to lack of practice","synonyms":["corroded","out of practice","unpractised","stiff"],"antonyms":["sharp","polished","fluent","well-practised"],"example":"My French is a bit rusty — I haven't spoken it in years.","collocation":"rusty skills, knowledge; a bit rusty"},
    {"word":"selfish","translation":"egoísta","definition":"Caring only about oneself and not about others","synonyms":["self-centred","self-serving","greedy","inconsiderate"],"antonyms":["selfless","generous","altruistic","considerate"],"example":"It would be selfish to take the last resources without sharing them.","collocation":"selfish behaviour, motive, attitude"},
    {"word":"solely","translation":"únicamente / exclusivamente","definition":"Not involving anyone or anything else; only","synonyms":["exclusively","only","purely","entirely"],"antonyms":["partly","jointly","collectively","also"],"example":"She was solely responsible for the financial decisions.","collocation":"solely responsible; based solely on; solely for"},
    {"word":"sullen","translation":"malhumorado / huraño","definition":"Bad-tempered and sulky; gloomy and resentful","synonyms":["surly","brooding","morose","resentful"],"antonyms":["cheerful","friendly","affable","good-natured"],"example":"He gave a sullen response and refused to explain his behaviour.","collocation":"sullen silence, look, mood, teenager"},
    {"word":"trustworthy","translation":"digno de confianza / fiable","definition":"Able to be relied on as honest or truthful","synonyms":["reliable","dependable","honest","credible"],"antonyms":["unreliable","dishonest","untrustworthy","deceptive"],"example":"You need a trustworthy partner to manage sensitive financial data.","collocation":"trustworthy source, adviser, friend"},
    {"word":"welfare","translation":"bienestar / asistencia social","definition":"The health, happiness, and prosperity of a person or group","synonyms":["wellbeing","prosperity","health","benefit"],"antonyms":["hardship","neglect","misery","harm"],"example":"The charity is dedicated to the welfare of displaced families.","collocation":"child welfare, animal welfare, public welfare, welfare state"},
    {"word":"wealthy","translation":"adinerado / pudiente","definition":"Having a great deal of money or assets; rich","synonyms":["affluent","prosperous","rich","well-off"],"antonyms":["poor","impoverished","destitute","penniless"],"example":"The policy was criticised for favouring wealthy landowners.","collocation":"wealthy individual, nation, elite"},
]

PHRASAL_VERBS = [
    {"pv":"account for","meaning":"explain or represent","translation":"explicar / representar","example":"How do you account for the missing data?","fill":"How do you ___________ the missing data?"},
    {"pv":"back down","meaning":"withdraw a claim or position","translation":"echarse atrás / ceder","example":"The company backed down after the public outcry.","fill":"The company ___________ after the public outcry."},
    {"pv":"bear out","meaning":"confirm or support","translation":"confirmar / corroborar","example":"The results bear out our initial hypothesis.","fill":"The results ___________ our initial hypothesis."},
    {"pv":"bring about","meaning":"cause something to happen","translation":"provocar / dar lugar a","example":"New technology has brought about radical changes.","fill":"New technology has ___________ radical changes."},
    {"pv":"build on","meaning":"use as a foundation to develop further","translation":"basarse en / aprovechar","example":"We need to build on last year's success.","fill":"We need to ___________ last year's success."},
    {"pv":"call for","meaning":"require or demand","translation":"exigir / requerir","example":"The situation calls for immediate action.","fill":"The situation ___________ immediate action."},
    {"pv":"carry out","meaning":"perform or conduct","translation":"llevar a cabo / realizar","example":"The team carried out a thorough investigation.","fill":"The team ___________ a thorough investigation."},
    {"pv":"come across","meaning":"find or meet by chance","translation":"encontrarse con / toparse con","example":"I came across a fascinating article about linguistics.","fill":"I ___________ a fascinating article about linguistics."},
    {"pv":"come up with","meaning":"produce or think of an idea","translation":"ocurrírsele algo / idear","example":"She came up with a creative solution to the problem.","fill":"She ___________ a creative solution to the problem."},
    {"pv":"cut back on","meaning":"reduce","translation":"reducir / recortar","example":"The government plans to cut back on public spending.","fill":"The government plans to ___________ public spending."},
    {"pv":"draw on","meaning":"make use of","translation":"recurrir a / valerse de","example":"She drew on her personal experience in writing the novel.","fill":"She ___________ her personal experience in writing the novel."},
    {"pv":"fall through","meaning":"fail to happen","translation":"venirse abajo / fracasar","example":"The deal fell through at the last minute.","fill":"The deal ___________ at the last minute."},
    {"pv":"give rise to","meaning":"cause or produce","translation":"dar lugar a / originar","example":"The new policy has given rise to widespread criticism.","fill":"The new policy has ___________ widespread criticism."},
    {"pv":"go ahead with","meaning":"proceed with something","translation":"seguir adelante con","example":"Despite the setbacks, they went ahead with the project.","fill":"Despite the setbacks, they ___________ the project."},
    {"pv":"hold out","meaning":"resist; offer as a possibility","translation":"resistir / aguantar","example":"Doctors held out little hope for a full recovery.","fill":"Doctors ___________ little hope for a full recovery."},
    {"pv":"iron out","meaning":"solve or eliminate problems","translation":"resolver / eliminar problemas","example":"We need to iron out the remaining issues before the launch.","fill":"We need to ___________ the remaining issues before the launch."},
    {"pv":"keep up with","meaning":"maintain the same pace as","translation":"seguir el ritmo / mantenerse al día","example":"It is hard to keep up with all the latest developments in AI.","fill":"It is hard to ___________ all the latest developments in AI."},
    {"pv":"lay off","meaning":"dismiss workers; stop doing something","translation":"despedir / dejar de hacer algo","example":"The company was forced to lay off several hundred staff.","fill":"The company was forced to ___________ several hundred staff."},
    {"pv":"look into","meaning":"investigate","translation":"investigar / examinar","example":"The authorities are looking into allegations of fraud.","fill":"The authorities are ___________ allegations of fraud."},
    {"pv":"make up for","meaning":"compensate for","translation":"compensar","example":"Nothing can make up for the time we have lost.","fill":"Nothing can ___________ the time we have lost."},
    {"pv":"pan out","meaning":"develop in a satisfactory way","translation":"salir bien / resultar","example":"The strategy did not pan out as expected.","fill":"The strategy did not ___________ as expected."},
    {"pv":"pick up on","meaning":"notice and draw attention to","translation":"captar / darse cuenta de","example":"The editor picked up on several factual errors in the draft.","fill":"The editor ___________ several factual errors in the draft."},
    {"pv":"play down","meaning":"make something seem less important","translation":"quitar importancia a / minimizar","example":"The minister tried to play down the scale of the crisis.","fill":"The minister tried to ___________ the scale of the crisis."},
    {"pv":"pull off","meaning":"succeed in doing something difficult","translation":"lograr / conseguir (algo difícil)","example":"Against all odds, they pulled off a remarkable victory.","fill":"Against all odds, they ___________ a remarkable victory."},
    {"pv":"put forward","meaning":"propose or suggest","translation":"proponer / presentar","example":"She put forward a compelling argument for reform.","fill":"She ___________ a compelling argument for reform."},
    {"pv":"rule out","meaning":"exclude from consideration","translation":"descartar","example":"The police have not ruled out the possibility of foul play.","fill":"The police have not ___________ the possibility of foul play."},
    {"pv":"run into","meaning":"encounter a problem or person","translation":"toparse con / encontrarse con","example":"The project ran into serious funding difficulties.","fill":"The project ___________ serious funding difficulties."},
    {"pv":"set out","meaning":"begin with a particular aim; explain clearly","translation":"proponerse / exponer","example":"The report sets out a clear vision for the future.","fill":"The report ___________ a clear vision for the future."},
    {"pv":"stand out","meaning":"be easily noticed","translation":"destacar / sobresalir","example":"Her academic record stood out among all the applicants.","fill":"Her academic record ___________ among all the applicants."},
    {"pv":"take on","meaning":"accept work or responsibility; employ","translation":"asumir / contratar","example":"The firm decided to take on three new associates.","fill":"The firm decided to ___________ three new associates."},
    {"pv":"turn out","meaning":"prove to be; happen in a particular way","translation":"resultar / acabar siendo","example":"The event turned out to be a great success.","fill":"The event ___________ to be a great success."},
    {"pv":"weigh up","meaning":"consider carefully before making a decision","translation":"sopesar / valorar","example":"You need to weigh up the pros and cons carefully.","fill":"You need to ___________ the pros and cons carefully."},
    {"pv":"work out","meaning":"find a solution; result; exercise","translation":"resolver / resultar / ejercitarse","example":"Fortunately, everything worked out in the end.","fill":"Fortunately, everything ___________ in the end."},
    {"pv":"write off","meaning":"dismiss as worthless; cancel a debt","translation":"descartar / dar por perdido","example":"Many experts wrote off the candidate early in the campaign.","fill":"Many experts ___________ the candidate early in the campaign."},
    {"pv":"boil down to","meaning":"be essentially reduced to; summarise as","translation":"reducirse a / resumirse en","example":"All his complaints boil down to one thing: he wants more money.","fill":"All his complaints ___________ one thing: he wants more money."},
    {"pv":"cover up","meaning":"conceal something wrong or embarrassing","translation":"encubrir / ocultar algo","example":"The investigation revealed an attempt to cover up the scandal.","fill":"The investigation revealed an attempt to ___________ the scandal."},
    {"pv":"cut corners","meaning":"do something badly to save time or money","translation":"hacer algo a medias / tomar atajos de baja calidad","example":"The builders cut corners, and the structure became unsafe.","fill":"The builders ___________, and the structure became unsafe."},
    {"pv":"fast-forward","meaning":"move quickly to a later point in time or action","translation":"avanzar rápido / saltarse al futuro","example":"Fast-forward ten years, and the city was unrecognisable.","fill":"___________ ten years, and the city was unrecognisable."},
    {"pv":"give away","meaning":"reveal something accidentally; donate for free","translation":"regalar / revelar (un secreto)","example":"His nervous smile gave away the fact that he was lying.","fill":"His nervous smile ___________ the fact that he was lying."},
    {"pv":"help out","meaning":"assist someone, especially in a difficult situation","translation":"echar una mano / ayudar","example":"She agreed to help out at the event over the weekend.","fill":"She agreed to ___________ at the event over the weekend."},
    {"pv":"mark down","meaning":"reduce the price of something","translation":"rebajar / poner en descuento","example":"All winter coats have been marked down by thirty per cent.","fill":"All winter coats have been ___________ by thirty per cent."},
    {"pv":"put up with","meaning":"tolerate something unpleasant","translation":"aguantar / tolerar","example":"I will not put up with this kind of behaviour any longer.","fill":"I will not ___________ this kind of behaviour any longer."},
    {"pv":"slow down","meaning":"reduce speed or pace; become less active","translation":"reducir la velocidad / calmarse","example":"The doctor advised him to slow down and reduce his workload.","fill":"The doctor advised him to ___________ and reduce his workload."},
]

VERBS_PREPOSITIONS = [
    {"verb":"abstain","prep":"from","meaning":"refrain from","translation":"abstenerse de","example":"She abstained from voting on the resolution.","fill":"She abstained ___________ voting on the resolution."},
    {"verb":"account","prep":"for","meaning":"explain or represent","translation":"explicar / representar","example":"How do you account for the sudden rise in costs?","fill":"How do you account ___________ the sudden rise in costs?"},
    {"verb":"adhere","prep":"to","meaning":"stick to or follow strictly","translation":"adherirse a / atenerse a","example":"All employees must adhere to the company's code of conduct.","fill":"All employees must adhere ___________ the company's code of conduct."},
    {"verb":"agree","prep":"on","meaning":"reach a shared decision","translation":"llegar a un acuerdo sobre","example":"Both parties agreed on the terms of the contract.","fill":"Both parties agreed ___________ the terms of the contract."},
    {"verb":"allude","prep":"to","meaning":"refer to indirectly","translation":"aludir a","example":"The speaker alluded to the recent scandal without naming anyone.","fill":"The speaker alluded ___________ the recent scandal without naming anyone."},
    {"verb":"amount","prep":"to","meaning":"add up to; be equivalent to","translation":"equivaler a / sumar","example":"His vague promises did not amount to much.","fill":"His vague promises did not amount ___________ much."},
    {"verb":"appeal","prep":"to","meaning":"attract or interest; make a formal request","translation":"apelar a / atraer","example":"The campaign was designed to appeal to younger voters.","fill":"The campaign was designed to appeal ___________ younger voters."},
    {"verb":"attribute","prep":"to","meaning":"regard as caused by","translation":"atribuir a","example":"The success was attributed to years of meticulous planning.","fill":"The success was attributed ___________ years of meticulous planning."},
    {"verb":"benefit","prep":"from","meaning":"gain an advantage from","translation":"beneficiarse de","example":"Students benefit considerably from personalised feedback.","fill":"Students benefit considerably ___________ personalised feedback."},
    {"verb":"cater","prep":"for","meaning":"provide what is needed by","translation":"atender / satisfacer las necesidades de","example":"The course caters for learners at all levels.","fill":"The course caters ___________ learners at all levels."},
    {"verb":"collaborate","prep":"with","meaning":"work jointly with","translation":"colaborar con","example":"They collaborated with researchers from five universities.","fill":"They collaborated ___________ researchers from five universities."},
    {"verb":"comply","prep":"with","meaning":"act in accordance with","translation":"cumplir con / acatar","example":"All contractors must comply with health and safety regulations.","fill":"All contractors must comply ___________ health and safety regulations."},
    {"verb":"concentrate","prep":"on","meaning":"focus attention on","translation":"concentrarse en","example":"Let us concentrate on solving the most urgent problems first.","fill":"Let us concentrate ___________ solving the most urgent problems first."},
    {"verb":"conform","prep":"to","meaning":"behave according to accepted standards","translation":"ajustarse a / conformarse con","example":"He refused to conform to the school's dress code.","fill":"He refused to conform ___________ the school's dress code."},
    {"verb":"consist","prep":"of","meaning":"be composed of","translation":"constar de / estar formado por","example":"The panel consists of five independent experts.","fill":"The panel consists ___________ five independent experts."},
    {"verb":"contribute","prep":"to","meaning":"give or supply to help achieve","translation":"contribuir a","example":"Chronic stress can contribute to serious health problems.","fill":"Chronic stress can contribute ___________ serious health problems."},
    {"verb":"deal","prep":"with","meaning":"take action on; handle","translation":"tratar con / ocuparse de","example":"The new policy aims to deal with rising inequality.","fill":"The new policy aims to deal ___________ rising inequality."},
    {"verb":"depend","prep":"on","meaning":"be determined by; rely on","translation":"depender de","example":"The outcome depends entirely on how well the team prepares.","fill":"The outcome depends entirely ___________ how well the team prepares."},
    {"verb":"devote","prep":"to","meaning":"give all of something to a particular activity","translation":"dedicar a / consagrar a","example":"He devoted his entire career to environmental research.","fill":"He devoted his entire career ___________ environmental research."},
    {"verb":"differ","prep":"from","meaning":"be unlike","translation":"diferir de / diferenciarse de","example":"This approach differs markedly from the conventional method.","fill":"This approach differs markedly ___________ the conventional method."},
    {"verb":"engage","prep":"in","meaning":"participate in; become involved in","translation":"participar en / embarcarse en","example":"Both sides agreed to engage in constructive dialogue.","fill":"Both sides agreed to engage ___________ constructive dialogue."},
    {"verb":"insist","prep":"on","meaning":"demand forcefully","translation":"insistir en / empeñarse en","example":"She insisted on receiving a written apology.","fill":"She insisted ___________ receiving a written apology."},
    {"verb":"interfere","prep":"with","meaning":"prevent from working properly","translation":"interferir con / entorpecer","example":"Excessive noise can interfere with concentration.","fill":"Excessive noise can interfere ___________ concentration."},
    {"verb":"invest","prep":"in","meaning":"put resources into","translation":"invertir en","example":"The company has decided to invest heavily in renewable energy.","fill":"The company has decided to invest heavily ___________ renewable energy."},
    {"verb":"object","prep":"to","meaning":"express opposition or disapproval","translation":"oponerse a / objetar","example":"Several board members objected to the proposed merger.","fill":"Several board members objected ___________ the proposed merger."},
    {"verb":"persevere","prep":"with","meaning":"continue in spite of difficulty","translation":"perseverar en","example":"It is worth persevering with the exercise, even when it is hard.","fill":"It is worth persevering ___________ the exercise, even when it is hard."},
    {"verb":"prevail","prep":"over","meaning":"prove more powerful than","translation":"prevalecer sobre / imponerse a","example":"Common sense eventually prevailed over fear.","fill":"Common sense eventually prevailed ___________ fear."},
    {"verb":"refrain","prep":"from","meaning":"stop oneself from doing","translation":"abstenerse de","example":"Please refrain from using mobile phones during the lecture.","fill":"Please refrain ___________ using mobile phones during the lecture."},
    {"verb":"result","prep":"in","meaning":"cause or bring about","translation":"resultar en / desembocar en","example":"The merger resulted in significant redundancies.","fill":"The merger resulted ___________ significant redundancies."},
    {"verb":"stem","prep":"from","meaning":"originate from","translation":"provenir de / tener su origen en","example":"Her confidence stems from years of dedicated practice.","fill":"Her confidence stems ___________ years of dedicated practice."},
    {"verb":"strive","prep":"for","meaning":"make great efforts to achieve","translation":"esforzarse por / aspirar a","example":"We should always strive for excellence in everything we do.","fill":"We should always strive ___________ excellence in everything we do."},
    {"verb":"subscribe","prep":"to","meaning":"agree with or support an idea","translation":"suscribir / estar de acuerdo con","example":"I do not subscribe to the view that competition always improves quality.","fill":"I do not subscribe ___________ the view that competition always improves quality."},
    {"verb":"succeed","prep":"in","meaning":"achieve something","translation":"lograr / conseguir","example":"After three attempts, she finally succeeded in passing the exam.","fill":"After three attempts, she finally succeeded ___________ passing the exam."},
    {"verb":"tamper","prep":"with","meaning":"interfere without permission","translation":"manipular / alterar","example":"It was clear that someone had tampered with the evidence.","fill":"It was clear that someone had tampered ___________ the evidence."},
    {"verb":"yield","prep":"to","meaning":"give way to pressure or demands","translation":"ceder ante","example":"The government eventually yielded to pressure from trade unions.","fill":"The government eventually yielded ___________ pressure from trade unions."},
]

COLLOCATIONS = [
    {"adj_noun":"reach a consensus","translation":"llegar a un consenso","example":"After hours of debate, the committee reached a consensus.","fill":"After hours of debate, the committee ___________."},
    {"adj_noun":"make concessions","translation":"hacer concesiones","example":"Both sides had to make concessions to reach an agreement.","fill":"Both sides had to ___________ to reach an agreement."},
    {"adj_noun":"draw a distinction","translation":"establecer una distinción","example":"It is important to draw a distinction between correlation and causation.","fill":"It is important to ___________ between correlation and causation."},
    {"adj_noun":"raise awareness","translation":"concienciar / sensibilizar","example":"The campaign was launched to raise awareness of mental health issues.","fill":"The campaign was launched to ___________ of mental health issues."},
    {"adj_noun":"cast doubt on","translation":"poner en duda","example":"New findings cast doubt on the validity of the original study.","fill":"New findings ___________ the validity of the original study."},
    {"adj_noun":"shed light on","translation":"arrojar luz sobre","example":"The documentary sheds light on the lives of migrant workers.","fill":"The documentary ___________ the lives of migrant workers."},
    {"adj_noun":"bear the brunt of","translation":"sufrir lo peor de","example":"The poorest communities bear the brunt of economic downturns.","fill":"The poorest communities ___________ economic downturns."},
    {"adj_noun":"bridge the gap","translation":"acortar la brecha / salvar la distancia","example":"Education can help bridge the gap between different social groups.","fill":"Education can help ___________ between different social groups."},
    {"adj_noun":"strike a balance","translation":"encontrar un equilibrio","example":"It is difficult to strike a balance between work and personal life.","fill":"It is difficult to ___________ between work and personal life."},
    {"adj_noun":"take precedence over","translation":"tener prioridad sobre","example":"Public safety must take precedence over financial considerations.","fill":"Public safety must ___________ financial considerations."},
    {"adj_noun":"come to terms with","translation":"asumir / hacer las paces con","example":"It took him years to come to terms with the loss.","fill":"It took him years to ___________ the loss."},
    {"adj_noun":"run counter to","translation":"ir en contra de / contradecir","example":"The proposal runs counter to established scientific evidence.","fill":"The proposal ___________ established scientific evidence."},
    {"adj_noun":"give credence to","translation":"dar credibilidad a","example":"The leaked documents give credence to the allegations.","fill":"The leaked documents ___________ the allegations."},
    {"adj_noun":"meet a demand","translation":"satisfacer una demanda","example":"The company struggled to meet a demand for its products.","fill":"The company struggled to ___________ for its products."},
    {"adj_noun":"pose a threat","translation":"representar una amenaza","example":"Climate change can pose a threat to biodiversity if left unchecked.","fill":"Climate change can ___________ to biodiversity if left unchecked."},
    {"adj_noun":"defy expectations","translation":"ir contra las expectativas","example":"Small enterprises often defy expectations by outperforming larger rivals.","fill":"Small enterprises often ___________ by outperforming larger rivals."},
    {"adj_noun":"uphold a principle","translation":"defender / mantener un principio","example":"Courts are expected to uphold a principle of equal treatment.","fill":"Courts are expected to ___________ of equal treatment."},
    {"adj_noun":"exert pressure on","translation":"ejercer presión sobre","example":"Lobby groups regularly exert pressure on governments to change policy.","fill":"Lobby groups regularly ___________ governments to change policy."},
    {"adj_noun":"reach a turning point","translation":"llegar a un punto de inflexión","example":"Negotiations can reach a turning point when both sides compromise.","fill":"Negotiations can ___________ when both sides compromise."},
    {"adj_noun":"fall short of","translation":"no alcanzar / quedarse por debajo de","example":"The results fall short of what was promised in the original proposal.","fill":"The results ___________ what was promised in the original proposal."},
    {"adj_noun":"gain momentum","translation":"ganar impulso / cobrar fuerza","example":"Reform movements gain momentum when they achieve small visible victories.","fill":"Reform movements ___________ when they achieve small visible victories."},
    {"adj_noun":"paint a picture of","translation":"dar una imagen de / describir","example":"Statistics alone cannot paint a picture of the human cost of poverty.","fill":"Statistics alone cannot ___________ the human cost of poverty."},
    {"adj_noun":"tackle an issue","translation":"abordar un problema","example":"There is no easy way to tackle an issue as complex as climate change.","fill":"There is no easy way to ___________ as complex as climate change."},
    {"adj_noun":"yield results","translation":"dar resultados","example":"Only consistent effort will yield results over the long term.","fill":"Only consistent effort will ___________ over the long term."},
    {"adj_noun":"carry implications for","translation":"tener implicaciones para","example":"Such findings carry implications for both policy and practice.","fill":"Such findings ___________ both policy and practice."},
]

CONNECTORS = {
    "Addition": [
        {"word":"furthermore","translation":"además / es más","example":"The plan is cost-effective; furthermore, it has the support of all stakeholders.","fill":"The plan is cost-effective; ___________, it has the support of all stakeholders."},
        {"word":"moreover","translation":"es más / asimismo","example":"The plan is efficient; moreover, it is financially viable.","fill":"The plan is efficient; ___________, it is financially viable."},
        {"word":"in addition to","translation":"además de","example":"In addition to the financial costs, there are significant social consequences.","fill":"___________ the financial costs, there are significant social consequences."},
        {"word":"what is more","translation":"es más / encima","example":"The journey was long; what is more, the roads were in terrible condition.","fill":"The journey was long; ___________, the roads were in terrible condition."},
        {"word":"not only...but also","translation":"no solo… sino también","example":"Not only did she pass the exam, but she also achieved the highest mark.","fill":"___________ did she pass the exam, but she also achieved the highest mark."},
        {"word":"on top of that","translation":"encima de eso / para colmo","example":"He was late; on top of that, he had forgotten the documents.","fill":"He was late; ___________, he had forgotten the documents."},
    ],
    "Contrast": [
        {"word":"nevertheless","translation":"sin embargo / no obstante","example":"The task was challenging; nevertheless, the team completed it on time.","fill":"The task was challenging; ___________, the team completed it on time."},
        {"word":"nonetheless","translation":"sin embargo / a pesar de todo","example":"The evidence is limited; nonetheless, we must reach a decision.","fill":"The evidence is limited; ___________, we must reach a decision."},
        {"word":"on the contrary","translation":"al contrario / por el contrario","example":"I don't find it tedious — on the contrary, I find it fascinating.","fill":"I don't find it tedious — ___________, I find it fascinating."},
        {"word":"even so","translation":"aun así / con todo","example":"The risks were well known; even so, they decided to proceed.","fill":"The risks were well known; ___________, they decided to proceed."},
        {"word":"whereas","translation":"mientras que / en tanto que","example":"She prefers action films, whereas her sister enjoys documentaries.","fill":"She prefers action films, ___________ her sister enjoys documentaries."},
        {"word":"in contrast to","translation":"en contraste con / a diferencia de","example":"In contrast to last year, sales have risen sharply this quarter.","fill":"___________ last year, sales have risen sharply this quarter."},
        {"word":"by contrast","translation":"en cambio / por el contrario","example":"Nordic countries have low inequality; by contrast, the US has very high levels.","fill":"Nordic countries have low inequality; ___________, the US has very high levels."},
    ],
    "Concession": [
        {"word":"although","translation":"aunque / a pesar de que","example":"Although the evidence was compelling, the jury remained undecided.","fill":"___________ the evidence was compelling, the jury remained undecided."},
        {"word":"admittedly","translation":"hay que reconocer que / ciertamente","example":"The new system has some flaws; admittedly, it is still an improvement overall.","fill":"The new system has some flaws; ___________, it is still an improvement overall."},
        {"word":"granted","translation":"es cierto que / concedido","example":"Granted, it is an expensive solution, but it is by far the most effective.","fill":"___________, it is an expensive solution, but it is by far the most effective."},
        {"word":"while","translation":"si bien / aunque","example":"While I understand your concerns, the benefits outweigh the risks.","fill":"___________ I understand your concerns, the benefits outweigh the risks."},
        {"word":"notwithstanding","translation":"a pesar de / no obstante","example":"Notwithstanding the difficulties, the project was completed on schedule.","fill":"___________ the difficulties, the project was completed on schedule."},
        {"word":"despite","translation":"a pesar de","example":"Despite the harsh conditions, the expedition was a success.","fill":"___________ the harsh conditions, the expedition was a success."},
    ],
    "Cause & Result": [
        {"word":"consequently","translation":"en consecuencia / por consiguiente","example":"Funding was cut; consequently, the programme had to be abandoned.","fill":"Funding was cut; ___________, the programme had to be abandoned."},
        {"word":"as a result","translation":"como resultado / en consecuencia","example":"She trained hard every day; as a result, her performance improved significantly.","fill":"She trained hard every day; ___________, her performance improved significantly."},
        {"word":"therefore","translation":"por lo tanto / por ende","example":"The data is unreliable and therefore cannot be included in the analysis.","fill":"The data is unreliable and ___________ cannot be included in the analysis."},
        {"word":"hence","translation":"de ahí que / por eso","example":"The experiment failed, hence the need to redesign the protocol.","fill":"The experiment failed, ___________ the need to redesign the protocol."},
        {"word":"thus","translation":"así / por tanto","example":"Supply fell sharply, thus pushing prices upward.","fill":"Supply fell sharply, ___________ pushing prices upward."},
        {"word":"owing to","translation":"debido a / a causa de","example":"Owing to heavy rain, the outdoor event was postponed.","fill":"___________ heavy rain, the outdoor event was postponed."},
        {"word":"as a consequence","translation":"como consecuencia","example":"As a consequence of the merger, several jobs were lost.","fill":"___________ the merger, several jobs were lost."},
    ],
    "Purpose": [
        {"word":"in order to","translation":"con el fin de / para","example":"She revised her notes thoroughly in order to prepare for the oral exam.","fill":"She revised her notes thoroughly ___________ prepare for the oral exam."},
        {"word":"with a view to","translation":"con vistas a / con el objetivo de","example":"They met with a view to resolving the long-standing dispute.","fill":"They met ___________ resolving the long-standing dispute."},
        {"word":"with the aim of","translation":"con el propósito de / con el objetivo de","example":"The scheme was launched with the aim of reducing carbon emissions.","fill":"The scheme was launched ___________ reducing carbon emissions."},
        {"word":"for the purpose of","translation":"con el propósito de / a efectos de","example":"Personal data is collected for the purpose of improving user experience.","fill":"Personal data is collected ___________ improving user experience."},
        {"word":"so that","translation":"para que / de modo que","example":"The instructions were simplified so that everyone could follow them.","fill":"The instructions were simplified ___________ everyone could follow them."},
    ],
    "Exemplification": [
        {"word":"for instance","translation":"por ejemplo","example":"There are several viable solutions — for instance, we could postpone the launch.","fill":"There are several viable solutions — ___________, we could postpone the launch."},
        {"word":"such as","translation":"como / tales como","example":"Factors such as diet, sleep, and stress play a key role in overall wellbeing.","fill":"Factors ___________ diet, sleep, and stress play a key role in overall wellbeing."},
        {"word":"in particular","translation":"en particular / especialmente","example":"The report highlights several concerns, in particular the issue of funding.","fill":"The report highlights several concerns, ___________ the issue of funding."},
        {"word":"namely","translation":"a saber / concretamente","example":"Two candidates impressed us, namely Chen and Rivera.","fill":"Two candidates impressed us, ___________ Chen and Rivera."},
        {"word":"to illustrate","translation":"para ilustrar esto","example":"Costs have fallen sharply; to illustrate, solar prices dropped 90% in a decade.","fill":"Costs have fallen sharply; ___________, solar prices dropped 90% in a decade."},
    ],
    "Emphasis": [
        {"word":"above all","translation":"ante todo / sobre todo","example":"Above all, we need to ensure the safety of the local population.","fill":"___________, we need to ensure the safety of the local population."},
        {"word":"in particular","translation":"en particular","example":"I was struck, in particular, by the clarity of her argument.","fill":"I was struck, ___________, by the clarity of her argument."},
        {"word":"indeed","translation":"de hecho / efectivamente","example":"The results were, indeed, far better than anticipated.","fill":"The results were, ___________, far better than anticipated."},
        {"word":"in fact","translation":"de hecho","example":"The situation is, in fact, more complex than it first appears.","fill":"The situation is, ___________, more complex than it first appears."},
        {"word":"it is worth noting that","translation":"cabe señalar que / es de señalar que","example":"It is worth noting that the majority of respondents were under thirty.","fill":"___________ the majority of respondents were under thirty."},
    ],
}

# ════════════════════════════════════════════════════════════════════════════
#  IDIOMS & EXPRESSIONS
# ════════════════════════════════════════════════════════════════════════════

IDIOMS = [
    {"idiom":"a piece of cake","translation":"pan comido / muy fácil","meaning":"something very easy to do","example":"I was worried about the driving test, but it was a piece of cake.","fill":"I was worried about the driving test, but it was ___________."},
    {"idiom":"hit the nail on the head","translation":"dar en el clavo","meaning":"describe exactly what is causing a situation or problem","example":"You really hit the nail on the head — that is exactly what is wrong with the system.","fill":"You really ___________ — that is exactly what is wrong with the system."},
    {"idiom":"every cloud has a silver lining","translation":"no hay mal que por bien no venga","meaning":"every difficult situation has a positive aspect","example":"She lost her job, but every cloud has a silver lining — she finally started her own business.","fill":"She lost her job, but every cloud has a ___________ — she finally started her own business."},
    {"idiom":"burn the midnight oil","translation":"trasnochar trabajando / quemarse las pestañas","meaning":"work late into the night","example":"She was burning the midnight oil to finish her dissertation before the deadline.","fill":"She was ___________ to finish her dissertation before the deadline."},
    {"idiom":"a taste of your own medicine","translation":"que te traten como tú tratas a los demás","meaning":"an experience of the same unpleasant treatment you give others","example":"He was always interrupting people, so it was a taste of his own medicine when nobody let him speak.","fill":"He was always interrupting people, so it was ___________ when nobody let him speak."},
    {"idiom":"not all it's cracked up to be","translation":"no tan bueno como lo pintan / no estar a la altura","meaning":"not as good as people say","example":"Fame is not all it's cracked up to be — it comes with a lot of pressure.","fill":"Fame is ___________ — it comes with a lot of pressure."},
    {"idiom":"cost an arm and a leg","translation":"costar un ojo de la cara","meaning":"be extremely expensive","example":"Getting a lawyer to handle the case cost an arm and a leg.","fill":"Getting a lawyer to handle the case ___________."},
    {"idiom":"a far cry from","translation":"muy diferente de / estar muy lejos de","meaning":"very different from","example":"This tiny flat is a far cry from the house she grew up in.","fill":"This tiny flat is ___________ the house she grew up in."},
    {"idiom":"bite off more than you can chew","translation":"abarcar más de lo que puedes / meterte en más de la cuenta","meaning":"take on more than you are able to handle","example":"He bit off more than he could chew when he agreed to manage three projects at once.","fill":"He ___________ when he agreed to manage three projects at once."},
    {"idiom":"be on the fence","translation":"estar indeciso / no tomar partido","meaning":"be undecided or uncommitted about something","example":"She is still on the fence about whether to accept the job offer abroad.","fill":"She is still ___________ about whether to accept the job offer abroad."},
    {"idiom":"cry over spilt milk","translation":"lamentarse por algo que no tiene remedio","meaning":"waste time feeling upset about something that cannot be changed","example":"There is no point crying over spilt milk — we need to focus on the next steps.","fill":"There is no point ___________ — we need to focus on the next steps."},
    {"idiom":"let sleeping dogs lie","translation":"no remover el pasado / dejar las cosas como están","meaning":"avoid raising a subject that could cause trouble","example":"I thought about asking for an explanation, but decided to let sleeping dogs lie.","fill":"I thought about asking for an explanation, but decided to ___________."},
    {"idiom":"see eye to eye","translation":"estar de acuerdo / ver las cosas de la misma manera","meaning":"agree with someone; share the same view","example":"The two directors rarely see eye to eye on budget decisions.","fill":"The two directors rarely ___________ on budget decisions."},
    {"idiom":"get the axe","translation":"ser despedido / (proyecto) ser cancelado","meaning":"be dismissed from a job, or (of a project) be cancelled","example":"Three departments got the axe in the latest round of cuts.","fill":"Three departments ___________ in the latest round of cuts."},
    {"idiom":"thus far","translation":"hasta ahora / hasta el momento","meaning":"up to this point; so far","example":"Thus far, no evidence has been found to support the allegations.","fill":"___________, no evidence has been found to support the allegations."},
    {"idiom":"stand to lose","translation":"correr el riesgo de perder / poder perder","meaning":"be in a position where one may lose something","example":"The company stands to lose millions if the deal collapses.","fill":"The company ___________ millions if the deal collapses."},
    {"idiom":"on the face of it","translation":"a primera vista / aparentemente","meaning":"judging by what can be seen; seemingly","example":"On the face of it, the proposal sounds reasonable, but the details are unclear.","fill":"___________, the proposal sounds reasonable, but the details are unclear."},
    {"idiom":"in hindsight","translation":"en retrospectiva / mirando atrás","meaning":"looking back on events with knowledge you now have","example":"In hindsight, accepting the deal without reading the small print was a mistake.","fill":"___________, accepting the deal without reading the small print was a mistake."},
    {"idiom":"take something with a pinch of salt","translation":"tomar algo con reservas / no creerse algo del todo","meaning":"not take something too seriously or literally; be sceptical","example":"I'd take those statistics with a pinch of salt — the methodology is questionable.","fill":"I'd ___________ those statistics — the methodology is questionable."},
    {"idiom":"the tip of the iceberg","translation":"la punta del iceberg","meaning":"a small visible part of a much larger hidden problem","example":"The redundancies announced this week are just the tip of the iceberg.","fill":"The redundancies announced this week are just ___________."},
    {"idiom":"go back to square one","translation":"volver a empezar desde cero","meaning":"return to the beginning after a failure","example":"The deal fell through, so we had to go back to square one.","fill":"The deal fell through, so we had to ___________."},
    {"idiom":"get the ball rolling","translation":"poner las cosas en marcha / dar el pistoletazo de salida","meaning":"start an activity or process","example":"The manager asked her to get the ball rolling on the new marketing strategy.","fill":"The manager asked her to ___________ on the new marketing strategy."},
    {"idiom":"be in the same boat","translation":"estar en la misma situación / estar en el mismo barco","meaning":"be in the same difficult situation as someone else","example":"We're all facing redundancy — we're in the same boat.","fill":"We're all facing redundancy — we're ___________."},
    {"idiom":"the elephant in the room","translation":"el elefante en la habitación / el tema que nadie quiere abordar","meaning":"an obvious problem or issue that everyone is aware of but avoids discussing","example":"Nobody mentioned the budget shortfall — it was the elephant in the room.","fill":"Nobody mentioned the budget shortfall — it was ___________."},
    {"idiom":"keep someone in the loop","translation":"mantener a alguien informado / al corriente","meaning":"keep someone informed about what is happening","example":"Please keep me in the loop regarding any developments with the contract.","fill":"Please ___________ regarding any developments with the contract."},
    {"idiom":"turn a blind eye to","translation":"hacer la vista gorda / mirar para otro lado","meaning":"deliberately ignore something wrong or illegal","example":"Management turned a blind eye to the safety violations for years.","fill":"Management ___________ the safety violations for years."},
    {"idiom":"the last straw","translation":"el colmo / la gota que colma el vaso","meaning":"the final problem in a series that makes a situation unbearable","example":"Being passed over for promotion was the last straw — she handed in her resignation.","fill":"Being passed over for promotion was ___________ — she handed in her resignation."},
    {"idiom":"play it by ear","translation":"improvisar / decidir sobre la marcha","meaning":"proceed without a fixed plan; decide as you go","example":"We don't have a set agenda for the meeting — let's just play it by ear.","fill":"We don't have a set agenda for the meeting — let's just ___________."},
]

# ════════════════════════════════════════════════════════════════════════════
#  CONFUSING EXPRESSIONS
# ════════════════════════════════════════════════════════════════════════════

CONFUSING_EXPRESSIONS = {
    "I can tell / You can tell": {
        "title": "I can tell / You can tell",
        "explanation": "'**Can tell**' does NOT mean *hablar* — it means **noticing or perceiving** something. It is used to express that someone is able to sense or deduce something from evidence.\n\n⚠️ Common mistake: *'I can tell you'* ≠ *'Te puedo decir'* (that's **I can tell you** = I can say). In this usage 'tell' = **darse cuenta / notar**.",
        "forms": [
            {"expression":"I can tell","spanish":"Puedo notar / Me doy cuenta","example":"I can tell you're nervous — your hands are shaking.","note":"Speaker perceives something about the other person"},
            {"expression":"You can tell","spanish":"Se nota / Es evidente","example":"You can tell she has worked very hard — the results speak for themselves.","note":"General observation, equivalent to 'it's obvious'"},
            {"expression":"I couldn't tell","spanish":"No me di cuenta / No sabría decirlo","example":"I couldn't tell they were twins — they look so different.","note":"Past: failed to notice or distinguish"},
            {"expression":"How can you tell?","spanish":"¿Cómo lo notas? / ¿Cómo sabes?","example":"How can you tell she's upset if she seems perfectly calm?","note":"Asking what the evidence is"},
            {"expression":"Can you tell the difference?","spanish":"¿Puedes notar la diferencia?","example":"Can you tell the difference between these two wines?","note":"Used for distinguishing between things"},
        ],
        "exercises": [
            {"prompt":"___ you're tired — you keep yawning. (I / can / tell)","answer":"I can tell"},
            {"prompt":"___ it's going to be a tough negotiation from the look on his face.","answer":"You can tell"},
            {"prompt":"___ they were sisters — they have completely different personalities.","answer":"I couldn't tell"},
            {"prompt":"'___ she's lying?' 'Because she won't make eye contact.'","answer":"How can you tell"},
        ],
    },
    "I'm afraid": {
        "title": "I'm afraid — 4 different meanings",
        "explanation": "'**I'm afraid**' is one of the most versatile expressions in English. The meaning changes **entirely** depending on the context. It is NOT always about fear!\n\n⚠️ In most formal or conversational contexts, 'I'm afraid' is a **softener** — a polite way to say something negative or to disagree.",
        "forms": [
            {"expression":"I'm afraid (literal fear)","spanish":"Tengo miedo","example":"I'm afraid of spiders — I can't be in the same room as them.","note":"The ONLY case where it means actual fear"},
            {"expression":"I'm afraid (cancelling/bad news)","spanish":"Me temo que / Lamentablemente","example":"I'm afraid I won't be able to attend the meeting tomorrow.","note":"Polite way to deliver disappointing news"},
            {"expression":"I'm afraid (correcting someone)","spanish":"Me temo que / La verdad es que...","example":"I'm afraid that figure is incorrect — the actual number is 42%.","note":"Softens a correction; avoids sounding harsh"},
            {"expression":"I'm afraid so / I'm afraid not","spanish":"Me temo que sí / Me temo que no","example":"'Is the project over budget?' 'I'm afraid so.'","note":"Short polite responses to yes/no questions with bad news"},
        ],
        "exercises": [
            {"situation":"You need to cancel plans with a friend.","prompt":"Complete: I'm afraid ___","answer":"I'm afraid I won't be able to make it tonight. / I'm afraid I have to cancel."},
            {"situation":"Someone states an incorrect fact. You need to correct them politely.","prompt":"Complete: I'm afraid ___","answer":"I'm afraid that's not quite right. / I'm afraid the correct figure is…"},
            {"situation":"Someone asks if the train has already left.","prompt":"Answer with 'I'm afraid…'","answer":"I'm afraid so."},
            {"situation":"Someone asks if there are any tickets left.","prompt":"Answer with 'I'm afraid…'","answer":"I'm afraid not. / I'm afraid there are none left."},
        ],
    },
    "May vs Might vs Should": {
        "title": "May / Might / Should — What's the difference?",
        "explanation": "These three modal verbs cause confusion because they all express **possibility or expectation**, but at different levels.\n\n| Modal | Use | Certainty |\n|---|---|---|\n| **May** | Real possibility (likely) | ~50% |\n| **Might** | Remote possibility (unlikely/hypothetical) | ~30% |\n| **Should** | Expectation / advice / obligation | ~80% |\n\n⚠️ **May vs Might**: In modern English the distinction is softening, but in formal/written English: *may* = more likely, *might* = more uncertain.\n\n⚠️ **Should** can mean: (1) advice (*You should see a doctor*), (2) expectation (*The report should be ready by Monday*), (3) mild obligation (*Staff should comply with the policy*), (4) in formal subjunctive structures (*I recommend that she should apply*).",
        "forms": [
            {"expression":"may + infinitive","spanish":"puede que / es posible que (probable)","example":"It may rain this afternoon — bring an umbrella just in case.","note":"Real likelihood (~50%)"},
            {"expression":"might + infinitive","spanish":"podría / quizás (menos probable)","example":"It might snow, but the forecast looks fine so far.","note":"More uncertain or hypothetical (~30%)"},
            {"expression":"should + infinitive","spanish":"debería / es de esperar que","example":"The results should be available by the end of the week.","note":"Expectation: something is likely based on logic"},
            {"expression":"may have + past participle","spanish":"puede que haya... (pasado)","example":"She may have already left — I didn't see her at the event.","note":"Past possibility (likely)"},
            {"expression":"might have + past participle","spanish":"podría haber... (pasado hipotético)","example":"If you had called, she might have answered.","note":"Past hypothetical or missed opportunity"},
            {"expression":"should have + past participle","spanish":"debería haber... (crítica del pasado)","example":"You should have told me earlier — I could have helped.","note":"Criticism or regret about the past"},
        ],
        "exercises": [
            {"prompt":"It ___ be too late to apply — the deadline was yesterday. (possibility, unlikely)","answer":"might"},
            {"prompt":"You ___ study the key word transformation exercises — they always come up. (advice)","answer":"should"},
            {"prompt":"She ___ have misunderstood the instructions — her answer is completely different. (past possibility)","answer":"may have / might have"},
            {"prompt":"The train ___ arrive at 9 — it's usually on time. (expectation)","answer":"should"},
            {"prompt":"He ___ be at home — try calling him. (possibility, likely)","answer":"may / might"},
            {"prompt":"I ___ told her the truth from the beginning. (regret about past)","answer":"should have"},
        ],
    },
    "used to / be used to / would": {
        "title": "used to / be used to / get used to / would",
        "explanation": "These structures are among the **most commonly confused** by Spanish speakers at C1/C2 level. They look similar but mean completely different things.\n\n| Structure | Meaning | Spanish |\n|---|---|---|\n| **used to + infinitive** | Past habit (no longer true) | *solía / antes...* |\n| **be used to + -ing/noun** | Accustomed to (current state) | *estar acostumbrado a* |\n| **get used to + -ing/noun** | Process of becoming accustomed | *acostumbrarse a* |\n| **would + infinitive** | Past habit (narrative, formal) | *solía (acciones)* |\n\n⚠️ **would** can ONLY replace *used to* for repeated ACTIONS, NOT states: ❌ *I would be shy* → ✅ *I used to be shy*\n\n⚠️ After **be/get used to**, you MUST use **-ing**: ❌ *I'm used to work late* → ✅ *I'm used to working late*",
        "forms": [
            {"expression":"used to + infinitive","spanish":"solía / antes (ya no)","example":"She used to live in Barcelona before moving to London.","note":"Past habit or state — NO LONGER TRUE. Cannot use 'would' for states."},
            {"expression":"would + infinitive","spanish":"solía (solo acciones repetidas)","example":"Every summer, he would rent a house by the sea.","note":"Past repeated ACTION only. More literary/formal than 'used to'."},
            {"expression":"be used to + -ing","spanish":"estar acostumbrado a","example":"She is used to working long hours — it doesn't bother her.","note":"CURRENT state of familiarity. -ing is MANDATORY after 'to'."},
            {"expression":"get used to + -ing","spanish":"acostumbrarse a (proceso)","example":"It took him months to get used to driving on the left.","note":"PROCESS of adapting. -ing is MANDATORY. 'Get' shows change."},
        ],
        "exercises": [
            {"prompt":"When I was a child, I ___ (walk) to school every day. (past habit)","answer":"used to walk / would walk"},
            {"prompt":"I'm finding the new schedule difficult, but I'm sure I'll ___ it soon. (adapt)","answer":"get used to it"},
            {"prompt":"He ___ (be) very shy, but now he speaks confidently in public. (no longer true state)","answer":"used to be (NOT 'would be')"},
            {"prompt":"She ___ working under pressure — she's done it her whole career. (accustomed to)","answer":"is used to working"},
            {"prompt":"Which is correct? A) I'm used to get up early. B) I'm used to getting up early.","answer":"B) I'm used to getting up early. (After 'used to' as adjective, -ing is required.)"},
            {"prompt":"Every morning, my grandfather ___ (read) the newspaper with his coffee. (past habit, action)","answer":"would read / used to read"},
        ],
    },
    "make vs do": {
        "title": "Make vs Do — the 'hacer' problem",
        "explanation": "Spanish has ONE verb (*hacer*) where English has TWO. This is one of the most persistent errors for Spanish speakers at ALL levels, including C1/C2.\n\n**General rule:**\n- **MAKE** → creating, producing, constructing something (resultado tangible)\n- **DO** → actions, tasks, activities, work (proceso, actividad)\n\n⚠️ BUT: English is full of **fixed collocations** that defy the rule — you simply have to memorise them.\n\n🔴 **Common errors:** ~~make a mistake~~ no, wait — that's correct! But: ❌ *make homework* → ✅ *do homework* | ❌ *do a photo* → ✅ *take a photo*",
        "forms": [
            {"expression":"make + noun (creation/result)","spanish":"hacer (producir)","example":"She made an excellent speech at the conference.","note":"make a speech/decision/mistake/effort/progress/exception/impression"},
            {"expression":"do + noun (activity/task)","spanish":"hacer (actividad)","example":"Have you done your homework yet?","note":"do homework/research/business/a course/damage/harm/work/exercise"},
            {"expression":"Fixed: make + decision","spanish":"tomar una decisión","example":"The board needs to make a decision by Friday.","note":"NOT 'do a decision'"},
            {"expression":"Fixed: do + research","spanish":"hacer/llevar a cabo una investigación","example":"She spent three years doing research into climate change.","note":"NOT 'make research'"},
            {"expression":"Fixed: make + progress","spanish":"progresar / avanzar","example":"The patient is making remarkable progress.","note":"'Make progress' is fixed — never 'do progress'"},
            {"expression":"Fixed: do + harm/damage","spanish":"causar daño","example":"The scandal did considerable damage to his reputation.","note":"'Do harm', 'do damage' — NOT 'make harm'"},
        ],
        "exercises": [
            {"prompt":"She ___ a serious mistake by ignoring the warning signs. (make/do)","answer":"made"},
            {"prompt":"The scientists have been ___ extensive research into the causes of the disease. (make/do)","answer":"doing"},
            {"prompt":"The government needs to ___ a decision on the new infrastructure project. (make/do)","answer":"make"},
            {"prompt":"Lack of sleep can ___ serious harm to your long-term health. (make/do)","answer":"do"},
            {"prompt":"The company has ___ significant progress in reducing its carbon footprint. (make/do)","answer":"made"},
            {"prompt":"Could you ___ me a favour and check these figures? (make/do)","answer":"do"},
        ],
    },
    "False Friends": {
        "title": "False Friends — Falsos amigos C1/C2",
        "explanation": "**False friends** (*falsos amigos*) are words that look identical or similar in Spanish and English but have **completely different meanings**. At C1/C2 level, these cause subtle but serious errors in both writing and speaking.\n\n⚠️ These are the false friends most frequently penalised in Cambridge C1/C2 exams.",
        "forms": [
            {"expression":"actually","spanish":"en realidad / de hecho (NOT actualmente)","example":"I thought the meeting was on Friday — actually, it's on Thursday.","note":"❌ 'Actually I am student' → ✅ 'Currently / At the moment I am a student'"},
            {"expression":"eventually","spanish":"finalmente / al final (NOT eventualmente)","example":"After years of hard work, she eventually got the promotion she deserved.","note":"❌ 'Eventually, something might happen' → ✅ 'Possibly / Perhaps something might happen'"},
            {"expression":"embarrassed","spanish":"avergonzado (NOT embarazada)","example":"He was embarrassed when he mispronounced the director's name in public.","note":"❌ 'She is embarrassed' (pregnant) → ✅ 'She is pregnant' / 'She is expecting'"},
            {"expression":"realise","spanish":"darse cuenta de (NOT realizar)","example":"I suddenly realised I had left my phone at home.","note":"❌ 'I realised my dream' (wrong register) → ✅ 'I achieved / fulfilled my dream'"},
            {"expression":"sensible","spanish":"sensato / razonable (NOT sensible)","example":"It was a sensible decision given the circumstances.","note":"❌ 'She is very sensible' (sensitive) → ✅ 'She is very sensitive'"},
            {"expression":"sympathetic","spanish":"comprensivo / empático (NOT simpático)","example":"The manager was sympathetic to her concerns about the workload.","note":"❌ 'He is very sympathetic' (nice/friendly) → ✅ 'He is very friendly / likeable'"},
            {"expression":"comprehensive","spanish":"exhaustivo / completo (NOT comprensivo)","example":"The report provides a comprehensive overview of the situation.","note":"❌ 'A comprehensive person' → ✅ 'An understanding person'"},
            {"expression":"involve","spanish":"implicar / suponer (NOT involucrarse)","example":"The project involves a significant amount of research.","note":"For 'involucrarse' → ✅ 'to get involved in / to be involved in'"},
        ],
        "exercises": [
            {"prompt":"I thought she was Spanish, but ___ she's from Argentina. (en realidad)","answer":"actually"},
            {"prompt":"After months of negotiations, they ___ reached an agreement. (al final)","answer":"eventually"},
            {"prompt":"He felt ___ when he forgot his colleague's name during the presentation. (avergonzado)","answer":"embarrassed"},
            {"prompt":"Only then did she ___ how serious the situation had become. (darse cuenta)","answer":"realise"},
            {"prompt":"Her advice was entirely ___ given the complexity of the situation. (sensato)","answer":"sensible"},
            {"prompt":"The doctor was very ___ and listened carefully to all her concerns. (comprensivo)","answer":"sympathetic"},
        ],
    },
    "look / seem / appear": {
        "title": "look / seem / appear / sound / feel — Linking verbs",
        "explanation": "These **linking verbs** (verbos copulativos) replace 'ser/estar/parecer' and are frequently misused at C1/C2 level. They are followed by **adjectives**, NOT adverbs.\n\n| Verb | Use | Spanish |\n|---|---|---|\n| **look** | visual appearance | parecer (visualmente) |\n| **seem** | general impression | parecer |\n| **appear** | formal; based on evidence | parecer (formal) |\n| **sound** | based on what you hear | sonar a / parecer (al oír) |\n| **feel** | physical/emotional sensation | sentirse |\n\n⚠️ Common C1/C2 errors:\n- ❌ *She looks happily* → ✅ *She looks happy* (adjective, not adverb)\n- ❌ *It looks like she is nervous* (visual) vs ✅ *It seems/appears that she is nervous* (impression)\n- ❌ *How does it look like?* → ✅ *What does it look like?*",
        "forms": [
            {"expression":"look + adjective","spanish":"tener aspecto de / parecer (visual)","example":"You look tired — have you been sleeping well?","note":"Visual appearance only. Followed by ADJECTIVE, never adverb."},
            {"expression":"look like + noun/clause","spanish":"parecerse a / parecer que","example":"That looks like a serious problem. / It looks like it's going to rain.","note":"'Look like' + noun or clause. NOT 'How does it look like?' → 'What does it look like?'"},
            {"expression":"seem + adjective/to-infinitive","spanish":"parecer (impresión general)","example":"She seems confident, but she is actually very nervous.","note":"General impression — not necessarily visual. 'Seem to be' is very common."},
            {"expression":"appear + adjective/to-infinitive","spanish":"parecer (formal, basado en evidencia)","example":"The company appears to be facing serious difficulties.","note":"More formal than 'seem'. Very common in academic and Cambridge writing."},
            {"expression":"sound + adjective","spanish":"sonar a / parecer (al oírlo)","example":"That sounds like a brilliant idea — tell me more.","note":"Based on what you HEAR or are told, not see."},
            {"expression":"feel + adjective","spanish":"sentirse / tener la sensación de","example":"I feel terrible about what happened — I should have acted sooner.","note":"Physical or emotional sensation. ❌ 'I feel terribly' (unless modifying a verb)."},
        ],
        "exercises": [
            {"prompt":"She ___ exhausted after the conference — she hadn't slept in two days. (visual appearance)","answer":"looked"},
            {"prompt":"The new proposal ___ to address all the concerns raised in the previous report. (formal impression)","answer":"appears"},
            {"prompt":"That ___ a reasonable solution given the constraints we are working with. (based on hearing)","answer":"sounds like"},
            {"prompt":"He ___ uncomfortable during the interview, though he tried to hide it. (general impression)","answer":"seemed"},
            {"prompt":"Correct this: 'The situation looks worryingly.' ","answer":"The situation looks worrying. (Adjective 'worrying', not adverb 'worryingly'.)"},
            {"prompt":"'___ does the new office look?' Fill with the correct question word.","answer":"What (NOT 'How') — 'What does it look like?'"},
        ],
    },
}

GRAMMAR_EXERCISES = [
    {
        "topic": "Inverted Conditionals",
        "explanation": "In **formal English**, 'if' can be omitted and the auxiliary moved before the subject:\n\n• **Had + subject + past participle** → If + subject + had + past participle\n→ *Had I known, I would have acted sooner.*\n\n• **Were + subject + to + infinitive** → If + subject + were to\n→ *Were she to resign, the company would be in difficulty.*\n\n• **Should + subject + infinitive** → If + subject + should\n→ *Should you need assistance, please contact us.*",
        "exercises": [
            {"instruction":"Rewrite using an inverted conditional:","prompt":"If she had prepared more carefully, she would have passed the exam.","answer":"Had she prepared more carefully, she would have passed the exam."},
            {"instruction":"Rewrite using an inverted conditional:","prompt":"If you should have any further questions, do not hesitate to contact us.","answer":"Should you have any further questions, do not hesitate to contact us."},
            {"instruction":"Rewrite using an inverted conditional:","prompt":"If he were to stand down, the party would face a leadership crisis.","answer":"Were he to stand down, the party would face a leadership crisis."},
            {"instruction":"Rewrite using an inverted conditional:","prompt":"If I had been informed earlier, I could have prevented the problem.","answer":"Had I been informed earlier, I could have prevented the problem."},
        ],
    },
    {
        "topic": "Cleft Sentences",
        "explanation": "**Cleft sentences** allow us to give special emphasis to one part of a sentence:\n\n• **It + be + emphasised element + relative clause**\n→ *It was the manager who made the final decision.*\n\n• **What + clause + be + emphasised element**\n→ *What we need is more time and resources.*\n\n• **The reason (why) + clause + be + that-clause**\n→ *The reason why she resigned is that she felt undervalued.*\n\n• **All + subject + verb + be + infinitive**\n→ *All I want is an honest explanation.*",
        "exercises": [
            {"instruction":"Rewrite as a cleft sentence emphasising the underlined element:","prompt":"**The marketing team** came up with the winning idea.","answer":"It was the marketing team that came up with the winning idea."},
            {"instruction":"Rewrite using 'What…':","prompt":"I need more time to complete this analysis.","answer":"What I need is more time to complete this analysis."},
            {"instruction":"Rewrite using 'The reason why…':","prompt":"She left the job because the hours were unsustainable.","answer":"The reason why she left the job is that the hours were unsustainable."},
            {"instruction":"Rewrite using 'All…':","prompt":"I simply want a straightforward explanation.","answer":"All I want is a straightforward explanation."},
        ],
    },
    {
        "topic": "Participle Clauses",
        "explanation": "**Participle clauses** replace adverbial or relative clauses in formal writing:\n\n• **Having + past participle** (completed action before the main verb)\n→ *Having reviewed the evidence, she reached a conclusion.*\n\n• **Past participle** (passive meaning in relative clauses)\n→ *The report, written by the director, caused debate.*\n\n• **Present participle** (simultaneous or causal)\n→ *Knowing the risks, he proceeded with caution.*\n\n• **Not + participle** (negative)\n→ *Not having received a reply, she sent a follow-up email.*",
        "exercises": [
            {"instruction":"Reduce to a participle clause:","prompt":"After she had reviewed all the evidence, she reached a conclusion.","answer":"Having reviewed all the evidence, she reached a conclusion."},
            {"instruction":"Reduce to a participle clause:","prompt":"The report, which was written by the director, caused considerable debate.","answer":"The report, written by the director, caused considerable debate."},
            {"instruction":"Reduce to a participle clause:","prompt":"Because he did not know the answer, he remained silent.","answer":"Not knowing the answer, he remained silent."},
            {"instruction":"Reduce to a participle clause:","prompt":"As she had not received a reply, she decided to contact them directly.","answer":"Not having received a reply, she decided to contact them directly."},
        ],
    },
    {
        "topic": "Subjunctive & Formal Structures",
        "explanation": "The **subjunctive** is used in formal English after verbs expressing commands, recommendations, or requirements:\n\n• **recommend / suggest / insist / demand / propose / require + that + subject + bare infinitive**\n→ *The committee recommended that the report be published immediately.*\n→ *It is essential that he attend every session.*\n\n• Note: In British English, 'should' is also common:\n→ *They suggested that she should apply for the position.*\n\n• Fixed expressions: *be that as it may; come what may; far be it from me to...*",
        "exercises": [
            {"instruction":"Complete with the correct subjunctive form:","prompt":"The inspector recommended that the building ___ (demolish) immediately.","answer":"The inspector recommended that the building be demolished immediately."},
            {"instruction":"Rewrite using a formal subjunctive:","prompt":"It is vital for all members to attend the annual general meeting.","answer":"It is vital that all members attend the annual general meeting."},
            {"instruction":"Rewrite using a formal subjunctive:","prompt":"They suggested that she should take a different approach.","answer":"They suggested that she take a different approach."},
            {"instruction":"Complete with the correct form:","prompt":"The board insisted that the CEO ___ (provide) a full written explanation.","answer":"The board insisted that the CEO provide a full written explanation."},
        ],
    },
    {
        "topic": "Passive & Reporting Structures",
        "explanation": "**Passive reporting structures** are used to distance the speaker from information:\n\n• **It is said/claimed/thought/believed/reported/alleged + that-clause**\n→ *It is widely believed that the economy will recover soon.*\n\n• **Subject + is/are + said/thought/reported + to + infinitive**\n→ *The minister is said to have resigned.*\n→ *The company is reported to be facing serious difficulties.*\n\n• **Subject + is/are + understood/known + to + perfect infinitive**\n→ *She is known to have been involved in the negotiations.*",
        "exercises": [
            {"instruction":"Rewrite using a passive reporting structure (beginning with 'It…'):","prompt":"People say that the new treatment is highly effective.","answer":"It is said that the new treatment is highly effective."},
            {"instruction":"Rewrite using a passive reporting structure (beginning with the subject):","prompt":"People believe that the suspect has fled the country.","answer":"The suspect is believed to have fled the country."},
            {"instruction":"Rewrite using a passive reporting structure:","prompt":"Experts report that the company is considering a takeover.","answer":"The company is reported to be considering a takeover."},
            {"instruction":"Rewrite beginning with the subject:","prompt":"People know that she played a crucial role in the negotiations.","answer":"She is known to have played a crucial role in the negotiations."},
        ],
    },
    {
        "topic": "Emphasis & Fronting",
        "explanation": "**Fronting** moves an element to the beginning of the sentence for emphasis:\n\n• **Fronted adverbial**: *Rarely have I seen such commitment.*\n• **Fronted object**: *This problem, we cannot ignore.*\n• **Fronted complement**: *Outstanding though the results were, much work remains.*\n\n**Inversion after negative/restrictive adverbials**:\n• *Never have I seen… | Not only did he… | No sooner had she… than… | Hardly had they… when…*\n• *Seldom does the committee agree unanimously.*",
        "exercises": [
            {"instruction":"Rewrite with fronting for emphasis (use inversion):","prompt":"I have rarely seen such dedication to a cause.","answer":"Rarely have I seen such dedication to a cause."},
            {"instruction":"Rewrite using 'Not only… but also':","prompt":"She won the award. She also gave a remarkable acceptance speech.","answer":"Not only did she win the award, but she also gave a remarkable acceptance speech."},
            {"instruction":"Rewrite using 'No sooner… than':","prompt":"She had barely sat down when her phone rang.","answer":"No sooner had she sat down than her phone rang."},
            {"instruction":"Rewrite using 'Seldom':","prompt":"The committee rarely reaches a unanimous decision.","answer":"Seldom does the committee reach a unanimous decision."},
        ],
    },
    {
        "topic": "Mixed Conditionals",
        "explanation": "**Mixed conditionals** combine different time references:\n\n• **Past condition → Present result** (unreal past → unreal present)\n→ *If she had studied medicine, she would be a doctor now.*\n→ If + past perfect | would + bare infinitive\n\n• **Present condition → Past result** (unreal present → unreal past)\n→ *If he were more careful, he would not have made that mistake.*\n→ If + past simple | would + have + past participle\n\n• **General truth → Past result**:\n→ *If she were not so talented, she would never have got the role.*",
        "exercises": [
            {"instruction":"Complete the mixed conditional:","prompt":"If she ___ (study) harder at university, she would have a better job now.","answer":"If she had studied harder at university, she would have a better job now."},
            {"instruction":"Complete the mixed conditional:","prompt":"If he ___ (be) more organised, he would not have missed the deadline.","answer":"If he were more organised, he would not have missed the deadline."},
            {"instruction":"Identify and correct the error:","prompt":"If they had invested earlier, they would be more wealthier now.","answer":"If they had invested earlier, they would be wealthier now. ('more wealthier' is incorrect — 'wealthier' already forms the comparative)"},
            {"instruction":"Write a mixed conditional sentence based on this situation:","prompt":"She didn't learn to drive as a teenager, so she can't take the job (which requires driving).","answer":"If she had learnt to drive as a teenager, she would be able to take the job."},
        ],
    },
    {
        "topic": "Hedging & Academic Tone",
        "explanation": "**Hedging** is essential in academic and formal writing to express uncertainty or caution:\n\n• **Modal verbs**: may, might, could, should (*This could suggest that…*)\n• **Adverbs**: apparently, arguably, presumably, seemingly (*Arguably, the results indicate…*)\n• **Verbs**: tend to, appear to, seem to, suggest (*The data appear to support…*)\n• **Nouns**: tendency, possibility, likelihood (*There is a possibility that…*)\n• **Passive + reporting verb**: It has been suggested that… | It would appear that…",
        "exercises": [
            {"instruction":"Rewrite adding appropriate hedging language:","prompt":"The new policy will cause unemployment to rise.","answer":"The new policy could/may cause unemployment to rise. / The new policy appears likely to lead to an increase in unemployment."},
            {"instruction":"Rewrite using a hedging verb:","prompt":"The results prove that exercise improves mental health.","answer":"The results suggest that exercise may improve mental health."},
            {"instruction":"Rewrite using a passive hedging structure:","prompt":"Experts think that the situation is improving.","answer":"It is thought that the situation may be improving."},
            {"instruction":"Add hedging language to make this less assertive:","prompt":"The increase in temperature is caused by human activity.","answer":"The increase in temperature is arguably/largely caused by human activity. / It would appear that the increase in temperature is caused, at least in part, by human activity."},
        ],
    },
]

USE_OF_ENGLISH = {
    # ── PART 4: Key Word Transformation ─────────────────────────────────────
    # 8 key patterns tested (>90% of exam questions):
    # 1. Passive/Reporting  2. Conditionals  3. Reported Speech
    # 4. Time expressions   5. Modal verbs   6. Causative have/get
    # 7. Cleft / emphasis   8. Set phrases / collocations
    "Key Word Transformation": [
        # PATTERN 1 — Passive & Reporting
        {"sentence":"They say he is the best candidate for the role.","key":"said","answer":"He is said to be the best candidate for the role.","pattern":"Passive reporting"},
        {"sentence":"Nobody told me about the change of plans.","key":"informed","answer":"I was not informed about the change of plans.","pattern":"Passive"},
        {"sentence":"The manager made everyone stay late.","key":"made","answer":"Everyone was made to stay late by the manager.","pattern":"Passive causative"},
        {"sentence":"People believe that the suspect has fled the country.","key":"believed","answer":"The suspect is believed to have fled the country.","pattern":"Passive reporting"},
        {"sentence":"Experts report that the company is struggling financially.","key":"reported","answer":"The company is reported to be struggling financially.","pattern":"Passive reporting"},
        {"sentence":"It is thought that the ancient temple was built in 300 BC.","key":"thought","answer":"The ancient temple is thought to have been built in 300 BC.","pattern":"Passive reporting"},
        # PATTERN 2 — Conditionals & Unless
        {"sentence":"If you don't hurry, you'll miss the train.","key":"unless","answer":"Unless you hurry, you'll miss the train.","pattern":"Conditional"},
        {"sentence":"She regrets not studying medicine.","key":"wishes","answer":"She wishes she had studied medicine.","pattern":"Unreal past / wish"},
        {"sentence":"I regret telling her the news so abruptly.","key":"wish","answer":"I wish I hadn't told her the news so abruptly.","pattern":"Wish + past perfect"},
        {"sentence":"Had I known about the problem, I would have helped.","key":"if","answer":"If I had known about the problem, I would have helped.","pattern":"Inverted conditional → standard"},
        {"sentence":"Provided that you study regularly, you will pass the exam.","key":"long","answer":"As long as you study regularly, you will pass the exam.","pattern":"Conditional connector"},
        # PATTERN 3 — Reported Speech
        {"sentence":"'I didn't take the money,' the accused said.","key":"denied","answer":"The accused denied taking the money.","pattern":"Reported speech — deny"},
        {"sentence":"'Why don't we meet earlier?' she said.","key":"suggested","answer":"She suggested meeting earlier.","pattern":"Reported speech — suggest"},
        {"sentence":"My friend advised me to see a doctor.","key":"suggested","answer":"My friend suggested that I (should) see a doctor.","pattern":"Reported speech — suggest"},
        {"sentence":"'I'll definitely finish by Friday,' she promised.","key":"promised","answer":"She promised to finish by Friday.","pattern":"Reported speech — promise"},
        {"sentence":"'You really should take a break,' he told me.","key":"urged","answer":"He urged me to take a break.","pattern":"Reported speech — urge"},
        # PATTERN 4 — Time expressions
        {"sentence":"I haven't spoken to her since last year.","key":"time","answer":"The last time I spoke to her was last year.","pattern":"Time expression"},
        {"sentence":"He started working here six months ago.","key":"for","answer":"He has been working here for six months.","pattern":"Present perfect + for"},
        {"sentence":"It was three years since she had visited her hometown.","key":"three","answer":"She hadn't visited her hometown for three years.","pattern":"Time expression"},
        {"sentence":"She immediately signed the contract on arriving at the office.","key":"sooner","answer":"No sooner had she arrived at the office than she signed the contract.","pattern":"No sooner… than (inversion)"},
        {"sentence":"He had barely sat down when his phone rang.","key":"sooner","answer":"No sooner had he sat down than his phone rang.","pattern":"No sooner… than (inversion)"},
        # PATTERN 5 — Modal verbs
        {"sentence":"It's possible that she has already left.","key":"may","answer":"She may have already left.","pattern":"Modal — possibility"},
        {"sentence":"It wasn't necessary for her to attend the meeting.","key":"need","answer":"She needn't have attended the meeting.","pattern":"Modal — needn't have"},
        {"sentence":"It was wrong of him to shout at the staff.","key":"shouldn't","answer":"He shouldn't have shouted at the staff.","pattern":"Modal — past criticism"},
        {"sentence":"He is unlikely to arrive before midnight.","key":"chance","answer":"There is little chance of him arriving before midnight.","pattern":"Modal — unlikelihood"},
        {"sentence":"It's possible that the package was lost in transit.","key":"might","answer":"The package might have been lost in transit.","pattern":"Modal — past possibility"},
        # PATTERN 6 — Causative have / get
        {"sentence":"A mechanic repaired her car.","key":"had","answer":"She had her car repaired (by a mechanic).","pattern":"Causative have"},
        {"sentence":"Someone stole his wallet while he was on the bus.","key":"had","answer":"He had his wallet stolen while he was on the bus.","pattern":"Causative have — negative event"},
        {"sentence":"The dentist is going to remove two of her teeth next week.","key":"get","answer":"She is going to get two of her teeth removed next week.","pattern":"Causative get"},
        # PATTERN 7 — Emphasis & Set expressions
        {"sentence":"It was such a boring film that I fell asleep.","key":"so","answer":"The film was so boring that I fell asleep.","pattern":"So… that"},
        {"sentence":"She spoke so quietly that nobody could hear her.","key":"audible","answer":"Her voice was barely audible to anyone in the room.","pattern":"Collocation — barely audible"},
        {"sentence":"I find it impossible to understand his motives.","key":"beyond","answer":"His motives are beyond my understanding.","pattern":"Set expression — beyond understanding"},
        {"sentence":"I have rarely seen such a dedicated team.","key":"rarely","answer":"Rarely have I seen such a dedicated team.","pattern":"Inversion with rarely"},
        {"sentence":"Not only was she late, she also forgot the documents.","key":"not","answer":"Not only was she late, but she also forgot the documents.","pattern":"Inversion — Not only"},
        # PATTERN 8 — Collocations & formal register
        {"sentence":"Despite working hard, he didn't pass the exam.","key":"although","answer":"Although he worked hard, he didn't pass the exam.","pattern":"Connector transformation"},
        {"sentence":"The project failed because the team lacked resources.","key":"due","answer":"The project failed due to a lack of resources.","pattern":"Connector transformation"},
        {"sentence":"We had to think carefully about all the options before deciding.","key":"consideration","answer":"We had to take all the options into consideration before deciding.","pattern":"Formal collocation"},
        {"sentence":"She can't stand people who arrive late to meetings.","key":"put","answer":"She can't put up with people who arrive late to meetings.","pattern":"Phrasal verb"},
        {"sentence":"He ignored all the advice his doctor gave him.","key":"notice","answer":"He took no notice of the advice his doctor gave him.","pattern":"Set expression — take no notice"},
        {"sentence":"The two scientists are working on the project jointly.","key":"collaboration","answer":"The two scientists are working on the project in collaboration.","pattern":"Formal register"},
    ],

    # ── PART 3: Word Formation ───────────────────────────────────────────────
    # Patterns: -ment (20%), un-/in- negatives (15%), -tion/-sion (15%),
    # person nouns -er/-or/-ist, adjectives -ive/-ous/-ful/-less/-able
    "Word Formation": [
        # Nouns from verbs
        {"base":"rely","prompt":"Her ___ on technology has grown significantly over the past decade. (RELY)","answer":"reliance"},
        {"base":"achieve","prompt":"The ___ of such outstanding results required years of dedication. (ACHIEVE)","answer":"achievement"},
        {"base":"persist","prompt":"Her ___ in the face of repeated setbacks was truly admirable. (PERSIST)","answer":"persistence"},
        {"base":"respond","prompt":"The government's ___ to the crisis was widely criticised as too slow. (RESPOND)","answer":"response"},
        {"base":"innovate","prompt":"The company's reputation for ___ has attracted investors worldwide. (INNOVATE)","answer":"innovation"},
        {"base":"consider","prompt":"She gave the matter careful ___ before reaching her conclusion. (CONSIDER)","answer":"consideration"},
        {"base":"appreciate","prompt":"Her ___ of classical music grew during her years studying in Vienna. (APPRECIATE)","answer":"appreciation"},
        {"base":"persevere","prompt":"___ is the key quality that distinguishes successful researchers. (PERSEVERE)","answer":"Perseverance"},
        {"base":"commit","prompt":"Her ___ to the project inspired everyone around her. (COMMIT)","answer":"commitment"},
        {"base":"manage","prompt":"Effective ___ of resources is crucial for any organisation. (MANAGE)","answer":"management"},
        {"base":"fulfil","prompt":"The sense of ___ she felt after the performance was overwhelming. (FULFIL)","answer":"fulfilment"},
        {"base":"judge","prompt":"His ___ of the situation turned out to be completely wrong. (JUDGE)","answer":"judgement"},
        # Nouns from adjectives
        {"base":"signify","prompt":"There has been no ___ improvement in air quality since the new regulations. (SIGNIFY)","answer":"significant"},
        {"base":"scrutinise","prompt":"The accounts have been subjected to intense public ___. (SCRUTINISE)","answer":"scrutiny"},
        {"base":"affluent","prompt":"The gap between ___ and poverty has widened considerably. (AFFLUENT)","answer":"affluence"},
        {"base":"subtle","prompt":"The distinction between the two concepts is one of ___. (SUBTLE)","answer":"subtlety"},
        {"base":"ambiguous","prompt":"There is some ___ in the wording of the contract. (AMBIGUOUS)","answer":"ambiguity"},
        {"base":"tolerant","prompt":"The city is known for its cultural ___ and openness. (TOLERANT)","answer":"tolerance"},
        {"base":"diverse","prompt":"The report highlights the ___ of approaches taken across different regions. (DIVERSE)","answer":"diversity"},
        # Adjectives from nouns/verbs
        {"base":"contradict","prompt":"The two studies produced entirely ___ findings. (CONTRADICT)","answer":"contradictory"},
        {"base":"knowledge","prompt":"She is exceptionally ___ about twentieth-century European history. (KNOWLEDGE)","answer":"knowledgeable"},
        {"base":"oblige","prompt":"Attendance at the seminar is ___ for all registered students. (OBLIGE)","answer":"obligatory"},
        {"base":"controversy","prompt":"The decision to close the hospital proved highly ___. (CONTROVERSY)","answer":"controversial"},
        {"base":"prevail","prompt":"The ___ view among experts is that further cuts are unavoidable. (PREVAIL)","answer":"prevailing"},
        {"base":"access","prompt":"The new ramp made the building fully ___ to wheelchair users. (ACCESS)","answer":"accessible"},
        {"base":"sustain","prompt":"Governments need to invest in ___ energy sources. (SUSTAIN)","answer":"sustainable"},
        # Adverbs
        {"base":"overwhelm","prompt":"The response to the charity appeal was ___ positive. (OVERWHELM)","answer":"overwhelmingly"},
        {"base":"consequent","prompt":"The factory closed, and ___ hundreds of workers lost their jobs. (CONSEQUENT)","answer":"consequently"},
        {"base":"remark","prompt":"She performed ___ well under pressure. (REMARK)","answer":"remarkably"},
        # Negatives with prefixes (un-, in-, dis-, mis-, ir-)
        {"base":"predict","prompt":"The long-term effects of the policy remain largely ___. (PREDICT)","answer":"unpredictable"},
        {"base":"responsible","prompt":"Driving under the influence is dangerously ___. (RESPONSIBLE)","answer":"irresponsible"},
        {"base":"approve","prompt":"The board expressed ___ of the proposed changes. (APPROVE)","answer":"disapproval"},
        {"base":"lead","prompt":"The advertising campaign was found to be deliberately ___. (LEAD)","answer":"misleading"},
        {"base":"avoidable","prompt":"Many of the complications were entirely ___. (AVOIDABLE)","answer":"unavoidable"},
        # Person nouns
        {"base":"investigate","prompt":"The case was handed over to a senior ___. (INVESTIGATE)","answer":"investigator"},
        {"base":"advocate","prompt":"She is a passionate ___ of prison reform. (ADVOCATE)","answer":"advocate"},
        {"base":"reside","prompt":"Long-term ___ of the neighbourhood opposed the development. (RESIDE)","answer":"residents"},
    ],

    # ── PART 1: Multiple Choice Cloze ────────────────────────────────────────
    # Tests vocabulary: collocations, fixed expressions, phrasal verbs, register
    "Multiple Choice Cloze": [
        {"sentence":"The new policy was met with widespread ___ from the business community.","options":["A) approval","B) resistance","C) compliance","D) encouragement"],"answer":"B","explanation":"'Resistance' collocates with 'met with' when something is opposed. This tests fixed collocations with 'met with'."},
        {"sentence":"She managed to ___ a deal with the investors at the very last minute.","options":["A) close","B) strike","C) make","D) take"],"answer":"B","explanation":"'Strike a deal' is a fixed collocation. This tests knowledge of verbs that collocate with 'deal'."},
        {"sentence":"The documentary ___ light on a rarely discussed social issue.","options":["A) put","B) cast","C) shed","D) threw"],"answer":"C","explanation":"'Shed light on' = make something clearer. A common Cambridge fixed expression."},
        {"sentence":"His behaviour was ___ out of character for someone so professional.","options":["A) distinctly","B) largely","C) highly","D) entirely"],"answer":"D","explanation":"'Entirely out of character' is the natural collocation. Tests adverb–adjective collocations."},
        {"sentence":"The research findings ___ into question the effectiveness of the treatment.","options":["A) called","B) brought","C) drew","D) cast"],"answer":"A","explanation":"'Call into question' = cast doubt on. Fixed phrase tested very frequently in Cambridge exams."},
        {"sentence":"The committee reached a ___ that the proposal should be withdrawn.","options":["A) resolution","B) conclusion","C) decision","D) settlement"],"answer":"B","explanation":"'Reach a conclusion' is the fixed collocation here. 'Decision' needs 'make', not 'reach', in this context."},
        {"sentence":"The organisation has gone to great ___ to ensure full transparency.","options":["A) lengths","B) distances","C) measures","D) levels"],"answer":"A","explanation":"'Go to great lengths' = make great efforts. A fixed idiomatic expression."},
        {"sentence":"She has a ___ grasp of the technical aspects of the project.","options":["A) solid","B) firm","C) tight","D) hard"],"answer":"A","explanation":"'A solid grasp of something' = thorough understanding. Tests adjective–noun collocations."},
        {"sentence":"The prime minister came ___ considerable criticism after the announcement.","options":["A) across","B) under","C) upon","D) through"],"answer":"B","explanation":"'Come under criticism/pressure/fire' is a fixed prepositional phrase meaning to be subjected to."},
        {"sentence":"The findings of the report ___ with official government statistics.","options":["A) contrast","B) compete","C) collide","D) clash"],"answer":"D","explanation":"'Clash with' = conflict with or be incompatible with. Tests verb–preposition collocations."},
        {"sentence":"The charity aims to raise ___ of the risks of social isolation.","options":["A) consciousness","B) awareness","C) understanding","D) knowledge"],"answer":"B","explanation":"'Raise awareness' is a fixed collocation. 'Raise consciousness' exists but is less common in this context."},
        {"sentence":"Her speech made a ___ impression on everyone who attended.","options":["A) lasting","B) remaining","C) continuing","D) staying"],"answer":"A","explanation":"'Make a lasting impression' is a fixed collocation. The others don't collocate with 'impression' in this way."},
        {"sentence":"The board ___ a decision to restructure the company after months of debate.","options":["A) did","B) made","C) took","D) reached"],"answer":"C","explanation":"'Take a decision' (formal British English) = 'make a decision'. Both are correct but 'take' is the key word tested here."},
        {"sentence":"His composure under pressure was ___ admired by his colleagues.","options":["A) widely","B) broadly","C) largely","D) greatly"],"answer":"A","explanation":"'Widely admired' is the fixed adverb–past participle collocation. 'Greatly' would also work but 'widely' is the stronger collocation here."},
        {"sentence":"The new initiative ___ a significant shift in government policy.","options":["A) signals","B) marks","C) shows","D) displays"],"answer":"B","explanation":"'Mark a shift/change/turning point' is a fixed collocation used in formal writing."},
    ],

    # ── PART 2: Open Cloze ───────────────────────────────────────────────────
    # Tests: articles, prepositions, pronouns, conjunctions, auxiliary verbs,
    # quantifiers, relative pronouns, linkers — ONE word per gap
    "Open Cloze": [
        {
            "title":"Technology & Society",
            "text":"The rapid pace of technological change has (1)___ rise to a range of ethical questions that society is only beginning to grapple (2)___. Critics argue that artificial intelligence, far (3)___ being a neutral tool, reflects the biases of those who create it. (4)___ is more, the concentration of data in the hands of a few corporations poses risks (5)___ democratic oversight. (6)___ these concerns are taken seriously, there is little doubt that regulation will need to keep pace with innovation.",
            "answers":{"1":"given","2":"with","3":"from","4":"What","5":"to","6":"Unless"},
            "tips":"Gap 1: fixed phrase 'give rise to'. Gap 2: 'grapple WITH'. Gap 3: 'far FROM being'. Gap 4: 'What is more' = connector. Gap 5: 'pose risks TO'. Gap 6: linker of condition."
        },
        {
            "title":"Urban Migration",
            "text":"It (1)___ widely acknowledged that urbanisation has transformed the social fabric of many countries. (2)___ growing numbers of people migrate from rural areas, cities face mounting pressure on housing and infrastructure. (3)___ all the challenges this entails, urban centres continue to attract those (4)___ seek better economic opportunities. Policymakers are increasingly aware (5)___ the need to strike a balance between economic growth and social cohesion, (6)___ as to avoid deepening existing inequalities.",
            "answers":{"1":"is","2":"As","3":"Despite","4":"who","5":"of","6":"so"},
            "tips":"Gap 1: passive structure 'It IS acknowledged'. Gap 2: linker showing simultaneous situation. Gap 3: concession preposition. Gap 4: relative pronoun for people. Gap 5: 'aware OF'. Gap 6: 'so as to' = purpose."
        },
        {
            "title":"The Value of Failure",
            "text":"Failure is (1)___ often perceived as something to be avoided at all costs. Yet (2)___ closer inspection, it becomes clear that setbacks play a crucial (3)___ in personal development. Some of the most successful entrepreneurs attribute (4)___ achievements not to their triumphs, but to the lessons learnt from their mistakes. (5)___ is not to say that failure should be welcomed for its (6)___ sake, but rather that our response to it defines our capacity for growth.",
            "answers":{"1":"all","2":"on","3":"role","4":"their","5":"This","6":"own"},
            "tips":"Gap 1: 'all too often' = fixed intensifying phrase. Gap 2: 'on closer inspection' = fixed expression. Gap 3: 'play a role'. Gap 4: possessive pronoun. Gap 5: referencing pronoun. Gap 6: 'for its own sake' = fixed phrase."
        },
        {
            "title":"The Future of Work",
            "text":"Automation is transforming the workplace at a pace (1)___ has few historical precedents. While many jobs are (2)___ to disappear, others will evolve, and entirely new roles will emerge. The key challenge facing governments and businesses (3)___ is how to equip workers with the skills they will need. (4)___ simply retraining existing workers, some economists argue that a more fundamental rethink of education is called (5)___. Without such investment, there is a real risk (6)___ large segments of the population will be left behind.",
            "answers":{"1":"that","2":"likely","3":"alike","4":"Beyond","5":"for","6":"that"},
            "tips":"Gap 1: relative pronoun for 'pace'. Gap 2: 'likely to disappear' = adverb. Gap 3: 'governments and businesses ALIKE' = fixed phrase. Gap 4: 'Beyond X-ing' = going further than. Gap 5: 'called FOR' = required. Gap 6: 'risk THAT' = introducing a that-clause."
        },
        {
            "title":"Cultural Heritage",
            "text":"Preserving cultural heritage has become (1)___ of the most pressing concerns of our time. Monuments and traditions that have survived (2)___ centuries are now threatened by climate change, urban development, and neglect. Governments (3)___ the world over have pledged resources to address this issue, (4)___ progress has been slow. Critics argue that without sustained funding, many sites will be lost (5)___ good. (6)___ the case may be, there can be no doubt that swift action is needed.",
            "answers":{"1":"one","2":"for","3":"across","4":"yet","5":"for","6":"Whatever"},
            "tips":"Gap 1: 'one of the most…' = superlative structure. Gap 2: 'survived FOR centuries'. Gap 3: 'across the world over' — no, 'ACROSS the world'. Gap 4: concessive connector. Gap 5: 'lost FOR good' = permanently. Gap 6: 'Whatever the case may be' = fixed concessive expression."
        },
    ],
}

# ════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ════════════════════════════════════════════════════════════════════════════

def init_state():
    defaults = {
        # scores
        "score_correct":0,"score_total":0,
        # vocab flashcard
        "vocab_idx":0,"vocab_revealed":False,
        # vocab fill
        "vocab_fill_idx":random.randint(0,len(VOCABULARY)-1),
        "vocab_fill_ans":"","vocab_fill_checked":False,
        # vocab quiz
        "vocab_quiz_idx":random.randint(0,len(VOCABULARY)-1),
        "vocab_quiz_options":[],"vocab_quiz_selected":None,"vocab_quiz_checked":False,
        # phrasal verbs flashcard
        "pv_idx":0,"pv_revealed":False,
        # phrasal verbs fill
        "pv_fill_idx":random.randint(0,len(PHRASAL_VERBS)-1),
        "pv_fill_ans":"","pv_fill_checked":False,
        # verbs+preps flashcard
        "vp_idx":0,"vp_revealed":False,
        # verbs+preps fill
        "vp_fill_idx":random.randint(0,len(VERBS_PREPOSITIONS)-1),
        "vp_fill_ans":"","vp_fill_checked":False,
        # collocations
        "coll_idx":0,"coll_revealed":False,
        "coll_fill_idx":random.randint(0,len(COLLOCATIONS)-1),
        "coll_fill_ans":"","coll_fill_checked":False,
        # connectors
        "conn_fill_flat_idx":0,"conn_fill_ans":"","conn_fill_checked":False,
        # grammar
        "gram_topic_idx":0,"gram_ex_idx":0,
        "gram_ans":"","gram_revealed":False,"gram_ai_fb":"",
        # kwt
        "kwt_idx":0,"kwt_ans":"","kwt_checked":False,
        # word formation
        "wf_idx":0,"wf_ans":"","wf_checked":False,
        # mcc
        "mcc_idx":0,"mcc_selected":None,"mcc_checked":False,
        # open cloze
        "oc_idx":0,"oc_answers":{},"oc_checked":False,
        # idioms
        "idiom_idx":0,"idiom_revealed":False,
        "idiom_fill_idx":0,"idiom_fill_ans":"","idiom_fill_checked":False,
        # confusing expressions
        "conf_topic":"I can tell / You can tell",
        "conf_ex_idx":0,"conf_ans":"","conf_revealed":False,
    }
    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

def add_score(correct:bool):
    st.session_state.score_total += 1
    if correct:
        st.session_state.score_correct += 1

# ════════════════════════════════════════════════════════════════════════════
#  AI HELPER
# ════════════════════════════════════════════════════════════════════════════

def get_ai_feedback(user_answer:str, correct_answer:str, context:str)->str:
    try:
        client = anthropic.Anthropic()
        r = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role":"user","content":f"""You are a Cambridge C1/C2 English examiner giving feedback to a Spanish-speaking student.

Context / exercise: {context}
Model answer: {correct_answer}
Student's answer: {user_answer}

Give concise feedback in 3–5 sentences:
1. Is the answer correct, partially correct, or incorrect?
2. If not fully correct, explain why and what the correct structure is.
3. A specific tip for this type of Cambridge exercise.
4. If partially correct, acknowledge what the student did well.

Be encouraging but precise. Write in English. No markdown, plain text only."""}])
        return r.content[0].text
    except Exception as e:
        return f"AI feedback unavailable: {str(e)}"

# ════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ════════════════════════════════════════════════════════════════════════════

st.sidebar.title("🎓 Laura_Inglés")
st.sidebar.markdown("**Cambridge C1/C2 Trainer**")
if st.session_state.score_total > 0:
    pct = int(100 * st.session_state.score_correct / st.session_state.score_total)
    st.sidebar.markdown(f"**Score:** {st.session_state.score_correct}/{st.session_state.score_total} ({pct}%)")
    st.sidebar.progress(st.session_state.score_correct / st.session_state.score_total)
st.sidebar.markdown("---")

section = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📚 Vocabulary",
    "⚡ Phrasal Verbs",
    "🔗 Verbs & Prepositions",
    "🤝 Collocations",
    "🔀 Connectors",
    "💬 Idioms & Expressions",
    "🔤 Confusing Expressions",
    "✍️ Grammar",
    "🎯 Use of English",
])

if st.sidebar.button("🔄 Reset score"):
    st.session_state.score_correct = 0
    st.session_state.score_total = 0
    st.rerun()

# ════════════════════════════════════════════════════════════════════════════
#  HOME
# ════════════════════════════════════════════════════════════════════════════

if section == "🏠 Home":
    st.title("🎓 Laura_Inglés")
    st.markdown("#### Cambridge C1/C2 — Your personalised preparation tool")
    st.markdown("---")
    cols = st.columns(4)
    sections_info = [
        ("📚","Vocabulary",f"{len(VOCABULARY)} words","Translations · synonyms · antonyms · collocations · flashcards · fill-in-the-blanks · quiz"),
        ("⚡","Phrasal Verbs",f"{len(PHRASAL_VERBS)} phrasal verbs","Translations · flashcards · fill-in-the-blanks"),
        ("🔗","Verbs & Prepositions",f"{len(VERBS_PREPOSITIONS)} combinations","Translations · flashcards · fill-in-the-blanks"),
        ("🤝","Collocations",f"{len(COLLOCATIONS)} collocations","Translations · flashcards · fill-in-the-blanks"),
        ("🔀","Connectors",f"{sum(len(v) for v in CONNECTORS.values())} connectors","7 categories · study · fill-in-the-blanks"),
        ("💬","Idioms & Expressions",f"{len(IDIOMS)} idioms","Translations · flashcards · fill-in-the-blanks"),
        ("🔤","Confusing Expressions","3 topics","I can tell · I'm afraid · May/Might/Should"),
        ("✍️","Grammar",f"{len(GRAMMAR_EXERCISES)} topics","Advanced structures · exercises · AI feedback"),
        ("🎯","Use of English","4 exercise types","KWT · Word Formation · MCC · Open Cloze"),
    ]
    for i,(icon,name,count,desc) in enumerate(sections_info):
        with cols[i % 4]:
            st.info(f"{icon} **{name}**\n\n*{count}*\n\n{desc}")
    st.markdown("---")
    st.markdown("💡 **Tips:** Work through sections in order. Use AI Feedback in Grammar to check open answers. Track your score in the sidebar.")

# ════════════════════════════════════════════════════════════════════════════
#  VOCABULARY
# ════════════════════════════════════════════════════════════════════════════

elif section == "📚 Vocabulary":
    st.title("📚 Vocabulary")
    tab1, tab2, tab3 = st.tabs(["Flashcards", "Fill in the Blank", "Multiple Choice Quiz"])

    # ── Flashcards ──────────────────────────────────────────────────────────
    with tab1:
        idx = st.session_state.vocab_idx
        w = VOCABULARY[idx]
        st.markdown(f"*Word {idx+1} of {len(VOCABULARY)}*")
        st.progress((idx+1)/len(VOCABULARY))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">🃏 {w['word'].upper()}</div>
            <div class="translation">🇪🇸 {w['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.vocab_revealed:
            st.success(f"**Definition:** {w['definition']}")
            c1,c2 = st.columns(2)
            with c1:
                st.markdown("**Synonyms:** " + " · ".join([f"`{s}`" for s in w['synonyms']]))
            with c2:
                st.markdown("**Antonyms:** " + " · ".join([f"`{s}`" for s in w['antonyms']]))
            st.markdown(f'<div class="example-box">💬 <em>{w["example"]}</em></div>', unsafe_allow_html=True)
            st.markdown(f"📎 **Collocation:** *{w['collocation']}*")
        else:
            if st.button("👁️ Reveal definition, synonyms & example", use_container_width=True):
                st.session_state.vocab_revealed = True
                st.rerun()
        col1,col2,col3 = st.columns(3)
        with col1:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.vocab_idx = (idx-1) % len(VOCABULARY)
                st.session_state.vocab_revealed = False
                st.rerun()
        with col2:
            if st.button("🔀 Random", use_container_width=True):
                st.session_state.vocab_idx = random.randint(0,len(VOCABULARY)-1)
                st.session_state.vocab_revealed = False
                st.rerun()
        with col3:
            if st.button("Next ➡️", use_container_width=True):
                st.session_state.vocab_idx = (idx+1) % len(VOCABULARY)
                st.session_state.vocab_revealed = False
                st.rerun()

    # ── Fill in the Blank ────────────────────────────────────────────────────
    with tab2:
        fi = st.session_state.vocab_fill_idx
        fw = VOCABULARY[fi]
        import re as _re
        hidden = _re.sub(_re.escape(fw["word"]), "___________", fw["example"], count=1, flags=_re.IGNORECASE)
        st.markdown("**Complete the sentence with the correct word:**")
        st.markdown(f'<div class="example-box">{hidden}</div>', unsafe_allow_html=True)
        st.markdown(f"🇪🇸 *{fw['translation']}* | 📖 *{fw['definition']}*")
        ans = st.text_input("Your answer:", key="vocab_fill_input", value=st.session_state.vocab_fill_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="vf_check"):
                st.session_state.vocab_fill_ans = ans
                st.session_state.vocab_fill_checked = True
                correct = ans.strip().lower() == fw["word"].lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next sentence", use_container_width=True, key="vf_next"):
                st.session_state.vocab_fill_idx = random.randint(0,len(VOCABULARY)-1)
                st.session_state.vocab_fill_ans = ""
                st.session_state.vocab_fill_checked = False
                st.rerun()
        if st.session_state.vocab_fill_checked:
            if st.session_state.vocab_fill_ans.strip().lower() == fw["word"].lower():
                st.success(f"✅ Correct! **{fw['word']}** — {fw['definition']}")
            else:
                st.error(f"❌ The answer is: **{fw['word']}**")
                st.markdown("**Synonyms:** " + " · ".join([f"`{s}`" for s in fw['synonyms']]))

    # ── Multiple Choice Quiz ─────────────────────────────────────────────────
    with tab3:
        qi = st.session_state.vocab_quiz_idx
        qw = VOCABULARY[qi]
        if not st.session_state.vocab_quiz_options:
            wrong = random.sample([v for v in VOCABULARY if v["word"] != qw["word"]], 3)
            opts = [qw["definition"]] + [v["definition"] for v in wrong]
            random.shuffle(opts)
            st.session_state.vocab_quiz_options = opts
        st.markdown("**What is the meaning of this word?**")
        st.markdown(f"""<div class="flashcard" style="padding:1.2rem 2rem;">
            <div class="word-title">{qw['word'].upper()}</div>
            <div class="translation">🇪🇸 {qw['translation']}</div>
        </div>""", unsafe_allow_html=True)
        sel = st.radio("Choose the correct definition:", st.session_state.vocab_quiz_options,
                       index=None, key=f"vocab_quiz_{qi}")
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="vq_check"):
                st.session_state.vocab_quiz_selected = sel
                st.session_state.vocab_quiz_checked = True
                add_score(sel == qw["definition"])
                st.rerun()
        with c2:
            if st.button("➡️ Next word", use_container_width=True, key="vq_next"):
                st.session_state.vocab_quiz_idx = random.randint(0,len(VOCABULARY)-1)
                st.session_state.vocab_quiz_options = []
                st.session_state.vocab_quiz_selected = None
                st.session_state.vocab_quiz_checked = False
                st.rerun()
        if st.session_state.vocab_quiz_checked:
            if st.session_state.vocab_quiz_selected == qw["definition"]:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Correct definition: **{qw['definition']}**")
            st.markdown(f'<div class="example-box">💬 <em>{qw["example"]}</em></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  PHRASAL VERBS
# ════════════════════════════════════════════════════════════════════════════

elif section == "⚡ Phrasal Verbs":
    st.title("⚡ Phrasal Verbs")
    tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

    with tab1:
        idx = st.session_state.pv_idx
        pv = PHRASAL_VERBS[idx]
        st.markdown(f"*{idx+1} of {len(PHRASAL_VERBS)}*")
        st.progress((idx+1)/len(PHRASAL_VERBS))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">⚡ {pv['pv'].upper()}</div>
            <div class="translation">🇪🇸 {pv['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.pv_revealed:
            st.success(f"**Meaning:** {pv['meaning']}")
            st.markdown(f'<div class="example-box">💬 <em>{pv["example"]}</em></div>', unsafe_allow_html=True)
        else:
            if st.button("👁️ Reveal meaning & example", use_container_width=True, key="pv_reveal"):
                st.session_state.pv_revealed = True
                st.rerun()
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True, key="pv_prev"):
                st.session_state.pv_idx = (idx-1) % len(PHRASAL_VERBS)
                st.session_state.pv_revealed = False
                st.rerun()
        with c2:
            if st.button("🔀 Random", use_container_width=True, key="pv_rand"):
                st.session_state.pv_idx = random.randint(0,len(PHRASAL_VERBS)-1)
                st.session_state.pv_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="pv_next_fc"):
                st.session_state.pv_idx = (idx+1) % len(PHRASAL_VERBS)
                st.session_state.pv_revealed = False
                st.rerun()

    with tab2:
        fi = st.session_state.pv_fill_idx
        pv = PHRASAL_VERBS[fi]
        st.markdown("**Complete the sentence with the correct phrasal verb:**")
        st.markdown(f'<div class="example-box">{pv["fill"]}</div>', unsafe_allow_html=True)
        st.markdown(f"🇪🇸 *{pv['translation']}* | 📖 *{pv['meaning']}*")
        ans = st.text_input("Your answer:", key="pv_fill_input", value=st.session_state.pv_fill_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="pv_fill_check"):
                st.session_state.pv_fill_ans = ans
                st.session_state.pv_fill_checked = True
                correct = ans.strip().lower() == pv["pv"].lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="pv_fill_next"):
                st.session_state.pv_fill_idx = random.randint(0,len(PHRASAL_VERBS)-1)
                st.session_state.pv_fill_ans = ""
                st.session_state.pv_fill_checked = False
                st.rerun()
        if st.session_state.pv_fill_checked:
            if st.session_state.pv_fill_ans.strip().lower() == pv["pv"].lower():
                st.success(f"✅ Correct! **{pv['pv']}** — {pv['meaning']}")
            else:
                st.error(f"❌ The phrasal verb is: **{pv['pv']}**\n\n*{pv['example']}*")

# ════════════════════════════════════════════════════════════════════════════
#  VERBS & PREPOSITIONS
# ════════════════════════════════════════════════════════════════════════════

elif section == "🔗 Verbs & Prepositions":
    st.title("🔗 Verbs & Prepositions")
    tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

    with tab1:
        idx = st.session_state.vp_idx
        vp = VERBS_PREPOSITIONS[idx]
        st.markdown(f"*{idx+1} of {len(VERBS_PREPOSITIONS)}*")
        st.progress((idx+1)/len(VERBS_PREPOSITIONS))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">{vp['verb'].upper()} + ___?</div>
            <div class="translation">🇪🇸 {vp['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.vp_revealed:
            st.success(f"**{vp['verb']} {vp['prep']}** — {vp['meaning']}")
            st.markdown(f'<div class="example-box">💬 <em>{vp["example"]}</em></div>', unsafe_allow_html=True)
        else:
            if st.button("👁️ Reveal preposition & meaning", use_container_width=True, key="vp_reveal"):
                st.session_state.vp_revealed = True
                st.rerun()
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True, key="vp_prev"):
                st.session_state.vp_idx = (idx-1) % len(VERBS_PREPOSITIONS)
                st.session_state.vp_revealed = False
                st.rerun()
        with c2:
            if st.button("🔀 Random", use_container_width=True, key="vp_rand"):
                st.session_state.vp_idx = random.randint(0,len(VERBS_PREPOSITIONS)-1)
                st.session_state.vp_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="vp_next_fc"):
                st.session_state.vp_idx = (idx+1) % len(VERBS_PREPOSITIONS)
                st.session_state.vp_revealed = False
                st.rerun()

    with tab2:
        fi = st.session_state.vp_fill_idx
        vp = VERBS_PREPOSITIONS[fi]
        st.markdown("**Fill in the missing preposition:**")
        st.markdown(f'<div class="example-box">{vp["fill"]}</div>', unsafe_allow_html=True)
        st.markdown(f"*Verb: **{vp['verb']}** + ?* | 🇪🇸 *{vp['translation']}*")
        ans = st.text_input("Preposition:", key="vp_fill_input", value=st.session_state.vp_fill_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="vp_fill_chk"):
                st.session_state.vp_fill_ans = ans
                st.session_state.vp_fill_checked = True
                correct = ans.strip().lower() == vp["prep"].lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="vp_fill_nxt"):
                st.session_state.vp_fill_idx = random.randint(0,len(VERBS_PREPOSITIONS)-1)
                st.session_state.vp_fill_ans = ""
                st.session_state.vp_fill_checked = False
                st.rerun()
        if st.session_state.vp_fill_checked:
            if st.session_state.vp_fill_ans.strip().lower() == vp["prep"].lower():
                st.success(f"✅ Correct! **{vp['verb']} {vp['prep']}** — {vp['meaning']}")
            else:
                st.error(f"❌ Preposition: **{vp['prep']}** → *{vp['verb']} {vp['prep']}* — {vp['meaning']}")

# ════════════════════════════════════════════════════════════════════════════
#  COLLOCATIONS
# ════════════════════════════════════════════════════════════════════════════

elif section == "🤝 Collocations":
    st.title("🤝 Collocations")
    tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

    with tab1:
        idx = st.session_state.coll_idx
        c = COLLOCATIONS[idx]
        st.markdown(f"*{idx+1} of {len(COLLOCATIONS)}*")
        st.progress((idx+1)/len(COLLOCATIONS))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">🤝 {c['adj_noun'].upper()}</div>
            <div class="translation">🇪🇸 {c['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.coll_revealed:
            st.markdown(f'<div class="example-box">💬 <em>{c["example"]}</em></div>', unsafe_allow_html=True)
        else:
            if st.button("👁️ Reveal example", use_container_width=True, key="coll_reveal"):
                st.session_state.coll_revealed = True
                st.rerun()
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True, key="coll_prev"):
                st.session_state.coll_idx = (idx-1) % len(COLLOCATIONS)
                st.session_state.coll_revealed = False
                st.rerun()
        with c2:
            if st.button("🔀 Random", use_container_width=True, key="coll_rand"):
                st.session_state.coll_idx = random.randint(0,len(COLLOCATIONS)-1)
                st.session_state.coll_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="coll_nxt_fc"):
                st.session_state.coll_idx = (idx+1) % len(COLLOCATIONS)
                st.session_state.coll_revealed = False
                st.rerun()

    with tab2:
        fi = st.session_state.coll_fill_idx
        col = COLLOCATIONS[fi]
        st.markdown("**Complete with the correct collocation:**")
        st.markdown(f'<div class="example-box">{col["fill"]}</div>', unsafe_allow_html=True)
        st.markdown(f"🇪🇸 *{col['translation']}*")
        ans = st.text_input("Your answer:", key="coll_fill_input", value=st.session_state.coll_fill_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="coll_fill_chk"):
                st.session_state.coll_fill_ans = ans
                st.session_state.coll_fill_checked = True
                correct = ans.strip().lower() == col["adj_noun"].lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="coll_fill_nxt"):
                st.session_state.coll_fill_idx = random.randint(0,len(COLLOCATIONS)-1)
                st.session_state.coll_fill_ans = ""
                st.session_state.coll_fill_checked = False
                st.rerun()
        if st.session_state.coll_fill_checked:
            if st.session_state.coll_fill_ans.strip().lower() == col["adj_noun"].lower():
                st.success(f"✅ Correct! **{col['adj_noun']}**")
            else:
                st.error(f"❌ The collocation is: **{col['adj_noun']}**")
                st.markdown(f'<div class="example-box">💬 <em>{col["example"]}</em></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  CONNECTORS
# ════════════════════════════════════════════════════════════════════════════

elif section == "🔀 Connectors":
    st.title("🔀 Connectors & Linkers")
    tab1, tab2 = st.tabs(["Study by Category", "Fill in the Blank"])

    with tab1:
        cat = st.selectbox("Select category:", list(CONNECTORS.keys()))
        for item in CONNECTORS[cat]:
            with st.expander(f"**{item['word']}** — 🇪🇸 *{item['translation']}*"):
                st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)

    with tab2:
        flat = [{"cat":cat,**item} for cat,items in CONNECTORS.items() for item in items]
        fi = st.session_state.conn_fill_flat_idx % len(flat)
        item = flat[fi]
        st.markdown(f"**Category hint: *{item['cat']}* | 🇪🇸 *{item['translation']}***")
        st.markdown(f'<div class="example-box">{item["fill"]}</div>', unsafe_allow_html=True)
        ans = st.text_input("Your connector:", key="conn_fill_input", value=st.session_state.conn_fill_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="conn_chk"):
                st.session_state.conn_fill_ans = ans
                st.session_state.conn_fill_checked = True
                correct = ans.strip().lower() in item["word"].lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="conn_nxt"):
                st.session_state.conn_fill_flat_idx = random.randint(0,len(flat)-1)
                st.session_state.conn_fill_ans = ""
                st.session_state.conn_fill_checked = False
                st.rerun()
        if st.session_state.conn_fill_checked:
            if st.session_state.conn_fill_ans.strip().lower() in item["word"].lower():
                st.success(f"✅ Correct! **{item['word']}**")
            else:
                st.error(f"❌ The answer is: **{item['word']}**")
                st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  GRAMMAR
# ════════════════════════════════════════════════════════════════════════════

elif section == "✍️ Grammar":
    st.title("✍️ Grammar Practice")
    topic_names = [t["topic"] for t in GRAMMAR_EXERCISES]
    sel_topic = st.selectbox("Choose a grammar topic:", topic_names, index=st.session_state.gram_topic_idx)
    ti = topic_names.index(sel_topic)
    if ti != st.session_state.gram_topic_idx:
        st.session_state.gram_topic_idx = ti
        st.session_state.gram_ex_idx = 0
        st.session_state.gram_ans = ""
        st.session_state.gram_revealed = False
        st.session_state.gram_ai_fb = ""
        st.rerun()

    topic = GRAMMAR_EXERCISES[ti]
    with st.expander("📖 Grammar explanation — click to expand", expanded=False):
        st.markdown(topic["explanation"])
    st.markdown("---")

    ei = st.session_state.gram_ex_idx
    ex = topic["exercises"][ei]
    st.markdown(f"**Exercise {ei+1} of {len(topic['exercises'])}**")
    st.markdown(f"*{ex['instruction']}*")
    st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)

    user_ans = st.text_area("Your answer:", value=st.session_state.gram_ans,
                             key=f"gram_input_{ti}_{ei}", height=90)
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("👁️ Show answer", use_container_width=True):
            st.session_state.gram_revealed = True
            st.session_state.gram_ans = user_ans
            st.rerun()
    with c2:
        if st.button("🤖 AI Feedback", use_container_width=True):
            st.session_state.gram_ans = user_ans
            if user_ans.strip():
                with st.spinner("Getting AI feedback..."):
                    fb = get_ai_feedback(
                        user_ans, ex["answer"],
                        f"{topic['topic']} — {ex['instruction']} Prompt: {ex['prompt']}"
                    )
                    st.session_state.gram_ai_fb = fb
            else:
                st.warning("Please write your answer before requesting feedback.")
            st.rerun()
    with c3:
        if st.button("⬅️ Previous ex.", use_container_width=True):
            st.session_state.gram_ex_idx = (ei-1) % len(topic["exercises"])
            st.session_state.gram_ans = ""
            st.session_state.gram_revealed = False
            st.session_state.gram_ai_fb = ""
            st.rerun()
    with c4:
        if st.button("Next ex. ➡️", use_container_width=True):
            st.session_state.gram_ex_idx = (ei+1) % len(topic["exercises"])
            st.session_state.gram_ans = ""
            st.session_state.gram_revealed = False
            st.session_state.gram_ai_fb = ""
            st.rerun()

    if st.session_state.gram_revealed:
        st.success(f"✅ **Model answer:** {ex['answer']}")
    if st.session_state.gram_ai_fb:
        st.info(f"🤖 **AI Feedback:** {st.session_state.gram_ai_fb}")

# ════════════════════════════════════════════════════════════════════════════
#  USE OF ENGLISH
# ════════════════════════════════════════════════════════════════════════════

elif section == "🎯 Use of English":
    st.title("🎯 Use of English")
    tab1, tab2, tab3, tab4 = st.tabs([
        "Part 4 — Key Word Transformation",
        "Part 3 — Word Formation",
        "Part 1 — Multiple Choice Cloze",
        "Part 2 — Open Cloze",
    ])

    # ── Part 4: Key Word Transformation ─────────────────────────────────────
    with tab1:
        st.markdown("**Rewrite the sentence using the key word. Do not change the key word. Use 3–6 words.**")
        kwt = USE_OF_ENGLISH["Key Word Transformation"]
        idx = st.session_state.kwt_idx
        ex = kwt[idx]
        st.markdown(f"*{idx+1} of {len(kwt)}*")
        st.progress((idx+1)/len(kwt))
        st.markdown(f'<div class="example-box">📝 {ex["sentence"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**Key word: `{ex['key']}`**")
        ans = st.text_input("Your answer:", key=f"kwt_input_{idx}", value=st.session_state.kwt_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="kwt_chk"):
                st.session_state.kwt_ans = ans
                st.session_state.kwt_checked = True
                correct = ans.strip().lower().rstrip(".") == ex["answer"].strip().lower().rstrip(".")
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="kwt_nxt"):
                st.session_state.kwt_idx = (idx+1) % len(kwt)
                st.session_state.kwt_ans = ""
                st.session_state.kwt_checked = False
                st.rerun()
        if st.session_state.kwt_checked:
            st.success(f"**Model answer:** {ex['answer']}")
            if "pattern" in ex:
                st.caption(f"🏷️ Pattern tested: *{ex['pattern']}*")
            user_norm = st.session_state.kwt_ans.strip().lower().rstrip(".")
            ans_norm = ex["answer"].strip().lower().rstrip(".")
            if user_norm == ans_norm:
                st.success("✅ Perfect match!")
            else:
                st.warning("⚠️ Compare carefully with the model answer above — minor variations may also be acceptable.")

    # ── Part 3: Word Formation ───────────────────────────────────────────────
    with tab2:
        st.markdown("**Use the word in capitals to form a new word that fits the gap.**")
        wf = USE_OF_ENGLISH["Word Formation"]
        idx = st.session_state.wf_idx
        ex = wf[idx]
        st.markdown(f"*{idx+1} of {len(wf)}*")
        st.progress((idx+1)/len(wf))
        st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)
        ans = st.text_input("Your answer:", key=f"wf_input_{idx}", value=st.session_state.wf_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="wf_chk"):
                st.session_state.wf_ans = ans
                st.session_state.wf_checked = True
                correct = ans.strip().lower() == ex["answer"].lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="wf_nxt"):
                st.session_state.wf_idx = (idx+1) % len(wf)
                st.session_state.wf_ans = ""
                st.session_state.wf_checked = False
                st.rerun()
        if st.session_state.wf_checked:
            if st.session_state.wf_ans.strip().lower() == ex["answer"].lower():
                st.success(f"✅ Correct! **{ex['answer']}**")
            else:
                st.error(f"❌ Correct form: **{ex['answer']}**")

    # ── Part 1: Multiple Choice Cloze ────────────────────────────────────────
    with tab3:
        st.markdown("**Choose the best option (A, B, C or D) to complete the sentence.**")
        mcc = USE_OF_ENGLISH["Multiple Choice Cloze"]
        idx = st.session_state.mcc_idx
        ex = mcc[idx]
        st.markdown(f"*{idx+1} of {len(mcc)}*")
        st.progress((idx+1)/len(mcc))
        st.markdown(f'<div class="example-box">📝 {ex["sentence"]}</div>', unsafe_allow_html=True)
        sel = st.radio("Choose:", ex["options"], index=None, key=f"mcc_radio_{idx}")
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="mcc_chk"):
                st.session_state.mcc_selected = sel
                st.session_state.mcc_checked = True
                correct = sel is not None and sel[0] == ex["answer"]
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="mcc_nxt"):
                st.session_state.mcc_idx = (idx+1) % len(mcc)
                st.session_state.mcc_selected = None
                st.session_state.mcc_checked = False
                st.rerun()
        if st.session_state.mcc_checked and st.session_state.mcc_selected:
            if st.session_state.mcc_selected[0] == ex["answer"]:
                st.success(f"✅ Correct! — {ex['explanation']}")
            else:
                st.error(f"❌ Correct answer: **{ex['answer']}** — {ex['explanation']}")

    # ── Part 2: Open Cloze ───────────────────────────────────────────────────
    with tab4:
        st.markdown("**Fill each gap with ONE word. No contractions.**")
        oc_list = USE_OF_ENGLISH["Open Cloze"]
        idx = st.session_state.oc_idx
        oc = oc_list[idx]
        st.markdown(f"*Text {idx+1} of {len(oc_list)}: **{oc['title']}***")
        st.markdown(f'<div class="example-box">📝 {oc["text"]}</div>', unsafe_allow_html=True)
        st.markdown("**Your answers:**")
        user_oc = {}
        cols = st.columns(3)
        for i,(num,correct) in enumerate(oc["answers"].items()):
            with cols[i % 3]:
                user_oc[num] = st.text_input(f"Gap ({num}):", key=f"oc_{idx}_{num}",
                                              value=st.session_state.oc_answers.get(num,""))
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check all", use_container_width=True, key="oc_chk"):
                st.session_state.oc_answers = user_oc
                st.session_state.oc_checked = True
                st.rerun()
        with c2:
            if st.button("➡️ Next text", use_container_width=True, key="oc_nxt"):
                st.session_state.oc_idx = (idx+1) % len(oc_list)
                st.session_state.oc_answers = {}
                st.session_state.oc_checked = False
                st.rerun()
        if st.session_state.oc_checked:
            right = sum(1 for num,correct in oc["answers"].items()
                        if st.session_state.oc_answers.get(num,"").strip().lower() == correct.lower())
            total = len(oc["answers"])
            if right == total:
                st.success(f"✅ Perfect! {right}/{total} correct!")
            else:
                st.warning(f"**{right}/{total} correct**")
            for num,correct in oc["answers"].items():
                user_val = st.session_state.oc_answers.get(num,"").strip()
                if user_val.lower() == correct.lower():
                    st.success(f"Gap ({num}): **{correct}** ✅")
                else:
                    st.error(f"Gap ({num}): your answer *{user_val or '—'}* → correct: **{correct}**")
            if "tips" in oc:
                with st.expander("💡 Gap-by-gap tips"):
                    st.markdown(oc["tips"])

# ════════════════════════════════════════════════════════════════════════════
#  IDIOMS & EXPRESSIONS
# ════════════════════════════════════════════════════════════════════════════

elif section == "💬 Idioms & Expressions":
    st.title("💬 Idioms & Expressions")
    tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

    with tab1:
        idx = st.session_state.idiom_idx
        item = IDIOMS[idx]
        st.markdown(f"*{idx+1} of {len(IDIOMS)}*")
        st.progress((idx+1)/len(IDIOMS))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">💬 {item['idiom'].upper()}</div>
            <div class="translation">🇪🇸 {item['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.idiom_revealed:
            st.success(f"**Meaning:** {item['meaning']}")
            st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)
        else:
            if st.button("👁️ Reveal meaning & example", use_container_width=True, key="idiom_reveal"):
                st.session_state.idiom_revealed = True
                st.rerun()
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True, key="idiom_prev"):
                st.session_state.idiom_idx = (idx-1) % len(IDIOMS)
                st.session_state.idiom_revealed = False
                st.rerun()
        with c2:
            if st.button("🔀 Random", use_container_width=True, key="idiom_rand"):
                st.session_state.idiom_idx = random.randint(0,len(IDIOMS)-1)
                st.session_state.idiom_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="idiom_next"):
                st.session_state.idiom_idx = (idx+1) % len(IDIOMS)
                st.session_state.idiom_revealed = False
                st.rerun()

    with tab2:
        fi = st.session_state.idiom_fill_idx % len(IDIOMS)
        item = IDIOMS[fi]
        st.markdown("**Complete the sentence with the correct idiom:**")
        st.markdown(f'<div class="example-box">{item["fill"]}</div>', unsafe_allow_html=True)
        st.markdown(f"🇪🇸 *{item['translation']}*")
        ans = st.text_input("Your idiom:", key=f"idiom_fill_{fi}", value=st.session_state.idiom_fill_ans)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="idiom_chk"):
                st.session_state.idiom_fill_ans = ans
                st.session_state.idiom_fill_checked = True
                correct = ans.strip().lower() in item["idiom"].lower() or item["idiom"].lower() in ans.strip().lower()
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="idiom_fill_nxt"):
                st.session_state.idiom_fill_idx = random.randint(0,len(IDIOMS)-1)
                st.session_state.idiom_fill_ans = ""
                st.session_state.idiom_fill_checked = False
                st.rerun()
        if st.session_state.idiom_fill_checked:
            if st.session_state.idiom_fill_ans.strip().lower() in item["idiom"].lower() or item["idiom"].lower() in st.session_state.idiom_fill_ans.strip().lower():
                st.success(f"✅ Correct! **{item['idiom']}**")
            else:
                st.error(f"❌ The idiom is: **{item['idiom']}**")
                st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
#  CONFUSING EXPRESSIONS
# ════════════════════════════════════════════════════════════════════════════

elif section == "🔤 Confusing Expressions":
    st.title("🔤 Confusing Expressions")
    st.markdown("*Master the expressions that cause the most confusion for Spanish speakers.*")

    topic_key = st.selectbox(
        "Choose a topic:",
        list(CONFUSING_EXPRESSIONS.keys()),
        index=list(CONFUSING_EXPRESSIONS.keys()).index(st.session_state.conf_topic)
    )
    if topic_key != st.session_state.conf_topic:
        st.session_state.conf_topic = topic_key
        st.session_state.conf_ex_idx = 0
        st.session_state.conf_ans = ""
        st.session_state.conf_revealed = False
        st.rerun()

    topic = CONFUSING_EXPRESSIONS[topic_key]
    tab1, tab2 = st.tabs(["📖 Study & Examples", "✏️ Exercises"])

    with tab1:
        with st.expander("📖 Explanation — click to expand", expanded=True):
            st.markdown(topic["explanation"])
        st.markdown("---")
        st.markdown("### Forms & Examples")
        for form in topic["forms"]:
            col1, col2 = st.columns([1,2])
            with col1:
                st.markdown(f"""<div class="flashcard" style="padding:0.8rem 1.2rem; margin:0.3rem 0;">
                    <div style="font-size:1rem; font-weight:700;">{form['expression']}</div>
                    <div style="font-size:0.9rem; color:#a8d8f0;">🇪🇸 {form['spanish']}</div>
                </div>""", unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="example-box" style="margin-top:0.6rem;">💬 <em>{form["example"]}</em><br><small>📝 {form["note"]}</small></div>', unsafe_allow_html=True)

    with tab2:
        exercises = topic["exercises"]
        ei = st.session_state.conf_ex_idx % len(exercises)
        ex = exercises[ei]
        st.markdown(f"**Exercise {ei+1} of {len(exercises)}**")

        # Different layouts depending on exercise type
        if "situation" in ex:
            st.info(f"🎭 **Situation:** {ex['situation']}")
            st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)

        user_ans = st.text_input("Your answer:", value=st.session_state.conf_ans, key=f"conf_input_{topic_key}_{ei}")

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("👁️ Show answer", use_container_width=True, key="conf_show"):
                st.session_state.conf_ans = user_ans
                st.session_state.conf_revealed = True
                st.rerun()
        with c2:
            if st.button("⬅️ Previous", use_container_width=True, key="conf_prev"):
                st.session_state.conf_ex_idx = (ei - 1) % len(exercises)
                st.session_state.conf_ans = ""
                st.session_state.conf_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="conf_next"):
                st.session_state.conf_ex_idx = (ei + 1) % len(exercises)
                st.session_state.conf_ans = ""
                st.session_state.conf_revealed = False
                st.rerun()

        if st.session_state.conf_revealed:
            st.success(f"✅ **Model answer:** {ex['answer']}")
            # Auto-check simple answers
            if user_ans.strip():
                user_norm = user_ans.strip().lower()
                ans_norm = ex["answer"].strip().lower()
                if user_norm in ans_norm or any(part.strip() in user_norm for part in ans_norm.split("/")):
                    st.success("✅ Your answer looks correct!")
                else:
                    st.warning("⚠️ Compare your answer with the model above.")
