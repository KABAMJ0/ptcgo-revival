from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="9840d09c-8677-571c-a3ef-8f2ab96d99f9",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Single Strike", "Banette"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=7,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=354,
    abilities=[
        Attack(
            title="Resolute Spite",
            game_text="Put up to 7 damage counters on this Pok\u00e9mon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Eerie Light",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)