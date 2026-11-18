from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4292127a-f02c-5268-837b-8813853d04b2",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Fusion Strike", "Latias"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=20,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Ability(
            title="Red Assist",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Latios.",
            effect=unimplemented,
        ),
        Attack(
            title="Dyna Barrier",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon VMAX.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)