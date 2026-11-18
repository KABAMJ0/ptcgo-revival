from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5262c48a-d8d0-52cf-a3d8-665211dc0b53",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaManectricex.Name",
    display_name="Mega Manectric ex",
    searchable_by=["Mega Manectric ex", "Stage 1", "MEGA", "ex", "MegaManectricex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=50,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Flash Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Riotous Blasting",
            game_text="You may discard all Energy from this Pok\u00e9mon and have this attack do 130 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)