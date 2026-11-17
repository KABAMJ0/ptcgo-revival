from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b859a80-2718-5717-9401-11e83d4f72ea",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Ability(
            title="In a Hungry Hurry",
            game_text="If this Pok\u00e9mon has no Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Energizer Wheel",
            game_text="Move 2 Darkness Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)