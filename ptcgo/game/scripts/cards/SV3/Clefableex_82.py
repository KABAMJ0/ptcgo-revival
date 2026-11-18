from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5ef30d2-693b-51e7-a508-51a9022faad1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefableex.Name",
    display_name="Clefable ex",
    searchable_by=["Clefable ex", "Stage 1", "ex", "Clefableex"],
    subtypes=["Stage 1", "ex"],
    collector_number=82,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Lunar Zone",
            game_text="All of your Pok\u00e9mon that have Psychic Energy attached have no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Wondrous Moon",
            game_text="You may move any amount of Psychic Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=170,
            effect=unimplemented,
        ),
    ],
)