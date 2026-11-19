from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c944b6a4-7fea-5a0a-a7ee-8fc3a6e792f2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozoex.Name",
    display_name="Dondozo ex",
    searchable_by=["Dondozo ex", "Basic", "ex", "Dondozoex"],
    subtypes=["Basic", "ex"],
    collector_number=66,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=977,
    abilities=[
        Attack(
            title="Avenging Billow",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=30),
        ),
        Attack(
            title="Dynamic Dive",
            game_text="You may do 120 more damage. If you do, this Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)