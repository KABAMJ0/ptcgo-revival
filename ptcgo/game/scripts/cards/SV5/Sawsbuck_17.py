from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92b7160e-3e38-586c-b819-f7b1d08a3ec4",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1", "Sawsbuck"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Ability(
            title="Changing Seasons",
            game_text="Once during your turn, you may search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Superpowered Horns",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)