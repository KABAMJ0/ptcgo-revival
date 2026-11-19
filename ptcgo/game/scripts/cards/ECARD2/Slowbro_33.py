from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _basic_not_baby(attacker, *_rest):
    if attacker is None:
        return False
    if attacker.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
        return False
    return "Baby" not in (subtypes_for(attacker.archetype_id) or [])


async def _energy_cannon(ctx):
    attacker = ctx.attacker
    if attacker is None:
        return
    spare = max(0, len(ctx.attached_energies(attacker)) - 2)
    await ctx.deal_damage(30 + 10 * min(2, spare))


card = PokemonCardDef(
    guid="4a25dcee-27f1-5865-98a7-6ca10ed17dcd",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Dense Body",
            game_text="Any damage done to Slowbro by attacks from Basic Pok\u00e9mon (excluding Baby Pok\u00e9mon) is reduced by 20.",
            passive=takes_less_passive(20, attacker_pred=_basic_not_baby),
        ),
        Attack(
            title="Energy Cannon",
            game_text="This attack does 30 damage plus 10 damage for each Energy attached to Slowbro but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_energy_cannon,
        ),
    ],
)