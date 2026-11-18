from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1abf6aaa-7f60-5fce-a80a-850685ba19f2",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=174,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Freezing Shroud",
            game_text="During Pok\u00e9mon Checkup, put 1 damage counter on each Pok\u00e9mon that has an Ability (both yours and your opponent's), except any Froslass.",
            effect=unimplemented,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)