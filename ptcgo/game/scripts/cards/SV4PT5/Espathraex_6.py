from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8aa967d3-3460-5088-b339-70a77ac2079f",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathraex.Name",
    display_name="Espathra ex",
    searchable_by=["Espathra ex", "Stage 1", "Tera", "ex", "Espathraex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=6,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Ability(
            title="Dazzling Gaze",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, attacks used by your opponent's Active Pok\u00e9mon cost Colorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Psy Ball",
            game_text="This attack does 30 more damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(lambda c: count_energy("self")(c) + count_energy("defender")(c), 30, base=30),
        ),
    ],
)