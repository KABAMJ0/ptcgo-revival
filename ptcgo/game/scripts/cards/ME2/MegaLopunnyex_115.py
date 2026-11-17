from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="948bf016-09ca-52c7-b8c4-4e7b2efd99a1",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLopunnyex.Name",
    display_name="Mega Lopunny ex",
    searchable_by=["Mega Lopunny ex", "Stage 1", "MEGA", "ex", "MegaLopunnyex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=115,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 170 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Spiky Hopper",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)