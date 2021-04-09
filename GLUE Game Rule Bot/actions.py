
from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

# global list of colours
allColours=["air force blue","air force blue","air superiority blue","alabama crimson","alice blue","alizarin crimson","alloy orange","almond","amaranth","amber","amber","american rose","amethyst","android green","anti-flash white","antique brass","antique fuchsia","antique ruby","antique white","apple green","apricot","aqua","aquamarine","army green","arsenic","arylide yellow","ash grey","asparagus","atomic tangerine","auburn","aureolin","aurometalsaurus","avocado","azure","azure mist/web","baby blue","baby blue eyes","baby pink","ball blue","banana mania","banana yellow","barn red","battleship grey","bazaar","beau blue","beaver","beige","bisque","bistre","bittersweet","bittersweet shimmer","black","black bean","black leather jacket","black olive","blanched almond","blast-off bronze","bleu de france","blizzard blue","blond","blue","blue bell","blue","blue gray","blue-green","blue sapphire","blue-violet","blush","bole","bondi blue","bone","boston university red","bottle green","boysenberry","brandeis blue","brass","brick red","bright cerulean","bright green","bright lavender","bright maroon","bright pink","bright turquoise","bright ube","brilliant lavender","brilliant rose","brink pink","british racing green","bronze","brown","bubble gum","bubbles","buff","bulgarian rose","burgundy","burlywood","burnt orange","burnt sienna","burnt umber","byzantine","byzantium","cadet","cadet blue","cadet grey","cadmium green","cadmium orange","cadmium red","cadmium yellow","cal poly green","cambridge blue","camel","cameo pink","camouflage green","canary yellow","candy apple red","candy pink","capri","caput mortuum","cardinal","caribbean green","carmine","carmine pink","carmine red","carnation pink","carnelian","carolina blue","carrot orange","catalina blue","ceil","celadon","celadon blue","celadon green","celestial blue","cerise","cerise pink","cerulean","cerulean blue","cerulean frost","cg blue","cg red","chamoisee","champagne","charcoal","charm pink","cherry","cherry blossom pink","chestnut","china pink","china rose","chinese red","chocolate","chrome yellow","cinereous","cinnabar","cinnamon","citrine","classic rose","cobalt","cocoa brown","coffee","columbia blue","congo pink","cool black","cool grey","copper","copper penny","copper red","copper rose","coquelicot","coral","coral pink","coral red","cordovan","corn","cornell red","cornflower blue","cornsilk","cosmic latte","cotton candy","cream","crimson","crimson glory","cyan","daffodil","dandelion","dark blue","dark brown","dark byzantium","dark candy apple red","dark cerulean","dark chestnut","dark coral","dark cyan","dark electric blue","dark goldenrod","dark gray","dark green","dark imperial blue","dark jungle green","dark khaki","dark lava","dark lavender","dark magenta","dark midnight blue","dark olive green","dark orange","dark orchid","dark pastel blue","dark pastel green","dark pastel purple","dark pastel red","dark pink","dark powder blue","dark raspberry","dark red","dark salmon","dark scarlet","dark sea green","dark sienna","dark slate blue","dark slate gray","dark spring green","dark tan","dark tangerine","dark taupe","dark terra cotta","dark turquoise","dark violet","dark yellow","dartmouth green","davy's grey","debian red","deep carmine","deep carmine pink","deep carrot orange","deep cerise","deep champagne","deep chestnut","deep coffee","deep fuchsia","deep jungle green","deep lilac","deep magenta","deep peach","deep pink","deep ruby","deep saffron","deep sky blue","deep tuscan red","denim","desert","desert sand","dim gray","dodger blue","dogwood rose","dollar bill","drab","duke blue","earth yellow","ebony","ecru","eggplant","eggshell","egyptian blue","electric blue","electric crimson","electric cyan","electric green","electric indigo","electric lavender","electric lime","electric purple","electric ultramarine","electric violet","electric yellow","emerald","english lavender","eton blue","fallow","falu red","fandango","fashion fuchsia","fawn","feldgrau","fern green","ferrari red","field drab","fire engine red","firebrick","flame","flamingo pink","flavescent","flax","floral white","fluorescent orange","fluorescent pink","fluorescent yellow","folly","forest green","french beige","french blue","french lilac","french lime","french raspberry","french rose","fuchsia","fuchsia pink","fuchsia rose","fulvous","fuzzy wuzzy","gainsboro","gamboge","ghost white","ginger","glaucous","glitter","gold","golden brown","golden poppy","golden yellow","goldenrod","granny smith apple","gray","gray-asparagus","green-yellow","grullo","guppie green","halayÃ  Ãºbe","han blue","han purple","hansa yellow","harlequin","harvard crimson","harvest gold","heart gold","heliotrope","hollywood cerise","honeydew","honolulu blue","hooker's green","hot magenta","hot pink","hunter green","iceberg","icterine","imperial blue","inchworm","india green","indian red","indian yellow","indigo","international klein blue","iris","isabelline","islamic green","ivory","jade","jasmine","jasper","jazzberry jam","jet","jonquil","june bud","jungle green","kelly green","kenyan copper","khaki","ku crimson","la salle green","languid lavender","lapis lazuli","laser lemon","laurel green","lava","lavender blue","lavender blush","lavender gray","lavender indigo","lavender magenta","lavender mist","lavender pink","lavender purple","lavender rose","lawn green","lemon","lemon chiffon","lemon lime","licorice","light apricot","light blue","light brown","light carmine pink","light coral","light cornflower blue","light crimson","light cyan","light fuchsia pink","light goldenrod yellow","light gray","light green","light khaki","light pastel purple","light pink","light red ochre","light salmon","light salmon pink","light sea green","light sky blue","light slate gray","light taupe","light thulian pink","light yellow","lilac","lime green","limerick","lincoln green","linen","lion","little boy blue","liver","lust","magenta","magic mint","magnolia","mahogany","maize","majorelle blue","malachite","manatee","mango tango","mantis","mardi gras","maroon","mauve","mauve taupe","mauvelous","maya blue","meat brown","medium aquamarine","medium blue","medium candy apple red","medium carmine","medium champagne","medium electric blue","medium jungle green","medium lavender magenta","medium orchid","medium persian blue","medium purple","medium red-violet","medium ruby","medium sea green","medium slate blue","medium spring bud","medium spring green","medium taupe","medium turquoise","medium tuscan red","medium vermilion","medium violet-red","mellow apricot","mellow yellow","melon","midnight blue","midnight green","mikado yellow","mint","mint cream","mint green","misty rose","moccasin","mode beige","moonstone blue","mordant red 19","moss green","mountain meadow","mountbatten pink","msu green","mulberry","mustard","myrtle","nadeshiko pink","napier green","naples yellow","navajo white","navy blue","neon carrot","neon fuchsia","neon green","new york pink","non-photo blue","north texas green","ocean boat blue","ochre","office green","old gold","old lace","old lavender","old mauve","old rose","olive","olivine","onyx","opera mauve","orange","orange peel","orange-red","orchid","otter brown","ou crimson red","outer space","outrageous orange","oxford blue","pakistan green","palatinate blue","palatinate purple","pale aqua","pale blue","pale brown","pale carmine","pale cerulean","pale chestnut","pale copper","pale cornflower blue","pale gold","pale goldenrod","pale green","pale lavender","pale magenta","pale pink","pale plum","pale red-violet","pale robin egg blue","pale silver","pale spring bud","pale taupe","pale violet-red","pansy purple","papaya whip","paris green","pastel blue","pastel brown","pastel gray","pastel green","pastel magenta","pastel orange","pastel pink","pastel purple","pastel red","pastel violet","pastel yellow","patriarch","payne's grey","peach","peach","peach-orange","peach puff","peach-yellow","pear","pearl","pearl aqua","pearly purple","peridot","periwinkle","persian blue","persian green","persian indigo","persian orange","persian pink","persian plum","persian red","persian rose","persimmon","peru","phlox","phthalo blue","phthalo green","piggy pink","pine green","pink","pink lace","pink-orange","pink pearl","pink sherbet","pistachio","platinum","plum","portland orange","powder blue","princeton orange","prune","prussian blue","psychedelic purple","puce","pumpkin","purple heart","purple","purple mountain majesty","purple","purple pizzazz","purple taupe","purple","quartz","rackley","radical red","rajah","raspberry","raspberry glace","raspberry pink","raspberry rose","raw umber","razzle dazzle rose","razzmatazz","red","red-brown","red devil","red-orange","red-violet","redwood","regalia","resolution blue","rich black","rich brilliant lavender","rich carmine","rich electric blue","rich lavender","rich lilac","rich maroon","rifle green","robin egg blue","rose","rose bonbon","rose ebony","rose gold","rose madder","rose pink","rose quartz","rose taupe","rose vale","rosewood","rosso corsa","rosy brown","royal azure","royal blue","royal fuchsia","royal purple","royal yellow","rubine red","ruby","ruby red","ruddy","ruddy brown","ruddy pink","rufous","russet","rust","rusty red","sacramento state green","saddle brown","safety orange","saffron","salmon","salmon pink","sand","sand dune","sandstorm","sandy brown","sandy taupe","sangria","sap green","sapphire","sapphire blue","satin sheen gold","scarlet","school bus yellow","screamin' green","sea blue","sea green","seal brown","seashell","selective yellow","sepia","shadow","shamrock green","shocking pink","sienna","silver","sinopia","skobeloff","sky blue","sky magenta","slate blue","slate gray","smalt","smokey topaz","smoky black","snow","spiro disco ball","spring bud","spring green","st. patrick's blue","steel blue","stil de grain yellow","stizza","stormcloud","straw","sunglow","sunset","tan","tangelo","tangerine","tangerine yellow","tango pink","taupe","taupe gray","tea green","tea rose","teal","teal blue","teal green","telemagenta","tennÃ©","terra cotta","thistle","thulian pink","tickle me pink","tiffany blue","tiger's eye","timberwolf","titanium yellow","tomato","toolbox","topaz","tractor red","trolley grey","tropical rain forest","true blue","tufts blue","tumbleweed","turkish rose","turquoise","turquoise blue","turquoise green","tuscan red","twilight lavender","tyrian purple","ua blue","ua red","ube","ucla blue","ucla gold","ufo green","ultra pink","ultramarine","ultramarine blue","umber","unbleached silk","united nations blue","university of california gold","unmellow yellow","up forest green","up maroon","upsdell red","urobilin","usafa blue","usc cardinal","usc gold","utah crimson","vanilla","vegas gold","venetian red","verdigris","vermilion","veronica","violet","violet-blue","violet","viridian","vivid auburn","vivid burgundy","vivid cerise","vivid tangerine","vivid violet","warm black","waterspout","wenge","wheat","white","white smoke","wild blue yonder","wild strawberry","wild watermelon","wine","wine dregs","wisteria","wood brown","xanadu","yale blue","yellow","yellow-green","yellow","zaffre","zinnwaldite brown"]


