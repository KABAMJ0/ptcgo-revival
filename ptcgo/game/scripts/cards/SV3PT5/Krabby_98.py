from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c5e5b21-6909-5a79-a52c-c67aa80de2cf",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    display_name="Krabby",
    searchable_by=["Krabby", "Basic", "Krabby"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=98,
    abilities=[
        Attack(
            title="Salt Water",
            game_text="Flip a coin. If heads, search your deck for up to 2 Basic Water Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 3},
            damage=50,
        ),
    ],
)