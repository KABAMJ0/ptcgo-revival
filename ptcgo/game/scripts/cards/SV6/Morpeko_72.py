from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="36472253-5aa8-5eb8-bc82-1608df360f38",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Ability(
            title="Snack Seek",
            game_text="Once during your turn, you may look at the top card of your deck. You may discard that card.",
            effect=unimplemented,
        ),
        Attack(
            title="Pick and Stick",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
    ],
)