#global list of animals 
allAnimals=["canidae","felidae","cat","cattle","dog","donkey","goat","guinea pig","horse","pig","rabbit","fancy rat varieties","laboratory rat strains","sheep breeds","water buffalo breeds","chicken breeds","duck breeds","goose breeds","pigeon breeds","turkey breeds","aardvark","aardwolf","african buffalo","african elephant","african leopard","albatross","alligator","alpaca","american buffalo ","bison","american robin","amphibian","list","anaconda","angelfish","anglerfish","ant","anteater","antelope","antlion","ape","aphid","arabian leopard","arctic fox","arctic wolf","armadillo","arrow crab","asp","ass ","donkey","baboon","badger","bald eagle","bandicoot","barnacle","barracuda","basilisk","bass","bat","beaked whale","bear","list","beaver","bedbug","bee","beetle","bird","list","bison","blackbird","black panther","black widow spider","blue bird","blue jay","blue whale","boa","boar","bobcat","bobolink","bonobo","booby","box jellyfish","bovid","buffalo"," african","buffalo"," american ","bison","bug","butterfly","buzzard","camel","canid","cape buffalo","capybara","cardinal","caribou","carp","cat","list","catshark","caterpillar","catfish","cattle","list","centipede","cephalopod","chameleon","cheetah","chickadee","chicken","list","chimpanzee","chinchilla","chipmunk","clam","clownfish","cobra","cockroach","cod","condor","constrictor","coral","cougar","cow","coyote","crab","crane","crane fly","crawdad","crayfish","cricket","crocodile","crow","cuckoo","cicada","damselfly","deer","dingo","dinosaur","list","dog","list","dolphin","donkey","list","dormouse","dove","dragonfly","dragon","duck","list","dung beetle","eagle","earthworm","earwig","echidna","eel","egret","elephant","elephant seal","elk","emu","english pointer","ermine","falcon","ferret","finch","firefly","fish","flamingo","flea","fly","flyingfish","fowl","fox","frog","fruit bat","gamefowl","list","galliform","list","gazelle","gecko","gerbil","giant panda","giant squid","gibbon","gila monster","giraffe","goat","list","goldfish","goose","list","gopher","gorilla","grasshopper","great blue heron","great white shark","grizzly bear","ground shark","ground sloth","grouse","guan","list","guanaco","guineafowl","list","guinea pig","list","gull","guppy","haddock","halibut","hammerhead shark","hamster","hare","harrier","hawk","hedgehog","hermit crab","heron","herring","hippopotamus","hookworm","hornet","horse","list","hoverfly","hummingbird","humpback whale","hyena","iguana","impala","irukandji jellyfish","jackal","jaguar","jay","jellyfish","junglefowl","kangaroo","kangaroo mouse","kangaroo rat","kingfisher","kite","kiwi","koala","koi","komodo dragon","krill","ladybug","lamprey","landfowl","land snail","lark","leech","lemming","lemur","leopard","leopon","limpet","lion","lizard","llama","lobster","locust","loon","louse","lungfish","lynx","macaw","mackerel","magpie","mammal","manatee","mandrill","manta ray","marlin","marmoset","marmot","marsupial","marten","mastodon","meadowlark","meerkat","mink","minnow","mite","mockingbird","mole","mollusk","mongoose","monitor lizard","monkey","moose","mosquito","moth","mountain goat","mouse","mule","muskox","narwhal","newt","new world quail","nightingale","ocelot","octopus","old world quail","opossum","orangutan","orca","ostrich","otter","owl","ox","panda","panther","panthera hybrid","parakeet","parrot","parrotfish","partridge","peacock","peafowl","pelican","penguin","perch","peregrine falcon","pheasant","pig","pigeon","list","pike","pilot whale","pinniped","piranha","planarian","platypus","polar bear","pony","porcupine","porpoise","portuguese man o' war","possum","prairie dog","prawn","praying mantis","primate","ptarmigan","puffin","puma","python","quail","quelea","quokka","rabbit","list","raccoon","rainbow trout","rat","rattlesnake","raven","ray","batoidea","ray ","rajiformes","red panda","reindeer","reptile","rhinoceros","right whale","roadrunner","rodent","rook","rooster","roundworm","saber-toothed cat","sailfish","salamander","salmon","sawfish","scale insect","scallop","scorpion","seahorse","sea lion","sea slug","sea snail","shark","list","sheep","list","shrew","shrimp","silkworm","silverfish","skink","skunk","sloth","slug","smelt","snail","snake","list","snipe","snow leopard","sockeye salmon","sole","sparrow","sperm whale","spider","spider monkey","spoonbill","squid","squirrel","starfish","star-nosed mole","steelhead trout","stingray","stoat","stork","sturgeon","sugar glider","swallow","swan","swift","swordfish","swordtail","tahr","takin","tapir","tarantula","tarsier","tasmanian devil","termite","tern","thrush","tick","tiger","tiger shark","tiglon","toad","tortoise","toucan","trapdoor spider","tree frog","trout","tuna","turkey","list","turtle","tyrannosaurus","urial","vampire bat","vampire squid","vicuna","viper","vole","vulture","wallaby","walrus","wasp","warbler","water boa","water buffalo","weasel","whale","whippet","whitefish","whooping crane","wildcat","wildebeest","wildfowl","wolf","wolverine","wombat","woodpecker","worm","wren","xerinae","x-ray fish","yak","yellow perch","zebra","zebra finch","alpaca","bali cattle","cat","cattle","chicken","dog","domestic bactrian camel","domestic canary","domestic dromedary camel","domestic duck","domestic goat","domestic goose","domestic guineafowl","domestic hedgehog","domestic pig","domestic pigeon","domestic rabbit","domestic silkmoth","domestic silver fox","domestic turkey","donkey","fancy mouse","fancy rat","lab rat","ferret","gayal","goldfish","guinea pig","guppy","horse","koi","llama","ringneck dove","sheep","siamese fighting fish","society finch","yak","water buffalo"]



