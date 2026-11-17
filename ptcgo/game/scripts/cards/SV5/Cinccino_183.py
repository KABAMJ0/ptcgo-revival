from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e369a489-2124-5bbd-a482-0fc4e79b2a3c",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=183,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Special Roll",
            game_text="This attack does 70 damage for each Special Energy card attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)