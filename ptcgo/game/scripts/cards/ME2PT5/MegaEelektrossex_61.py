from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70ddf21e-0504-59e6-b683-06b5db02f673",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEelektrossex.Name",
    display_name="Mega Eelektross ex",
    searchable_by=["Mega Eelektross ex", "Stage 2", "MEGA", "ex", "MegaEelektrossex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=61,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Split Bomb",
            game_text="This attack does 60 damage to each of 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Disaster Shock",
            game_text="You may discard 2 Lightning Energy from this Pok\u00e9mon and make your opponent's Active Pok\u00e9mon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=190,
            effect=unimplemented,
        ),
    ],
)