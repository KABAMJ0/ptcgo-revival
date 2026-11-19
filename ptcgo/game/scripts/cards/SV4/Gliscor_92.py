from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="8cd46c97-0ef5-5487-9a52-d2d774f91e82",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Toxic Sting",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 2 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=condition_attack(SpecialConditions.POISONED, flip=True, counters=2),
        ),
    ],
)