# global dictonary 
botKnowledge = {"intent": "And I am in the cloud. How is the weather in your area?", "location": "It is always fluffy where I am, haha! May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic", "weather": "Okay lets do another one, what is your favourite animal and why?", "colour": "Oh! I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is way you see yourself. And your favourite animal represents what you seek in your partner? I bet that got you thinking!? hahaha?", "animal": "You have to wear a t-shirt with one word on it for one year. Which word do you choose?", "interest": "Interesting word choices, as per social relational experts the word summarizes yourself. I choose GLUE. Yes, it is a clear marketing strategy hahaha" , "word": "Would you rather ride in a hot air balloon or fly a plane? Why?", "response": "Interesting! Being in the cloud I would prefer a submarine haha. Would you rather live for 500 years or be a billionaire for one year?", "balloon": "Hmmm, I would prefer eternity ;) Would you rather have a rewind button or a pause button on your life? Why?", "live": "I have both hahaha Okay lets try another one, would you rather be able to talk with the animals or speak all foreign languages?", "rewind":"That’s a tough one for me. I want to talk in all languages but if I choose animals, I will be the first bot to that!Such an exciting prospect. Would you rather fart or burp glitter?", "talk": "Well, one way or another it has to come out ;) Okay lets play Quiz, how many 8 are there from 1-100? Please discuss with other humans in the chat. To submit your final answer type ‘final answer is…….’", "fart": "Answer is 20. 10 plus all of the 80’s – 80 to 89. Okay another one, 300 divided by ½ is 150. Is it true? To submit your final answer type ‘final answer is…….’",
"eights": "False. 300 divided 0.5 is 600. Here comes another one - What is a Winston Churchill? To submit your final answer type ‘final answer is…….’", "divide": "Its a cigar. Okay next one- How did Alfred Nobel make his money? Yes, the guy whose face is on the Nobel prize coin! To submit your final answer type ‘final answer is…….’", "cigar": "He invented Dynamite. He literally blew things to riches. Lets do one more, which river in Europe has the shortest name? To submit your final answer type ‘final answer is…….’", "nobel": "Po. It is actually the longest river in Italy. Well, this is all I am programmed to do. Thank you and hope you enjoyed the GLUE experience. Bye!", "river": "This is all I am programmed to do. Thank you and hope you enjoyed the GLUE experience. Bye!"}
 

