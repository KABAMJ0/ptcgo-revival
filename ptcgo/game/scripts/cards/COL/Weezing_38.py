from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="015b55c6-6e98-5804-9770-f07764b62cdc",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="COL",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Super Poison Breath",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Super Explosion",
            game_text="Weezing does 90 damage to itself, and don't apply Weakness to this damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)