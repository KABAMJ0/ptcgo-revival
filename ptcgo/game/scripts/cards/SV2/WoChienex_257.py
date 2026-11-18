from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f802e50-2192-52fc-9eb5-918ff19391d8",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WoChienex.Name",
    display_name="Wo-Chien ex",
    searchable_by=["Wo-Chien ex", "Basic", "ex", "WoChienex"],
    subtypes=["Basic", "ex"],
    collector_number=257,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=1001,
    abilities=[
        Attack(
            title="Covetous Ivy",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pok\u00e9mon for each Prize card your opponent has taken.\u00a0(Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Forest Blast",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
        ),
    ],
)