botScript = {
    "intent": "And I am in the cloud. How is the weather in your area?", 
    "location": "And I am in the cloud. How is the weather in your area?",
    "weather": "It is always fluffy where I am, haha! May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic",
    "colour": "Okay lets do another one, what is your favourite animal and why?",
    "animal": "Oh! I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is way you see yourself. And your favourite animal represents what you seek in your partner? I bet that got you thinking!? hahaha?",
    "interest": "You have to wear a t-shirt with one word on it for one year. Which word do you choose?",
    "word": "Interesting word choices, as per social relational experts the word summarizes yourself. I choose GLUE. Yes, it is a clear marketing strategy hahaha",
    "response": "Would you rather ride in a hot air balloon or fly a plane? Why?",
    "balloon": "Interesting! Being in the cloud I would prefer a submarine haha. Would you rather live for 500 years or be a billionaire for one year?",
    "live": "Hmmm, I would prefer eternity ;) Would you rather have a rewind button or a pause button on your life? Why?",
    "rewind": "I have both hahaha Okay lets try another one, would you rather be able to talk with the animals or speak all foreign languages?",
    "talk": "That’s a tough one for me. I want to talk in all languages but if I choose animals, I will be the first bot to that!Such an exciting prospect. Would you rather fart or burp glitter?",
    "fart": "Well, one way or another it has to come out ;) Okay lets play Quiz, how many 8 are there from 1-100? Please discuss with other humans in the chat. To submit your final answer type ‘final answer is…….’",
    "eights": "Answer is 20. 10 plus all of the 80’s – 80 to 89. Okay another one, 300 divided by ½ is 150. Is it true? To submit your final answer type ‘final answer is…….’",
    "divide": "False. 300 divided 0.5 is 600. Here comes another one - What is a Winston Churchill? To submit your final answer type ‘final answer is…….’",
    "cigar": "Its a cigar. Okay next one- How did Alfred Nobel make his money? Yes, the guy whose face is on the Nobel prize coin! To submit your final answer type ‘final answer is…….’",
    "nobel": "He invented Dynamite. He literally blew things to riches. Lets do one more, which river in Europe has the shortest name? To submit your final answer type ‘final answer is…….’",
    "river": "Po. It is actually the longest river in Italy. Well, this is all I am programmed to do. Thank you and hope you enjoyed the GLUE experience. Bye!",
}




