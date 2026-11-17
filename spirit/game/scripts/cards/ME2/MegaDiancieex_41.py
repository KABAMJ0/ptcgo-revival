from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e48063b5-0eeb-57cb-8597-69f210345b7b",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDiancieex.Name",
    display_name="Mega Diancie ex",
    searchable_by=["Mega Diancie ex", "Basic", "MEGA", "ex", "MegaDiancieex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=41,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=719,
    abilities=[
        Ability(
            title="Diamond Coat",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Garland Ray",
            game_text="Discard up to 2 Energy cards from this Pok\u00e9mon, and this attack does 120 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)