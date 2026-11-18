from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="21270245-4c40-5358-a24e-35f580a0624a",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeex.Name",
    display_name="Mr. Mime ex",
    searchable_by=["Mr. Mime ex", "Basic", "ex", "MrMimeex"],
    subtypes=["Basic", "ex"],
    collector_number=111,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Evens",
            game_text="If Mr. Mime ex would be damaged by an attack, prevent that attack's damage done to Mr. Mime ex if that damage is 20, 40, 60, 80, 100, 120, 140, 160, or 180.",
            effect=unimplemented,
        ),
        Attack(
            title="Breakdown",
            game_text="Count the number of cards in your opponent's hand. Put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)