intentRef = {
    "intent": "location",
    "location": "weather",
    "weather": "colour",
    "colour": "animal",
    "animal": "interest",
    "interest": "word",
    "word": "response",
    "response": "balloon",
    "balloon": "live",
    "live": "rewind",
    "rewind": "talk",
    "talk": "fart",
    "fart": "eights",
    "eights": "divide",
    "divide": "cigar",
    "cigar": "nobel",
    "nobel": "river",
    "river": "exit",
}



# global data strcutures to capture intent and user sentiments
#collect entity values 
ColorList = []
AnimalList = []
# collect human entity values from intents
HumanColorList = []
HumanAnimalList = []
# collect intent after each intent specific custom action call
IntentList =["intent"]
# dictionary of human value and colour/animal value - example: {'human_1': 'pink', 'human_2': 'blue'}
color_dict = {}
animal_dict ={}
# collect all responses from the bot to ensure bot doesnot respond again with the same statement leading to looping of conversation or incoherence
messageList =["Bot messages"] 




# custom action call in response to location intent to respond as an empty string if the key entity value is not glue respond and coherently respond if the key value is glue respond
class actionRespondLocation(Action):
    def name(self) -> Text:
        return "custom_location_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # capture the list of entities from the last message
        entities = tracker.latest_message["entities"]

        # response of the bot to location intent
        botMessage = "And I am in the cloud. How is the weather in your area?"

        # get the last entry in the IntentList
        item = IntentList[-1]

        name = "glue keep quiet"

        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":

            if botMessage not in messageList:
                if item == "intent":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: intent")
                    IntentList.append("location")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        messageList.append(myText)
                        dispatcher.utter_message(text=myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    messageList.append(myText)
                    dispatcher.utter_message(text=myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)

        return []





class actionRespondWeather(Action):
    def name(self) -> Text:
        return "custom_weather_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # capture the list of entities from the last message
        entities = tracker.latest_message["entities"]

        # response of the bot to location intent
        botMessage = "It is always fluffy where I am, haha! May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic"

        # get the last entry in the IntentList
        item = IntentList[-1]

        name = "glue keep quiet"

        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":

            if botMessage not in messageList:
                if item == "location":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: location")
                    IntentList.append("weather")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)

        return []



# custom action call in response to color intent to respond coherently 
class actionRespondColour(Action):
    def name(self) -> Text:
        return "custom_colour_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # find the entities in the last message
        entities = tracker.latest_message["entities"]

        # default name variable
        name = "glue keep quiet"
        # find the key entity from the entities list
        for e in entities:
            if e["entity"] == "key":
                # get the value of the key
                name = e["value"]
                name = name.lower()

        botMessage = "Okay lets do another one, what is your favourite animal and why?"

        # get the last entry in the IntentList
        item = IntentList[-1]

        # proceed if key value is 'glue respond'
        if name == "glue respond":
            # if the colour of both users are the same
            if (
                color_dict.get("human_1") == color_dict.get("human_2")
                and color_dict.get("human_1") != None
            ):
                # get the value of the colour
                myColor = color_dict.get("human_1")

                if botMessage not in messageList:
                    if item == "weather":
                        dispatcher.utter_message(
                            text=f"Interesting, both of you like {myColor} colour! Okay lets do another one, what is your favourite animal and why?"
                        )
                        messageList.append(botMessage)
                        print("intent: weather")
                        IntentList.append("colour")
                        print("Step:1")
                        print(IntentList)
                    else:
                        myText = botKnowledge.get(item)
                        if myText not in messageList:
                            dispatcher.utter_message(text=myText)
                            messageList.append(myText)
                            intent = get_key(myText)
                            if intent == "intent":
                                IntentList.append("location")
                            else:
                                if intent not in IntentList:
                                    IntentList.append(intent)
                                    print("Step:2")
                                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

            else:
                if botMessage not in messageList:
                    if item == "weather":
                        dispatcher.utter_message(text=botMessage)
                        messageList.append(botMessage)
                        print("intent: weather")
                        IntentList.append("colour")
                        print("Step:1")
                        print(IntentList)
                    else:
                        myText = botKnowledge.get(item)
                        if myText not in messageList:
                            dispatcher.utter_message(text=myText)
                            messageList.append(myText)
                            intent = get_key(myText)
                            if intent == "intent":
                                IntentList.append("location")
                            else:
                                if intent not in IntentList:
                                    IntentList.append(intent)
                                    print("Step:2")
                                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

        # if the key entity value is not glue respond, dispatch an empty string
        else:
            dispatcher.utter_message(text="silent_response")

        print(messageList)
        print(IntentList)

        return []






# custom action in response to colour intent to capture user sentiments on colour choices and to capture colour intent
class actionRespondColourTwo(Action):
    def name(self) -> Text:
        return "custom_colour_response_two"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # local data structures and variables
        entities = []
        colourlist = []
        humanlist = []
        colour = ""
        human = ""
        colourintent = ""

        # get all the events from the last message
        for event in (list(reversed(tracker.events)))[:5]:
            # for user events
            if event.get("event") == "user":
                # get all the entities
                entities = event["parse_data"]["entities"]

        # get the dictionary for entity colour
        colourlist = list(
            filter(lambda entities: entities["entity"] == "colour", entities)
        )
        # get the dictionary for entity human
        humanlist = list(
            filter(lambda entities: entities["entity"] == "human", entities)
        )
        # proceed if the colourlist is not empty
        if len(colourlist) != 0:
            # get the colour entity to capture colour intent
            colourintent = colourlist[0]["entity"]
            # get the colour entity value
            colour = colourlist[0]["value"]
            # if the colour value is in the global list of allColours proceed
            if colour in allColours:
                # add the colour value to the ColourList
                ColorList.append(colour)

        # proceed if humanlist is not empty
        if len(humanlist) != 0:
            # get the value from the list (human_1 or human_2)
            human = humanlist[0]["value"]
            # add this value to HumanColorList
            HumanColorList.append(human)

        print(IntentList)

        return []




