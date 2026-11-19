from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _defender_has_special_energy(ctx) -> bool:
    defender = ctx.defender
    if defender is None:
        return False
    return any(is_special_energy(energy)
               for energy in ctx.attached_energies(defender))

card = PokemonCardDef(
    guid="cf1730da-e9b6-5462-89e0-5d32300f3a49",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Special Blow",
            game_text="If the Defending Pok\u00e9mon has any Special Energy cards attached to it, this attack does 30 damage plus 50 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_defender_has_special_energy, 50, base=30),
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 40 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(90)),
        ),
    ],
)