from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.passives_common import no_energy_free_retreat_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _was_on_bench_this_turn(ctx) -> bool:
    return ctx.attacker is not None and ctx.entered_active_this_turn(ctx.attacker)

card = PokemonCardDef(
    guid="5aee8201-302c-50e1-bd14-c429399d2464",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=276,
    abilities=[
        Ability(
            title="Big Wing",
            game_text="If Swellow has no Energy attached to it, Swellow's Retreat Cost is 0.",
            passive=no_energy_free_retreat_passive(),
        ),
        Attack(
            title="Mach Descent",
            game_text="If Swellow was on your Bench this turn, this attack's base damage is 60 instead of 30.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bonus_if(_was_on_bench_this_turn, 30, base=30),
        ),
    ],
)