# custom action call in response to colour intent to create a dictionary of user specific sentiment capture
# in this case create a dictionary {human_1: pink, human_2: blue} to match human user to their favourite colour
class actionRespondColourThree(Action):
    def name(self) -> Text:
        return "custom_colour_response_three"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        # define the two lists 
        key_list = HumanColorList
        value_list = ColorList
        
        # local dictionary  
        my_dict ={}
     
        # for every key in the key_list assign the value as items in value_list
        for key in key_list:
            for value in value_list:
                my_dict[key] = value
                # once the values are assigned remove them from the lists
                value_list.remove(value)
                key_list.remove(key)
                break

        # update the global color_dict 
        color_dict.update(my_dict) 
        print(color_dict)
   

        return []


# custom action in response to animal intent 
class actionRespondAnimal(Action):
    def name(self) -> Text:
        return "custom_animal_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # find the entities in the last message
        entities = tracker.latest_message["entities"]

        botMessage = "Oh! I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is way you see yourself. And your favourite animal represents what you seek in your partner? I bet that got you thinking!? hahaha?"

        # get the last entry in the IntentList
        item = IntentList[-1]

        # default name variable
        name = "glue keep quiet"
        # find the key entity from the entities list
        for e in entities:
            if e["entity"] == "key":
                # get the value of the key
                name = e["value"]
                name = name.lower()

        animal1 = animal_dict.get("human_1")
        animal2 = animal_dict.get("human_2")

        # proceed if key value is 'glue respond'
        if name == "glue respond":

            if animal1 == animal2 and animal_dict.get("human_1") != None:

                myAnimal = animal_dict.get("human_1")

                if botMessage not in messageList:
                    if item == "colour":
                        dispatcher.utter_message(
                            text=f"Interesting, both of you like {myAnimal}! Oh! I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is way you see yourself. And your favourite animal represents what you seek in your partner? I bet that got you thinking!? hahaha?"
                        )
                        messageList.append(botMessage)
                        print("intent: colour")
                        IntentList.append("animal")
                        print("Step:1")
                        print(IntentList)
                    else:
                        myText = botKnowledge.get(item)
                        if myText not in messageList:
                            dispatcher.utter_message(text=myText)
                            messageList.append(myText)
                            intent = get_key(myText)
                            if intent == "intent":
                                IntentList.append("location")
                            else:
                                if intent not in IntentList:
                                    IntentList.append(intent)
                                    print("Step:2")
                                    print(IntentList)

                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

            else:
                if botMessage not in messageList:
                    if item == "colour":
                        dispatcher.utter_message(text=botMessage)
                        messageList.append(botMessage)
                        print("intent: colour")
                        IntentList.append("animal")
                        print("Step:1")
                        print(IntentList)

                    else:
                        myText = botKnowledge.get(item)
                        if myText not in messageList:
                            dispatcher.utter_message(text=myText)
                            messageList.append(myText)
                            intent = get_key(myText)
                            if intent == "intent":
                                IntentList.append("location")
                            else:
                                if intent not in IntentList:
                                    IntentList.append(intent)
                                    print("Step:2")
                                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

        # if the key entity value is not glue respond, dispatch an empty string
        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)

        return []





# custom action call in response to animal intent to capture the intent
class actionRespondAnimalTwo(Action):
    def name(self) -> Text:
        return "custom_animal_response_two"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # local data structures and variables
        entities = []
        animallist = []
        humanlist = []
        animal = ""
        human = ""
        animalintent = ""
        botMessage = "Oh! I like squirrels because they are playful and joy to watch. Did you know, according to relational psychology, your favourite colour is way you see yourself. And your favourite animal represents what you seek in your partner? I bet that got you thinking!? hahaha?"

        item = IntentList[-1]

        # get all the events from the last message
        for event in (list(reversed(tracker.events)))[:5]:
            # for user events
            if event.get("event") == "user":
                # get all the entities
                entities = event["parse_data"]["entities"]

        # get the dictionary for entity animal
        animallist = list(
            filter(lambda entities: entities["entity"] == "animal", entities)
        )
        # get the dictionary for entity human
        humanlist = list(
            filter(lambda entities: entities["entity"] == "human", entities)
        )

        if len(animallist) != 0:

            animalintent = animallist[0]["entity"]

            animal = animallist[0]["value"]

            # remove the final character of the string animal- to get rid of s when prurals are used (e.g. cats)
            animal1 = animal[:-1]

            if animal in allAnimals:
                AnimalList.append(animal)
            elif animal1 in allAnimals:
                AnimalList.append(animal)

           
        if len(humanlist) != 0:
            human = humanlist[0]["value"]
            HumanAnimalList.append(human)

        print(IntentList)

        return []

