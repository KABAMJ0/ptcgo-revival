from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9ba3027-c0f5-5b61-9b77-002a916a8c84",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    display_name="Surskit",
    searchable_by=["Surskit", "Basic", "Surskit"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=283,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Surskit during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)