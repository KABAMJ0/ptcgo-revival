from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="74e2cbfc-97f7-56a6-b0b4-fc4d79b0ade8",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparceex.Name",
    display_name="Dudunsparce ex",
    searchable_by=["Dudunsparce ex", "Stage 1", "ex", "Dudunsparceex"],
    subtypes=["Stage 1", "ex"],
    collector_number=121,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    family_id=206,
    abilities=[
        Attack(
            title="Tenacious Tail",
            game_text="This attack does 60 damage for each of your opponent's Pok\u00e9mon ex in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Destructive Drill",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)