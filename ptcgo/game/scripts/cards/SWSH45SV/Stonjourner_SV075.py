from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_energy

def _has_extra_energy(ctx) -> bool:
    total_cost = sum(ctx.ability.cost.values())
    return _ENERGY_ON_SELF(ctx) > total_cost


_ENERGY_ON_SELF = count_energy("self")

card = PokemonCardDef(
    guid="12554ae2-6a10-5f11-96c6-15d20d7d9535",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic", "Stonjourner"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Power Press",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached (in addition to this attack's cost), this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_has_extra_energy, 60),
        ),
    ],
)