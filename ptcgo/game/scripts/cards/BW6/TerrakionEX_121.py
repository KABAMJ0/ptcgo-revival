from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.support_common import distribute_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def _pump_up_smash(ctx):
    """Printed damage, then attach up to 2 basic Energy from hand to your
    Benched Pokemon, one holder per card."""
    await ctx.deal_damage()
    hand = [card for card in ctx.hand() if is_basic_energy_card(card)]
    bench = ctx.my_bench()
    if not hand or not bench:
        return
    picks = await ctx.choose_cards(
        hand, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach to your Benched Pok\u00e9mon")
    if picks:
        await distribute_energy(ctx, picks, bench)


card = PokemonCardDef(
    guid="5f3cfa72-2b29-5d75-8721-bcf26f454db2",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TerrakionEX.Name",
    display_name="Terrakion-EX",
    searchable_by=["Terrakion-EX", "Basic", "EX", "TerrakionEX"],
    subtypes=["Basic", "EX"],
    collector_number=121,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
        Attack(
            title="Pump-up Smash",
            game_text="Attach 2 basic Energy cards from your hand to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=_pump_up_smash,
        ),
    ],
)