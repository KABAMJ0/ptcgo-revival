from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.pokemon import is_energy_card, energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import distribute_energy


async def blossom_tail(ctx):
    """Attach up to 2 basic Energy cards from your discard pile to your
    Benched Pokemon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach to your Benched Pokémon",
    )
    if picks:
        await distribute_energy(ctx, picks, bench)

card = PokemonCardDef(
    guid="b2fbebe7-48c7-534d-9701-7e2fec8dfa86",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnamorusV.Name",
    display_name="Enamorus V",
    searchable_by=["Enamorus V", "Basic", "V", "EnamorusV"],
    subtypes=["Basic", "V"],
    collector_number=18,
    set_code="SWSH11TG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=905,
    abilities=[
        Ability(
            title="Guardian of Love",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's Abilities done to each of your Pok\u00e9mon that has any Psychic Energy attached, except any Enamorus V.",
            effect=unimplemented,
        ),
        Attack(
            title="Blossom Tail",
            game_text="Attach up to 2 basic Energy cards from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=blossom_tail,
        ),
    ],
)