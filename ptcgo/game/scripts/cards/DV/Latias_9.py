from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _latios_on_bench(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Latios"
               for p in ctx.my_bench())


async def sky_heal(ctx):
    await ctx.deal_damage()
    if _latios_on_bench(ctx):
        await ctx.heal(20, ctx.attacker)


card = PokemonCardDef(
    guid="ce7ef366-c12c-5bc2-8196-d2e792004a98",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=380,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(is_basic_energy_card, count=1, target="choice"),
        ),
        Attack(
            title="Sky Heal",
            game_text="If Latios is on your Bench, heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=sky_heal,
        ),
    ],
)
