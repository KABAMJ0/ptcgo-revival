from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="705fa3f6-c297-5eea-9553-c01ff67ee41c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanineex.Name",
    display_name="Arcanine ex",
    searchable_by=["Arcanine ex", "Stage 1", "Tera", "ex", "Arcanineex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=32,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Raging Claws",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=30),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=250,
            effect=unimplemented,
        ),
    ],
)