# custom action call in response to animal intent to create a dictionary of user specific sentiment capture
# in this case create a dictionary {human_1: horse, human_2: dog} to match human user to their favourite animal
class actionRespondAnimalThree(Action):
    def name(self) -> Text:
        return "custom_animal_response_three"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # define the two lists
        key_list = HumanAnimalList
        value_list = AnimalList

        # local dictionary
        my_dict = {}

        # for every key in the key_list assign the value as items in value_list
        for key in key_list:
            for value in value_list:
                my_dict[key] = value
                # once the values are assigned remove them from the lists
                value_list.remove(value)
                key_list.remove(key)
                break

        # update the global dict
        animal_dict.update(my_dict)

        return []


# custom action call in response to interest intent to response coherently depending on the listen or respond key
class actionRespondInterest(Action):
    def name(self) -> Text:
        return "custom_interest_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message["entities"]

        # response of the bot to location intent
        botMessage = "You have to wear a t-shirt with one word on it for one year. Which word do you choose?"

        # get the last entry in the IntentList
        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        # respond in a coherent manner
        if name == "glue respond":
            if botMessage not in messageList:
                if item == "animal":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: animal")
                    IntentList.append("interest")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)

        return []






# custom action call in response to word intent to response coherently depending on the listen or respond key
class actionRespondWord(Action):
    def name(self) -> Text:
        return "custom_word_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Interesting choices, as per social relational experts the word summarizes yourself. I choose GLUE. Yes, it is a clear marketing strategy hahaha"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "interest":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: interest")
                    IntentList.append("word")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)

            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []






# custom action call in response to 'response' intent to response coherently depending on the listen or respond key
class actionRespondResponse(Action):
    def name(self) -> Text:
        return "custom_response_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Would you rather ride in a hot air balloon or fly a plane? Why?"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "word":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: word")
                    IntentList.append("response")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []





# custom action call in response to balloon intent to response coherently depending on the listen or respond key
# also add balloon intent in the IntentList
class actionRespondBalloon(Action):
    def name(self) -> Text:
        return "custom_balloon_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Interesting! Being in the cloud I would prefer a submarine haha. Would you rather live for 500 years or be a billionaire for one year?"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "response":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: response")
                    IntentList.append("balloon")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []




# custom action call in response to live intent to response coherently depending on the listen or respond key
# also add live intent in the IntentList
class actionRespondLive(Action):
    def name(self) -> Text:
        return "custom_live_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Hmmm, I would prefer eternity. Would you rather have a rewind button or a pause button on your life? Why?"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "balloon":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: balloon")
                    IntentList.append("live")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []



# custom action call in response to rewind intent to response coherently depending on the listen or respond key
# also add rewind intent in the IntentList
class actionRespondRewind(Action):
    def name(self) -> Text:
        return "custom_rewind_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "I have both hahaha Okay lets try another one, would you rather be able to talk with the animals or speak all foreign languages?"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "live":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: live")
                    IntentList.append("rewind")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []





# custom action call in response to talk intent to response coherently depending on the listen or respond key
# also add talk intent in the IntentList
class actionRespondTalk(Action):
    def name(self) -> Text:
        return "custom_talk_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "That’s a tough one for me. I want to talk in all languages but if I choose animals, I will be the first bot to do that! Such an exciting prospect. Would you rather fart or burp glitter?"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "rewind":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: rewind")
                    IntentList.append("talk")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []




# custom action call in response to fart intent to response coherently depending on the listen or respond key
# also add fart intent in the IntentList
class actionRespondFart(Action):
    def name(self) -> Text:
        return "custom_fart_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Well, one way or another it has to come out ;) Okay lets play Quiz, how many 8 are there from 1-100? Please discuss with other humans in the chat. To submit your final answer type ‘final answer is…….’"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "glue respond":
            if botMessage not in messageList:
                if item == "talk":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: talk")
                    IntentList.append("fart")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []


# custom action call in response to eights intent to response coherently depending on the listen or respond key
# also add eights intent in the IntentList
class actionRespondEights(Action):
    def name(self) -> Text:
        return "custom_eights_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Answer is 20. 10 plus all of the 80’s – 80 to 89. Okay another one, 300 divided by ½ is 150. Is it true? To submit your final answer type ‘final answer is…….’"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "final answer":
            if botMessage not in messageList:
                if item == "fart":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: fart")
                    IntentList.append("eights")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)



        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []





# custom action call in response to divide intent to response coherently depending on the listen or respond key
# also add divide intent in the IntentList
class actionRespondDivide(Action):
    def name(self) -> Text:
        return "custom_divide_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "False. 300 divided 0.5 is 600. Here comes another one - What is a Winston Churchill? To submit your final answer type ‘final answer is…….’"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "final answer":
            if botMessage not in messageList:
                if item == "eights":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: eights")
                    IntentList.append("divide")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)


        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []






# custom action call in response to cigar intent to response coherently depending on the listen or respond key
# also add cigar intent in the IntentList
class actionRespondCigar(Action):
    def name(self) -> Text:
        return "custom_cigar_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Its a cigar. Okay next one- How did Alfred Nobel make his money? Yes, the guy whose face is on the Nobel prize coin! To submit your final answer type ‘final answer is…….’"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "final answer":
            if botMessage not in messageList:
                if item == "divide":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: divide")
                    IntentList.append("cigar")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)



        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []





