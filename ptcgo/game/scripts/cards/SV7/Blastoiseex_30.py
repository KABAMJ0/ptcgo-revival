from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61e76822-9bd7-57b8-90c9-c8e103ef38e8",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoiseex.Name",
    display_name="Blastoise ex",
    searchable_by=["Blastoise ex", "Stage 2", "ex", "Blastoiseex"],
    subtypes=["Stage 2", "ex"],
    collector_number=30,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=9,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Twin Cannons",
            game_text="Discard up to 2 Basic Water Energy cards from your hand. This attack does 140 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=140,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)