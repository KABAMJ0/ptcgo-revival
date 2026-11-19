from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.attributes import AttrID

async def gulf_stream(ctx):
    """Printed 20, +20 per damage counter on this Pokemon while exactly 6 Prize
    cards remain."""
    pile = ctx.board.find_player_area(ctx.player_id, "prizePile")
    remaining = len(pile.children) if pile else None
    max_hp = ctx.max_hp(ctx.attacker)
    counters = max(0, (max_hp - (ctx.attacker.get_attribute(AttrID.HP) or max_hp)) // 10)
    bonus = 20 * counters if remaining == 6 else 0
    await ctx.deal_damage(20 + bonus)


card = PokemonCardDef(
    guid="5ebafa68-179c-5118-ae4c-5638a0f0df14",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozma.Name",
    display_name="Dawn Wings Necrozma",
    searchable_by=["Dawn Wings Necrozma", "Basic", "Ultra Beast", "DawnWingsNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=106,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=800,
    abilities=[
        Attack(
            title="Gulf Stream",
            game_text="If you have exactly 6 Prize cards remaining, this attack does 20 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=gulf_stream,
        ),
        Attack(
            title="Sword of Dawn",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)