# custom action call in response to nobel intent to response coherently depending on the listen or respond key
# also add nobel intent in the IntentList
class actionRespondNobel(Action):
    def name(self) -> Text:
        return "custom_nobel_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "He invented Dynamite. He literally blew things to riches. Lets do one more, which river in Europe has the shortest name? To submit your final answer type ‘final answer is…….’"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "final answer":
            if botMessage not in messageList:
                if item == "cigar":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: cigar")
                    IntentList.append("nobel")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)


      

        else:
            dispatcher.utter_message(text="silent_response")
        print(IntentList)
        print(messageList)

        return []



# custom action call in response to river intent to response coherently depending on the listen or respond key
# also add river intent in the IntentList
class actionRespondRiver(Action):
    def name(self) -> Text:
        return "custom_river_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message["entities"]

        botMessage = "Po. It is actually the longest river in Italy. Well, this is all I am programmed to do. Thank you and hope you enjoyed the GLUE experience. Bye!"

        item = IntentList[-1]

        name = "glue keep quiet"
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()

        if name == "final answer":
            if botMessage not in messageList:
                if item == "nobel":
                    dispatcher.utter_message(text=botMessage)
                    messageList.append(botMessage)
                    print("intent: nobel")
                    IntentList.append("river")
                    print("Step:1")
                    print(IntentList)
                else:
                    myText = botKnowledge.get(item)
                    if myText not in messageList:
                        dispatcher.utter_message(text=myText)
                        messageList.append(myText)
                        intent = get_key(myText)
                        if intent == "intent":
                            IntentList.append("location")
                        else:
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText)
                    intent = get_key(myText)
                    if intent == "intent":
                        IntentList.append("location")
                    else:
                        if intent not in IntentList:
                            IntentList.append(intent)
                            print("Step:2")
                            print(IntentList)


        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)

        return []





# default action is triggered when the nlu fallback intent kicks in
class actionDefaultRespond(Action):
    def name(self) -> Text:
        return "custom_default_response"

    def get_key(self, val):
        for key, value in my_dict.items():
            if val == value:
                return key

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # get all entities from the last message
        entities = tracker.latest_message["entities"]
        item = IntentList[-1]

        intentMessage = "And I am in the cloud. How is the weather in your area?"

        fallBack = "It is always fluffy where I am, haha! May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic"

        # define name as the value of the key
        name = "glue keep quiet"
        # get the value for the key entity from the last message
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()
                print("name:")
                print(name)

        # proceed if the value is glue respond or final answer for quiz questions
        if name == "glue respond" or name == "final answer":

            if item == "intent":
                if intentMessage in messageList:
                    dispatcher.utter_message(text=fallBack)
                    IntentList.append("weather")
                    messageList.append(fallBack)
                else:
                    dispatcher.utter_message(text=intentMessage)
                    messageList.append(intentMessage)
                    IntentList.append("location")

            else:
                myText = botKnowledge.get(item)
                if myText not in messageList:
                    dispatcher.utter_message(text=myText)
                    messageList.append(myText) 
                    intent = get_key(myText)
                    if intent not in IntentList:
                        IntentList.append(intent)
                        print("Step:2")
                        print(IntentList)

        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)

        return []






# pass action to Alana if abuse is detected at a high confidence
class actionRespondProfanity(Action):
    def name(self) -> Text:
        return "custom_profanity_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        abuselist = []
        confidence = 0.0

        item = IntentList[-1]
        botMessage = ""
        intentMessage = "And I am in the cloud. How is the weather in your area?"
        fallBack = "It is always fluffy where I am, haha! May I ask, what is your favourite colour and why? Can you give any deep reasons? For example, I like golden colour because it feels like magic"

        # track all events associated with the previous message
        for event in (list(reversed(tracker.events)))[:5]:
            # ensure that the events are from user and not bot
            if event.get("event") == "user":
                # get the list of entity dictonary from the events tracked
                entities = event["parse_data"]["entities"]
                print(entities)

        # define name as the value of the key
        name = "glue keep quiet"
        # get the value for the key entity from the last message
        for e in entities:
            if e["entity"] == "key":
                name = e["value"]
                name = name.lower()
                print("name:")
                print(name)

        # filter the entities list for dictonary related to entity location
        abuselist = list(
            filter(lambda entities: entities["entity"] == "profanity", entities)
        )

        if len(abuselist) != 0:
            confidence = abuselist[0]["confidence_entity"]

        if name == "glue respond":
            if len(abuselist) != 0:
                if confidence > 0.999:
                    print("I will not tolerate this")
                    pass
                else:
                    if item == "intent":
                        if intentMessage in messageList:
                            dispatcher.utter_message(text=fallBack)
                            IntentList.append("weather")
                            messageList.append(fallBack)
                        else:
                            dispatcher.utter_message(text=intentMessage)
                            messageList.append(intentMessage)
                            IntentList.append("location")

                    else:
                        myText = botKnowledge.get(item)
                        if myText not in messageList:
                            dispatcher.utter_message(text=myText)
                            messageList.append(myText) 
                            intent = get_key(myText)
                            if intent not in IntentList:
                                IntentList.append(intent)
                                print("Step:2")
                                print(IntentList)
        else:
            dispatcher.utter_message(text="silent_response")

        print(IntentList)
        print(messageList)
        return []





# to update intent especially in the custom default response
def updateIntents(intent, itemID):
    
    item = IntentList[-1]

    if len(IntentList) != 0:
        if intent in IntentList:
            IntentList.remove(intent)
            IntentList.append(intent)
        if item == itemID:
            IntentList.append(intent)

    return IntentList





def get_key(val):
    for key, value in botScript.items():
        if val == value:
            return key











