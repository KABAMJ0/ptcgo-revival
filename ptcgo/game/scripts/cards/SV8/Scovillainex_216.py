from ptcgo.game.card_effects.attacks_common import damage_counters_on
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d55c858a-b2b0-5ba0-a664-762a8470a8e8",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillainex.Name",
    display_name="Scovillain ex",
    searchable_by=["Scovillain ex", "Stage 1", "ex", "Scovillainex"],
    subtypes=["Stage 1", "ex"],
    collector_number=216,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pok\u00e9mon is in play, it is Grass and Fire type.",
            effect=damage_per(damage_counters_on("self"), 70),
        ),
        Attack(
            title="Spicy Rage",
            game_text="This attack does 70 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)