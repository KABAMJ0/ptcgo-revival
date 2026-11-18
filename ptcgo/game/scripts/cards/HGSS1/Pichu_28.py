from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c542bb58-5a9b-52c7-937b-9f1125a5af01",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=172,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Pichu is Asleep, prevent all damage done to Pichu by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Playground",
            game_text="Each player may search his or her deck for as many Basic Pok\u00e9mon as he or she likes, put them onto his or her Bench, and shuffle his or her deck afterward. (You put your Pok\u00e9mon on the Bench first.) Pichu is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)